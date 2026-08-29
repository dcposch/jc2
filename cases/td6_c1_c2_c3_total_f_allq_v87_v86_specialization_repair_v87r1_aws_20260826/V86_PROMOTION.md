# Promotion: TD6 literal total-`(F,q2)` raw-source identity

Date: 2026-08-26

Status: **PROMOTED AFTER CORRECTED DIFFERENT-MODEL HOSTILE REVIEW.**

## Charged evidence

```text
22fb1c6c437e26f212a38857157050f68e773dcee8482e3d384da47fffc09c02
  cases/td6_c1_c2_c3_total_f_q2_raw_p12_source_v86tfq2_aws_20260826/RESULT.md
492117581f014bdc60bc13262a4d6ae89c478646c9f4a79b1db29206e1bcf94e
  cases/td6_c1_c2_c3_total_f_q2_raw_p12_source_v86tfq2_aws_20260826/EVIDENCE.sha256
82083dd26b44766779beb2fec64e34f0842769a8f81fe73aee1f105cb8510c79
  cases/td6_c1_c2_c3_total_f_q2_raw_p12_source_v86tfq2_aws_20260826/FREEZE.sha256
d86ec28236b9b97746150d04b3a0891ec05f5bc6eed02e78fc02b0f864d221f6
  cases/td6_c1_c2_c3_total_f_q2_raw_p12_source_v86tfq2_aws_20260826/SOURCE.sha256
9e70d6ceef3572cecada81160357684c8478fb8994cfe7d6176793d58ca1532e
  xmodel/td6-v86-total-f-q2-hostile-review-grok-v2-20260826.md
```

The first review assignment paired the freeze digest with the wrong manifest
path and was cancelled without a verdict.  The corrected assignment rehashed
every charged pin and independently recovered the algebra; its verdict is
**CONFIRMED**.

## Promoted identity

On the normalized three-center literal source slice with

```text
q=t+beta*t^2+t^25,
F=C*U-V^2+U^3,
H=C-3*U^2,
```

the genuine raw degree-twelve polynomial and all 38 packed FIRST maps obey

```text
U^12*H^3*B3
  = aP*P12(C,V,U,beta)
    + sum_i ai*FIRST_i(C,V,U,beta)
    + F*hF + beta*hbeta
```

in the localization of `Q[C,V,U,beta]` by `U*H*B3`.  The coefficient ring
in `beta` is untruncated.  Both live beta paths are retained: the affine
transport source and `q'=1+2*beta*t+25*t^24`.  The common denominator is
`U*H`; neither `F` nor `beta` is inverted.  The cleared `hF` is the frozen
V85 quotient, and the cleared `hbeta` has beta degree zero.

Consequently, on `D(U*H*B3)`, no DVR arc in this literal family can kill all
raw P12/FIRST rows while satisfying both `v(F)>0` and `v(beta)>0`: the left
side is a unit and every term on the right has positive valuation.

## Firewall

This theorem covers only the simultaneous positive-`F`, positive-`q2` locus
of the displayed literal normalized slice.  It does not cover unit-`q2`
fibres, other `q` jets, dead stretch, correction, orbit/pole, centering,
boundary moduli, a full total-Rees chart, whole fixed A3, TD6, SP-2, or JC2.
The all-`q` V87 successor is independent and remains in computation.
