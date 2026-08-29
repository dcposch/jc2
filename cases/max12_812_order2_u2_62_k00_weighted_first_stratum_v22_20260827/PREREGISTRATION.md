# Preregistration: V22 first honest weighted K00 stratum

Date: 2026-08-27

Status: **FROZEN BEFORE COMPILER OR ALGEBRA.  V20R2/V21R1 REVIEW
DEPENDENCIES REMAIN PROVISIONAL.**

## Charged finite prefix

Use the corrected contracted V20R1 design and the honest weights.  On a
valuation-one coefficient arc write

```text
d_i=Lambda*x_i+O(Lambda^2),   k10=kappa+O(Lambda),   kappa!=0.
```

The first-six equations at grade two are the six quadratic initials
`Q_i(x)`.  The `k6,k2,mu2,mu4,mu6,Jdet` terms cannot contribute to the first
canonical contracted obstruction.  V18's exact K10 lift through normal
degree three and first failure at degree four imply that the first weighted
contracted obstruction occurs at `Lambda^6` and has the form

```text
kappa*F10(x)=0,
```

for a homogeneous quartic representative `F10` obtained by subtracting the
complete frozen D3 lift from `D_K10` and taking degree four.

V22 must independently reconstruct and serialize `F10`, replay that the
residual vanishes through degree three, and verify its pairing with the D4
dual is exactly `25/45056`.  A sign or omitted-lift mutation must fail.

It then analyzes the exact homogeneous leading stratum

```text
L=(Q1,...,Q6,F10) in Q[x0,...,x5].
```

Allowed outcomes are:

```text
M1_STRATUM_EMPTY_FORCES_HIGHER_VALUATION
M1_STRATUM_NONEMPTY_REMAINS
RESOURCE_CAP_NO_VERDICT
SOURCE_OR_REPLAY_FAILURE
```

Projective nonemptiness must be certified by exact homogeneous dimension or
an explicit algebraic/projective witness; a random finite-field point is not
enough.  If the stratum remains, the exact quartic equation and its tangent
ideal are the required next Fitting/constructible branch variables.

## Scope

This is the first weighted prefix only.  Nonmembership on the open
`F10!=0` stratum excludes that prefix; `F10=0` remains live unless the exact
projective calculation says otherwise.  No outcome covers grades 7--19,
proves or disproves a finite full jet, excludes an arc, decides K00 closure
incidence, or implies order two, maximum twelve, or JC2.
