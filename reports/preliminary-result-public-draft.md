# The Reader’s Summary May Be an Orientation Key

*Preliminary Chapter 1 model pilot in passage-only teaching and re-entry*

A small result changed the question.

We were testing whether a teacher model could guide a student through a book while being prohibited from explaining it. After the initial interaction, the teacher could output only canonical passage IDs. The system validated those IDs, retrieved the exact source text, and showed it to the student without exposing the addresses.

After teaching, the student scored `22/25` on a fresh no-restoration reconstruction. We then branched from the same frozen post-teaching state and tested several re-entry cues:

| Re-entry cue | Score | Difference from no cue |
|---|---:|---:|
| No restoration | `22/25` | — |
| One exact passage | `23/25` | `+1` |
| Passage addresses only | `12/25` | `−10` |
| Short quotation | `19/25` | `−3` |
| Model’s own prior summary | `25/25` | `+3` |
| Full ordered route | `24/25` | `+2` |

This was one Chapter 1 trajectory, not a general effect estimate.

**Important boundary:** the fresh semantic pretest was unavailable, so this experiment cannot estimate acquisition. These scores compare re-entry conditions from a frozen post-teaching state; they do not show how much the student improved relative to its prior capability. The branches used independent calls and equivalent but different evaluation forms, so the experiment also does not establish that cue type caused the score differences.

## What was observed

The six branch scores produce a pattern worth testing:

- The largest cue was not the highest-scoring cue.
- The shortest cue was not automatically the weakest.
- Addresses without their text scored below no restoration.
- An isolated quotation scored below no restoration.
- The model’s own prior summary produced the highest score in this run.

The passage was not necessarily the lesson.

That is an observation about this trajectory, not a conclusion about summaries in general.

## One hypothesis suggested by the result

The measurement does not tell us why the summary branch scored highest. One hypothesis is that the response encoded the book in a representation better matched to that particular model’s prior reconstruction.

A summary may therefore be doing something other than compressing the source. It may encode a path back into the source from the representational position of a particular reader.

The book supplies shared coordinates. The response may preserve how one reader found them.

This is the point where the research becomes generational.

## The next experiment

Can one reader produce a bounded response artifact that helps a fresh reader orient faster without increasing distortion?

```text
book + routed experience -> reader 1 -> response 1
book + response 1       -> reader 2 -> response 2
book + response 2       -> reader 3 -> response 3
```

Each generation would begin in a fresh context. No hidden conversation would cross the boundary. The inherited response would have a fixed size. The canonical book would remain available as a reference.

The primary measurement is not whether a later reader gives a plausible answer. It is whether that reader reaches the same performance threshold with less work:

- fewer sessions,
- fewer passages,
- fewer intervention tokens,
- fewer failed interpretations,
- or less teaching context.

Any speed gain must be checked against fidelity. A response that helps a reader move faster while dropping a key distinction, limitation, or counterexample is not a successful transmission. It is efficient drift.

The proposed generational publishing-house idea is therefore a falsifiable hypothesis, not the result of this pilot:

```text
book -> reader -> response artifact -> fresh reader -> new response artifact
```

The first lineage study will compare book-only controls with direct inheritance from the immediately preceding response. Later studies can test cumulative, selected, corrupted, and bookless inheritance. Response artifacts will be bounded so that longer documents cannot masquerade as better translation.

## What this pilot does not show

It does not establish:

- acquisition beyond fresh prior capability,
- passage-order causality,
- durable retention,
- cross-model transfer,
- a whole-book semantic effect,
- or generalization beyond Chapter 1.

The other twelve chapter contracts now exist, but they have not yet produced provider-backed semantic results. The full manuscript is inventoried and ready for a properly contracted expansion; it has not been given a whole-book score.

The useful result is smaller and stranger:

> In one Chapter 1 model pilot, a teacher restricted to selecting exact book passages produced a restoration pattern in which performance varied with cue form and context, not simply with the amount of text supplied. Whether a reader-generated response can help the next reader orient faster remains open.

The next artifact is not another claim. It is a protocol, a bounded response schema, and a replication invitation.
