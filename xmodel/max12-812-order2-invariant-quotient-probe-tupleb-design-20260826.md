# Exact-order-two invariant quotient: tuple-B control

Date: 2026-08-26

Status: **PREREGISTERED NAVIGATION CONTROL; NO GENUS OR ELIMINATION CLAIM.**

This is an independent-specialization control for
`max12-812-order2-invariant-quotient-probe-design-20260826.md`.  It uses the
same exact seven tails, involution, saturation, fixed-locus test, and two
invariant functions, but specializes at

```text
(k10,k6,k2,mu2,mu4,mu6)=(17,19,23,29,31,37),
characteristic=65521.
```

The tuple and prime were fixed before launch.  The compiler must pin the
tuple-A compiler bytes and exact-transform only the three specialization
sites: base characteristic, printed load sentinel, and the three even target
constants.  It patches the compiler's load dictionary before reconstructing
the tails, so every load-dependent coefficient is regenerated from the exact
tail JSON rather than text-substituted in a polynomial.

Compare tuple B with tuple A only on:

1. saturated fibre dimension and basis size;
2. deck parity and saturated-ideal stability;
3. affine fixed-locus dimension and basis size;
4. invariant-plane image dimension, basis size, factor count, and polynomial
   support/degree.

Agreement suggests the chosen specialization is not exceptional and licenses
an exact generic-load successor.  Disagreement identifies a specialization
or projection discriminant to investigate.  Neither outcome computes a
normalization genus or excludes a source.
