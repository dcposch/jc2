# Hostile review — `K00-V20R2-RAM-E2-M1-B11111` grade-five prefix certificate

Reviewer: Opus 5 (independent hostile)
Date: 2026-08-29
Review basis: `55067d08c111f473945700ded838a7798b8b3fb2`
Verdict: **PASS_WITH_MATERIAL_REPAIRS**

Everything below was reconstructed from the raw 569-monomial tail JSON with a
review-local sparse rational polynomial implementation. The producer engine
`xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py` was **not** imported for
any mathematical conclusion; it was executed once, separately, only to check
that the producer replay reproduces its own advertised banners. Every verdict
in sections 2--6 rests on the review-local reconstruction.

## 0. Headline

The load-bearing mathematics survives and, in one place, is stronger than
claimed. The grade-two/three rank kill, the grade-four and grade-five closed
forms, the freeness of `d[4]`, the finite prefix witness, and the restricted
grade calendar `G6/G7`, `G14/G15`, `G22`, `G29/G33/G37/G38` are all CONFIRMED
by independent reconstruction.

Three statements are wrong as written and must be repaired before promotion:

```text
R1  "Its four nonzero two-by-two minors"            -> there are 36.
R2  "K10/G7 = 5/32768"                              -> the true value is 5/65536.
R3  "cheapest next solve ... K10 G7 equation"       -> G6 strictly dominates G7.
```

`R2` is a genuine arithmetic defect in the pinned replay, not a typo in prose:
the replay computes the grade-seven K10 coefficient as `DM4(ell)[u]` and drops
the cubic term `A10^[3](ell)`.

Four further gaps are recorded: a stale frozen basis, an undefined generator
`F10` in the transported grade-three theorem, an unbacked section 2, and a
mutation suite of which two of six controls are vacuous and one is described
by a mutation that is provably invisible where it is claimed to bite.

## 1. Custody

Recomputed on the review basis:

```text
a6fd11f1c6d5b32cc2e497722245cbe7381356ffdbba02c6db050ad5fe67ced0  certificate (full)     MATCH
0b6bb668ac1c3056338dbdf167d435c90bfde86765e9018834feeedc627de5df  certificate body       MATCH
10078                                                             certificate body bytes MATCH
b4fd505d0345b21a2978f06ff63cb0c9fcacd9d7226d7accaa0b2ab489b210ea  replay                 MATCH
98fb38535405f1cc853dd4d430e26876a84f6f97c538f862f18a0446c0c97ecf  parent packet (full)   MATCH
c15bda710b725c04c6ccf289fcf570c3414fe8825669ae68238c1d26fe96d51c  parent packet body     MATCH
11063                                                             parent body bytes      MATCH
```

All six digests in the replay `EXPECTED` table match the worktree:

```text
d72f774c...  tails.json                                   MATCH
2ac7653c...  compile_contracted_source_v20r2.py           MATCH
2c918d5b...  k00-r2-full-rank-fan-replay-sol56 (engine)   MATCH
d453b956...  k00-rank5-rankle1-coordinator-integration    MATCH
fbe5b580...  k00-grade4-rank0-plane-coordinator-integr.   MATCH
98fb3853...  k00-v20r2-valuative-comparison-v1            MATCH
```

**GAP C1 (frozen basis).** The certificate declares
`Frozen campaign basis: 31777ce90994a106aade85064c0d868e32863f94`. Its own
primary source dependency, `xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md`,
does not exist in the tree at `31777ce9`; it first appears at `55067d08`. A
certificate cannot be frozen at a basis that does not contain the packet it
restricts. The other five pinned inputs are byte-identical at `31777ce9`, at
`55067d08`, and in the worktree, so there is **no content drift** — this is a
declaration defect, not a source defect. Repair: restate the basis as
`55067d08`.

**Nit C2.** The certificate's body-end marker string occurs twice, once as the
real standalone marker at line 295 and once quoted inside the seal's own body
definition at line 299; the "unique standalone" wording disambiguates. The
recomputed body bytes and digest agree, so this is cosmetic.

## 2. Source typing, normalization, census — CONFIRMED

Reconstructed independently from `tails.json` with the compiler's variable
order `C0..C6,k10,k6,k2` and weights `(8,7,6,5,4,3,2 | 2,6,10)`:

```text
term census                                      569   CONFIRMED
weight law  sum(m_i w_i) = 12+l  for every term         CONFIRMED
load linearity  sum(m[7:]) <= 1                        CONFIRMED
coordinate images = certificate (2.2)                  CONFIRMED (byte-level)
ord_d R    = (2,2,2,2,2,3,2)                           CONFIRMED
ord_d A10  = (2,2,2,2,2,2,2)                           CONFIRMED
ord_d A6   = (1,1,1,2,1,2,1)                           CONFIRMED
ord_d A2   = (1,1,1,1,1,1,1)                           CONFIRMED
```

`e=2`, `m=1`, `B11111` typing. With `Lambda=t^2` the pinned compiler's
`Lambda`-shifts `(k10,k6,k2)=(2,6,10)` give `t^4,t^12,t^20`, and the target
weights `(mu2,mu4,mu6,Jdet)=(14,16,18,19)` with `target_sign=-1` and the
`Jdet/4` factor give `t^28,t^32,t^36,t^38`. All CONFIRMED against the frozen
compiler source. `m=1` means `x=d[1] != 0`, which is exactly the open
`D(d0[1]) u ... u D(d5[1])`, i.e. `(s,t)!=(0,0)` after restriction to the
plane. `B11111` is the order vector of `(k6,k2,mu2,mu4,mu6)` in the parent's
displayed order — CONFIRMED consistent.

Kummer/unit normalization. `Lambda=u(t)t^e -> t^e` and `C6=1` by the
weight-two action (`C6 -> a^2 C6`) both adjoin only roots of units; over a
complete DVR with algebraically closed residue field these exist by Hensel
without further ramification, and `e` and every displayed order and unit open
are preserved. CONFIRMED as sound. This is the parent's normalization
restated; the certificate adds nothing here and claims nothing more.

Boundary zeros and column census, re-derived:

```text
331 = 6*38 + 35+27+19+11+7+3+1                       CONFIRMED
326 = 331 - 5   (k6[0],k2[0],mu2[0],mu4[0],mu6[0])   CONFIRMED
316 = 222+33+25+17+19                                CONFIRMED
 10 inert = d_i[38] (6) + k10[33,34] + k6[26] + k2[18]  CONFIRMED
273 = 7*39                                           CONFIRMED
```

The occurrence bounds behind `316` were re-derived from the stencil, not
copied: `d_i[n]` needs `n+1<=38`; `k10[j]` needs `j+6<=38`; `k6[j]` needs
`j+13<=38`; `k2[j]` needs `j+21<=38`; `mu2/mu4/mu6/Jdet` need
`28+j,32+j,36+j,38<=38`.

## 3. Grade two and three — CONFIRMED, with a stronger independent proof

### 3.1 Leading cone — CONFIRMED

Only unloaded rows can occur at grades 2 and 3 (first load grade is 6), so the
grade-two system is `Q_r(x)=0` and the grade-three system is
`DQ_r(x)[u]+c3_r(x)=0`, `u=d[2]` free. CONFIRMED.

`Q_6` is identically zero and `span{Q_1,...,Q_7}` has dimension **4**, not 7.
The certificate's phrase "the seven leading quadrics" is loose but its
statement is nonetheless true. In the adapted linear coordinates

```text
y0=A(x)=16x1-4x3+x5,  y1=B(x)=x0-4x2+2x4,
x=(y1+2b+2al, a, b, 8a+be, b-al, y0+16a+4be),
```

the quadrics read

```text
Q1 = -3/2048 y0y1 - 3/1024 be*y1 + 3/1024 al*y0
Q2 = 15/2048 y0^2 + 3/256 be*y0 + 3/16384 al*y1
Q3 =  3/8192 (y0y1 + be*y1 - al*y0)
Q4 =  3/524288 (y1^2 - 64 y0^2)
Q5 =  3/262144 (-y0y1 + 2be*y1 - 2al*y0)
Q6 =  0
Q7 =  3/1048576 (be*y1 - al*y0)
```

Every `Q_r` lies in `(A,B)_2`, and exact graded linear algebra gives
`y0^3, y1^3 in (Q_1,...,Q_7)`. Hence

```text
sqrt(Q_1,...,Q_7) = (A,B),      V(Q) = V(A,B) exactly.   CONFIRMED
```

The ideal has no degree-one part, so `y0,y1` are not in it: the scheme is
**nonreduced**. CONFIRMED. Parameterization (2.1) is a linear bijection onto
`{A=B=0}` (inverse `a=x1, b=x2, be=x3-8x1, al=x2-x4`). CONFIRMED. Setting
`al=be=0` and `(a,b)=(t/8,s)` gives exactly `ell(s,t)=(2s,t/8,s,t,s,2t)`.
CONFIRMED.

### 3.2 Rank fan — CONFIRMED except the minor count

On the cone every row of `DQ` is `c_r0*A + c_r1*B` with

```text
(c_r0, c_r1) = ( 3al/1024,      -3be/1024   )   r=1
               ( 3be/256,        3al/16384  )   r=2
               (-3al/8192,       3be/8192   )   r=3
               ( 0, 0 )                          r=4
               (-3al/131072,     3be/131072 )   r=5
               ( 0, 0 )                          r=6
               (-3al/1048576,    3be/1048576)   r=7
```

so rows 4 and 6 vanish identically, rows 1,3,5,7 are mutually proportional,
and only row 2 is independent. Consequences:

```text
no rank >= 3 on the leading base                               CONFIRMED
rank 2  <=>  Delta = al^2 + 64 be^2 != 0                       CONFIRMED
rank 1  <=>  Delta = 0 and (al,be) != (0,0)                    CONFIRMED
rank 0  <=>  al = be = 0                                       CONFIRMED
```

**REFUTED (R1).** "Its four nonzero two-by-two minors are nonzero rational
multiples of `Delta`." The `7x6` Jacobian in the `x` coordinates has **36**
nonzero `2x2` minors on the cone, falling into **19** distinct rational
multiples of `Delta`. Zero minors fail to be a multiple of `Delta`, so the
mathematical substance is intact; only the count is wrong. "Four" is the
number of nonzero **row pairs**, namely `{(1,2),(2,3),(2,5),(2,7)}`; each
contributes `9` nonzero column pairs, `4*9=36`.

Repair: *"Every nonzero `2x2` minor of `DQ` on the cone is a nonzero rational
multiple of `Delta=al^2+64be^2`; exactly four row pairs `(1,2),(2,3),(2,5),(2,7)`
contribute, giving 36 nonzero minors in 19 rational classes. Hence
`rank DQ >= 2` iff `Delta != 0`."*

### 3.3 Grade-three exclusion — CONFIRMED, and provable without transport

The certificate consumes the promoted grade-three incidence theorem. That
transport has a gap (section 3.4). It is not needed: the kill follows directly
and cheaply from the frozen rows alone.

Writing `P=A(u)`, `S=B(u)` (two independent free scalars, since `A,B` are
independent linear forms in `u`), the grade-three system on the cone is
`c_r0 P + c_r1 S + c3_r = 0`. Rows 4 and 6 have `c_r0=c_r1=0`, and rows
3,5,7 are `-1/8, -1/128, -1/1024` times row 1. This yields five `u`-free
homogeneous cubic necessary conditions in `Q[a,b,al,be]`, valid at **every**
rank:

```text
c3_3 + (1/8)   c3_1 = 0
c3_5 + (1/128) c3_1 = 0
c3_7 + (1/1024)c3_1 = 0
c3_4 = 0
c3_6 = 0
```

Exact graded linear algebra on the ideal `I` they generate gives

```text
dim I_3 = 4/20,   dim I_4 = 14/35,   dim I_5 = 32/56
al^5 in I,   be^5 in I.
```

Therefore every grade-three-compatible cone point has `al=be=0`, i.e.
`DQ`-rank zero. Conversely on `al=be=0` both `DQ(ell)=0` and `c3_r(ell)=0`
for all seven rows, so grades two and three vanish identically with `d[2]`
entirely free. Hence, over any field of characteristic zero — in particular
over `Q`, over `Q(i)` (both rank-one sign branches), and over any algebraic
closure —

```text
V(G2,G3) = Pi x A^6_{d[2]},     Pi = { ell(s,t) },
```

and imposing `m=1` removes the origin, giving `(s,t)!=(0,0)`. The
rank-two stratum, both rank-one sign branches, and the origin are all
**empty at grade three**. CONFIRMED.

This is strictly stronger than the transported theorem, because it uses only
the six nonzero unloaded grade-two quadrics.

### 3.4 The transport route — GAP

**GAP C3.** The promoted theorem in
`xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md` is stated
for `B = B2 + (F10)`, where `B2` is the six nonzero literal grade-two rows.
`F10` occurs exactly once in that document (line 39) and is **never defined**
there or anywhere else in the K00 series. Two readings:

- if `F10` is redundant given `B2`, then `B=B2` and the transport is fine;
- if `F10` is independent — the natural reading of a "load-ten" form — then
  `V(B) ( V(B2)` strictly, and the theorem cannot be applied "verbatim" to a
  cell whose entire grade-two content is `B2`. The theorem would then be
  proving emptiness under a hypothesis this cell does not impose.

The second reading is live: I checked that the K10 leading quadratic `M4_l` is
**not** in `span{Q_1,...,Q_7}` for rows 1,2,3,5,7, and adjoining the `M4_l`
raises the span from dimension 4 to 6.

Repair: replace the transport in certificate section 2 by the direct argument
of section 3.3 above, which is self-contained, cheaper, and free of `F10`.
The certificate's conclusion is unaffected.

**GAP C4 (section 2 has no replay backing).** The replay hash-pins the two
integration documents but never reads them, and computes no rank, no minor and
no `Delta` anywhere. `LEADING_NONZERO_MATRIX_RANKS=EMPTY_AT_G3` is printed
unconditionally. `form_a`/`form_b` are constructed only to be serialized into
the residual; the claim that they are the reduced support of the grade-four
scheme is never checked by the replay. The whole of certificate section 2 is
therefore prose plus an unparsed citation. It is true — I verified it — but it
carried no evidence in the artifact as shipped.

## 4. Grade four and grade five — CONFIRMED

Reconstructed by substituting `d_i(tau) = ell_i tau + u_i tau^2 + v_i tau^3 +
p_i tau^4` with `(u,v,p)=(d[2],d[3],d[4])` **fully symbolic** (18 free
variables) and `(s,t)` symbolic, then extracting coefficients:

```text
G0 = G1 = G2 = G3 = 0                    identically, all 7 rows   CONFIRMED
G4_r = Q_r(w),          w = d[2] - mu    all 7 rows                CONFIRMED
G5_r = DQ_r(w)[d[3]] + (1/2) D^2 c3_r(ell)[w,w]   all 7 rows       CONFIRMED
mu(s,t) = (s^2, st/8, 16t^2, 0, 0, 0)                              CONFIRMED
d[4] absent from G4 and from G5 in every row                       CONFIRMED
```

"All legal columns symbolic" is CONFIRMED in the strong sense: `k10[j]` cannot
occur before grade `j+6 >= 6`, and `k6,k2,mu,Jdet` cannot occur before grades
14, 22, 29, so `d[1..4]` really are the only legal columns at grade `<= 5`,
and all of `d[2],d[3],d[4]` were carried symbolically.

The grade-four scheme `(Q_1(w),...,Q_7(w))` is proper and nonreduced with
reduced support the linear four-plane `A(w)=B(w)=0` — this is section 3.1
verbatim with `w` in place of `x`. CONFIRMED.

**Nonclaim to record.** `mu` is not canonical. The grade-four identity forces
only `Dc3(ell)[.] = -DQ(mu)[.]` as linear forms, which determines `mu` modulo
the directions annihilated by the polarization of the seven quadrics. The
certificate presents `mu` as a definite object; the replay's `16t^2 -> 15t^2`
mutation shows the choice is not free *in that direction*, which is not the
same as uniqueness. Nothing downstream depends on this.

## 5. The prefix witness — CONFIRMED and correctly typed

Independent full-series evaluation with actual load series
(`k10=1`, `k6=tau`, `k2=tau`) at

```text
s=1, t=0  =>  ell=(2,0,1,0,1,0),   w=0 => d[2]=mu(1,0)=(1,0,0,0,0,0),
d[3]=0,   d[4]=0
```

gives, in all seven rows and every sector, zero at grades 0 through 5.
CONFIRMED. Transverse order is exactly one since `ell(1,0) != 0`. CONFIRMED.

Typing is correct. This is a finite jet in `K[t]/(t^39)` satisfying five
equations per row; it is not an arc, not a point of a closure, not a map, and
no attainment is inferred. The certificate's section 6 says so explicitly, and
the residual carries `"attainment": false`. CONFIRMED — no carrier/attainment
violation.

## 6. Restricted calendar — one REFUTED value, one overstatement

### 6.1 K10

```text
M4_r(ell) = 0   for all seven rows                    CONFIRMED
=> the generic G6 K10 arrival vanishes on Pi          CONFIRMED
K10 first possible at G7                              CONFIRMED
```

but the reasoning and the number are both defective.

The grade-seven K10 sector coefficient is

```text
k10[0] * ( DM4_r(ell)[u] + A10^[3]_r(ell) ),
```

because `A10` has a nonzero cubic part. The certificate argues only that
"at least one polarization `DM4_r(ell)[u]` is nonzero"; that alone does not
give a nonzero sum. (The conclusion does survive, by the separate observation
that `A10^[3](ell)` is `u`-free while `DM4(ell)[u]` is not, so they cannot
cancel identically.)

**REFUTED (R2).** The replay omits `A10^[3](ell)` entirely:

```python
m4_g7.append(directional(module, ring, m4[row_index], x, u))   # DM4 only
```

Row-by-row at the witness:

```text
row   DM4(ell)[u]     A10^[3](ell)      true G7 coefficient
 1        0                0                    0
 2     5/32768         -5/65536              5/65536
 3        0                0                    0
 4        0                0                    0
 5        0                0                    0
 6        0                0                    0
 7        0                0                    0
```

So `K10/G7 = 5/65536`, not `5/32768` — a factor-of-two error. Verified two
independent ways: direct polarization of the tail data, and a full
`tau`-expansion of `t^4 * k10(t) * A10(d(t))` to grade 22.

Note the contrast: the K6 branch of the same replay *does* include its
quadratic term (`L6(u) + A6^[2](ell)`), so this is an isolated omission in the
K10 branch, not a systematic convention.

### 6.2 K6

```text
L6_r(ell) = 0   for all seven rows                    CONFIRMED (literally)
K6 first possible at G15                              CONFIRMED
G15 coefficient = k6[1]*( L6_r(u) + A6^[2]_r(ell) )   CONFIRMED
K6/G15 row 2 = 3/2048                                 CONFIRMED
```

**GAP C5 (overstatement).** "generic G14 cancels in every row" and
"all-seven-row cancellation" are misleading. `L6_4` and `L6_6` are identically
zero **as polynomials**, because `ord_d A6 = (1,1,1,2,1,2,1)`: rows 4 and 6
have no generic grade-fourteen K6 term at all, so there is nothing there to
cancel. The parent packet's own table says exactly this (`K6` rows `4,6` first
grade 15). Honest statement: *five* rows (1,2,3,5,7) carry a generic G14
arrival and all five cancel on `Pi`; rows 4 and 6 start at G15 by stencil.
The conclusion "K6 first possible at G15" is unaffected. This is a
flag/place/series-style conflation of "absent" with "cancelled".

### 6.3 K2 and targets

```text
N2_r(ell) nonzero on rows 1,2,3,5,7 (zero on 4,6)     CONFIRMED
K2 first possible at G22                              CONFIRMED
K2/G22 row 2 = 1/32                                   CONFIRMED
targets  mu2 G29, mu4 G33, mu6 G37, Jdet G38          CONFIRMED
```

### 6.4 Unit/localizer divisions

The three reported numbers are the cofactors of `k10[0]`, `k6[1]`, `k2[1]`
with those leading units set to one. That is legal on the open (4.3), where
each is invertible, and the certificate states the normalization adjacent to
the numbers. CONFIRMED for K6 and K2; the same normalization applies to the
corrected K10 value `5/65536`.

Recorded observation: at this witness all three sector coefficients are
nonzero **only** in row 2, which is why the row-2 sector is the one reported.

## 7. Replay, dependencies, mutations, successor

### 7.1 Execution — CONFIRMED

```text
python3 -B  ...replay.py     exit 0
python3 -B -O ...replay.py   exit 0
stdout identical, sha256 = abbf34b8c5b0a5f0d8b71a2041830c77aeaba9c5a9d45f6391927bd2b3ed27e0
RESIDUAL_BYTES = 26852,  RESIDUAL_SHA256 = f471559d...   reproduced
```

The replay writes no files and makes no network calls. CONFIRMED.

The engine is imported via `exec_module` under the name `k00_exact_engine`, so
its `if __name__ == "__main__"` guard prevents any unpinned top-level work;
the engine's own custody check lives inside `main()` and does not fire, but the
outer replay digests `tails.json` itself, so custody is still covered. No
library-import pin gap here. CONFIRMED.

The residual contains every grade-four and grade-five polynomial, the two
reduced forms, the source pins, the opens, `later_literal_grades = [6,38]` and
`"attainment": false`. CONFIRMED. It does **not** contain the calendar witness
values, so `RESIDUAL_SHA256` provides no protection against `R2` — and,
usefully, repairing `R2` will not change the residual digest.

### 7.2 Mutations — GAP C6

Of the six advertised controls:

```text
CUSTODY            tautological  asserts sha256(bytes+"\n") != sha256(bytes)
CUBIC              weak          checks only that the added d0^3 is nonzero on Pi (=8s^3);
                                 the G3 identity is never re-run
MU                 sound         16t^2 -> 15t^2 genuinely re-derives G4 and compares
K10_SCALE          VACUOUS       see below
K6_RESTRICTION     sound         perturbs the plane, checks L6 no longer vanishes
ODD_COLUMN_DROP    VACUOUS       see below
```

`K10_SCALE` computes `kap * M4_i(generic_x)` and asserts it is nonzero. No
mutation is applied anywhere; the assertion is equivalent to "some `M4_i` is
nonzero", already implied by the ord-profile check thirty lines earlier.

`ODD_COLUMN_DROP` computes `Q_i(generic_x)` — the variable is literally named
`correct_generic_g2` — and asserts it is nonzero. Nothing is dropped.

Worse, the mutation `K10_SCALE` *describes* is provably invisible where it is
claimed to bite. Certificate section 5 item 4 says replacing `t^4` by `t^2`
"creates a generic G4 load". On the surviving plane it does not:

```text
scale t^4:  K10 sector at G4 = 0 (all rows),  at G5 = 0 (all rows)
scale t^2:  K10 sector at G4 = 0 (all rows),  at G5 = 5/65536 in row 2
```

because the grade-four contribution under the wrong scale is exactly
`k10[0]*M4(ell)`, which the certificate itself proves is zero. The certified
identity `G4_r = Q_r(w)` is **unchanged** by that mutation on `Pi`; it first
becomes visible at grade five. Repair: relabel the control as a grade-five
control and implement it as an actual re-derivation, as `MU` is implemented.

Certificate section 5's summary sentence "These are source and semantic
controls" is not supportable for four of the six.

### 7.3 Successor — GAP C7 (R3)

The successor *cell* `K00-V20R2-RAM-E2-M1-B11111-G5-RESIDUAL/v1` is correctly
typed and correctly names `G6,...,G38` as pinned by the compiler and tails.
The roadmap sentence is wrong: "the cheapest next solve is a rank/Fitting
split of (3.3) over the exact G4 scheme, followed by the corrected K10 G7
equation" skips grade six. Computed directly:

```text
G6 unloaded: nonzero in all seven rows
G6: d[5] absent in every row  (DQ(ell)=0 again kills the newest coefficient)
G6: d[4] present in rows 1,2,3,4,5,7
G6: K10 sector = k10[0]*M4(ell) = 0 in every row
G7: d[5] present;  d[6] absent;  K10 sector nonzero in rows 1,2,3,5,7
```

So grade six is a nonzero, purely unloaded equation in exactly the variables
already carried `(s,t,w,d[3],d[4])`, introducing **no** new free column,
whereas grade seven introduces `d[5]` and requires load modelling. Grade six
strictly dominates grade seven as the cheapest sound continuation.

Bonus finding, offered as a free extension: the mechanism that makes `d[4]`
free through grade five persists one step further —

```text
d[5] is free through G6,   d[6] is free through G7.
```

## 8. Claim-by-claim ledger

```text
#   claim                                                        verdict
--  -----------------------------------------------------------  --------------------
 1  certificate/replay/parent hashes and body bytes              CONFIRMED
 2  frozen basis 31777ce9                                        GAP (C1) -> 55067d08
 3  569 tails, weights, load-linearity, stencil (3.1)            CONFIRMED
 4  e=2/m=1/B11111 typing; scales t^4,t^12,t^20; targets         CONFIRMED
 5  Kummer/unit normalization and (2.2)                          CONFIRMED
 6  boundary zeros; 331/326/316/10; 273 equations                CONFIRMED
 7  G2,G3 contain only unloaded rows                             CONFIRMED
 8  reduced zero locus of the quadrics is A=B=0                  CONFIRMED
 9  parameterization (2.1)                                       CONFIRMED
10  "four nonzero 2x2 minors"                                    REFUTED (R1): 36
11  every nonzero 2x2 minor is a rational multiple of Delta      CONFIRMED
12  rank fan 0/1/2, none >= 3                                    CONFIRMED
13  rank two empty at G3                                         CONFIRMED (direct)
14  rank one empty at G3, both signs                             CONFIRMED (direct)
15  surviving leading base = ell(s,t), (s,t)!=(0,0)              CONFIRMED
16  transport of the promoted G3 theorem "verbatim"              GAP (C3): F10 undefined
17  section 2 backed by the replay                               GAP (C4): unbacked
18  G4_r = Q_r(w), all seven rows                                CONFIRMED
19  G5_r = DQ_r(w)[v] + 1/2 D^2c3_r(ell)[w,w], all seven rows    CONFIRMED
20  d[4] free through G5                                         CONFIRMED
21  all legal columns symbolic                                   CONFIRMED
22  G4 scheme proper, nonreduced, support A(w)=B(w)=0            CONFIRMED
23  mu presented as canonical                                    NONCLAIM (see 4)
24  witness solves G2..G5; transverse order one                  CONFIRMED
25  witness typed as a formal jet, not arc/map/attainment        CONFIRMED
26  M4_r(ell)=0 all rows; K10 G6 zero on Pi                      CONFIRMED
27  K10 first possible at G7                                     CONFIRMED (reasoning
                                                                 incomplete as written)
28  K10/G7 row 2 = 5/32768                                       REFUTED (R2): 5/65536
29  L6_r(ell)=0 all rows                                         CONFIRMED
30  "generic G14 cancels in every row"                           GAP (C5): rows 4,6 absent
31  K6 first possible at G15; row 2 = 3/2048                     CONFIRMED
32  K2 first possible at G22; row 2 = 1/32                       CONFIRMED
33  targets G29/G33/G37/G38                                      CONFIRMED
34  ordinary and -O replay reproduce residual + banners          CONFIRMED
35  replay writes no files, no network, no unpinned import       CONFIRMED
36  six mutation controls are "source and semantic"              GAP (C6): 2 vacuous,
                                                                 1 tautological, 1 weak
37  K10 scale mutation "creates a generic G4 load"               REFUTED: invisible at G4
38  G7 is the cheapest sound continuation                        REFUTED (R3): G6 is
```

## 9. Required repairs

```text
P1  Restate the frozen basis as 55067d08 (or reissue at a basis containing the
    parent packet).
P2  Replace "Its four nonzero two-by-two minors" by the row-pair formulation of
    section 3.3 above (36 minors, 19 classes, 4 row pairs).
P3  Fix the replay's grade-seven K10 coefficient to
        DM4_r(ell)[u] + A10^[3]_r(ell)
    i.e. add  eval_dpoly(dhom(loads["K10"][r], 3), x, ring)  to m4_g7[r];
    change the expected tuple to (5/65536, 3/2048, 1/32) and the
    CALENDAR_WITNESS_ROW2 banner accordingly.  RESIDUAL_SHA256 = f471559d...
    is unaffected, since the residual does not serialize these values.
P4  Replace the transport of the promoted grade-three theorem by the direct
    proof of section 3.3, or define F10 and show it vanishes on the ramified
    cell's grade-two locus.
P5  Restate the K6 cancellation as five rows cancelling and two rows absent by
    stencil.
P6  Reimplement K10_SCALE and ODD_COLUMN_DROP as actual mutations, and relabel
    the K10 scale control as a grade-five control.
P7  Correct the roadmap: the cheapest sound continuation is G6, not G7.
P8  Add the G7 justification that A10^[3](ell) is u-free while DM4(ell)[u] is
    not, so the two cannot cancel identically.
```

None of these repairs disturbs the theorem below.

## 10. Maximum safe theorem

Let `K` be a field of characteristic zero (algebraically closed where the
grade-three converse is used), and work in the finite jet ring `K[t]/(t^39)`
for the source cell `K00-V20R2-RAM-E2-M1-B11111/v1` as pinned by

```text
98fb3853...  xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md
d72f774c...  tails.json          2ac7653c...  compile_contracted_source_v20r2.py
```

with `Lambda=t^2`, `ord_t d = 1`, `k10` and `Jdet` units, `k6,k2,mu2,mu4,mu6`
of exact order one, and `C6=1` under the pinned weight/Kummer normalization.
Write `ell(s,t)=(2s,t/8,s,t,s,2t)` and `mu(s,t)=(s^2,st/8,16t^2,0,0,0)`.
Then, for the seven rows `Psi_1,...,Psi_7`:

1. `[t^0]Psi_r = [t^1]Psi_r = 0` identically.
2. The grade-two and grade-three coefficients involve no load and no target,
   and their common zero locus is exactly
   `{ d[1] = ell(s,t) : (s,t) != (0,0) } x A^6_{d[2]}`.
   Equivalently: on the leading cone `A=B=0`, the `DQ`-rank-two stratum and
   both `DQ`-rank-one sign branches are empty at grade three, and the
   rank-zero stratum survives with `d[2]` entirely free.
3. On that locus, with `w := d[2] - mu(s,t)`, for every `r`:
   `[t^4]Psi_r = Q_r(w)` and
   `[t^5]Psi_r = DQ_r(w)[d[3]] + (1/2) D^2 c3_r(ell)[w,w]`,
   and `d[4]` does not occur at grades four or five.
4. The scheme `(Q_1(w),...,Q_7(w))` is proper and nonreduced with reduced
   support the linear four-plane `A(w)=B(w)=0`.
5. The finite jet `s=1, t=0, w=0, d[3]=0, d[4]=0` satisfies grades zero
   through five in all seven rows and has transverse order exactly one.
6. Restricted to that locus the load calendar is: K10 sector identically zero
   at grade six and first possibly nonzero at grade seven; K6 sector
   identically zero at grade fourteen and first possibly nonzero at grade
   fifteen; K2 sector first possibly nonzero at grade twenty-two; targets at
   grades 29, 33, 37, 38. At the jet of (5), with the relevant leading unit
   set to one, the row-two sector coefficients are
   `K10/G7 = 5/65536`, `K6/G15 = 3/2048`, `K2/G22 = 1/32`.
7. Grade six is a nonzero purely unloaded equation in all seven rows in which
   `d[5]` does not occur; `d[6]` does not occur at grade seven.

Item 2 is proved here directly from the frozen rows and does not depend on the
promoted grade-three integration or on `F10`.

## 11. Exact nonclaims

This review establishes nothing about the following, and no downstream
consumer may infer them:

```text
- No attainment.  "First possible" is a floor on where a load column can enter;
  it is not a proof that any load coefficient is nonzero at any point of the
  cell, and REPRESENTATIVE is not FULL_ACTUAL_EXIT.
- No arc, no map.  The grade-five jet is a truncated formal object in
  K[t]/(t^39).  It is not a formal arc, a Taylor trajectory, a rational
  section, a polynomial map, a Keller pair, or a counterexample.
- No nonemptiness of the cell.  Grades 6 through 38 are untouched; nothing
  here shows the 273-equation system has a solution.
- No incidence verdict.  Nothing is proved about properness of H, about the
  saturation order (1.1), or about the C6=0 tip, k10=0, other load rays, or
  other square normals.
- No cross-valuation inference.  Nothing transfers to or from valuations one,
  two, three, four or five, to other (e,m,load-order) cells, to other
  ramifications, to Gate T, to order two, to maximum twelve, or to JC2.
- No reduction of e>1 to e=1.  The parent packet's negative control is
  restated, not strengthened.
- No exit price is asserted and no charge basis is declared by this review.
- The producer replay's PASS banner is not treated as evidence anywhere above;
  in particular LEADING_NONZERO_MATRIX_RANKS=EMPTY_AT_G3 is an unconditional
  print and was independently re-derived here instead.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31151`.
- Body SHA-256:
  `a2cadbae0232d194ec90093a9f8283c27721583ac32b04200f97b9a29474e900`.
- Frozen basis: `55067d08c111f473945700ded838a7798b8b3fb2`.
