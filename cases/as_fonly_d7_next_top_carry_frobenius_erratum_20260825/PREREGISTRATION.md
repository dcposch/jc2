# Preregistered source audit

Over the integers, construct generic homogeneous `C7,D7,C6,D6,C5,D5` and
the six degree-six Frobenius first-digit directions `UF,VF`.  Before any
reduction, assert formal divisibility and compute

```text
MF7/3 = ({UF,D7}+{C7,VF})/3,
MF6/3 = ({UF,D6}+{C6,VF})/3,
Kdouble/9 = {UF,VF}/9                         modulo 3.
```

Require nonzero explicit controls `UF=x^6,D7=y^7` at degree 11 and
`UF=x^6,VF=y^6` at degree 10.  Emit canonical hashes of the corrected
generic rows.  A failed divisibility assertion or zero witness is a source
failure and no verdict.

This audits universal source terms only; predecessor incidence and corrected
finite counts are separate successors.
