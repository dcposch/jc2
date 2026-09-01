# Research lane: DOMRINA-GAP-REPAIR — repair or refute the two named first-half gaps

The charged REPLAY-1 of Domrina II (official PDF:
`refs/domrina2000_izv64_four_sheeted_general_case.pdf`, SHA-256
`0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018`,
verify before reading) left exactly two gaps in the first half:

- GAP-CANDIDATE[ROOT-U-LAST-CHAIN] — Corollary 3.8(b), p.10:
  the exact missing implication is stated in the charged
  replay §4.2 (read it there, do not paraphrase from memory).
- GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION] — Lemma 3.15,
  pp.14-15: the replay found that linearity alone does not make
  an open-chain determinant one; §4.2 states the residual.

Task, flagship effort:
(1) For each gap: attempt a complete repair. Admissible routes:
    (a) a desk proof of the missing implication from Domrina's
    own setup; (b) a proof from promoted campaign machinery
    (cite the exact promoted statement — the charged rowkill
    integration lists the arsenal; splice-diagram/determinant
    arguments from the campaign's Eisenbud-Neumann work are
    fair game); (c) a proof from the pinned literature
    (refs/zoladek2008_official.pdf 88d5a354, refs/sigray_full.pdf
    9bf9f032, refs/orevkov1990 7c3ba931 — hash-verify anything
    you open).
(2) If a repair fails: characterize the obstruction. Is the
    implication possibly FALSE? Construct the candidate
    countermodel space (the replay's data model §1 gives the
    state space) and either exhibit a countermodel to the
    IMPLICATION (not to the theorem) or explain why none exists
    within the model.
(3) Verdict per gap: REPAIRED (with the proof, self-contained) /
    UNREPAIRED-LIKELY-TRUE (with what is missing) /
    IMPLICATION-FALSE (with countermodel — in which case
    Domrina's Theorem loses this route and the campaign's
    independent N=4 chain becomes the only live path; state that
    consequence soberly, no triumphalism).
(4) Consequence paragraph for the campaign soundness ledger:
    what each verdict does to DOMRINA-II-SOUNDNESS and to the
    N=4-LITERATURE-CLOSED reception line.

Report: `xmodel/domrina-gap-repair-opus5-20260901.md`.
Seal-at-completion contract; target 25-35KB.
charged_input=xmodel/domrina-ii-replay1-sol56-20260901.md
charged_input=xmodel/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  {{LANE_INPUTS}}/domrina-ii-replay1-sol56-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  {{LANE_INPUTS}}/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```
