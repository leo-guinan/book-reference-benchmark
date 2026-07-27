import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
BENCHMARK_ROOT = ROOT / "benchmarks/art-of-time-and-war"
DIMS = ["recognition", "explanation", "application", "discrimination", "transfer"]


def test_public_contracts_preserve_evaluation_shape_without_source_text():
    for number in range(1, 14):
        path = BENCHMARK_ROOT / f"chapter-{number:02d}" / "benchmark.json"
        benchmark = json.loads(path.read_text())

        assert benchmark["chapter"]["number"] == number
        assert benchmark["source"]["status"] == "omitted_public_projection"

        evaluation = benchmark["evaluation_items"]
        assert len(evaluation["pretest"]) == 1
        assert len(evaluation["held_out"]) == 5
        assert [item["dimension"] for item in evaluation["held_out"]] == DIMS
        assert len(evaluation["final_check"]) == 5
        assert len(evaluation["session_forms"]) >= 3
        assert all(len(form) == 5 for form in evaluation["session_forms"])
        assert all([item["dimension"] for item in form] == DIMS for form in evaluation["session_forms"])

        schedule = benchmark["session_protocol"]["evaluation_schedule"]
        assert schedule["fresh_form_per_session"] is True
        assert schedule["final_check_passages"] == []
        assert len(schedule["restoration_budgets"]) == 5

        routing = benchmark["passage_only_protocol"]
        assert routing["allowed_controls"] == ["ordered", "shuffled", "reverse", "random"]
        assert routing["same_selection_across_order_controls"] is True
        assert benchmark["session_protocol"]["convergence"]["require_all_dimensions"] is True
        assert benchmark["session_protocol"]["convergence"]["require_held_out_completion"] is True
