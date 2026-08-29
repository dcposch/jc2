# K00 grade-three rank-at-most-one chart-free Fitting split

Author: Grok 4.6, equal-standing independent primary  
Date: 2026-08-29  
Lifecycle: **PRIMARY EXACT DESK THEOREM / INDEPENDENT REPLAY REQUIRED /
NO CANONICAL PROMOTION IN THIS FILE**  
Frozen campaign basis: `92ebe92ad5986a47f01af9ed901260595dfed869`

The Sol grade-three rank-two note
`xmodel/k00-chartfree-next-sol56-20260829.md` (full SHA-256
`ac843e4c3da54a60d96f8b15961f1d75ffb45ca7ebef1664d44c755fffb25d76`)
is charged only as the branch pointer.  It is provisional and is not a
premise.

## 0. Binary disposition

```text
PASS_K00_G3_RANKLE1_CHARTFREE
  RANK1_COMPATIBLE_GEOMETRIC_LOCUS = EMPTY
  RANK0_COMPATIBLE_LOCUS           = SURVIVES (reduced 2-plane)
```

Both Fitting strata over `V(J1)` are decided at desk scale.  The weak
automatic condition `I3(E3)=0` is not rank-one compatibility.  No
projection of `V(J1)` is treated as a lift.

## 1. Maximum theorem

Let `A` be the frozen V26 grade-seven newest-variable `7 x 7` matrix in
`R = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1]`, let `B` be the seven-element
leading ideal `(Q1,...,Q5,Q7,F10)`, and let

```text
J2 = B + I3(A),     J1 = J2 + I2(A)
```

as in the reviewed V27 six-variable filtration.  Independently from the
seven literal source-labelled rows with `(Lambda_grade,row)=(3,1..7)`,

```text
P3(x,u) = C(x) u + c3(x),
C = A[:,1..6],
E3 = [C | c3],
```

in the twelve-variable ring
`T = Q[d0_1,...,d5_1,d0_2,...,d5_2]`, with `u=(d0_2,...,d5_2)`.
Every second `u`-derivative vanishes, affine reconstruction is exact,
and `C` equals the first six columns of `A` coefficientwise.  Row 6 of
`C` is identically zero; no `c3` slot is zero; `k10_*` does not occur
in `P3`.

Over `V(J1)`, where `rank(A)<=1` and therefore `rank(C)<=1`,

```text
I2(C) subset J1,     I3(E3) subset J1,
```

while `I2(E3)` is not contained in `J1` (120 of 441 slots have nonzero
normal form).  Write

```text
R1 = J1 + I2(E3),          % closure of rank(E3)<=1 on V(J1)
J0 = J1 + I1(C),           % rank(C)=0 locus on V(J1)
R0 = J0 + (c3).            % rank-zero compatibility
```

Then, as ideals in `R`,

```text
R0 = J0 = (2*d3_1 - d5_1,  d2_1 - d4_1,  16*d1_1 - d5_1,  d0_1 - 2*d4_1).
```

This is a prime linear complete intersection of affine dimension two
(four independent linear forms; leading-term dimension two).  On the
corresponding 2-plane, `A=0` and `c3=0` identically, so `P3` vanishes
for every `u`.  Parametrically the plane is

```text
(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1) = (2s, t/8, s, t, s, 2t).
```

Further:

- `J1 subset R1 subset J0`, all proper, all affine dimension two;
- `(2*d3_1-d5_1)^4` and the other three linear generators of `J0` to
  the fourth power lie in `R1`, hence `sqrt(R1)=J0`;
- `R1 + (z*(2*d3_1-d5_1)-1) = (1)`;
- `J1 + (z*(2*d3_1-d5_1)-1)` is proper of affine dimension two, so
  `2*d3_1-d5_1` is not in `sqrt(J1)`, and `V(J1)` is not contained in
  the plane;
- the further pin `d4_1=0`, `d5_1=1` on that chart is proper of
  dimension zero, hence `V(J1)` contains a nonempty finite `Q-bar`
  scheme of points with `rank(C)=1`.

Therefore, over an algebraic closure:

> A point of `V(J1)` solves the seven grade-three equations for some
> `u` if and only if it lies on the displayed 2-plane.  Equivalently
> the geometric rank-exactly-one compatible locus is empty, while the
> rank-zero compatible locus is this reduced 2-plane, on which `A=0`,
> `c3=0`, and every `u` works.  The automatic vanishing `I3(E3)=0` on
> `V(J1)` does not decide rank-one solvability.

Fresh `J1` equals the reviewed V27 `BASE2` ideal by mutual reduction.
Ordinary `std` and `slimgb` agree on `J1`, `R1`, `J0`, `R0`, and the
named charts.

## 2. What this does not prove

This is not a review of the provisional rank-two obstruction; not a
rank-five statement; not a full-`P6` statement; not a statement at
grades four through six or seven through nineteen; not a
`k10_0`-open source point; not a formal or convergent arc; not a
Keller pair; not a counterexample; not an order-two exclusion; and
not a result on JC2.  Free `u` on the 2-plane is an identity of `P3`,
not a jet.  Nonempty `D(2*d3_1-d5_1) cap V(J1)` is not a lift.
Minimal associated primes of `J1` itself were not completed.

## 3. Custody and charged inputs

`git rev-parse HEAD` was `92ebe92ad5986a47f01af9ed901260595dfed869`
at the start of work.  No canonical, ladder, case, guardrail, or
operations file was edited.  No commit, push, web lookup, AWS, remote
shell, or `jc2-lean` access.  Scratch lived under `/tmp/k00_g3_rankle1/`
only.  The only repository file created is this report.

Independently rehashed charged inputs:

```text
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json
5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32
  .../COMPILED_SOURCE.sha256
f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97
  .../RESULT.json
ce5063930117bc8fe9869dc80f1535459dd41209a35406ed7edacde1213618dd
  cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/aws_r6a_alt_full_p6_rank2_chart_r5r7_c6c7/output/P6_LITERAL_SOURCE_LABELS.json
c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0
  .../aws_r6a_r2_exact_base3/output/BASE3_R2_STANDARD_BASIS.txt
a840c9b69d64646e900531dddfba8ba9309336c61a83ddefb424a33d2fcdc26b
  .../aws_r6a_r3_exact_base2/output/BASE2_R3_STANDARD_BASIS.txt
738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a
  xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md
c42c0482f0b5861f5099e6e121c60a93d018c87a9619749ee1844f5954545c39
  cases/.../RESULT_V27_BASE3_R2_EXACT_PREPASS.md
8e4b545d72e2dc62a1c60090e2d956969320d738c6c35968944039e3bccb80a2
  cases/.../RESULT_V27_BASE2_R3_EXACT_PREPASS.md
ceb69e22c43cb366d52a2e7d9bd3ec9d5ae4befd18368202d711a20e4b5e3f99
  cases/.../DESIGN_ERRATUM_R3_SIZE_NCOLS.md
2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/SOURCE_COLUMNS.json
ac843e4c3da54a60d96f8b15961f1d75ffb45ca7ebef1664d44c755fffb25d76
  xmodel/k00-chartfree-next-sol56-20260829.md   (pointer only; not a premise)
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
  FALLACY-v2.md
```

All seven grade-three `singular_text_sha256` labels match
`sha256(atlas_singular.strip()+'\n')`:

```text
(3,1) 3da8e359ab74f5f47fb957ab693b93ed85e38fc16b03d1843fe4e5645bbe2249
(3,2) 6d72aae5c227bd8840c8a9d0ee4d7d66c4b2d6dc161e7035f76b0f8f691b5fc8
(3,3) 40bbadeb1f18283e0fac03d1bdd5bea106897c4954237e8d1517eded59eddd5a
(3,4) d76571853127a095bc2c8fb19041c08a469db18a6e11fbeed6b73bccc7caba56
(3,5) 2ae891d515cf450446a6196786924d5ff980271bbd9a19e656638976e3a109cf
(3,6) 17eb9e7f9b58d59de4e4d062bcfa06176c75ac189397188482091f6b4241c0f3
(3,7) c12da043acb83e79170c7c1d6368bfa2ac6e2f9056143bd0847274b8ebb489b3
```

All 49 literal `(Lambda_grade,row)` labels match the same convention.
Engine: Singular 4.4.1p5, arm64-Darwin, exact `Q`, `dp`.  This is a
different implementation from the V27 Linux 4.3.2 producer.

## 4. Reconstruction of `P3 = C u + c3`

Ring map, declared: coefficient field `Q`; `T` generator order
`(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1,d0_2,d1_2,d2_2,d3_2,d4_2,d5_2)`;
`R` generator order `(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1)`; `C` is obtained
in `T` by `diff(P3[row], d{j-1}_2)` and compared with `A[row,j]` for
`j=1..6`; `c3 = killU(P3)` with `killU: T -> T` sending every `d*_2`
to `0`; image of `(A,C,c3)` in `R` is by the ring map
`toR = imap` killing `u`.  Matching names were not used as proof.

Exact `Fraction` parse of atlas `exact_terms`, then an independent
Singular reconstruction, both returned:

```text
SECOND_DERIVATIVE_BAD=0
AFFINE_RECONSTRUCTION_BAD=0
C_A_MISMATCH=0
C_A_MISMATCH_AFTER_IMAP=0
P3_NCOLS=7
P3_ZERO_SLOTS=0
C_ZERO_ENTRIES=6
C3_ZERO_SLOTS=0
K10_ABSENT_FROM_T_RING=1
RECONSTRUCTION=PASS
```

The six vanishing `C` entries are the entire sixth row, matching
`A[6,1..6]=0` with `A[6,7]` quadratic and nonzero as a polynomial.
`c3` is homogeneous of degree 3; `C` is homogeneous of degree 1.
Python term counts for `c3`: `(7,9,13,15,19,21,23)`.

## 5. Fitting ideals, `ncols`, ordinary versus optimized

`B` is the six nonzero grade-two rows `Q1..Q6` plus `F10`, all in the
six leading variables (`B_NCOLS=7`, `B_ZERO_SLOTS=0`).  Minors were
built by `minor(_,k)` and counted with `ncols`, never `size()` as a
positional bound.

```text
I3A_NCOLS=813   I3A_NONZERO=813
I2A_NCOLS=441   I2A_NONZERO=351
I2C_NCOLS=315   I2C_NONZERO=225
I2E_NCOLS=441   I2E_NONZERO=351
I3E_NCOLS=813   I3E_NONZERO=813
```

On this 4.4.1 engine, `minor(A,3)` stores only the 813 nonzero `3 x 3`
minors, whereas reviewed V27/Linux 4.3.2 retains 1225 labelled slots
of which 813 are nonzero.  The nonzero census matches.  `I2A` and
`I2E` retain the full `C(7,2)^2=441` slots.  Ideal membership uses
the nonzero generators; the dropped zero `3 x 3` slots do not change
`I3(A)` or `I3(E3)`.

```text
J2_STD_NCOLS=9   J2_NF1=1   J2_DIM=3
J1_STD_NCOLS=10  J1_SLIM_NCOLS=10
J1_STD_NF1=1     J1_SLIM_NF1=1
J1_STD_DIM=2     J1_SLIM_DIM=2
J1_STD_SLIM_MUTUAL=1
FRESH_J1_SUBSET_V27BASE2=1
V27BASE2_SUBSET_FRESH_J1=1
I2C_OUTSIDE_J1=0
I3E_OUTSIDE_J1=0
I2E_INSIDE_J1=321
I2E_OUTSIDE_J1=120
R1_STD_NCOLS=13  R1_SLIM_NCOLS=13
R1_STD_NF1=1     R1_SLIM_NF1=1
R1_STD_DIM=2     R1_SLIM_DIM=2
R1_STD_SLIM_MUTUAL=1
J1_SUBSET_R1=1   R1_SUBSET_J1=0
I1C_NCOLS=20     I1C_ZERO_SLOTS=0
J0_STD_NCOLS=4   J0_SLIM_NCOLS=4
J0_STD_NF1=1     J0_SLIM_NF1=1
J0_STD_DIM=2     J0_SLIM_DIM=2
J0_STD_SLIM_MUTUAL=1
J1_SUBSET_J0=1   J0_SUBSET_J1=0
R0_STD_NCOLS=4   R0_EQ_J0=1
R0_STD_NF1=1     R0_STD_DIM=2
R1_SUBSET_R0=1   R0_SUBSET_R1=0
```

`I3(E3) subset J1` is the automatic weak condition `rank(E3)<=2` on a
rank-`<=1` base.  The 120 nonzero normal forms of `I2(E3)` are the
rank-one compatibility conditions.  `I1C_NCOLS=20` is the engine
storage after adjoining the 42 slots of `C` (six of which are the zero
row); the Groebner basis of `J0` has four linear generators.

Serialized bases (scratch, not repository):

```text
43972fa44305a31ac6cd9ba5145bc16a81a3c1fa3c5a4f2ff2d0b06a972c279a  SJ1o.txt
4818a64b4860b44249bbbab675440f13f97a6791cb6ade620be5148faae7374f  SR1o.txt
4b305133f471d254306468434751125b21f6c04a6681e707af2d301d5193d436  SJ0o.txt = SR0o.txt
```

`J0`/`R0` content is exactly

```text
2*d3_1-d5_1, d2_1-d4_1, 16*d1_1-d5_1, d0_1-2*d4_1
```

## 6. Rank-zero stratum: the plane survives

`R0=J0` means `c3` already lies in `J1+I1(C)`.  Exact evaluation of
every entry of `A` and of `c3` at `(s,t)` in
`{(1,0),(0,1),(1,1),(0,0)}` returns the zero matrix and the zero
vector, hence `rank(A)=rank(C)=rank(E3)=0` on a spanning set of the
plane.  Because `C` is linear and `J0` is radical, this is the
polynomial identity `I1(A) subset J0`, not a sampling claim.

There is no residual “rank lives only in column 7” piece inside
`V(J1)`: `C=0` forces `A=0` on this base.  Origin membership is
trivial by homogeneity (`ORIGIN_BAD=0`) and is not a useful point.

On the plane `P3` is the zero polynomial in `u`.  That is an identity
of the seven labelled grade-three rows, not a projection of a later
ideal, not a grade-four solution, and not a `k10_0`-open source point.

## 7. Rank-one stratum: compatible locus empty, incompatible locus nonempty

Fourth powers of all four linear generators of `J0` lie in `R1` and
not in `J1`:

```text
G1_R1_K=4  G1_J1_K=0   (through k=12 still not in J1)
G2_R1_K=4  G2_J1_K=0
G3_R1_K=4  G3_J1_K=0
G4_R1_K=4  G4_J1_K=0
```

Together with `R1 subset J0` this gives `sqrt(R1)=J0`.  The displayed
linear ideal is prime, so it is the unique minimal prime of `R1`.
`minAssGTZ(J1)` was not completed (58-second cap on a dedicated
primdec process); that is recorded as a blocker for a component list
of `V(J1)`, not for the radical of `R1`.

Rabinowitsch, ring `Q[d0_1,...,d5_1,z]`, `dp`:

```text
R1 + (z*(2*d3_1-d5_1)-1) : NF1=0, DIM=-1, unit
J1 + (z*(2*d3_1-d5_1)-1) : NF1=1, DIM=2, proper  (std and slimgb)
J1 + (z*(d2_1-d4_1)-1)    : NF1=1, DIM=2, proper
J1-chart + (d4_1, d5_1-1) : NF1=1, DIM=0, proper
J1-chart + (d4_1-1, d5_1) : NF1=1, DIM=0, proper
```

The unit chart on `R1` is the positive control that `2*d3_1-d5_1`
lies in `sqrt(R1)`.  The proper dimension-two chart on `J1` is the
negative control that it does not lie in `sqrt(J1)`.  The
dimension-zero pins are nonempty finite schemes over `Q-bar` of
points of `V(J1)` with `2*d3_1-d5_1 != 0`, hence `rank(C)=1`.  No
rational point of that scheme is exhibited (the pin `d4_1=1,d5_1=0`
has negative quadratic discriminant; the pin `d4_1=0,d5_1=1` is a
nonsquare positive discriminant).  Those points cannot lie in
`V(R1)=V(J0)`, so they fail `I2(E3)=0`.

## 8. When `k10_0 != 0` first enters

Three typed facts, kept distinct:

1. `SOURCE_COLUMNS.json` records `k10_0` as kind `load`,
   `first_Lambda_grade=2`, `boundary_status=FREE`.
2. Frozen contracted `P6` support first contains the variable `k10_0`
   at `Lambda_grade=4`.  Grades 0--3 have no `k10_*` term.  Grade 3
   uses only `{d0_1,...,d5_1,d0_2,...,d5_2}`.  Column 7 of `A` is the
   later newest variable `k10_3`, correctly absent from `P3`.
3. The V27 six-variable ring of this check does not contain `k10_0`.

This computation therefore neither imposes `z*k10_0-1` nor saturates
by `k10_0`.  The source-open condition is not a generator here, and
it is not projected away.  It first becomes a polynomial-ring
condition on a successor that adjoins a frozen row in which `k10_0`
actually appears, i.e. at Lambda grade 4 on the rank-zero plane.
`SOURCE_COLUMNS` grade 2 does not license a Rabinowitsch generator
in a ring that does not contain the variable.

## 9. Deduplication against V27/K00 history

- V27 R3 (reviewed) owns `J1` as the proper dimension-two rank-`<=1`
  coefficient-base ideal, with the `ncols` census repair 291/60.  It
  does not treat grade-three solvability, `I2(E3)`, or the 2-plane.
- V27 R2 owns `J2` of dimension three and `rank(A)<=2`.  Used here
  only as the ambient of `J1`, freshly recomputed.
- The provisional Sol rank-two note points at this split and is not
  consumed.  In particular `q^4 in J2+I3(E3)` is not used.
- No existing K00/V27 result owns `I2(E3)` over `J1`, the equality
  `R0=J0`, the 2-plane, or emptiness of the rank-exactly-one
  compatible locus.

The AS-fonly `rank<=1` language in unrelated lanes is a different
ring and is not this stratum.

## 10. Controls

| control | result |
|---|---|
| unit `J1+1` | `NF1=0` |
| known proper `(d0_1)` | `NF1=1`, `DIM=5` |
| origin of `J1,R1,J0,R0` | all vanish (`ORIGIN_BAD=0`) |
| `c3[1] += 1` | 30 of 441 `I2(E3)` slots change |
| `C[1,1] += 1` | trips `C=A[:,1..6]` |
| `A[1,1] += 1` | trips `C=A[:,1..6]` |
| `std` versus `slimgb` | mutual reduction on `J1,R1,J0,R0` and the `J1` chart |
| positional loops | `ncols`/`nrows` only |
| R1 Rabinowitsch unit | `NF1=0` |
| J1 Rabinowitsch proper | `NF1=1`, `DIM=2` |
| fresh `J1` versus V27 `BASE2` | equal as ideals |

No `sat()` wrapper was used.  Rabinowitsch ideals were named, built
in a declared ring, reduced by `std`, and checked by the unit/proper
pair above.

## 11. Commands, outputs, resource

Main Fitting process, one Singular invocation, generated from the
atlas singular strings, scratch path `/tmp/k00_g3_rankle1/rankle1.sing`
(SHA-256 `06cee70f144fd33d4147f11b3c9ea3fab5510d9fcea890300110aa3ec8ec7d73`):

```text
wall 0.189 s
ru_maxrss 29753344 bytes (~28.4 MB; macOS ru_maxrss is bytes)
swap not used
rc 0
stdout SHA-256 a0b937aa521c9e3c2d4c8137648f6d6dd7e5c57ef50398d3f79a630445420c91
```

CPU/address-space caps were 55 s / 1 GB; the run did not approach
either.  Subsequent linear-power, Rabinowitsch, pin, and V27-compare
processes were each under 0.02 s and under 6 MB RSS.

`minAssGTZ(J1)` on a dedicated process hit the 58-second wall and
emitted no primdec output.  That is not a verdict on `J1`'s
components.  No AWS packet is required for the theorem of §1; an
optional later packet for `minAssGTZ(J1)` would be a component list
of the incompatible rank-one coefficient-base piece, not a lift.

## 12. Exact blockers and smallest successors

Blockers (typed, not filled by cap or analogy):

- `OPEN`: irreducible / minimal-prime decomposition of `J1`.
- `OPEN`: a rational point of `D(I1(C)) cap V(J1)`.
- The Sol rank-two fourth-power identities remain unreviewed and
  unused.
- No tracked Bezout column for `R1` versus `J0` beyond the four
  explicit fourth powers of the linear generators.

Smallest rank-one successor: none at grade three.  The compatible
rank-exactly-one locus is empty.  Do not launch selected `I2(E3)`
minor charts, and do not impose `k10_0` on an empty set.  The only
optional follow-up on this side is a component list of
`D(I1(C)) cap V(J1)`, which cannot lift through `P3`.

Smallest rank-zero successor: the 2-plane `V(J0)`, in the ring that
first contains the seven literal `(Lambda_grade,row)=(4,1..7)` rows.
Retain `k10_0 != 0` at that grade, where `k10_0` first appears as a
`P6` variable; do not project it away and do not impose it earlier.
`u` remains a free fibre coordinate of `P3` on the plane until a
later grade constrains it.  That is not a full-`P6` job and not a
rank-five job.

## 13. Scope firewall

No rank-two review, no rank five, no full `P6`, no grades after
three, no formal or convergent arc, no Keller pair, no
counterexample, no order-two exclusion, no JC2.  No exit price is
declared.

## Seal (outside the sealed body)

- Body definition: all bytes before the literal `## Seal` heading.
- Body length: `17523` bytes.
- Body SHA-256: `33c9ff079d97933b3c2f59984e2593f4ee70111de8174b0fda063eeb3f08f2dc`.
- Full-file SHA-256: `3e2b13b2f064e28200972a57da87d6daca300144fd2dc36b0f53c6bbc1455cfc`
  (SHA-256 of this complete file after replacing this 64-hex field by zeros).
- Frozen basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.

END_K00_GRADE3_RANKLE1_PRIMARY_GROK46_92E_20260829
