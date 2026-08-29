# Promotion: TD6 high-q total-`F` K-repaired unit identity

Date: 2026-08-26

Status: **PROMOTED AFTER DIFFERENT-MODEL HOSTILE REVIEW.**

## Frozen custody

```text
8db237a7c466b420060623576b9d778427392fd827a3af856d276707dd618546
  cases/td6_c1_c2_c3_high_q_total_f_k_repair_v89h4_aws_20260826/RESULT.md
70625a4460778bab5b14ae736b548c963952f5ce052819f6491928ef1a08340d
  cases/td6_c1_c2_c3_high_q_total_f_k_repair_v89h4_aws_20260826/EVIDENCE.sha256
3406db430e1a23bae2e3755f5dca3135773aced2af032c621ae1bbc0e28c3721
  cases/td6_c1_c2_c3_high_q_total_f_k_repair_v89h4_aws_20260826/FREEZE.sha256
c9f6b7078bfbf8b0bdd3df71e50e54303b36d88c25e748b2802a7cdab48bc842
  cases/td6_c1_c2_c3_high_q_total_f_k_repair_v89h4_aws_20260826/SOURCE.sha256
ea95d613822b72e3438df42078926f006c0e3501bedd2cd7ab4177eb01de8387
  xmodel/td6-v89h4-high-q-total-f-k-repair-hostile-review-grok-v2-20260826.md
```

The first Claude review deployment terminated immediately at its API usage
limit and made no mathematical finding.  The immutable assignment was
relaunched through Grok 4.6.  That review rehashed all charged custody,
independently replayed the coefficient identities and multiplier table, and
returned **CONFIRMED**.

## Promoted theorem

On the literal normalized high-q residue block

```text
q2=...=q14=0,
q15 absent under the reviewed target shear,
q16,...,q24 independent and untruncated,
```

let

```text
F  = C*U - V^2 + U^3,
H  = C - 3*U^2,
G  = 2*C*U - V^2 + 2*U^3,
K  = 2*C*V^2*U + 16*C*U^4 - V^4 - 14*V^2*U^3 + 16*U^6.
```

The genuine raw degree-twelve P12 and all 38 packed raw FIRST maps satisfy
the exact identity

```text
(1/8)*B3^2*U^2*H^2
  = a_P*P12_raw + sum_i a_i*FIRST_i,raw + F*(2*A*G),
A = (1/8)*B3*U^2*H^2,
```

in the localization of the untruncated polynomial coefficient ring by
`U*H*B3`.  The 2,651 nonzero multiplier coordinates are the frozen table.
Their final common denominator is `U*H`.

The construction first clears the sole unregistered denominator factor
`K`, whose exponent is exactly one, and then uses

```text
B3 = K + 2*F*G
```

coefficientwise.  Neither `K`, `F`, nor any q polynomial is inverted.  The
left side is a unit on `D(U*H*B3)`, so `(P12_raw,FIRST_raw,F)` is the unit
ideal on exactly this high-q residue block.  Omitting P12, the charged FIRST
source, or F breaks the displayed identity.

Equivalently, no DVR arc in this retained literal family can kill raw P12
and all raw FIRST rows while `F` has positive valuation.

## Firewall

This is a total-`F` theorem and explicitly not a P12/FIRST-only collapse.
It sets every `q2,...,q14` to zero and therefore supplies no low-q unit-chart
cover.  It does not cover an independent q15 source modulus, total-Rees or
source lifting, omitted correction, orbit/pole, moving-center, deck/torsion,
or other boundary variables.  It is not a source point, whole fixed A3,
TD6, SP-2, or JC2 theorem.
