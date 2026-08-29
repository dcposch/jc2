# Hostile review assignment: H17 upper affine-graph load unit

Work in `/Users/dc/code/math/jc2`.  Write an independent hostile review at

```text
xmodel/max12-812-order2-affine-faber-a-h17-upper-graph-load-unit-hostile-review-grok-20260826.md
```

Do not edit charged artifacts, producers, shared ledgers, or `jc2-lean`.
Recompute every SHA before reading verdict prose.  Exact Q is evidence;
F65521 is a software control only.

## Charged custody

```text
773b4d773cee9cc967645b6c67417d7d60c3058d2e5ae898f06d12b4863800fc
  xmodel/max12-812-order2-affine-faber-a-h17-upper-graph-load-unit-theorem-20260826.md
37d43ffdf7098028e02a79509461b6e06777e203ab04b57ee1d0c5f3801d5f57
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/RESULT.md
b9c11be5a6821d31826a947f8c73562c1f6447423894d2718ff7020fb178e909
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/EVIDENCE.sha256
7b2534e945398a31e8ce5111786e0bad45fc0ca125354178242189de4227891c
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/FREEZE.sha256
34d701dc7b33125774a89a11e47bd1284c21f8650cffaaf085c14e589f189553
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/RESULTS.sha256
ae18b65c01e0b7381c6944754a1bb9690ed006255a922399716ef2cc99bc550e
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/evidence/Box02/aws_qgraph/output/hseries_affine_graph_support.json
```

## Required attacks

1. Independently redo the exact polynomial substitution
   `K6=(15/32)K10E^2`, `K2=(15/256)K10E^4` in the complete Hseries support.
   Confirm 468 terms and coefficient `5/4` of `K10*a^3*E^7`.
2. Compare every reduced affine weight under H17.  Confirm or refute that
   this load monomial is uniquely least exactly on `7<q<17/2`, and that at
   `q=7` only it and `-2lambda^3M^3E^2` tie.
3. Audit the positive-deviation composition.  With
   `K6=t^42((15/32)kappa E^2+d6)` and similarly for K2, check whether
   `v(d6),v(d2)>0` really forces every deviation-bearing expansion term to
   have strict excess, including terms created by central cancellation.
4. Check raw-row functional signs, target/load completeness, rational
   ramification, unit localization `D(kappa*a*E)`, and whether moving E/a
   jets can tie the initial term.
5. Keep scope internal: no literal source/total-Rees access, q=7 boundary,
   factor-degenerate, whole order-two, max12, or JC2 upgrade.  State the
   strongest licensed theorem and smallest defect if any.

Begin with a verdict table and end with exactly one token on its own line:
`CONFIRMED`, `REPAIR`, or `REFUTED`.
