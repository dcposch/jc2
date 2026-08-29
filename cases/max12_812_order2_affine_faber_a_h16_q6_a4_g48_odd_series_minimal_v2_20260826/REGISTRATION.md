# Registration: minimal V2 odd-series grade-48 functional

Date: 2026-08-26

Status: preregistered exact-source certificate probe; no theorem.

The V1 series client retained and evaluated all seven tail polynomials before
forming a functional that uses only rows 1, 3, and 7.  V2 mechanically drops
the unused `T2,T4,T5,T6` and `P2,P4,P5,P6` assignments from the source emitted
by the pinned complete compiler.  It then computes only

```text
[s^48] (P7 - E(s)^2 P3/32 + E(s)^3 P1/64).
```

All substitutions inside the three used source rows are unchanged, including
moving center/tangent/normal/complement variables and every load that those
rows contain.  Exact `Q` is evidence and characteristic `65521` is a control.
The V1 5-minute and broad 15-minute timeouts are navigation-negative only.

This probe emits a raw ideal member, not a predecessor reduction, and makes no
rational-regrading, source/Rees coverage, order-two, maximum-twelve, or JC2
claim.
