# V22 R1 narrow quadratic-profile repair

Date: 2026-08-27

Status: **FROZEN BEFORE R1 COMPILATION OR ALGEBRA.**

Preserve R0 as a pre-algebra source-profile failure.  Replace only its false
requirement that all six quadratic initials be nonzero by the exact frozen
K00 profile

```text
Q1,...,Q5 are nonzero; Q6 is exactly zero.
```

Two mutations are mandatory: adding a nonzero quadratic term to `Q6` must
invalidate the profile, and zeroing one of `Q1,...,Q5` must invalidate it.
No other algebra, lift, dual, weighting, branch criterion, resource cap, or
firewall changes.  The allowed outcomes and charged scope remain exactly
those of `PREREGISTRATION.md`.
