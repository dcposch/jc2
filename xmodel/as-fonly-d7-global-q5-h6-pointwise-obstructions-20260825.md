# AS F-only `D=7`: both displayed global Q6/high survivors stop at Q5

**Status: PRODUCER EXACT AT TWO DISPLAYED STATES; PROVISIONAL PENDING
DIFFERENT-MODEL SOURCE/REPLAY REVIEW.**

The two source-replayed global Q6/high SAT models are filtered source states,
not chronological complete maps.  A fail-closed direct determinant check
first established that low coefficients of `det(P,Q)-1` still occur at
orders 27 and 81.  Thus the quotient `(det-1)/243` is defined at the already
terminal degrees 7 through 12, but not globally.  The attempted low-Cartier
successor is quarantined as a source-order `TYPE-FAIL`, not an obstruction.

The correct next diagonal layer is Q5.  Adjoin the fourteen coefficients of
homogeneous degree-six order-81 digits `(H6,J6)`.  The charged equations are

```text
6 rows:  G5 + (H6)_x + (J6)_y = 0;
63 rows: R12,...,R7 = 0 after including the H7+H6 cross-carry.
```

For each displayed model the resulting 69-by-14 system is affine over
`F3`.  Exact zero/unit substitution, every pairwise unit control, and direct
row elimination give rank pair

```text
rank(A) = 8,   rank([A|b]) = 9.
```

Sparse left-null certificates use the row convention
`[x^i y^(d-i)] row_d = i`:

```text
base 513:
  weights 2,2,1,1,1 on
  G5[y^5], G5[x y^4], G5[x^2 y^3],
  R8[x^3 y^5], R8[x^4 y^4];
  the coefficient columns pair to 0 and the affine RHS pairs to 1.

base 519:
  weights 2,1,1,1,1 on
  G5[y^5], G5[x y^4], G5[x^2 y^3],
  R8[x^3 y^5], R8[x^5 y^3];
  the coefficient columns pair to 0 and the affine RHS pairs to 1.
```

Exact hashes are:

| base | matrix | RHS | result JSON |
|---|---|---|---|
| 513 | `637e305327ed6476efb38bae644733e7bd34e99645e48f746b73b52fff1aa2ff` | `701276f3ed1fe63abbc18f935af703f6323a38276aff33c2a6cd16967de2d7f5` | `801ea4d43399a145de3a9995fba0445420b341b989995779884002180e594f61` |
| 519 | `c54bc693624c71ddb07fd3c9136311d0e02a31b1194ff826af7aedbfcb16ff91` | `2fc0d96fecb119141829ef51546666d3efa9535fbbab15f9e7fd8e6a139b0aee` | `d3709b94d3e8b8f6172773acc8b8b0331017f2f48fa0c70fdf1cc770cff436af` |

The source is frozen at
`cases/as_fonly_d7_global_q5_h6_pointwise_20260825/`; its exact Box02 result
archive has SHA
`9a2be2103ab31c1ac9f5415ee14d157f491839a6787054a39f4e5a6478a237e8`.
The V1 type-fail archive has SHA
`f1242aea0acec759c815156f1117f1edd39325a6536226f76a005c8f728f551b`.

Therefore these **two displayed states** do not admit a compatible Q5
restoration.  This says nothing about the other Q9/Q8/Q7/H7 points in bases
513 or 519, the other structural bases, all `D=7`, or an all-depth/characteristic-
zero lift.  The next exact gate must globalize Q5 over the complete accepted
Q6/high fibre, retaining all 69 rows.  The five-row certificates are a
compression hint, not a licence to discard the other rows before symbolic
source verification.
