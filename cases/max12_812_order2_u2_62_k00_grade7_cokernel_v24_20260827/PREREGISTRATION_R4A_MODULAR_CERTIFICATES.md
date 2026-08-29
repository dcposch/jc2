# Preregistration: V24R4A tracked modular unit certificates

Date: 2026-08-27

Status: **FROZEN BEFORE EXECUTION OR ALGEBRA.**

This is the modular producer stage of frozen V24R4 design
`92e6b7362b6d60808b53e8fbbbde9a7d949691548b6f4fcc458ff0bf1e6f6e9e`.
It runs only after the live exact-Q V24R2 gate has spent 60 minutes without
an endpoint, and it does not interrupt or supersede that exact job.

At the eight preregistered primes from V24R4, use the identical 36 ordered
generators (35 prior generators plus `zinv*k10_0*W-1`) and compute a tracked
`liftstd`.  Replay the basis transform and an explicit 36-entry unit
certificate.  Serialize every multiplier as a separate canonical Singular
polynomial and independently parse it to sorted `(monomial,residue)` JSON.

Mandatory mutations add one to the first multiplier and swap the first two
generators without changing multipliers; both must break the identity.  Every
denominator in the frozen rational source must be invertible at every prime.

Allowed outcomes:

```text
PASS_MODULAR_UNIT_CERTIFICATES_STABLE_SUPPORT_READY_FOR_EXACT_LIFT
PASS_MODULAR_UNIT_CERTIFICATES_SUPPORT_VARIES_NO_EXACT_LIFT_YET
RESOURCE_CAP_NO_VERDICT
SOURCE_OR_REPLAY_FAILURE
```

Both PASS outcomes are theorem-ineligible modular evidence.  They prove no
exact-Q identity, chart emptiness over characteristic zero, compatibility,
stratum, jet, arc, closure, order-two, maximum-twelve, or JC2 claim.  A
separately frozen R4B must rationally reconstruct and replay an exact-Q
identity before any exact conclusion.

