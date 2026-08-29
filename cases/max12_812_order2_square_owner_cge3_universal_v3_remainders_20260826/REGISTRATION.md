# Registration: `c>=3,r>=1` universal receiver V3 remainder repair

Date: 2026-08-26

V1 found the full source/Laurent bridge but tested the wrong cubic scalar.
V2 repaired `1/16` and exposed the second precise issue: the moving-base
grade-15 congruence is an on-shell identity modulo the grade-13 and grade-14
proper remainders, not an off-shell polynomial identity.

V3 pins both immutable failed controls.  It computes the six coefficients
of each corrected remainder modulo `L0^3`, checks their degree bounds, and
tests

```text
C15+(1/16)A0^3 in (L0, coeffs(R13), coeffs(R14)).
```

For a genuine source arc, the lower-unitriangular row bridge makes every
coefficient of `R13,R14` zero; the resulting grade-15 congruence therefore
forces `L0|A0^3`.  All other source/Faber and dual-field sentinels are
unchanged.  Scope remains only `c>=3,r>=1` on `D(p*k0)` after the reviewed
first-normal and half-weight gates.
