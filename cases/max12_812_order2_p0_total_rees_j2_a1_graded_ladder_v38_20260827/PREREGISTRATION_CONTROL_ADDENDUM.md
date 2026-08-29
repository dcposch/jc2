# V38 census addendum: complete low-weight `a1`/`k` shape controls

Date: 2026-08-27

The primary census preregistration remains immutable.  This separately frozen
addendum answers a blind-review concern: the exponent-four and exponent-five
ladders alone do not inventory lower mixed monomials such as `a1*k`,
`a1*k^2`, or `a1^2*k`.

Before freezing the decision runner, enumerate every target

```text
a1^i*k^j  with i >= 1, j >= 0, and 5*i + 4*j <= 25.
```

There are sixteen labeled pairs:

```text
i1_j0 W5    i1_j1 W9    i1_j2 W13   i1_j3 W17   i1_j4 W21   i1_j5 W25
i2_j0 W10   i2_j1 W14   i2_j2 W18   i2_j3 W22
i3_j0 W15   i3_j1 W19   i3_j2 W23
i4_j0 W20   i4_j1 W24
i5_j0 W25
```

The source and enumeration semantics are exactly those hash-pinned by the V38
primary census: all frozen homogeneous raw ordered-`a1`, `rho=0` rows through
grade 19; all monomial cofactors of the required weight; no cofactor-degree
cap; faithful omission of variables absent from every row.  This stage emits
only exact censi and has no membership or JC2 implication.  An AWS validator
must independently reconstruct every labeled census before its output can be
pinned by the decision preregistration.
