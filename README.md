# The Reader’s Summary May Be an Orientation Key

Public research artifacts for a preliminary Chapter 1 model pilot in passage-only teaching and re-entry.

## The result

From the same frozen post-teaching state, the pilot produced these branch scores:

| Re-entry cue | Score | Difference from no cue |
|---|---:|---:|
| No restoration | `22/25` | — |
| One exact passage | `23/25` | `+1` |
| Passage addresses only | `12/25` | `−10` |
| Short quotation | `19/25` | `−3` |
| Model’s own prior summary | `25/25` | `+3` |
| Full ordered route | `24/25` | `+2` |

This is one Chapter 1 trajectory, not a general effect estimate.

The fresh semantic pretest was unavailable. These scores compare re-entry conditions from a frozen post-teaching state; they do not estimate acquisition relative to prior capability. The branches used independent calls and equivalent but different evaluation forms, so they do not establish cue-type causality.

## Read first

- [Preliminary public note](reports/preliminary-result-public-draft.md)
- [Publication plan](reports/preliminary-result-publication-plan.md)
- [Full generational protocol](reports/generational-orientation-protocol-v0.md)

## Repository contents

- `benchmarks/` — thirteen chapter evaluation contracts. Source text is intentionally excluded from this public projection.
- `reports/` — publication note, editorial plan, and proposed generational experiment.
- `schemas/` — response-artifact schema.
- `src/` — benchmark core and response-artifact validator.
- `tests/` — executable contract and validator tests.
- `worksheets/` — human reader worksheets for chapters 1–13 and the final book.
- `schema/` — reader-response schema.
- `scripts/` — worksheet validation script.

## What this repo does not claim

This repository does not claim:

- that the book taught the model;
- acquisition beyond fresh prior capability;
- passage-order causality;
- durable retention;
- cross-model transfer;
- a whole-book semantic effect;
- or a completed generational publishing-house experiment.

The generational publishing-house idea is a proposed falsifiable experiment. The response-artifact schema is an instrument for that experiment, not evidence that generational transfer has occurred.

## Verification

Benchmark tests:

```bash
python -m pytest -q
```

Worksheet validation:

```bash
python scripts/validate.py
```

The source project uses a local virtual environment for the benchmark suite. No provider credentials are required to run the contract and schema tests in this public repository.

## Public-release boundary

This is a curated public projection. It intentionally excludes:

- manuscript source text;
- provider-run raw receipts;
- local paths and credentials;
- virtual environments and generated caches;
- private reader responses or identities.

The preliminary result is reported as an observation with explicit missing evidence. Replication artifacts should preserve null results and protocol failures rather than replacing them with inferred scores.
