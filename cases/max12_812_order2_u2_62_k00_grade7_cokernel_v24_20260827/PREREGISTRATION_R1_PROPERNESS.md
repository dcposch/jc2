# Preregistration: V24R1 modular properness repair

Date: 2026-08-27

Status: **FROZEN BEFORE EXECUTION OR ALGEBRA.**

V24 found that both exact grade-seven compatibility polynomials have zero
normal form over `F_65521` modulo the prior honest grade-2-through-6 system
plus `F10`, localized at `k10_0*W`.  Its script omitted a check that this
localized ideal is proper, so the normal forms cannot yet be consumed.

V24R1 changes no V24 algebra.  It reads the frozen V24 modular script,
extracts exactly its ring declaration, prior ideal declaration, and
localization equation, recomputes the standard basis, and records

```text
reduce(1,G) == 1
dim(G) >= 0.
```

Both conditions are required for `PROPER_LOCALIZED_IDEAL`.  A negative
control adjoining `1` must instead give `reduce(1,Gunit)==0`; if it does not,
the run fails closed.  The original V24 normal-form files must remain the
two-byte polynomial `0` and retain their frozen hashes.

Allowed outcomes:

```text
PASS_F65521_PROPER_LOCALIZED_PRIOR_IDEAL_AND_ZERO_NORMAL_FORMS
F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION
SOURCE_OR_REPLAY_FAILURE
RESOURCE_CAP_NO_VERDICT
```

Even a PASS establishes only genuine `F_65521` membership of the two V24
compatibility polynomials on the single chart `D(k10_0*W)`.  It does not
establish exact-Q membership, cover `W=0`, reach grade eight, produce a full
jet or arc, decide K00 closure incidence, or imply JC2.
