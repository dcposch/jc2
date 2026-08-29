# V36 first-occurrence receiver amendment

Date: 2026-08-27

The frozen V36 compiler checks that no variable of sigma weight exactly 19
occurs.  Sigma weight is not, in general, the same thing as the grade at
which a source coordinate first occurs, so that check alone is not an
honest prolongation census.

An exact comparison of all hash-pinned rho-zero rows through grade 18 with
the seven V35 grade-19 rows gives the actual first-occurrence census:

```text
Tg19_1: cs7, rs7, k10_6, ac8, az8, ez8, k6_1, ec9
Tg19_2: ell8, rs7, k10_6, ac8, ez8, k6_1
Tg19_3: ell8, ez8
Tg19_4: none
Tg19_5: none
Tg19_6: none
Tg19_7: none
```

Thus the V36 conclusion survives the terminology repair: the sole
obstructing row `Tg19_7` is jet-free in the honest first-occurrence sense,
so none of the nine new grade-19 coordinates can cancel its normal form.
The unit-ideal calculation still concerns only the V34/V32 component and
does not close other ordered-`T-a1` supports.
