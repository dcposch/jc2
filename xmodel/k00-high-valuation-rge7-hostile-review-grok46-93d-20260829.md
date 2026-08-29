# Hostile different-model review — K00 valuation at least seven through Lambda^19

Reviewer: Grok 4.6, equal-standing independent adversarial reviewer
Date: 2026-08-29
Frozen campaign basis: `93db679d3160c957b0610297afccc1f2fad53125`
  (`git rev-parse HEAD` at start of work)
Output: this file only. Scratch lived under `/tmp/k00_rge7_rev_grok46/`.
No canonical, case, ladder, guardrail or operations file was edited.
No web, network, commit, push, AWS, remote shell, or `jc2-lean` access.
No exit price is asserted. No heavy CAS: exact `Fraction` polynomial
arithmetic on the frozen 569 tails and the seven V14 multipliers, plus
desk parsing of the serialized `K_VECTOR`. Producer `PASS` / `ENDPOINT`
tokens were not used as characteristic-zero evidence.

The producer is not a premise. The contracted identity, minimum
`d`-degrees, boundary orders, odd-row K6 linear forms, and the
coefficient `-5 Jdet[0]` were rebuilt from frozen tails and the V14
unit witness / multipliers.

## 0. Binary disposition

```text
REVIEW                         CONFIRMED
NARROW r>=7 THEOREM            CONFIRMED
RAW-ROW r>=10 ODD-K6 IDENTITY  CONFIRMED (weaker, independent)
r=1 COMBINATION                LICENSED ONLY ON THE OPENS IN §6
K00 CLOSURE / ARC / JC2        NOT CLAIMED, NOT LICENSED
charge_basis                   ABSENT
```

The charged narrow theorem survives every load-bearing attack below.
The Result-section slogan that only valuations `2,...,6` remain is
honest solely after the scope intersection in §6; it is not a
closure theorem, not an attainment statement, and not licensed off
`D(Jdet[0])` or off the reviewed valuation-one client.

## 1. Charged inputs (rehashed)

```text
sha256                                bytes  path
93db679d3160c957b0610297afccc1f2fad53125
         frozen campaign HEAD
b3861ac2623b89aa70d44af67d6821d60fa5b8f39dbdf23c5d6f27318f54fa31
      6729  xmodel/k00-high-valuation-rge7-coordinator-provisional-sol56-93d-20260829.md
3c3a3f98bc86939b293e6f03dfe9f2cff406fdbb97eab511b294e7314f04bf03
      6464  producer body through first BODY-END inclusive
1148e7836458966aa382dae27cdbfd7c9d156b53911ba9f48efdb6eb9649edec
      3496  .../PREREGISTRATION_V20R2_SOURCE_COMPILER.md
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
     46112  .../compile_contracted_source_v20r2.py
9e304f58310fda008a3930b21bf0f49bc198322ee5dd98d805af04068ed5b3c8
      2402  .../RESULT_V20R2.md
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a
      3624  .../aws_r6b_r2_pass/output/K_VECTOR.txt
cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c
      3125  .../output/CONTRACTED_TARGET.txt
a2147de95bc37e8adb629201e2b39b788b99df3d4586da54af7bd41f269a9f15
      6984  .../output/RESULT.json
2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c
     29053  .../output/SOURCE_COLUMNS.json
35de48fc3ac4943843fbbb027e747f7e4c775b7b936a6d523efdcb611921bec5
       293  .../output/source_replay.stdout
50095796c650191ec5d093dd7a7b95a5105b5d6156b38a8ea289f57733de659d
       176  .../output/contract_replay.stdout
b205bd9fae6e82b9727511d85841eba3225147453d83b879aefdbc2a61c16f56
      4128  .../HARVEST_EVIDENCE_R2.sha256
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
     25383  .../tails.json
6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8
         —  canonical tails digest (sort_keys, 569 terms)
87ced4afe1680f11073eb62bda7c7894f297925283557b2ccf0e951daba09e04
         9  V14 LOCAL_UNIT_WITNESS_R1.txt   (= 63*d4+20)
6c4ebd6d61189e0f80fd9021edd509cbb323826774644d92828a0badd0943a29
     24999  xmodel/max12-812-order2-k00-v8-v9-hostile-review-grok-20260827.md
fbe5b580662b7f77326c61f5fec54b3a9a2059f1684f52994fee8652efc49448
      5984  xmodel/k00-grade4-rank0-plane-coordinator-integration-sol56-20260829.md
917207a71e7aea537e0a079205dfa91fec853a4b00bff01ceaffe597701117c7
      5663  grade-four coordinator body
1ec95a45d97658fbd3b2464831deb768ee19574feefc8bb9dcac656d5f79bb2e
     25987  xmodel/k00-grade4-rank0-plane-opus5-hostile-review-grok46-40c-20260829.md
7e9e591672a9f1a6b1e8b5bc56053947fa3a665b8541d91e20d90894e465f546
      6799  xmodel/k00-grade5-rank0-plane-coordinator-integration-sol56-20260829.md
11d0d69ddeff40ad7d26ee360fb7035b77c9909af06ad3507e5c3ba6c1510f6b
      6478  grade-five coordinator body (matches its seal)
fa37693c353d24d2202a2113ae5150d5df9727b678b75f5f2dfeddf80055bb24
     34733  xmodel/ideation-20260829T1517Z-crosspoll-grok46.md
d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860
      6355  xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md
0f2debfecf1ae127db20de8a806e93842a0f333fce3592a3e09231a48ad3b53b
      4040  DESIGN_ERRATUM_V20R1.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
      1985  FALLACY-v2.md
```

Producer custody hashes for tails, compiler, `RESULT_V20R2.md`, and the
V8/V9 review match the independent recomputation. Harvest manifest:
23/23 paths byte-agree with `HARVEST_EVIDENCE_R2.sha256`. Compiler
`EXPECTED` pins for tails, canonical tails, preregistration, V14 `h,u_i`,
and V21 load/target files match the bytes used below. V20R2
`RESULT.json` records `jacobian_parameter=Jdet` and
`collision_ideals_not_parameters=["J1","J2"]`.

Declared ring map (FALLACY-v2): coefficient field `Q`; generators
`d0,...,d5` in that order; K00 chart at the Kummer slice `C6=1`

```text
C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3,
C4=(3+d4)/8,   C5=d5, C6=1.
```

Matching names are not the map. Images were substituted into every
frozen tail monomial. Unmapped names raise.

## 2. Attack 1 — contraction, signs, shifts, boundary zeros, `Jdet`

**PASS.**

Write the seven mixed rows as in the V20R2 compiler and the V20R1
erratum, 1-based:

```text
Phi_i = R_i(d) + p10 A10_i(d) + p6 A6_i(d) + p2 A2_i(d)
        - Lambda^(12+i) delta_i,
p10=Lambda^2 k10,  p6=Lambda^6 k6,  p2=Lambda^10 k2,
delta=(0, mu2, 0, mu4, 0, mu6, Jdet/4).
```

Compiler `target_specs` uses `target_sign=-1` and scale `1/4` on row 7,
so the displayed minus sign is the live source, not a leading-form
convention. Targets live only on rows 2, 4, 6, 7. `Jdet` is a single
grade-19 column `Jdet_0`; it is not `J1` or `J2`, and the tails contain
no Jacobian symbol.

Frozen V14 witness `h=63*d4+20` and multipliers `u1,...,u6` satisfy
the exact polynomial identity, after independent tail reconstruction,

```text
h R_7 - sum_{i=1}^6 u_i R_i  =  0
```

in `Q[d0,...,d5]` (`BASE_RELATION_ZERO`, leftover term count 0).
Source-replay stdout independently prints `K00_V20R2_BASE_RELATION=1`
and `K00_V20R2_H0=20`. Consequently the scalar

```text
Rmix = h Phi_7 - sum_{i=1}^6 u_i Phi_i
```

collapses exactly, not modulo a quotient, to the V20R1 `D_p`
specialization

```text
Rmix = p10 D10 + p6 D6 + p2 D2
     + Lambda^14 mu2 u2 + Lambda^16 mu4 u4
     + Lambda^18 mu6 u6 - Lambda^19 Jdet h/4,
D_k = h A_k7 - sum_{i=1}^6 u_i A_ki.
```

The minus on the Jacobian term is `h * (-Jdet/4)`, from `Phi_7`. The
plus on the `mu` terms is `-u_{2j} * (-mu_{2j})`. Odd-row multipliers
`u1,u3,u5` have nonzero constants; they do not enter the `mu` slots.

Serialized `K_VECTOR` is not `(D10,D6,D2,u2,u4,u6,h)`. The compiler
writes

```text
DK10*gen(1)+DK6*gen(2)+DK2*gen(3)+u2*gen(4)+u4*gen(5)+u6*gen(6)-(h/4)*gen(7).
```

Component 7 is `-h/4`, constant `-5`. The producer's degree table names
`h` with `h(0)=20`; that is the witness, not the serialized seventh
coordinate. The coefficient algebra is the same.

`SOURCE_COLUMNS.json`: 169 labelled columns, 164 free, five
`FIXED_ZERO_BEFORE_SOLVE`

```text
k6_0, k2_0, mu2_0, mu4_0, mu6_0.
```

Every `d_i` starts at `series_index=1`, `first_Lambda_grade=1`. There
is no `d_i[0]`. Transverse valuation 0 is not a source column.
Shifts: `k10` by 2, `k6` by 6, `k2` by 10, `mu2` by 14, `mu4` by 16,
`mu6` by 18, `Jdet` by 19. Boundary zeros therefore give

```text
ord(p10)>=2,  ord(p6)>=7,  ord(p2)>=11,
ord(Lambda^14 mu2)>=15,  ord(Lambda^16 mu4)>=17,
ord(Lambda^18 mu6)>=19,  ord(Lambda^19 Jdet)=19.
```

On `D(k10[0])` the first is equality. The r>=7 bound uses only
`ord(p10)>=2`.

## 3. Attack 2 — independent minimum `d`-degrees and `h(0)`

**PASS. No missed degree-zero or degree-one term. No cancellation
that drops a claimed minimum.**

Independently reconstructed from the 569 tails, then compared with
V21 `target_K*.txt` and with a round-trip parse of `K_VECTOR.txt`
(151 terms, reconstructs the file bytewise):

```text
component   terms  mindeg  constant           match K_VECTOR  match V21
D10           79      3    0                  True            True
D6            41      2    0                  True            True
D2            16      2    0                  True            True
u2             7      1    0                  True            (V14 u2)
u4             4      1    0                  True            (V14 u4)
u6             2      1    0                  True            (V14 u6)
-h/4           2      0    -5                 True            h=20+63 d4
```

Degree histograms: D10 has 27 cubics and nothing below; D6 has 9
quadratics; D2 has 8 quadratics. Linear parts

```text
u2^[1] = 21 d1 - 21/4 d3 + 21/16 d5 = 21 L(d),
u4^[1] = 84 d1 - 43 d3 + 65/4 d5,
u6^[1] = -147 d3 + 339/2 d5,
(-h/4)^[1] = -63/4 d4,
L(d) = d1 - d3/4 + d5/16.
```

`u1,u3,u5` have constants `-25/256, -15/32, -5/2` and are not claimed
to have minimum degree 1. Their constants feed `D_k` and cancel in
D6/D2/D10 down to the displayed minima: D6 is not estimated from the
K6 stencil, it is the contracted polynomial. The V9 load-normal
stencil (`k6` minima `1,1,1,2,1,2,1`) is a per-row lower bound, not a
substitute for `D6`. Using the stencil as if it were `D6` would
falsely suggest a linear contracted K6 term and would break r=7;
that leak is not present in the serialized contraction.

Uncontracted source, same reconstruction:

```text
R_i     mindeg (2,2,2,2,2,3,2); all constants and linears empty
A10_i   mindeg 2 on every row; constants empty
A6_i    mindeg (1,1,1,2,1,2,1); constants empty
A2_i    mindeg 1 on every row; constants empty
```

This agrees with the V8/V9 hostile review (unloaded constants/linears
vanish; load stencil as above) and with the producer ledger. R6 has
minimum degree 3, which is stronger than “at least two”.

`h(0)=20` is the constant of the frozen 9-byte witness, the constant
of the reconstructed polynomial, and the source-replay print. Then
`(-h/4)(0)=-5`. Characteristic 5 would kill that constant; the source
is `Q`.

## 4. Attack 3 — order inequalities at `r=7` and the coefficient of `Lambda^19`

**PASS.**

Hypothesis: every `d_i` is divisible by `Lambda^r` with `r>=7`. Total
degree times `r` is the correct conservative bound (weighted
homogeneity is stronger on some monomials and is not used). With the
V20R2 boundary zeros,

```text
p10 D10                 2+3r = 23
p6  D6                  7+2r = 21
p2  D2                 11+2r = 25
Lambda^14 mu2 u2       15+ r = 22
Lambda^16 mu4 u4       17+ r = 24
Lambda^18 mu6 u6       19+ r = 26
Lambda^19 Jdet (h-20)  19+ r = 26
```

Every displayed order is strictly greater than 19. The only grade-19
term of `Rmix` is therefore

```text
- Lambda^19 Jdet[0] h(0)/4 = -5 Jdet[0] Lambda^19.
```

The grade-19 contracted equation forces `Jdet[0]=0` in characteristic
zero, contradicting `D(Jdet[0])`. The zero transverse 19-jet is
included: then every positive-`d` summand vanishes and the same
constant remains. This is divisibility `Lambda^7 | d_i`, not exact
valuation 7.

Load-bearing minima, each independently nonempty at the claimed
degree: if D10 were quadratic then `2+2r=16<19`; if D6 were linear
then `7+r=14<19`; if D2 were linear then `11+r=18<19`; if `u6(0)`
were nonzero then, with `mu6[0]=0`, the `mu6` slot would hit grade
19. None of those occur.

The producer writes `ord(p10)=2` because `k10[0]` is a unit. That
equality needs `D(k10[0])`. The inequality used in the bound is
`ord(p10)>=2`, which holds without the unit. The five boundary zeros
are likewise unnecessary for the contracted r=7 arithmetic: dropping
them still gives

```text
6+2r=20,  10+2r=24,  14+r=21,  16+r=23,  18+r=25,
```

all `>19`. The strongest coefficient theorem therefore does not
consume the boundary zeros or the `k10` unit. The V20R2 source
includes both; the producer’s displayed statement is a valid
specialization.

Unloaded rows individually have order `>=2r=14` at r=7, below 19.
They cancel in `Rmix` by the polynomial syzygy, not by an order
count. That cancellation was checked as a polynomial identity, not
as a truncated series identity.

## 5. Attack 4 — raw-row `r>=10` odd K6 identity

**PASS as a weaker independent check. Not a substitute for r=7.**

Let `L(d)=d1-d3/4+d5/16`. Direct extraction of the degree-1 part of
the reconstructed K6 load sector, agreeing with V21 `load_K6.txt`:

```text
A6_1^[1] =  (3/4)    L(d),
A6_2^[1] =  (3/1024) d0 - (3/256) d2 + (3/512) d4,   (even, not a multiple of L)
A6_3^[1] = -(3/32)   L(d),
A6_4^[1] =  0,
A6_5^[1] = -(3/512)  L(d),
A6_6^[1] =  0,
A6_7^[1] = -(3/4096) L(d).
```

Four odd-row identities hold as polynomial equalities, leftover `{}`.
Rows 4 and 6 have no linear K6. Load-sector constants vanish on all
seven K6 rows. The remaining linear K6 coordinate is the even form
on row 2; `mu` coefficients occupy only rows 2, 4, 6 and cannot
alter rows 1 and 7.

If every `d_i` is divisible by `Lambda^10`, then through grade 19 the
surviving nontarget source terms are exactly `p6 A6^[1](d)`:

```text
R_i            >= 2r = 20
p10 A10        >= 2+2r = 22
p2  A2         >= 11+r = 21
p6  A6^[>=2]   >= 7+2r = 27
p6  A6^[1]     >= 7+r  = 17   (grades 17,18,19 live)
```

The threshold `r>=10` is sharp: at `r=9` the unloaded rows start at
18. Row 1 has no target, so the grade-19 coefficient is
`(3/4) theta=0` with `theta=[Lambda^19](p6 L(d))`. In characteristic
zero, `theta=0`. Row 7 at the same grade is

```text
-(3/4096) theta - Jdet[0]/4 = 0,
```

hence `Jdet[0]=0`. Characteristic 2 or 3 would break `3/4`; the
source is `Q`. This confirms the high end of the contracted argument
and does not reach r=7.

## 6. Attack 5 — combination with the reviewed valuation-one client

**The producer may honestly conclude that the remaining positive
transverse valuations are `2,...,6`, and only on the intersection
below. As a slogan on “this source” without those opens, no.**

Valuation one is a different truncation of the same normalized K00
source. The binding objects, used only as already reviewed
incidence, are:

- rank-five / rank-at-most-one coordinator: complete grade-three
  incidence `V(B,P3)=Pi × A^6_u` with

  ```text
  Pi: (d0_1,...,d5_1)=(2s, t/8, s, t, s, 2t);
  ```

- grade-four coordinator, Grok review `PASS_WITH_REPAIR`: closed form
  on that plane, radical `(RA,RB,z k-1)`, no grade-four kill;

- grade-five coordinator, Grok `G5-COLLAPSE PASS_WITH_REPAIR`:
  projection of the reduced grade-five locus in `D(k10[0])` onto
  `(s,t)` is the origin, fibre nonempty. Fable 5’s two-input primary
  headline `CONDITIONAL BRANCH KILL = NOT AVAILABLE` is the nonempty
  fibre, not a refutation of the projection. The producer cites the
  coordinator open `D(k10[0]) ∩ (D(s) ∪ D(t))`, which is the correct
  object.

Reviewed source typing of the valuation-one prefix: nonzero leading
block `x`, `k10[0]!=0`, `C6=1`. The origin `s=t=0` is `v(d)>1`, not
a valuation-one point. Therefore valuation exactly one is empty on
`D(k10[0])`. Combined with §4, every compatible 19-jet on the
intersection

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
D(Jdet[0]) ∩ D(k10[0]),
```

has minimum transverse valuation in `{2,3,4,5,6}`. Scope conditions
that sentence needs, all of them:

1. Coefficient field `Q` (the constant `-5` dies in characteristic 5;
   the raw-row `3/4` dies in characteristics 2 and 3).
2. Exact normalized V20R2 K00 chart and mixed `Lambda<=19` source,
   or equivalently the contracted identity through grade 19.
3. `Jdet` the Jacobian parameter, distinct from `J1,J2`.
4. `D(Jdet[0])` for the r>=7 exclusion.
5. `D(k10[0])` for the valuation-one client. Not required for r>=7.
6. Complete grade-three incidence, so every valuation-one leading
   vector lies on `Pi`.
7. Grade-five projection theorem on `D(k10[0]) ∩ (D(s) ∪ D(t))`,
   together with the typing that `s=t=0` is not valuation one.
8. Five boundary zeros as part of the V20R2 source (present;
   optional for the contracted r>=7 bound itself).
9. The object is a 19-jet of the truncated system, not a formal
   arc, algebraic arc, polynomial map, germ, order-two
   configuration, maximum-twelve configuration, K00 closure, or
   JC2.
10. “Remaining” is an exclusion of `{1} ∪ {7,8,...} ∪ {∞}` on that
    open. It is not existence, not attainment of 2 or of 6, and
    not a statement that every omitted grade vanishes.

Off `D(k10[0])` the grade-five localizer is absent and valuation one
is not excluded by the cited theorem. Off `D(Jdet[0])` the r>=7
coefficient is zero and does not obstruct. The producer’s first
display already has `Jdet[0]!=0`; the combination paragraph must
keep both opens.

## 7. Attack 6 — jet/arc, divisibility, opens, characteristic

**PASS on the charged theorem. One wording leak in the equivalently
sentence, not a mathematical leak.**

- Formal 19-jet versus arc. The charged object is the 140 coefficient
  equations `(Phi_i, Lambda^n)`, `1<=i<=7`, `0<=n<=19`, equivalently
  the grade-19 coefficient of `Rmix`. Writing `d_i in Lambda^7
  Q[[Lambda]]` means those 19-jets have `d_{i,1}=...=d_{i,6}=0`. It
  does not exclude a formal or algebraic arc, and the producer’s
  firewall says so.
- Exact valuation versus divisibility. The hypothesis is
  divisibility, including the zero series. The Result sentence
  “every compatible nonconstant K00 jet would have transverse
  valuation at most six” is slightly loose: the zero transverse
  19-jet is also excluded on `D(Jdet[0])`, and “nonconstant” is not
  a source predicate. The first display is the precise statement.
- Opens. `D(Jdet[0])` is load-bearing for r>=7. `D(k10[0])` is
  load-bearing for valuation one and not for r>=7.
- Characteristic. Source `Q`. The displayed coefficient `-5 Jdet[0]`
  is nonzero in `Q`. No modular reduction was used as evidence.
- Floor versus attainment. Excluding `r>=7` does not attain `r=6`.
  The preflight table in producer §3 is correctly labelled a
  preflight: at `r=6` the contracted K6 slot hits grade 19, and
  earlier raw rows are live.
- Not a K00 closure theorem, not JC2. Agreed.

FALLACY-v2 items not in play: flag/place/series, per-ray charge,
`REPRESENTATIVE` versus `FULL_ACTUAL_EXIT`, pole identities, `sat()`,
raw remainder degree, prime-as-derivative, merge-free M-descent,
target/arrival index. No exit-price declaration.

## 8. Strongest exact theorem that survives

Work over `Q`. Let `R_i`, `A10_i`, `A6_i`, `A2_i` be the unloaded and
affine load sectors of the frozen 569-term tails after the normalized
K00 chart of §1, and let `h=20+63 d4` and `u1,...,u6` be the frozen
V14 multipliers. Then `h R_7=sum u_i R_i` as polynomials, and the
mixed residual `Rmix` equals the specialized `D_p` identity of §2.
The contracted vector has minimum total `d`-degrees
`(3,2,2,1,1,1,0)` in `(D10,D6,D2,u2,u4,u6,h)` with `h(0)=20` and
serialized seventh component `-h/4`.

Consequently, in the exact V20R2 mixed source truncated at
`Lambda^19`, there is no solution over `Q` of the seven series
equations with

```text
C6=1,
Jdet[0] != 0,
d_i in Lambda^7 Q[[Lambda]]/(Lambda^20)  for i=0,...,5.
```

The five boundary zeros and the condition `k10[0]!=0` are not
required for this coefficient argument; they hold in the V20R2
source and are part of the producer’s displayed specialization.
The same vanishing on `D(Jdet[0])` follows from the weaker raw-row
odd-K6 identity under the additional restriction `r>=10`.

Combined with the already reviewed valuation-one client — complete
grade-three incidence on `Pi`, grade-five projection empty on
`D(k10[0]) ∩ (D(s) ∪ D(t))`, origin of `Pi` typed as `v(d)>1` —
every compatible 19-jet on

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
D(Jdet[0]) ∩ D(k10[0])
```

has minimum transverse valuation in `{2,3,4,5,6}`. This does not
assert that any of those five values occurs, does not exclude a
formal arc or a polynomial map, and does not close K00 or JC2.

## 9. Cheapest next test

Do not rerun V20R2 and do not launch a common-source elimination.
The first contracted collision below r=7 is r=6: with the boundary
zeros,

```text
p6 D6  hits  7+2*6=19,
p10 D10 starts at 20,
all mu slots and (h-20) start at >=21.
```

Grade 19 of `Rmix` at exact valuation 6 is the single linear
constraint `k6[1] D6^[2](x) = 5 Jdet[0]` on the leading vector `x`
and on `k6[1]`. That equation does not kill `D(Jdet[0])` by itself
(`D6^[2]` has nine nonzero quadratics). The cheap next producer is
the exact associated-graded seven-row system at exact valuation 6,
with projective leading-vector cover, the five boundary zeros
substituted before solve, and this contracted grade-19 relation
kept as a linear constraint on `k6[1]`. Run on AWS if it uses CAS.
The remaining values `r=2,3,4,5` are separate covers; r=6 is the
smallest new algebra.

## 10. Firewall

Confirmed: a one-row contracted coefficient obstruction to
`Lambda^7 | d` through grade 19 on `D(Jdet[0])` in the normalized
K00/V20R2 source over `Q`. Confirmed, weaker: the odd-row K6
identity at `r>=10`. Licensed only on the opens of §6: remaining
positive transverse valuations `{2,3,4,5,6}`.

Not licensed: existence of a 19-jet of valuation 2, 3, 4, 5, or 6;
a formal or algebraic arc; local-ring membership; K00 closure
incidence; order two; maximum twelve; a characteristic-zero
counterexample; JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21826`.
- Body SHA-256: `f552ba471021bfe007070640d62362d6683ebfade6fa95c0371f80c9106fa519`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
