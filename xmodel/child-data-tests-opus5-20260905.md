# Child characteristic data — three decision tests on the U-NEGATIVE / child-top conventions

Lane `child-data-tests-opus5-20260905`; adapter opus. Drivers
`box/child-data-20260905/`. Frozen inputs `/tmp/jc2-lane.KOq6fN/inputs`.

## 0. Verdict first

```text
TEST 1  OPEN[UNEG-SHAPE-LICENCE]   -> LICENCE PROVED, WRONG MECHANISM NAMED.
  V'_2 does NOT count branches of h'.  Moh Def 5.1(1) p.179 makes V_{i+1} a
  NORMALISED COUNT OF ROOTS OF g: "In the disc D_i the polynomials g(y) have
  precisely (n/d_{i+1}) V_{i+1} roots."  For the child that reads: g' has
  (n'/d'_2) V'_2 roots in D'_1.  Prop 6.3(2) p.197 gives g' EXACTLY n' roots
  (monic in pi, pi-degree u_s n/d_s).  A disc holds at most all the roots, so
      (n'/d'_2) V'_2 <= n'  =>  V'_2 <= d'_2 = gcd(n',m') = K'  =>  u' >= 0.
  One line, no induction, no top convention, no h'.  The frozen h-support
  theorem does NOT settle it and in fact REMOVES shape.py's mechanism.

TEST 2  OPEN[CHILD-TOP-CONVENTION] -> PROVED AT u_s=1, UNPROVED AT u_s>=2.
  Moh p.174 Definition-Remark: "The last effective characteristic pair is
  denoted by M_s in this article" (drop a terminal M_h = n-1).  Moh p.150:
  M_{h+1} = infinity, so the chain closes at the first h with d_{h+1}=1.
  Closed form, checked 1420/1420:  d'_{s'+1} = gcd(n',M'_1..M'_{s'}) = u_s,
  so the child's chain closes iff u_s = 1 (1,110 rows) and stays OPEN on all
  310 u_s>=2 rows.  Instance (96,72) M=(36,78,94) V=(4,3,5): child (16,12)
  M'=(-12,6,13), d'=(16,4,2,1), d'_4=1 -> M'_4 = infinity:  THE TOWER CLOSES
  AT 13, not at n'-2 = 14.  Moh's p.207: the five rows he descends all have
  u_s=1 and all close; the ONE he skips, (99,66), has u_s=3 and does not.

TEST 3  OPEN[UNEG-192-144-SPLIT-3/2] -> EXCLUDED, all four rows, by (L).
  (u_s,v_s)=(2,4), delta*=3/2: t = (delta-1)/(v_s-u_s*delta) = 1/2, k = W-1/2.
  Only partition of u_s=2 with >=2 blocks is [1,1]; k*lam = W-1/2 is not an
  integer so both roots are HIGH, sum nu = 2W+2 > deg q = 2W+1.  DEAD.

CONSEQUENCE (a): all 90 operative U-NEGATIVE rows are dead -- 84 at u_s=1
  (Prop 6.4 forces the descent), 2 at u_s=2 with an empty split window, and the
  4 of TEST 3.  CONSEQUENCE (b): (C-TOP) becomes LICENSED on the 1,110 u_s=1
  rows and kills 936 of them (p.174-effective count); it stays UNLICENSED on the
  310 u_s>=2 rows.  Corrected partition in Sec. 3.4.  No ledger edit here.
```

No new exit-price assertion is made, so no `charge_basis` line is licensed.

---

## 1. Frozen-input gate

Manifest built with `awk` from the `charged_input_<i>_basename=` /
`charged_input_<i>_sha256=` lines of
`xmodel/child-data-tests-opus5-20260905.run.v2` and checked with
`sha256sum -c`: **8/8 `OK`**, no digest retyped. Banked at
`box/child-data-20260905/inputs.sha256`; artifacts at `artifacts.sha256`.

Page images rendered here at 300 dpi from the charged PDF (its text layer drops
the display math on all of them): **p.150** (`pMID-11.png`), **p.174**
(`p174-35.png`), **p.179** (`p179-40.png`), **p.196/197/198**
(`pP63-57/58/59.png`). Every quotation below is read off those images.

---

## 2. TEST 1 — OPEN[UNEG-SHAPE-LICENCE]

### 2.1 What V'_2 counts, from the print

Moh 1983 **p.179, Definition 5.1(1)**, verbatim:

> (1) In the disc `D_i` the polynomials `g(y)` have precisely `(n/d_{i+1}) V_{i+1}`
> roots. `T_j^psi(y)` has precisely `(-mu_j/d_{i+1}) V_{i+1}` roots for `j=1,…,i`,

and **Definition 5.1(2)**: "`V_{i+1} d_i/d_{i+1} >= V_i > d_i/(n-M_i)` for
`i = r+1,…,s`, `V_{s+1} = d_{s+1}`". So `V_{i+1}` is a **normalised root count of `g` in `D_i`**: the fraction of
roots inside `D_i` is `V_{i+1}/d_{i+1}`, the same for `g` and every `T_j^psi`.
It is **not** a multiplicity in `h`; `h` does not occur in Def 5.1 at all.
At `i = 1` for the child, `V'_2` is fixed by

```text
#{roots of g' in D'_1}  =  (n'/d'_2) V'_2 .
```

The charged docstring (`shape.py:1-21`, "`deg_x h = u' = d_2' - V_2'`", leading
form `y^{V_2}(y-x)^{u'}`) is a *downstream* reading via Lemma 5.3's two-point
leading form, licensed by its own text only at `delta'_2 = -1` — true on **1 of
the 90** operative U-NEGATIVE rows. As the named mechanism it is **REFUTED**.

### 2.2 The derivation that does work

Moh **p.197, Prop 6.3(2)**, verbatim: "`gbar(sigma), T1bar^psi(sigma), …,
T_{s-1}bar^psi(sigma)` are monic in `pi` with `pi`-degree `u_s n/d_s`,
`u_s(-mu_1)/d_s`, …, `u_s(-mu_{s-1})/d_s` respectively", confirmed by the proof
on **p.198**: `deg gbar_sigma(pi) = u_s n/d_s`. So `g'` is monic of degree
exactly `n' = u_s n/d_s` in the child's root variable `pi`, with `n'` roots. Then

```text
(n'/d'_2) V'_2  =  #{roots of g' in D'_1}  <=  #{roots of g'}  =  n'
        =>  V'_2 <= d'_2 = gcd(n',m') = K'        =>   u' = K' - V'_2 >= 0.
```

Two remarks. (i) The same one-liner at general `i` gives `V_{i+1} <= d_{i+1}` at
**every** level with no induction and no top convention. (ii) It uses only
`d'_2 = gcd(n',m')` and the child's level-2 identification — **not** the child's
top — so it is untouched by TEST 2's negative half.

### 2.3 The concrete row (delta'_2 != -1)

`box/child-data-20260905/test12_childdata.py`, first of the 84:

```text
parent  n=108 m=72  M=(-72,-18,60,106)  V=(2:11, 3:15, 4:5)   s=4, d_s=6, u_s=1
child   (n',m') = (18,12)   K' = d'_2 = 6   V'_2 = 11   u' = -5   ell = 3
        delta'_2 != -1  (so Lemma 5.3's two-point leading form is unavailable)

Def 5.1(1) at i=1, parent :  (n/d_2) V_2   = (108/36)*11 = 33 roots of g in D_1
Def 5.1(1) at i=1, child  :  (n'/d'_2) V'_2 = (18/6)*11  = 33 roots of g' in D'_1
Prop 6.3(2)               :  g' has exactly n' = 18 roots in all.
                             33 > 18.   CONTRADICTION.
```

The count is *preserved* — `n'/d'_2 = n/d_2` identically, which is why Moh
writes the parent's `V_2` as the child's on p.207 — while the *total* drops by
`u_s/d_s`. U-NEGATIVE is exactly `(n/d_2)V_2 > n'`: the level-2 cluster is asked
to hold more branches than the whole descended curve has. Mechanically, over the
frozen enumeration (`test12-childdata.json`):

| check | result |
|---|---|
| 90 U-NEG rows: parent `D_1` count `==` child `D'_1` count | **90/90** |
| 90 U-NEG rows: child count `> n'` (Def 5.1(1) violated) | **90/90** |
| CONTROL — 1,330 non-U-NEG operative rows: Def 5.1(1) violations | **0** |
| CONTROL — Moh's five p.207 descended rows: all legal | **5/5** |

### 2.4 Does the h-support theorem or Thm 1.2 settle it? No — and it matters

The frozen source-support theorem
(`moh-hsupport-gate-astra-20260905.md:110`) is

```text
deg_x [y^a] F <= floor(d (L-a)),   d = -delta_s > 0,
G_1 = {(b,a) : 0 <= a < K, 0 <= b <= floor(d(K-a))}.
```

`floor(d(K'-a)) >= 0` for every `0 <= a < K'`, so `G_1` is **never empty** and
never negative: it cannot produce the `U-NEGATIVE` verdict and cannot supply the
licence. Worse for the old reading, `shape.py:141-147` returns
`reason="U-NEGATIVE"` when `u < 0 or degx_h < 0` with `degx_h = u*K//d2` — the
**old cap `deg_x h = u' = K'-V'_2`**, which the frozen h-support gate rejects in
terms ("the two old h caps are not justified by D1", line 3). Under the promoted
theorem the *code's* kill mechanism is void. Theorem 1.2 is ruled out by the same
report, line 13: "Nor does it state that a y-monic polynomial of degree K has
x-degree <= K-V2." The kill survives the repair **only because it rests on
Def 5.1(1), not on any property of `h'`.**

### 2.5 VERDICT (TEST 1)

**LICENCE PROVED — with the source corrected.** `u' = K' - V'_2 >= 0` holds for
every descended pair whose level-2 datum is the child's own Def 5.1 datum, by
Def 5.1(1) p.179 + Prop 6.3(2) p.197. The charged wording ("a multiplicity among
the `K'` branches of `h'`") is **not** the mechanism. The 86 kills of
scope-leaks §3.2/§3.3 become unconditional. The residual hypothesis is no longer
about `h'`: it is the single identification `V'_2 = V_2`, `d'_2 = gcd(n',m')`,
printed by Moh 5/5 on p.207 (all `u_s=1`) — retyped as
`OPEN[CHILD-LEVEL2-IDENTIFICATION]`, narrower than what it replaces.

---

## 3. TEST 2 — OPEN[CHILD-TOP-CONVENTION]

### 3.1 The child's own characteristic data, from first principles

Moh **p.150**, verbatim, for a pair `(f,g)` with `f = eta^{-m} + sum_{j>-m} f_j(x) eta^j`:

> `d_1 = n`, `d_{j+1} = g.c.d.(n, M_1, …, M_j)`,
> `M_j = min {i : f_i(x) != 0, d_j /| i}`, `M_{h+1} = infinity`.

Two consequences, neither a convention: `d_j = 1` makes `{i : d_j /| i}`
**empty**, so `M_j = min(empty) = infinity` — the chain terminates at exactly
the first `h` with `d_{h+1} = 1` and nowhere else; and `M_1 = -m`, so
`d_2 = gcd(n,m)`.

Moh **p.174, Definition–Remark**, verbatim:

> The conclusion (1) implies that if `M_h = n-1`, then we should drop it from
> our own consideration. The "effective" characteristic pairs exclude `M_h` if
> `M_h = n-1`. **The last effective characteristic pair is denoted by `M_s` in
> this article.**

So `s` is *defined* as the index of the last effective characteristic pair —
**not** by `M_s = n-2` and **not** by `delta_s = -1`, which are the Keller-pair
search conditions the census imposes on top. This is where scope-leaks §3.5 went
wrong: it declined (C-TOP) because "the child has neither `M'_{s'} = n'-2` nor
`delta'_{s'} = -1`". What the convention needs is that the child's chain closed.

### 3.2 When does the child's chain close?

`M'_i = M_i u_s/d_s` and `n' = n u_s/d_s` (Prop 6.3(2) + the banked closed
form), so

```text
d'_{s'+1} = gcd(n', M'_1, …, M'_{s'}) = (u_s/d_s) gcd(n, M_1, …, M_{s-1})
          = (u_s/d_s) d_s = u_s .
```

Checked mechanically on **1420/1420** operative rows, **0 violations**
(`test12-childdata.json:T2_closed_form`). Hence

| `u_s` | rows | `d'_{s'+1}` | child chain at level `s'+1` |
|---:|---:|---:|---|
| 1 | 1,110 | 1 | **closes** — `M'_{s'+1} = infinity` by p.150 |
| 2 | 265 | 2 | stays open |
| 3 | 34 | 3 | stays open |
| 4 | 9 | 4 | stays open |
| 5 | 2 | 5 | stays open |

At `u_s = 1` the child's effective characteristic data is exactly
`M'_1, …, M'_{s'}` — no further pair can exist — so `s'` is the last effective
index and Def 5.1(2)'s `V'_{s'+1} = d'_{s'+1} = 1` is **forced**, not assumed.

At `u_s >= 2` the chain has **not** closed: the child has at least one further
pair `M'_{s'+1} < infinity` whose value is a fact about the child's own `f'`
expansion, not determined by the parent's data. The convention could still be
rescued if that extra pair were exactly `n'-1` — `gcd(u_s, n'-1) = 1`
identically since `u_s | n'`, so one such level would close the chain and be
dropped by p.174 — but whether it *is* `n'-1` is undecided here. **Not proved.**

### 3.3 The named instance, and Moh's own table

Parent `(96,72)`, `M = (-72, 36, 78, 94)`, `V = (4,3,5)`, `s = 4`,
`d = (96, 24, 12, 6, 2)`, `d_s = 6`, `V_s = 5`, `u_s = 1`, `ell = 3`:

```text
child  n' = 16,  m' = 12,  M' = (-12, 6, 13),  s' = 3
       d'_1..d'_4 = (16, 4, 2, 1)          <- gcd(16,-12)=4, gcd(4,6)=2, gcd(2,13)=1
       d'_4 = 1  =>  M'_4 = min(empty) = infinity          [p.150]
  ==>  THE TOWER CLOSES AT 13.  It cannot continue to n'-2 = 14, and the p.174
       terminal level n'-1 = 15 does not arise.
       V'_{s'} = V_3 = 3  vs  d'_{s'} = 2   ->  (C-TOP) FAILS on this row.
       delta'_{s'} != -1 and M'_{s'} != n'-2, as required by the charge.
```

For contrast the parent's own chain does not close at `s`: `d_5 = 2 > 1`, so it
has a further pair, necessarily the terminal `M_5 = n-1 = 95` (`gcd(2,95)=1`)
that p.174 drops. That is the asymmetry §3.5 sensed but mis-attributed.

Cross-check against Moh's printed p.202 → p.207 descent
(`test12-childdata.json:T2_moh_p207_crosscheck`):

| parent `(n,m)`, `V` | `u_s` | child `(n',m')`, `M'` | child `d'` | closes | Moh p.207 |
|---|---:|---|---|---|---|
| `(64,48)` `V=(3,3)` | 1 | `(16,12)` `M'=(-12,13)` | `16,4,1` | **yes** | `(16,12); 13; 3` ✓ |
| `(84,56)` `V=(2,3)` | 1 | `(21,14)` `M'=(-14,16)` | `21,7,1` | **yes** | `(21,14); 16; 2` ✓ |
| `(84,56)` `V=(5,3)` | 1 | `(21,14)` `M'=(-14,18)` | `21,7,1` | **yes** | `(21,14); 18; 5` ✓ |
| `(75,50)` `V=(3,4)` | 1 | `(15,10)` `M'=(-10,11)` | `15,5,1` | **yes** | `(15,10); 11; 3` ✓ |
| `(75,50)` `V=(2,4)` | 1 | `(15,10)` `M'=(-10,11)` | `15,5,1` | **yes** | `(15,10); 11; 2` ✓ |
| `(99,66)` `V=(8,8)` | 3 | `(27,18)` `M'=(-18,21)` | `27,9,3` | **no** | *skipped by Moh* |

5/5 match on `(n',m')`, `M'_2`, `V'_2`. The one row Moh declines to descend is
exactly the one whose child chain does not close — a printed positive *and*
negative control for the criterion, not an analogy.

### 3.4 VERDICT (TEST 2), and the corrected partition

**PROVED at `u_s = 1` by a general argument (p.150 termination + p.174's
definition of `M_s` + the closed form `d'_{s'+1} = u_s`); UNPROVED at
`u_s >= 2`.** It is not "holds for this instance only": the instance is a
corollary of the general argument.

Consequences over the 1,420 operative rows. (C-TOP) is `V'_{s'} <= d'_{s'}`,
i.e. Def 5.1(2) at `i = s'` given the top convention, counted with the p.174
drop applied to the child's `M'` list (90 rows carry `M'_{s'} = n'-1`; disjoint
from the 90 U-NEGATIVE rows — the equal counts are a coincidence):

| class | rows | status after this lane |
|---|---:|---|
| `u_s=1`, (C-TOP) fails | **936** | **licensed kill** (incl. all 84 `u_s=1` U-NEG) |
| `u_s=1`, (C-TOP) holds | 174 | live; 46 degree pairs; by `s'` `{2:24, 3:100, 4:41, 5:9}` |
| `u_s>=2` | 310 | (C-TOP) **not licensed**; 6 U-NEG rows dead by Secs. 2 and 4 |

So scope-leaks §3.5's "1,195 of 1,420 die" splits into **936 licensed** and the
rest unlicensed; the operative residual is **174 + 310 = 484 rows**, not 225,
and the `u_s>=2` block is now the whole obstruction. No ledger entry here.

---

## 4. TEST 3 — OPEN[UNEG-192-144-SPLIT-3/2]

Driver `box/child-data-20260905/test3_split32.py`; the screen functions are
**imported** from `box/g9966n1b3-20260903/face_screen.py`, not retyped.
`(u_s, v_s) = (2,4)`, `delta* = 3/2`, the sole member of the charged radius
window `{delta in (1, v_s/u_s) : den(delta) <= u_s}`.

Certificate, identical for all four rows (`test3-split32.json`):

```text
X = u*delta - v = -1 ,  a = W*X - 1 + delta = -W + 1/2 ,  k = a/X = W - 1/2 ,
t = W - k = (delta-1)/(v - u*delta) = (1/2)/1 = 1/2 ,   Q = den(delta) = 2 ,
deg q = W*u + 1 = 2W + 1 .

partitions of u_s = 2 with >= 2 blocks:  [1,1]  (only one)
(G): {r,-r}, r != 0, is zeta_2-stable  ->  (G) does NOT kill.
(L): low branch needs k*lam = W - 1/2 in Z  ->  FAILS for lam = 1.
     So both roots are high:  nu = lam*W + 1 = W + 1 each,  sum nu = 2W + 2.
     2W + 2 > 2W + 1 = deg q.        ->  no admissible assignment.  DEAD.
Equivalently the counting bound  #high <= t*(sum low) + 1 = 1  vs  #high = 2.
```

| row | `M` | `V_2` | `d_s` | `(u_s,v_s)` | window | verdict |
|---|---|---:|---:|---|---|---|
| R1 | `(-120,-12,18,190)` | 23 | 6 | (2,4) | `{3/2}` | **DEAD by (L)** |
| R2 | `(-72,12,78,190)` | 22 | 6 | (2,4) | `{3/2}` | **DEAD by (L)** |
| R3 | `(-72,12,78,190)` | 31 | 6 | (2,4) | `{3/2}` | **DEAD by (L)** |
| R4 | `(-24,132,174,190)` | 23 | 6 | (2,4) | `{3/2}` | **DEAD by (L)** |

Controls, all pass:

* **CONTROL A (replay).** The imported screen reproduces the banked
  `face-screen.json` (G)+(L) live/dead split on all five `(99,66)` skeletons
  `S1,S2,S3,S4,S7`, every `(delta,partition)` chart: `pass = True`.
* **CONTROL C (positive).** The same call at `(u,v) = (4,7)`, `delta = 3/2`
  leaves `[2,2]` and `[2,1,1]` **alive** — the screen is not vacuously killing.
* **CONTROL W.** The banked W-sweep was run at the `(99,66)` shape only; re-run
  here for `(u,v) = (2,4)`, `W = 5…59`: the single verdict vector `['DEAD']`
  throughout. `t = (delta-1)/(v-u*delta)` and the `(L)` test contain no `W`, so
  no `W` closed form for `(192,144)` is needed.

**VERDICT: EXCLUDED.** The window is empty for all four rows, `(R)` is forced,
Prop 6.3 applies, and Sec. 2's contradiction kills them. Family (a) of the
scope-leaks report is now **CLOSED, 90/90**, with no typed residual convention
other than `OPEN[CHILD-LEVEL2-IDENTIFICATION]`.

---

## 5. FALLACY-v2 ledger

| clause | where it bit |
|---|---|
| Carrier/attainment | Moh p.208(1) is one printed *instance* of a descended leading form; §2.1 refuses it as the definition of `V'_2`. The p.207 table is a 5/5 control, never the general theorem — §3.2's general statement comes from p.150. |
| Floor/attainment | The h-support bound is a *bound*; §2.4 uses only its non-negativity and never promotes it to an equality. |
| Prime label/derivative | `M'`, `d'`, `V'`, `s'`, `delta'` are descended-datum labels, never derivatives. `p'`/`q'` in §4 ARE derivatives — the banked face identity's own notation, flagged to keep the two apart. |
| Target/arrival index | `s` (parent, last effective pair) and `s'` (child) kept distinct throughout; the p.174 drop is applied to the child's own `M'` list in §3.4 and the two 90-row sets checked disjoint. |
| Merge-free / M-descent | §3.2's negative half is the refusal to assume a merge-free child top at `u_s>=2`. |
| Variable/ring map | The child's root variable is `pi`, with `gamma = theta^{1/u_s}`, `theta = y^{-1}`, per p.198's inversion `x = (1/b)[theta^{-1}+…]`, `z = y - bx - e`: the child's roots are `z`-roots over `y`, **not** a sub-multiset of the parent's `y`-roots. `n'/d'_2 = n/d_2` is asserted as arithmetic only, never as a carry-over of individual roots. |
| positive/negative controls | CONTROL A/C/W in §4; non-U-NEG (0/1,330) and Moh-5 in §2.3; the `(99,66)` printed negative control in §3.3. |
| `sat()`, raw remainder degree | No Gröbner run in this lane; `k killed inline = 0`. |

Corrections to earlier campaign statements, stated once:

* scope-leaks §3.3 names the licence as a statement about branches of `h'`. That
  is not what Def 5.1 says and it is unavailable on 89/90 of the rows; the true
  source is Def 5.1(1)'s root count for `g'`. The conclusion is unchanged.
* scope-leaks §3.5 declines (C-TOP) because the child lacks `M'_{s'} = n'-2` and
  `delta'_{s'} = -1`. Those are not what `V_{s+1} = d_{s+1}` requires; p.174
  defines `M_s` as the last **effective** characteristic pair, and the criterion
  is `d'_{s'+1} = 1`, i.e. `u_s = 1`. (C-TOP) is licensed on 1,110 rows.
* This lane's §3.4 (C-TOP) failure count is 936, not the 970 obtained without
  the p.174 drop; both are in `test2-partition.log`.

---

## OPENS RAISED

```text
OPEN[CHILD-LEVEL2-IDENTIFICATION]
  QUANTITY: the child's own Def 5.1 level-2 datum satisfies V'_2 = V_2 and
    d'_2 = gcd(n',m'), for every descended pair, including u_s >= 2.
  STATUS: d'_2 = gcd(n',m') is p.150 arithmetic on the child's degrees and is
    not at issue.  V'_2 = V_2 is printed by Moh p.207 on 5/5 rows, ALL with
    u_s = 1, and is re-derived here from the count identity n'/d'_2 = n/d_2.
    Untested against print at u_s >= 2.
  CHEAPEST TEST: descend one u_s >= 2 row and read V'_2 off the child's own
    p.150 expansion; or find the u_s >= 2 analogue of Moh's p.207 column.
  BLAST RADIUS: replaces OPEN[UNEG-SHAPE-LICENCE], which is now discharged.
    The 84 u_s=1 U-NEGATIVE kills do not depend on it beyond what p.207 prints.

OPEN[CHILD-TOP-AT-US-GE-2]
  QUANTITY: at u_s >= 2 the child's chain has d'_{s'+1} = u_s > 1, so at least
    one further characteristic pair M'_{s'+1} < infinity exists; is it equal to
    n'-1 (whence p.174 drops it and V'_{s'+1} = d'_{s'+1} is restored), or not?
  STATUS: undecided from the parent datum.  gcd(u_s, n'-1) = 1 identically, so
    a single such level WOULD close the chain; existence is the open part.
  CHEAPEST TEST: compute M'_{s'+1} for one u_s = 2 row from the child's own
    f' expansion (p.150 recipe) rather than from the parent's transformed labels.
  BLAST RADIUS: 310 operative rows; decides whether (C-TOP) extends from 936
    to 1,161 kills and whether the residual is 484 rows or 259.

OPEN[CTOP-PROMOTION]
  QUANTITY: (C-TOP) = "V'_{s'} <= d'_{s'}" is licensed on the 1,110 u_s = 1
    operative rows and kills 936 of them, leaving 174 in 46 degree pairs.
  STATUS: derived here from Def 5.1(2) at i = s' plus the now-proved child top
    convention; NOT entered in any ledger by this lane (no ledger edits charged).
  CHEAPEST TEST: rerun_screens on the 174 survivors before any Groebner spend.
  BLAST RADIUS: cuts the s'>=3 compute obligation (scope-leaks class C) from 978
    chartable rows to the u_s=1 survivors only.
```

<!-- BODY-END -->
