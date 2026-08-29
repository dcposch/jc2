# Hostile review charge — V87R1 repair plus V88 q15 composition

Date: 2026-08-26

Required report path (write exactly one mathematical report here):

```text
xmodel/td6-v87r1-v88-composition-hostile-review-20260826.md
```

Do not edit any producer file, addendum, ledger, coordination file, or
`jc2-lean`.  Do not treat producer PASS banners or dual-host equality as
mathematical proof.  Return one overall verdict `CONFIRMED`, `REPAIR`, or
`REFUTED`; for any non-confirmation, give the smallest failing identity or
smallest exact repair.

## Charged theorem

The original V87 hostile review returned `REPAIR` solely because V87 did not
emit an exact comparison of its q2-only specialization to the promoted,
hostile-reviewed V86 total-`(F,q2)` objects.  V87R1 claims to close exactly
that gap with output-explicit source and quotient comparisons.  V88 then
claims an exact two-sided total target-shear coordinate map making q15 an
arbitrary orbit coordinate while leaving literal raw P12/FIRST invariant.

Together, on the registered `D(U H B3)` fixed-p source component, the claimed
identity is

```text
U^12 H^3 B3
 = a_P P12_raw + sum_i a_i FIRST_i,raw
   + F h_F + sum_{e=2..14,16..24} q_e h_e,
```

with no q15 term.  Hence no DVR arc in this retained family can kill P12 and
all FIRST rows while `F` and all 22 transverse q coordinates have positive
valuation; q15 may have arbitrary valuation.  No unit theorem for the other
22 q coordinates is claimed.

## Immutable primary pins

Original V87 review:

```text
xmodel/td6-v87-total-f-allq-hostile-review-20260826.md
c4f3ea4a1de7f9675cd46029ba568d58dfe2374540d8e1d99dccc73db51ee1f4
```

Controlling repair addendum:

```text
xmodel/td6-v87-total-f-allq-hostile-review-repair-addendum-20260826.md
572c4b4c36f14a234041990cbc25f39621699888184c97b6a343c466d2215419
```

V87 producer package:

```text
cases/td6_c1_c2_c3_total_f_allq_raw_p12_source_v87tfaq_aws_20260826/
RESULT.md       6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda
EVIDENCE.sha256 074072f04a88b2e74e1545afdbdd173e8dbc0d68bd2052b6ea37ebad05e754c5
FREEZE.sha256   ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9
SOURCE.sha256   f82ebe8ef8018542c02d9cbe3654c84b2c6336f442d5e8b83633cdeebbf3e874
```

V87R1 repair package:

```text
cases/td6_c1_c2_c3_total_f_allq_v87_v86_specialization_repair_v87r1_aws_20260826/
RESULT.md       824344bc520e85621bd88455397a6ca2ad9997616055f7187b3cfc9923404089
AWS_LAUNCH.md   2796a9fd3b3e08ba3ba49078e5dc23d09bfe86b2146e57320ba67156cf0bbdf1
EVIDENCE.sha256 43d796d9b392c7c94a70af89d2e397bbc9fa7f37a3f286e342a70c6408b34cf7
FREEZE.sha256   1caf9fa6bda9f9b0a04573345866b7b9aa6fb505feed78e1df6e0809e7e85393
SOURCE.sha256   a0c4421bf52784cd949a649bb09a9045de8bb13f84c22f087245becba7967614
source.tar.gz   c7933417e0d0ad2e69a99a2a982a3a2cf2d670eecf0b018f72ac8ea402675a78
client          5227b6763aca6833c8aab117337f74c45b0be89b6112b0c35f0b6580c1143237
```

V88 producer package and design:

```text
cases/td6_c1_c2_c3_q15_total_shear_pullback_v88q15_aws_20260826/
RESULT.md       c34ae948e91b86e51a6030a93ea379e8bc570c457d3619c1e8ff57a33255a3df
AWS_LAUNCH.md   ca4d382e944c9f3fce70c028e5d9678af318e3eda31f9cf11c21beb5fe6b1616
EVIDENCE.sha256 e3ffec3f7ca1e26000ef7c5b1e4fd9aefb8fc07099af66a9eb0b4c7841c61317
FREEZE.sha256   20f9a6caafa3677db0da55a5d729bc7b45639a614b26fac46853d27c9e7445cd
SOURCE.sha256   146cebda99ee7c4264c5e1e50a3905901cd92a3d8d7005d5b908f5b6953de433
xmodel/td6-v88-q15-target-shear-total-coordinate-design-20260826.md
                 eac77fcc8dc019e5e05c4d58c5172040076daa151e16cf87bcc2245040a3f03f
```

## Required attacks

1. **Custody.** Recompute every primary pin, every V87R1
   `EVIDENCE.sha256`/`FREEZE.sha256` row, and the source archive/manifest
   correspondence.  Distinguish mathematical outputs from host metadata.

2. **Exact 39-source comparison.** Inspect
   `V87_V86_Q2_SOURCE_COMPARISON.tsv` from both AWS trees.  Confirm 1 P12 plus
   38 FIRST rows, exact keys, all non-q2 coordinates specialized to zero,
   live V87 full hashes checked against frozen V87, q2-slice hashes checked
   against frozen V86 full-beta hashes, and beta-zero hashes checked against
   frozen V86 beta-zero hashes.  Audit the serializer; do not accept shared
   source code as the comparison.

3. **Actual h outputs.** Byte-compare each emitted
   `V87_Q2_HF_CLEARED.tsv` and `V87_Q2_H2_CLEARED.tsv` with the frozen V86
   `TOTAL_F_Q2_HF_CLEARED.tsv` and `TOTAL_F_Q2_HBETA_CLEARED.tsv`.  Independently
   check the localized digests, 2,797/3,330 term counts, 50,346/59,940 scalar
   coordinates, and common clearing exactly `U*H`.  Attack hidden F/q2/q
   inversion and any serializer collision.

4. **Repair scope.** Decide whether those output comparisons close the sole
   gap in the original V87 review.  Confirm that V87R1 neither silently
   changes V87 nor adds a unit-q theorem.  If any original V87 issue remains
   controlling after this evidence, name it precisely.

5. **V88 two-sided map.** Verify on the full coefficient rectangles that
   `q_raw=q_bar+b p`, `f_raw=f_bar`, `g_raw=g_bar+b f_bar` and the subtraction
   formulas are mutually inverse integral polynomial maps with determinant
   one.  Check all 3,602 coefficient coordinates, the 976 shared f/g slots,
   all original transport rows, and the unique q15 boundary RHS.

6. **Literal receiver invariance.** Re-derive exact cancellation in FIRST and
   genuine degree-12 raw CURRENT/P12 after both the section shear and
   `q_raw'=q_bar'+15 b t^14` are installed.  Check both omission controls,
   the 39 source hashes, q15 degree zero, and absence of a q15 denominator.

7. **Composition.** Check that pulling the repaired V87 identity through the
   exact V88 map leaves `F,U,H,B3`, multipliers, source-row typing, and the 22
   transverse q coordinates unchanged and produces exactly zero q15
   remainder.  Do not replace this with a tangent or homogeneity argument.

8. **DVR consequence and firewall.** Re-derive the valuation contradiction
   on `D(U H B3)`.  Attack whether regularity of every h coefficient survives
   the pullback.  Enforce the firewall: q15 alone may be a unit; a unit among
   q2..q14,q16..q24 is not covered.  No omitted-modulus, total-Rees, whole-A3,
   TD6, SP-2, or JC2 claim is licensed.

9. **Dual AWS.** Confirm distinct hosts, `rc=0`, byte-identical mathematical
   outputs, zero swap, and that nonempty stderr consists only of successful
   `/usr/bin/time -v` telemetry.  Host agreement is custody, not proof.

The V89 unit-q/Fitting-atlas note is deliberately outside this charge and
must not be used to strengthen the theorem.
