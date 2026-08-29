# Preregistration: V25 honest grade-eight newest-coefficient block

Date: 2026-08-27

Status: **FROZEN BEFORE COMPILER EXECUTION OR ALGEBRA.**

Continue conditionally on the V24 prefix, without assuming that the prefix
is nonempty or that V24's two compatibility equations are automatic over
`Q`.  At Lambda grade eight the honest newest coefficients are

```text
d0_7,...,d5_7,k10_4,k6_1.
```

The fixed boundary coefficient `k6_0=0` remains restricted before the
solve.  The exact `7 x 8` newest block is the V23 grade-seven matrix

```text
[ Jac(Q1,...,Q7)(x) | K10_quadratic(x) ]
```

with one new column `K6_linear(x)` for the free coefficient `k6_1`.
The compiler must reconstruct this column from the frozen K6 loads, verify
the source-column types (`k6_0` fixed zero, `k6_1` free), and independently
check it against the literal V20R2 Lambda-grade-eight DAG over exact `Q` and
`F_65521`.  Restoring `k6_0` at grade seven must reproduce the same nonzero
linear initial, while omitting the allowed `k6_1` must leave V23's rank-five
block.

Because V23's first seven columns have generic rank five, adjoining one
column gives rank at most six.  Extend V23's frozen nonzero `5 x 5` pivot
minor by the K6 column and each remaining row; an exact nonzero `6 x 6`
minor proves rank six.  If both extensions vanish, report rank five on the
V23 chart and do not search blindly for unrelated monomial orders.

Allowed outcomes:

```text
PASS_EXACT_GRADE8_RANK6_ONE_COMPATIBILITY_REMAINS
PASS_EXACT_GRADE8_RANK5_TWO_COMPATIBILITIES_REMAIN
SOURCE_OR_REPLAY_FAILURE
RESOURCE_CAP_NO_VERDICT
```

This is a newest-variable/Fitting block only, conditional on the full V24
prefix and the named V23 pivot chart.  It does not decide the grade-eight
inhomogeneous compatibility relation, establish that any prefix exists,
cover other rank charts or grades 9 through 19, produce a full jet or arc,
decide K00 closure incidence, or imply order two, maximum twelve, or JC2.
