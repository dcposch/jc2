# Preregistration: V24R3 independent-prime properness preflight

Date: 2026-08-27

Status: **FROZEN BEFORE EXECUTION OR ALGEBRA.**

Purpose: while the tracked exact-Q V24R2 gate runs, test whether the
`F_65521` localized unit ideal is visibly exceptional.  From the same frozen
literal V24 prior ideal, change only the coefficient field to each of the
predeclared primes

```text
32003, 65519, 65537.
```

For each prime compute `G=std(P)`, `reduce(1,G)`, and `dim(G)`.  The identical
forced-unit mutation `P+(1)` must reduce `1` to zero.  Each process is a
single-core Singular process with a ten-minute wall cap and 64-GiB virtual
memory cap; the three primes may run concurrently on AWS.

Allowed per-prime statuses are `UNIT`, `PROPER`, and `RESOURCE_CAP`.  A
proper marker requires normal form exactly `1` and dimension at least zero;
a unit marker requires normal form exactly `0` and dimension `-1`.

This is **preflight only**.  No combination of modular outcomes proves exact-Q
properness or unit membership.  In particular, a unit special fibre may be a
bad-prime vertical effect, and a proper special fibre may be caused by a
denominator in a characteristic-zero unit certificate.  V24R2 remains the
sole exact gate.  The scan gives no compatibility, stratum, jet, arc,
closure, order-two, maximum-twelve, or JC2 conclusion.

