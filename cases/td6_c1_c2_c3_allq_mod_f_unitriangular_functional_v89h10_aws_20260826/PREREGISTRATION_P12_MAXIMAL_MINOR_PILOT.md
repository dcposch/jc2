# TD6 V89H13 P12 augmented-maximal-minor pilot

Date: 2026-08-26

Status: finite-field diagnostic gate; no characteristic-zero theorem is
claimed before structural lifting and independent review.

Consume only the frozen V89H12 complete P12 normal form on exact `F=0` and
`D(U*H*B3)`.  Its 18 E3 coordinates have the form

```text
R(q,y) = c(q) + A(q)y,
```

where `y` is the exact 16-element surviving quotient-variable list and q is
`q2,...,q14`; the retained q16,...,q24 coefficients vanished in V89H12.
The matrix `A` is homogeneous linear in q, while `c` is affine linear in q.

For two independent good-prime/good-base-point AWS lanes, rebuild the exact
18-by-16 matrix and augmented 18-by-17 matrix directly from the frozen TSV.
Report ranks and all 18 maximal minors at q=0, on every pure q-axis, and at a
fixed set of deterministic dense q samples.  On each pure axis write

```text
Delta_i(t q_e) = t^16 (a_i + t b_i)
```

for every row-deletion minor, validate this scaling at a third t-value, and
decide exactly over the chosen finite field whether the 18 linear residuals
`a_i+t b_i` have a common nonzero t.  This is a decisive modular diagnostic
for each pure axis, not a characteristic-zero exclusion.

The pilot passes only if input custody and the separate-degree structure are
verified and all output is exact finite-field arithmetic.  Any denominator
zero at the chosen `(U,V)` is fail-closed.  Dense-rank samples and pure-axis
tests may guide the next symbolic maximal-minor ideal client, but sampling
alone proves nothing about mixed q or characteristic zero.

No Singular qring is allowed.  This gate does not prove a unit ideal,
source-point exclusion, total-Rees map, TD6, or JC2.
