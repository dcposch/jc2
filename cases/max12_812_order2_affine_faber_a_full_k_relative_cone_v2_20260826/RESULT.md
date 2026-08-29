# Result: raw `K` coefficient grouping and fixed delayed relative cone

Date: 2026-08-26

Status: **DUAL-AWS EXACT SUPPORT ANALYSIS PASS; PROVISIONAL NAVIGATION.**

The exact 371-term normalized polynomial has 371 distinct valuation groups
after treating `E,M` as coefficient-ring units.  Thus no two raw monomials
were accidentally merged into an unrecorded `E,M` coefficient factor.

On the fixed delayed schedule

```text
a:5, lambda:15, X:Y:q, R*:S*:2q,
K10:K6:K2:mu2:42, mu4:48, mu6:54, J:57,
```

the intrinsic term has weight 45.  At `q=6` it is the unique raw-`K`
minimum and the next support weight is 47.  In fact the raw functional has a
strict direct-unit cone for

```text
q>5.
```

At the equality wall `q=5`, exactly four support terms tie the intrinsic
term.  Factoring out `lambda^2`, their initial polynomial is

```text
-3*M^2*X^2*a/8
+3*E*Y^2*a/2
-3*Y^2*X/16
+3*M^2*R0*X/16.
```

This is a genuine center/kernel/complement equality face.  It is not
resolved by the raw functional and must be reduced by the complete
predecessor initial ideal.  It also explains why a center-truncated q6-style
compiler is not a coverage certificate.

The whole row system has separate schedule walls

```text
30+2*q=42  at q=6       (unloaded quadratic versus delayed load),
30+2*q=45  at q=15/2    (unloaded quadratic versus intrinsic cubic).
```

Those walls are not derived from `K` alone; their coefficient ideals must be
emitted from all seven predecessor rows.  The present result therefore does
not promote the q<6 or q=6 composition.

For each of `K2,K6,K10`, the Pareto-minimal raw load forms have

```text
(a exponent, lambda exponent) = (1,0) and (0,1),
```

so their weights are `v(Ki)+v(a)` and `v(Ki)+v(lambda)`.  The target forms
are `v(mu2)+v(a)` and `v(mu4)+v(a)`.  Consequently lower unexplored load
slopes can beat or tie `3*v(lambda)`; cancellations on an affine load graph
must be proved through predecessor/source equations rather than inferred
from this support table.

Both AWS lanes emitted identical coefficient groups and stdout endpoints.
This artifact is not a predecessor reduction, factor saturation, Newton-fan
coverage, total-Rees/source overlap, order-two result, maximum-twelve
result, or JC2 result.
