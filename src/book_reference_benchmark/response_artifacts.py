from __future__ import annotations

from typing import Any


REQUIRED_FIELDS = {
    "lineage_id",
    "generation",
    "condition",
    "artifact_type",
    "budget_tokens",
    "text",
    "canonical_invariants",
    "known_limits",
    "creation_cost",
    "fidelity",
}
VALID_CONDITIONS = {
    "canonical_only",
    "direct_inheritance",
    "cumulative_inheritance",
    "selected_inheritance",
    "corrupted_inheritance",
    "bookless_inheritance",
}
VALID_ARTIFACT_TYPES = {"summary", "route", "repair_guide", "hybrid"}


def validate_response_artifact(artifact: Any) -> dict[str, Any]:
    """Validate a bounded generational response artifact without judging its semantics."""
    if not isinstance(artifact, dict):
        return {"valid": False, "failure_reason": "artifact_not_object"}
    missing = sorted(REQUIRED_FIELDS - artifact.keys())
    if missing:
        return {"valid": False, "failure_reason": f"missing_fields:{','.join(missing)}"}
    if not isinstance(artifact["lineage_id"], str) or not artifact["lineage_id"].strip():
        return {"valid": False, "failure_reason": "lineage_id_not_nonempty_string"}
    if not isinstance(artifact["generation"], int) or artifact["generation"] < 0:
        return {"valid": False, "failure_reason": "generation_not_nonnegative_integer"}
    if artifact["condition"] not in VALID_CONDITIONS:
        return {"valid": False, "failure_reason": "unknown_condition"}
    if artifact["artifact_type"] not in VALID_ARTIFACT_TYPES:
        return {"valid": False, "failure_reason": "unknown_artifact_type"}
    if not isinstance(artifact["budget_tokens"], int) or artifact["budget_tokens"] <= 0:
        return {"valid": False, "failure_reason": "budget_tokens_not_positive_integer"}
    if not isinstance(artifact["text"], str) or not artifact["text"].strip():
        return {"valid": False, "failure_reason": "text_not_nonempty_string"}
    if not isinstance(artifact["canonical_invariants"], list):
        return {"valid": False, "failure_reason": "canonical_invariants_not_list"}
    if not isinstance(artifact["known_limits"], list):
        return {"valid": False, "failure_reason": "known_limits_not_list"}
    if not isinstance(artifact["creation_cost"], dict):
        return {"valid": False, "failure_reason": "creation_cost_not_object"}
    if not isinstance(artifact["fidelity"], dict):
        return {"valid": False, "failure_reason": "fidelity_not_object"}
    parent = artifact.get("parent_artifact_id")
    if artifact["generation"] == 0 and parent is not None:
        return {"valid": False, "failure_reason": "generation_zero_has_parent"}
    if artifact["generation"] > 0 and (not isinstance(parent, str) or not parent.strip()):
        return {"valid": False, "failure_reason": "later_generation_missing_parent"}
    return {"valid": True, "failure_reason": None}
