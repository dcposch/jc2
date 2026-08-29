# Hostile review: V24R6R1 exact leading-base `D(W)` certificate

Date: 2026-08-27  
Reviewer: Codex Sol Ultra subagent, independent fail-closed algebra lane  
Charged producer report:
`cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/RESULT_V24R6R1_LEADING_BASE_DW.md`  
Charged report SHA-256:
`8da4f616bba29b03522458e4b0c1c4ff42301264c16c293553d1833307cbd747`

## Verdict

**PASS at the exact narrow scope stated by the producer.**

There is no mathematical correction to the certificate or its localization
consequence.  Independently over `Q`, I obtain

```text
W = A1*Q1 + A3*Q3 + A4*Q4.
```

Consequently every point of the leading quadratic scheme already has `W=0`,
so its `D(W)` chart is empty.  Under the frozen substitution
`x_i -> d_i_1`, `z -> zinv*k10_0`, the exact 36-generator V24 prefix ideal is
also the unit ideal on `D(k10_0*W)`.  Thus V24's conditional grade-seven
rank-five theorem remains correct, but its chosen `W`-chart has no source
point after the earlier leading equations are imposed.

This does **not** exclude the complementary `W=0` locus.  It does not decide
another rank-five minor chart, rank at most four, grades 7--19 there, a full
finite jet, an arc, K00 closure incidence, order two, maximum twelve, or
JC2.

## Line-item audit

| Required attack | Independent result |
| --- | --- |
| Seven-generator small ideal over `Q` | PASS: `size(B)=7`, `NF_B(1)=0`, `dim(B)=-1` |
| Exact certificate | PASS: all eight logical files replay and give the unit identity |
| Global identity `W in (Q1,Q3,Q4)` | PASS: separate Groebner reduction and separate exact lift both give residual zero |
| Zero `Q6` custody | PASS: actual ideal has seven entries; logical slot 6 is literal zero |
| Full source map | PASS: `Q1..Q5 -> P1..P5`, `F10 -> P35`, and localizer `-> P36` coefficientwise |
| Full 36-entry identity | PASS in a fresh exact process |
| Load-bearing mutations | PASS in producer, small replay, full replay, and additive syzygy replay |
| R6 pre-algebra erratum | PASS: both stated Singular behaviors reproduce |
| Scope/firewall | PASS, with the sharpening that the result forces survivors into `W=0` but does not analyze them there |

## 1. Frozen inputs and custody

The following charged hashes reproduce from the live bytes:

```text
925dad8f37a705021797769af75a596c4fa7c7406f9cf3d25f2d33696149c4bd  PREREGISTRATION_R6R1_LEADING_BASE_DW.md
768ea90ab4505023bde9c6c1ff1c42e3e5f70d7bfe4b3a2016987ecebf11fbc1  compile_v24r6r1_leading_base_dw.py
0f1edca725a1fbc834aa297e898ab53ce20ec281f0705c1a8f95a5d9b12654ce  run_v24r6r1_leading_base_dw_aws.sh
09edf52ff79b049d4f9501e831bef598a806e7be2f9594ba1659077f100db9ae  SOURCE_FREEZE_R6R1_LEADING_BASE_DW.sha256
b0a537864954b95f5c5893cee998e46b73f30b4a20443fee749297b0f18487ce  aws_box02_r6r1_unit/output/RESULT.json
7d952021b475aaa2cc37409b4aee2f5b11ad884741ff65faa1ef147aeb750abb  aws_box02_r6r1_unit/EVIDENCE.sha256
```

The source-freeze manifest replays **14/14** entries.  After rebasing only
the frozen AWS path prefix, the evidence manifest replays **26/26** entries.
The exact source objects relevant to the mathematical identity also rehash:

```text
fd90f064ca43715c37fd7b02c99c842b0b21a6ecd7f5f2eeaf7b8645f95e62a2  unloaded Q1,...,Q6
c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8  F10
957181065328c7ef930c6c400272f45ab93a055ff1069ced7f3cca8b3c89bbde  W
6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a  frozen V24 prior/localizer source
```

Two nonblocking custody observations:

1. `outer.stdout` and `outer.stderr` are the two files in the original
   harvest not listed by `EVIDENCE.sha256`.  Both are empty and hash to
   `e3b0c442...b855`.  The producer claims 26/26 manifest entries, not an
   exhaustive-tree census, so this is hygiene rather than a false claim.
2. The producer report and the later `independent_replay/` and
   `aws_box02_r6r1_w_syzygy_replay/` additions necessarily postdate the
   producer evidence freeze.  The charged report hash above and this review
   should be pinned by the downstream adjudication rather than silently
   treated as members of the producer manifest.

Telemetry agrees with the report: the registered Box02 lane exited zero in
0.13 seconds, used 42,064 KiB maximum RSS, and recorded zero swaps.

## 2. The R6 failure and the seven/eight-slot repair

I reproduced both pre-algebra facts in the retained R6 erratum:

- In Singular, `ideal I=x,0,y` has `size(I)=2`; a literal zero generator is
  removed from the actual ideal representation.
- For the proper ideal `(x,y)`, `lift(I,ideal(1),U,"slimgb")` emits
  `2nd module does not lie in the first`; it is not a typed nonmembership
  branch.

R6R1 therefore correctly works with the seven actual generators

```text
B=(Q1,Q2,Q3,Q4,Q5,F10,z*W-1)
```

while serializing the eight logical slots

```text
(Q1,Q2,Q3,Q4,Q5,Q6=0,F10,z*W-1).
```

The exact `slimgb` preflight returns

```text
actual generators = 7
NF(1)             = 0
dimension         = -1.
```

Only after this exact unit decision does R6R1 call direct `lift`.  The
logical-to-actual map is correct: slots 1--5 map to actual entries 1--5,
slot 6 is serialized as literal zero, slot 7 maps to actual entry 6, and
slot 8 maps to actual entry 7.

## 3. Independent reconstruction of `W in (Q1,Q3,Q4)`

I did not use the producer's branch marker as evidence.  Starting from the
frozen V22 quadrics and V23 witness in a fresh exact-Q Singular process, I
formed

```text
J=(Q1,Q3,Q4).
```

An independent `slimgb(J)` has five basis elements and gives

```text
NF_J(W)=0.
```

A separate exact `lift(J,ideal(W),...)` returns a `3 x 1` coefficient
matrix; all three entries are nonzero and direct multiplication gives zero
residual.  This independently establishes `W in J` without the localizing
variable or `F10`.

I then audited the producer's serialized eight logical coefficients.  Their
SHA-256 profile is

```text
c1  e570129629517e9dd8eb14ae9545fca95381298cd86f0bb60c084fceeb98315f
c2  9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  (=0)
c3  9e1a2829d8ab82ab0ab983af38e07a5c8530f4cc4ffa98bf016d68dea4fe55b0
c4  57ea69e9a5977dc17e7a2b37ac2feb05aa164b60851738c77fbae3a5e244f992
c5  9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  (=0)
c6  9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  (=0 logical Q6 slot)
c7  9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  (=0 F10 slot)
c8  ee3aa64bb94a50845d5024cd4bd20202a4567aed5cd5328c0d97e9920775fc28  (=-1)
```

Exact substitution at `z=1` produces polynomials `A1,A3,A4`, and direct
coefficientwise checks give

```text
c1=z*A1,  c3=z*A3,  c4=z*A4,
A1*Q1+A3*Q3+A4*Q4-W=0.
```

Thus the serialized unit identity is not a localization artifact:

```text
c1*Q1+c3*Q3+c4*Q4-(z*W-1)
 = 1 + z*(A1*Q1+A3*Q3+A4*Q4-W)
 = 1.
```

The additive AWS derivation independently serializes the same three
polynomials and replays this global identity in a fresh process.  Its result
is
`8cd2afdd86f3f94749cbfcefa57055c437fc95ece2480ab9455e138aa56dc9ce`;
its source-freeze manifest is
`20a12f73f129f856ae6640820f10c3e0d44271099ef3f502633a2dc2f92b2265`
and replays 13/13 inputs.

## 4. Exact full-ring embedding

The full replay uses the charged V24 source honestly.  I compared bytes:

- lines 2 and 3, containing the prior ideal and `zinv*k10_0*W-1`, are
  byte-identical to the frozen V24 source;
- line 1 is byte-identical after the sole replacement
  `ring R=65521,` by `ring R=0,`.

This replacement is legitimate here because V24's compiler serialized the
prior equations from exact rational polynomial dictionaries before Singular
interpreted them in characteristic 65521.  The hostile-reviewed V24 source
independently reconstructed all 35 grade-2--6 rows and the exact witness.

In the exact-Q full ring the replay verifies `size(P)=36` and the source maps

```text
P1..P5 = Q1..Q5 after x_i -> d_i_1,
P35    = F10 after x_i -> d_i_1,
P36    = zinv*k10_0*W(d_i_1)-1.
```

The embedded coefficient vector has support only at positions `1,3,4,36`.
All other positions are zero; in particular, the logical `Q6` coefficient
is zero and the `F10` coefficient at `P35` is zero.  With
`z -> zinv*k10_0`, exact multiplication of the 36-generator row by this
vector is `1`.  Fresh local replay reproduces the frozen stdout hashes

```text
60ed7462e541aedcdf20c79d3101b4ac9e676bc05fd1cc0aa9adc8384dcd9b12  small
8f8790c6f46979d8bf768b0ec7383e5275ba3d9b0be8448b033ad777931a79a0  full
```

and the separately harvested replay has the same two hashes byte-for-byte.

## 5. Mutation audit

The selected contributing coefficient is `c1`.  The mutations are genuinely
load bearing:

- dropping `c1` changes the small residual from zero to `-c1*Q1`;
- adding `1` to `c1` changes it to `Q1`;
- after the full substitution, the corresponding residuals are
  `-c1_full*P1` and `P1`.

All four polynomials are nonzero over the exact polynomial rings.  The direct
producer, fresh small-ring replay, and fresh full-ring replay each reject
both mutations.  The additive global-syzygy replay also rejects drop/add
mutations of its first supporting coefficient.

## 6. Exact consequence and firewall

Let

```text
I=(Q1,Q2,Q3,Q4,Q5,F10) in Q[x0,...,x5].
```

Since `W in (Q1,Q3,Q4) subset I`, the localized quotient
`(Q[x]/I)[1/W]` is the zero ring.  Equivalently,
`(I,zW-1)=(1)`.  This proves that the leading-base/F10 scheme has empty
`D(W)`; in fact `Q2`, `Q5`, and `F10` are not needed for this conclusion.

Under the exact full source map, `P1=P3=P4=0` forces the mapped witness to
vanish, while `P36=0` asserts that `zinv*k10_0*W=1`.  Hence the full prior
prefix localized at `k10_0*W` is also empty as a scheme, not merely empty on
sampled points.

The only permissible campaign inference is therefore:

> all surviving points of this normalized prefix, if any, lie in `W=0`;
> the selected V24 Cramer chart `D(W)` (and its narrower constructible chart
> `D(k10_0*W)`) contributes no source points.

No equation here resolves the `W=0` locus or any later grade on it.  In
particular, the unit result must not be promoted to emptiness of the whole
valuation-one prefix, nonexistence of a finite jet or arc, K00 closure
exclusion, or a JC2 theorem.
