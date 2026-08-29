# Preregistration: V23 honest grade-seven newest-coefficient block

Date: 2026-08-27

Status: **FROZEN BEFORE COMPILER EXECUTION OR ALGEBRA.**

## Charged block

Continue only on the V22 valuation-one, `k10(0)=kappa!=0`, `F10=0`
candidate prefix.  In the seven literal row equations at Lambda grade seven,
the honest newest coefficients are

```text
d0_6,...,d5_6,k10_3.
```

Their exact `7 x 7` coefficient matrix has first six columns the Jacobian
of the seven unloaded quadratic initials at `x=(d0_1,...,d5_1)` and last
column the seven quadratic K10-load initials.  V23 reconstructs this matrix
from the frozen normalized rows and load polynomials rather than assuming
it, serializes it, and determines its generic rank exactly over `Q(x)` by
determinants/minors.

The boundary restriction is prior to this block: `k6_0=0`.  The mandatory
negative control restores the forbidden `k6_0`; its grade-seven column is
the vector of linear K6-load initials and must be nonzero.  It must not be
included in the honest matrix.

Allowed exact outcomes are:

```text
GENERIC_RANK_7_NO_GRADE7_COMPATIBILITY_ON_OPEN_DET
GENERIC_RANK_6_ONE_SCALAR_AUGMENTED_COMPATIBILITY_REMAINS
GENERIC_RANK_LE5_HIGHER_FITTING_BLOCK_REMAINS
SOURCE_OR_REPLAY_FAILURE
RESOURCE_CAP_NO_VERDICT
```

If rank is below seven, this producer reports the precise dimension of the
remaining left-cokernel and freezes a nonzero maximal-rank minor.  The next
producer must contract the literal grade-seven inhomogeneous term against
that cokernel and reduce it on the complete prior honest source ideal; a raw
remainder from one D3 lift is forbidden.

## Scope

This is a representation-invariant newest-variable/Fitting block from the
literal seven-row source, conditional on the prior V22 candidate prefix.  It
does not by itself show that any prior prefix lifts, decide the augmented
compatibility equation, cover grades 8--19, produce a full jet or arc,
decide K00 closure incidence, or imply order two, maximum twelve, or JC2.
