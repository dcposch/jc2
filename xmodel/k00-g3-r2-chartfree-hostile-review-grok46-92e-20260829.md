# Hostile review: K00 grade-three rank-two chart-free obstruction

Reviewer: **Grok 4.6** (`xAI`), equal-standing independent hostile replay,
different model from the Sol 5.6 producer note.
Date: 2026-08-29.
Frozen campaign basis:
`92ebe92ad5986a47f01af9ed901260595dfed869`.

Charged target:

```text
ac843e4c3da54a60d96f8b15961f1d75ffb45ca7ebef1664d44c755fffb25d76
  xmodel/k00-chartfree-next-sol56-20260829.md
body 11951 bytes
  6e7bacc0e0d338847ff59fb92d77c071edc998ecd297185ca6706737c73bbed5
```

Body cut independently verified: all bytes before the literal heading
`## Seal` (index 11951), SHA-256 `6e7bacc0…c73bbed5`.  Full-file SHA-256
matches the charged pin.  `jc2-lean` was not entered.  No canonical,
ladder, case, or ops file was edited.  No web, AWS, or unpublished `/tmp`
producer transcript was consumed.

## Verdict

**PASS_WITH_REPAIR**

Every charged coefficientwise source identity, both radical containments,
the fourth-power memberships `291, 60, 36, 0`, and the dimensions
`dim H = 2 = dim(H+I2(A))` reconstruct on a fresh characteristic-zero
desk pass.  The maximum safe theorem below is licensed after one
reporting repair to the producer note.  This is not a counterexample,
arc, occurrence, order-two exclusion, or JC2 conclusion.

| # | Charge | Verdict |
|--:|---|---|
| 1 | Seven literal `(Lambda_grade,row)=(3,1..7)` rows; `P3=C u+c3` with `C=A[:,1..6]` | **CONFIRMED** |
| 2 | Second derivatives, affine reconstruction, `C` versus `A` | **CONFIRMED** (`0,0,0` failures) |
| 3 | Grade-3 lift on `V(J2)` implies `I3(E3)=0` when `rank(A)<=2`, including `rank(C)<rank(A)` | **CONFIRMED** |
| 4 | `H subset J2+I2(A)` by labelled Laplace identities | **CONFIRMED** (`LAPLACE_BAD=0`, `H_SUBSET_J1_BAD=0`) |
| 5 | `I2(A) subset sqrt(H)` by `q^4` on every nonzero labelled slot | **CONFIRMED** (`291,60,36,0`) |
| 6 | `dim H=2`, `dim(H+I2(A))=2`, both proper | **CONFIRMED** |
| 7 | Nullstellensatz corollary empties every full-`P6` rank-two minor chart; old cap is not a certificate | **CONFIRMED** |
| 8 | Mutations of one `c3` coefficient, one `C/A` entry, and a perturbed `q^4` | **CONFIRMED** (all three fire) |
| 9 | Novelty versus V27 | **CONFIRMED**: V27 forbade this conclusion |
| 10 | Producer `I3E_NCOLS=813` as labelled universe | **REPAIR**: labelled `ncols=1225` with `412` zeros |

## 1. Custody and source location

Named frozen inputs, all bytes verified on disk:

```text
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json
c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0
  cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/aws_r6a_r2_exact_base3/output/BASE3_R2_STANDARD_BASIS.txt
738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a
  xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md
4780282b40a8bb0c83da3b3cd887c8e2edb5af99816203e8188a253f1174d6d8
  cases/max12_812_order2_u2_62_k00_aws_custody_20260828/CUSTODY.sha256
```

Exact V26 compiler/source manifest used, not a status string:

```text
24640d0dacec16b27b4c7eb83419188aa86e3fc80b481b0ba64aa136348fc892
  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/compile_fitting_atlas_v26.py
8e6d6acb948c01b81809920023e3e20c25fb0166d07686c2309f961e02fbabc0
  .../SOURCE_FREEZE_R1_W0_HELD_COMPILE.sha256
5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32
  .../aws_box02_r2_held_compile/output/COMPILED_SOURCE.sha256
2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/SOURCE_COLUMNS.json
ce5063930117bc8fe9869dc80f1535459dd41209a35406ed7edacde1213618dd
  cases/.../output/P6_LITERAL_SOURCE_LABELS.json
```

The compiler writes `P6_literal_rows_through_grade6` as every
`(row, Lambda_grade)` in `{1..7} x {0..6}` from the V20 literal DAG,
zeros retained.  The seven grade-three rows are the unique items with
`Lambda_grade=3` and `row=1..7`.  Each atlas `singular` string hashes,
after the V27 `object_digest` convention `sha256(text.strip()+"\n")`,
to the frozen label file:

```text
row 1  3da8e359ab74f5f47fb957ab693b93ed85e38fc16b03d1843fe4e5645bbe2249  nterms=23
row 2  6d72aae5c227bd8840c8a9d0ee4d7d66c4b2d6dc161e7035f76b0f8f691b5fc8  nterms=26
row 3  40bbadeb1f18283e0fac03d1bdd5bea106897c4954237e8d1517eded59eddd5a  nterms=31
row 4  d76571853127a095bc2c8fb19041c08a469db18a6e11fbeed6b73bccc7caba56  nterms=33
row 5  2ae891d515cf450446a6196786924d5ff980271bbd9a19e656638976e3a109cf  nterms=35
row 6  17eb9e7f9b58d59de4e4d062bcfa06176c75ac189397188482091f6b4241c0f3  nterms=21
row 7  c12da043acb83e79170c7c1d6368bfa2ac6e2f9056143bd0847274b8ebb489b3  nterms=35
LABEL_HASH_BAD=0
```

None of these seven polynomials is the zero polynomial.  Row 6 is
identically independent of `u` (`C` row 6 is the zero row of `A[:,1..6]`).
No `k10_*` variable occurs in any grade-three row.

Producer transcript
`0990f7dd2ced2449b8b391b4e74fb36df1f267a07181f2dce29574529e31d2c7`
exists only as a citation inside the charged note.  It was not located
in the frozen tree and was not used.

## 2. Ring map, field, and reconstruction

Declared map, not name-matching:

- Coefficient field: `Q` (Singular `ring …=0,…`).
- Affine check ring:
  `S=0,(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1,d0_2,d1_2,d2_2,d3_2,d4_2,d5_2),dp`.
- Six-variable chart, identical to reviewed V27:
  `R=0,(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1),dp`.
- Leading variables `x=(d0_1,...,d5_1)`; next variables
  `u=(d0_2,...,d5_2)`.
- Atlas `ring_variables` is the 33-variable prior list (family-major).
  Image check: every reconstructed `A` entry, every `B` generator, every
  `c3` row, and every labelled minor used below lies in `Q[x]`.  `P3`
  lies in `Q[x,u]` and involves no other prior or newest name.
- `B` is the six nonzero literal grade-two rows (labels `(2,1..5)` and
  `(2,7)`) plus `F10`.  Coefficientwise `Q1_to_Q6` equals those six
  rows.  Grade-two row 6 is the stored zero.
- Frozen nine-element `J2` basis imported from
  `BASE3_R2_STANDARD_BASIS.txt` and compared with a freshly computed
  `std(B+I3(A))`.  Mutual reduction: `J2_FROZEN_VS_FRESH_BAD=0`.
- Ordinary `std` versus `slimgb` on `H`: `H_STD_VS_SLIMGB_BAD=0`.
- Positional loops bound by `ncols()`, never `size()`.  Diagnostic
  `size()` prints were recorded and ignored as counts.

Independent exact-`Q` reconstruction of `P3` from `exact_terms`, then a
second reconstruction in Singular by `diff` and `subst`, both returned:

```text
SECOND_DERIVATIVE_BAD=0
AFFINE_RECONSTRUCTION_BAD=0
C_A_MISMATCH=0
FOREIGN_VARS_BAD=0
C_ROW6_NONZERO_COLS=0
A_COL7_NONQUADRATIC=0
```

Thus `P3(x,u)=C(x) u+c3(x)` with `C=A[:,1..6]` coefficientwise, and the
seventh (quadratic, `k10`-newest) column of `A` is absent at grade three.
`E3=[C|c3]` is the labelled `7 x 7` matrix used below.

## 3. Labelled minors, zeros, and scalar classes

Every literal slot was enumerated by strictly increasing row and column
subsets.  Zeros were retained.

```text
I2(A):  ncols=441  size=351  zero=90  nonzero=351
I2(C):  ncols=315  size=225  zero=90  nonzero=225
I3(A):  ncols=1225 size=813  zero=412 nonzero=813
I3(E3): ncols=1225 size=813  zero=412 nonzero=813
I3E_OUTSIDE_J2=399
```

Every `2 x 2` of `C` equals the corresponding `A`-slot that avoids
column 7.  All 90 zero slots of `I2(A)` lie in that `C`-block: the 126
slots that use column 7 are nonzero as polynomials.  So `rank(C)<rank(A)`
is possible as a polynomial-matrix phenomenon; it is not excluded by
source identity.

Unique exact nonzero `2 x 2` polynomials of `A`: **326**, matching the
reviewed V26/V27 census (327 exact polynomials including the zero class).
`Q`-proportionality classes of the 351 nonzero slots: **187**
(extras 164).  The producer tested every nonzero slot rather than a
class representative; that is the correct membership contract.

Repair to the producer note: `I3E_NCOLS=813` is the nonzero-only
`size()` of `I3(E3)`, not the labelled universe.  The labelled object
required by the producer’s own promotion packet is

```text
I3E_LABELLED_NCOLS=1225
I3E_ZERO=412
I3E_NZ=813
```

The 813/399 nonzero and outside-`J2` counts are confirmed.

## 4. Fresh `H` and the two radical containments

`J2` rebuilt as `B+I3(A)` in `R`:

```text
J2_NF1=1
J2_DIM=3
J2_NCOLS=9
```

`H=J2+I3(E3)` from the raw 1225 labelled `E3` minors, ordinary `std`:

```text
H_NF1=1
H_DIM=2
H_NCOLS=20
H_SIZE=20
H1=H+I2(A):  NF1=1  DIM=2  NCOLS=10
J1=J2+I2(A): NF1=1  DIM=2  NCOLS=10
```

**Containment `H subset J1`.**  Every `3 x 3` minor of `E3` was checked
against its Laplace expansion along the last used column, with cofactors
the labelled `2 x 2` minors of `C`.  `LAPLACE_BAD=0`.  Hence
`I3(E3) subset I2(C) subset I2(A)` as ideals, so
`H=J2+I3(E3) subset J2+I2(A)=J1`.  Independently, every labelled
`I3(E3)` generator (and every `B` and `I3(A)` generator) reduces to zero
modulo a fresh basis of `J1`: `H_SUBSET_J1_BAD=0`.  This is an identity,
not a dimension coincidence.

**Containment `I2(A) subset sqrt(H)`.**  For each of the 441 labelled
`I2(A)` slots, looping `mi=1..ncols(I2A)`, the zero slots were skipped
and each of the 351 nonzero polynomials `q` was reduced at powers 1, 2,
3, 4 against the fresh basis of `H`:

```text
POWER1_NONZERO_NF=291
POWER2_NONZERO_NF=60
POWER3_NONZERO_NF=36
POWER4_NONZERO_NF=0
```

So every labelled generator of `I2(A)` has fourth power in `H`.
Therefore `I2(A) subset sqrt(H)`.  Combined with the Laplace
containment, `sqrt(H)=sqrt(J1)`.

The 60 slots with `q in H` are exactly the 60 interior slots of the
reviewed V27 census `I2(A) cap J2`.  Reason: `J2 subset H` by
construction, Fable 5 independently proved 60 of 351 lie in `J2`, and
the power-1 count shows 60 of 351 lie in `H`; the two 60-element sets
therefore coincide.  Dimension drop `3 -> 2` from `J2` to `H` is
consistent with those 60 already lying in `J2` while the remaining 291
enter the radical only at higher power.

No `sat()` wrapper was used.  Remainders were raw normal forms in the
declared quotient `R/H` with global order `dp`.  Vanished leaders are
the usual `reduce==0` branch; the zero polynomial was handled by
skipping zero slots.

## 5. Hostile checks

**Lift implies `I3(E3)=0`, including `rank(C)<rank(A)`.**
On `V(J2)` one has `rank A(x)<=2`.  Solvability of `C(x) u=-c3(x)` is
`rank E3(x)=rank C(x)`.  Always `rank C<=rank A`, so
`rank E3<=2` and every `3 x 3` minor of `E3` vanishes.  If
`rank C<rank A=2`, then `rank C<=1` and `rank E3<=2` still, so
`I3(E3)=0` remains necessary (and is automatic even without a lift
once `rank C<=1` and `c3` does not raise the rank above 2).  The
obstruction does not pretend that `I3(E3)=0` is sufficient for a lift
on the `rank C<=1` locus; sufficiency is not claimed.  Necessity is
enough, because the radical containment then forbids `rank A=2` at any
point of `V(H)`.

**Nullstellensatz corollary.**  Any point of `V(P6+I3(A))` solves the
grade-three subsystem, hence projects into `V(H)` after the lift
condition.  `I2(A) subset sqrt(H)` forces `rank A<=1` on `V(H)`.
Therefore

```text
V(P6+I3(A)) intersect D(I2(A)) = empty
```

over an algebraic closure, and for every literal `2 x 2` minor `m`,

```text
P6+I3(A)+(z*m-1)=(1)
```

as a Nullstellensatz consequence, not as a computed Bezout column.
The historical selected-chart run remains `RESOURCE_CAP_NO_VERDICT`.
It is not retroactively a certificate.  The target ideal is
mathematically predicted unit; the executable full-ring witness is
still absent and is not required to stop rank-two full-`P6` work.

**V27 did not license this.**  The frozen Fable 5 review, Section 8,
explicitly forbids inference of the full prior `P6`, any later-grade
compatibility, and any nilpotent or later-grade lifting.  The present
grade-three obstruction is new.

**Controls.**

```text
KNOWN_PROPER_NF1=1          # (d0_1) remains proper
FORCED_UNIT_NF1=0           # adding 1 yields the unit ideal
MUT_C3_AUGMINOR_CHANGED=1   # c3_1 := c3_1+1 changes det E3[{1,2,3},{1,2,7}]
MUT_C_A_ENTRY_BREAKS=1      # C[1,1]+1 != A[1,1]
MUT_Q4_REMAINDER_NONZERO=1  # (q+1)^4 has nonzero NF modulo H
```

The mutated `q` was a labelled nonzero `2 x 2` whose cube was already
outside `H` (`FIRST_P3_SLOT=1`).  A nonzero mutated remainder is the
required negative control.

## 6. Maximum safe theorem, repair, and stop rule

After the labelled-slot erratum in Section 3, the following may be
promoted on the six-variable chart `R=Q[d0_1,...,d5_1]`, frozen V26
`A,B,P3` and reviewed V27 `J2=B+I3(A)`.

**Theorem (K00-G3-R2-CHARTFREE).**
No geometric point of `V(J2)` with `rank A=2` lifts through the seven
literal Lambda-grade-three rows.  Equivalently, `I2(A) subset sqrt(H)`
for `H=J2+I3(E3)` with `E3=[A[:,1..6]|c3]`, and therefore
`V(P6+I3(A))` does not meet `D(I2(A))`.

Exact repair, required in the producer note and in any promotion
packet before freeze:

1. Quote labelled `I3(E3)` as `ncols=1225` / `zero=412` / `nonzero=813`.
   Do not write `I3E_NCOLS=813` as if zero slots were absent.
2. Keep every membership loop on `ncols()`.  The 351 nonzero `I2(A)`
   slots were all tested; scalar-proportional sharing is optional and
   was not used here.

No algebraic blocker remains on the rank-exactly-two grade-three
question.

**Stop rank-two full-`P6` work.**  Yes.  Do not rerun the capped
selected-minor engine, do not launch another rank-two minor chart, and
do not spend AWS extracting a redundant full-ring Bezout certificate
unless archival software closure is separately valued.

**Smallest independent successors**, neither of which is licensed here:

1. **Rank at most one.**  On `V(J1)` one has `rank A<=1`, so
   `I3(E3)=0` is automatic and is not a compatibility test.  Split
   chart-freely into `rank(C)=1`, requiring `I2(E3)=0`, and
   `rank(C)=0`, requiring `C=0` and `c3=0`.  `k10_0` is absent from
   the grade-three rows; retain the source-open condition at the first
   successor where that column is actually typed.
2. **Rank five.**  Finish the registered `MAX5CLASS` comparison of the
   two proportionality classes of maximal minors.  V27 did not treat
   this branch.

These may run in parallel.  They are not this theorem.

## 7. Replay

Scratch only, under `/tmp/k00-g3-r2-review-grok46/`.  Engine: Singular
4.4.1 (`arm64-Darwin`), one local process, characteristic zero.

```text
python3 /tmp/k00-g3-r2-review-grok46/rebuild.py
Singular -q /tmp/k00-g3-r2-review-grok46/rebuild.sing
```

```text
rebuild.py     sha256=0d97ae973db321643f5f6d28716e28d14ced8a0bcedccf775563dfda67c0f34b  bytes=21736
rebuild.sing   sha256=f13f5fcd6d5c29091033f5df5c26b49d48971dab12272bf2b952bc94b640e40d  bytes=30304
affine stdout  sha256=c7663fd74961ae2b3af508135d5afbdefe299889824a6e5c35d5df9ed144d893  bytes=2020
singular stdout sha256=5ca3dbae9ab3069bd1ebf3418da9ab419549896b54b84f1ad12aca29d75e28a0  bytes=998098
Singular wall  real 0.74 s  user 0.71 s  sys 0.02 s
```

The Singular wall is inside the producer’s measured sub-3-second desk
envelope.  Marker extract from the replay (complete identity block):

```text
SECOND_DERIVATIVE_BAD=0
AFFINE_RECONSTRUCTION_BAD=0
C_A_MISMATCH=0
I2A_NCOLS=441 I2A_SIZE=351 I2A_ZERO=90 I2A_NZ=351
I3E_NCOLS=1225 I3E_SIZE=813 I3E_ZERO=412 I3E_NZ=813
LAPLACE_BAD=0
J2_NF1=1 J2_DIM=3 J2_FROZEN_VS_FRESH_BAD=0
I3E_OUTSIDE_J2=399
H_NF1=1 H_DIM=2 H_NCOLS=20
H_STD_VS_SLIMGB_BAD=0
H_SUBSET_J1_BAD=0
H1_NF1=1 H1_DIM=2 H1_NCOLS=10
POWER1_NONZERO_NF=291
POWER2_NONZERO_NF=60
POWER3_NONZERO_NF=36
POWER4_NONZERO_NF=0
KNOWN_PROPER_NF1=1
FORCED_UNIT_NF1=0
MUT_C3_AUGMINOR_CHANGED=1
MUT_C_A_ENTRY_BREAKS=1
MUT_Q4_REMAINDER_NONZERO=1
REPLAY_DONE
```

A reviewer `intvec` uniqueness loop and an `else if` census of
`I2` modulo `J2` were skipped by Singular syntax; they were not used.
Scalar classes were obtained from an independent exact Python
determinant census of all 441 slots.  The `I2 cap J2` identification
uses the named Fable 5 review together with `J2 subset H` and the
power-1 count, as in Section 4.

## 8. Firewall

This review licenses only the grade-three rank-exactly-two obstruction
on the six-variable coefficient base, after the labelled `I3(E3)`
census repair.  It does not license rank-five, rank-one, or rank-zero
lifts; grades 4--6 or 8--19; `k10_0` source-open reachability; any
finite jet, formal or convergent arc, closure incidence, order-two or
maximum-twelve statement, polynomial Keller map, counterexample, or
JC2.

FALLACY-v2: no exit-price assertion is made, so `charge_basis` is
absent.  No `sat()` wrapping.  No pole identity.  No flag/place/series
identification.  Variable/ring map and generator order are declared in
Section 2.  Remainder degree is the raw `dp` normal form, including
the zero case.

<!-- END-SEALED-BODY::k00-g3-r2-chartfree-hostile-review-grok46-92e-20260829 -->

## Seal (outside the sealed body)

Convention: the sealed body is the byte range from the first byte of this
file through and including the newline that terminates the unique marker
line above.  This seal section is excluded.

```text
sealed-body bytes      16883
sealed-body SHA-256    ecdb42543df6a34dd72a0973d047911ce3430e6e9d74773ec38171e8641768f2
  cut at 16882 bytes   06ad25bc0fb41a7a5a1b2d38f71448a41c274c4c33f36640d2f110d8693839f0
  cut at 16884 bytes   460764303bc0240dbe8d99b5916ff3c0824e239c6aaa27b4705d82c100cb3d31
```

Frozen basis `92ebe92ad5986a47f01af9ed901260595dfed869`.  Charged target
and four named frozen inputs reproduced their declared SHA-256 values
before this write.  `charge_basis` is absent.
