# Research lane: extend the exact one-place `S4` genus ladder past conductor 28

You are a bounded primary research lane, not a reviewer. Your task is to
extend the exact genus-ladder census to the next conductors in the charged
progression, expected to be 34 and 40 — derive the correct next targets from
the packets' own parametrization before computing, and say so explicitly if
they differ. Do not edit canonical ledgers, any charged file, or inspect
`jc2-lean`.

charged_input=xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
charged_input=xmodel/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
charged_input=ops/block_descent_a1_genus_ladder_s4_replay.py
charged_input=ops/block_descent_a1_genus_ladder_next_s4_replay.py

Your parent inputs are frozen read-only copies in `{{LANE_INPUTS}}`; read
them there. Verify these SHA-256 hashes first and stop on any mismatch:

```text
e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_s4_replay.py
e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_next_s4_replay.py
```

Both parent packets are lifecycle `PROVISIONAL` and under separate
different-model review. Label every dependence on them `PROVISIONAL` in your
report so descendants can be rolled back mechanically.

Task, in order:

1. Reconstruct the reduced Assi--Garcia-Sanchez delta-sequence census at
   each target conductor under the exact axioms of the parent packets, with
   the same reducedness inequalities and completeness argument.
2. Convert survivors to iterated torus knots with the parents' signed cable
   and framing conventions.
3. Run the split `V4 -> S4 -> S3` exact `F3`/`F2` linear-algebra coloring
   test on every surviving knot. Record exact survivor and exclusion sets.
4. Write a deterministic exact-Python replay script
   `ops/block_descent_a1_genus_ladder_c34_c40_s4_replay.py` in the style of
   the parent replays: pure stdlib, byte-stable output, passing under
   normal, `-O`, and `-OO`, with at least one deliberate old-pass/new-fail
   mutation control documented in the report.
5. State the exact `Delta_aff` consequence of any exclusion in the charged
   irreducible one-place quartic-transposition class, and state explicitly
   what remains open. No monotone extrapolation beyond computed conductors.

Stop conditions: if the census at a target conductor exceeds roughly 50,000
delta sequences or your replay would run longer than about five minutes on
one core, freeze the enumeration design instead of running it, and report
the exact object that needs an AWS registration. Never run Singular,
msolve, any CAS, or any uncertain-duration computation on this machine.

Write one report and no other file except the named replay script:

```text
xmodel/block-descent-a1-genus-ladder-conductor34-40-s4-census-grok46-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 6,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Do not include a `charge_basis` declaration: this lane
asserts no new exit price.
