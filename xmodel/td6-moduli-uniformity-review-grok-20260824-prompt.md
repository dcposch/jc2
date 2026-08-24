# Hostile different-model review — TD6 MODULI UNIFORMITY

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/td6-moduli-uniformity-gate-20260824.md`
- every file under `cases/td6_moduli_uniformity_20260824/`
- the confirmed TD6 first-band and numerical-next-row producers/reviews
- the cited canonical SP-2/F1/r9 source-typing material

Frozen hashes:

- report: `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06`
- replay: `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab`
- freeze: `8d28ce7bc0ca31b51887457e9f5e33537f0ec86d950a6e0e21c78813a78994af`

Independently rerun the replay and attack exactly:

1. Verify the general F1 pattern
   `R(z)=(z-C)^2(z-U)(z-V)`, definitions of `E1,E2`, the fixed rectangles
   and x-boundary scope, and which centering/pole/dead-stretch moduli are
   genuinely quantified versus specialized.
2. Independently derive all three coefficient extractions in (7) from the
   global monomials and F1 pole line. Prove that every contribution involving
   arbitrary `c1,c2,c3` lies on a forbidden stricter line. Then derive
   `[t^0]g1=-E1/5` from the first row and recompute
   `[s^-1 t^13]J=(6/5)(5E2-2E1^2)`, including recovery of the frozen numerical
   value.
3. Audit the quadratic stratification: expansion (10), negative-definiteness
   over real moduli, normalized complex zero locus, and every source-open
   exclusion. Check that complex orbit values are licensed and produce a
   genuine nonempty open subset rather than a formal zero only.
4. Rebuild or independently audit the exact symbolic transport on the
   normalized survivor. Verify rank `3508/3602`, exhaustive dependent-row
   conditions (17), absence of hidden parameter denominators/rank jumps, the
   Taylor factor `L`, pole patterns, ODE, and normalization `L^8 A^3=9`.
5. Audit all complete next-row claims: 40 x slots, degree-13 as the only
   affine compatibility, homogeneous x rank 36, pole rows (19) adding exactly
   rank two modulo x when `LA!=0`, no extra affine condition, and final
   dimension 56. Seek copied coefficient blocks or a parameter-special rank
   drop that changes the conclusion.
6. Independently verify the explicit algebraic survivor
   `10S^2-35S+37=0`, `D=S-22/25`, `L=3`, `A=1/9`, including
   `U,V` nonzero/distinct/not 1, the obstruction zero, and pole normalization.
   Confirm it proves finite-band nonemptiness only, not a Keller pair.
7. Enforce scope: the formula is uniform in common centering and pole data
   only for the retained normalized x-boundary/F1 pattern. It neither kills
   SP-2 nor quantifies broader boundary patterns, other terminal classes,
   landing, or JC2. Identify the smallest valid next band on the 56-space.

Try hard to find a source-typing, line-extraction, rank, or field-specialization
error. Do not edit producer/canonical files, append the successor band, or
launch AWS.

Write exactly one file:

`xmodel/td6-moduli-uniformity-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent exact checks, parameter/source-typing caveats, scope
exclusions, and promotion advice.
