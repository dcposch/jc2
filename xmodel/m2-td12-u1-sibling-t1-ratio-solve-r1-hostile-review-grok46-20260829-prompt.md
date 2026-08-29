# Hostile review: td12 U1 sibling T1 ratio solve

Work only in `/Users/dc/code/math/jc2`. Independently review the sealed
Sol 5.6 producer

`xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md`

- full SHA-256
  `9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc`;
- body SHA-256
  `d505e3668a9c2152762e8beb7101e12a52db48c4c1d110ab55fcac2b383892ba`.

Reconstruct from Proposition 8.1(iv), the reviewed BOOK P0 repairs, and the
charged td12 tuple. Required attacks:

1. Derive the literal p/q root shapes and decide whether the printed squared
   arrival factor in q is indeed incompatible with root valuation and degree.
2. Re-derive the Wronskian reduction, checking every factor 17 and 13 and
   every division.
3. Solve the polynomial identity independently and verify/refute
   `B+C=9A/4`, `BC=45A^2/32`, and `B/A=(9±3i)/8`.
4. Check distinctness, nonzero roots, noncollision with A, nonzero RHS,
   degree/gcd data, and all stated P0 side conditions.
5. Audit the gauge quotient: common dilation versus translation, ordered
   versus unordered ratios, and whether any continuous modulus survives.
6. Keep this T1 verdict logically independent of the provisional sibling
   charge report. State the maximum safe downstream interface if it passes.

Give `PASS`, `PASS_WITH_REPAIR`, `GAP`, or `REFUTED`, including at least one
explicit mutation/negative control. Write only

`xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-hostile-review-grok46-20260829.md`

and seal it. Do not edit the target or canonical files, commit, push, browse,
use AWS/heavy compute, or enter, enumerate, search, read, build, status,
modify, or control `jc2-lean`.
