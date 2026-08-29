# Preregistration: V24 honest grade-seven two-cokernel contraction

Date: 2026-08-27

Status: **FROZEN BEFORE COMPILER EXECUTION OR ALGEBRA.**

## Charged constructible chart

Consume V23's exact generic-rank-five `7 x 7` newest-coefficient matrix
`A(x)` for the grade-seven literal row system.  Use its frozen nonzero
`5 x 5` pivot minor

```text
W = det A[rows 0,1,2,3,4; columns 0,1,2,3,6].
```

On the open chart `W!=0`, derive the complete two-dimensional left kernel
of `A` by exact Cramer minors, not by numeric sampling.  Each covector must
annihilate all seven columns coefficientwise over `Q[x]`.  A sign/minor
mutation must break this identity.

Independently reconstruct from the normalized frozen seven rows and K10
load polynomials the literal grade-seven system

```text
A(x) * (d0_6,...,d5_6,k10_3)^T + b = 0
```

for

```text
d_i = sum_{n=1}^6 d_i_n Lambda^n,
k10 = sum_{n=0}^3 k10_n Lambda^n.
```

The reconstruction must compare `A` coefficientwise to V23 and replay the
full grade-seven coefficient against the frozen V20R2 literal DAG on exact
and modular fixtures.  The honest boundary `k6_0=0` is applied before this
system; no raw tail row or literal K00 evaluation may substitute for the
normalized rows.

Contract `b` with the two polynomial left-kernel covectors and serialize the
two exact compatibility polynomials `C6,C7`.  On the constructible prior
source chart

```text
Phi[row,grade]=0 for all rows and grades 2..6,
F10=0, k10_0!=0, W!=0,
```

grade-seven solvability is equivalent to `C6=C7=0`.  This equivalence is
linear algebra on the `W` chart; it is not an arc or closure statement.

V24 should attempt a bounded modular reduction of `C6,C7` modulo the prior
honest ideal localized at `k10_0*W`.  Modular zero/nonzero is diagnostic
only.  No exact ideal-membership or stratum-exclusion claim may be promoted
without an exact-Q reduction or a separately valid lifted certificate.

## Allowed outcomes and scope

```text
PASS_EXACT_TWO_COMPATIBILITY_POLYNOMIALS_MODULAR_REDUCTION_RECORDED
SOURCE_OR_REPLAY_FAILURE
RESOURCE_CAP_NO_VERDICT
```

The PASS scope is the exact two-equation grade-seven compatibility block on
the single rank-five chart `W!=0`, conditional on all listed prior equations
and `k10_0!=0`.  It does not cover `W=0`, grades 8--19, prove a full jet or
arc, decide K00 closure incidence, or imply order two, maximum twelve, or
JC2.
