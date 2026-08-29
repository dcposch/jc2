# Controlling repair addendum — V87 total-F/all-q review and V88 q15 pullback

Date: 2026-08-26

Status: **producer-tier repair complete; fresh hostile composition review
required before promotion.**

## Review controlled by this addendum

The independent report

```text
xmodel/td6-v87-total-f-allq-hostile-review-20260826.md
SHA-256 c4f3ea4a1de7f9675cd46029ba568d58dfe2374540d8e1d99dccc73db51ee1f4
```

returned `REPAIR`.  It found no failing identity in the represented V87
all-q certificate.  Its sole controlling gap was the absence of an exact,
output-explicit comparison between the V87 q2-only specialization and the
promoted, hostile-reviewed V86 total-`(F,q2)` source and quotient artifacts.
Shared code and equal term counts were expressly insufficient.

## Exact smallest repair

The frozen repair package is

```text
cases/td6_c1_c2_c3_total_f_allq_v87_v86_specialization_repair_v87r1_aws_20260826/
```

with primary pins

```text
RESULT.md       824344bc520e85621bd88455397a6ca2ad9997616055f7187b3cfc9923404089
AWS_LAUNCH.md   2796a9fd3b3e08ba3ba49078e5dc23d09bfe86b2146e57320ba67156cf0bbdf1
EVIDENCE.sha256 43d796d9b392c7c94a70af89d2e397bbc9fa7f37a3f286e342a70c6408b34cf7
FREEZE.sha256   1caf9fa6bda9f9b0a04573345866b7b9aa6fb505feed78e1df6e0809e7e85393
SOURCE.sha256   a0c4421bf52784cd949a649bb09a9045de8bb13f84c22f087245becba7967614
source.tar.gz   c7933417e0d0ad2e69a99a2a982a3a2cf2d670eecf0b018f72ac8ea402675a78
client          5227b6763aca6833c8aab117337f74c45b0be89b6112b0c35f0b6580c1143237
```

Two exact AWS clients rebuilt live V87 P12, all 38 FIRST maps, `h_F`, and
`h_2`; set all non-q2 coordinates to zero; and compared them under the V86
serializer.  Both clients returned `rc=0` and byte-identical mathematical
evidence.  The emitted evidence is:

```text
39-row source comparator  e60173b3e8f224d6fab09f0ef3a831c846a27137718ba1d188d08b009453fae4
actual cleared h_F table  89ecec18cea6547fe465fc4f6088f7f94ec9b6d717eefb33386f5b3fab6d49e0
actual cleared h_2 table  590f88a20183a4d4363a4e14397084cae347838331abc6df536f60129f2f0384
exact result record       64147317dedd7c79a64e7ee95875c966e5f82c5e2232db721c876fa1c4d3749c
mathematical stdout       c0104ec08b10e9349ca4b4fa8267eb858785a4b5da45e7ac0a0e654be6f9d4f1
```

Every V87 q2 source slice equals frozen V86, coefficientwise under the
documented digest serializer.  The actual V87 cleared quotient tables are
byte-identical to the frozen V86 `h_F` and `h_beta` tables.  The common
clearing is exactly `U*H`; no F, q2, or q expression is inverted.  The
repair pins the corrected V86 hostile review `9e70d6ce...` and promotion
`677513a2...` as dependencies.

This is exactly the smallest repair requested.  It controls the original
review's sole `REPAIR` item, subject to the fresh independent review below.
It changes no V87 algebra and adds no unit-q claim.

## V88 composition

The independently frozen V88 producer package is

```text
cases/td6_c1_c2_c3_q15_total_shear_pullback_v88q15_aws_20260826/
```

with pins

```text
RESULT.md       c34ae948e91b86e51a6030a93ea379e8bc570c457d3619c1e8ff57a33255a3df
AWS_LAUNCH.md   ca4d382e944c9f3fce70c028e5d9678af318e3eda31f9cf11c21beb5fe6b1616
EVIDENCE.sha256 e3ffec3f7ca1e26000ef7c5b1e4fd9aefb8fc07099af66a9eb0b4c7841c61317
FREEZE.sha256   20f9a6caafa3677db0da55a5d729bc7b45639a614b26fac46853d27c9e7445cd
SOURCE.sha256   146cebda99ee7c4264c5e1e50a3905901cd92a3d8d7005d5b908f5b6953de433
design          eac77fcc8dc019e5e05c4d58c5172040076daa151e16cf87bcc2245040a3f03f
```

V88 emits mutually inverse integral polynomial maps on all 3,602 global
section coefficients,

```text
q_raw=q_bar+b*p,
f_raw=f_bar,
g_raw=g_bar+b*f_bar,

q_bar=q_raw-b*p,
f_bar=f_raw,
g_bar=g_raw-b*f_raw,
```

with `p=t^15` and `b=q15`.  The maps have triangular determinant one and
introduce no denominator.  Exact transport replay finds the single added
boundary source `('g','X',0,15)=b`.  Including both section shear and direct
`15*b*t^14` in `q_raw'` makes literal raw P12 and all 38 raw FIRST maps
exactly b-independent; either omission changes 15 FIRST rows.  Thus pulling
the repaired V87 identity back gives

```text
U^12 H^3 B3
 = a_P P12_raw + sum_i a_i FIRST_i,raw
   + F h_F + sum_{e=2..14,16..24} q_e h_e,
```

with no q15 remainder.

## Narrow consequence after repair and composition

On the same fixed-p normalized three-center source component and registered
open `D(U H B3)`, no DVR arc can kill literal raw P12 and all raw FIRST rows
while `F` and every one of the 22 transverse q coordinates have positive
valuation.  The q15 target-shear coordinate is arbitrary, including a unit.

This conclusion still does not cover a unit among the other 22 q
coordinates, dead stretch, correction, F1-orbit/pole, moving centers,
deck/torsion, other boundary data, a complete total-Rees chart, whole fixed
A3, TD6, SP-2, or JC2.  The V89 projective/Fitting-atlas document is a
successor design only and is not imported into this repaired theorem.
