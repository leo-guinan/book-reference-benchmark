from book_reference_benchmark.response_artifacts import validate_response_artifact


def artifact(**overrides):
    value = {
        "lineage_id": "lineage-g0",
        "generation": 0,
        "condition": "direct_inheritance",
        "artifact_type": "hybrid",
        "budget_tokens": 250,
        "text": "A bounded orientation artifact.",
        "canonical_invariants": ["one distinction"],
        "known_limits": ["one limit"],
        "creation_cost": {"estimated_usd": None},
        "fidelity": {"status": "not_scored", "score": None},
    }
    value.update(overrides)
    return value


def test_valid_generation_zero_artifact():
    assert validate_response_artifact(artifact())["valid"] is True


def test_later_generation_requires_parent():
    result = validate_response_artifact(artifact(generation=1))
    assert result == {"valid": False, "failure_reason": "later_generation_missing_parent"}


def test_generation_zero_cannot_have_parent():
    result = validate_response_artifact(artifact(parent_artifact_id="old"))
    assert result == {"valid": False, "failure_reason": "generation_zero_has_parent"}


def test_invalid_condition_is_protocol_failure():
    result = validate_response_artifact(artifact(condition="prompt_optimization"))
    assert result == {"valid": False, "failure_reason": "unknown_condition"}
