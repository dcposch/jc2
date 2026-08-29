# Promotion: TD6 total-`(F,q)` identity with arbitrary q15 shear

Date: 2026-08-26

Status: **PROMOTED AFTER REPAIR AND DIFFERENT-MODEL HOSTILE REVIEW.**

## Frozen custody

```text
6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda
  cases/td6_c1_c2_c3_total_f_allq_raw_p12_source_v87tfaq_aws_20260826/RESULT.md
074072f04a88b2e74e1545afdbdd173e8dbc0d68bd2052b6ea37ebad05e754c5
  cases/td6_c1_c2_c3_total_f_allq_raw_p12_source_v87tfaq_aws_20260826/EVIDENCE.sha256
ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9
  cases/td6_c1_c2_c3_total_f_allq_raw_p12_source_v87tfaq_aws_20260826/FREEZE.sha256
824344bc520e85621bd88455397a6ca2ad9997616055f7187b3cfc9923404089
  cases/td6_c1_c2_c3_total_f_allq_v87_v86_specialization_repair_v87r1_aws_20260826/RESULT.md
43d796d9b392c7c94a70af89d2e397bbc9fa7f37a3f286e342a70c6408b34cf7
  cases/td6_c1_c2_c3_total_f_allq_v87_v86_specialization_repair_v87r1_aws_20260826/EVIDENCE.sha256
1caf9fa6bda9f9b0a04573345866b7b9aa6fb505feed78e1df6e0809e7e85393
  cases/td6_c1_c2_c3_total_f_allq_v87_v86_specialization_repair_v87r1_aws_20260826/FREEZE.sha256
c34ae948e91b86e51a6030a93ea379e8bc570c457d3619c1e8ff57a33255a3df
  cases/td6_c1_c2_c3_q15_total_shear_pullback_v88q15_aws_20260826/RESULT.md
e3ffec3f7ca1e26000ef7c5b1e4fd9aefb8fc07099af66a9eb0b4c7841c61317
  cases/td6_c1_c2_c3_q15_total_shear_pullback_v88q15_aws_20260826/EVIDENCE.sha256
20f9a6caafa3677db0da55a5d729bc7b45639a614b26fac46853d27c9e7445cd
  cases/td6_c1_c2_c3_q15_total_shear_pullback_v88q15_aws_20260826/FREEZE.sha256
c4f3ea4a1de7f9675cd46029ba568d58dfe2374540d8e1d99dccc73db51ee1f4
  xmodel/td6-v87-total-f-allq-hostile-review-20260826.md
572c4b4c36f14a234041990cbc25f39621699888184c97b6a343c466d2215419
  xmodel/td6-v87-total-f-allq-hostile-review-repair-addendum-20260826.md
068b33a797c81187dd375fb2ba83cae32cd7cf74c6acbaaa1689abf5bf8240df
  xmodel/td6-v87r1-v88-composition-hostile-review-20260826.md
```

The first V87 review found no algebraic defect but required an exact
coefficientwise q2-specialization comparison to the promoted V86 theorem.
V87R1 supplied that comparison for all 39 sources and both cleared quotient
tables.  The fresh review independently confirmed the repair and the V88
composition.

## Promoted identity

On the registered normalized three-center, fixed-`p=t^15` literal source
slice and on `D(U*H*B3)`, put

```text
E={2,...,14,16,...,24}.
```

Literal raw degree-twelve P12 and all 38 packed raw FIRST maps satisfy

```text
U^12*H^3*B3
 = a_P*P12_raw + sum_i a_i*FIRST_i,raw
   + F*h_F + sum_{e in E} q_e*h_e.                 (1)
```

All quotient coefficients are regular in the registered localization; the
common clearing is `U*H`, and neither `F` nor a q coordinate is inverted.

The omitted coefficient `q15=b` is an exact target-shear coordinate.  The
two-sided integral map

```text
q_raw=q_bar+b*p,  f_raw=f_bar,  g_raw=g_bar+b*f_bar
```

and its subtraction inverse have determinant one on all 3,602 section
coordinates.  With the corresponding derivative term installed, raw P12
and every FIRST row are exactly b-independent, so (1) has zero q15
remainder.

Consequently no DVR arc in this retained family can kill P12 and all FIRST
rows while `F` and every one of the 22 transverse coordinates `q_e`,
`e in E`, have positive valuation.  The valuation of q15 is arbitrary,
including zero.

## Firewall

This promotion supplies no unit theorem for `q2..q14,q16..q24`.  It does
not cover dead stretch, correction, orbit/pole, moving centers, deck/torsion,
other boundary moduli, a total-Rees chart, whole fixed A3, TD6, SP-2, or
JC2.  V89 remains a successor design.

