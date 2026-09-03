# CENSUS-REBASE — Moh's search conditions (8)–(13) recovered verbatim from the printed page; the campaign's reconstruction of (10) is exactly right and its (10)₁ is exactly Moh's (12)/(13), but the recovered α = 0 branch (11) was missing and it costs a factor 4 in groups; and (1)–(13) AS PRINTED is provably not the whole of Moh's program

Lane CENSUS-REBASE (Opus 5), 2026-09-02. Charged inputs verified (7/7 SHA-256).
Source: `refs/moh1983_jram340_configurations_of_roots.pdf`,
sha256 `6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51`,
74 pp., rendered at 300 dpi with `pdftoppm` and read as images (pp. 150–151,
179, 188–189, 198–199, 200–202, 207 = PDF pages 11–12, 40, 49–50, 59–60,
61–63, 68). The `pdftotext` OCR in `box/depth-drivers-20260902/moh.txt` drops
every display formula in that range, which is why (8)–(13) were unrecoverable
before.

## 0. Headline

1. **(8)–(13) RECOVERED VERBATIM** (§1). `Δ_j` of the calibration lane is Moh's
   `A_j`, defined identically. The α = 0 alternative **(11) is recovered**:
   `V_{r−1} ≡ □_{r−1} (mod A_{r−1})`, where `□` is the *remainder* of Moh's
   division algorithm (9) and `△` its *quotient*.
2. **The calibration lane's reconstruction of (10) at `j ≥ 2` is EXACTLY Moh's
   printed (10)** — not a weakening, not a sharpening: `A_jV_j ≤ V_{j+1}d_j/d_{j+1}`
   ⟺ `V_j ≤ △_j`, verified on 521 190 (level, assignment) pairs with 0 exceptions
   (CONTROL 7).
3. **The calibration lane's (10)₁ is Moh's (12)/(13), and is EQUIVALENT to it**,
   not weaker as one would expect from the printed conjunction — because Moh's
   p. 188 identity `A_1 | (n*+m*)V_2 − 1` holds identically on the census
   (0 failures in 242 099 assignments, CONTROL 6). Its `Δ_1 = den(L_1δ_1)` matches
   Moh's `A_1` verbatim.
4. **Branch (11) is where the calibration over-killed.** `OPEN[MOH-11]` was real:
   94 645 of 521 190 level-pairs at `D ≤ 100` are admitted *only* by (11). On the
   true space `48 ≤ D ≤ 120` the census is **1 692 V-assignments / 1 189 groups**,
   against the calibration's 329/287 with (11) omitted — a **4.1× under-count of
   groups**. Everything downstream of the calibration's 287 must be re-read.
5. **DECISIVE NEGATIVE (§5).** (1)–(13) **as printed** admits all six of Moh's
   published rows (fail-closed control, PASSES) but leaves **658 rows in 63 `(n,m)`
   classes at `n ≤ 100`**, where Moh's p. 202 table has 6 rows in 4 classes. So
   the printed list is **not** the whole of Moh's program; the campaign may not
   treat "(1)–(13)" as "Moh's admissible space". `OPEN[MOH-PROGRAM]`, bounded
   quantity 652 excess rows.
6. **Rebased integration #17 at `D ≤ 120`** (§6): 1 189 groups; with the pinned-N
   knapsack (`N ∈ ℤ, N ≥ 6`) **670 alive**, with `N ∈ [6,16]` **589 (UNI) / 648
   mixed**. `D = 48` is emptied; `D = 66` and `D = 78` carry no (1)–(13) skeleton
   at all. **No `D > 100` empties.** `D = 105` → **3 groups**, all with `m = 70`.
7. **ERRATUM on p. 202** (PROVED-HERE, §3): the bracketed alternate of the `n = 75`
   row prints `δ_1 = 1/3`; Def 5.1(3) gives `2/3`, and `1/3` is attained by **no**
   (1)–(7)-admissible skeleton at `(75,50)` whatsoever.

Artifacts (all tracked, one core, < 4 GB, total wall 128 s):

```text
box/moh_skeleton_full.py                              d20bf0841a1ba2b2  28 761 B
box/censusrebase-drivers-20260902/run_all.py          792eb15e74932a08   5 896 B
box/censusrebase-drivers-20260902/run_all.log         15b4f80251a9d6f2  60 601 B
box/censusrebase-drivers-20260902/survivors-D48-120.txt 47f5990692..(pre-fix) 54 136 B
```

`box/moh_skeleton_N.py`, `d1floor.py`, `general.py` are **not modified**;
`moh_skeleton_full.py` re-derives the (1)–(7) core and CONTROL 0 checks it row for
row against the imported original (83 860 V-assignments, `48 ≤ n ≤ 90`, identical).

---

## 1. The printed text (PROVED-HERE = transcribed from the page image)

### 1.1 Search conditions (1)–(7), p. 200 l. 44 – p. 201 l. 13

> **p. 200, l. 44–46.** *One application of the theorem and the propositions of this
> article is to solve the Jacobian conjecture for all polynomials of degrees less
> than 100. For this purpose we consider a pair of polynomials `f` and `g` with the
> nonrestrictive assumption that `f = T_1^ψ`. We shall search for the sequences of
> integers `{n, M_1, …, M_s}` with*
>
> (1) `deg f(x,y) = m = −M_1 < deg g(x,y) = n ≤ 100`,
> (2) `m ∤ n`, `M_s = n − 2`,
> (3) `J_{x,y}(f(x,y), g(x,y)) = 1` and the degrees of `f(x,y)` and `g(x,y)` can not
>     be reduced simultaneously,
> (4) `{n, M_1, …, M_s}` is the part of characteristic data of `(f,g)` which are
>     less than `n − 2`,
> (5) `d_r = g.c.d.{n, M_1, …, M_{r−1}}`.
>
> **p. 201 l. 10–13.** *Note that it follows from Corollary 6.1 that `d_s ≥ 4`. A
> simple computation shows that `s ≤ 5`. Combining this with Proposition 5.5 we
> conclude*   (6) `3 ≤ s ≤ 5`, `d_s ≥ 4`.
>
> **p. 201 l. 15–18.** *Furthermore we assign a sequence of integers `{V_s, …, V_2}`
> for a hypothetically existing tower of major discs `D_s ⊃ ⋯ ⊃ D_1` (cf. Theorem
> and Definition 5.1) with*   (7) `V_{r+1}(d_r/d_{r+1}) ≥ V_r > d_r/(n − M_r)`.

`s ≤ 5` is a **consequence**, not an axiom: `d_2 = K > d_3 > ⋯ > d_s ≥ 4` with each
dividing the previous forces `K ≥ 4·2^{s−2}`, and `K ≤ n/3` (from `e = n/K ≥ 3`),
so `n ≤ 100 ⟹ s ≤ 5`. MEASURED: `s ≤ 5` still holds throughout `D ≤ 120`, and
**fails at `D ≤ 200`** — the first `s = 6` skeleton is `n = 192, m = 128,
M = (−96,−80,−72,−68,190)`. Any use of "s ≤ 5" above `D = 120` is unlicensed.

### 1.2 Conditions (8)–(13), p. 201 l. 20–52 — verbatim

> **(8)** *the radii `δ_s, …, δ_1` of `D_s, …, D_1` can be computed from Definition
> 5.1. We shall consider the increment of the denominator `A_{r−1}` of `δ_{r−1}`
> with respect to `δ_s, …, δ_r`. Namely let the l.c.m. of the reduced denominators
> of `δ_s, …, δ_r` be `L`. Then `A_{r−1}` is defined to be the reduced denominator
> of `Lδ_{r−1}`. Let us consider the following division algorithm equation*
>
> **(9)**   `V_r (d_{r−1}/d_r) = △_{r−1} A_{r−1} + □_{r−1}`
>
> *Let `(t̄)^{L A_{r−1}} = t`. Due to the existence of the following automorphism of
> `k⟪t̄⟫` over `k⟪t̄^{A_{r−1}}⟫`,  `t̄ → ω t̄`,  where `ω` is a `A_{r−1}`-th root of
> unity, the value of `V_{r−1}` is further restricted by*
>
> **(10)**   `V_{r−1} ≦ △_{r−1}`
>
> *if the corresponding factor of `p(π)` is of the form `π − a` with `a ≠ 0` or for
> some `j` the following*
>
> **(11)**   `V_{r−1} = j A_{r−1} + □_{r−1}`
>
> *if the corresponding factor of `p(π)` is of the form `π`. Finally, when `r = 2`
> we must have the following (cf. the proof of Proposition 5.5):*
>
> **(12)**   `A_1 | (n/d_2) V_2`,  `A_1 | (m/d_2) V_2 − 1`
>  *or*
> **(13)**   `A_1 | (m/d_2) V_2`,  `A_1 | (n/d_2) V_2 − 1`.
>
> *Furthermore we shall note that the situation indicated by the equation (11) can
> not always happen as established by Proposition 5.6.*

**Every symbol, from Moh's own text.**

| symbol | Moh's definition | page |
|---|---|---|
| `δ_i` | logarithmic radius of `D_i`, Def 5.1(3): `δ_i = 1 − (n−M_i)∏_{j>i}[V_j(n−M_j)−d_j] / ((n−M_s−1)∏_{j>i}[V_j(n−M_{j−1})−d_j])` | 179 |
| `L` (`= L_{r−1}`) | `lcm{den δ_s, …, den δ_r}`, reduced denominators | 201 (8) |
| `A_{r−1}` | reduced denominator of `L_{r−1}·δ_{r−1}` — the *increment* of the denominator | 201 (8) |
| `△_{r−1}` | **quotient** of `V_r(d_{r−1}/d_r)` by `A_{r−1}` (division algorithm (9)) | 201 (9) |
| `□_{r−1}` | **remainder** of the same division, `0 ≤ □_{r−1} < A_{r−1}` | 201 (9) |
| `p(π)` | the bottom polynomial at the general point `σ_r = Σα_jt^j + πt^{δ_r}` (Def 5.1(4)); its factor type `π − a` (`a ≠ 0`) vs `π` (`a = 0`) selects (10) vs (11) | 179, 201 |
| `n/d_2, m/d_2` | Moh's `n*, m*` of p. 188 — the campaign's `e` and `d` | 188, 201 |
| `V_{s+1}` | `= d_{s+1}` (Def 5.1(2)) | 179 |

`d_{r+1} | d_r`, so `V_r(d_{r−1}/d_r) ∈ ℤ` and (9) is an honest division algorithm.
`δ_{r−1}` depends on `V_r, …, V_s` only (Def 5.1(3) product runs over `j > r−1`), so
(9)–(11) is a well-posed **top-down** pruning rule: at the moment `V_{r−1}` is
chosen, `A_{r−1}, △_{r−1}, □_{r−1}` are already determined. `δ_s = −1` identically
(from `M_s = n−2`), so `L_{s−1} = 1`.

**Reading of (10)/(11) (the mechanism, from the automorphism sentence).** `p(π)` has
degree `Q := V_r(d_{r−1}/d_r)` and the order-`A_{r−1}` Galois automorphism permutes
its roots. If the selected factor is `(π−a)^{V_{r−1}}` with `a ≠ 0`, its whole orbit
of `A_{r−1}` distinct conjugate factors sits inside `p`, so `A_{r−1}V_{r−1} ≤ Q`,
i.e. **(10)**. If the factor is `π^{V_{r−1}}` (`a = 0`) it is fixed, the rest splits
into free orbits, so `A_{r−1} | Q − V_{r−1}`, i.e. `V_{r−1} ≡ □_{r−1} (mod A_{r−1})`
— **(11)**. In (11), `j ≥ 0` is automatic (`V_{r−1} ≥ 1 > □_{r−1} − A_{r−1}`).

**Scope.** (9)–(11) constrain `V_{r−1}` for `r = s, …, 3`, i.e. `V_j` for
`j = s−1, …, 2`. `V_s` is unconstrained by them (there is no `V_{s+1}`-level `A`).
(12)/(13) is the **separate** `r = 2` condition, applied always (both branches).
`V_1` does not exist: Def 5.1's assigned sequence is `{V_i : i = r+1, …, s+1}` with
`r = 1`, i.e. exactly `{V_2, …, V_{s+1}}`.

### 1.3 Where (12)/(13) comes from — p. 188 l. 1–13

> *The conjugations of `k((t^{1/A}))` over `k((t))` show us that if the reduced
> denominator `A` of `δ_1` is not a factor of `deg g_σ(π) = n*V_2` then `π` is a
> factor of `g_σ(π)`. Moreover if `A` is a factor of `n*V_2` then `g_σ(π) ∈ k[π^A]`
> and `π` is a factor of `(d/dπ)g_σ(π)`. In view of the two co-prime conditions
> above we must have*
>   `A | n*V_2 and A ∤ m*V_2`  *or*  `A ∤ n*V_2 and A | m*V_2`.
> *Moreover we always have from the very definition of `A` the following*
>   `A | (n* + m*)V_2 − 1`.

This last identity is what makes the printed conjunctions collapse (§2.2).

### 1.4 Proposition 5.6 (p. 188 l. 40 – p. 189)

> **Proposition 5.6.** *Suppose that `s ≥ 2` and that a tower of major discs
> `D_s ⊋ D_{s−1} ⊋ ⋯ ⊋ D_1` has been constructed. If the corresponding π-root `σ_1`,
> which is the unique one in `D_1`, is of the following form  `σ_1 = πt^{δ_1}`
> then either `k[x,y] = k[T_1^ψ, g] = k[f,g]` or there exists an automorphism
> `k[x,y] → k[x,y]` which will reduce the degrees of `f(x,y)`, `g(x,y)` and
> `T_1^ψ(f(x,y), g(x,y))` simultaneously.*

Both alternatives contradict search condition (3). `σ_1 = πt^{δ_1}` means every
`α_j` vanishes, i.e. the `a = 0` branch was taken at *every* level. Its numerical
shadow — **NOT-ALL-(11)**: at least one `j ∈ {2,…,s−1}` satisfies (10) — is
MEASURED below but **not** folded into the (1)–(13) count, because the exact
correspondence "all levels take (11)" ⟺ `σ_1 = πt^{δ_1}` also involves the `r = 2`
step, whose branch data (12)/(13) does not expose. `OPEN[PROP-5.6-SHADOW]`.

---

## 2. What this changes for the TIME-FUNCTION CALIBRATION lane

### 2.1 Its reconstructed (10) at `j ≥ 2` is *exact*

The lane wrote `Δ_j V_j ≤ V_{j+1}d_j/d_{j+1}` and typed it as a reconstruction that
"may over-kill". Since `Q = V_{j+1}d_j/d_{j+1} ∈ ℤ`,
`V_j ≤ △_j = ⌊Q/A_j⌋ ⟺ A_jV_j ≤ Q`. **CONFIRMED, exact, not a weakening.**
CONTROL 7: 521 190 (level, V-assignment) pairs over `48 ≤ D ≤ 100`, **0** mismatches.
Its `Δ_j` is Moh's `A_j` with the same `L_j = lcm{den δ_s,…,den δ_{j+1}}`.

### 2.2 Its (10)₁ is Moh's (12)/(13) — and EQUIVALENT to it, not weaker

The lane proved `a_1 = eV_2 ≡ 0 or 1 (mod Δ_1)` and typed it "= Moh (8)–(11) at
`r = 1`". **Two corrections.** (a) It is not (8)–(11) at `r=1`; it is Moh's separate
`r = 2` condition **(12)/(13)**. (b) Moh prints a *conjunction* in each branch, so
one expects (12)∨(13) to be strictly stronger than the lane's single congruence.
MEASURED (CONTROL 6, 242 099 V-assignments, `48 ≤ D ≤ 100`): **0 discrepancies in
either direction.** The reason is Moh's own p. 188 identity, which is an identity on
the census (0 failures): given `A_1 | (e+d)V_2 − 1`,
`(12) ⟺ A_1 | eV_2` and `(13) ⟺ A_1 | eV_2 − 1`, so `(12)∨(13) ⟺ (10)₁`.
So (10)₁ was **complete** at the bottom level. The lane's `Δ_1 = den(L_1δ_1)`,
`L_1 = lcm{den δ_s,…,den δ_2}` is Moh's `A_1` verbatim.

### 2.3 The real gap was (11), and it is a factor of 4

`OPEN[MOH-11]` was the whole cost. MEASURED: of 521 190 level-pairs at `D ≤ 100`,
**94 645 (18.2 %)** are admitted only by the `α = 0` branch (11).

| space, `48 ≤ D ≤ 120` | V-assignments | groups `(n,m,M_*,V_s)` |
|---|---|---|
| (1)–(7) only (campaign census today) | 902 893 | 10 637 |
| + (10) alone at `j ≥ 2` (calibration) | 3 760 | 1 012 |
| + (10)₁ (calibration's endpoint) | 329 | 287 |
| **+ (10)∨(11) and (12)/(13) — this lane** | **1 692** | **1 189** |

CONTROL (fail-closed, `run_all.log:770–773`): the calibration lane's 3 760/1 012 and
329/287 are **reproduced to the unit** by an independent re-implementation. Its
arithmetic was right; only branch (11) was missing. The correct group count is
**1 189, not 287** — a 4.14× under-count. Every filter number the calibration lane
reported below its 287 is a *floor on the kill*, i.e. an over-kill, and must be
re-read from §6 here.

---

## 3. ERRATUM on Moh p. 202 (PROVED-HERE)

Moh's p. 202 table (his complete `n ≤ 100` output; bracketed alternates split out):

```text
   n   m=−M_1   M_2       M_3   M_4    V_3   V_2      δ_2         δ_1
  64      48     52        62    63     3     3       1/4         9/16
  84      56     64 [72]   82    83     3     2 [5]   2/7 [1/4]   16/21 [7/12]
  75      50     55        73    —      4     3 [2]   1/5         1/2  [1/3]
  99      66     77        97    —      8     8       1/3         4/9
```

`M_4 = n−1` appears exactly when `d_{s+1} = gcd(d_s, n−2) > 1`, i.e. when one more
characteristic value is needed to bring the gcd to 1 (p. 151: *"`M_i ≤ n−1` for all
`i ≤ h` … all `M_i`'s terminate at `n−1`"*; p. 148: the *effective* pairs exclude
`M_h = n−1`, and `M_s` is the last effective one). It is not a search datum.

Def 5.1(3) reproduces **11 of the 12** printed `δ` entries exactly (CONTROL 1),
including both other bracketed alternates. The exception:

> `(75,50)`, `M_2 = 55`, `V_3 = 4`, `V_2 = 2`: printed `δ_1 = 1/3`; Def 5.1(3) gives
> **`δ_1 = 2/3`**.

**PROVED-HERE that `1/3` is a misprint**, not an alternative skeleton: exhaustive
search over the *entire* (1)–(7) census at `(n,m) = (75,50)` (every `M_2`, every
`V_3`, every `V_2`) produces **no** skeleton with `δ_1 = 1/3`. By hand: `δ_2 = 1/5`
forces `V_3 = 4` uniquely, and then `δ_1 = 1/3` forces `V_2 = −1/2`. The read-off
`[1/3]` is unambiguous at 600 dpi; the correct value is `[2/3]`.

The campaign's `MOH_SURVIVORS` carried `None` for both `(75,50)` rows (the OCR was
illegible); its `V` data are correct and now confirmed against the printed columns.

Separately, p. 207 l. 4 prints the degrees as **"(64, 68)"**; p. 202 gives `m = 48`
for `n = 64` and the whole skeleton is consistent with `48`. This re-confirms the
`(64,68) → (64,48)` correction already banked in `[[jc2-depth-ceiling-opus5]]`.

The p. 207 table is **not** a second survivor list: it is the Prop 6.3 image of the
p. 202 table under `(n,m,M_i) ↦ (n/d_s, m/d_s, M_i/d_s)`, valid for the three rows
with `u_s = d_s − V_s = 1`. Verified: `(64,48)/4 = (16,12)`, `M_2 = 52/4 = 13`;
`(84,56)/4 = (21,14)`, `M_2 = 64/4 = 16 [72/4 = 18]`; `(75,50)/5 = (15,10)`,
`M_2 = 55/5 = 11` — all matching p. 207 to the unit. Those rows are **outside** the
search space (`K = 4, 7, 5 < 16`) and are not skeletons. Incidentally this pins the
census convention: `V_s` **is** Moh's `v_s` (`u_3 = d_3 − v_3 = 1` for exactly the
first three rows; `(99,66)` has `d_3 = 11, V_3 = 8, u_3 = 3`, which is why Moh
excludes it there).

---

## 4. Implementation and controls

`box/moh_skeleton_full.py` (derived copy of `moh_skeleton_N.py`; the original is
untouched). Conditions (8)–(13) are implemented as an in-recursion pruning rule:

```python
def A(self, j):                      # (8)
    L = 1
    for i in range(j+1, self.s+1): L = lcm(L, self.delta[i].denominator)
    return (L*self.delta[j]).denominator

def div9(self, j):                   # (9), r = j+1
    Q = self.V[j+1]*self.d[j]//self.d[j+1]; A = self.A(j)
    return divmod(Q, A) + (A, Q)

def cond1011(self, j):               # (10) or (11)
    tri, sq, A, Q = self.div9(j)
    return (self.V[j] <= tri) or ((self.V[j]-sq) % A == 0)

def cond1213(self):                  # (12) or (13),  n* = e, m* = d
    A1 = self.A(1); ns, ms, V2 = self.e, self.dd, self.V[2]
    return ((ns*V2 % A1 == 0 and (ms*V2-1) % A1 == 0) or
            (ms*V2 % A1 == 0 and (ns*V2-1) % A1 == 0))
```

Controls (all pass; `run_all.log`, exit 0, wall 128 s, one core):

```text
CONTROL 0  re-derived (1)-(7) core == box/moh_skeleton_N.py, 83 860 V-assignments,
           48<=n<=90, byte-identical output; delta/u/windows identical.
CONTROL 1  Def 5.1(3) reproduces 11/12 printed delta entries on p.202; the 12th is
           the ERRATUM, itself checked fail-closed (1/3 attained by NO skeleton).
CONTROL 2  ALL SIX printed rows satisfy (1)-(13).  Branch used: (12) for five rows,
           (13) for (75,50) V_2=3.  Moh's p.188 identity holds on all six.
CONTROL 3  in-recursion pruning == post-filter by full_ok(), 48<=n<=75.
CONTROL 4  (1)-(13) over Moh's own n<=100 space (no GGV K>=16): every printed row
           survives  [PASS] ;  658 rows total  [MEASURED, see section 5].
CONTROL 5  Moh's "25 possible values for M_2" and "2 possible values for V_3" at
           (75,50) reproduced; V_3 pinned to 4 by (1)-(13)  [PASS].
CONTROL 6  (12)/(13) <=> (10)_1 on 242 099 V-assignments; p.188 identity, 0 failures.
CONTROL 7  printed (10) == calibration's reconstructed (10), 521 190 pairs, 0 diffs;
           branch (11) admits 94 645 of them alone.
CROSS      calibration lane's 3760/1012 and 329/287 reproduced to the unit.
```

Per-row detail of CONTROL 2 (the fail-closed gate the task specifies):

```text
row                     s  L_2  A_2  △_2  □_2  V_2  (10)  (11)  L_1  A_1  branch
(64,48)                 3    1    4    3    0    3  True False    4    4   (12)
(84,56) M2=64,V2=2      3    1    7    3    0    2  True False    7    3   (12)
(84,56) M2=72,V2=5      3    1    4    5    1    5  True  True    4    3   (12)
(75,50) V2=3            3    1    5    4    0    3  True False    5    2   (13)
(75,50) V2=2            3    1    5    4    0    2  True False    5    3   (12)
(99,66)                 3    1    3    8    0    8  True False    3    3   (12)
```

All six also satisfy NOT-ALL-(11) (§1.4). Note how hard (10) bites: at `(64,48)`
the (7) window top is `V_2 ≤ V_3d_2/d_3 = 12` and (10) cuts it to `V_2 ≤ 3`.

---

## 5. (1)–(13) as printed is NOT the whole of Moh's program — MEASURED

p. 202 l. 1–3: *"The above discussion can be easily put into a computer program. The
computer program produces only the following exceptions which satisfy the necessary
numerical restrictions."* So the p. 202 table is claimed to be the **complete**
output at `n ≤ 100`.

Run over **Moh's own space** (`n ≤ 100`, `K = gcd(n,m)` unrestricted — GGV's
`K ≥ 16` and the campaign's `D ≥ 48` are later, not his):

```text
(1)-(13) survivors at n <= 100 : 658 rows in 63 (n,m) classes   [Moh: 6 rows, 4 classes]
of which with K >= 16          : 592
largest classes: (96,64) 137, (90,60) 87, (96,72) 82, (72,48) 53, (84,56) 46,
                 (100,80) 31, (80,60) 24, (60,40) 18, (100,40) 17, (100,60) 15,
                 (80,48) 11, (64,48) 10, (96,80) 10, (75,50) 9, (99,66) 8
```

At `(75,50)` — the case Moh discusses by name — (1)–(13) pins `V_3 = 4` (his "one
possible value for `V_3`") but leaves `M_2 ∈ {5, 10, 40, 55, 60}` and 9 rows, where
he reports one `M_2` and 2 rows. Moh's "25 possible values for `M_2`" is his
*a-priori* count (multiples of `d_3 = 5` in `[M_1, n−2)`); the census's own count
after `gcd(d_2,M_2) = d_3` and `M_2 > M_1` is 20 of those 25.

**Falsification attempts on my own transcription** (each would have made the
implementation stronger; each is rejected because it kills printed rows):

| variant | `n ≤ 100` survivors | printed rows killed |
|---|---|---|
| `A_j = den(L_jδ_j)` **[printed]**, (10)∨(11) | 658 | 0 |
| `A_j = den(δ_j)` (drop the "increment") | 15 | **4 of 6** |
| printed `A_j`, (10) forced (no (11)) | 156 | 0 |
| `A_j = den(δ_j)`, (10) forced | 7 | **4 of 6** |

The two readings that come close to 6 both destroy Moh's own table, so they are
wrong. Conditions checked and found **automatic** on the census, hence not the
missing filter: `d_s ∤ M_s`; `gcd(d_{s+1}, n−1) = 1`; `λ_j < 0` and `μ_j = λ_j/d_j`
integral for all `j` (the Abhyankar–Moh quantities of p. 150); integrality of the
Def 5.1(1) root counts `(−μ_j/d_{i+1})V_{i+1}`; `s ≤ 5`. Also checked and not
separating: `u_s = 1`, `V_2 ≥ 2`, `A_1 > 1`, `δ_1 ≥ 1/2`, `e − d = 1`, `s = 3`.
Theorem p. 200 (4)–(7) (the minor-disc clauses) reduce to the *lower* half of (7)
— `V_r > d_r/(n−M_r)` — already present, so they add nothing.

> **`OPEN[MOH-PROGRAM]` (bounded quantity: 652 excess rows, 59 excess `(n,m)`
> classes, at `n ≤ 100`).** Moh's program encoded a restriction beyond the printed
> list (1)–(13) which I could not recover from pp. 148–151, 179, 188–189, 198–202.
> Until it is found, the campaign must type its admissible space as
> **"(1)–(13)", a strict superset of Moh's**, and may not cite "Moh's search space"
> for any emptiness claim. Everything in §6 is on (1)–(13) and is therefore a
> **superset** of Moh's — i.e. the kills below are *conservative*.

The natural next probes, in order of cheapness: (i) Prop 5.3's construction of
`p(π)`, pp. 181–185, for a constraint linking `V_{r−1}` to the *multiplicity
structure* rather than just the orbit size; (ii) `[A-M.1]` p. 68 and `[M.3]` for
a semigroup condition on `{M_i}` that the tree data must satisfy; (iii) the
possibility that Moh's program also enforced the *minor* branch conditions of §6
(Props 6.1–6.4) as a numerical filter.

---

## 6. The rebased integration-#17 programme, `48 ≤ D ≤ 120`

Pipeline: Moh (1)–(13) → groups `(m, M_2..M_s, V_s)` → D1-PIN
`N = Σ_B V_2(B)q(B)`, `Σ_B V_2(B) ≤ u = V_sK/d_s`, `q = (1−δ_1)de/(d+e)` →
integrality with `N ∈ ℤ`, `N ≥ 6` (integration #17 A.8's frontier floor) and
`N ∈ [6,16]`, in (UNI) form (`N = kV_2q`, `kV_2 ≤ u`) and mixed form (exact
knapsack over Fractions, no cap ever hit at `D ≤ 120`).

```text
    D          V7   grp7        V13  grp13   uni>=6  uni6-16  mix6-16
   48        1301     50          2      2        0        0        0   <- EMPTIED
   54         514     40          2      2        2        2        2
   60        3623    110         18     15       13       13       13
   63         438     30          2      2        1        1        1
   64        2417     84         10      9        7        7        7
   66         390     25          0      0        0        0        0   <- no skeleton
   72       15694    316         55     46       26       26       26
   75         682     40          9      5        3        3        3
   78         558     30          0      0        0        0        0   <- no skeleton
   80       16074    496         45     40       23       23       23
   81         764     40          2      2        1        1        1
   84       10748    207         51     38       21       21       23
   88         550     35          1      1        1        1        1
   90       30107    577         91     62       36       36       36
   96      130186   1113        229    157       86       83       90
   99        1180     50          8      7        6        4        4
  100       26873    732         67     57       32       32       32
  102         984     40          3      3        3        3        3
  104         786     42          4      3        3        3        3
  105        5037    264         15     14        7        3        3
  108       85205    824        206    125       87       71       76
  110        1890    120          3      3        1        1        1
  112       47655   1163         76     71       33       29       29
  114        1242     45          4      3        3        3        3
  117        1686     60          7      7        4        4        4
  120      516309   4104        782    515      271      219      264
  TOTAL     902893  10637       1692   1189      670      589      648
```

* (1)–(13) cuts the V-assignment space by **534×** and the group space by **8.9×**.
* **`D = 48` is emptied** (2 groups, both killed by integrality) — the calibration
  lane's `D = 48` kill **survives** the recovery of branch (11).
* **`D = 66` and `D = 78` carry no (1)–(13) skeleton at all** — emptied by (8)–(13)
  before any knapsack. Also consistent with the calibration lane.
* **No `D > 100` empties**, as expected. `D = 105` is the smallest degree above 100
  and drops from 264 groups to **3**.
* The mixed (no-(UNI)) knapsack is *weaker* than (UNI) at the group level (648 alive
  vs 589) because it can combine several branch data; it never over-kills. Killed
  under `N ∈ [6,16]`: **600 (UNI) / 541 mixed** of 1 189.
* (1)–(7) baseline reproduces integration #17 A.7 exactly (105: 264, 108: 824,
  112: 1163, 117: 60, 120: 4104; totals 902 893/10 637).

### 6.1 Moh's six published rows on the rebased pipeline

```text
row                     δ_2    δ_1     q     u   achievable N (UNI, N>=6)
(64,48)                 1/4   9/16   3/4    12   [9]
(84,56) M2=64,V2=2      2/7  16/21   2/7    21   []        <- dies at N>=6 (only 4)
(84,56) M2=72,V2=5      1/4   7/12   1/2    21   [10]
(75,50) V2=3            1/5    1/2   3/5    20   [9]
(75,50) V2=2            1/5    2/3   2/5    20   [8]
(99,66)                 1/3    4/9   2/3    24   [16]
```

All six pass (1)–(13) (as they must: Moh killed them in Appendix II, not here), and
the achievable-N sets reproduce integration #17 A.8 **to the unit**, including the
death of `(84,56) M_2=64` at `N ≥ 6`. Note `(75,50) V_2 = 2` gives `N = 8` from
`δ_1 = 2/3`, the ERRATUM value — with the printed `1/3` the row is not a skeleton at
all, so #17 A.8's `8` was already computed on the correct `δ_1`.

---

## 7. The surviving groups at `D ∈ {105,108,112,117,120}`, listed in full

Full-fidelity listing (all per-branch `V_*`, `q`, `δ_1`) in
`box/censusrebase-drivers-20260902/survivors-D48-120.txt`. Here, in full: `D = 105`,
`117`, `112` with per-branch data; `D = 108`, `120` as `m | M_2..M_s | V_s | N`
(the group key is exactly `(m, M_*, V_s)`, so this listing is complete).

### `D = 105` — 3 groups, all `m = 70`, `K = 35`, `(d,e) = (2,3)`

```text
m=70 M=[28,103] V_s=5  u=25 | V={2:1,3:5}  q=1/2   δ_1=7/12   N = 6..12
m=70 M=[28,103] V_s=6  u=30 | V={2:1,3:6}  q=9/13  δ_1=11/26  N = 9
m=70 M=[40,103] V_s=4  u=28 | V={2:1,3:4}  q=9/17  δ_1=19/34  N = 9
```

### `D = 117` — 4 groups, all `m = 78`, `K = 39`, `(d,e) = (2,3)`

```text
m=78 M=[13,115]  V_s=8   u=24 | V={2:3,3:8}   q=3/7  δ_1=9/14   N = 9
m=78 M=[52,115]  V_s=10  u=30 | V={2:1,3:10}  q=3/7  δ_1=9/14   N = 6,9,12
m=78 M=[52,115]  V_s=11  u=33 | V={2:1,3:11}  q=1/2  δ_1=7/12   N = 6..16
m=78 M=[91,115]  V_s=11  u=33 | V={2:2,3:11}  q=2/7  δ_1=16/21  N = 8
```

### `D = 112` — 29 groups

```text
m= 32 M=[8,36,110]     V_s=3  u=12 | V={2:1,3:6,4:3}  q=1     δ_1=5/14   N=6..12
m= 32 M=[8,52,110]     V_s=3  u=12 | V={2:1,3:6,4:3}  q=1     δ_1=5/14   N=6..12
m= 32 M=[8,92,110]     V_s=3  u=12 | V={2:1,3:6,4:3}  q=1     δ_1=5/14   N=6..12
m= 48 M=[72,108,110]   V_s=3  u=12 | V={2:1,3:5,4:3}  q=7/8   δ_1=7/12   N=7
m= 48 M=[84,110]       V_s=3  u=12 | V={2:1,3:3}      q=7/10  δ_1=2/3    N=7
m= 48 M=[88,110]       V_s=7  u=14 | V={2:1,3:7}      q=7/10  δ_1=2/3    N=7
m= 64 M=[-40,100,110]  V_s=3  u=12 | V={2:2,3:1,4:3}  q=2/3   δ_1=31/42  N=8
m= 64 M=[8,100,110]    V_s=3  u=12 | V={2:2,3:1,4:3}  q=2/3   δ_1=31/42  N=8
m= 64 M=[56,100,110]   V_s=3  u=12 | V={2:2,3:1,4:3}  q=2/3   δ_1=31/42  N=8
m= 64 M=[56,110]       V_s=7  u=14 | V={2:1,3:7}      q=7/4   δ_1=5/16   N=7,14
m= 80 M=[88,110]       V_s=5  u=10 | V={2:3,3:5}      q=1     δ_1=23/35  N=6,9
m= 80 M=[100,110]      V_s=3  u=12 | V={2:3,3:3}      q=5/4   δ_1=4/7    N=15
m= 84 M=[-42,105,110]  V_s=6  u=24 | V={2:1,3:9,4:6}  q=9/7   δ_1=1/4    N=9
m= 84 M=[-42,110]      V_s=11 u=22 | V={2:1,3:11}     q=6/5   δ_1=3/10   N=6,12
m= 84 M=[14,110]       V_s=13 u=26 | V={2:1,3:13}     q=4/3   δ_1=2/9    N=8,12,16
m= 84 M=[42,105,110]   V_s=6  u=24 | 4 branches (below)                  N=6..16
m= 84 M=[42,110]       V_s=9  u=18 | V={2:1,3:9}      q=6/11  δ_1=15/22  N=6
m= 84 M=[42,110]       V_s=13 u=26 | V={2:1,3:13}     q=9/8   δ_1=11/32  N=9
m= 84 M=[60,110]       V_s=3  u=21 | V={2:1,3:3}      q=12/19 δ_1=12/19  N=12
m= 84 M=[68,110]       V_s=3  u=21 | V={2:1,3:3}      q=1/2   δ_1=17/24  N=6..10
m= 84 M=[70,77,110]    V_s=5  u=20 | V={2:1,3:1,4:5}  q=3/8   δ_1=25/32  N=6
m= 84 M=[70,77,110]    V_s=6  u=24 | V={2:1,3:12,4:6} q=4/7   δ_1=2/3    N=8,12
m= 84 M=[70,91,110]    V_s=6  u=24 | V={2:1,3:12,4:6} q=4/7   δ_1=2/3    N=8,12
m= 84 M=[70,105,110]   V_s=6  u=24 | V={2:1,3:12,4:6} q=4/7   δ_1=2/3    N=8,12
m= 84 M=[70,110]       V_s=12 u=24 | V={2:1,3:12}     q=4/7   δ_1=2/3    N=8,12
m= 84 M=[70,110]       V_s=13 u=26 | V={2:1,3:13}     q=12/19 δ_1=12/19  N=12
m= 96 M=[8,36,110]     V_s=3  u=12 | V={2:1,3:6,4:3}  q=2     δ_1=8/21   N=6,8,10,12,14,16
m= 96 M=[8,52,110]     V_s=3  u=12 | V={2:1,3:6,4:3}  q=2     δ_1=8/21   N=6,8,10,12,14,16
m= 96 M=[8,92,110]     V_s=3  u=12 | V={2:1,3:6,4:3}  q=2     δ_1=8/21   N=6,8,10,12,14,16

  m=84 M=[42,105,110] V_s=6 branches:
     V={2:1,3:5,4:6}  q=3/4    δ_1=9/16      V={2:1,3:8,4:6}  q=12/13 δ_1=6/13
     V={2:1,3:11,4:6} q=1      δ_1=5/12      V={2:4,3:11,4:6} q=4/3   δ_1=2/9
```

`K = 16` for `m ∈ {32,48,64,80,96}` (`(d,e) = (2,7),(3,7),(4,7),(5,7),(6,7)`) and
`K = 28`, `(d,e) = (3,4)` for `m = 84`.

### `D = 108` — 76 groups (`m | M_2..M_s | V_s | achievable N`)

```text
72 -60,-40,106 3 8,16
72 -60,-20,106 3 8,16
72 -60,20,106 3 8,16
72 -60,40,106 3 8,16
72 -60,80,106 3 8,16
72 -60,100,106 3 6,8,9,12,15,16
72 -48,68,106 3 -
72 -48,102,106 5 10,15
72 -24,4,106 3 -
72 -24,32,106 3 -
72 -24,88,106 3 8,12
72 -24,102,106 4 8
72 -24,102,106 5 6,12
72 -24,104,106 3 12
72 -24,106 11 6..16
72 -18,30,106 5 -
72 -18,78,106 5 8
72 -18,81,106 7 6,8
72 -18,99,106 7 15
72 -18,99,106 8 6,8,10,12,14,16
72 -18,102,106 5 8,12,15,16
72 12,30,106 4 10,12
72 12,54,106 4 10
72 12,66,106 4 10,12
72 12,102,106 4 10,12
72 12,102,106 5 10,15
72 18,45,106 7 15
72 18,81,106 7 9
72 18,99,106 7 15
72 18,99,106 8 9
72 18,106 17 6,12
72 24,42,106 5 16
72 24,78,106 5 6..16
72 24,88,106 3 6
72 24,90,106 5 6,8
72 24,104,106 3 6..13
72 40,106 3 12
72 42,106 5 10,15
72 48,52,106 3 9
72 48,56,106 3 9
72 48,64,106 3 9,14,15
72 48,68,106 3 9
72 48,76,106 3 9
72 48,80,106 3 9,14
72 48,88,106 3 9
72 48,90,106 5 6,9,12
72 48,92,106 3 9,14
72 48,100,106 3 9
72 48,102,106 4 6
72 48,102,106 5 6,9,12
72 48,104,106 3 6,9
72 48,106 9 9
72 48,106 11 10,15
72 54,60,106 5 16
72 54,66,106 5 16
72 54,78,106 5 8,9,12,16
72 54,84,106 4 -
72 54,84,106 5 16
72 54,96,106 4 9
72 54,96,106 5 16
72 54,99,106 6 8
72 54,99,106 8 6,9,12
72 54,102,106 5 9,16
72 54,106 13 6
72 54,106 15 16
72 54,106 17 12
72 56,106 3 6
72 60,78,106 5 6,8,9,12,16
72 60,80,106 3 8,16
72 60,88,106 3 8
72 60,100,106 3 8,16
72 84,88,106 3 9
72 84,104,106 3 16
81 -9,106 7 10
81 36,106 8 8,16
90 78,106 5 6..15
```

### `D = 120` — 264 groups (`m | M_2..M_s | V_s | achievable N`)

```text
48 -12,100,118 3 10
48 -12,114,118 5 15
48 -12,118 11 10,15
48 12,32,118 3 7,14
48 12,44,118 3 7,14
48 12,52,118 3 7,14
48 12,76,118 3 7,14
48 12,92,118 3 7,14
48 12,112,118 3 7,14
48 42,118 5 15
48 60,78,118 4 6,8,10
48 60,102,118 5 10
48 60,104,118 3 -
48 60,114,118 4 6,8,10
48 60,114,118 5 10
48 78,118 5 10
48 80,118 5 6
48 80,118 7 10
48 104,108,118 3 6,9
72 -60,90,118 5 6,8,10,12,14,16
72 -36,90,118 5 6,8,10,12,14,16
72 -36,100,118 3 8
72 -36,102,118 5 8
72 -12,90,118 5 6,8,10,12,14,16
72 -12,100,118 3 8
72 -12,102,118 5 8
72 12,32,118 3 9,12
72 12,44,118 3 9,10
72 12,52,118 3 9,12
72 12,76,118 3 9,10,12
72 12,90,118 5 6,8,10,12,14,16
72 12,92,118 3 9,12
72 12,112,118 3 6,9,12
72 36,90,118 5 6,8,10,12,14,16
72 36,100,118 3 8
72 36,102,118 5 8
72 36,116,118 3 6,8,10,12,14,16
72 60,90,118 5 6,8,10,12,14,16
72 84,90,118 5 6,8,10,12,14,16
72 84,100,118 3 -
72 90,118 5 6,8,10,12,14,16
80 -60,-50,-25,118 4 16
80 -60,-50,-5,118 4 16
80 -60,-50,5,118 4 -
80 -60,-50,25,118 4 16
80 -60,-50,75,118 4 16
80 -60,-50,85,118 4 16
80 -60,-50,105,118 4 -
80 -60,-30,-5,118 4 -
80 -60,-30,5,118 4 -
80 -60,-30,105,118 4 -
80 -60,-10,-5,118 4 -
80 -60,-10,5,118 4 -
80 -60,-10,25,118 3 6,9
80 -60,-10,105,118 4 -
80 -60,-5,118 4 -
80 -60,5,118 4 -
80 -60,10,105,118 4 -
80 -60,30,105,118 4 -
80 -60,50,55,118 4 -
80 -60,50,65,118 4 -
80 -60,50,75,118 4 16
80 -60,50,85,118 4 -
80 -60,50,95,118 4 -
80 -60,50,105,118 4 16
80 -60,50,115,118 4 -
80 -60,50,118 8 -
80 -60,70,75,118 4 16
80 -60,70,85,118 4 16
80 -60,70,95,118 4 16
80 -60,70,105,118 4 16
80 -60,70,115,118 4 6..16
80 -60,70,118 8 16
80 -60,70,118 9 16
80 -60,85,118 4 8
80 -60,90,105,118 4 -
80 -60,90,118 7 6,9,12,15
80 -60,105,118 4 16
80 -60,108,118 3 6,9,12,15
80 -50,-25,118 4 13,16
80 -50,-5,118 4 13,16
80 -50,25,118 4 13,16
80 -50,75,118 4 13,16
80 -50,85,118 4 13,16
80 -48,-28,118 3 8,12,16
80 -48,12,118 3 8,12,16
80 -48,52,118 3 8,12,16
80 -48,92,118 3 8,12,16
80 -20,10,75,118 3 -
80 -20,12,118 3 -
80 -20,30,115,118 3 6
80 -20,30,115,118 4 6,9,12,15
80 -20,30,118 9 -
80 -20,50,75,118 4 16
80 -20,50,105,118 4 16
80 -20,50,118 7 10
80 -20,70,75,118 4 8,16
80 -20,70,85,118 4 16
80 -20,70,95,118 4 16
80 -20,70,105,118 4 16
80 -20,70,115,118 4 6..16
80 -20,70,118 8 16
80 -20,70,118 9 16
80 -20,76,118 3 -
80 -20,84,118 3 16
80 -20,85,118 4 8
80 -20,90,115,118 3 6
80 -20,90,115,118 4 6,8,10,12
80 -20,92,118 3 8
80 -20,108,118 3 8,9,12,16
80 -20,110,115,118 3 6,8
80 -20,110,115,118 4 8,12,15,16
80 -20,110,118 9 6,8,10,12,14,16
80 -20,115,118 4 8,16
80 -10,45,118 3 -
80 -8,68,118 3 -
80 10,75,118 3 -
80 10,115,118 4 8,12,16
80 16,44,118 3 16
80 16,60,118 3 16
80 16,100,118 3 16
80 16,118 7 8,10,12,15,16
80 20,50,75,118 4 8,16
80 20,50,105,118 4 16
80 20,50,115,118 4 6,12,15
80 20,50,118 7 6..14
80 20,70,75,118 4 16
80 20,70,85,118 4 16
80 20,70,95,118 4 16
80 20,70,105,118 4 16
80 20,70,115,118 4 6..16
80 20,70,118 8 16
80 20,70,118 9 16
80 20,85,118 4 8
80 20,90,115,118 4 9
80 20,110,115,118 4 6,12,15
80 20,110,118 7 6,10,12
80 20,110,118 9 9
80 32,84,118 3 -
80 32,116,118 3 6..15
80 48,118 5 6
80 50,75,118 4 16
80 50,105,118 4 16
80 60,70,75,118 4 16
80 60,70,85,118 3 -
80 60,70,85,118 4 8,12,16
80 60,70,95,118 3 -
80 60,70,95,118 4 16
80 60,70,105,118 4 16
80 60,70,115,118 4 6..16
80 60,70,118 8 16
80 60,70,118 9 16
80 60,84,118 3 6
80 60,85,118 3 -
80 60,85,118 4 8,9,12,16
80 60,90,95,118 3 -
80 60,90,118 9 6,9,12,15
80 60,95,118 3 -
80 60,104,118 3 6
80 60,108,118 3 6,9
80 60,110,115,118 3 -
80 60,110,115,118 4 9
80 60,110,118 6 -
80 60,110,118 7 9
80 60,110,118 9 6,8,9,12,15,16
80 60,112,118 3 9
80 60,115,118 4 9
80 60,116,118 3 6,9
80 64,118 7 6,9,11,12,15
80 70,75,118 4 6,16
80 70,85,118 4 6,16
80 70,95,118 4 6,16
80 70,105,118 4 6,16
80 70,115,118 4 6..16
80 70,118 8 6,16
80 70,118 9 6,9,16
80 72,92,118 3 -
80 72,100,118 3 -
80 85,118 4 8
80 88,108,118 3 9
80 88,118 7 6,8,10,12,14,16
80 96,108,118 3 10,15
80 96,118 7 6
80 100,105,118 4 6,9,12,15
80 100,108,118 3 9,10,15
80 100,110,115,118 4 6,9,10,12,15
80 100,110,118 8 6,9,12,15
80 100,115,118 4 6,9,12,15
80 100,118 16 6,9,12,15
80 100,118 17 9
90 -80,-45,118 3 8
90 -80,5,118 3 8
90 -80,25,118 3 8
90 -80,95,118 3 8
90 -45,-10,118 3 -
90 -45,25,118 3 -
90 -45,95,118 3 -
90 -45,115,118 4 6,12
90 -15,65,118 3 -
90 -15,85,118 3 -
90 -10,25,118 3 8
90 -10,95,118 3 8
90 -10,115,118 4 10
90 10,118 7 16
90 18,118 5 8,16
90 40,75,118 4 16
90 40,85,118 4 16
90 42,118 5 6..16
90 45,85,118 4 6,8,10,12,14,16
90 45,100,118 3 -
90 45,110,118 4 6,9,12,15
90 45,115,118 4 6,12
90 50,118 7 6,8,10,12,14
90 66,118 5 8,16
90 70,75,118 4 8
90 70,85,118 4 8
90 70,95,118 4 8
90 70,105,118 4 8
90 70,115,118 4 6,7,8,9,10,11,12,14
90 70,118 7 8
90 70,118 8 8
90 70,118 9 8,16
90 75,85,118 4 6..12
90 75,110,118 4 6,9
90 75,115,118 4 6
90 78,118 5 8
90 100,105,118 3 7
90 108,118 5 7,14
96 -84,-30,118 4 10
96 -84,6,118 4 10
96 -84,78,118 4 10
96 -40,-12,118 3 10
96 -40,28,118 3 10
96 -40,44,118 3 10
96 -40,100,118 3 10
96 12,112,118 3 6..16
96 16,118 7 10,15
96 32,52,118 3 16
96 32,84,118 3 16
96 32,92,118 3 16
96 36,66,118 4 10
96 36,102,118 4 10
96 60,78,118 4 10
96 60,114,118 4 10
96 60,114,118 5 15
96 64,118 7 10,15
96 78,118 5 15
96 80,116,118 3 10
96 80,118 7 15
96 88,118 7 10
100 -50,-25,118 4 6,8,10,12,14,16
100 -50,-5,118 4 6,8,10,12,14,16
100 -50,25,118 4 6,8,10,12,14,16
100 -50,75,118 4 6,8,10,12,14,16
100 -50,85,118 4 6,8,10,12,14,16
100 -30,55,118 4 -
100 -10,25,118 3 6
100 -10,45,118 3 6
100 -10,95,118 3 6
100 50,75,118 4 10
100 50,118 7 10,15
100 84,118 3 12
100 90,118 9 12
100 92,118 3 6,9
```

`D = 120`: `m ∈ {48,72,80,90,96,100}` with `K = 24,24,40,30,24,20` and
`(d,e) = (2,5),(3,5),(4,6)… ` — the `(d,e)` and `u` columns are in the artifact file.

---

## 8. Extension to `D ≤ 200` (count, and — since it was cheap — the knapsack too)

Counts on the (1)–(13) space, `121 ≤ D ≤ 200` (wall 4.5 s):

```text
125:4/4      126:150/106  128:170/129  130:6/6      132:98/70    135:94/58
140:221/190  144:2287/1216 147:23/21   150:445/337  152:6/5      153:8/7
154:3/3      156:117/77   160:1255/882 162:359/216  165:46/36    168:1470/1001
170:3/3      171:10/10    174:7/6      175:35/30    176:160/135  180:4687/2559
182:6/6      184:4/4      186:6/5      189:202/113  190:10/10    192:7276/3589
195:35/32    196:190/166  198:350/204  200:2285/1591       (V-assignments/groups)

TOTAL 121<=D<=200 : 22 028 V-assignments, 12 827 groups
TOTAL  48<=D<=200 : 23 720 V-assignments, 14 016 groups
```

Knapsack over the same range (wall 26 s, one capped group at `D = 192` counted as
ALIVE, so the kill is a floor):

```text
121<=D<=200 : groups 12 827 ; (UNI) alive N>=6  8 161 (killed 4 666)
                              (UNI) alive [6,16] 6 210 (killed 6 617)
                              mixed alive [6,16] 6 651 (killed 6 176, capped 1)
              degrees emptied: NONE
```

No degree in `[121,200]` empties, under either form. The group count grows roughly
like the number of divisor chains, i.e. it is driven by highly composite `D`
(`192: 3 589`, `180: 2 559`, `200: 1 591`, `168: 1 001`) — consistent with
`[[jc2-n-vs-mapdeg-opus5]]`'s NO-CEILING: nothing in (1)–(13) plus integrality
bounds `D`.

MEASURED variant (§1.4), reported and **not** used: adding NOT-ALL-(11) —
at least one level `j ∈ {2,…,s−1}` satisfying (10) — gives 1 305 V-assignments /
**969 groups** at `48 ≤ D ≤ 120` (from 1 692/1 189) and 17 666/**11 415** at
`121 ≤ D ≤ 200` (from 22 028/12 827). All six of Moh's rows survive it. It is a
19 %/11 % cut and it does **not** empty any further degree.

---

## 9. Reading

The recovery is a **net loosening** of the campaign's current picture, not a
tightening, and that is the important thing:

* The calibration lane's arithmetic was right at every step that could be checked
  (its 3 760/1 012 and 329/287 reproduce to the unit), and its two named objects —
  the reconstructed (10) and the proved (10)₁ — are, respectively, *exactly* Moh's
  printed (10) and *equivalent* to Moh's printed (12)/(13). Both promotions stand.
* But `OPEN[MOH-11]` was load-bearing: with the `α = 0` branch restored the group
  count at `D ≤ 120` is **1 189, not 287**. Any downstream statement that consumed
  "287 groups / 233 knapsack-alive" as the size of the admissible space is off by
  4.1× and must be re-based on §6.
* The three degree kills (`48`, `66`, `78`) **survive** the restoration, which is
  the reassuring half.
* `D = 105` is genuinely thin — 3 groups, one `(m, K, d, e) = (70, 35, 2, 3)`, two
  distinct `M_2 ∈ {28,40}` — so the D1-SUBTREE/time-function flagship's choice of
  `D = 105` as the smallest surviving degree above 100 is confirmed on the true
  space, with the *same* 3 groups the calibration lane reported.
* The negative result of §5 is the one that changes how the campaign may speak. The
  census is now on "(1)–(13)", a space Moh's own program is a strict subset of by a
  factor of ~100 at `n ≤ 100`. Nothing here licenses "Moh's search excludes X".

## 10. OPENs raised (each with its bounded quantity)

* **`OPEN[MOH-PROGRAM]`** — the restriction beyond printed (1)–(13) that Moh's
  program encoded. Bounded quantity: **652 excess rows / 59 excess `(n,m)` classes
  at `n ≤ 100`**; specifically at `(75,50)` it must cut `M_2 ∈ {5,10,40,60}` and
  the rows `(55,73)/V_2∈{2,3}` must survive. Probes listed at the end of §5.
* **`OPEN[PROP-5.6-SHADOW]`** — is NOT-ALL-(11) the exact numerical content of
  Prop 5.6? Bounded quantity: **220 groups at `D ≤ 120`** (1 189 → 969) and
  **1 412 at `121 ≤ D ≤ 200`**. Needs the `r = 2` step's branch datum, which
  (12)/(13) does not expose.
* **`OPEN[P202-ERRATUM-SCOPE]`** — the p. 202 `δ_1 = 1/3` misprint is settled; but
  it means the printed table has at least one typo, so the *other* printed columns
  are only as reliable as Def 5.1(3) confirms them. Bounded quantity: 1 of 12 `δ`
  entries; all 6 `V` and 9 `M` entries are confirmed by CONTROL 2 passing.

## 11. FALLACY-v2 check

* **Flag/place/series.** `A_j` (place: the *radius* `δ_j` and its denominator
  increment) is kept distinct from `V_j` (multiplicity at level `j`) and from
  `deg p(π) = Q` (series). (10) is an inequality on the *orbit* of a root of `p`,
  (11) a congruence on the *complement* of a fixed root; they are not the same
  charge and are never summed.
* **Carrier/attainment.** `N ≥ 6` and `N ≤ 16` are consumed as a *window*, not as
  attainment; a group survives if *some* branch multiset realises an integer in the
  window. Capped knapsack states are counted ALIVE, so every kill number is a floor.
* **Floor/attainment.** §5's 658 is an exact count on (1)–(13), and it is stated as
  a **superset** of Moh's space, never as Moh's space.
* **Target/arrival index.** Moh's `A_{r−1}` is indexed by the *lower* level `r−1`
  but built from `δ_s,…,δ_r` at the *upper* levels; the implementation takes the
  index from the printed subscript, and CONTROL 2 pins it against six printed rows
  with `A_2 ∈ {3,4,5,7}` and `A_1 ∈ {2,3,4}` — indices that would not match if the
  offset were wrong.
* **Prime label/derivative.** `△`/`□` are Moh's own quotient/remainder glyphs from
  the division algorithm (9), not labels; both are used with that meaning only.
* No exit claim is made in this lane, so no `charge_basis` line is due.

## 12. Typed block

```text
LANE          CENSUS-REBASE (Opus 5), 2026-09-02
SOURCE        Moh 1983, JRAM 340, pp.148-151/179/188-189/198-202/207, read at
              300-600 dpi from 6c8847a8d8374f7d (74 pp.)
PROVED-HERE   (8)-(13) transcription (sec.1.2); the symbol dictionary (sec.1.2);
              p.202 ERRATUM delta_1[75,50,V2=2] = 2/3 not 1/3, with an exhaustive
              non-attainment proof; printed (10) == calibration's reconstruction;
              (12)v(13) <=> (10)_1 given Moh's p.188 identity.
CONFIRMED     calibration lane's Delta_j = Moh's A_j; its reconstructed (10);
              its (10)_1; its 3760/1012 and 329/287 counts; its D=48/66/78 kills;
              integration #17 A.7 baseline (902893/10637) and A.8 survivor N-sets.
CORRECTED     (10)_1 is Moh's (12)/(13) at r=2, NOT (8)-(11) at r=1, and it is
              EQUIVALENT to the printed pair, not weaker.
NEW           branch (11) recovered: V_{r-1} = jA_{r-1} + square_{r-1}.  Its
              omission cost 4.14x in groups (287 -> 1189 at D<=120).
MEASURED      D<=120 on (1)-(13): 1692 V-assignments, 1189 groups; knapsack
              N in Z, N>=6: 670 alive; N in [6,16]: 589 (UNI) / 648 mixed;
              emptied: D=48 (knapsack), D=66,78 (no skeleton); NO D>100 empties;
              D=105 -> 3 groups.  D<=200: 23720 assignments / 14016 groups,
              6651 mixed-alive in [6,16], no degree emptied.  s<=5 fails at
              D<=200 (first s=6 at D=192).
REFUTED       "(1)-(13) as printed = Moh's admissible space": it leaves 658 rows
              at n<=100 against his 6.  Also refuted: A_j = den(delta_j) (kills
              4 of his 6 rows).
NOT CLAIMED   any recovery of Moh's missing restriction; any emptiness of a degree
              above 100; that NOT-ALL-(11) is licensed.
OPEN          MOH-PROGRAM (652 excess rows); PROP-5.6-SHADOW (220 groups at
              D<=120); P202-ERRATUM-SCOPE (1 of 12 printed delta entries).
ARTIFACTS     box/moh_skeleton_full.py; box/censusrebase-drivers-20260902/
              {run_all.py, run_all.log, survivors-D48-120.txt, compact-108.txt,
              compact-120.txt}.  One core, < 4 GB, 128 s + 26 s.
```

<!-- BODY-END -->
