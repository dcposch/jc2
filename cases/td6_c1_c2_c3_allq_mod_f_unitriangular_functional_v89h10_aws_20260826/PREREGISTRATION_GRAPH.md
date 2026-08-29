# TD6 V89H10G full-q transported-FIRST topology gate

Date: 2026-08-26

Status: exact producer diagnostic only.

Rebuild literal FIRST with all 22 licensed q variables, impose exactly
`F=0` on `D(U)`, and form the same registered relative pivot matrix
`B=A(0)^(-1)A(q)` as V89H10.  Without multiplying polynomial matrices,
emit every affine-q edge of `N=B-I`, its exact coefficient, and the strongly
connected decompositions for the full q set, q2..q14, and q16..q24.

As a cheap obstruction test, evaluate the exact determinant of the relevant
SCC blocks at the preregistered integer points

```text
low_one:  q2=...=q14=1, q16=...=q24=0
all_one:  every licensed q is 1
all_sign: q_e=(-1)^e
```

over the generic specialized E3 coefficient field.  A determinant different
from one rigorously rejects unimodularity of this registered pivot block.  A
determinant equal to one at finitely many points is telemetry only, not a
polynomial identity.  This gate makes no P12, functional, unit-ideal,
whole-TD6, total-Rees, or JC2 claim.
