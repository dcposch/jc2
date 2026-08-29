# TD6 V89H11 literal-P12 triangular-functional gate

Date: 2026-08-26

Status: producer gate; no result claimed before dual AWS replay.

Work in the exact V89H10T scope: impose `F=0` on the registered
`D(U*H*B3)` open, omit q15 only under the reviewed target shear, and retain
all 22 independent untruncated coordinates

```text
q2,...,q14,q16,...,q24.
```

Rebuild literal P12 and all 38 literal FIRST rows.  Reconstruct the frozen
V89H10T common flag and strict-upper full-q matrix, rather than expanding its
finite Neumann inverse.  Since every FIRST row is affine-linear in the jet
parameters, set the nonpivot parameters to zero and solve the remaining
38-by-38 affine system by exact triangular back-substitution in the emitted
flag basis.  Verify the solution by direct substitution in the original
FIRST coefficient matrix.

Evaluate literal specialized P12 at this exact pivot solution.  This is the
empty-parameter coefficient of the unique original-FIRST normal form.  Emit
the complete untruncated q polynomial, support and degree telemetry, pivot
solution, denominator ledger, and exact digests.  Require its pure-q14
E3-coordinate-0 coefficient to equal the promoted V89H7 functional exactly.
Also require that specialization `q2=...=q13=0` has no positive support
other than pure q14, as in V89H7; high q are retained before this explicit
comparison.

All basis, solution and functional denominator factors must lie in the
registered radical generated on `F=0` by `U`, `V`, and `V^2-4U^3`.  A new
factor, a failed original-FIRST replay, any q truncation, or failure of the
V89H7 comparison is fail-closed.

A pass proves only that the empty-parameter quotient functional extends as
an exact polynomial functional over the all-22-q coefficient ring and is
nonzero on literal P12.  It does not compute the full 17-parameter normal
form, prove a unit ideal or source-point exclusion, license q15 as a source
coordinate, supply total-Rees, close TD6, or resolve JC2.
