# Hostile review: td12 U1 sibling exact charge and twin depth-16 gates

Work only in `/Users/dc/code/math/jc2`. Review, do not extend, the Sol 5.6
producer:

`xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md`

- full SHA-256
  `52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69`;
- body SHA-256
  `306d69f61eb4b9345bcc2bb09dde41411c8762be5203be905eecb108415bba02`.

Reconstruct independently from the reviewed first-trunk primary/review,
corrected Statement 9.3, Corollary 7.1, and the exact flag/place/series
dictionary. Required attack points:

1. Recompute every sibling field and verify that there are exactly two
   distinct nonzero NE direction-orbits, each reduced multiplicity one.
2. Check that each actual direction supplies a cv flag and that the two
   flags may be inserted simultaneously in the shared budget eight. Do not
   assume an MFE-selected subset exhausts places or series.
3. Try all conjugate-shedding, distinct-place split, shared-endpoint, and
   different-`q` branches. Decide whether saturation really forces one
   `q=1` flag of exact weight four per direction and `tau_0=17`.
4. Verify or refute the claimed two depth-16 pure-power gates, endpoint
   qualification, `i=6n`, and gcd degree `6n-1`.
5. Check execution order: whether reduced T1 at `(17,68,52)` must precede
   source extraction, and whether anything already known kills or solves it.
6. Audit scope: no realization, landing, full-book, degree-ceiling,
   `G2-PSC`, `G2-BD`, or JC2 overread.

Give `PASS`, `PASS_WITH_REPAIR`, `GAP`, or `REFUTED`, with the maximum safe
statement and cheapest next discriminator. Include at least one explicit
counterexample attempt and one negative control. Write only

`xmodel/m2-td12-u1-sibling-exact-charge-r1-hostile-review-fable5-20260829.md`

and seal it. Do not edit the target or canonical files, commit, push, browse,
use AWS/heavy compute, or enter, enumerate, search, read, build, status,
modify, or control `jc2-lean`.
