# Hostile review assignment: H17/q7/a3 sequential grade-51 receiver

Work in `/Users/dc/code/math/jc2`.  Produce an independent hostile review
at exactly

```text
xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-sequential-g51-hostile-review-grok-20260826.md
```

Do not edit any charged artifact, producer, shared top-level ledger, or
`jc2-lean`.  Exact Q is mathematical evidence; F65521 is a software
control.  Recompute every SHA pin.  Do not infer correctness from PASS
tokens.

## Charged custody

```text
4cfbda6e3188e72460aa46d5a2d5bf95b384755d53551d883b569df00666fc7f
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/RESULT.md
735a89c01b685f3bbe03d71f0828e35bbec533bafbfd6b9c4beb860857e08c6b
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/EVIDENCE.sha256
ba04614debcc85e590f716ec966deae7d13fbd9ffbfee39f6596dd4748b88904
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/FREEZE.sha256
248b3f466451a11330f9389c29f438e65438fc018e85c77daa8b4e94d3de7cbb
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/RESULTS.sha256
44fc3d616b241047198612d0020be6217f49fe511ecb6150fa68189e1cae8d6d
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/evidence/Box03/aws_qg51seq/output/chart_reductions.json
2c1b0acda6c3244a7a60df192ebb04ebad4c3bdd7f136fde2114b78141227692
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/evidence/Box02/aws_pg51seq/output/chart_reductions.json
1e626d0832d511a2bea5936eb1d687084f51a58f7f44062af23c3f71e88318ee
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_through_g51_sparse_v5_20260826/evidence/Box03/aws_qg51/output/rows_g48_g51.json
71ff2027b1d17c421bb84738a7298eed3f8136d8f488b39ab5f9414767c2542a
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_through_g51_sparse_v5_20260826/evidence/Box03/aws_qg51/output/functionals_g51.json
e7df100dcbed28bf85e14108bb033c1663ae6334c810696e31d9927362a17f1c
  xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-grade48-predecessor-hostile-review-grok-20260826.md
```

## Required attacks

1. Independently parse/reduce the exact-Q V5 rows, without using V6's
   expected formulas.  On `D(x0*p*m*a3)` check the grade-by-grade pivots
   `P1:s0j, P3:yj, P6:d2j, P2:dmj, P4:d4j`; on `D(y0*p*m*a3)` replace
   `yj` by `xj`.  Verify every pivot is linear with a single registered
   monomial-unit coefficient and that there is no illicit inversion.
2. Check that `P5=P7=0` after reduction in grades 48,49,50 on both charts.
   Audit that all complete V5 source jets which can reach grade 51 remain
   in the input; `mu6` first occurs at 54 and `J` at 57.
3. At grade 51 independently verify, after the five pivots,
   `K51=P5_51` and `H51=16*p*P5_51+64*P7_51`.  Solve `K51=0` for `d60`
   and check exactly

   ```text
   d60=36*(r00*m^2-y0^2)/p^4
       -5*kk0*a3^2*p-2*m^3/(a3*p^4).
   ```

   Then prove or refute that `K51=P5_51=0` and the only residual is
   `64*P7_51=H51=-2*m^3*p^2+(5/4)*kk0*a3^3*p^7` on both charts.
4. Audit the custom Laurent reducer for coefficient parsing, negative
   exponents/localizations, substitution order, accidental double
   substitution, and comparison semantics.  It uses ordinary exact sparse
   dictionaries and is not affected by the quarantined Singular-qring
   equality bug.  Check F65521 only as coefficient/support reduction.
5. Audit the endpoint and scope.  A confirmation licenses finite
   prolongation through grade 51 and the receiver
   `5*kk0*a3^3*p^5-8*m^3=0` only in the fixed normalized
   `(H,q,ord(a))=(17,7,3)` graph.  It does not prove all-orders lifting,
   literal-source/total-Rees accessibility, terminal/Taylor compatibility,
   order-two, maximum-twelve, or JC2.

Start with a pin table and state reviewer/model, smallest failed identity
or missing hypothesis, and verdict `CONFIRMED`, `REPAIR`, or `REFUTED`.
Give enough exact algebra to audit both charts.  End with the verdict token
alone.
