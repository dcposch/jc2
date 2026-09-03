# P202-10 gate audit — Sol's sharpest candidate vs Moh's six + four extras

Lane `p202-ten-rows-gate-audit-grok46-20260903`. Desk-scale, one core, < 3 min.
No ledger edit; no `jc2-lean`; no other `ideation-20260903T1015Z-*` than the
three charged; no other running lane's report opened.

**Frozen inputs (SHA-256 verified before any read; all matched):**

```text
20f290f7e33a3b8a4f97d303751633b9d9b2df50ca8cbd0a46498856be5d5b2f  ideation-20260903T1015Z-sol56.md
486b0192d6cb1f3e064e00d16b57877ed67a2360543d8ec662c837afe5fc6456  ideation-20260903T1015Z-fable5.md
b13149ecac656f7f3548e6cd388b1699c514ff49a53882f7239039a2c0022562  ideation-20260903T1015Z-opus5.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
```

Source-read: Moh 1983 JRAM 340 rendered at 300 dpi (`pdftoppm -r 300`); journal
page N = PDF page N−139. Pages opened as images: 179–189, 193–194, 196–202,
207–212 (PDF 40–50, 54–55, 57–63, 68–73), plus Prop 4.6 at p.171. Predicates run
on `census(n, Kmin=2, full=True)` of `box/moh_skeleton_full.py` (unmodified).
`forced-(10)` := `cond1011(j)[1]` at every `j ∈ {2,…,s−1}` (require the printed
nonzero branch; a row that also admits (11) is kept — otherwise the printed
`(84,56) M_2=72, V_2=5` row dies).

---

## 0. Headline

Sol's conjunction `M_2 > n − d_2 ∧ forced-(10) at every level` is reproduced
fail-closed: **10 rows / 6 classes, 6/6 printed kept**, `(75,50)` residue exactly
`M_2=55, V_2∈{2,3}`. It is **not** Moh's program. Prop 5.6 licenses NOT-ALL-(11),
not forced-(10)-at-every-`j`. `M_2 > n − d_2` is **not** printed (Def 5.1 and
Lemma 6.1 give *upper* bounds on `M`). No printed assertion kills the four
extras and spares the six. Appendix II names only `(64,48), (84,56), (75,50),
(99,66)`; extras live at `(96,64)` and `(100,40)`. Favoured reading:
**unprinted program rule**. The `(75,50,40,1)` falsifier is killed by
`M_2 > n−d_2` (`d_2=25`, `n−d_2=50`, `40 ≯ 50`), by `M_2>m`, and by `V_2≥2`;
it passes forced-(10) and Prop 5.3 at `r=2`; the bottom star exists for `b≠0`;
the two-level glue does not fail a printed local condition.

`OPEN[MOH-PROGRAM]` stays: bounded **652 excess rows / 59 classes**
unconditionally; **4 extras** after Sol's unlicensed conjunction.

---

## 1. Four gates, fail-closed — MEASURED

Base: `(1)–(13)`, `n≤100`, `Kmin=2`, `full=True`: **658 rows / 63 classes**.
Printed control = the six p.202 rows in `MOH_TABLE` (bracketed alternates split).

```text
predicate                                         rows  cls  printed  (75,50) residue
(1)-(13) baseline                                  658   63   6/6     9 rows, M2 in {5,10,40,55,60}
SOL  M2 > n-d2                                      57   16   6/6     4: (55,V2=2,3), (60,V2=9,20)
SOL  forced-(10) every j                           156   40   6/6     5: (10,1),(40,1),(40,2),(55,2),(55,3)
SOL  conjunction (the P202-10 gate)                 10    6   6/6     2: (55,2),(55,3)   <-- exact
FABLE M2 > m                                        94   32   6/6     4: (55,2,3),(60,9,20)
FABLE M2 > m AND UNI N>=6                           33   17   5/6     2: (55,2),(55,3)
                                                     missing printed (84,56) M2=64 V2=2
OPUS INCREMENT Aj>=2                               391   62   6/6     7
OPUS NOT-ALL-(11) (= any (10))                     469   43   6/6     5
OPUS MAJOR-MULT Vj>=2 all j                        312   55   6/6     7
OPUS-3  INCREMENT ∧ NOT-ALL-(11) ∧ MAJOR-MULT       51   13   6/6     2: (55,2),(55,3)   <-- exact
SOL unlicensed A_{s-1}|(n-m)                       181   29   6/6     2: (55,2),(55,3)   <-- exact
```

Every 6/6 claim keeps all six except Fable's `N>=6` (kills printed `(84,56) M_2=64`). Exact `(75,50)` residue is met by Sol-conj, Opus-3, and `A_{s-1}|(n-m)`, not by the solo clauses. Sweep 0.5 s.

### 1.1 2×2 of Sol's two clauses (658 rows)

```text
                     forced-(10)=T          forced-(10)=F
M2 > n-d2 = T        10 / 6 cls, 6/6        47 / 14 cls, 0/6
M2 > n-d2 = F       146 / 40 cls, 0/6       455 / 52 cls, 0/6
```

Neither clause implies the other. The printed six sit only in the `TT` cell.

### 1.2 2×2×2: Sol-conj × Fable `M_2>m` × Opus MAJOR-MULT

```text
Sol10  Fable  Major    rows / cls   printed
  T      T      T       10 /  6      6/6     <-- all ten live here
  T      T      F        0 /  0      0
  T      F      T        0 /  0      0
  T      F      F        0 /  0      0
  F      T      T       67 / 29      0
  F      T      F       17 /  7      0
  F      F      T      235 / 44      0
  F      F      F      329 / 37      0
```

Sol-conj sits only in the `TTT` cell: it implies both `M_2>m` and MAJOR-MULT
(and Opus-3: 10 ⊂ 51). The 2×2×2 of Sol's two clauses against `M_2>m` (resp.
MAJOR-MULT) has the same degeneracy: 0 rows with `M_2>n−d_2` and not `M_2>m`
(resp. not MAJOR-MULT).

### 1.3 Which implies which on the 658 (proper inclusions only)

```text
M2 > n-d2          =>  M2 > m          (57 ⊂ 94)
M2 > n-d2          =>  MAJOR-MULT      (57 ⊂ 312)
forced-(10)        =>  NOT-ALL-(11)    (156 ⊂ 469)     [tautological]
Sol-conj           =>  each conjunct, M2>m, INCREMENT, NOT-ALL-(11),
                       MAJOR-MULT, Opus-3
Opus-3             =>  each of its three clauses
M2>m ∧ N>=6        =>  M2 > m
```

`M_2>n−d_2 ⇒ M_2>m` because `n−d_2=K(e−1) ≥ Kd^*=m`, equality iff `e−d^*=1`
(all six printed and the three `(96,64)` extras; the `(100,40)` extra has
`(d^*,e)=(2,5)`, `n−d_2=80>m=40`). `M_2>n−d_2 ⇒ MAJOR-MULT` because (7) is
`V_2 > d_2/(n−M_2)` and the hypothesis makes the lower window `>1`, so
`V_2≥2` (measured: all 57 have `V_j≥2` every `j`) — a *consequence*, not a
source. Sol-conj does **not** imply `A_{s−1}|(n−m)` (three extras fail it).

### 1.4 Symmetric difference Sol's ten vs Fable's 33 — MEASURED

`|Sol10|=10`, `|Fable33|=33`, intersection **9**, `|Sol10 Δ Fable33|=25`.

**Sol10 \ Fable33 (1 row):** the printed `(84,56) M=(64,82) V=(2,3)`, which has
`M_2>m` but no integral UNI `N≥6` (census-rebase §6.1: achievable `N={4}`).

**Fable33 \ Sol10 (24 rows).** Six of them have `M_2>n−d_2` and die only on
forced-(10): `(80,60)[68,78] V=(7,3)`; `(84,56)[70,77,82] V=(5,10,5)`;
`(96,72)[80,84,94] V=(7,6,3)`; `(96,64)[80,84,94] V=(5,4,3)`;
`(96,64)[80,88,92,94] V=(5,10,5,3)`; `(100,75)[85,98] V=(7,3)`.
The other 18 fail `M_2>n−d_2` (Fable's charged residual list: `(75,45)`, four
`(80,*)`, `(84,36)`, `(84,60)`, `(90,36)`, `(96,60)`, `(98,42)`, nine
`(100,40)` with `M_2=50`). Full 24-line dump in `/tmp/p202-audit/gates.out`.

The four Sol extras **are in the intersection** (they have integral `N≥6`).
Fable's “28 extras beyond the printed table” = these 24 plus the four Sol extras
(the printed `(84,56) M_2=64` is in Sol10 but not in the 33, so 33−5 printed
survivors of `N≥6` = 28).

**Typed.** MEASURED. Bounded: 658 rows; cheapest test is the table above.

---

## 2. Source-audit of Sol's two clauses

### 2.1 Forced-(10) at every level — OVER-READING of Prop 5.6; not licensed by Prop 5.3

**Prop 5.6 (p.188–189), quote:**

> Suppose that `s ≥ 2` and that a tower of major discs
> `D_s ⊇ D_{s−1} ⊇ ⋯ ⊇ D_1` has been constructed. If the corresponding π-root
> `σ_1`, which is the unique one in `D_1`, is of the following form
> `σ_1 = π t^{δ_1}` then either `k[x,y] = k[T_1^ψ, g] = k[f,g]` or there exists
> an automorphism `k[x,y] → k[x,y]` which will reduce the degrees of `f(x,y)`,
> `g(x,y)` and `T_1^ψ(f(x,y), g(x,y))` simultaneously.

Both alternatives contradict search (3). `σ_1 = π t^{δ_1}` means every `α_j`
vanishes, i.e. the selected factor of `p(π)` was `π` (`a=0`, branch (11)) at
**every** level of the tower. That is the all-(11) configuration.

**p.201 l.52, quote (the program's own gloss):**

> Furthermore we shall note that the situation indicated by the equation (11)
> can not always happen as established by Proposition 5.6.

“Can not always” is NOT-ALL-(11): at least one `j` admits (10). It is not
“(11) can never happen at any level.” Moh *prints* (11) as a numbered search
option. The `(84,56) M_2=72, V_2=5` printed row admits **both** (10) and (11)
(`TRI=5, SQ=1, V_2=5`); a reading that forbids (11) outright would have to be
reconciled with that row, and a reading that *requires* (10) at every level is
strictly stronger than Prop 5.6.

Opus's NOT-ALL-(11) (469 rows) is the numerical shadow already raised as
`OPEN[PROP-5.6-SHADOW]`. Sol's forced-(10) (156 rows) is a sharpening of that
shadow, not the proposition.

**Prop 5.3 (p.180), quote — construction of the next disc from a factor of `p(π)`:**

> Let `π − C_r` be a factor of `p(π)` as in the conclusions of Proposition 4.6
> with multiplicity `V_r` satisfying
> `deg p(π) = V_{r+1}(d_r/d_{r+1}) ≥ V_r > d_r/(n−M_r)`.

`C_r` is **not** required to be nonzero. Prop 5.3 licenses both `π−a` (`a≠0`,
(10)) and `π` (`C_r=0`, (11)). The rest of the proof constructs
`δ_{r−1} = δ(M_{r−1})` and extends the major-disc tower; it never forces the
nonzero branch.

**p.184 (Prop 5.4, `δ_i > −1`, `i>1`).** Moh takes a factor `π−a` with `a≠0`
and the automorphism `y → y−h(x)` to *reduce* `σ` to `π t^{δ_i}` and drop
degrees, contradicting search (3). That uses (10) as a reduction tool, not as
a search constraint that every surviving tower must choose (10). The search
case `δ_s=−1` is exactly when this reduction does not fire.

**Typed.** Forced-(10) at every `j`: **NOT-IN-SOURCE** as a necessary condition;
**OVER-READING** of Prop 5.6 (which forbids ALL levels taking (11), not ANY
level taking only (11)). Prop 5.3 **licenses both branches**. NOT-ALL-(11) is
the licensed numerical shadow (**DERIVED** from Prop 5.6 + search (3), with
the residual `r=2` gap already typed in census-rebase §1.4). MEASURED cut of
the over-reading: 658 → 156 vs licensed shadow 658 → 469.

### 2.2 `M_2 > n − d_2` — NOT-IN-SOURCE; the printed inequalities go the other way

**Def 5.1(2), p.179, quote:**

> `V_{i+1} d_i / d_{i+1} ≥ V_i > d_i/(n − M_i)` for `i = r+1,…,s`,
> `V_{s+1} = d_{s+1}`.

At `i=2`: `V_2 > d_2/(n−M_2)`, i.e. **`M_2 < n − d_2/V_2`** — an *upper* bound
on `M_2`. Sol's predicate is the *lower* bound `M_2 > n − d_2`. They are
compatible on a nonempty interval of length `d_2(1−1/V_2)` when `V_2≥2`, but
Def 5.1 does not assert the lower bound.

**Lemma 6.1, p.194, quote:**

> Suppose that `g(x,y)` is monic in `y` with `deg g = deg_y g = n > 1`. Let
> `D_s ⊇ D_{s−1}` be a tower of major discs with logarithmic radii `δ_s` and
> `δ_{s−1}`. If `δ_s = −1` then `δ_{s−1} ≥ 0`.

The preceding display (same page) is

```text
δ_{s−1} = 1 − (n−M_{s−1})[v_s(n−M_s)−d_s] / ((n−M_s−1)[v_s(n−M_{s−1})−d_s])
        = [u_s(n−M_{s−1}) − d_s] / [v_s(n−M_{s−1}) − d_s]
```

with `u_s = d_s − v_s` and `M_s = n−2`. Denominator `> 0` by the window, so
`δ_{s−1} ≥ 0` iff `u_s(n − M_{s−1}) ≥ d_s` iff (for `u_s ≥ 1`)

**`M_{s−1} ≤ n − d_s/u_s`**

— again an *upper* bound, and on `M_{s−1}` relative to `d_s`, not `d_2`. On
`s=3` this is `M_2 ≤ n − d_3/u_3`, far weaker than `M_2 > n−d_2` and in the
opposite direction. MEASURED: `δ_2 ≥ 0` holds on all 658 rows (Fable §2.2
“automatic”); Lemma 6.1 is not the missing filter. All ten Sol rows satisfy
it (`u_s(n−M_2)−d_s ∈ {8,15,16,24,55}`).

**Prop 5.5, p.186–188** is the `s=2` reduction (hence search (6) starts at
`s≥3`). Its p.187 formulae are the source of (12)/(13), not of `M_2>n−d_2`.
**Theorem p.200 (4)–(7)** (major iff `> n/(n−M_r)` roots of `g`) was already
checked to reduce to the lower half of (7) and add no cut (census-rebase §5);
`M_2>n−d_2` rearranges that count to the same window. **Prop 5.6's proof
p.189** gets `δ_1≥δ_{s−1}≥0` only inside the forbidden all-(11) case, then
contradicts it — not a search bound on `M_2`.

No display or numbered condition on pp.179–189, 194, 200–202 asserts
`M_2 > n−d_2` or `M_2 > m`.

**Typed.** `M_2 > n−d_2`: **NOT-IN-SOURCE**. Compatible with Def 5.1(2) as an
optional extra lower bound, **not derived**. Lemma 6.1 ⇒ an *upper* bound
`M_{s−1} ≤ n − d_s/u_s` (**PROVED-IN-SOURCE**, and it does not yield Sol's
inequality). `M_2 > m` is likewise **NOT-IN-SOURCE** (Fable's own typing).
MEASURED: 57 rows / 16 classes, 6/6 kept; implies `M_2>m` and MAJOR-MULT.

---

## 3. The ten rows — reconstructed factor data; no printed kill of the extras

p.202 table (image, 300 dpi; `M_4=n−1` when `d_{s+1}>1`; the `(75,50) V_2=2`
bracket `[1/3]` is the banked ERRATUM, Def 5.1(3) gives `2/3`):

```text
 n   m   M2      M3   M4   V3  V2     δ2          δ1
64  48   52      62   63    3   3    1/4         9/16
84  56   64[72]  82   83    3   2[5] 2/7[1/4]    16/21[7/12]
75  50   55      73    —    4   3[2] 1/5         1/2 [1/3]   <- ERRATUM, true [2/3]
99  66   77      97    —    8   8    1/3         4/9
```

Appendix II p.207 transformed table (Prop 6.3 on the three `u_s=1` classes;
`(99,66)` has `u_3=3` and is the p.209 dichotomy instead):

```text
 n   m   M2      V2     δ2         δ1        Jacobian
16  12   13       3     -1         1/4       X
21  14   16[18]   2[5]  -1/2[-1]   7/6[1/3]  X
15  10   11       3[2]  -1         1/2[4/3]  X^2
```

and p.209, first `(99,66)` arm: `(27,18,21; V_2=8, δ_2=−1, δ_1=0, Jacobian X^4)`.

### 3.1 Per-row reconstructed data (Def 5.1 + (9)–(13); extras have no p.202 line)

`Q = V_3 d_2/d_3`, `(10) = V_2 ≤ TRI`, `(11) = V_2 ≡ SQ (mod A_2)`,
`Lem61 = u_s(n−M_2)−d_s` (Lemma 6.1 numerator; all `≥0`).
`lo2 = d_2/(n−M_2)`; Sol's inequality is `lo2 > 1`.
Descended signature = `(n/d_s, m/d_s, M_2/d_s, V_2, J=X^{V_s−2})` when `u_s=1`.

```text
tag n,m     M           V         d2 ds n-d2 A2 TRI SQ (10)(11) (12/13) us Lem61  lo2   desc AppII
P 64,48   52,62       3,3       16  4  48   4   3  0  T F     12 / —   1   8    4/3  (16,12,13,3,X)     p.207 row 1
P 84,56   64,82       2,3       28  4  56   7   3  0  T F     12 / —   1  16    7/5  (21,14,16,2,X)     p.207 row 2
P 84,56   72,82       5,3       28  4  56   4   5  1  T T     12 / —   1   8    7/3  (21,14,18,5,X)     p.207 [18]
P 75,50   55,73       3,4       25  5  50   5   4  0  T F     —  / 13  1  15    5/4  (15,10,11,3,X^2)   p.207 row 3
P 75,50   55,73       2,4       25  5  50   5   4  0  T F     12 / —   1  15    5/4  (15,10,11,2,X^2)   p.207 [2]
P 99,66   77,97       8,8       33 11  66   3   8  0  T F     12 / —   3  55    3/2  u_s=3, no Prop 6.3  p.209 (27,18,21) or Ω
E 96,64   68,94       2,3       32  4  64  10   2  4  T F     12 / —   1  24    8/7  (24,16,17,2,X)     NONE
E 96,64   76,94       3,3       32  4  64   7   3  3  T T     —  / 13  1  16    8/5  (24,16,19,3,X)     NONE
E 96,64   72,94       2,7       32  8  64  10   2  8  T F     12 / —   1  16    4/3  (12,8,9,2,X^5)     NONE
E 100,40  88,98       3,3       20  4  80   4   3  3  T T     12 / —   1   8    5/3  (25,10,22,3,X)     NONE
```

Extras' deltas (Def 5.1(3), not printed): `(68): δ=(2/3,3/10)`; `(76):
(9/14,2/7)`; `(72): (2/3,1/10)`; `(88): (13/20,1/4)`. All `s=3`, `δ_s=−1`,
`d_{s+1}=2` so `M_4=n−1` would be 95,95,95,99 (same convention as the first
two printed rows). Selected factor at `j=2` is `π−a`, `a≠0`, except the rows
that also admit (11): printed `(84,56) V_2=5` and extras `(76)` and `(88)`.

### 3.2 Row-by-row: which printed assertion kills extras and spares the six?

Checked against every printed numerical condition on the pages read, and against
the four measured gates:

| candidate | extras | printed six |
|---|---|---|
| (1)–(13) as printed | all 4 pass | 6/6 |
| Prop 5.6 / NOT-ALL-(11) | all 4 pass (they have (10)) | 6/6 |
| Prop 5.3 window / factor `π−C_r` | all 4 pass | 6/6 |
| Def 5.1(2) windows | all 4 pass | 6/6 |
| Lemma 6.1 `δ_{s−1}≥0` | all 4 pass | 6/6 |
| Theorem p.200 (4)–(7) | automatic on (7) | 6/6 |
| `d_s≥4` (Cor. 6.1 / search (6)) | 4,4,8,4 | 6/6 |
| `u_s=1` (App II hyp. for Prop 6.3) | all 4 have `u_s=1` | **kills (99,66)** (`u_3=3`) |
| `e−d^*=1` | 3 of 4 pass; kills `(100,40)` | 6/6; leaves the three `(96,64)` |
| `A_{s−1}|(n−m)` (unlicensed) | kills 3 of 4; **spares `(100,40)`** (`4\|60`) | 6/6 |
| `SQ=0` | kills all 4 (`SQ∈{4,3,8,3}`) | **kills printed `(84,56) V_2=5`** (`SQ=1`) |
| Sol-conj / Opus-3 / `M_2>m` | **all 4 pass** | 6/6 |
| Fable `N≥6` | all 4 pass | **kills printed `(84,56) M_2=64`** |

**None of the printed assertions kills the four extras and spares the six.**

The closest unlicensed scalar, `A_{s−1}|(n−m)`, fails the fourth extra.
`e−d^*=1` fails the fourth extra and is already rejected as a filter
(census-rebase: 578 rows, weak). Forcing `SQ=0` kills a printed row.

Appendix II cannot be the kill: it *starts from* the p.202 output and treats
those four degree classes (plus the `(99,66)` dichotomy). p.207 l.4–8 names
the degrees as `(64,68)` [erratum `(64,48)`], `(84,56)`, `(75,50)`, `(99,66)`
with coefficient counts 3370, 5308, 4352, 7348. The extras are at **`(96,64)`
and `(100,40)`**, degrees Moh does not name. p.211 closes:

> All other cases can be computed directly as above. There is no counter-example
> of polynomials of degrees less than or equal to 100 for the Jacobian conjecture.

That completeness sentence is hostage to the program's output list.

### 3.3 Which reading the evidence favours — typed

Two live readings, neither fillable by analogy:

**(R1) Unprinted program rule.** The 658→6 gap is inside p.202's “computer
program”, not Appendix II. Sol's 658→10 cut is **not** that program: if it
were, p.202/p.207 would list `(96,64)` and `(100,40)` (or Prop 6.3 images
`(24,16)`, `(12,8)`, `(25,10)`). The unprinted rule is therefore strictly
stronger than Sol's conjunction, or incomparable on those two classes.

**(R2) p.202 incomplete.** Against this: 652 silent misses, and even the
last-mile four occupy two degree classes Appendix II would have had to
coefficient-count.

**Favoured: (R1); last-mile 10→6 still OPEN.** Sol's clauses emit degrees
Appendix II does not mention, so they are not Moh's code. The four extras are
the residue of the sharpest fail-closed *measured* gate.

**Typed.** (R1) DERIVED from the mismatch between Sol's ten and App II's four
degree classes; (R2) OPEN; no printed kill **PROVED-IN-SOURCE**. Bounded
quantity of the last-mile: **4 extras**. Cheapest test already run: the table
in §3.2.

---

## 4. The `(75,50, M_2=40, V_2=1)` falsifier

### 4.1 Through the four gates — MEASURED

Row (unique): `n=75, m=50, M=(−50,40,73), V=(2:1, 3:4)`,
`d=(75,25,5,1)`, `s=3`, `K=d_2=25`, `e=3`, `d^*=2`,
`δ_2=2/9`, `δ_1=13/18`, `A=(A_1=2, A_2=9)`, `q=1/3`, `u=20`,
`(10)=T` (`TRI=2, SQ=2, Q=20, V_2=1≤2`), `(11)=F`,
`(12)=F (13)=T`, `u_s=1`.

**`d_2 = gcd(75,50) = 25`, so `n − d_2 = 75 − 25 = 50`.** Sol's first clause
is `M_2 > 50`. Here `M_2=40`, so **`40 > 50` is false.**

```text
gate                         this row
SOL M2 > n-d2 = 50           KILL     (40 ≯ 50)     <-- the clause that kills it
SOL forced-(10)              KEEP
SOL conjunction              KILL     via M2 > n-d2
FABLE M2 > m=50              KILL     (40 ≯ 50)
FABLE + UNI N>=6             KILL     (already dead; N-set {6,9,12} would have passed)
OPUS INCREMENT               KEEP     (A1=2, A2=9)
OPUS NOT-ALL-(11)            KEEP
OPUS MAJOR-MULT              KILL     (V2=1)
OPUS-3                      KILL     via MAJOR-MULT
A_{s-1}|(n-m)                KILL     (A2=9 does not divide 25)
```

Window: `V_2=1 > d_2/(n−M_2)=25/35=5/7`, so (7) holds. Lemma 6.1 numerator
`1·(75−40)−5=30>0`. This is Sol's named local witness that no *bottom-only*
filter among (12)/(13), squarefree/coprime, or `A_1≥2` kills it: those all pass.

### 4.2 Bottom star — PROVED-HERE (sympy, exact)

With `p(π)=π^3+(3b/2)π`, `q(π)=π^2+b`, Moh `D(a,b,p,q)=a p q' − b q p'`:

```text
D(3,2,p,q)  = -3 b^2
Res(p,q)    = b^3 / 4
disc(p)     = -27 b^3 / 2
disc(q)     = -4 b
p odd, q even     (C2: p(-π)=-p(π), q(-π)=q(π))
```

For `b≠0`: squarefree, coprime, `D≠0`. Matches Sol's charged identities.
p.188 applied at this row: `A_1=2` does not divide `n^* V_2=3`, so `π` *is* a
factor of `g_σ` — and `p=π(π^2+3b/2)` has that factor, as (13) requires.

### 4.3 Extending through the remaining major level (Prop 5.3 at `r=2`)

`s=3`, so one step remains: `D_3 ⊃ D_2 ⊃ D_1`. Prop 5.3 at `r=2` takes a
factor `π−C_2` of `p_{D_2}(π)` of degree

```text
deg p_{D_2} = V_3 (d_2/d_3) = 4 · 25/5 = 20
```

with multiplicity `V_2=1` and window `1 > 5/7`. Branch (10) (`C_2 ≠ 0`) is the
one taken. The constructed radius is Def 5.1(3)'s `δ_1=13/18`; the jump is
`δ_1−δ_2=1/2`. Galois increment `A_2=9` consumes an orbit of size `A_2 V_2=9`;
remainder `20−9=11`. All of this is already the census row: **Prop 5.3's
numerical hypotheses hold**. The construction does not fail.

Count-wise the glue is Def 5.1(1) at `D_1`: `e V_2=3` roots of `g` and
`d^* V_2=2` of `T_1^ψ` inside the cluster selected by a simple factor of the
degree-20 `p_{D_2}`. Prop 4.6 (p.171) writes `D(nλ,(−μ_r)λ,g_σ,T_{r,σ}^ψ)=C`
at each disc separately and adds no extra printed obstruction at `r=2`.

**The `r=2` step does not fail a printed condition** (Prop 5.3, Def 5.1, (10),
(13), Lemma 6.1, Prop 5.6). A failure of the two-level *polynomial* tower is
**global**, Appendix-II-scale (4352 raw coefficients for the printed `(75,50)`
class), not a local bottom filter — Sol's charged point, confirmed. Prop 6.3
(`u_s=1`) sends this row to **`(15,10, M_2=8, V_2=1, X^2)`**, which is *not*
Moh's treated `(15,10, M_2=11, V_2=3[2], X^2)` (pp.210–211). Re-applying
`M_2>n−d_2` after descent (`8 ≯ 15−5`) is the same unlicensed clause.

**Typed.** Gate table MEASURED. Bottom identities PROVED-HERE. `r=2` numerical
glue **PROVED-IN-SOURCE to succeed** (Prop 5.3 hypotheses hold on the row).
Polynomial-tower non-existence **OPEN** (global; not a printed local filter).
Bounded: this one row; cheapest test is the gate table plus the 8-line sympy
check.

---

## 5. OPENs, cheapest tests, FALLACY-v2

* **`OPEN[MOH-PROGRAM]`** (existing). Bound **652 excess / 59 classes** at
  `n≤100`; last-mile after Sol's unlicensed conjunction **4 extras / 2 classes**.
  Cheapest test: this audit (run). Any new rule is checked on the ten before
  promotion.
* **`OPEN[PROP-5.6-SHADOW]`**. Licensing answered: NOT-ALL-(11) (469/43 at
  `n≤100`), not forced-(10)-every-`j`. Residual: the `r=2` branch datum.
* **`OPEN[M2-ABOVE-M]`** and `M_2>n−d_2`: both **NOT-IN-SOURCE**. Next test is
  a derivation from pp.152–160 (Fable H1) or a realised skeleton with
  `M_2≤m` (564 such rows; the falsifier is the unit test), not another census.
* Last-mile **4 extras**: a new candidate must kill those four, spare the six,
  and be a printed implication — already negative on the pages charged.

FALLACY-v2: no exit-price assertion (no `charge_basis`). `A_j` (radius
increment), `V_j` (selected-factor multiplicity), `Q=deg p(π)` kept distinct;
(10) orbit-size, (11) zero-factor congruence. Formal UNI `N≥6` is a knapsack
floor, never attainment. No `sat()`, no merge-free/M-descent, no pole identity.
Lemma 6.1's `δ` is Moh's logarithmic radius. Missing route-to-state ⇒ OPEN.

---

## 6. Typed block

```text
LANE          p202-ten-rows-gate-audit-grok46-20260903
SOURCE        Moh 1983 PDF 6c8847a8d8374f7d, 300 dpi, pp.179-189/193-194/196-202/207-212
PROVED-IN-SOURCE
              Prop 5.6 = all-(11) forbidden (σ1=π t^{δ1}); p.201 "can not always"
              = NOT-ALL-(11), not forced-(10); Prop 5.3 factor is π-C_r, C_r free;
              Def 5.1(2) and Lemma 6.1 give UPPER bounds on M (M2 < n-d2/V2,
              M_{s-1} <= n - d_s/u_s); Lemma 6.1 is δ_{s-1}>=0 when δ_s=-1.
DERIVED       Sol-conj => M2>m and => MAJOR-MULT on the 658 (lo2>1 => V2>=2;
              n-d2 >= m); App II degree list => Sol's ten is not Moh's output.
NOT-IN-SOURCE forced-(10) at every j (OVER-READING); M2 > n-d2; M2 > m;
              A_{s-1}|(n-m); MAJOR-MULT at j=2.
MEASURED      gates as §1; 2x2 and 2x2x2 as §1.1-1.2; Sol10 Δ Fable33 = 1+24;
              ten-row factor table §3.1; falsifier gate table §4.1;
              sympy D=-3b^2, Res=b^3/4, discs, C2.
REFUTED       forced-(10) licensed by Prop 5.6 or 5.3; M2>n-d2 from Lemma 6.1
              / Def 5.1 / Prop 5.5 / Thm p.200; a printed assertion that kills
              the four extras and spares the six.
OPEN          MOH-PROGRAM (652; last-mile 4 extras); polynomial glue of the
              (75,50,40,1) two-level tower (global, not local).
FAVOURED      unprinted program rule (R1), not a 4-row omission of p.202 (R2).
NOT CLAIMED   any D-ceiling; any realisation; that M2>m or M2>n-d2 is a theorem.
ARTIFACTS     /tmp/p202-audit/{gates.py,gates.out,ten_and_falsifier.py,pdf/};
              this report. One core, < 3 min, no ledger, no jc2-lean.
```

<!-- BODY-END -->
