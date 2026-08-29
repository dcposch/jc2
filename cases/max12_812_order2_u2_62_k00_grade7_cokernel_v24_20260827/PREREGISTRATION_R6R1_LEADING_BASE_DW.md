# Preregistration: V24R6R1 six-leading-variable exact D(W) gate

Date: 2026-08-27

Status: **FROZEN BEFORE EXECUTION OR TARGET ALGEBRA.**

This is the fail-closed repair of the pre-algebra R6 design failure recorded
in `DESIGN_ERRATUM_R6_LEADING_BASE_DW.md`.  Let `Q1,...,Q6` be the reviewed
exact V22 unloaded quadratic initials (`Q1,...,Q5` nonzero, `Q6=0`), let
`F10` be the reviewed exact quartic, and let `W` be V23's exact rank-five
witness.  All lie in `Q[x0,...,x5]`.  The mathematical ideal is

```text
B = (Q1,Q2,Q3,Q4,Q5,F10,z*W-1) in Q[x0,...,x5,z].
```

The logical source order remains the eight slots
`(Q1,...,Q6,F10,zW-1)`, with the `Q6` coefficient required to be serialized
as literal zero.  This distinction is mandatory because Singular removes a
zero generator from an ideal.

The producer first computes `S=slimgb(B)` over exact `Q` and uses only
`NF_S(1)` and `dim(S)` to choose a branch:

- Unit branch: require `NF_S(1)=0` and `dim(S)=-1`, then and only then run
  `lift(B,ideal(1),U,"slimgb")`.  Require `U=1`, serialize seven actual
  coefficients plus the zero `Q6` slot, and replay the eight-slot identity in
  a fresh exact process.
- Proper branch: require `NF_S(1)=1` and `dim(S)>=0`, then compute a tracked
  exact `liftstd(B,T)`.  Replay `matrix(B)*T=matrix(G)`, require
  `NF_G(1)=1` and the same nonnegative dimension, serialize `G,T`, and replay
  them from bytes in a fresh exact process.  This tracked standard basis and
  dimension are the exact properness witness; normal-form telemetry alone is
  not an endpoint.

For a unit result, expand to the logical eight-entry certificate and apply

```text
x_i -> d_i_1,       z -> zinv*k10_0.
```

Replay coefficientwise in the full exact-Q V24 source, proving
`Q1..Q5 -> P1..P5`, `F10 -> P35`, and `zW-1 -> P36`; the zero `Q6` slot maps
to zero.  The embedded coefficient vector has all other entries zero.  A
nonzero contributing coefficient is frozen, and drop/add mutations must break
the identity in the producer, fresh small-ring replay, and fresh full-ring
replay.  On the proper branch, a transform-entry drop and adjoining `1` must
break the respective tracked identity/properness state in both processes.

Allowed outcomes:

```text
PASS_EXACT_LEADING_BASE_DW_UNIT_WITH_FULL_36_GENERATOR_EMBEDDED_IDENTITY
PASS_EXACT_LEADING_BASE_DW_PROPER_WITH_TRACKED_BASIS_AND_DIMENSION
RESOURCE_CAP_NO_VERDICT
SOURCE_OR_REPLAY_FAILURE
```

The unit outcome proves only that the normalized valuation-one prefix has no
point on `D(k10_0*W)` already at the leading-base/F10 level.  The proper
outcome proves only that this leading-base chart survives; it does not show
that the full prior-jet chart survives.  Neither outcome covers `W=0`, grades
7--19, a full jet or arc, K00 closure incidence, order two, maximum twelve,
or JC2.
