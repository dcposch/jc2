# TD6 q2-beta raw `U=0` scope erratum

## Verdict

**NONMUTATING THEOREM-SCOPE CORRECTION.**  The frozen V33/V69 algebra gives
an exact first-band unit incompatibility only on

```text
U=0 and C!=0
```

inside the fixed source-typed normalized A3 q2-beta section.  It does not
prove the whole raw divisor `U=0` empty.  Hostile review
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-review-grok-20260825.md`, SHA-256
`706f6ad408e680de1b0bb1d9b23c10e49829ab803a9bf06553253e4231b2e291`,
returned `CONFIRMED_WITH_REPAIRS` and identified the exact omitted
localization.

## Exact defect and surviving theorem

The V33/V69 raw specialization retains `C,V` and sets `U=0`.  Its transport
rank is `3470/3602`; the first system has rank `36/132` and unique dependent
original row `('X-2',14)`, with a 14-row original-source combination,
beta-degree-zero residual, and monic compatibility gcd one.  Those facts and
V69's canonical digest repair survive.

However, the transport elimination accepts two nonconstant pivots:

```text
transport_event[0] ... num=(-C)
transport_event[1] ... num=(-C)
```

so its transport chart is `D(C^2)`.  The producer's displayed
`first_compatibility_certificate_denominator=(1)` included only the
residual, Bezout, and first-row combination denominators.  It omitted the
transport chart (and therefore was not a complete parent-style
denominator).  At `C=0` both pivots vanish and the old echelon cannot be
specialized.

Accordingly, these frozen sentences are withdrawn:

- V33 report/README: “the entire raw `U=0` center divisor is empty” and
  “complete certificate denominator = 1” as a complete chart claim;
- V69 report/README: “the raw `U=0` divisor is empty for every `beta`”;
- the earlier N13-localization erratum sentence “The all-beta `U=0` theorem
  remains valid.”

They are replaced by: the fixed A3 q2-beta source is inconsistent on
`U=0,D(C)` for every beta.  The raw intersection `C=U=0`, named
`u-h-zero`, is a separate source-rebuild obligation; if its chart inverts
`V`, the origin `C=V=U=0` is a further separate leaf.

## Dependency quarantine

No frozen bytes are changed.  Until the raw exceptional leaves are rebuilt
and reviewed, every all-beta composition that used V33/V69 as a
whole-`U=0` theorem is quarantined, including:

- the parameter-zero endpoints in the all-beta rational-line and N13
  exceptional-curve packages;
- the `U=0`/origin endpoints in the all-beta B3 chart cover and V68 route
  composition (the V68 route equalities themselves survive);
- the asserted all-beta whole-`H=0`, whole-`B3=0`, and fixed-A3 unions.

The narrow direct theorems on their own stated opens remain evidence.  In
particular, this erratum does not alter V64 on
`H=0,D(U*V*P3*QH)`, V62D on `V=H=0,D(U)`, or the older separately stratified
beta-zero trivariate atlas.  It only withdraws downstream coverage that
specifically consumed the overbroad V33/V69 all-beta conclusion.

## Repair gate

The raw `u-h-zero` producer must rebuild original transport rows at
`C=U=0`, retain polynomial beta and direct
`q_beta'=1+2 beta t+25 t^24`, print every transport event, compose the full
transport/source/combination/residual denominator, and replay its
incompatibility against original rows with a wrong-row or omission control.
It must run from byte-identical source on two AWS hosts.  Every remaining
denominator-zero leaf, including the origin if `V` is inverted, must be
rebuilt rather than specialized from a fraction field.  Hostile review is
required before restoring any whole-divisor composition.

No whole A3, other TD6 modulus, TD6, SP-2, landing, or JC2 conclusion follows.
