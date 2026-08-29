# V24R6R1 exact six-leading-variable D(W) result

Date: 2026-08-27

Status: **PRODUCER PASS; PROVISIONAL PENDING INDEPENDENT HOSTILE REVIEW.**

## Exact result

In

```text
Q[x0,x1,x2,x3,x4,x5,z]
```

the ideal

```text
(Q1,Q2,Q3,Q4,Q5,F10,z*W-1)
```

is the unit ideal.  Here `Q1,...,Q5` are the reviewed nonzero V22 unloaded
quadratic initials, the logical sixth quadratic is exactly `Q6=0`, `F10` is
the reviewed exact V22 quartic, and `W` is V23's exact rank-five witness.

The serialized logical eight-slot certificate has exact coefficients

```text
(c1,0,c3,c4,0,0,0,-1)
```

and the producer and a fresh Singular process both replayed

```text
c1*Q1 + c3*Q3 + c4*Q4 - (z*W-1) = 1.
```

Each of `c1,c3,c4` is visibly `z` times a polynomial in `x0,...,x5`.
Equivalently, the certificate exhibits the global exact-Q identity

```text
W in (Q1,Q3,Q4).
```

After the frozen substitution `x_i -> d_i_1` and
`z -> zinv*k10_0`, a separate exact process checked the source maps

```text
Q1..Q5 -> P1..P5,
F10    -> P35,
zW-1   -> P36,
```

and replayed the corresponding 36-entry identity for the exact-Q V24 prior
ideal.  Drop/add mutations at the first nonzero coefficient broke the small
and full identities in both processes.

Thus the exact normalized leading-base/F10 scheme has empty `D(W)`, and the
full normalized V24 prefix has empty `D(k10_0*W)`.  In particular, the V24
conditional grade-seven cokernel theorem on this open chart has no surviving
source point.  This says nothing about the required complementary `W=0`
chart.

## Chronology and fail-closed repair

The original R6 draft was not executed.  Toy type controls showed that
Singular drops the zero `Q6` ideal entry and that direct `lift(B,1)` errors on
a proper ideal rather than returning a typed fallback.  The R6 draft is
retained as a pre-algebra failure in `DESIGN_ERRATUM_R6_LEADING_BASE_DW.md`.

R6R1 used seven actual ideal generators and eight logical certificate slots.
An exact `slimgb` normal-form/dimension preflight selected the unit branch;
only then was direct `lift(B,1,U,"slimgb")` invoked.  No proper/nonunit
fallback was inferred from direct-lift behavior.

## Frozen producer and evidence

- preregistration:
  `PREREGISTRATION_R6R1_LEADING_BASE_DW.md`, SHA-256
  `925dad8f37a705021797769af75a596c4fa7c7406f9cf3d25f2d33696149c4bd`
- compiler: `compile_v24r6r1_leading_base_dw.py`, SHA-256
  `768ea90ab4505023bde9c6c1ff1c42e3e5f70d7bfe4b3a2016987ecebf11fbc1`
- runner: `run_v24r6r1_leading_base_dw_aws.sh`, SHA-256
  `0f1edca725a1fbc834aa297e898ab53ce20ec281f0705c1a8f95a5d9b12654ce`
- source freeze: `SOURCE_FREEZE_R6R1_LEADING_BASE_DW.sha256`, SHA-256
  `09edf52ff79b049d4f9501e831bef598a806e7be2f9594ba1659077f100db9ae`
- harvested evidence: `aws_box02_r6r1_unit/`
- producer result: `aws_box02_r6r1_unit/output/RESULT.json`, SHA-256
  `b0a537864954b95f5c5893cee998e46b73f30b4a20443fee749297b0f18487ce`
- evidence manifest: `aws_box02_r6r1_unit/EVIDENCE.sha256`, SHA-256
  `7d952021b475aaa2cc37409b4aee2f5b11ad884741ff65faa1ef147aeb750abb`
- final validation: `aws_box02_r6r1_unit/run/FINAL.validation`, SHA-256
  `47259838de14abac15d883bc3a08c004970d51d1bbc9b99aa461b9eac24cf9f0`

The source freeze replayed 14/14 inputs on AWS.  The evidence manifest
replayed 26/26 files on AWS and again after harvest by rebasing only its
absolute Box02 path prefix; artifact bytes were unchanged.

AWS lane:

```text
max12_812_order2_u2_62_k00_v24r6r1_leading_base_dw_20260827T154400Z_box02
```

Runtime was 0.13 seconds, maximum RSS was 42,064 KiB, and swaps were zero.

## Firewall

This result excludes only the normalized open chart `D(k10_0*W)` at the
displayed leading-base/full-prior prefix.  It does not analyze `W=0`, grades
7--19 on that complementary chart, a complete finite jet, an arc, K00 closure
incidence, order two, maximum twelve, or JC2.  It does not consume V24R2 or
V24R5, which remain independent live cross-checks.
