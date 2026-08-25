# TD6 q2-beta P3/QH curve source-DAG certificates (V65)

Frozen status: **producer-exact localized source identities; hostile review
pending.**

Inside the fixed source-typed normalized A3 section
`(c1,c2,c3)=(C,V,U)` with

```text
H  = C - 3 U^2,
P3 = V^4 - 32 V^2 U^3 + 128 U^6,
QH = V^4 + 8 V^2 U^3 - 64 U^6,
q_beta(t) = t + beta t^2 + t^25,
```

V65 rebuilds the exact function fields of the two curves
`H=P3=0` and `H=QH=0`, retaining polynomial beta, direct
`q_beta'=1+2 beta t+25 t^24`, the fixed `p=t^15` boundary, frozen pole/F1
data, and arbitrary-degree original source rows.  It uses no weighted source
scaling.

On each component, exact staged ranks are

```text
transport       3470 / 3602
first             38 / 132
previous/pole     38 / 94
current           25 / 56.
```

The singleton current row 13 gives `N13=(k/25) beta` and traces through
exactly previous row `('X-1',14)` plus original first rows.  The cached
quadratic row `('X-1',0)` is an independent positive control and is not an
N13 edge.  Genuine P12 has 2,885 terms and 28 nonzero original first rows;
its direct source replay composes with N13 to give the unit residual
`-k/50`.

Every emitted leaf and chart denominator has radical `{U}` (the source uses
the polynomial variable name `x` for `U`).  The complete chart is `U^13`.
Thus the package proves the original-row identity only on the two opens

```text
H=P3=0, D(U),
H=QH=0, D(U).
```

The raw `U=0` endpoint is separate.  The QH run also checks

```text
T=V^2/U^3,
P3/U^6=T^2-32T+128,
QH/U^6=T^2+8T-64,
((5T-136)QHnorm-(5T+64)P3norm)/512=1.
```

This proves P3 and QH are disjoint on `D(U)`; it does not itself exclude
either component.  The two source identities do that independently.

Box02 and r6d ran the identical source archive under 12-GiB caps.  Their
stdout differs only in the absolute artifact path; canonicalized streams and
both emitted artifacts agree exactly.  The frozen direct-qprime omission run
prints `direct_qprime_omission_changes_N13=true` and then exits one in the
reporter because the expected N13 record is absent.  It is a negative
control, never theorem evidence.

Run the lightweight custody/marker audit with:

```bash
python3 verify.py
```

No whole P3/QH curve, whole H divisor, whole A3, other TD6 modulus, TD6,
SP-2, landing, or JC2 statement is claimed here.  Composition with the
separately reviewed raw `U=0` theorem and the other H-cover leaves remains a
separate review obligation.
