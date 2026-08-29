# Hostile different-model review — K00 valuation-six hand obstruction

Reviewer: Grok 4.6, equal-standing independent adversarial reviewer
Date: 2026-08-29
Frozen campaign basis: `93db679d3160c957b0610297afccc1f2fad53125`
  (`git rev-parse HEAD` at start of work)
Output: this file only. Scratch lived under `/tmp/k00_r6_rev_grok46/`.
No canonical, case, ladder, guardrail or operations file was edited.
No web, network, commit, push, AWS, remote shell, or `jc2-lean` access.
No exit price is asserted. No heavy CAS: exact `Fraction` polynomial
arithmetic on the frozen 569 tails, the seven V14 multipliers, and a
desk parse of serialized `K_VECTOR`. Producer prose and previous
`PASS` tokens were not used as characteristic-zero evidence.

The producer is not a premise. `Q1`, `Q3`, `D_{K6}^{[2]}`, the
contracted grade-19 coefficient, the five boundary zeros, and the
minimum `d`-degrees were rebuilt from frozen tails and V14
witness / multipliers.

## 0. Binary disposition

```text
REVIEW                                      CONFIRMED
Lambda^6 | d ON D(Jdet[0]) THROUGH 19       CONFIRMED
IDENTITY D_K6^[2] = -4 Q1 - 32 Q3           CONFIRMED
G12 ROWS 1,3 ARE RAW Q1(x)=Q3(x)=0          CONFIRMED
x=0 INCLUDED; NO CHART/SAT REQUIRED         CONFIRMED
19-JET / SAME-SOURCE FORMAL ARC             CONFIRMED
REMAINING POSITIVE VALUATIONS {2,3,4,5}     CONFIRMED ON THE OPENS IN §9
EXISTENCE OF 2,3,4,5 / CLOSURE / JC2        NOT CLAIMED, NOT LICENSED
charge_basis                                ABSENT
```

The charged hand obstruction survives every load-bearing attack
below. Grades 13 through 18 need not be solved. The five V20R2
boundary zeros are part of the displayed source; only `k6[0]=0` is
consumed by the coefficient arithmetic. The unit `k10[0]!=0` and
the exact-valuation open `x!=0` are not consumed.

## 1. Charged inputs (rehashed)

```text
sha256                                bytes  path
93db679d3160c957b0610297afccc1f2fad53125
         frozen campaign HEAD
c9563ced370809e0fe48843ac2ae768dc1decb880f8c8624804148236605ae6b
     11851  xmodel/k00-valuation6-successor-design-sol56-93d-20260829.md
52ca8725c5ca7e8322a2ac8aaca81c69bce75a933ce0aa9151764638f8f23408
     11532  producer body through first BODY-END inclusive
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
     25383  .../tails.json                         (569 terms)
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
     46112  .../compile_contracted_source_v20r2.py
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a
      3624  .../aws_r6b_r2_pass/output/K_VECTOR.txt
d88ed015576f32f3c3211c89a3b33a03736ed395a03c5cfb7ad207eaf0cdf921
       653  .../input/target_K6.txt
cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c
      3125  .../output/CONTRACTED_TARGET.txt
2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c
     29053  .../output/SOURCE_COLUMNS.json
a2147de95bc37e8adb629201e2b39b788b99df3d4586da54af7bd41f269a9f15
      6984  .../output/RESULT.json
87ced4afe1680f11073eb62bda7c7894f297925283557b2ccf0e951daba09e04
         9  V14 LOCAL_UNIT_WITNESS_R1.txt   (= 63*d4+20)
ed096c8246ff96cb5ab621a9a74061b24e1678ff061a98137a067c387969e1e5
       133  V14 UNIT_MULTIPLIER_1.txt
1f8369edbbb10bfbbb155250775399170e696e0fdbe33bb75f54bb5639f78791
        70  V14 UNIT_MULTIPLIER_2.txt
ce8b51a7e9a11f0fa3a3594480fbe3e4b556e9fd0a17cf29175b273474104f0f
        74  V14 UNIT_MULTIPLIER_3.txt
5d9f371cf8302502d05a56effbfe3bbbbeafd28d6dfdad8cf7f1bba3ebb60f18
        32  V14 UNIT_MULTIPLIER_4.txt
135c17e36fd53a438e98c36104e350e6ed362223dfba38e7e927c6dccf65a98e
        29  V14 UNIT_MULTIPLIER_5.txt
93762abdfa9b12b520a47848e55776176d9227eaca253deb80a6a9a13b4c3295
        17  V14 UNIT_MULTIPLIER_6.txt
f552ba471021bfe007070640d62362d6683ebfade6fa95c0371f80c9106fa519
     21826  rge7 Grok review body (dependency, not evidence)
efec8e4e94315afee74dc47f2658fccd9be1d99c078dadbc61f3f88b25235cf3
     14379  higher-valuation preflight body (dependency, not evidence)
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
      1985  FALLACY-v2.md
```

Producer body bytes `11532` and body SHA-256 match the launch pin.
Tails, compiler, `K_VECTOR`, `target_K6`, and V14 witness hashes
match the compiler `EXPECTED` pins and the rge7 custody list.
`RESULT.json` records `jacobian_parameter=Jdet` and
`collision_ideals_not_parameters=["J1","J2"]`. Source columns: 169
labelled, 164 free, five `FIXED_ZERO_BEFORE_SOLVE`

```text
k6_0, k2_0, mu2_0, mu4_0, mu6_0.
```

Declared ring map (FALLACY-v2): coefficient field `Q`; generators
`d0,...,d5` in that order; K00 chart at the Kummer slice `C6=1`

```text
C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3,
C4=(3+d4)/8,   C5=d5, C6=1.
```

Matching names are not the map. Images were substituted into every
frozen tail monomial. Unmapped names raise. Tail load exponents are
0-or-1 in a single slot (569/569); there is no bilinear load sector.

## 2. Attack 1 — source/boundary ledger and grades below 12

**CONFIRMED.**

`SOURCE_COLUMNS.json` serializes, 1-based in the producer’s names,

```text
d_i     series_index 1..19,   first_Lambda_grade = index,
k10     0..17,                first_Lambda_grade = 2+index,
k6      0..13,                first_Lambda_grade = 6+index,  k6_0 FIXED_ZERO,
k2      0..9,                 first_Lambda_grade = 10+index, k2_0 FIXED_ZERO,
mu2     0..5,                 first_Lambda_grade = 14+index, mu2_0 FIXED_ZERO,
mu4     0..3,                 first_Lambda_grade = 16+index, mu4_0 FIXED_ZERO,
mu6     0..1,                 first_Lambda_grade = 18+index, mu6_0 FIXED_ZERO,
Jdet    0..0,                 first_Lambda_grade = 19.
```

No `d_i[0]` column exists. The compiler writes `target_sign=-1` and
scale `1/4` on row 7, so the displayed mixed source

```text
Phi = R(d) + Lambda^2 k10 A10(d) + Lambda^6 k6 A6(d) + Lambda^10 k2 A2(d)
    - Lambda^14 mu2 e2 - Lambda^16 mu4 e4 - Lambda^18 mu6 e6
    - Lambda^19 (Jdet/4) e7
```

is the live sign, not a leading-form convention. Targets occupy only
rows 2, 4, 6, 7.

Independent tail reconstruction, 569 terms, after the chart of §1:

```text
R_i     mindeg (2,2,2,2,2,3,2); constants and linears empty
A10_i   mindeg 2 on every row; constants empty
A6_i    mindeg (1,1,1,2,1,2,1); constants empty
A2_i    mindeg 1 on every row; constants empty
```

Quadratic counts of `R` are `(8,11,9,12,8,0,6)`. Row 6 is cubic at
minimum, so its grade-12 slot is identically zero at `r=6`.

Hypothesis `Lambda^6 | d_i`. Weighted-degree lower bounds:

```text
R            >= 2r = 12
Lambda^2 k10 A10            >= 2+2r = 14
Lambda^6 k6 A6, k6[0]=0     >= 7+ r = 13
Lambda^10 k2 A2, k2[0]=0    >= 11+ r = 17
Lambda^14 mu2               >= 15
Lambda^16 mu4               >= 17
Lambda^18 mu6               >= 19
Lambda^19 Jdet              =  19
```

Every bound is `>=12`. Grades `0` through `11` vanish identically.
The first live raw grade is 12, and the only sector that hits 12
after the boundary zeros is the unloaded quadratic `R^{[2]}(x)`,
`x=(d_0[6],...,d_5[6])`. Cubics of `R` start at `3r=18`. The K6
quadratic `A6^{[2]}` starts at `7+2r=19`. So

```text
G12 = R^{[2]}(x) = (Q1(x), Q2(x), Q3(x), Q4(x), Q5(x), 0, Q7(x)).
```

Precision, not a leak: grades below 12 already vanish from `r>=6`
alone. If `k6[0]` is left free, `Lambda^6 k6 A6^{[1]}` hits grade 12
exactly, not below it. The boundary zero `k6[0]=0` is therefore not
needed for the vanishing of grades `0..11`, and is needed for the
identity `G12=R^{[2]}(x)`. The other four boundary zeros first
appear at grades `>=16` in the raw rows and are not used for this
vanishing.

The 74-column window census is an upper bound on coefficients that
*can* occur in grades 12 through 19, not a solve:

```text
v0..v7 (d[6..13])  48,   a0..a5  6,   b1..b7  7,
c1..c3  3,   m1..m5  5,   n1..n3  3,   o1,J  2.
```

Each cutoff is forced by a minimum-degree plus shift: `a6` starts at
20, `b8` at 20, `c4` at 20, `d[14]` at 20 via `2B(v0,v8)`. Later
serialized V20R2 columns exist and remain in source custody; they
do not enter the hand obstruction.

## 3. Attack 2 — grade-19 contracted census, every load, Jacobian sign/scale

**CONFIRMED.**

V14 witness `h=63*d4+20` and multipliers `u1,...,u6` satisfy the
exact polynomial identity in `Q[d0,...,d5]`

```text
h R_7 - sum_{i=1}^6 u_i R_i  =  0
```

(leftover term count 0). Consequently the mixed residual

```text
Rmix = h Phi_7 - sum_{i=1}^6 u_i Phi_i
```

equals, identically as series and not modulo a quotient,

```text
Rmix = Lambda^2 k10 D10 + Lambda^6 k6 D6 + Lambda^10 k2 D2
     + Lambda^14 mu2 u2 + Lambda^16 mu4 u4
     + Lambda^18 mu6 u6 - Lambda^19 Jdet h/4,
D_k = h A_k7 - sum_{i=1}^6 u_i A_ki.
```

The minus on the Jacobian term is `h*(-Jdet/4)` from `Phi_7`. The
plus on the `mu` slots is `-u_{2j}*(-mu_{2j})`. Independently
reconstructed contracted polynomials match `K_VECTOR` componentwise
and match `target_K6.txt` on `D6`:

```text
component   terms  mindeg  constant
D10           79      3    0
D6            41      2    0          (= target_K6, = K_VECTOR gen(2))
D2            16      2    0
u2             7      1    0
u4             4      1    0
u6             2      1    0
-h/4           2      0   -5
```

`D10` has 27 cubics and 0 quadratics. `D6` has 9 quadratics, 0
linears, 0 constant. `D2` has 8 quadratics, 0 linears. `u2,u4,u6`
have vanishing constants. Serialized `K_VECTOR` gen(7) is `-h/4`,
constant `-5`; the producer’s degree table names the witness `h`
with `h(0)=20`. The coefficient algebra is the same.

With `Lambda^6 | d` and the five boundary zeros,

```text
Lambda^2 k10 D10       >= 2+3r = 20
Lambda^6 k6 D6         >= 7+2r = 19     (equals 19; only b1 D6^[2](x))
Lambda^10 k2 D2        >= 11+2r = 23
Lambda^14 mu2 u2       >= 15+ r = 21
Lambda^16 mu4 u4       >= 17+ r = 23
Lambda^18 mu6 u6       >= 19+ r = 25
Lambda^19 Jdet (h-20)/4 >= 19+ r = 25
```

The only grade-19 terms of `Rmix` are therefore

```text
[Lambda^19] Rmix = b1 D6^[2](x) - 5 Jdet[0].             (3.1)
```

Isolation of the `D6` slot: `k6 = b1 Lambda + b2 Lambda^2 + ...`
and `d = x Lambda^6 + v1 Lambda^7 + ...`, so

```text
k6[1] Lambda * D6^[2](x) Lambda^{12} * Lambda^6  ->  grade 19,
k6[1] * 2 polar_{D6}(x,v1)                         ->  grade 20,
k6[2] * D6^[2](x)                                  ->  grade 20,
k6[1] * D6^[3](x)                                  ->  grade 25.
```

No other homogeneous part of `D6` reaches 19. Load-bearing minima,
each independently nonempty at the claimed degree: if `D10` were
quadratic then `2+2r=14<19`; if `D6` were linear then `7+r=13<19`;
if `D2` were linear then `11+r=17<19`; if `u6(0)` were nonzero then
the `mu6` slot with `mu6[0]=0` would hit grade 19. None occur.

Without `k6[0]=0` the K6 slot starts at `6+2r=18`, and grade 19
picks up an extra `k6[0] * 2 polar_{D6}(x,v1)` term. Equation (3.1)
would fail. That boundary zero is load-bearing for the census.
Dropping `k2[0]=0` still gives `10+2r=22>19`. Dropping `mu2[0]=0`
still gives `14+r=20>19` because `u2` has no constant. The `mu4`
and `mu6` slots remain strictly above 19 with or without their
boundary zeros. The unit `k10[0]!=0` is not used: the bound is
`ord(p10)>=2`.

Characteristic 5 would kill the constant `-5`. The source is `Q`.

## 4. Attack 3 — exact extraction of `D_{K6}^{[2]}`, `Q1`, `Q3`

**CONFIRMED.**

`Q1` and `Q3` are the degree-2 parts of reconstructed unloaded rows
1 and 3 after the chart of §1, not copies of producer formulas and
not the unsaturated `c=C6` slice. Direct extraction:

```text
Q1 =
  3/64   d1*d2 + 3/1024 d0*d3 - 3/64   d1*d4
  -3/128  d2*d3 - 3/2048 d0*d5 + 9/512  d3*d4
  +9/1024 d2*d5 - 3/512  d4*d5,                         (8 terms)

Q3 =
  3/1024 d0*d1 - 9/512  d1*d2 - 9/8192 d0*d3
  +3/256  d1*d4 + 3/512  d2*d3 + 3/8192 d0*d5
  -15/4096 d3*d4 - 15/8192 d2*d5 + 9/8192 d4*d5.        (9 terms)
```

`D_{K6}^{[2]}` is the degree-2 part of reconstructed `D6`, agreeing
with `K_VECTOR` gen(2) and with `target_K6.txt`:

```text
D_K6^[2] =
  -3/32   d0*d1 + 3/8    d1*d2 + 3/128  d0*d3
  -3/32   d2*d3 - 3/16   d1*d4 + 3/64   d3*d4
  -3/512  d0*d5 + 3/128  d2*d5 - 3/256  d4*d5.          (9 terms)
```

Producer-printed polynomials match these three extractions
coefficientwise (leftover `{}` on each). Support of `D_{K6}^{[2]}`
equals the union of the supports of `Q1` and `Q3`; `Q3` carries the
extra monomial `d0*d1`.

Row labels: tails key `"1"` is `Phi_1` (no target); tails key `"3"`
is `Phi_3` (no target). A 1-3 permutation would mix in a different
quadratic and break §5.

## 5. Attack 4 — coefficientwise identity `D_{K6}^{[2]} = -4 Q1 - 32 Q3`

**CONFIRMED.**

In `Q[d0,...,d5]`,

```text
D_K6^[2] + 4 Q1 + 32 Q3  =  0
```

as a dictionary of monomials (leftover term count 0). Equivalent:
`D_{K6}^{[2]} = -4 Q1 - 32 Q3`. This is an identity of these three
extracted polynomials, not a syzygy tautology (the V14 relation
identifies *unloaded* rows, whereas `D6` is contracted from the K6
*load* sector). It is used only after it has been checked.

A point evaluation at `(2,-1,3,5,-7,11)` gives both sides
`-225/64`. Origin evaluation is `0=0`.

## 6. Attack 5 — raw grade-12 rows 1 and 3 impose `Q1(x)=Q3(x)=0`

**CONFIRMED, before any quotient, localization, or saturation.**

After `Lambda^6 | d` and `k6[0]=0`, the seven scalar equations
`G12=0` are the seven polynomials `R^{[2]}(x)=0` in the affine ring
`Q[x0,...,x5]`. Coordinates 1 and 3 of that vector are exactly
`Q1(x)` and `Q3(x)`. Setting them to zero is two polynomial
equations. No `sat()`, no colon, no Rabinowitsch chart, no
`D(x_j)`, no `Proj`, and no localization is invoked or required.

The other five grade-12 coordinates (`Q2,Q4,Q5,0,Q7`) are additional
constraints that a full 19-jet would also satisfy. They are not
used. In particular the quadratic identity `Q6=0` is the empty
polynomial (row 6 has minimum degree 3), not a hidden saturation.

FALLACY-v2 `sat()` wrapping is not in play. If `k6[0]` is not
substituted, grade 12 becomes `R^{[2]}(x)+k6[0] A6^{[1]}(x)`, and
row 1 is no longer `Q1(x)=0`: independently, `A6_1^{[1]}=(3/4)L`
with `L=d1-d3/4+d5/16` nonzero. That mutation is fail-closed.

## 7. Attack 6 — emptiness of `Lambda^6 | d` on `D(Jdet[0])`, including `x=0`

**CONFIRMED.**

Any 19-jet of the V20R2 source with `Lambda^6 | d_i` satisfies
`G12=0` and `Rmix \equiv 0 (mod Lambda^{20})`. The first gives
`Q1(x)=Q3(x)=0`. The identity of §5 then gives `D_{K6}^{[2]}(x)=0`.
Equation (3.1) collapses to `-5 Jdet[0]=0`. Characteristic zero
forces `Jdet[0]=0`, contradicting `D(Jdet[0])`.

At `x=0` one has `Q1(0)=Q3(0)=D_{K6}^{[2]}(0)=0` automatically, and
the same constant `-5 Jdet[0]` remains. The zero transverse 19-jet
is included. This is divisibility `Lambda^6 | d`, not exact
valuation 6, and it subsumes the contracted `r>=7` coefficient
obstruction (there `D6` itself starts at 21).

Opens and boundary zeros, load-bearing versus optional:

```text
required     C6=1 chart, source Q, D(Jdet[0]), k6[0]=0
not used     D(k10[0]), x!=0, a0!=0, D(x_j), Rabinowitsch, sat()
optional     k2[0]=mu2[0]=mu4[0]=mu6[0]=0
             (present in V20R2; not consumed by this coefficient bound)
```

Grades 13 through 18 need not be solved: they are not an input to
`G12` or to the specialized identity (3.1). The contracted formula
is an identity of the mixed residual, always, and `[Lambda^{19}]`
of both sides after the valuation/boundary substitution is a
polynomial identity in the remaining jet coefficients. A full
solution through grade 19 would force that coefficient to vanish.

The producer’s first display retains `k10[0]!=0` and, for exact
valuation six, `x!=0`. Both are mandatory in the V20R2 source
declaration. Neither is consumed. Retaining a superfluous
hypothesis does not falsify the statement.

No new exit price is asserted. FALLACY-v2 flag/place/series,
per-ray charge, `REPRESENTATIVE` versus `FULL_ACTUAL_EXIT`, pole
identities, raw remainder degree, prime-as-derivative, merge-free
M-descent, and target/arrival index are not in play.

## 8. Attack 7 — 19-jet / formal-arc / map scope

**CONFIRMED.**

The charged object is a 19-jet of the exact normalized V20R2 mixed
source: the 140 coefficient equations `(Phi_i, Lambda^n)` for
`1<=i<=7` and `0<=n<=19`, equivalently `G12=0` together with
`[Lambda^{19}] Rmix=0` after the substitutions of §2–§3. A formal
solution of *this same exact source* (any series solution whose
truncation agrees with the V20R2 mixed rows through `Lambda^{19}`)
truncates to a compatible 19-jet, hence is also impossible on
`D(Jdet[0])` under `Lambda^6 | d`.

The converse is unavailable: emptiness of 19-jets does not by
itself exclude a differently truncated source, a different
normalization, a support with `k6[0]` or `k2[0]` a unit, an
algebraic arc of another type, a convergent germ, a polynomial
Keller map, the K00 closure incidence, order two, maximum twelve,
or JC2. Nothing is inferred about sources outside this normalized
client.

## 9. Attack 8 — composition with the reviewed valuation-one result

**CONFIRMED on the intersection below. Not an existence statement.**

Valuation one is a different truncation of the same normalized K00
source. It is used only as already-reviewed incidence, from the
rge7 Grok review on this same frozen basis: complete grade-three
incidence on the plane `Pi`, grade-five projection empty on
`D(k10[0]) ∩ (D(s) ∪ D(t))`, origin of `Pi` typed as
`v(d)>1`. Thus exact valuation one is empty on `D(k10[0])`.

Combined with §7, every compatible 19-jet on

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
D(Jdet[0]) ∩ D(k10[0])
```

has minimum transverse valuation in `{2,3,4,5}`. Scope conditions
that sentence needs, all of them:

1. Coefficient field `Q` (`-5` dies in characteristic 5;
   identity coefficients `-4,-32` are even).
2. Exact normalized V20R2 K00 chart and mixed `Lambda<=19` source.
3. `Jdet` the Jacobian parameter, distinct from `J1,J2`.
4. `D(Jdet[0])` for the `Lambda^6 | d` exclusion.
5. `D(k10[0])` for the valuation-one client. Not required for §7.
6. Five boundary zeros as part of the V20R2 source; of these only
   `k6[0]=0` is consumed by §7.
7. The object is a 19-jet of this truncated system, or a formal
   solution of the same exact source. It is not a polynomial map.
8. “Remaining” is an exclusion of `{1} ∪ {6,7,...} ∪ {∞}`
   on that open. It is not existence, not attainment of 2 or of 5,
   and not a statement that every omitted raw grade vanishes.

Off `D(k10[0])` the grade-five localizer is absent and valuation one
is not excluded by the cited theorem. Off `D(Jdet[0])` the
coefficient `-5 Jdet[0]` is zero and does not obstruct. The
producer’s firewall sentence that the packet “says nothing about
valuations two through five” is the correct non-existence clause
for *this* derivation; the composition above is the strongest
statement the two reviewed packets jointly license.

Floor versus attainment: excluding `r>=6` does not attain `r=5`.
The producer does not claim attainment.

## 10. Mutations and negative controls

All run as exact `Fraction` dictionary arithmetic on the same
extracted polynomials.

```text
control                                         outcome
one D6^[2] coefficient (d0*d1 += 1)             leftover {d0*d1}
coefficient -32 of Q3 changed to -31            leftover 9 terms
Q3 dropped from the combination                 leftover 9 terms
row label Q1 replaced by Q2                     leftover 19 terms
k6[0]=0 not substituted                         G12 += k6[0] A6^[1];
                                                (3.1) gains k6[0]*2 polar(x,v1)
one d_i below grade 6 restored                  R^[2] starts at <12;
                                                D6^[2](d) starts at <12;
                                                (3.1) isolation fails
h(0)=20 changed to 21                           Jacobian coeff -21/4, not -5
target_sign flipped to +1                       Jacobian coeff +5, not -5
Jdet aliased with J1 or J2                      tails contain no such symbol;
                                                RESULT.json forbids the alias
origin x=0                                      Q1=Q3=D6^[2]=0, (3.1)=-5J
point (2,-1,3,5,-7,11)                          both sides of (3.2) = -225/64
```

Every listed mutation changes or fails a claimed identity or a
claimed source ledger. The identity is therefore not an artifact of
an omitted monomial class, a row-label swap, or a copied formula.

The raw G13–G19 polarization table in producer §2 was not expanded
term-by-term. It is a source window consistent with the reconstructed
minima and shifts; it is not an input to the hand obstruction. No
verdict is issued on sequential affine solving of those grades.

## 11. Strongest exact theorem that survives

Work over `Q`. Let `R_i`, `A10_i`, `A6_i`, `A2_i` be the unloaded
and affine load sectors of the frozen 569-term tails after the
normalized K00 chart of §1, and let `h=20+63 d4` and `u1,...,u6` be
the frozen V14 multipliers. Then `h R_7=sum u_i R_i` as polynomials,
and the mixed residual `Rmix` equals the specialized `D_p` identity
of §3. The degree-2 parts satisfy the coefficientwise identity

```text
D_K6^[2] = -4 Q1 - 32 Q3
```

in `Q[d0,...,d5]`, where `Q1,Q3` are the quadratic parts of `R_1,R_3`.

Consequently, in the exact V20R2 mixed source truncated at
`Lambda^{19}`, there is no solution over `Q` of the seven series
equations with

```text
C6=1,
k6[0]=0,
Jdet[0] != 0,
d_i in Lambda^6 Q[[Lambda]]/(Lambda^{20})   for i=0,...,5.
```

The zero transverse 19-jet is included. The conditions `k10[0]!=0`
and `x!=0` are not required for this coefficient argument; they
hold in the V20R2 source and are part of the producer’s displayed
specialization. The remaining four boundary zeros are likewise
present and not consumed. Grades 13 through 18 need not be solved.

Combined with the already reviewed valuation-one client, every
compatible 19-jet on

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
D(Jdet[0]) ∩ D(k10[0])
```

has minimum transverse valuation in `{2,3,4,5}`. This does not
assert that any of those four values occurs, does not exclude a
formal or algebraic arc of a different source type, and does not
close K00 or JC2.

## 12. Firewall

Confirmed: a two-row raw grade-12 plus one-row contracted grade-19
obstruction to `Lambda^6 | d` through grade 19 on `D(Jdet[0])` in
the normalized K00/V20R2 source over `Q`, including `x=0`.
Confirmed: the coefficientwise identity `D_{K6}^{[2]}=-4 Q1-32 Q3`.
Licensed only on the opens of §9: remaining positive transverse
valuations `{2,3,4,5}`.

Not licensed: existence of a 19-jet of valuation 2, 3, 4, or 5; a
formal or algebraic arc of another source; local-ring membership;
K00 closure incidence; order two; maximum twelve; a
characteristic-zero counterexample; JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22926`.
- Body SHA-256: `45a6b8d83df5fa99cc2762bef82fb1ed331bc7bca7aeac9ee59afcf38d63020a`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
