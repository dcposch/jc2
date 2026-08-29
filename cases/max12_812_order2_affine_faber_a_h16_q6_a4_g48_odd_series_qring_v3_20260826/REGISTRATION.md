# Registration: truncated-qring V3 odd-series functional

Date: 2026-08-26

Status: preregistered exact coefficient accelerator; no theorem.

The ordinary minimal V2 retains only rows 1, 3, and 7 but expands all powers
above the requested grade before extracting `[s^48]`.  V3 performs the same
frozen substitutions in the exact quotient `Q[s,...]/(s^49)`.  Coefficients
through grade 48 are unchanged, while every irrelevant higher power is
discarded during multiplication.

The emitted functional is exactly

```text
[s^48] (P7 - E(s)^2 P3/32 + E(s)^3 P1/64).
```

The inherited 49-entry extractor control is mandatory and is evaluated in
the quotient ring, so any shift/division incompatibility fails closed.  The
compiler also verifies that only the intended `T1,T3,T7` and `P1,P3,P7`
assignments remain.  Exact `Q` is evidence and characteristic `65521` is a
software control.

This client tests a raw complete-source ideal member.  It does not by itself
prove predecessor reduction, chart coverage, rational regrading, source/Rees,
order two, maximum twelve, or JC2.
