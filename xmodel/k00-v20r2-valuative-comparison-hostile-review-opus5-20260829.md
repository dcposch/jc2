# Hostile review — `K00-V20R2-VALUATIVE-COMPARISON/v1`

Reviewer: Claude Opus 5 (independent hostile review)
Date: 2026-08-29
Coordinator basis: `0375694aa21fd8db3b465ef2098ca539106a1582`
Target: `xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md`

Verdict:

```text
PASS_WITH_REPAIRS_AND_ONE_MATERIAL_OMISSION
```

The report's arithmetic is correct everywhere I could recompute it, its
normalization is faithful to the pinned compiler byte-for-byte, and its
endpoint is honestly typed. The material omission is not an error but a
blind spot: **the report never looks at its own grade-2 block**, which
collapses from a nominal six quadrics to exactly **two linear conditions**,
and which together with grade 3 pins the leading jet to a **2-parameter
family** — a complete exact result I derived below in closed form.

---

## 1. Custody

Byte-exact, recomputed:

| item | expected | recomputed | verdict |
|---|---|---|---|
| full SHA-256 | `98fb3853…c0c97ecf` | `98fb38535405f1cc853dd4d430e26876a84f6f97c538f862f18a0446c0c97ecf` | CONFIRMED |
| body bytes | 11063 | 11063 | CONFIRMED |
| body SHA-256 | `c15bda71…96d51c` | `c15bda710b725c04c6ccf289fcf570c3414fe8825669ae68238c1d26fe96d51c` | CONFIRMED |

Body = bytes through the target's unique standalone body-end marker line
at line 347 including its newline; 331-byte seal trailer excluded. Exactly one
such marker occurrence in the target.

All eight pinned bytes resolve to real files at the current worktree:

```text
d72f774c  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/
            run/output/compiled_v2/tails.json
2ac7653c  cases/…_k00_common_lambda19_kuranishi_v20_20260827/
            compile_contracted_source_v20r2.py
9e304f58  cases/…_kuranishi_v20_20260827/RESULT_V20R2.md
4cdbd2ca  cases/…_kuranishi_v20_20260827/PREREGISTRATION.md
c2996ec8  cases/…_k00_closure_incidence_v1_20260827/PREREGISTRATION.md
abcb00ab  cases/…_k00_closure_incidence_v1_20260827/HISTORY_TYPE_AUDIT.md
5abd181a  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
e5e3472f  xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md
```

**Basis drift, benign.** The report's seal freezes
`31777ce90994a106aade85064c0d868e32863f94`, not the coordinator's
`0375694a`. `31777ce9` is an ancestor of `0375694a` and **no commit between
them touches any of the three pinned case directories**, so every pinned
byte is identical at both commits. Repair R8: state the coordinator basis
alongside the frozen one.

### 1.1 Literal section functor vs closure-first DVR arc

The report keeps these distinct and is right to. The two objects are:

* the **literal `K[[Lambda]]` section functor** — a map
  `A -> K[[Lambda]]` in which `Lambda` is *itself* the uniformizer, so every
  source coordinate is a power series in `Lambda`;
* the **closure-first DVR arc** — curve selection plus normalization gives
  `A -> R=K[[t]]` with `t` the uniformizer and `Lambda in m_R \ {0}`
  arbitrary, hence `Lambda = u(t) t^e` with `e = ord_t(Lambda) >= 1`.

The second specializes to the first only when `e=1`. V20R2 is the *first*
object: I confirmed its compiler truncates at `Q[Lambda]/(Lambda^20)`
(`compile_contracted_source_v20r2.py:888`) and emits `140 = 7*20` equations
in `Lambda`-grades `0..19`. So the report's premise — that V20R2 does not
represent `e>1` — is CONFIRMED at the level of the source functor, not
merely asserted.

---

## 2. Independent reconstruction of the source

I re-parsed `tails.json` from scratch without reading the report's
derivations.

**569 tails, CONFIRMED.** Row sizes `36, 54, 58, 81, 89, 120, 131`, summing
to `569`. The exponent vector has ten slots; the slot order
`(C0,…,C6,k10,k6,k2)` and the weight assignment are *forced* by the data,
not fitted.

**Weight action, CONFIRMED and overdetermined.** Under

```text
C_i -> a^(8-i) C_i,  k10 -> a^2 k10,  k6 -> a^6 k6,  k2 -> a^10 k2
```

**every one of the 569 monomials in row `l` has weight exactly `12+l`**;
zero violations. Because the load slots are `Lambda^2 k10`, `Lambda^6 k6`,
`Lambda^10 k2` and `Lambda` has weight 0, the slot weights are `2,6,10`,
matching. The target weights are then *forced*, not chosen:
`mu2:14, mu4:16, mu6:18, Jdet:19` are exactly `12+l` for `l=2,4,6,7`. This is
a 569-fold overdetermined confirmation of §2's weight table.

**Affine load-linearity, CONFIRMED.** Zero monomials have total degree `>1`
in `(k10,k6,k2)`. Sector census (R / A10 / A6 / A2) per row:
`19/12/4/1`, `27/18/7/2`, `30/19/7/2`, `40/27/10/4`, `44/30/11/4`,
`57/40/16/7`, `63/44/17/7`.

**`M_K00` is weight-homogeneous**, hence so is the whole chain (1.1):
`8C4-3C6^2` (weight 4), `16C2-C6^3` (6), `256C0-C6^4` (8) each scale
cleanly, and `Lambda`, `Jdet`, `C6*k10*Jdet` are homogeneous. Saturation and
colon by homogeneous elements preserve homogeneity, so `I, KL, K, B, H` are
all `G_m`-stable. This is the check that licenses acting by
`a(t) in R^* = G_m(R)` rather than by a constant, and the report does not
state it. Repair R9: state it; it is what makes §2 legitimate.

**Normalization (2.2), CONFIRMED byte-identical to the pinned compiler.**
Lines 890–891 of `compile_contracted_source_v20r2.py` read

```text
"C0": "(1+d0)/256", "C1": "d1", "C2": "(1+d2)/16",
"C3": "d3", "C4": "(3+d4)/8", "C5": "d5", "C6": "1"
```

i.e. exactly (2.2). So (2.2) is transcribed, not invented, and the `d_i` are
precisely the `C6=1` specializations of the six `M_K00` `C`-generators. Note
what this means for the report's standing: **V20R2 already assumed `C6=1`;
§2 supplies the Kummer justification V20R2 lacked.** That is a genuine
contribution and the report undersells it.

**Target signs and shifts, CONFIRMED byte-exactly.** Compiler lines 424–427
and 586–589:

```text
2: ("mu2", 14, -1)   4: ("mu4", 16, -1)
6: ("mu6", 18, -1)   7: ("Jdet", 19, Fraction(-1, 4))
```

matching `Phi_l = r_l - Lambda^(12+l) delta_l`,
`delta=(0,mu2,0,mu4,0,mu6,Jdet/4)`. The `1/4` on `Jdet` is real.

**Incidence (1.1), CONFIRMED verbatim** against
`…closure_incidence_v1_20260827/PREREGISTRATION.md:19-22`. The
preregistration itself (`:39`) *mandates* verifying that the
restriction-first localization is the unit ideal — so §6 is a required
control, not an optional one.

---

## 3. The stencil (3.1) — CONFIRMED, and it is an equality

I recomputed the `d`-order of every sector by exact expansion of all 569
monomials under (2.2):

| row | `ord_d R` | `ord_d A10` | `ord_d A6` | `ord_d A2` |
|---:|---:|---:|---:|---:|
|1|2|2|1|1|
|2|2|2|1|1|
|3|2|2|1|1|
|4|2|2|**2**|1|
|5|2|2|1|1|
|6|**3**|2|**2**|1|
|7|2|2|1|1|

This reproduces (3.1) exactly. **These are exact minima, not lower bounds.**
The report writes `>=`. For the literal §5 claim ("first *possible* grade")
`>=` is the correct direction and the report is not wrong; but the calendar
is only non-vacuous under equality, which I supply. Repair R1.

**Singularity, CONFIRMED and stronger than stated.** §0 says the source is
"singular to first transverse order". In fact **the entire Jacobian of all
seven rows in all thirteen variables vanishes** at the K00 point with
`Lambda=0`: every sector has zero constant and zero linear `d`-part
(`R(0)=A10(0)=A6(0)=A2(0)=0`, verified), every load carries `Lambda^{>=2}`,
every target carries `Lambda^{>=14}`, and `dPhi/dLambda = 0` at `Lambda=0`.
So no smooth/étale projection theorem can apply, for a stronger reason than
the report gives.

---

## 4. Ramification: can `e>1` be reparameterized away?

**(2.1), CONFIRMED.** `Lambda = u(t) t^e`, `u(0)!=0`, `R=K[[t]]` complete,
char 0. Adjoining an `e`th root of `u(0)` to the residue field and applying
Hensel gives `v in R^*` with `v^e=u`; then `t' = v t` is a uniformizer and
`Lambda = t'^e`. `ord_{t'} = ord_t` on everything else because `v` is a
unit. `e` is untouched. **No fractional exponent is introduced anywhere**:
the Kummer extensions in §2 are *residue-field* extensions, not
uniformizer extractions — this is the one place a conflation could hide, and
it does not.

Worth recording (the report omits it): after fixing `Lambda=t^e` the
residual gauge group is exactly `mu_e = {t -> zeta t}`. For `e=2` this is
`{t -> ±t}`, which flips the signs of odd-`t` coefficients but cannot
annihilate them. I use this in §7.

**`C6=1` Kummer, CONFIRMED.** `C6(t)` is a unit, so `a(t)^2 C6(t)=1` is
solvable in a quadratic residue extension by Hensel; `a` is a unit, so no
`ord_t` and no unit open changes; `Lambda` has weight 0 so `Lambda=t^e`
survives. Unit factors are harmless exactly because the ideal is
weight-homogeneous (§2 above). The two normalizations commute.

**`x^2-Lambda` control, CONFIRMED.** `K[Lambda,x]/(x^2-Lambda) = K[x]`, a
DVR at the origin with uniformizer `x` and `Lambda = x^2`. `D(Lambda)` is
`{x != 0}`, whose closure contains the origin; the arc is `Lambda=t^2, x=t`.
A section `x in K[[Lambda]]` needs `2 ord_Lambda(x)=1`. Impossible.
`e=2` is intrinsic here, not a bad choice of parameter.

**Scoping, CONFIRMED and honest.** §3 says outright: "This control does not
prove that the K00 source has a ramified arc; it proves that the proposed
`e=1` reduction is not licensed by general formal logic." That is exactly
the right claim and exactly as much as the control gives. No overreach.

**`x - Lambda*m` control (§6), CONFIRMED by hand.**
`K[Lambda,m,x]/(x-Lambda m) ≅ K[Lambda,m]` is a domain in which `Lambda*m`
is nonzero, so `I0:(Lambda m)^inf = I0`. Then
`I0+(Lambda)+(x) = (Lambda,x)`, and `(Lambda,x):m^inf = (Lambda,x)` — proper,
`m` a unit. Restriction first: `I0+(x) = (x, Lambda m)`, which contains
`Lambda m`, so `(x,Lambda m):(Lambda m)^inf = (1)`. Both outcomes are as
printed.

---

## 5. The literal cell: census — all CONFIRMED

**331 labelled.** `6*38 + 35 + 27 + 19 + 11 + 7 + 3 + 1 = 331`. Reproduced.
Truncation indices follow the naive prefactor rule
(`k10: 4+j<=38 -> j<=34`; `k6: j<=26`; `k2: j<=18`; `mu2: j<=10`;
`mu4: j<=6`; `mu6: j<=2`; `Jdet: j=0`).

**326 free** = 331 − 5 boundary zeros `k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0`.

**316 syntactically live.** Using the *stencil* (not the prefactor):
`d_i[n]` needs a partner `d` of order `>=1` so `n<=37` → `6*37=222`;
`k10[j]` needs `4+j+2<=38` → `j<=32` → 33; `k6[j]` needs `12+j+1<=38` →
`1<=j<=25` → 25; `k2[j]` needs `20+j+1<=38` → `1<=j<=17` → 17; targets 19.
`222+33+25+17+19 = 316`. Reproduced.

**10 inert** = `d_i[38]` (6) + `k10[33..34]` (2) + `k6[26]` (1) + `k2[18]`
(1); `316+10=326`. Reproduced.

**273 rows** `= 7*39`. Reproduced.

**Independent cross-validation of the whole convention.** Applying the *same*
labelling rule at `e=1`, depth `Lambda^19` gives
`6*19 + 18 + 14 + 10 + 6 + 4 + 2 + 1 = 169` labelled and `164` free — which
are **exactly the numbers V20R2 independently reports**
(`RESULT_V20R2.md`: "169 labelled source columns, five boundary constants…
164 free columns"). The report's 331/326 is the same convention at doubled
depth. This is the strongest available confirmation of §4 and it is
independent of the report.

### 5.1 GAP: the 273 figure is 33 short of substantive

Two deductions the report does not make:

* **14 trivial.** Grades `G00,G01` are `0=0` in all seven rows (the report
  says so in §5 but does not subtract them).
* **19 definitional.** Each target column appears in **exactly one** of the
  273 equations, **linearly, with constant coefficient** `-1` or `-1/4`:
  `mu2[1..10]` at row 2 grades 29–38; `mu4[1..6]` at row 4 grades 33–38;
  `mu6[1..2]` at row 6 grades 37–38; `Jdet[0]` at row 7 grade 38. All 19 are
  solvable for their own column and impose **no constraint whatsoever**.

So the substantive system is **240 equations in 297 columns**, and the entire
target sector — `mu2, mu4, mu6, Jdet`, i.e. the whole right-hand side of the
K00 deformation — is **vacuous at cutoff 38**. The `t^38` cutoff is the last
grade at which `Jdet` still costs nothing. Repair R4; this materially
changes what a successor solve at this depth can possibly decide.

---

## 6. The calendar (§5) — CONFIRMED entry by entry

With `Lambda=t^2`: loads `t^4 k10`, `t^12 k6`, `t^20 k2`; targets
`t^{2(12+l)} delta_l`. With `m=1`, `ord k10 = ord Jdet = 0`, and the other
five boundary orders `=1`:

| sector | first grade | derivation | verdict |
|---|---:|---|---|
| unloaded, rows 1,2,3,4,5,7 | 2 | `ord_d R = 2`, `m=1` | CONFIRMED |
| unloaded, row 6 | 3 | `ord_d R_6 = 3` | CONFIRMED |
| `t^4 k10 A10`, all rows | 6 | `4+0+2` | CONFIRMED |
| `t^12 k6 A6`, rows 1,2,3,5,7 | 14 | `12+1+1` | CONFIRMED |
| `t^12 k6 A6`, rows 4,6 | 15 | `12+1+2` | CONFIRMED |
| `t^20 k2 A2`, all rows | 22 | `20+1+1` | CONFIRMED |
| `t^28 mu2`, row 2 | 29 | `28+1` | CONFIRMED |
| `t^32 mu4`, row 4 | 33 | `32+1` | CONFIRMED |
| `t^36 mu6`, row 6 | 37 | `36+1` | CONFIRMED |
| `t^38 Jdet/4`, row 7 | 38 | `38+0` | CONFIRMED |

Source signs and target shifts are the compiler's (§2 above). The sequential
ledger `G00–G38` follows.

### 6.1 Why this is not the valuation-four packet with grades doubled

The report asserts non-importation ("The calendar does not import any
valuation-two/four/five periodicity") but never argues it. §7 mutation 6
("deletion of all odd `t` columns") tests it without stating it. The
argument is available and I supply it:

The "doubled" locus is exactly `{all odd-t columns = 0}` — every coordinate
a series in `t^2 = Lambda`, which is precisely the `e=1` packet
reparameterized. The emitted cell is **disjoint** from it, twice over:
the open (4.3) forces some `d_i[1] != 0`, and `B11111` forces
`k6[1], k2[1], mu2[1], mu4[1], mu6[1] != 0` — all odd-`t` columns. And no
reparameterization can repair this, because with `Lambda=t^2` fixed the
residual gauge is only `mu_2 = {t -> ±t}`, which flips odd coefficients'
signs but cannot kill them. Repair R5a.

**But the report should also record the countervailing fact, which cuts
against its own framing.** The minimum load grade is `2e+2` for *any* `e>=1`,
so **grades 2 and 3 are literally identical polynomials for `e=1` and
`e=2`**. The separation first occurs at **grade 4**, where the `e=1` packet
has a `k10` term and the `e=2` packet does not. The front of the calendar —
the only part any cheap solve reaches — is shared with V20R2 and carries no
ramified content at all. Repair R5b. This is not a refutation; it relocates
where the report's own thesis becomes testable.

---

## 7. MATERIAL OMISSION — exact grade-2/grade-3 collapse

The report emits the source and stops. Its grade-2 block is desk-scale and
collapses. Everything below is my own exact computation over `Q`, done
from `tails.json` and (2.2) only.

Since loads start at grade `2e+2 >= 6`, grade 2 is exactly
`R_l^{(2)}(d[1]) = 0` — six quadratic forms `Q_1,…,Q_5,Q_7` in the six
unknowns `d[1]`, with `Q_6 ≡ 0`. Cleared to primitive integer form:

```text
Q1 = 2 d0d3 - d0d5 + 32 d1d2 - 32 d1d4 - 16 d2d3 + 6 d2d5 + 12 d3d4 - 4 d4d5
Q2 = d0d2 - d0d4 + 2048 d1^2 - 2048 d1d3 + 768 d1d5 - 4 d2^2 + 6 d2d4
     + 384 d3^2 - 256 d3d5 - 2 d4^2 + 40 d5^2
Q3 = 8 d0d1 - 3 d0d3 + d0d5 - 48 d1d2 + 32 d1d4 + 16 d2d3 - 5 d2d5
     - 10 d3d4 + 3 d4d5
Q4 = d0^2 - 8 d0d2 + 4 d0d4 - 16384 d1^2 + 8192 d1d3 - 2048 d1d5 + 16 d2^2
     - 16 d2d4 - 1024 d3^2 + 512 d3d5 + 4 d4^2 - 64 d5^2
Q5 = -32 d0d1 + 6 d0d3 - d0d5 + 96 d1d2 - 32 d1d4 - 16 d2d3 + 2 d2d5 + 4 d3d4
Q7 = -8 d0d1 + d0d3 + 16 d1d2 - d2d5 - 2 d3d4 + d4d5
```

**(a) Rank is 4, not 6.** Two exact universal syzygies, verified literally:

```text
Q1 + Q3 + Q7      == 0
3*Q1 + 4*Q3 + Q5  == 0        (equivalently Q5 = Q1 + 4*Q7)
```

These are identities among the *frozen tails*; they hold for every `e` and
every cell. **No item of the §7 producer contract would detect them**: a
producer satisfying all seven items emits a grade-2 block it believes has
six rows and reports a rank wrong by 2.

**(b) `Q4` factors.** With

```text
P := d0 - 4 d2 + 2 d4        R := 16 d1 - 4 d3 + d5
```

one has, exactly, `Q4 = (P - 8R)(P + 8R)`, and **all six `Q_l` lie in the
ideal `(P,R)`** (verified by reduction).

**(c) The grade-2 locus is exactly the linear space `V(P,R)`.**
Let `sigma: d_i -> (-1)^i d_i`. Then `sigma` negates `Q1,Q3,Q5,Q7` and fixes
`Q2,Q4` (every monomial of the first group is even·odd, of the second
even·even), so `sigma` preserves the locus, fixes `P` and negates `R`, hence
swaps the two `Q4` branches. On the branch `P=8R`, each `Q_l` restricts to
`R * W_l` with `W_l` linear, and `rank{W_1,W_2,W_3,W_7} = 3` with
`R in span{W_l}` — so the branch contributes nothing outside `{R=0}`, giving
`V(Q) ∩ {P=8R} = V(P,R)`; `sigma` transports this to `{P=-8R}`. Hence

```text
V(Q1,...,Q7) = V(P,R),   a codimension-2 LINEAR subspace.
```

Six quadrics reduce to **two linear conditions**. (Prime navigation agreed
in advance: the affine cone has exactly `p^4` points for
`p = 5,7,11,13,17,19`.)

**(d) Grade 3 supplies exactly two `d[2]`-free cubics.** Grade 3 is
`grad Q_l(d[1]) · d[2] + R_l^{(3)}(d[1]) = 0`. Row 6 has `Q_6 ≡ 0`, and each
syzygy kills its own gradient combination, so three necessary conditions on
`d[1]` alone drop out — and the two syzygy cubics are negatives of each
other, leaving two. On `V(P,R)`, with

```text
u := d2[1] - d4[1]        v := 8 d1[1] - d3[1]
```

they factor exactly:

```text
F1 := R_6^(3)                        =  u * (192 v^2 -   u^2)
F2 := (3/128)R_1^(3) + (1/8)R_3^(3) + R_5^(3)
                                     =  v * ( 64 v^2 - 3 u^2)
```

`u=0 => F2 = 64v^3 = 0 => v=0`; `v=0 => F1 = -u^3 = 0 => u=0`; and
`u^2=192v^2` with `3u^2=64v^2` gives `576v^2=64v^2`, so `v=0`. In char 0 the
only common zero is `u=v=0`.

**(e) Conclusion — the leading jet is pinned to a plane.** Combining
`P=R=u=v=0`:

```text
d0[1] = 2 d2[1],   d3[1] = 8 d1[1],   d4[1] = d2[1],   d5[1] = 16 d1[1]
```

i.e. `d[1] = (2mu, lam, mu, 8lam, mu, 16lam)` — a **2-dimensional** space
`L`, down from 6. It meets the open (4.3) off the origin, so **the emitted
cell is not empty at grades 2–3**.

**(f) `L` is the common kernel; grade 3 is then vacuous.** On `L` every
`grad Q_l` vanishes and every `R_l` vanishes to order `>= 4` (exact symbolic
restriction), so all seven grade-3 equations read `0=0` and `d[2]` is
entirely free. Two structural consequences:

* at **every** grade `g`, the column `d[g-1]` is absent, because its only
  possible coefficient is `2B_l(d[1], ·) = grad Q_l(d[1]) = 0`; the newest
  live `d`-column at grade `g` is `d[g-2]` (a one-step lag);
* row 6 is identically zero at grades 2, 3 **and 4** (`Q_6 ≡ 0`,
  `grad R_6^{(3)} ≡ 0` on `L`, `R_6^{(4)}|_L = 0`), so the calendar's `G03`
  entry for row 6 is **never realized** — its first possibly-live grade is 5.

**End-to-end validation.** With `d[1] in L`, `d[2]`, `d[3]` random and
`k10` random, direct series evaluation of all 569 tails mod `t^8` gives
`[t^0..t^3] = 0` in all seven rows and nonzero `t^4` in rows 1,2,3,4,5,7
(row 6 zero) — confirming the whole pipeline independently of the algebra.

**(g) This applies to V20R2 as well.** Grades 2 and 3 are `e`-independent,
so (a)–(f) hold verbatim for V20R2's own `e=1` packet. The collapse is a
gap in both.

---

## 8. Endpoint audit — `RAMIFIED_RESIDUAL_EMITTED`

I checked the endpoint against each forbidden claim:

| must not claim | status |
|---|---|
| a surviving point | CLEAN — §0: "not a point and not an assertion that it is nonempty"; §8: "does not prove … that the emitted cell has a point" |
| an arc | CLEAN — §8: "does not prove … that any formal arc is algebraic, Taylor-realizable, rational, polynomial" |
| a map | CLEAN — §8: "Formal data are not a map" |
| a counterexample | CLEAN — §8 disclaims Keller attainment and JC2 |
| a source-wide closure theorem | CLEAN — §8: "proves only that `e=1` is not presently reducible from the pinned source" |
| a JC2 consequence | CLEAN — §8 explicit |

The endpoint is honestly typed. §8 is one of the better scope firewalls in
the campaign: it separates "no theorem exists in the pinned corpus" from
"the negation is true", and never crosses. `FALLACY-v2` floor/attainment,
carrier/attainment and `sat()`-wrapping hazards are all respected;
`sat()` order is preregistered and controlled (§6).

Two wording items:

* §0 "The pinned source does not contain a theorem…" is a negative over a
  corpus. I verified the eight pinned artifacts and V20R2's own firewall
  ("does not … exclude a formal or algebraic arc"). Marked
  **CONFIRMED-AT-PINNED-SCOPE**; a corpus-wide negative is not
  independently checkable at desk scale and should be typed as such.
* "`B11111` records the five exact boundary-series orders in the displayed
  order" — the displayed block lists **seven** orders (`k10` and `Jdet` at 0
  come first). The five are recoverable but the phrase is ambiguous. Repair
  R6.

### 8.1 Omitted support/load faces

Every face the emitted cell does **not** cover. The five marked **(S)** are
separately omitted and *silent* — §8's list does not name them:

1. `e >= 3` (all higher ramification). Named in §8.
2. `e=2, m >= 2` (higher transverse order). Named in §8.
3. **(S)** `ord_t(k6) >= 2`, including `k6 ≡ 0`.
4. **(S)** `ord_t(k2) >= 2`, including `k2 ≡ 0`.
5. **(S)** `ord_t(mu2) >= 2`, including `mu2 ≡ 0`.
6. **(S)** `ord_t(mu4) >= 2`, including `mu4 ≡ 0`.
7. **(S)** `ord_t(mu6) >= 2`, including `mu6 ≡ 0`.
   Items 3–7 matter more than the report suggests: (4.3) demands
   `k6[1], k2[1], mu2[1], mu4[1], mu6[1]` all nonzero, so the cell requires
   **all three multipliers to have order exactly 1 simultaneously**. The
   `mu_j ≡ 0` faces — arguably the generic K00 situation, since `mu2, mu4,
   mu6` are `M_K00` generators — are entirely outside the cell.
8. `V(k10)` — named in §8.
9. `V(C6)`, the tip — named in §8. Note the whole of §2's normalization
   fails here, so this face needs a different derivation, not just a
   different cell.
10. `V(Jdet)` — excluded twice (saturated in `K`, then localized in `H`).
11. **(S)** the six sub-faces of `m=1`. (4.3) pools
    `D(d0[1]) ∪ … ∪ D(d5[1])` without stratifying by which `d_i` attains the
    minimum. My §7 result shows the surviving stratum is the plane `L`,
    inside which `lam=0` and `mu=0` are two further distinguished sub-faces
    the census does not separate.
12. Non-K00 boundary strata of `V(K) ∩ V(Lambda)` — `M_K00` is imposed, so
    only the K00 stratum is seen.
13. Gate T, order two, maximum twelve, other load rays / square normals,
    JC2 — all named in §8.

---

## 9. Claim-by-claim verdicts

| # | claim | verdict |
|---|---|---|
| 1 | custody: full/body SHA, body bytes | **CONFIRMED** (byte-exact) |
| 2 | eight pinned bytes resolve | **CONFIRMED** (all 8 located) |
| 3 | frozen basis `31777ce9` | **CONFIRMED-BENIGN** (ancestor; pinned dirs unchanged) |
| 4 | 569 frozen tails, weights, load-linearity | **CONFIRMED** (0 violations / 569) |
| 5 | weight action on every source coordinate | **CONFIRMED** (target weights forced) |
| 6 | `Lambda = u t^e -> t^e` removes only a unit | **CONFIRMED** |
| 7 | `C6=1` weight-two Kummer, orders/opens unchanged | **CONFIRMED** |
| 8 | no fractional exponent / quotient point / formal-section conflation | **CONFIRMED** |
| 9 | normalization (2.2) | **CONFIRMED** (= compiler lines 890–891) |
| 10 | stencil (3.1) | **CONFIRMED**, and exact equality |
| 11 | K00 singular, no étale/smooth reduction | **CONFIRMED**, full Jacobian vanishes |
| 12 | `x^2-Lambda` negative control | **CONFIRMED**, correctly scoped |
| 13 | `x-Lambda*m` restriction/saturation control | **CONFIRMED** |
| 14 | incidence (1.1) | **CONFIRMED** (= preregistration :19–22) |
| 15 | 331 labelled columns | **CONFIRMED** |
| 16 | 326 free columns | **CONFIRMED** |
| 17 | 316 syntactically live columns | **CONFIRMED** (syntactic reading) |
| 18 | 10 certified-inert columns | **CONFIRMED** |
| 19 | 273 rows through `t^38` | **CONFIRMED** as a count; **GAP** as content (14 trivial + 19 definitional; 240 substantive) |
| 20 | calendar G2/G3/G6/G14/G15/G22/G29/G33/G37/G38 | **CONFIRMED** (all 10) |
| 21 | target signs and shifts | **CONFIRMED** (compiler :424–427) |
| 22 | "not the doubled valuation-four packet" | **CONFIRMED but UNARGUED** — proof supplied (R5a); needs the grade-2/3 identity caveat (R5b) |
| 23 | minimality of `e=2, m=1` | **CONFIRMED-AS-DEFINITIONAL / GAP as mathematics** (see below) |
| 24 | `B11111` naming | **GAP** (display shows seven orders) |
| 25 | V20R2 does not represent `e>1` | **CONFIRMED** (`Q[Lambda]/(Lambda^20)`) |
| 26 | endpoint `RAMIFIED_RESIDUAL_EMITTED` | **CONFIRMED CLEAN** |
| 27 | §7 producer contract adequacy | **GAP** — syzygy-blind and rank-blind |
| 28 | grade-2 block has six independent rows | **REFUTED** (rank 4; two exact syzygies) — *implicit in §5's "rows 1,2,3,4,5,7 begin"*, never asserted outright |
| 29 | "cancellations … must be decided from the literal equations" (§5) | **CONFIRMED and now decided** — see §7 |

On **#23**: `e=2` and `m=1` are lex-minimal by fiat under a declared,
non-canonical order; `m>=1` is forced by `d(0)=0`, the five boundary orders
`>=1` by `M_K00`, and `ord k10 = ord Jdet = 0` by the localizer — so none of
these is a free choice. The only mathematical content is "`e>=2` is not
excluded", which §3 establishes solely as *not formally licensed*. Under a
different ordering (e.g. by codimension, or by the grade of first
obstruction) the "first" cell is different. The report's own gloss
("'First' means…") is honest; the word should not be read as a theorem.

---

## 10. Required repairs

* **R1** — state (3.1) as exact equalities (verified), noting the calendar
  needs equality to be non-vacuous.
* **R2** — record that on the unique surviving leading-jet stratum row 6 is
  identically zero through grade 4, so the `G03` calendar entry is never
  realized.
* **R3** — record the two exact syzygies `Q1+Q3+Q7=0`, `3Q1+4Q3+Q5=0` and
  the grade-2 rank 4; add producer item (8): *certify the rank of the
  grade-2 block and reproduce both syzygies*.
* **R4** — record that 14 of the 273 are trivial and 19 are pure target
  definitions; state the substantive system as 240 equations in 297 columns
  and that the target sector is vacuous at cutoff 38. Add producer item (9)
  certifying the target columns are sinks.
* **R5a** — supply the disjointness argument against the doubled packet
  (odd-`t` content forced by (4.3) and `B11111`; residual gauge only `mu_2`).
* **R5b** — state that grades 2 and 3 are `e`-independent, so separation from
  V20R2 begins at grade 4, not grade 2.
* **R6** — disambiguate `B11111` (the display lists seven orders, the label
  encodes five).
* **R7** — pin the `d_i[0]` convention. §4 labels `d_i` from `n=1` while
  labelling `k6,…` from `j=0` and then zeroing; a producer that labels
  `d_i[0]` gets 337, not 331. Both give 326 free, but the headline differs.
* **R8** — reconcile the frozen basis with the coordinator basis.
* **R9** — state that `I, KL, K, B, H` are weight-homogeneous; this is what
  licenses acting by `a(t) in G_m(R)` rather than a constant in §2.
* **R10** — §7 mutation 6 lists "deletion of all odd `t` columns" but §5/§0
  never state what that mutation is *for*; tie it to R5a.

None of R1–R10 touches the endpoint; all are additive.

---

## 11. Maximum safe statement

> Relative to the frozen basis and the eight pinned artifacts, the pinned
> K00 source supplies no theorem reducing a closure-first DVR arc through
> the generic K00 ray to `ord_t(Lambda)=1`; the general implication
> "closure incidence ⟹ `K[[Lambda]]` section" is refuted by the exact
> control `x^2-Lambda`, and the K00 rows have identically vanishing full
> Jacobian at the K00 point with `Lambda=0`, so no reviewed smooth or étale
> projection theorem supplies the reduction. V20R2 is exactly the `e=1`
> source functor (truncation `Q[Lambda]/(Lambda^20)`, `140=7*20` equations,
> 169 labelled / 164 free columns); the constructible cell
> `e=2, m=1, B11111` is therefore not represented by it, and its literal
> finite source through `t^38` is the stated 331/326/316-column,
> 273-equation system with the stated ten-entry grade calendar, of which 14
> equations are trivial and 19 are pure target definitions.
>
> Independently and exactly: the grade-2 block of that system has rank 4,
> not 6, with the universal syzygies `Q1+Q3+Q7=0` and `3Q1+4Q3+Q5=0`; its
> zero locus is the codimension-2 *linear* space `V(P,R)`,
> `P=d0-4d2+2d4`, `R=16d1-4d3+d5`; and grades 2–3 together force the
> leading jet onto the 2-plane `d0=2d2, d3=8d1, d4=d2, d5=16d1`, on which
> every grade-3 equation is vacuous and `d[2]` is free. This plane is
> nonempty and meets the cell's exactness open, so the cell survives grades
> 2 and 3. Because grades 2 and 3 are `e`-independent, the same collapse
> applies to V20R2's own `e=1` packet.
>
> This establishes no point of the cell over any field, no arc, no map, no
> lift of any jet past grade 3, no counterexample, no closure verdict for
> `H`, and nothing about order two, maximum twelve, Gate T, or JC2. The
> cell's non-emptiness at grades 2–3 is a statement about the truncated
> jet system only, not about the scheme `H`.

---

## 12. Cheapest exact successor attack on the emitted cell

The grade-2/3 work above is done and exact. The successor is **grade 4**,
and it is desk-scale. Three reasons it is the right target:

1. It is the **first grade at which `e=2` differs from `e=1`** (`k10` enters
   at grade `2e+2`), so it is where the report's own thesis first becomes
   testable.
2. `d[3]` is **absent** from it (§7(f) one-step lag), so it is a system in
   `d[2]` alone over the 2-parameter base `(lam,mu)`.
3. Row 6 is identically zero there, so it is **six** equations, not seven.

Explicitly, for `d[1] in L` the grade-4 system is

```text
Q_l(d[2])  +  grad R_l^(3)(d[1]) · d[2]  +  R_l^(4)(d[1])  =  0,
                                      l = 1,2,3,4,5,7
```

— six equations in the six unknowns `d[2]` plus the two parameters
`(lam,mu)`, with the **same** quadrics `Q_l` acting on `d[2]`. Because those
`Q_l` carry the `(P,R)` collapse and the two syzygies, the syzygies
immediately produce two more `d[2]`-free conditions, now **quartics** in
`(lam,mu)`; a binary quartic in two homogeneous parameters either vanishes
identically or has at most four roots in `P^1`. So the cheapest exact
successor is:

> Compute the two syzygy combinations of the grade-4 equations. Each is a
> `d[2]`-free binary form in `(lam,mu)`. If their gcd is 1, the leading jet
> is cut to **finitely many points of `P^1`** and the cell is decided at
> grade 4 by hand.

This is a few minutes of exact rational arithmetic on the same 569 tails,
needs no Singular, no prime, and no AWS. It should be run **before** any
273-equation producer is commissioned, since it may make the producer
unnecessary.

Secondary, also cheap: the same computation at `e=1` (where `k10` *does*
enter at grade 4) is the matching control, and the difference between the
two is the first quantitative measure of what ramification buys.

**Marked boundary.** I did not carry out the grade-4 solve. Everything
reported in §7 is exact over `Q` and complete; grade 4 and beyond is
untouched, as is every omitted face in §8.1.

---

## 13. Execution record

Environment: pure CPython, no `sympy`, no `numpy`, exact `fractions.Fraction`
throughout. No Singular. No network. `jc2-lean` never entered, listed,
searched, stat'ed, built, or read. No canonical ledger or existing artifact
modified; this file is the only repository write.

Exact (mathematical lane, over `Q`): tail parse and 569-monomial weight and
load-linearity audit; sector orders (3.1); all column and row counts; the
`e=1` cross-validation against V20R2's 169/164; grade-2 rank and both
syzygies; the `Q4` factorization; ideal membership in `(P,R)`; the branch and
`sigma` argument for `V(Q)=V(P,R)`; the `F1,F2` factorizations and their
common zero; the symbolic restriction of all seven rows to `L`; the
vanishing of `grad Q_l` and `grad R_6^(3)` on `L`; the end-to-end series
check mod `t^8`.

Navigation only (primes, no verdict rests on it): point counts of the
grade-2 cone (`p^4` for `p=5,7,11,13,17,19`) and of the grade-3-solvable
locus (`p+1` for `p=7,11,13,17,19,23,29,31`). Both were superseded by the
exact arguments above and are reported only as the route by which the
closed forms were found.

Not attempted, and flagged rather than guessed: any grade `>= 4` solve; any
statement about `H` itself; any corpus-wide search for an `e=1` reduction
theorem outside the eight pinned artifacts.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `32746`.
- Body SHA-256:
  `abda4663bff675ba258223eaf9bf20874a2c8f427f440797f79c04f9688c09e9`.
- Frozen basis: `0375694aa21fd8db3b465ef2098ca539106a1582`.
