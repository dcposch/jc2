# Erratum: P3 raw-curve origin certificate band

This note corrects one mechanism label in the immutable P3 raw-curve
producer package.  It does not mutate the frozen case or its charged report.

The frozen case README says that the raw center origin was

> proved it first-band inconsistent with a unit chart

and the charged report says it was

> killed by a unit-chart first-band certificate.

Both uses of **first-band** are wrong.  The cited immutable origin output

```text
cases/td6_c1_c2_c3_trivariate_checkpoint_20260825/evidence/v14/origin.stdout
```

(SHA-256
`c31a0f60eef078150bf7dd59878456fd332d55273181635d5ead11da52f0fc18`)
proves a **transport-band** incompatibility: transport rank `3468/3602`, one
incompatibility, a 21-original-row certificate with unit chart and exact
original-row replay, and
`first_band_and_P12_skipped_transport_empty=true`.  Thus the corrected
sentence is:

> The raw center origin was proved transport-inconsistent by a separately
> frozen 21-original-row unit-chart certificate.

The correction strengthens the timing of the obstruction and changes no
set-theoretic conclusion, hypothesis, exceptional locus, or scope.  In
particular, the decomposition
`{H=P3=0}={H=P3=0,U!=0} union {C=V=U=0}` and the whole-curve conclusion remain
valid.

The hostile review
`xmodel/td6-c1-c2-c3-p3-raw-curve-review-claude-20260825.md` independently
identified this wording defect and returned **CONFIRMED**.  The immutable
bytes being corrected are:

- case README SHA-256
  `6ff987876fc8ec5eb8307517a282710bc4f8070ae8067260ed5bd2602a8e80da`;
- charged report SHA-256
  `a15c85c5bfd2a4219c2f7540b5e2577f5af123c18b40483a2749118c5ac2bcab`;
- hostile review SHA-256
  `def9c7392f156b88252e5f143af505aa684e1135bc99b7beb5ff203d2238788c`.

Strict scope is unchanged: the fixed source-typed normalized three-center
TD6 section only; no neighborhood, full-centering, boundary/dead-stretch,
SP-2, or JC2 claim.
