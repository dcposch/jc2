# Hostile review: formal weighted affine-Faber `A` direct unit

Work in `/Users/dc/code/math/jc2`.  Independently review the immutable
center-complete formal-weighted producer:

```text
0ef7cfc84691c5fa466e98cf76f942d6bcd217547d0eb91b0f3860240da8eae5
  cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/FREEZE.sha256
86883cc16a48e0ee4b4a1ea01844cedbdd212eb41414fe918f641d6654582f48
  cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/EVIDENCE.sha256
5736a3b00ec6e1b74b43c5112b8fadccf340b98558854b63ddd6ca9042d8370d
  cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/RESULT.md
1946cec19e71fcce5b7a38a68125362a158bb589c61347b196d36bb6cdc62fbf
  cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/RESULTS.sha256
06e2709344b47ec09549638a53f193b79ca4f791d40c2c0b9c8c04e0284330be
  xmodel/max12-812-order2-affine-faber-a-loaded-kernel-q6-hostile-review-grok-20260826.md
```

Write exactly one report to

```text
xmodel/max12-812-order2-affine-faber-a-formal-weighted-h3-h5-hostile-review-grok-20260826.md
```

Edit no other file, do not touch `jc2-lean`, and do not edit shared
ledgers.  Rehash every charged file.  Do not trust producer status or PASS
tokens.  Exact Q is characteristic-zero evidence; F65521 is a software
control only.

Independently verify:

1. All seven frozen complete ordinary-Faber tails are reconstructed from
   the pinned source and the exact substitutions really encode
   `Q=A^2(A^2+4aA+E)+(X+R1)A+R0` and
   `N=lambda*(MA(A^2+4aA+E)+YA+MX/2+S1A+S0)` after depression.
2. Check the inverse-Faber connection and directly rederive, modulo
   `t^46`,
   `H3=-(3/8)t^42 lam^2 MXY-(1/16)t^45 lam^3 M^3` and
   `H5=(3/8)t^42 E lam^2 MXY`.  Check all signs, powers, load/target
   cancellations, and `K45=-E lam^3 M^3/16`.
3. Audit that treating `a,E,M,X,Y,R,S,lam` as independent polynomial
   variables really makes arbitrary power-series substitution legitimate.
   In particular, test the omitted `a6` moving-center jet from the earlier
   q6 REPAIR, every intermediate tangent/complement jet, fractional orders
   after common ramification, and higher kernel powers through weight 45.
4. Distinguish the formal weighted identity from global source coverage.
   It should repair the algebraic center-truncation defect for the stated
   moving-discriminant chart, but it must not silently prove that every raw
   source arc enters that chart.  State the exact remaining two-sided
   coordinate/Rees gate, if any.
5. Keep scope narrow: `q<6` is a separate homogeneous certificate; `m=0`,
   other load slopes, terminal/Taylor, total fan, order two, maximum twelve,
   and JC2 are not claimed.

If anything fails, give the smallest false monomial or missing valuation
face and the strongest surviving statement.  End with exactly one
standalone token: `CONFIRMED`, `REPAIR`, or `REFUTED`.
