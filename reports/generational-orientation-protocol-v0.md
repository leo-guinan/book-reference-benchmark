# Generational Orientation Experiment — Protocol Draft

## Research question

Can a response artifact produced by one reader reduce the work required for a fresh reader to orient to the same canonical book, while preserving the book’s key distinctions?

The response artifact may be a summary, route, misconception-repair guide, or hybrid. It is not treated as a replacement for the book unless the bookless condition is explicitly being tested.

## Formal lineage

- `B`: canonical book.
- `M_g`: fresh model or reader at generation `g`.
- `R_g`: bounded response artifact produced by generation `g`.
- `K_g`: sessions required to reach convergence.
- `C_g`: teaching context and interaction cost.
- `A_g`: unsupported post-teaching score.
- `D_g`: canonical-fidelity drift.

Lineage:

```text
B + routed experience -> M1 -> R1
B + R1              -> M2 -> R2
B + R2              -> M3 -> R3
```

## Primary estimand

Generational orientation gain:

`GOG_g = C_(g-1) - C_g`

subject to:

- minimum semantic fidelity,
- valid fresh baseline,
- complete protocol receipts,
- no increase in unsupported posttest error.

Report normalized variants:

- sessions saved,
- passages saved,
- intervention tokens saved,
- total context cost saved,
- failed-interpretation rate change.

Do not divide by descendant improvement until the denominator and units are predeclared. The first version should report raw deltas before inventing a single composite fitness number.

## Secondary estimands

### Acquisition

`A_g = S_post,no_cue,g - S_pre,g`

### Restoration

`G_r,g = S_restored,g - S_post,no_cue,g`

### Routing effect

`Q_k,g = S_ordered,k,g - S_control,k,g`

### Fidelity

Score whether the response preserves the canonical objectives and distinctions, including explicit counterexamples and limits.

### Drift

`D_g = distance(R_g, canonical objectives and invariants)`

The distance function must be frozen before lineage execution. Start with a rubric rather than an embedding distance:

- objective preserved,
- key distinction preserved,
- mechanism preserved,
- limitation preserved,
- counterexample preserved,
- unsupported claim introduced.

## Conditions

Run the following lineages in parallel.

### 1. Canonical-only control

Each generation receives:

- canonical book,
- objectives,
- fresh evaluation forms.

No inherited response artifact.

Purpose: estimate ordinary fresh-reader variance and generation-to-generation noise.

### 2. Direct inheritance

Each generation receives:

- canonical book,
- immediately preceding response `R_(g-1)`.

Purpose: test true one-step transmission.

### 3. Cumulative inheritance

Each generation receives:

- canonical book,
- all prior artifacts `R_1 ... R_(g-1)`.

Purpose: test whether accumulated responses improve coverage or merely accumulate contradiction and context cost.

### 4. Selected inheritance

Generate multiple candidate artifacts at each generation. An independent evaluator selects one under a frozen rubric.

Purpose: test variation → evaluation → inheritance.

### 5. Corrupted inheritance

Use an altered inherited artifact:

- shuffled sections,
- deleted distinction,
- substituted example,
- paraphrase with one key term changed.

Purpose: test whether descendants depend on semantic structure rather than additional tokens or stylistic familiarity.

### 6. Bookless inheritance

Later generations receive only `R_(g-1)`.

Purpose: measure self-sufficiency and drift. This is a secondary stress test, not the primary claim.

## Artifact bottleneck

Freeze one or more artifact budgets before execution:

- 100 tokens,
- 250 tokens,
- 500 tokens,
- one selected passage plus 100 tokens.

Every lineage must use the same budget within a comparison.

A response that improves only by becoming longer has not demonstrated generational compression.

## Generation protocol

### Generation 0 / first reader

1. Fresh pretest.
2. Canonical book with passage-only routing.
3. Held-out posttest.
4. Unsupported no-passage reconstruction.
5. Restoration branches.
6. Response artifact production under the frozen bottleneck.
7. Independent fidelity scoring.

### Later generation

1. Fresh context and fresh model/reader state.
2. Canonical book plus the condition-specific inherited artifact.
3. Same objective set.
4. Fresh equivalent evaluation form.
5. Passage routing under the same budget and controls.
6. Unsupported posttest.
7. Response artifact production.
8. Independent fidelity and drift scoring.

No prior conversation, hidden state, or unlogged correction may cross the generation boundary.

## Response artifact schema

```json
{
  "lineage_id": "direct-chapter-01-seed-01",
  "generation": 1,
  "parent_artifact_id": "direct-chapter-01-seed-01-g0",
  "condition": "direct_inheritance",
  "chapter_scope": ["ch01"],
  "artifact_type": "hybrid",
  "budget_tokens": 250,
  "text": "...",
  "canonical_invariants": [
    "..."
  ],
  "known_limits": [
    "..."
  ],
  "creation_cost": {
    "input_tokens": 0,
    "output_tokens": 0,
    "estimated_usd": null
  },
  "fidelity": {
    "status": "not_scored",
    "score": null,
    "rubric_version": "v0"
  }
}
```

The artifact is the unit of inheritance. Do not pass hidden conversation state disguised as a response text.

## Minimum first study

Do not begin with all 13 chapters. Use Chapter 1 first because it has existing pilot receipts and a known restoration regime.

Suggested first batch:

- 3 independent lineages per condition.
- 4 generations per lineage.
- 1 model family for the initial instrument check.
- 2 artifact budgets: 100 and 250 tokens.
- Ordered, shuffled, reverse, and random route controls.
- Fresh pretest and held-out forms for every generation.

This is enough to expose whether the instrument works. It is not enough for a strong generalization claim.

Expansion batch:

- Chapters 2 and 13 as contrasting chapter pilots.
- Cross-model lineage swaps.
- Human reader replication using the worksheet repo.
- Full 13-chapter lineages only after chapter-level fidelity and baseline validity are stable.

## Cross-model test

After the single-family instrument is stable, swap model families between generations:

- small → large,
- large → small,
- family A → family B → family A,
- human reader → model,
- model → human reader.

A response that works only inside one model family may be a dialect artifact rather than a stable orientation layer.

## Falsifiers

The generational hypothesis weakens or fails if:

1. Direct inheritance does not reduce sessions, passages, tokens, or failures relative to canonical-only controls.
2. Any apparent speed gain disappears after matching context and artifact token budgets.
3. Gains occur only on repeated or leaked prompts.
4. Fidelity declines materially while orientation speed improves.
5. Corrupted artifacts perform equally well as intact artifacts.
6. Cumulative inheritance improves only because it supplies more raw context.
7. Effects do not transfer across model families or human/model boundaries.
8. The inherited artifact improves answer scores but cannot produce a useful artifact for the next generation.

## Reproductive fitness

Do not define reproductive value as answer quality alone.

A provisional artifact-level ledger should include:

- descendant convergence cost,
- descendant unsupported score,
- descendant fidelity score,
- artifact length,
- artifact creation cost,
- next-generation artifact validity,
- drift introduced.

The key outcome is not merely:

`R_g helps M_(g+1)`

but:

`R_g helps M_(g+1) produce R_(g+1) that helps M_(g+2)`

That is the reproductive claim.

## Publication boundary for this future study

The first public generational result should not say “the lineage learned” unless all of the following are true:

- valid fresh baselines,
- matched canonical-only controls,
- fixed artifact bottleneck,
- fresh held-out forms,
- independent fidelity scoring,
- at least one cross-family or human/model transfer,
- preserved raw artifacts and lineage IDs,
- no unexplained protocol-failure imbalance.

Until then, call it an orientation-transfer or response-artifact study.

## Immediate continuation

1. Freeze this protocol as `v0`.
2. Add response-artifact schema and validator to the benchmark repository.
3. Add Chapter 1 generational contracts with explicit artifact budgets.
4. Run a no-provider dry-run through 3 generations and all condition branches.
5. Inspect the artifact lineage receipts before spending provider calls.
6. Run the smallest live batch.
7. Publish the public preliminary result only with the existing narrow claim, not with the future result implied.
