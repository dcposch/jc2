# Certificate slice: three two-place obstruction cores

Status: **COMPLETE**.  All listed replay, perturbation, custody, and structural
checks passed before sealing.

## 0. Result and scope

The three deaths do share one filtered obstruction-map construction, but they
do **not** share one stable numerical minor.  The precise outcome is

```text
FILTRATION-PAGE-RULE;
NO UNIVERSAL FINAL MINOR FROM (d_s,u_s,V_s,delta,weights) ALONE.
```

The common object is obtained by ordering the necessary rows as

```text
incidence < outer order-zero facts < pole < Jacobian < localization,
```

homogenizing affine rows with one constant column, and eliminating only
nonzero rational `Q*` pivots.  The first nonzero obstruction appears on
different pages: the common-`h3` incidence page for `D=108`, the stage-4
pole/Jacobian page for `(99,66), delta=2` (Jacobian `t`-power 4, pole-local
power 8), and a pole Schur page whose construction reaches normalized
`t`-power 8 for `(99,66), delta=5/2`.

Here “minimal certificate” has a deliberately checkable meaning: zero
multipliers are pruned after back-substitution through the **fixed charged
pivot order**, and inclusion-minimality is asserted only where the replay has
leave-one-out witnesses or a unique square-block dual.  It does not mean a
globally sparsest syzygy under arbitrary changes of generators.  Several charged
interfaces hard-code a quotient without serializing its inverse; those
pre-quotient lifts are typed `OPEN`, rather than silently treated as row
identities.

| kill | literal certificate boundary | retained rows by family `(I,O,P,J,L)` | audited DAG | deepest normalized `t` | live `A2/A3/B2` | `T2/T3` |
|---|---|---:|---|---:|---|---|
| `(99,66), delta=2` | raw selected rows, fixed face exposed | `(1,0,4,3,0)` = **8** | **106** transitive nodes inside 128 scheduled candidates | 8 | none | none |
| `(99,66), delta=5/2` | post-outer-`D2`, declared common-`h3` map | `(0,0,1,6,0)` = **7** | 36-row joint DAG; `D1` lifts 38/43; `h3` audits 11/17 | 8 (`s^16`) | none | none |
| `D=108, delta=3` | seven-coordinate post-major common-`h3` chart | `(9,0,0,0,1)` = **10** | all seven `Q*` pivots in the nine incidence rows | 8 | none | none |

`I,O,P,J,L` mean incidence, outer, pole, Jacobian, and localization.  The
`(99,66)` constants are units already over `Q`; adjoining the declared
`rho != 0` or `c != 0` wrapper changes neither identity and gives that wrapper
coefficient zero.  No `J0` factor occurs or is divided by.  The `D=108` death,
by contrast, genuinely uses `c != 0` through `L=Zc*c-1`.

This is a certificate **slice** of the declared necessary charts.  It is not a
claim about an uncovered ambient chart, an exit price, or the unrestricted
Jacobian conjecture.

## 1. Custody, rings, and trace rule

### 1.1 Frozen input custody

Before any algebra, the lane receipt
`xmodel/two-place-obstruction-core-sol56-20260903.run.v2` was parsed with
`awk`: its paired `charged_input_i_sha256` and
`charged_input_i_basename` fields generated the `sha256sum -c` manifest for
`/tmp/jc2-lane.C9HiZU/inputs`.  All **16/16** entries returned `OK`.  No digest
was transcribed into the check.  The running Opus lane
`minor-residue-formula-opus5` was not opened; only its already sealed charged
report and clean-room engine artifacts were used.

The `(99,66)` specialization throughout is exactly the gated tuple

```text
M=(-66,77,97),  d=(99,33,11,1),  V=(8,8),
top h3 = w^3(w-1)^8.
```

For `D=108` the corresponding data used by the standalone incidence replay are

```text
d=(108,36,9,1),  (u3,v3)=(2,7),  V=(7,7),
top h3 = w^2(w-1)^7,  primitive order weights (2,3).
```

Each script declares its polynomial ring over `Q`.  `rho`, `c`, and the jet
variables are forbidden pivot variables.  A `Q*` pivot is accepted only when
the chosen variable occurs as a pure linear monomial with coefficient in
`Q*`; hence no branch-dependent denominator is hidden.

### 1.2 Backward DAG and certificate lift

Write a pivot source row as

```text
R_v = a_v x_v + b_v,   a_v in Q*,   x_v = -b_v/a_v.
```

When a later row `T` contains `x_v`, substitution is recorded as the exact
row operation

```text
T|_{x_v=-b_v/a_v}
  = T - ((T-T|_{x_v=-b_v/a_v})/R_v) R_v.
```

The multiplier is kept symbolically.  Repeating this operation constructs a
DAG edge from the later row to every pivot row it consumes.  If the terminal
normal form is `q in Q*`, division of the accumulated row combination by `q`
gives `1=sum c_i R_i`.  Rows with final multiplier zero are then pruned.  This
separates three numbers that the old ledgers conflated:

1. scheduled candidate rows;
2. recursive dependency nodes actually reached;
3. nonzero source rows in the final certificate.

The same procedure is used for outer zero-facts.  In particular, the
weight-93 `B1` `D1` block has boundary columns

```text
(r,q)=(3,21),(7,18),(11,15),(15,12),(19,9),(23,6),(27,3),(31,0)
```

and row entries `binom(q,k)`.  Its exact lift of the first boundary coordinate
is

```text
B1c_3_21 = (374/19683)D1_1 -(20/729)D1_2 +(166/6561)D1_3
           -(112/6561)D1_4 +(55/6561)D1_5 -(2/729)D1_6
           +(1/2187)D1_7.
```

The `D1_0` coefficient is zero.  In the engine's sequential lex path this is
the two-step chain

```text
B1c_3_21 = -B1c_7_18/7     (D1_6, pivot coefficient 5103),
B1c_7_18 = 0                (D1_7, pivot coefficient -2187/7).
```

These rows are genuine outer **zero-facts for `B1`**, not appearances of a
live `A2`, `A3`, or `B2` coefficient.

## 2. Kill A: `(99,66), delta=2`

### 2.1 Exact inner range and DAG

The declared place is

```text
w = u*t^2 + zeta*t^3,
```

and is kept distinct from both the major flag parameter and the cover series.
The clean-room derivation proves that, after the order preblock and through
`t^21`,

```text
KF=K2^3,                 KG=K2^2+t*KB1*K2.
```

`A2` and `B2` begin only at outer level 21 and `A3` at 53, whereas every row
in this core has `t`-power at most 8.  Thus their absence is an exact support
statement, not a truncation guess (`g9966-independent-engine-opus5-20260903.md:
150-174`).

The selected source reconstruction first exposes the fixed equality
coefficient as the incidence row

```text
I_face = face+8 = 0,
```

instead of baking in `face=-8`.  It then reconstructs the low `B1` support
before `D2/D1`, replays charged pivots, and reduces
`stage4_J_d159_k35` to `6264`.

The broad candidate pool has 128 rows: one face row, 90 touched `B1-D2`
coordinate zero rows, eight weight-93 `B1-D1` rows, 28 earlier joint pivots,
and the terminal row.  Recursive dependency pruning reaches 106 nodes.  Final
multiplier pruning is far stronger: all `D2/D1` multipliers cancel and only
eight raw rows remain, with family counts

```text
incidence 1, outer 0, pole 4, Jacobian 3, localization 0.
```

The seven non-face rows are also the exact quotient DAG after the fixed face
and the order zero-facts are imposed.  No `A2/A3/B2` symbol occurs in their
raw support, and no `T2/T3` row exists in the ledger.  The deepest row is the stage-4 pole row at
local/normalized power 8.  The source chronology contains more pivots than
the recursive closure; rows outside that closure are not called ancestors.
Ancestors whose final multipliers cancel—including the 98 outer rows—remain
counted in the 106-node DAG but not in the eight-row certificate.

### 2.2 Certificate and controls

Abbreviate

```text
a=K2c_5_21,  b0=K2c_6_20, b1=K2c_6_21,
c0=K2c_7_19, c1=K2c_7_20, c2=K2c_7_21, h=Hc_7_4,
C3=a/512-9*rho*u/64,
C2=a^2/4096-9*a*rho*u/256-b0/512+b1/512
   +81*rho^2*u^2/64-81*rho^2/256-21*u^3/128-3483*u/1856,
C1=-45*h/512+a^3/32768-27*a^2*rho*u/4096-a*b0/2048+a*b1/2048
   +243*a*rho^2*u^2/512-81*a*rho^2/1024-21*a*u^3/512
   -3483*a*u/14848+9*b0*rho*u/256-9*b1*rho*u/256
   +c0/512-c1/512+c2/512-729*rho^3*u^3/64
   +729*rho^3*u/128+189*rho*u^4/64+218151*rho*u^2/14848
   +2848*rho/2465.
```

The exact inclusion-minimal seven-row identity in the fixed-face/support
quotient is

```text
1 = (1/6264)*stage4_J_d159_k35
  + C1*stage1_G_local5_coord0
  - (991*rho/177480)*stage1_J_d162_k36
  + C2*stage2_G_local6_coord0
  + (u/174)*stage2_J_d161_k36
  + C3*stage3_G_local7_coord0
  + (1/64)*stage4_G_local8_coord0.
```

Before fixing the face, there is one additional term
`C_face*(face+8)`, where the replay computes

```text
C_face=cancel((1-sum(the seven displayed multipliers*raw rows))/(face+8))
```

and asserts exact polynomial division.  The unabridged (large) `C_face` is
emitted by `--multipliers`.  This eight-row raw identity is inclusion-minimal
on its displayed fixed-ledger support: a rational leave-one-out common zero is
checked for every row.  Global sparsity over alternative charged rows remains
`OPEN[ALTERNATIVE-LEDGER-SPARSE-SYZYGY]`.

This is not the invalid shorthand `raw(stage4_J_d159_k35)/6264=1`; the script asserts
that shorthand is false before back-substitution.  The fully expanded
coefficients are emitted deterministically with `--multipliers`, while the
ordinary run prints the row names and family counts.  No coefficient has a
`rho` denominator.  Since the resulting element is already `1` in `Q[...]`,

```text
1 = previous identity + 0*(Zrho*rho-1)
```

is the requested localized version.

The perturbation control replaces the stage-4 pole source by

```text
stage4_G_local8_coord0 - face^2.
```

The frozen certificate becomes `1-face^2/64`, hence is not the identity; at
`face=-8` it evaluates to zero.  Together with `all B1c=0`, this is an
explicit common zero of the perturbed source slice.  Thus the test changes
the ideal, not merely a pretty-printed normal form.

Replay:

```bash
timeout 1800 python3 box/obscore-20260903/delta2_certificate.py
timeout 1800 python3 box/obscore-20260903/delta2_certificate.py --multipliers
```

The script mechanically verifies the charged `stage4.json` digest from the
lane receipt before using its pivot ledger.  The identity is exact in the
declared `K2c/B1c/Hc` chart.  A further coefficient-by-coefficient lift to the
original `C2/C3` coordinates is
`OPEN[C2/C3-INVERSE-LEDGER-NOT-SERIALIZED]`, as the charged artifact records no
inverse map.

## 3. Kill B: `(99,66), delta=5/2`

### 3.1 Backward trace and the stage-8 non-dependency

Here the physical place is declared as

```text
t=s^2,   w=u*s^4+v*s^6+pi*s^7,
[s^21]K3=pi*(pi^2-c).
```

Local power 16 therefore corresponds to normalized `t`-power 8.  After the
outer-`D1` quotient, but before any cumulative joint substitution, the
terminal pole row contains 35 `B1` variables, all at levels 0 through 3.
Replaying the ledger gives exactly the earlier Jacobian pivots

```text
stage 1 / 2 / 3 / 4: 9 / 9 / 9 / 8,
```

so the post-major, post-order dependency DAG is **one pole row plus 35
Jacobian rows = 36 rows**.  In particular none of the seven chronological
stage-8 pivots

```text
B1c_7_19,...,B1c_7_25,   coefficients 675,576,477,378,279,180,81
```

is an ancestor.  Calling the kill “after seven pivots” is chronologically
correct but provenance-inexact.

The exact boundary counts are:

| boundary | incidence | outer `D1` | pole | Jacobian | total |
|---|---:|---:|---:|---:|---:|
| post-major/post-order joint ancestry | 0 | 0 | 1 | 35 | 36 |
| reduced `D1` pivot DAG | 0 | 2 | 1 | 35 | 38 |
| original `D1` row support | 0 | 7 | 1 | 35 | 43 |
| support-minimal post-`D2` certificate | 0 | 0 | 1 | 6 | 7 |
| `K2^2` constant-component `h3` dependency audit (not a lifted certificate) | 11 | 0 | 1 | 6 | 18 |

These are nested presentations, not quantities to add.

The outer prerequisite audit replays all eight weight-93 `B1-D1` rows and the
seven-row support lift displayed in §1.2.  All eight Schur-dual coefficients
are ultimately zero.  None of the seven `h2-D1` pivot variables occurs in the
core.  Before the common-`h3` map the **unpruned terminal pole row** directly
contains 17 `Hc` variables; their recursive closure uses 17 of the 20
incidence pivots:

```text
h3_s2_pi^0, h3_s4_pi^0, h3_s6_pi^0, h3_s8_pi^0, h3_s10_pi^0,
h3_s12_pi^0, h3_s14_pi^0,
h3_s9_pi^1, h3_s11_pi^1, h3_s13_pi^1, h3_s15_pi^1, h3_s17_pi^1,
h3_s19_pi^1, h3_lead_pi^1,
h3_s16_pi^2, h3_s18_pi^2, h3_s20_pi^2.
```

`Hc_11_0` is absent, agreeing with the charged no-Xu-ODE control: removing
that convention changes dimension by one but leaves residue 64 unchanged
(`g9966-independent-engine-opus5-20260903.md:363-366`).

Separately, the pre-`h3` `K2^2` summand of the terminal has 230 monomials and
ten direct `Hc` variables.  One pivot RHS adds an eleventh; its exact 11-row
incidence closure is

```text
h3_s2_pi^0, h3_s4_pi^0, h3_s6_pi^0, h3_s10_pi^0,
h3_s9_pi^1, h3_s11_pi^1, h3_s13_pi^1, h3_s17_pi^1,
h3_s16_pi^2, h3_s18_pi^2, h3_s20_pi^2,
```

and reduces that summand to 64.  Thus 11 audits that summand and 17 audits the
unpruned terminal; neither is a serialized pre-major certificate row count.

The counts above deliberately remain boundary-stratified.  The charged
branch builder hard-codes the post-`D2` support projector and common-`h3` map
but does not serialize their inverse row multipliers.  Therefore a literal
single pre-`D2`, pre-major sum with explicit incidence and projector
multipliers is

```text
OPEN[PRE-D2/PRE-MAJOR-MULTIPLIERS-NOT-SERIALIZED].
```

What is exact is the post-`D2` certificate below, the 36-row joint DAG, the
eight-row `D1` replay, and the 17-row incidence dependency audit.  No count is
manufactured by adding these overlapping interfaces.

The full outer `D2` projector is also exactly counted, but is not falsely
called the minimal slice: it has 5,598 zero-coordinate rows,
`A2/A3/B1/B2 = 1386/2442/384/1386`.  Because its multiplier map was not
serialized, the number retained in a literal pre-`D2` certificate is `OPEN`,
not 5,598 and not zero.

### 3.2 The 43-by-43 Schur certificate

Form the square `B1` block `A` from the eight outer-`D1` rows followed by the
35 Jacobian rows, and let `ell` be the `B1` coefficient functional of the
terminal pole row `P`.  Exact inversion over `Q[u,v]` (the determinant of `A`
is a nonzero rational unit) gives the unique dual `alpha=A^{-T}ell` and

```text
P - sum_i alpha_i*row_i = 64.
```

All eight `D1` entries and 29 of the 35 Jacobian entries of `alpha` vanish.
Writing `K521=K2c_5_21`, `K620=K2c_6_20`, `K621=K2c_6_21`, and
`K719,K720,K721` similarly, the six nonzero entries are

```text
a1=(17371*K521*u+145*K719-145*K720+145*K721-6525*c
    +1433412*u^2*v-190680*v)/125280,
a2=2*(29*K521*u+2088*u^2*v-240*v)/1305,
a3=-(29*K620-29*K621+2436*u^3+27864*u+6264*v^2)/24273,
a4=-32*u/87,
a5=(K521+72*u*v)/810,
a6=-8/783.
```

They multiply, in order,

```text
J(162,35), J(162,36), J(161,35), J(161,36), J(160,35), J(159,35).
```

Hence the support-minimal identity in this quotient is

```text
1 = P/64 - (a1*J(162,35)+a2*J(162,36)+a3*J(161,35)
             +a4*J(161,36)+a5*J(160,35)+a6*J(159,35))/64.
```

Equivalently, the replay prints the seven already-divided coefficients; the
last two are `-(K521+72uv)/51840` and `1/6264`.  Because `A` is square and
invertible, the cancellation functional is unique in this 43-row linear
core, so its seven nonzero support rows cannot be further pruned there.

No live `A2`, `A3`, or `B2` coefficient and no bridge row occurs.  The
localization is explicit but unused:

```text
1 = displayed identity + 0*(Zc*c-1).
```

Perturbing the consumed row `J(159,35)` by `+B1c_3_22` changes the frozen
certificate to `1+B1c_3_22/6264`; the control therefore fails exactly as it
should.

Replay:

```bash
timeout 1800 python3 box/obscore-20260903/delta52_certificate.py
```

The script checks the sealed independent-engine files and the charged stage-8
manifest before doing algebra.

## 4. Kill C: `D=108, delta=3`

### 4.1 Standalone common-`h3` expansion

This replay imports no campaign engine or ledger.  Starting with the
seven-coordinate post-major chart for `w^2(w-1)^7`, it converts `z=w-1` to
`w`, substitutes

```text
y=jet1*t+jet2*t^2+pi*t^3,
w=t*y=jet1*t^2+jet2*t^3+pi*t^4,
K3=-t^8*(pi^2-c)+O(t^9),
```

and uses the exact contribution rule

```text
a[r,j] * multinomial(j;a,b,k) * jet1^a*jet2^b*pi^k
at t-power r+2a+3b+4k,   a+b+k=j.
```

The minus sign is forced by `w^2(w-1)^7=-w^2+O(w^3)`; the literal-plus
control would create a spurious `-2`.  Extraction through power 8 produces
the 13 labels

```text
(1,0),(2,0),(3,0),(4,0),(5,0),(5,1),(6,0),(6,1),
(7,0),(7,1),(8,0),(8,1),(8,2),
```

where `(n,k)` abbreviates `minor_n{n}_pi{k}`.  Twelve rows are nonzero and
`minor_n8_pi2=0` is checked rather than discarded silently.

### 4.2 Seven pivots and residues

Exact `Q*` elimination gives

| pivot row | variable | coefficient | resolved value |
|---|---|---:|---|
| `(1,0)` | `Hc_1_7` | -1 | 0 |
| `(2,0)` | `Hc_2_6` | 1 | 0 |
| `(3,0)` | `Hc_3_6` | 1 | 0 |
| `(4,0)` | `Hc_4_5` | -1 | `jet1^2` |
| `(5,0)` | `Hc_5_4` | 1 | 0 |
| `(5,1)` | `Hc_1_8` | -1 | 0 |
| `(6,1)` | `Hc_2_7` | 1 | `2*jet1` |

The five normal forms are

```text
r60=-jet2^2,
r70=2*jet1^2*jet2,
r71=-2*jet2,
r80=-c-jet1^4+9*jet1*jet2^2,
r81=2*jet1^2.
```

Thus the three requested residues `r71,r80,r81` are reproduced from the
common expansion, not copied.  This agrees with the charged construction
(`g108-joint-band-sol56-20260903.md:228-279`).

### 4.3 Minimal localized certificate

With `L=Zc*c-1`, the readable certificate is

```text
1 = -(9/2)*jet1*jet2*Zc*r71 - Zc*r80
    -(1/2)*jet1^2*Zc*r81 - L.
```

Strict support pruning removes `r71`.  Put

```text
A = -9*jet1*jet2^2*Zc^2-Zc,
B = -(9/2)*jet1^3*jet2^2*Zc^2
    +(81/2)*jet2^4*Zc^2-(1/2)*jet1^2*Zc,
C = -9*jet1*jet2^2*Zc-1.
```

Then the smaller exact identity is

```text
1 = A*r80 + B*r81 + C*L.
```

Dropping any one of `r80,r81,L` leaves an explicit common zero, so this
three-generator reduced support is inclusion-minimal.  Back-substitution
through the fixed seven-pivot ledger uses nine nonzero raw incidence rows;
with `L`, the certificate has family counts `(9,0,0,0,1)` and size **10**.
Every one of the seven pivot rows lies in its dependency closure.  The older
readable certificate lifts to ten incidence rows plus `L`.

Perturbing `minor_n8_pi0` by deleting its `-c` term breaks the identity.
Moreover all `Hc`, `jet1`, and `jet2` zero with `c=Zc=1` is a common zero of
the perturbed support and wrapper.  This is both an identity-failure and an
ideal-level negative control.

The literal lift is exact in the declared seven-coordinate post-major chart.
The charged aggregate does not serialize an inverse from all 45 raw `h3`
order rows to that chart, so a certificate in that earlier coordinate module
is `OPEN[PRE-MAJOR-ROW-LIFT]`.  This limitation does not alter the exact
post-major necessary slice.  The conflicting charged `D=108` outer ranks
`6449` and `7710` are also quarantined: no outer, pole, or Jacobian row is
used by this incidence-page unit (`g108-delta3-kill-gate-gpt55-20260903.md:
218-256`).

Replay:

```bash
timeout 1800 python3 box/obscore-20260903/d108_certificate.py
```

## 5. One filtered obstruction map

### 5.1 Block construction

Let `R` be the branch-parameter polynomial ring and add a homogenizing
coordinate `e=1`.  At any filtration page, order already-pivotable
coefficients as `x` and the survivors plus `e` as `y`.  The relevant part of
the obstruction map has matrix

```text
             x    y
pivot rows   A    B
test rows    C    D
```

with `A` a triangular or square rational-unit pivot block.  Row elimination
gives

```text
S = D-C*A^(-1)*B,
det([[A,B],[C,D]]) = det(A)*det(S).
```

For a scalar test functional this says that the fraction-free bordered minor
is `det(A)` times the terminal Schur scalar.  The coefficients of
`-C*A^(-1)` are exactly the backward-certificate multipliers.  For a one-column
residual presentation, its entries generate the residual determinantal
(equivalently, appropriate Fitting) ideal; adding a localization row and a
Bezout functional can make that ideal the unit ideal.

The three specializations are therefore:

| case | pivot block / page | Schur object |
|---|---|---|
| `delta=2` | fixed-face plus its reached pole/Jacobian pivots | scalar `6264`; eight-row lifted Bezout identity |
| `delta=5/2` | 43-square `B1` block (8 `D1`, 35 Jacobian) | scalar `64`; unique dual has only six nonzero Jacobian entries |
| `D=108` | seven rational common-`h3` incidence pivots, pivot product `-1` | five-residue vector; `(r80,r81,L)` has a unit Bezout combination |

In fraction-free notation the first two cores are the bordered minors

```text
m_delta2  = det(A_delta2)*6264,
m_delta52 = det([[A,r0],[ell^T,p0]]) = det(A)*64.
```

For `D=108`, elimination instead gives the residual column
`S=(r60,r70,r71,r80,r81)^T`; adjoining `L` and applying the explicit Bezout
row `(0,0,0,A,B,C)` from §4.3 sends `(S,L)` to 1.  That is its residual
determinantal/Fitting formulation.

This is one common **filtered block-elimination schema**, not one literal
same-sized matrix.  The page at which its cokernel acquires a unit changes with the
skeleton, exactly the filtration-page alternative anticipated in
`ideation-20260904T0000Z-sol56.md:633-654`.

### 5.2 Symbolic first-point Jacobian block

Let

```text
H(w)=w^(u3)*(w-1)^(v3),
A0=H^(d2/d3),
N=3*d2,
u3+v3=d3, gcd(u3,v3)=1, d3 divides d2, 0<=n<=d2.
```

Below the outer onset, once lower `B1` levels vanish, the normalized Jacobian
band is `A0^3 L_n(B_{n-1})`, where the prime now explicitly means `d/dw` and

```text
L_n(B)=N*A0*B'-(N-3n)*A0'*B.
```

In ascending monomial bases, if `A0=sum p_a w^a`, its exact matrix entry is

```text
(L_n)_(ell,k) = (N*k-(N-3n)*(ell-k+1))*p_(ell-k+1).
```

Solving the first-order equation gives

```text
ker L_n = Q * H^(d2/d3-n/d3)   if d3 divides n,
ker L_n = 0                     otherwise,
```

under the displayed divisibility, coprimality, and degree-range hypotheses.
The exact matrix driver checks:

| skeleton / level | shape | rank | kernel |
|---|---:|---:|---|
| `(99,66)`, `n=4` | `66 x 34` | 34 | 0 |
| `(99,66)`, `n=11` | `66 x 34` | 33 | `Q*w^6(w-1)^16` |
| `D=108`, `n=9` | `72 x 37` | 36 | `Q*w^6(w-1)^21` |

This validates the first-point `L_n` mechanism used by the cores; it does not
promote the broader conjectural `MINOR-5.6` statement.

Replay:

```bash
timeout 1800 python3 box/obscore-20260903/filtered_obstruction.py
```

### 5.3 Exact symbolic extent

The requested symbols determine substantial, but not complete, matrix data.

| component | replacement extent |
|---|---|
| order support | Symbolic once the order weights and thresholds are supplied: a `D2` row is a coordinate projector selected by a weighted inequality; an at-level `D1` block has binomial entries `binom(q,k)`. |
| common incidence | Symbolic after the physical branch exponents are supplied: `a[r,j]` contributes the multinomial term shown in §4.1.  The weights determine which terms can occur. |
| first-point Jacobian | Fully symbolic in `d2,d3,u3,v3,n` under the displayed divisibility, coprimality, and degree-range hypotheses; the `L_n` entry and kernel formula are exact. |
| pole functional | Its support is weight-symbolic, but its affine right-hand side also needs the branch series, face polynomial, gauge, and jet coefficients. |
| final Schur scalar | **Not** determined by `(d_s,u_s,V_s,delta,weights)` alone.  It also depends on the branch partition, face normalization and the jet/low-tower coefficients. |

Consequently `6264`, `64`, and the `D=108` polynomials in `c,jet1,jet2`
are branch-specific evaluations of a symbolic obstruction-map template.  They
cannot honestly be replaced by a single expression in only the requested
skeleton symbols.  The exact promotion is the block formula, the support
rule, and the `L_n` kernel theorem; the universal final minor remains
`OPEN[UNIVERSAL-TWO-PLACE-OBSTRUCTION]`.

## 6. FALLACY-v2 audit

| guard | audit result |
|---|---|
| flag / place / series | The major parameter, physical minor place, and cover coordinate are declared separately in §§2–4.  `t=s^2` is a reparameterization, not a flag identification. |
| per-ray / exit-set charge | No exit-price assertion is made.  Therefore no `charge_basis` line is due. |
| carrier / attainment | No representative, actual exit, floor, or attainment statement is used.  These are necessary-chart emptiness certificates only. |
| pole / interior | The `(99,66)` pole rows express Laurent polynomiality only after the branch series is declared and within the imported vertex/source hypotheses.  The `D=108` certificate reaches no pole row. |
| floor / attainment | Order inequalities select necessary coordinates; no lower bound is promoted to equality. |
| `sat()` wrapping | No `sat()` call occurs.  `c != 0` is represented by the explicit Rabinowitsch row `Zc*c-1`.  Charged `(99,66)` runs supply raw/empty/point controls; slice scripts assert exact identities and perturbation controls, and `D=108` also supplies a perturbed common zero. |
| raw remainder degree | Zero rows are checked (`minor_n8_pi2=0`), nonzero terminal normal forms are constants in the declared quotient, and hard-coded quotient boundaries are disclosed as `OPEN` rather than lifted by analogy. |
| variable / ring map | Every replay uses `Q`, declares generator names, and tests identities by expansion.  The `delta2/delta52` drivers check charged hashes/manifests; the `D=108` and filtered-map drivers are standalone.  The independent engine's `vv` is explicitly mapped to displayed `v`. |
| prime label / derivative | The only primes in this report are explicitly `d/dw` in `L_n`; `pi` is a branch-coordinate label, not differentiation. |
| merge-free / `M`-descent | No statement 8.5 descent or merge claim is used. |
| target / arrival index | Fixed terminal labels are kept separate from stage and incoming indices.  The stage-8 Jacobian rows are expressly excluded from the `delta=5/2` ancestry. |

The `D=108` outer-rank disagreement is not repaired by choosing the convenient
number; it is irrelevant to the incidence-page ideal and remains quarantined.
All identified missing pre-quotient or inverse maps are likewise typed open.
This is the safe replacement required by FALLACY-v2.

## 7. Replay inventory

All jobs are foreground and bounded by `timeout 1800`.

| artifact | role |
|---|---|
| `box/obscore-20260903/delta2_certificate.py` | receipt-authenticated raw selected-row lift, DAG, exact identity, perturbation control |
| `box/obscore-20260903/delta52_certificate.py` | manifest-authenticated 43-square Schur calculation, stage-8 ancestry audit, exact seven-row identity |
| `box/obscore-20260903/d108_certificate.py` | standalone 13-label expansion, seven pivots, residues, minimal localized raw-row certificate |
| `box/obscore-20260903/filtered_obstruction.py` | exact `L_n` matrices, ranks/kernels, and Schur determinant identity |

The final replay/compile pass returned exit 0 for every driver.  The observed
wall times were approximately 90 s, 20 s, 1.2 s, and 3.5 s in table order
(machine load affects the first two).  Final SHA-256 values are

```text
916f430726b60b2a87dc89f474ce8412984f545e8cbe703380a14755a31deb77  delta2_certificate.py
ff457563bad9edd8667999408c9e7e5e610abd6d380cbec7f8dfd965d03788c7  delta52_certificate.py
e271a767abc4d4052ec510a68b06ddc1ca2653c11bdb55d4fa91372b6e9ac2ed  d108_certificate.py
f386e644efee0785c6f8e1a07ba5a56b39d1b908431f204a7a02c845f6a6311e  filtered_obstruction.py
```

## 8. Verdict

The numerical skeleton has compressed to three small, provenance-bearing
cores.  The `(99,66),delta=2` certificate has eight retained raw rows; the
`delta=5/2` certificate has seven rows in the exact post-`D2` common-`h3`
quotient; and the `D=108` localized certificate has ten retained rows after
fixed-ledger back-substitution.  All stop by normalized power 8, none uses a
live `A2/A3/B2` coefficient, and none touches a `T2/T3` bridge.

The common theorem-sized content is the filtered Schur/Fitting construction
and its symbolic first-point operator.  The first obstruction page varies,
and the final entries require branch and face data not present in
`(d_s,u_s,V_s,delta,weights)`.  Verdict:

```text
CERTIFICATE-SLICE: EXACT at the declared boundaries above.
PATTERN: FILTRATION-PAGE-RULE.
UNIVERSAL NUMERICAL MINOR: NO from the requested symbols alone.
OPEN: identified pre-D2, pre-major, and C2/C3 inverse lifts.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `28292`.
- Body SHA-256:
  `4ccd91a79a1496e5b71c03f71ab9da95ed3aef4c5073e22a46ba12fdb65a84bf`.
- Frozen basis: `39ca589b03ed04a7248197958cd21742eafdc67e`.
