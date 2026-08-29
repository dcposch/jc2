# Preregistration: V24R6 six-leading-variable exact D(W) gate

Date: 2026-08-27

Status: **FROZEN BEFORE EXECUTION OR ALGEBRA.**

Let `Q1,...,Q6` be the reviewed exact V22 unloaded quadratic initials
(`Q1,...,Q5` nonzero and `Q6=0`), let `F10` be the reviewed exact quartic,
and let `W` be V23's exact rank-five witness.  All lie in
`Q[x0,...,x5]`.  Define

```text
B = (Q1,...,Q6,F10,z*W-1) in Q[x0,...,x5,z].
```

This is a structural coefficient-base test, not a new term order.  Since the
full V24 prior ideal contains `Q1,...,Q5,F10` and its last generator is
`zinv*k10_0*W-1`, a unit certificate for `B` maps to the full ring under

```text
x_i -> d_i_1,       z -> zinv*k10_0.
```

The producer first requests the direct target lift
`lift(B,ideal(1),U,"slimgb")`.  If it returns an identity, it must serialize
all eight coefficients, replay `B*C=1` in a second exact process, apply the
displayed substitution, and replay the embedded 36-generator full-V24
identity coefficientwise.  It must prove the exact source map
`Q1..Q5 -> P1..P5`, `F10 -> P35`, and `zW-1 -> P36`; the zero `Q6`
coefficient is retained in the eight-entry certificate but contributes zero.
Dropping a nonzero contributing coefficient and adding one to it must break
both the small-ring and embedded full-ring identities.

If the direct lift is not an identity, compute a tracked exact
`liftstd(B,T)`, replay `matrix(B)*T=matrix(G)`, require `NF_G(1)=1` and
`dim(G)>=0`, and serialize `G,T`, the dimension, and a second-process replay.
This exact proper standard basis is the required nonempty scheme witness;
normal-form telemetry alone is not an endpoint.  Adding `1` must change the
ideal to the unit ideal.

Allowed outcomes:

```text
PASS_EXACT_LEADING_BASE_DW_UNIT_WITH_FULL_36_GENERATOR_EMBEDDED_IDENTITY
PASS_EXACT_LEADING_BASE_DW_PROPER_WITH_TRACKED_BASIS_AND_DIMENSION
RESOURCE_CAP_NO_VERDICT
SOURCE_OR_REPLAY_FAILURE
```

The unit outcome proves the normalized valuation-one prefix has no point on
`D(k10_0*W)` already at the leading-base/F10 level.  The proper outcome only
shows that this leading-base chart survives; it does not imply that the full
prior-jet chart survives.  Neither outcome covers `W=0`, grades 7--19, a full
jet or arc, K00 closure incidence, order two, maximum twelve, or JC2.
