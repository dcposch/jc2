# Hostile review assignment: conductor-12..28 genus-ladder census extension

Act as an independent hostile mathematical referee. Review exactly the
one-place `S4` census-extension packet named below, which claims exact
exclusion of conductors 22 and 28 (with survivors at 12, 14, 18, 20), hence
provisionally `Delta_aff notin {5,8,11,14}` in the charged irreducible
one-place quartic-transposition class. Do not promote it, edit any charged
file, edit canonical ledgers, or inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
charged_input=xmodel/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md.artifact.json
charged_input=ops/block_descent_a1_genus_ladder_next_s4_replay.py
charged_input=xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
charged_input=ops/block_descent_a1_genus_ladder_s4_replay.py
charged_input=xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md

Your charged inputs are frozen, read-only copies in `{{LANE_INPUTS}}`. Read
them there, not from the live repository. Before mathematical reading,
reproduce these SHA-256 hashes against the frozen copies:

```text
1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
731636008ad4ae0daa402a3f74b670b921d03776d81bd8fd172af78c3746918b  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md.artifact.json
e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_next_s4_replay.py
e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_s4_replay.py
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa  {{LANE_INPUTS}}/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
```

If any hash fails, stop and report the mismatch instead of reviewing. Note
that the predecessor conductor-10/16 packet is itself provisional and under
separate review: treat its statements as declared inputs, verify every use
the census extension makes of them, and flag any load-bearing dependence
that would not survive a 10/16 correction.

Independently test:

1. delta-sequence census completeness at each conductor 12, 14, 18, 20, 22,
   and 28, under the exact reduced Assi--Garcia-Sanchez axioms, and the
   correctness of every claimed survivor and exclusion;
2. the split `V4 -> S4 -> S3` quotient construction: that the claimed
   quotient and lift are exact, that the `F3` and `F2` linear-algebra
   reductions faithfully encode the transposition-coloring conditions, and
   that no coloring is lost or spuriously killed at the 18-strand rows;
3. the conversion of surviving delta sequences to iterated torus knots,
   including cable parameter order and framing;
4. the exact scope translation from conductor exclusions to
   `Delta_aff notin {5,8,11,14}`, and that no monotone or interpolated
   claim beyond the six computed conductors is smuggled in — adjacent
   survivors must remain survivors in your reading;
5. all normal, `-O`, `-OO`, and mutation replay claims, by running
   `python3 {{LANE_INPUTS}}/block_descent_a1_genus_ladder_next_s4_replay.py`
   yourself in all three modes.

Actively seek a missing delta sequence, a quotient kernel error (a coloring
visible to `S4` but invisible to the split reduction), a field-arithmetic
transcription error, a wrong strand count, or an
embedding-versus-abstract-semigroup overclaim. State the weakest exact
hypotheses, any correction and blast radius, and one best next
falsification test. Give a per-claim verdict from `CONFIRMED`, `REFUTED`,
`GAP`, with the attack shown.

Computation rules: only the named exact-Python replays above and short exact
desk arithmetic. Never run Singular, msolve, any CAS, or any computation of
uncertain duration or memory on this machine; if one seems necessary, record
exactly what is blocked and why instead of running it.

Write one report and no other file:

```text
xmodel/block-descent-a1-genus-ladder-conductor22-28-hostile-review-gpt55-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 6,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Do not include a `charge_basis` declaration: this review
asserts no new exit price.
