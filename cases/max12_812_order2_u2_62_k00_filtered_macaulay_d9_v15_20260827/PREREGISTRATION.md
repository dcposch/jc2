# Preregistration: K00 filtered Macaulay degree 9 V15

Date: 2026-08-27

Status: **FROZEN D9 EXTENSION; NO D9 RESULT AT REGISTRATION.**

Accepted exact-Q V10 proves cumulative compatibility through D8:
`r7 in (r1,...,r6)+m^9` at the normalized K00 germ `C6=1`.  V15 uses the
identical frozen tail expansion and complete cumulative map, extended through
normal degree 9 with every multiplier monomial of degree at most 7.  Its
frozen shape is

```text
equations=4998,
multiplier_coefficients=10296.
```

The first launch is a `p=65521` navigation preflight only.  D8 required 11.3
seconds and 285,692 KiB at this prime; the D9 sparse file and dense field
matrix are roughly three times larger, so a 30-minute/64-GiB cap is safely
conservative.  No modular result is characteristic-zero evidence.

Any later exact-Q lane must use this same frozen map.  Equality of rank and
augmented rank must be accompanied by a rational multiplier jet replaying all
4,998 equations; inequality must have an exact replayed left functional.
Exact incompatibility would make degree 9 the first filtered obstruction;
exact compatibility would give membership modulo `m^10`.  Neither outcome
decides local/formal membership, mixed Lambda/load/target reachability,
closure-first incidence, Taylor realization, or JC2.
