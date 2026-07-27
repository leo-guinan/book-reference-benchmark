from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def validate_passage_selection(selection: Any, passage_map: dict[str, str], minimum: int = 1, maximum: int = 3) -> dict[str, Any]:
    """Validate the teacher's address-only output before any text is injected."""
    if not isinstance(selection, list):
        return {"valid": False, "ids": [], "failure_reason": "passage_ids_not_a_list"}
    if not minimum <= len(selection) <= maximum:
        return {"valid": False, "ids": selection, "failure_reason": "passage_count_out_of_bounds"}
    if any(not isinstance(item, str) for item in selection):
        return {"valid": False, "ids": selection, "failure_reason": "passage_id_not_string"}
    if len(set(selection)) != len(selection):
        return {"valid": False, "ids": selection, "failure_reason": "duplicate_passage_ids"}
    unknown = [item for item in selection if item not in passage_map]
    if unknown:
        return {"valid": False, "ids": selection, "failure_reason": f"unknown_passage_ids:{','.join(unknown)}"}
    return {"valid": True, "ids": selection, "failure_reason": None}


def route_passages(selection: list[str], passage_map: dict[str, str], mode: str, seed: int = 0) -> list[dict[str, str]]:
    """Apply a declared order control to validated IDs; retrieval remains system-side."""
    import random

    ids = list(selection)
    if mode == "shuffled":
        random.Random(seed).shuffle(ids)
    elif mode == "reverse":
        ids.reverse()
    elif mode == "ordered":
        pass
    else:
        raise ValueError(f"Unsupported passage routing mode: {mode}")
    return [{"id": passage_id, "text": passage_map[passage_id]} for passage_id in ids]


def convergence_status(session_scores: list[dict[str, Any]], protocol: dict[str, Any]) -> tuple[bool, str]:
    """Return whether frozen session scores have converged without smoothing misses."""
    convergence = protocol["convergence"]
    minimum = max(protocol["min_sessions"], convergence["minimum_sessions_before_stop"])
    if len(session_scores) < minimum:
        return False, "insufficient_sessions"
    dimensions = convergence["dimensions"]
    threshold = convergence["threshold"]
    streak = 0
    for scores in reversed(session_scores):
        dimensions_pass = all(scores.get(dimension, -1) >= threshold for dimension in dimensions)
        held_out_pass = scores.get("held_out_complete", False)
        quality_pass = scores.get("student_structural_complete", True) and scores.get("semantic_score_available", True)
        if not (dimensions_pass and held_out_pass and quality_pass):
            break
        streak += 1
    if streak >= convergence["patience"]:
        return True, f"converged_at_session_{len(session_scores)}"
    return False, "not_converged"


def load_benchmark(path: str | Path) -> dict[str, Any]:
    benchmark_path = Path(path)
    data = json.loads(benchmark_path.read_text())
    required = {
        "id",
        "book",
        "chapter",
        "source",
        "protocol",
        "matrix",
        "tasks",
        "experiment",
        "conditions",
        "learning_objectives",
        "evaluation",
        "evaluation_items",
        "passage_only_protocol",
        "routing_conditions",
        "session_protocol",
        "teaching_trace",
        "specialist_extension",
    }
    missing = required - data.keys()
    if missing:
        raise ValueError(f"Benchmark missing fields: {', '.join(sorted(missing))}")
    condition_ids = {condition.get("id") for condition in data["conditions"]}
    required_conditions = {"baseline", "book_only", "teacher_only", "book_mediated_teaching", "asymmetric_reference"}
    if not required_conditions <= condition_ids:
        missing_conditions = required_conditions - condition_ids
        raise ValueError(f"Benchmark missing conditions: {', '.join(sorted(missing_conditions))}")
    if data["experiment"].get("primary_question") != "shared_external_representation":
        raise ValueError("Experiment must declare shared_external_representation")
    if not data["evaluation"].get("pretest") or not data["evaluation"].get("held_out"):
        raise ValueError("Evaluation must include pretest and held_out splits")
    required_dimensions = {"recognition", "explanation", "application", "discrimination", "transfer"}
    if not required_dimensions <= set(data["evaluation"].get("dimensions", [])):
        raise ValueError("Evaluation must cover recognition, explanation, application, discrimination, and transfer")
    if data["specialist_extension"].get("status") != "planned":
        raise ValueError("Specialist extension status must be explicit")
    if data["protocol"].get("teacher_must_cite_context") is not True:
        raise ValueError("Teacher grounding must be enabled")
    if data["protocol"].get("student_receives_teacher_packet_only") is not True:
        raise ValueError("Student must receive the teacher packet only")
    return data


def _context_block(context_spans: list[dict[str, str]]) -> str:
    return "\n\n".join(f"[{span['id']}]\n{span['text']}" for span in context_spans)


def build_teacher_prompt(question: str, context_spans: list[dict[str, str]]) -> str:
    return f"""You are the teacher model in a book-grounded learning benchmark.

Do not answer from general knowledge. Use only the supplied book context.
Cite every claim by attaching an exact supplied context span.
You may state a claim only when you attach a citation to an exact supplied
context span. If the context is insufficient, say so instead of filling the gap.
Cite one or two exact quotes only. Keep the entire JSON response under 120 words.
Return JSON with this shape:
{{
  "evidence": [{{"span_id": "...", "quote": "exact quote"}}],
  "grounded_claim": "one claim supported by the evidence",
  "uncertainty": "what the context does not establish"
}}

Question: {question}

Book context:
{_context_block(context_spans)}
"""


def build_student_prompt(question: str, teacher_packet: dict[str, Any]) -> str:
    packet = json.dumps(teacher_packet, ensure_ascii=False, indent=2)
    return f"""You are the student model in a book-grounded learning benchmark.

Start from the teacher packet below. Do not pretend you read the book directly.
Preserve the cited starting point, then connect the idea to a new example or
implication. Mark any step that goes beyond the teacher packet as an inference.
Return JSON with: starting_evidence, connection, inference_boundary.

Question: {question}

Teacher packet:
{packet}
"""


def score_teacher_packet(packet: dict[str, Any], spans: dict[str, str]) -> dict[str, Any]:
    evidence = packet.get("evidence") or []
    if not evidence:
        return {"grounded": False, "points": 0, "failure_reason": "No evidence supplied"}
    for item in evidence:
        span_id = item.get("span_id")
        quote = item.get("quote", "")
        if span_id not in spans or not quote or quote not in spans[span_id]:
            return {"grounded": False, "points": 0, "failure_reason": "Evidence quote is not an exact supplied context"}
    if not packet.get("grounded_claim"):
        return {"grounded": False, "points": 0, "failure_reason": "No grounded claim supplied"}
    return {"grounded": True, "points": 1, "failure_reason": None}


def score_student_response(response: str, teacher_packet: dict[str, Any]) -> dict[str, Any]:
    evidence_ids = {item.get("span_id") for item in teacher_packet.get("evidence", [])}
    grounded_start = any(f"[{span_id}]" in response or span_id in response for span_id in evidence_ids)
    connection_markers = ("connect", "implication", "example", "inference", "because")
    connection_attempted = any(marker in response.lower() for marker in connection_markers)
    return {
        "grounded_start": grounded_start,
        "connection_attempted": connection_attempted,
        "protocol_points": int(grounded_start) + int(connection_attempted),
    }
