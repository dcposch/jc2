# K00 closure V4: repaired positive Faber block order

Date: 2026-08-27

Status: **PREREGISTERED REPAIR; NO ENDPOINT.**

V3's zero weights failed the mandatory invariant-core gate and are rejected.
V4 retains the exact V2 g-open ideal but uses the genuine global block order

```text
(wp(1,8,7,6,5,4,3,2),dp(7))
```

on the ordered variable blocks

```text
(Lambda,C0,C1,C2,C3,C4,C5,C6) | (k10,k6,k2,mu2,mu4,mu6,Jdet).
```

The first block is the exact positive Faber/Lambda grading.  Every source
row is homogeneous in that block; all retained loads remain ordinary
polynomial variables in the second global `dp` block.  No zero weight,
coefficient-field projection, parameter normalization, or boundary-first
restriction is used.  Monomial order changes the Gröbner algorithm, not the
ideal or V2 equivalence.

The wrapper also changes unsupported `quit(code)` gate exits to supported
`exit(code)` calls.  The invariant core, restriction identity, and
restriction-first unit must all pass before the source saturation marker.

First screen: characteristic 65521 on AWS Box01, 20-minute / 64-GiB cap.
It is an algorithm/control lane only.  A fast validated endpoint licenses a
separate exact-Q replay.  Failure, timeout, OOM, or missing/nonunique marker
is no verdict.
