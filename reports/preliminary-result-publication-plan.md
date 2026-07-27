# Preliminary Result Publication Plan

## Working title

**The Reader’s Summary May Be an Orientation Key**

Alternative titles:

- **What Happens When a Book Teaches Through Its Readers?**
- **The Passage Was Not the Lesson**
- **A Book, a Reader, and the Problem of Re-entry**
- **Preliminary Result: Cue Form Changed Reconstruction More Than Cue Size**

## Publication objective

Introduce the public to a narrow, reproducible preliminary result and make the larger research question legible without claiming that the book has already taught a model, improved capability, or demonstrated a whole-book effect.

The public piece should do three things:

1. Show the observed result with exact numbers.
2. Explain why the result is interesting without over-interpreting it.
3. Invite readers into the next experiment: whether response texts from one reader can orient a fresh reader faster, while preserving fidelity to the book.

The Von Neumann publishing-house idea should be introduced as a testable hypothesis, not as an achieved result.

## Public claim

> In one Chapter 1 model pilot, a teacher restricted to selecting exact book passages produced a restoration pattern in which cue form mattered more than cue size. From the same frozen post-teaching state, no restoration scored 22/25, one exact passage scored 23/25, the model’s own prior summary scored 25/25, and the full route scored 24/25, while passage addresses and an isolated quotation scored 12/25 and 19/25. Because this was one trajectory without a valid fresh pretest, the pilot does not establish acquisition, passage-order causality, durability, or generalization across the manuscript.

This is the sentence the evidence can currently carry.

## What not to say

Do not say:

- “The book taught the model.”
- “The model learned from the book.”
- “The full book improved model capability.”
- “The model’s summary is better than the book.”
- “Reading order caused the result.”
- “The publishing house is already reproducing intelligence.”
- “The result generalizes across models or chapters.”

Those are future hypotheses or unmeasured claims. The market already has enough numbers and adjectives that should not exist.

## Proposed public format

### Primary essay

Length: 1,200–1,800 words.

Structure:

1. **Opening observation** — The same prior state produced materially different outcomes depending on the re-entry cue.
2. **The small table** — Show all five Pilot A restoration conditions.
3. **The control case** — Explain the ceiling perturbation pilot and why `25/25` is not evidence of restoration.
4. **The missing baseline** — State plainly that acquisition `A = null` because the fresh pretest was not semantically judgeable.
5. **Why the own-summary branch matters** — A response can be a reader-relative re-entry key rather than a mere compression.
6. **The hypothesis** — A response artifact may help a new reader orient faster than replaying the canonical route.
7. **The next experiment** — Generational lineages, bottlenecks, controls, fidelity, and drift.
8. **Invitation** — Readers can inspect the contracts and complete the worksheets; researchers can challenge the protocol or reproduce it.

### Supporting artifacts

Publish alongside the essay:

- Chapter 1 pilot report.
- Raw pilot JSON receipts, with private/provider-sensitive fields checked.
- Full-book processing report.
- 13 evaluation contracts.
- Reader worksheet repository.
- A short reproducibility README with exact commands and claim boundaries.
- A one-page diagram of canonical book → reader response → fresh reader → new response.

## Visuals

### Figure 1 — Restoration curve

A six-bar chart showing both score and difference from no restoration:

- No restoration: `22/25`
- One exact passage: `23/25`
- Addresses only: `12/25`
- Short quotation: `19/25`
- Own prior summary: `25/25`
- Full ordered route: `24/25`

Label it: **Pilot A, one Chapter 1 trajectory; not a general effect estimate.** Show a zero reference line for the difference column.

### Figure 2 — The boundary diagram

```
canonical book B
       |
       v
teacher selects passages
       |
       v
reader/model reconstruction S'
       |
       v
response artifact R1
       |
       v
fresh reader/model M2
```

Add a red boundary around the unresolved quantities:

- acquisition,
- durability,
- routing causality,
- cross-chapter generalization.

### Figure 3 — The proposed generational loop

```
B + routed experience -> M1 -> R1
B + R1               -> M2 -> R2
B + R2               -> M3 -> R3
```

The caption must say: **proposed experiment, not observed result.**

## Reader invitation

The public call should ask for three kinds of participation:

1. **Critical replication** — Inspect the contracts and identify leakage, ambiguity, or missing controls.
2. **Human worksheet replication** — Read the book, complete chapter worksheets, and record pretest, posttest, uncertainty, transfer, and retention.
3. **Generational orientation test** — Produce a bounded response artifact that another reader can use as supplemental orientation, then measure whether the next reader needs fewer cues while preserving the book’s distinctions.

Do not ask for testimonials. Ask for null results, failed interpretations, and artifacts.

## Publication sequence

### Release 1 — Short introduction

A 500–700 word post containing:

- the claim,
- the restoration table,
- the own-summary observation,
- the missing-baseline disclaimer,
- the link to artifacts.

### Release 2 — Full research note

Publish the 1,200–1,800 word essay with methods, receipts, caveats, and the generational hypothesis.

### Release 3 — Open worksheet and replication call

Publish the reader worksheet repo and invite human beta readers. Keep this separate from the result announcement so recruitment does not look like evidence for the result.

### Release 4 — Generational protocol pre-registration

Publish the protocol before running the lineage experiment. Freeze:

- artifact budgets,
- control lineages,
- model selection,
- held-out forms,
- fidelity rubric,
- drift metric,
- stopping rules,
- failure handling.

## Editorial safeguards

- Put the exact sample size in the first screen of the methods section.
- Keep Pilot A and Pilot B visibly separate.
- Do not average them into one score.
- Mark all unavailable semantic results as unavailable, not zero.
- Separate protocol failures from semantic failures.
- State that the fresh baseline failed in both pilots.
- State that the full-book score does not exist yet.
- Disclose that the author is also designing the book and the benchmark.
- Preserve the raw receipts and the failed branches.

## Publication readiness gate

Publish only when the package contains:

- [ ] Exact public claim approved.
- [ ] Pilot A and Pilot B receipts linked.
- [ ] Fresh-baseline failure stated.
- [ ] No unsupported whole-book claim.
- [ ] Figure captions include sample and scope.
- [ ] Provider/model identifiers and cost receipts checked for public release.
- [ ] Private data and credentials removed.
- [ ] Generational protocol clearly labeled proposed.
- [ ] Reader worksheet link works.
- [ ] Reproduction instructions run from a clean checkout.

## Success condition for the public piece

The piece succeeds if a skeptical reader can answer:

- What actually happened?
- What did not happen?
- Why is the result interesting?
- What experiment would distinguish the interesting hypothesis from ordinary summarization, prompt variance, or model-specific behavior?

If the reader leaves impressed but unable to answer those questions, the piece has become marketing. That is not the experiment.
