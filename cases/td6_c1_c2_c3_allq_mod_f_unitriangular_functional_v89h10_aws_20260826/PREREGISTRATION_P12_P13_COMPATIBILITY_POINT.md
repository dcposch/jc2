# TD6 V89H16 exact P12/P13 compatibility-point gate

Date: 2026-08-26

Status: preregistered producer gate; no result is claimed before two
independent AWS runs agree exactly.

Use only the frozen complete P12 and P13 normal forms modulo the original
FIRST module in the exact `F=0`, all-22-q, `D(U*H*B3)` scope.  At the fixed
denominator-safe rational base point

```text
(U,V,C)=(1,3,8),  F=0,  H=5,  B3=81,
```

form the 22 y-independent compatibility equations consisting of P12
coordinates 2 through 7 and P13 coordinates 2 through 17.  Retain all q
columns `q2,...,q14,q16,...,q24` and compute their exact 22-by-22 coefficient
matrix over Q.  Do not choose, normalize, or delete a q coordinate.

If this matrix is nonsingular, solve its exact affine system.  Then evaluate
the remaining P12/P13 coordinates 0 and 1 as four exact affine equations in
all 94 quotient variables, solve them if consistent, and replay every one of
all 36 normal-form coordinates exactly.  Emit the complete q/y witness,
matrix, determinant, ranks, denominator/open check, and perturbation omission
controls.  If either stage is singular or inconsistent, stop with the exact
rank diagnostic and no point claim.

A successful witness proves only that the literal P12+P13 equations modulo
original FIRST have a common rational point at the displayed base point in
this specialized quotient.  It is not a literal total-source point, does not
impose P14 or later CURRENT, and does not prove or disprove TD6 or JC2.
