# Hostile review: H17/q7/a3 normalized formal Kummer lift

Work in `/Users/dc/code/math/jc2`.  Write the unique report

```text
xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-normalized-formal-kummer-lift-hostile-review-grok-20260826.md
```

Do not edit any charged artifact, shared ledger, or `jc2-lean`.

Charged theorem:

```text
8af6d72e0044314ca091c4ae0d74876f57ba718a572ccde6f32a597fa2e41a97
  xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-normalized-formal-kummer-lift-theorem-20260826.md
```

Reviewed finite dependencies:

```text
e7df100dcbed28bf85e14108bb033c1663ae6334c810696e31d9927362a17f1c
  xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-grade48-predecessor-hostile-review-grok-20260826.md
465f53cd423d94645f0b99f4e96d18853bb469b96dc2f85590dc7fe912d158ec
  xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-sequential-g51-hostile-review-grok-20260826.md
4cfbda6e3188e72460aa46d5a2d5bf95b384755d53551d883b569df00666fc7f
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/RESULT.md
```

Rehash every pin.  Independently audit:

1. that the displayed normalized coordinate series define complete formal
   row functions and the first five divided equations have exactly the
   stated unit triangular Jacobian on both projective charts;
2. that after the first implicit block, `K,H` are divisible by `t^51`, and
   the second Jacobian in `(d6,kappa)` has diagonal
   `(-a3*p^5/32,5*a3^3*p^7/4)`;
3. the full determinant, including sign and powers of `a3,p,m,x/y,2`;
4. the logical all-orders step: substitution of the first formal graph,
   coefficient recursion/completeness, uniqueness, and freedom to prescribe
   `mu6` and a unit-leading determinant target at weight 57;
5. whether the constant Kummer receiver and `d6(0)` formulas are exactly
   those proved by the finite review; and
6. scope: normalized complete-local graph only.  Do not import literal
   source/Rees, Taylor, order-two, max12, or JC2.

Try to falsify the claim by finding an omitted target, a nonanalytic
division, a future-jet/lookahead dependence, or a Jacobian that is only a
finite-truncation artifact.  Start with a pin/verdict table, state the
smallest failed identity or missing hypothesis, and end with exactly one
standalone token `CONFIRMED`, `REPAIR`, or `REFUTED`.
