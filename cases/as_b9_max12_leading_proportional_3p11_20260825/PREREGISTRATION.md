# Preregistration — degree-12 proportional-leading-form gate

Consume the complete `3^183` fixed-D12 solution family modulo
`3^11=177147` over the displayed B9 mod-243 parent.  Reintroduce all 165
predecessor and 182 fresh trits, impose all 276 literal determinant
coefficients modulo `177147`, and impose the necessary characteristic-zero
leading-form condition

```text
P_12 * Q_(0,12) = P_(0,12) * Q_12  (mod 177147).
```

The seed makes `Q_(0,12)` a unit, so these 13 cross-products are equivalent
to `P_12=c Q_12` and include the `P_12=0` case.  Use widened 64-bit products
with reduction after every gate.  SAT is accepted only after literal integer
determinant and leading-form replay; UNSAT needs a checked certificate.

This is a necessary-condition locus over one fixed parent, not a proof that
the locus continues, an all-depth point, or a JC2 result.
