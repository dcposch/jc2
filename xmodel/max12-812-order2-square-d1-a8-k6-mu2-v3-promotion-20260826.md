# Promotion: generic-square D1 contact `a=8`

Date: 2026-08-26

Status: **PROMOTED — HOSTILE REVIEW CONFIRMED.**

## Frozen authority

- producer result:
  `cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_v3_k60count_20260826/RESULT.md`,
  SHA-256
  `67e0c08119e67d410904e63f55b5586131bfa987e4b7d7045c02e24dd6a2e9a7`;
- evidence manifest: same case, `EVIDENCE.sha256`, SHA-256
  `a3a64018a350a61b02ea53aec7edbd56e159eb8def325d78d05fbd59ecb1effb`;
- source freeze: same case, `FREEZE.sha256`, SHA-256
  `dcd6c3eb2d390375f1c56bc638215a4e447efe680a4c5f345c18011945514f7f`;
- independent hostile review:
  `xmodel/max12-812-order2-square-d1-a8-k6-mu2-v3-hostile-review-grok-20260826.md`,
  SHA-256
  `b5944e1582a2df9ff37224bd7c5875520321f0ee0998c63c8ceeeedfbb66bba2`,
  verdict **CONFIRMED**.

Every path named by the source and evidence manifests rehashed in the
review.  Exact Q on Box03 and the independent `F_65521` control on r6d both
returned engine `rc=0`, passed their fail-closed validators, and recorded
zero swap.

## Promoted statement

Assume the already reviewed generic-square first-normal, half-weight, and
`M=0` gates.  On `D(p*k10)`, no finite-order normalized source arc has the
fixed contact

```text
ord(A)=8,  ord(C)=9,  ord(R)>=8.
```

The complete seven-row Faber/source calculation exhausts the leading `k6`
jet in two sections.

1. On `D(k60)`, the grade-26 simple pole
   `[(3/4)k60*C0/L]_-` forces `C0=0`, contrary to the registered contact.
2. On `V(k60)`, with
   `k6=sigma*k61+sigma^2*k62+...`, grades 27 and 28 retain the moving
   Laurent-to-Faber connection, the `k10*R*C/L` term, the complete `k6*C`
   module, and the inverse-Faber `mu2` target.  The first numerator is
   `C0(A0+k61)`.  Both root allocations of squarefree
   `L=z^2+p/2` leave the nonzero next residue
   `(3/2)lambda^2*cv^2`; the residual face
   `A0+k61 identically 0` is killed by the same double-pole numerator.

Thus the two `k6` sections admit no arc in this fixed contact.  The result is
arcwise and set-theoretic; it does not assert reduced scheme structure.

## Firewall

This promotion proves exactly the fixed `a=8` contact statement above.  It
does **not** cover `a>=9`, positive-order `k10`, `p=0`, `k10=0`, any other
valuation face, zero/infinity receivers, the whole square branch, exact
order two, `(8,12)`, maximum twelve, or JC2.  It does not contradict the
tied-load Chebyshev/Pell survivor.  The corrected `a=9` source-support
census is navigation for the next receiver, not an `a=9` theorem.
