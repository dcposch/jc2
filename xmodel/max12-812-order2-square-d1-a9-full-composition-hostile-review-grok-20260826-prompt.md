# Hostile review: complete D1 `a=9` composition through grade 30

Work in `/Users/dc/code/math/jc2`.  This is an adversarial, read-only
mathematical review.  Do not trust PASS markers, producer prose, or finite-field
agreement.  Write exactly one report to

```text
xmodel/max12-812-order2-square-d1-a9-full-composition-hostile-review-grok-v3-20260826.md
```

Edit no other file and do not touch `jc2-lean`.  Independently rehash and inspect
the frozen source compiler, both exact-Q and `F_65521` compiled scripts, stdout,
metadata, and all cited ancestors.  Exact Q is the theorem endpoint;
`F_65521` is only an independent implementation control.

## Charged endpoint custody

```text
bbb1d718a08247d7ff344033e51c988ee52f7ae88a19e98cb059b0ebd8d7cf1c
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade30_c2_obstruction_20260826/RESULT.md
dc223883009026a2e242735563170a51f081b0c049a966751521e4fff8396f52
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade30_c2_obstruction_20260826/EVIDENCE.sha256
6881229bb9d8f89fe1be3314a7e7a8b654cf2e8f7f101a9b6a5936add1ba3570
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade30_c2_obstruction_20260826/FREEZE.sha256
```

The prior `D(k60)` result and its different-model review are:

```text
3679d0dbd883c74a4d1d7d1175daf9461c123dd83272bdf2e713ebd7c3412a88
  cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_v2_target_precedence_20260826/RESULT.md
95e9990bca73d42c2b4ba513ee4bf95acfe9ad6dfbd3d461ab67201a7b2f943e
  xmodel/max12-812-order2-square-d1-a9-k60-grade27-hostile-review-grok-20260826.md
```

Also charge the corrected source census and the grade-28--29 `V(k60)` collision:

```text
cases/max12_812_order2_square_owner_d1_a9_source_support_census_v3_parenthesized_loads_20260826/
cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade28_29_collision_v2_syntax_20260826/
```

## Audit charges

Independently rederive enough of the seven literal Faber rows to decide every
item below.  If a claim fails, exhibit the smallest explicit wrong identity,
missing monomial/variable, or invalid localization step.

1. **Ancestry and source completeness.**  Verify the corrected recursive source
   inventory, its grade convention, the parenthesized rational loads, and that
   every source through grade 30 is present.  Verify that the full grade-27--30
   ideal on `V(k60,k60_1)` equals, *before radicals*, the compact ideal
   ```text
   (k60,k60_1,mu20,e29z,e29c,g30_1,g30_2,
    c1*c0,2*c0^2-p*c1^2).
   ```
   Check both containments by exact polynomial reduction, not by comparing only
   radicals, dimensions, or sampled points.

2. **Grade-28--29 collision.**  Check the exact four source equations
   ```text
   e28z=(3/4)c1*k60_1
   e28c=(3/4)c0*k60_1-mu20
   e29z=(3/4)(a0*c1+a1*c0+c1_1*k60_1+c1*k60_2)
   e29c=-(3/8)p*a1*c1+(3/4)a0*c0
         +(3/4)c0_1*k60_1+(3/4)c0*k60_2-mu20_1
   ```
   and the claimed moving-connection dependencies in rows 3, 5, and 7.

3. **Hand-derived grade-30 invariant.**  Recompute signs and coefficients in
   ```text
   g30_3+(p/4)g30_1+(ell1/2)e29z=(3/4)c1*c0
   g30_4=(3/16)(2*c0^2-p*c1^2)
   g30_5=-(p^2/32)g30_1-(p*ell1/8)e29z-(3/16)p*c1*c0
   g30_6=0
   g30_7=-(p^3/128)g30_1-(3*p^2*ell1/64)e29z
         -(3/128)p^2*c1*c0.
   ```
   Check that these are identities in the exact-Q quotient actually claimed,
   and not identities obtained only after silently discarding a correction.

4. **All loads and targets.**  Trace every grade-30 contribution from higher
   normal jets, moving-connection corrections, delayed `k20`, `k0_1`,
   `k60_4`, and all timed `mu4`, `mu6`, and `J` target jets.  Confirm that the
   compiler has not set a variable to zero before its legal time, conflated a
   load with a target, or omitted a term that changes the compact ideal.

5. **Exhaustive successor split.**  Verify that `D(k60_1)` and `V(k60_1)` are
   scheme-theoretically exhaustive after `V(k60)`.  Explicitly decide whether
   an intermediate valuation/contact stratum over a DVR is missed by this
   open/closed split.

6. **Exact-contact localization.**  Audit both claimed contradictions without
   replacing exact contact by a mere nonzero coefficient:
   - on `D(k60_1)`, `e28z` gives `c1=0`, `g30_4` gives `c0^2=0`, and the exact
     contact equation/Bezout localization must make the ideal the unit ideal;
   - on `V(k60_1)`, `c1*c0=0` and `2*c0^2-p*c1^2=0` on `D(p)` give cubic
     nilpotence of both `c0,c1`, and the exact-contact equation must again make
     the ideal the unit ideal.
   Check this over arbitrary characteristic-zero residue extensions and
   ramified DVRs.  Flag any misuse of “nonzero,” “unit,” “unimodular pair,”
   radicalization, or projective-chart coverage.

7. **Controls.**  Confirm exact-Q evidence really ran the frozen compiled input,
   the finite-field lane is independent enough to detect translation/software
   errors, and the Chebyshev/Pell positive control is genuinely nonempty rather
   than vacuous.

8. **Composition and scope.**  Decide whether the reviewed `D(k60)` grade-27
   obstruction plus the new exhaustive `V(k60)` analysis proves precisely:
   for the seven literal Faber source rows, after the cited upstream square/D1
   gates, the fixed D1 contact cell
   ```text
   ord_sigma(A)=9, ord_sigma(C)=10, ord_sigma(R)>=9
   ```
   is empty on `D(p*k0)` in characteristic zero.  The firewall must remain:
   this says nothing by itself about `a>=10`, `p=0`, `k0=0`, other D1 cells,
   the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

Give a compact audit trail including recomputed identities and exact hashes.
End with exactly one standalone token: `CONFIRMED`, `REPAIR`, or `REFUTED`.
