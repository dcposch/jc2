# Preregistration: V24R4B exact-Q reconstruction and replay

Date: 2026-08-27

Status: **FROZEN DESIGN BEFORE R4A ENDPOINT; NO EXECUTION.**

Activation requires a byte-frozen V24R4A endpoint in which all eight
preregistered prime lanes replay a 36-entry unit certificate and have exactly
the same labelled monomial support.  A resource cap, a failed lane, or
support variation stops R4B with no characteristic-zero conclusion.

For every labelled multiplier and monomial in that common support, combine
the eight finite-field residues by CRT in the registered prime order.  Apply
standard rational reconstruction with the symmetric uniqueness bound
`max(|numerator|,denominator) <= floor(sqrt(M/2))`, require positive
denominator, coprimality, and a residue replay at all eight primes.  No
missing or additional monomial may be inserted.

Rebuild the exact 36 ordered generators directly from the frozen rational
V24 source by changing only `ring R=65521` to `ring R=0`.  In one fresh exact
Singular process, replay coefficientwise

```text
matrix(P_Q) * C_Q = 1.
```

Then use a second process to serialize each exact generator canonically and
an independent Python sparse-rational parser/multiplier to replay the same
identity.  The sparse parser may consume only integer/rational coefficients,
the frozen 34 variable names, products, and nonnegative powers.  It must not
call a CAS for its arithmetic.  Deleting one nonzero reconstructed term and
changing one reconstructed coefficient must each make both replay engines
nonzero.

Allowed outcomes:

```text
PASS_EXACT_Q_LOCALIZED_PRIOR_IDEAL_UNIT_WITH_REPLAYED_36_ENTRY_IDENTITY
NO_STABLE_EXACT_CERTIFICATE_NO_VERDICT
RATIONAL_RECONSTRUCTION_OR_REPLAY_FAILURE
RESOURCE_CAP_NO_VERDICT
```

Only the exact PASS proves that the normalized valuation-one finite prefix
through grade six has no point on `D(k10_0*W)` over characteristic zero.  It
does not cover `W=0`, other valuation/unit strata, grades 7--19, a full jet or
arc, K00 closure incidence, order two, maximum twelve, or JC2.  Modular
agreement and reconstructed-but-unreplayed bytes are theorem-ineligible.
