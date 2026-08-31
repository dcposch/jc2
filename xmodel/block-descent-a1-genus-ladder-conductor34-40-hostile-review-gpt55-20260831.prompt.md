# Hostile review assignment: conductor 30--40 genus-ladder census

Act as an independent hostile mathematical referee. Review exactly the
conductor-30..40 census packet named below (producer: Grok 4.6). Its
headline negative claim matters strategically: conductors 34 and 40 have
full-`S4`-colourable survivors, so the `C=10+6k` complete-exclusion
pattern STOPS at 28 and `Delta_aff = 17, 20` are not excluded. Hostile
attention should run in both directions: a missed row that would break a
claimed exclusion, and a colouring error that would fabricate or destroy a
survivor. Do not promote, edit any charged file, edit canonical ledgers,
or inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-genus-ladder-conductor34-40-s4-census-grok46-20260831.md
charged_input=ops/block_descent_a1_genus_ladder_c34_c40_s4_replay.py
charged_input=xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
charged_input=xmodel/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
charged_input=ops/block_descent_a1_genus_ladder_s4_replay.py
charged_input=ops/block_descent_a1_genus_ladder_next_s4_replay.py

Your charged inputs are frozen read-only copies in `{{LANE_INPUTS}}`. Read
them there. Reproduce these SHA-256 hashes first and stop on mismatch:

```text
76fb397395bf841fe3b2d91478a18467ecf9ceba0245ea39bfbd3657c48bb70f  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor34-40-s4-census-grok46-20260831.md
bfb746d50a5fae31606fda09ec4d78542a89d175417e80d7ee86493ea41fa3d4  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_c34_c40_s4_replay.py
e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_s4_replay.py
e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b  {{LANE_INPUTS}}/block_descent_a1_genus_ladder_next_s4_replay.py
```

Both parent packets were promoted on 2026-08-31 after independent reviews;
consume them as promoted interfaces but still flag any use the census
makes of them beyond their exact charged scope.

Independently test:

1. census completeness and the exact reduced axioms at all six conductors
   30, 32, 34, 36, 38, 40 (152 rows total), including the two one-stage
   desk factorisations at 34 and 40 and the four-term survivor
   `(12,8,14,15)` arithmetic;
2. the signed cabling dictionary on nested satellites, the zero-framing
   correction `q - w*e(beta)`, and the Burau/Alexander controls, hunting
   especially for an error that only bites at winding `w>=3` or depth-3
   cables (the `1512`- and `936`-count rows);
3. the `V4 -> S4 -> S3` counts: spot-recompute by an independent method at
   least the conductor-34 survivor (expected 72), one zero row killed at
   the `S3` quotient, one complement-only row, and one high-count row of
   your choice; verify the report's warning that the winding-two residue
   theorem must NOT be applied to satellite companions;
4. the exact scope of (0.1): row-level exclusions only for zero rows;
   positive counts are compatibility, not existence; no odd conductors;
   no extrapolation past 40;
5. all replay claims: run the frozen replay in normal, `-O`, and `-OO`
   modes (expected stdout SHA-256 `60c044ac2bc4d83f...`) and all four
   mutations, checking each fails at its advertised gate — in particular
   `--mutate-promote-exclusion`, the old-pass/new-fail control for the
   headline claim.

State the weakest exact hypotheses, any correction and blast radius, and
one best next falsification test. Give a per-claim verdict from
`CONFIRMED`, `REFUTED`, `GAP`, with the attack shown.

Computation rules: only the named exact-Python replays and short exact
desk arithmetic. Never run Singular, msolve, any CAS, or any computation
of uncertain duration or memory on this machine.

Write one report and no other file:

```text
xmodel/block-descent-a1-genus-ladder-conductor34-40-hostile-review-gpt55-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section. Keep it under roughly 6,000 words. End its
body with a single standalone `<!-- BODY-END -->` line and write
absolutely nothing after that line. Do not include a `charge_basis`
declaration: this review asserts no new exit price.
