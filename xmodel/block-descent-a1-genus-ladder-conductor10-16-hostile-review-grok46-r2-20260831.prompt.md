# Hostile review assignment: conductor-10/16 genus ladder (fresh review)

Act as an independent hostile mathematical referee. Review exactly the
one-place `S4` obstruction packet named below. Do not promote it, edit any
charged file, edit canonical ledgers, or inspect `jc2-lean`. This is a fresh
review; no prior review of this packet is charged or available to you.

charged_input=xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
charged_input=xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md.artifact.json
charged_input=ops/block_descent_a1_genus_ladder_s4_replay.py
charged_input=xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
charged_input=xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md
charged_input=xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md

Your charged inputs are frozen, read-only copies in `{{LANE_INPUTS}}`. Read
them there, not from the live repository. Before mathematical reading,
reproduce these SHA-256 hashes against the frozen copies:

```text
e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
373aa3b1790084848710291d09b5b4af7840818242833a6faf94f71b44c1b33f  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md.artifact.json
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_s4_replay.py
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa  {{LANE_INPUTS}}/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4  {{LANE_INPUTS}}/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md
070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5  {{LANE_INPUTS}}/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
```

If any hash fails, stop and report the mismatch instead of reviewing.

Independently test:

1. the exact Assi--Garcia-Sanchez reduced delta-sequence axioms and whether
   the recursion is complete, including the conductor-14 published control;
2. the conductor-10 and conductor-16 censuses and their conversion to the
   four claimed iterated knots;
3. the signed cable braid/framing convention, knot closure, and Alexander
   polynomial control;
4. every full-`S4` transposition-coloring count and the reusable
   `C_(2,q)(T(2,n))` iff `3|q,3|n` theorem;
5. the meridian-surjection implication and the exact maximum-safe scope;
6. all normal, `-O`, `-OO`, and mutation replay claims, by running
   `python3 {{LANE_INPUTS}}/block_descent_a1_genus_ladder_s4_replay.py`
   yourself in all three modes.

Actively seek a missing delta sequence, a wrong reducedness inequality, a
wrong cable parameter order, a braid blackboard-framing error, a full-image
filter error, or an embedding-versus-abstract-semigroup overclaim. State the
weakest exact hypotheses, any correction and blast radius, and one best next
falsification test. Give a per-claim verdict from `CONFIRMED`, `REFUTED`,
`GAP`, with the attack shown.

Computation rules: only the named exact-Python replay above and short exact
desk arithmetic. Never run Singular, msolve, any CAS, or any computation of
uncertain duration or memory on this machine; if one seems necessary, record
exactly what is blocked and why instead of running it.

Write one report and no other file:

```text
xmodel/block-descent-a1-genus-ladder-conductor10-16-hostile-review-grok46-r2-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 6,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Do not include a `charge_basis` declaration: this review
asserts no new exit price.
