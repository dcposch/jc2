# Q2/Q1 nonlinear-carry checkpoint V2

Pin and consume V1 at SHA-256
`cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd`.
V1 established only that the first `/27` layer is affine and stopped when the
restricted `/81` layer failed an affine-design assertion.

For each of base0000, base0270, and base0513:

1. recompute the complete `/27` affine system and its RREF parameterization;
2. emit exact rank, kernel, row/column support hashes, and source-variable
   effect cones;
3. find the lexicographically first exact failure of an affine identity for
   the `/81` carry function, recording its input coordinate(s), all mismatching
   rows, and the literal values;
4. test the complete quadratic design and state whether a quadratic polynomial
   over F3 is sufficient, without assuming it is.

This is a diagnostic/compiler gate, not a SAT/UNSAT result at `/81`, not a
complete map modulo 243, and not an all-depth or JC2 claim.  Run on AWS only.
