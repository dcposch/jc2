# V2 coefficientwise universal `H3/H5` certificate

Date: 2026-08-26

V1 forms the full inverse-Faber polynomials before truncation and is a
correct but potentially expensive deployment.  V2 imports V1's immutable
complete-source emitter and changes only the verification strategy.

The source control proves every coefficient of every ordinary row `P_i`
below sigma grade 42 is zero.  Since `B=4a` has order five, every
positive-`B` term in the inverse-Faber connection has order at least 47.
Therefore modulo `s^46` the exact rows are

```text
H3=P3-(E/4)P1,
H5=P5-(3E/4)P3+(5E^2/32)P1.
```

V2 constructs these from the exact grade-42--45 coefficients emitted by
the complete source and verifies the raw congruences and direct unit
`[s^45](E*H3+H5)=-p*m^3/16`.  It makes no source-equation substitution.
Exact Q is evidence and F65521 is a software control.  Scope and coverage
firewalls are identical to V1.
