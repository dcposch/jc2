# Fable5 hostile review — V38 graded ladder and V39 compatibility

Act as a different-model adversarial reviewer.  Review two new Sol-produced
exact claims that landed after the `20260827T0635Z` blind snapshot:

```text
97e3af988719fca94b23243652deebc3ad80dd5a51fc4978e65c0e3776f74f19
  xmodel/max12-812-order2-p0-total-rees-j2-a1-graded-ladder-v38-producer-sol-20260827.md
dbec09d2021e81549c8305bc19d0a46a00cf9721aade9a7e530b6daeec77bfd6
  xmodel/max12-812-order2-p0-total-rees-j2-a1-w19-tg19-7-compatibility-v39-producer-sol-20260827.md
```

Read both reports and every directly referenced preregistration, freeze,
compiler, validator, result, certificate, evidence manifest, erratum, and
source row needed to decide the claims.  Verify all pins before relying on
them.  Run the complete desk-scale harvest/certificate replays.  Independently
reconstruct enough exact arithmetic to avoid treating validator PASS tokens or
dual-host agreement as mathematical review; in particular, evaluate the V39
four-coordinate dual directly on the target and all 802 products, and sample
or fully rebuild V38 fixed-weight products/certificates as feasible.  Do not
run heavy CAS locally and do not use AWS.

Required verdicts:

1. V38: for all `i>=1,j>=0,5i+4j<=25`, is
   `a1^i*k^j` an exact nonmember of the homogeneous raw ordered-`a1`,
   `rho=0` ideal generated through grade 19?  Audit completeness, connected
   components, exact rank/span replay, rational duals, canonical agreement,
   schemas, relocatable evidence, the launcher erratum, and negative controls.
   Preserve the crucial distinction: W17--W19 are final at fixed weight;
   W20--W25 negatives are only relative to rows through grade 19.
2. V39: is the full 552-term `Tg19_7` outside the complete W19 ideal generated
   by the other 69 named rows?  Audit target exclusion, all-term component
   seeding, the 802-product census, exact rank 92, the four-coordinate dual,
   the 24-term residual, external coefficient-deletion control, and evidence
   custody.  Preserve ordinary unsaturated scope: no radical,
   `a1`-saturation, honest chart, Rees, Gate-T, or JC2 inference.
3. Check consistency with the exact rank-two symbol report
   `xmodel/max12-812-order2-p0-total-rees-j2-a1-first-occurrence-symbol-spencer-design-sol-20260827.md`
   and with the V37 erratum.  Explain what V39 adds and what V38 rules out;
   do not infer nonemptiness from nonmembership.
4. For each material claim return `CONFIRMED`, `REFUTED`, or `GAP`, with the
   exact attack and any necessary scope amendment.  State whether either
   artifact is promotion-ready under the campaign's different-model rule.

Do not browse.  Do not edit any campaign artifact except the output report.
Do not read, enter, build, inspect status of, edit, stage, clean, or otherwise
touch `jc2-lean`.  Write the complete review to:

`xmodel/max12-812-order2-p0-total-rees-j2-a1-v38-v39-hostile-review-fable5-20260827.md`

End with a file/tool/edit disclosure.
