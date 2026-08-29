# Preregistration: exact unloaded K00 row-7 membership V7

Date: 2026-08-27

Status: **FROZEN TWO-LANE MEMBERSHIP TEST; NO RESULT AT REGISTRATION.**

Let `r1,...,r7` be the unloaded (`k10=k6=k2=0`) frozen ordinary tails after
the exact K00 transverse change

```text
C5=d5,                    C4=(3*C6^2+d4)/8,
C3=d3,                    C2=(C6^3+d2)/16,
C1=d1,                    C0=(C6^4+d0)/256.
```

V7 asks the exact stronger question

```text
r7 in (r1,...,r6) over Q[C6,C6^-1,d0,...,d5] ?
```

It freezes two exact-Q AWS lanes before either runs.

1. **Direct localized lane.**  Adjoin `t` and the equation `1-t*C6`; compute
   the standard basis of `(r1,...,r6,1-t*C6)`, reduce `r7`, and, on zero
   residual, save a `lift` matrix and replay the identity exactly.  A nonzero
   residual is also saved.  This is literally the localization at `C6`.
2. **Six-normal lane.**  Use weighted homogeneity and the faithfully flat
   Kummer cover `C6=u^2`,
   `d5=u^3*e5,d4=u^4*e4,...,d0=u^8*e0`, with `u` invertible.  Dividing each
   weight-`12+i` row by its unit power of `u` normalizes to `C6=1` and six
   variables `e0,...,e5`.  Compute the standard basis and normal form there,
   again saving and replaying a lift or saving a residual.  Faithful-flat
   descent makes membership equivalent to the direct localized question.

Both lanes fail closed on source/type/hash mismatch, a unit source ideal,
missing or nonunique markers, Singular diagnostics, failed replay, timeout,
or absent evidence.  A pass with membership says only that the pure unloaded
coefficient contribution of row 7 is redundant after the first six rows on
`D(C6)`; the first possible K00 separator is then mixed in `Lambda`/loads or
targets.  Nonmembership identifies a pure coefficient separator.  Neither
outcome decides the full K00 closure, Taylor realization, or JC2.
