# Preregistration: V24R5 exact-Q direct-target unit lift

Date: 2026-08-27

Status: **FROZEN BEFORE EXECUTION OR ALGEBRA.**

The full-transform exact V24R2 job remains live and untouched.  V24R5 is a
distinct algorithm: over the identical exact-Q ring and identical 36 ordered
generators, call

```text
matrix U;
matrix C = lift(P,ideal(1),U,"slimgb");
```

This asks directly for the single target `1`; it does not compute or consume
a full tracked `liftstd` transform.  A result is theorem-eligible only if
`U` is exactly the 1-by-1 identity and a coefficientwise exact replay proves

```text
matrix(P)*C = 1.
```

Serialize all 36 multipliers separately and replay the identity from those
bytes in a second fresh exact Singular process.  Select a multiplier whose
generator and coefficient are both nonzero.  Setting that multiplier to zero
and adding one to it must each make the identity nonzero in both the producer
and replay process.  A missing lift, warning/error, nonidentity `U`, failed
mutation, or failed byte replay is a fail-closed no-verdict endpoint.

The job is one core, exact Q, at most 900 GiB virtual memory and six hours on
AWS.  Allowed outcomes are:

```text
PASS_EXACT_Q_DIRECT_UNIT_LIFT_REPLAYED_36_ENTRY_IDENTITY
RESOURCE_CAP_NO_VERDICT
SOURCE_OR_REPLAY_FAILURE
```

An exact PASS proves only that the normalized valuation-one finite prefix
through grade six has no point on `D(k10_0*W)` over characteristic zero.  It
does not cover `W=0`, other valuation/unit strata, grades 7--19, a full jet or
arc, K00 closure incidence, order two, maximum twelve, or JC2.
