# M2-DESCENT — Opus 5 — 2026-09-03

Lane `m2-descent-opus5-20260903`. Flagship seat. Charged inputs verified by SHA-256
against the launch manifest (7/7 match, `/tmp/jc2-lane.ObaLc7/inputs`). Moh 1983 read
from `refs/moh1983_jram340_configurations_of_roots.pdf`
(sha256 `6c8847a8…`, matches), rendered at 300 dpi with `pdftoppm`, pages read as
images: **148–151, 179, 196–199, 207–212**. Every Moh citation below is typed
`SOURCE-READ` (page opened by this lane at 300 dpi) or `SOURCE-UNVERIFIED`.

Discipline: no canonical ledger edited; `jc2-lean` not inspected; no other
`ideation-20260903T1015Z-*` file than the charged Fable one opened; no running lane's
report opened. Drivers in `box/m2descent-drivers-20260903/`.

## 0. Headline

1. **`OPEN[M2-ABOVE-M]` — REFUTED as stated.** `M_2 > m` is **not** a theorem for
   Keller pairs in Moh's gauge. Twelve explicit witnesses (polynomial automorphisms of
   `A^2_Q`, put in Moh's gauge, Jacobian verified a nonzero constant) have `M_2 <= m`;
   the smallest is printed in full in §2.3 (`n = 4, m = 2, M_2 = 1`). Four of them
   satisfy Moh's condition (6) datum `d_s >= 4` as well. Consequently routes **H1**
   (Ω-symmetry + Lemma 2.1) and **H2** (Prop 5.6 coprimality) **cannot work as posed**:
   both use only hypotheses the witnesses satisfy. `PROVED-HERE / UNREVIEWED`.
2. **Source evidence that `M_2 > m` is not Moh's hidden restriction.** p.151
   (`SOURCE-READ`), immediately after Lemma 2.1: *"We shall call the reader's attention
   to our **ignorance about the numbers M_i**… the value `M_2` could never be 13. It
   shows how little we know about `M_i` in the polynomial case."* Moh explicitly
   disclaims a general constraint on `M_2`. §2.1.
3. **The Fable measurement reproduces exactly** (fail-closed): 6/6 printed p.202 rows
   kept, 658 → 94 rows / 32 classes at `n <= 100`, `(75,50)` pinned to
   `M_2 ∈ {55,60}` and to Moh's two rows after integral `N >= 6`, 1189 → 179 groups at
   `48 <= D <= 120` → 63 alive (`N>=6`), 59 in `[6,16]`, `D = 105` with 0 alive. §1.
4. **`OPEN[DESCENT-POLYGON]` — closed on the degrees, open on the radii.**
   `PROVED-HERE`: `deg_π P = deg_z ḡ = deg_x g = u_s n/d_s`; `P` monic in `π` forces the
   `z^B`-coefficient of `ḡ` to be `± y^{n v_s/d_s}`, whose consistency is exactly Moh's
   p.207 identity `u_s = d_s − v_s`; hence `g`'s leading form is
   `y^{n v_s/d_s}·(z‑part)^{n u_s/d_s}` and `deg_γ P = u' n'/d'`. Confirmed twice against
   the source (p.208, p.211). Moh's coefficient counts 244/373/202 are **exactly**
   `C(n'+2,2)+C(m'+2,2)`: the descended pair has total degree = π-degree. The
   `δ_2', δ_1'` columns of p.207 are **not** reproduced — typed residue, §3.4.
5. **`OPEN[DESCENT-CLOSURE]` — partly closed.** `M_2 > m`, the windows (7), and the
   gcd conditions (2),(3),(5) descend verbatim (all are homogeneous of weight 1 in
   `{M_i, d_i}` and `V_i' = V_i`). Condition (6) does **not** descend (`s' = s−1`, and
   Moh's own descended rows have `s' = 2`); (4) `M_s = n−2` does not descend. §3.5.
6. **Appendix II control PASSES — and turns up an erratum.** The `(15,10; X^2)` case
   (Moh pp.210–211) is re-run mechanically: his `α` is reproduced, his `γ` is **not** —
   the printed `−a_9^2 a_{10} B` must be `−a_9^2 a_8 B`. With the audited `γ`, his
   Case 2 (`a_9 ≠ 0 ⇒ a_{10}=0, deg_y γ = 0`) does not close; the kill instead comes one
   step later and is **decisive**: the five equations `c_2 − 3γ ∈ k` saturate to the
   unit ideal at `a_9 ≠ 0`. **SATURATED-EMPTY.** Moh's conclusion stands; his printed
   route to it does not. §4.2, `ERRATUM[APPII-GAMMA-B]`.
7. **The two descended D = 105 problems are written explicitly** (§4.3): G2 →
   `(15,10)`, `J = c x^4`, `M_2' = 4`, `V_2' = 1`, `d_2' = 5`; G3 → `(21,14)`,
   `J = c x^2`, `M_2' = 8`, `V_2' = 1`, `d_2' = 7`; G1 (`u_s = 2`) → conditionally
   `(30,20)`, `J = c x^2`. **Typed `COUNTING-BOUND only`**, not solved: the Appendix-II
   reduction from 202 coefficients to 22 [15 or 13] runs through the descended `δ_1'`
   (p.210: *"The datum `δ_1 = 1/2` implies that the polynomials `h` and `β` must be of
   the following form"*), which is exactly the §3.4 residue. The shape-free normal form
   stands at 172 unknowns — outside the desk budget, so the lane emits it and stops, as
   instructed.

## 1. Reproduction of the measurement (fail-closed)

Driver `box/m2descent-drivers-20260903/repro_m2_filter.py`, `repro_degrees.py`; both
import the tracked, unmodified `box/moh_skeleton_full.py`.

```text
CONTROL P (fail-closed gate): the six printed p.202 rows all have M_2 > m
   (64,48) M_2=52 | (84,56) M_2=64, 72 | (75,50) M_2=55 (twice) | (99,66) M_2=77
   printed kept: 6/6 ; Abhyankar-Moh semigroup: 6/6 ; u_s = 1 on five of the six

(1)-(13) baseline            rows= 658  classes= 63
+ Abhyankar-Moh semigroup    rows= 658  classes= 63   (AUTOMATIC: True)
+ M_2 > m                    rows=  94  classes= 32
+ all M_i > m (i>=2)         rows=  94  classes= 32   (same set)

(75,50): 9 rows -> 4 with M_2>m, M_2 in {55,60};
         M_2=60 rows have no integral N -> exactly Moh's two rows survive.
M_2>m AND integral pinned N>=6 (UNI): 33 rows / 17 classes, 5/6 printed,
         28 residual rows (24 with u_s = 1).
```

Degree sweep `48 <= D <= 120` on the `(1)-(13)` space: **1189 groups → 179 under
`M_2 > m` → 63 alive at integral `N >= 6` → 59 in `[6,16]`**; twelve degrees empty
(48, 54, 63, 88, 102, 104, 110, 114 outright; 60, 72, 81, 105 lose all `N`-alive
groups); `D = 105` keeps 5 of 14 groups under the filter but **none** of the three
`N`-alive groups (the trio has `M_2 ∈ {28,40} < 70`); `D = 108` keeps 5 groups,
2 in `[6,16]`. Every number in Fable §2.2–§2.3 is reproduced to the unit.

`MEASURED`. This lane changes none of it; what follows is about whether the filter is
a *theorem*.

## 2. Task (1) — `M_2 > m`: REFUTED as a theorem for Keller pairs in Moh's gauge

### 2.1 What the source says about `M_2` (SOURCE-READ, p.150–151)

p.150 fixes the object: `g = η^{-n}`, `η = g^{-1/n} = y^{-1}+α_2(x)y^{-2}+… ∈ k[x]((η))`,
`f = η^{-m} + Σ_{j>−m} f_j(x) η^j`; `Ω_i(x)=x, Ω_i(η)=ω^i η`; equation (1)
`Π_{i=1}^n (f − Ω_i f) = 0` is the analytic factorisation of the defining equation at
`g = ∞`. *"Due to the existence of the automorphisms `Ω_i`, the tree data … are
completely symmetric. Hence the tree data along any root will determine the tree data
completely."* Then `d_1 = n`, `d_{j+1} = gcd(n, M_1,…,M_j)`,
`M_j = min{ i : f_i(x) ≠ 0, d_j ∤ i }`, `M_{h+1} = ∞`, and the auxiliary
`n_j = d_j/d_{j+1}`, `q_1 = M_1`, `q_j = M_j − M_{j−1}`, `λ_j = Σ_{i≤j} q_i d_i`,
`μ_j = λ_j/d_j`, `θ_j = μ_j − M_j`.

Lemma 2.1 (p.151): `J_{x,y}(f,g) = c ≠ 0` **iff**
`ord_η(Σ f_i(x)η^i − Σ f_i(0)η^i) = n−1` **and** `deg_x f_{n−1}(x) = 1`; equivalently
`f_i'(x) = 0 ∀ i < n−1` and `f_{n−1}'(x)` a nonzero constant.

Immediately after, and this is the decisive citation for this lane:

> *"Note that since `f_{n−1}(x) ≠ 0` and `(n, n−1) = 1`, then `M_i ≤ n−1` for all
> `i ≤ h`. … **We shall call the reader's attention to our ignorance about the numbers
> `M_i`.** For instance, after long computation we (as verified by A. Sathaye)
> established that for the following polynomials over `k`, `X = T^6+… = θ^{-6}`,
> `Y = T^8+… = θ^{-8}+…+θ^{M_2}+…`, the value `M_2` could never be 13. **It shows how
> little we know about `M_i` in the polynomial case.**"* — Moh, p.151, `SOURCE-READ`.

Two things follow. (i) The only constraint on `M_i` Moh states in §2 is the *upper*
bound `M_i ≤ n−1`; there is no lower bound `M_2 > m` anywhere on the pages read
(148–151, 179, 196–199, 207–212). (ii) Moh's own illustration is a *one-variable*
pair with no Jacobian condition at all, and the constraint he reports there
(`M_2 ≠ 13` for `(n,m) = (6,8)`) is of the wrong shape to be `M_2 > m` (`13 > 8`).
The hypothesis that `M_2 > m` is Moh's hidden restriction is **not supported** by the
source. `SOURCE-READ`.

### 2.2 The refutation

**Design.** `M_2 > m` as posed in the charge is a statement about *Keller pairs in
Moh's gauge*: `f, g ∈ k[x,y]` monic in `y`, `deg f = deg_y f = m`,
`deg g = deg_y g = n`, `J(f,g) ∈ k^*`. That class is non-empty and completely
computable: it contains every polynomial automorphism of `A^2` after a generic linear
precomposition. So the predicate can be *tested*, not merely searched for.

**Engine** (`box/m2descent-drivers-20260903/etaexp.py`, stdlib only, exact
`Fraction` arithmetic, coefficients in `Q[x]`): from `g` monic in `y` build
`η = g^{-1/n}` as a Laurent series in `u = y^{-1}` (rational-exponent unit power by the
`N e_N = α Σ j g_j e_{N−j} − Σ k e_k g_{N−k}` recursion), then peel
`f = η^{-m} + Σ_{j>−m} f_j(x)η^j` greedily and read off `{M_j, d_j}` by Moh's p.150
definition. Smoke test: `g = y^2+x`, `f = y` returns
`f = η^{-1} − (x/2)η + …`, `M = [−1]`, `d = [2,1]`.

**Population** (`autoscan.py`, `autoscan2.py`): automorphisms built as compositions
`(F,G) ↦ (G, F + p(G))` of elementary maps over `Q`, then precomposed with a random
`GL_2` element and scaled monic. **Fail-closed**: a pair enters the table only after
`J(f,g)` is verified to be a single nonzero constant monomial and
`deg = deg_y` is verified for both members.

```text
  build              n    m  M_1..M_s                 d_1..                M_2>m   s   d_s
  [2, 2]             4    2 [-2, 1]                   [4, 2, 1]            False   2     2
  [3, 2]             6    3 [-3, 2]                   [6, 3, 1]            False   2     3
  [4, 2]             8    4 [-4, 3]                   [8, 4, 1]            False   2     4
  [2, 2, 2]          8    4 [-4, 2, 5]                [8, 4, 2, 1]         False   3     2
  [5, 2]            10    5 [-5, 4]                   [10, 5, 1]           False   2     5
  [3, 2, 2]         12    6 [-6, 3, 8]                [12, 6, 3, 1]        False   3     3
  [2, 3, 2]         12    6 [-6, 4, 9]                [12, 6, 2, 1]        False   3     2
  [6, 2]            12    6 [-6, 5]                   [12, 6, 1]           False   2     6
  [2, 2, 2, 2]      16    8 [-8, 4, 10, 13]           [16, 8, 4, 2, 1]     False   4     2
  [4, 2, 2]         16    8 [-8, 4, 11]               [16, 8, 4, 1]        False   3     4
  [2, 4, 2]         16    8 [-8, 6, 13]               [16, 8, 2, 1]        False   3     2
  [3, 3, 2]         18    9 [-9, 6, 14]               [18, 9, 3, 1]        False   3     3
   ( the twelve M_2 <= m witnesses; the scan also produced 13 pairs with M_2 > m --
     [2,3],[2,4],[3,3],[2,5],[2,6],[3,4],[4,3],[2,2,3],[3,5],[5,3],[2,2,4],[4,4],[3,2,3] )

  total pairs 25 ; M_2 > m : 13 ; M_2 <= m : 12
  witnesses with M_2 <= m and d_s >= 4 : (8,4), (10,5), (12,6), (16,8) with d_s = 4,5,6,4
```

**Statement (PROVED-HERE / UNREVIEWED).** *There exist pairs `f, g ∈ Q[x,y]`, monic in
`y`, with `deg f = deg_y f = m`, `deg g = deg_y g = n`, `1 < m < n`, `n ∤ m`,
`J_{x,y}(f,g) ∈ Q^*`, whose Moh characteristic data satisfy `M_2 ≤ m`.* Twelve are
listed above; one is printed in full below. In particular the predicate `M_2 > m` is
**not** a consequence of the Jacobian condition together with Moh's gauge, and it is
not a consequence of the Jacobian condition together with `d_s ≥ 4`.

### 2.3 A witness, printed in full (checkable by hand)

```text
n = deg g = deg_y g = 4 ,  m = deg f = deg_y f = 2 ,  K = gcd(n,m) = 2
g = y^4 - 3xy^3 + 27/8 x^2y^2 - 27/16 x^3y + 81/256 x^4
      + 2y^3 - 35/8 xy^2 + 51/16 x^2y - 99/128 x^3
      + 9/8 y^2 - 25/16 xy + 139/256 x^2 + 9/64 y - 25/256 x + 1/256
f = y^2 - 3/2 xy + 9/16 x^2 + y - 11/16 x
J(f,g) = 1/1024                      (a nonzero constant: FAIL-CLOSED check)
deg g = deg_y g = 4 ;  deg f = deg_y f = 2 ;  both monic in y
eta-expansion  f = eta^{-2} + sum_j f_j(x) eta^j ,  eta = g^{-1/4} :
   f_{-2} = 1     f_0 = -1/16    f_1 = -1/128    f_2 = 1/256
   f_3 = -3/4096 + x/4096                         <- deg_x f_{n-1} = deg_x f_3 = 1 (Lemma 2.1)
characteristic data  M = [-2, 1] ,  d = [4, 2, 1]
M_2 = 1  <=  m = 2      ->   "M_2 > m" is FALSE on a genuine Keller pair.
```

Every hypothesis of Moh §2 holds: `f_i(x)` is constant for `i < n−1 = 3` and
`deg_x f_3 = 1` (Lemma 2.1, both clauses); `M_i ≤ n−1` (p.151 note); `y ∈ k(x,f,g)`
(the pair is an automorphism). `PROVED-HERE / UNREVIEWED`.

### 2.4 What this kills, and what it does not

* **H1 (Ω-symmetry + Lemma 2.1, Moh §2–§3) is dead as posed.** Ω-symmetry of the tree
  data, constancy of `f_i` below `n−1`, linearity of `f_{n−1}`, and `M_i ≤ n−1` all hold
  verbatim for the witnesses, so any argument using only those ingredients proves a
  false statement. The precise obstruction (`PROVED-HERE`): `M_2 = ord_η(f − Ω_i f)` for
  any `i` with `gcd(n,i) = n/K` — a *contact order between conjugate branches*, since
  `f − Ω_i f = Σ_j f_j(1−ω^{ij})η^j` has order `min{ j : f_j ≠ 0, (n/gcd(n,i)) ∤ j } = M_r`
  with `r = max{ r : (n/d_r) | i }`. Ω-symmetry fixes the *multiplicities*
  (`#{i : r(i)=r} = d_r − d_{r+1}`, so `ord_η Π_{i<n}(f−Ω_i f) = Σ_r (d_r−d_{r+1})M_r`)
  but bounds no single `M_r` from below; and that "different" identity carries no
  information under the Jacobian condition, since `F(x,f,g) ≡ 0` gives
  `F_T·[f,g] = −F_x·g_y` while Lemma 2.1 gives `F_x(x,f,g) = −aη^{n−1}F_T(f,g)`, so it
  collapses to the automatic `g_y = (c/a)η^{-(n−1)}`.
* **H2 (Prop 5.6 coprimality, p.189) is dead as posed** for the same reason: `g` and
  `T_1^ψ` are coprime for the witnesses too, so an order inequality derived from
  coprimality alone cannot yield `M_2 > m`.
* **H3 (the elementary `h = f^e − c g^d` route) gives the wrong inequality.** With
  `n = Ke, m = Kd`, `[h,g] = e f^{e−1}[f,g]` gives `deg h ≥ K(de−d−e)+2` (the bound in
  the charge). In the `η`-gauge, `deg_y h = (e−1)m − j_0` where
  `j_0 = min{ j > −m : f_j ≠ 0 }`, so the Jacobian bound reads `j_0 ≤ n−2` — a
  *restatement of* `M_s ≤ n−2`, not a lower bound on `M_2`. The matching **upper**
  bound on `deg h` does not exist: weighted-degree (Newton-polygon) inequalities all
  run `w(J) ≤ w(P)+w(Q)−w(x)−w(y)`, i.e. they bound degrees from **below**. `PROVED-HERE`
  (the direction of every available inequality is the wrong one).
* **NOT refuted:** that `M_2 > m` holds for skeletons satisfying the *full* `(1)–(13)`
  together with the minimal-counterexample hypotheses. The witnesses all fail (6)
  (`3 ≤ s ≤ 5` and/or `d_s ≥ 4`) or (4) (`M_s = n−2`); indeed the census and the
  witnesses are disjoint by construction. So `OPEN[M2-ABOVE-M]` survives in the
  narrowed form below — but it is now a *conditional* statement whose proof must
  consume `(1)–(13)`, i.e. it can no longer be hoped for from the soft §2 theory.

### 2.5 Candidate skeletons with `M_2 ≤ m` that no known necessary condition kills

`(1)–(13)` rows at `n ≤ 100` with `M_2 ≤ m`: **564 rows / 54 classes**; with an
integral pinned `N ≥ 6` (UNI, `uni_hits`, `N_min = 6` read from the frontier line and
not re-derived): **293 rows / 33 classes**, of which **243 have `u_s = 1`** and hence
descend by Prop 6.3. The six smallest:

```text
n=45 m=30 M=[-30,10,43] V={2:1,3:4} u_s=1 q=2/3 N=[6,8]    | n=48 m=36 M=[-36,18,46] V={2:1,3:5} u_s=1 N=[6..10]
n=54 m=36 M=[-36,24,52] V={2:1,3:5} u_s=1 q=1/2 N=[6,7]    | n=54 m=36 M=[-36,27,52] V={2:3,3:7} u_s=2 N=[9]
n=56 m=42 M=[-42,21,54] V={2:1,3:5} u_s=2 q=3/4 N=[6]      | n=60 m=40 M=[-40,-10,58] V={2:2,3:7} u_s=3 N=[8]
-- and at D = 105 the trio itself (all three have M_2 <= m):
m=70 M=[-70,40,103] V={2:1,3:4} M_2=40 u_s=1 N=[9] | M=[-70,28,103] V={2:1,3:5} M_2=28 u_s=2 N=[6..12]
                                                   | M=[-70,28,103] V={2:1,3:6} M_2=28 u_s=1 N=[9]
```

These satisfy `(1)–(13)`, the Abhyankar–Moh semigroup conditions (automatic, Fable
§2.4 reproduced here), the integrality/`N`-pin, and — being (1)–(13)-admissible — every
necessary condition the campaign owns. `n = 45, m = 30, M = [−30,10,43]` is the
smallest; it is the cheapest target for a direct realisability attack if one wants to
attack `M_2 ≤ m` head-on. `MEASURED`.

### 2.6 Consequence for `OPEN[MOH-PROGRAM]`

The 658 → 94 cut may **not** be applied as a theorem. Fable's downstream numbers
(`D = 105` empty, twelve degrees empty, `D_min ≥ 108`, the 28-row residue) are
therefore **conditional on an unproved and now source-unsupported hypothesis**, and
the campaign's frontier statement must not consume them. `OPEN[MOH-PROGRAM]` stays at
its banked bound (652 excess rows at `n ≤ 100`); this lane neither sharpens nor
loosens it.

## 3. Task (2) — `OPEN[DESCENT-POLYGON]`

### 3.1 The descent, as printed (SOURCE-READ, pp.196–198)

Prop 6.3 (p.197). Hypotheses: `g` monic in `y`, `deg g = deg_y g = n > 1`, `δ_s = −1`,
and the logarithmic radius of the minor disc satisfies `δ*_{s−1} ≥ v_s/u_s`. With
`z` defined by equation (10), `y^{-1} = θ`, and `g, T_1^ψ,…,T_{s−1}^ψ` regarded as
`ḡ(z), T̄_i^ψ(z) ∈ k⟪θ⟫[z]`, there is a π-root
`σ = Σ a_j θ^j + π θ^{v_s/u_s}` such that with `γ = θ^{1/u_s}`:

1. `ḡ(σ), T̄_1^ψ(σ),…,T̄_{s−1}^ψ(σ) ∈ k[γ,π]`;
2. they are monic in `π` of π-degrees `u_s n/d_s, u_s(−μ_1)/d_s, …, u_s(−μ_{s−1})/d_s`;
3. `J_{γ,π}(ḡ(σ), T_1^{−ψ}(σ)) = −(u_s/b) γ^{v_s−u_s−1}`.

The proof (p.198) fixes the substitution explicitly: `z = y − bx − e`,
`x = (1/b)[θ^{-1} + Σ_{i=1}^{<v_s/u_s} c_iθ^i + …]`, and
`σ = (c_0−e) + Σ_{i=0}^{<v_s/u_s} c_iθ^i + πθ^{v_s/u_s}`, with
`ḡ(σ) = ḡ_σ(π) + (terms of higher degree in θ and lower degree in π)`,
`deg ḡ_σ(π) = u_s n/d_s`. Prop 6.4 (p.198): if in addition `u_s = 1` then
`δ*_{s−1} ≥ v_s/u_s = v_s` **automatically**, so Prop 6.3 applies unconditionally.
Appendix II p.207 states the identity used throughout: **`u_3 = d_3 − v_3 = 1`** for
the first three classes. Note `μ_1 = M_1 = −m`, so the second π-degree is `u_s m/d_s`.

(There is a sign slip inside the p.198 proof: its last display reads
`−u_s/(bγ^{v_s−u_s−1})`, i.e. the reciprocal of the statement (3). The p.207 table
(`X, X, X^2` against `v_s−u_s−1 = 1,1,2`) shows the statement is what is meant.
`ERRATUM[PROP63-JAC-SIGN]`, minor, `SOURCE-READ`.)

### 3.2 The γ-degree — PROVED-HERE

Let `u_s`, `v_s`, `d_s`, `b`, `e` be as above; write `q(γ) := (c_0−e) + Σ_{i≥1} c_iγ^{i u_s}`
(`deg_γ q < v_s` since `i u_s < v_s`), so that `σ = q(γ) + π γ^{v_s}` is a **polynomial**
in `k[γ,π]`, and `y = θ^{-1} = γ^{-u_s}`. Put `ḡ(y,z) = Σ_{a,b} c_{ab} y^a z^b`,
`B := deg_z ḡ`, `P(γ,π) := ḡ(γ^{-u_s}, σ)`.

**(P1) `deg_π P = B = deg_x g`.** `P = Σ_{a,b} c_{ab} γ^{−a u_s} σ^b`; the coefficient of
`π^B` is `γ^{B v_s}·Σ_a c_{aB} γ^{−a u_s}`, a nonzero Laurent polynomial (distinct `a`
give distinct γ-exponents), so `deg_π P = B`. And `z = y − bx − e` is linear with `x`
appearing to degree 1, so `deg_z ḡ = deg_x g`. Combining with Prop 6.3(2):
**`deg_x g = u_s n/d_s`.** ∎

**(P2) The `z`-leading coefficient of `ḡ` is `y^{n v_s/d_s}`, and `u_s + v_s = d_s`.**
`P` monic in `π` forces `γ^{B v_s}Σ_a c_{aB}γ^{−a u_s} = 1`, so exactly one `a`
survives, `a = B v_s/u_s`, with `c_{aB} = 1`. With `B = u_s n/d_s` this is
`a = n v_s/d_s`. Since `deg ḡ = deg g = n` (linear change of coordinates) and the
monomial `y^a z^B` occurs, `a + B = n(v_s+u_s)/d_s ≤ n`, i.e. `u_s + v_s ≤ d_s`;
Moh's p.207 identity `u_s = d_s − v_s` is the equality case, so `y^{n v_s/d_s} z^{u_s n/d_s}`
is a **top-degree** monomial and the leading form of `g` is
`c·y^{n v_s/d_s}·(z\text{-part})^{u_s n/d_s}` with `z = y − bx` at top order. ∎

**Two independent source confirmations.**
*(i)* Moh p.208 (`SOURCE-READ`), the descended `(16,12)` pair:
`h(x,y) = y^3(y−x) + b_1y^3 + b_2y^2 + b_3y + b_4`, `ḡ = h^4 + α_1h^3+α_2h^2+α_3h+α_4`,
`deg_y α_i ≤ 3`. So the leading form of `ḡ` is `y^{12}(y−x)^4`. Apply (P2) to the
descended pair: `n' = 16`, `d_2' = gcd(16,12) = 4`, `V_2' = 3` (p.207 table), so
`u' = d_2' − v' = 1` and the predicted leading form is
`y^{16·3/4}(y−x)^{16·1/4} = y^{12}(y−x)^4`. **Exact match.** And (P1) predicts
`deg_x ḡ = u'n'/d' = 4`, which is what `h` of `deg_x h = 1` raised to the 4th power
gives. **Exact match.**
*(ii)* Moh p.211 (`SOURCE-READ`), the descended `(15,10)` pair with `V_2 = 3`:
`h = (y^2 − x^2 + a_1y + a_2x + a_3)y^3 + (a_4x+a_5)y^2 + (a_6x+a_7)y + a_8`, so
`h_top = y^3(y^2−x^2)`, `deg_x h = 2`, and `g_top = h_top^3 = y^9(y−x)^3(y+x)^3`.
(P2) predicts `y^{15·3/5}·(deg-6 part) = y^9·(…)^6` ✓, and (P1) predicts
`deg_x g = 2·15/5 = 6 = 3·deg_x h` ✓. (Here the `z`-part splits into two linear
factors — the `V_2 = 3` subdisc split, "three subdiscs which contains 2, 2, 6 of roots",
p.210 — so (P2) must be read as a statement about the `z^B`-coefficient in a
`z`-adapted frame, which is exactly how it was proved.)

### 3.3 The Newton polygon of the descended pair

Moh's own coefficient counts settle the total degree, and they check to the unit three
times over. p.207: *"the numbers of coefficients of the pairs of polynomials involved
are 3370, 5308, 4352 and 7348"* for `(64,48), (84,56), (75,50), (99,66)`; and after
the descent, *"reduced to 244, 373 and 202 respectively"*.

```text
   C(n+2,2)+C(m+2,2) :  (64,48) 2145+1225 = 3370  ✓   (84,56) 3655+1653 = 5308  ✓
                        (75,50) 2926+1326 = 4352  ✓   (99,66) 5050+2278 = 7348  ✓
   descended         :  (16,12)  153+ 91  =  244  ✓   (21,14)  253+ 120 =  373  ✓
                        (15,10)  136+ 66  =  202  ✓
```

So Moh counts the descended pair as a **general pair of total degrees `(n', m') =
(u_s n/d_s, u_s m/d_s)`**. Combined with (P1)–(P2):

> **`OPEN[DESCENT-POLYGON]`, degree part (answer).** The Newton polygon of `P = ḡ(σ)`
> in `(γ, π)` is contained in the triangle `{(a,b) : a + b ≤ n', b ≤ n'}` with
> `n' = u_s n/d_s`; its `π`-leading coefficient is `1` (γ-degree `0`); and
> `deg_γ P = u' n'/d_2'` where `(d_2', V_2' = V_2, u' = d_2' − V_2)` is the descended
> pair's own top-level datum. Same statement for `Q = T̄_1^ψ(σ)` with `m' = u_s m/d_s`.
> Numerically: `(16,12)` → `deg_γ P = 4`, `deg_γ Q = 3`; `(21,14)` → `15, 10` for
> `V_2 = 2` and `6, 4` for `V_2 = 5`; `(15,10)` → `6, 4` for `V_2 = 3` and `9, 6` for
> `V_2 = 2`. The full descended π-degree tower is `(u_s n/d_s, u_s(−μ_j)/d_s)_{j<s}`,
> e.g. `(15, 10, 9)` for Moh's `(75,50)` row.
> `PROVED-HERE` for (P1),(P2); `SOURCE-READ` (coefficient counts) for the total degree.

### 3.4 Residue: the `δ_2', δ_1'` columns are NOT reproduced

The p.207 transformed table (`SOURCE-READ`) is

```text
    n   m=-M_1   M_2      V_2      delta_2      delta_1     Jacobian
   16     12      13       3          -1          1/4          X
   21     14    16 [18]  2 [5]   -1/2 [-1]    7/6 [1/3]        X
   15     10      11     3 [2]        -1        1/2 [4/3]      X^2
```

This lane reproduces `n, m, M_2, V_2, Jacobian` on **all four `u_s = 1` rows exactly**
(gate `G1`, `descent_table.py`):

```text
  row                      u_s   v_s   d_s |   n'   m'   M_2'  V_2' Jac
  (64,48)                    1     3     4 |   16   12     13     3 X^1
  (84,56) M2=64,V2=2         1     3     4 |   21   14     16     2 X^1
  (84,56) M2=72,V2=5         1     3     4 |   21   14     18     5 X^1
  (75,50) V2=3               1     4     5 |   15   10     11     3 X^2
  (75,50) V2=2               1     4     5 |   15   10     11     2 X^2
  (99,66)                    3     8    11 |   27   18      7     8 X^4   (u_s>1: Prop 6.3 N/A)
  p.207 (n, m, M_2, Jacobian) columns reproduced on all four u_s=1 rows: True
```

so the transformation rule is `n' = n/d_s`, `m' = m/d_s`, `M_i' = M_i/d_s`,
`d_i' = d_i/d_s`, `V_i' = V_i` (the last is `SOURCE-INFERRED` from the three-fold
`V_2` match, not stated in Prop 6.3).

The two `δ` columns are **not** reproduced by any natural candidate: Def 5.1(3) on the
descended data with `s' = 2` gives `−1/2, −1/4, −1/2, −1/3` where the table prints
`−1, −1/2, −1, −1` (ratios `2,2,2,3`, no single rule); the shift `δ_i' = δ_{i+1}` works
on `(64,48)` and fails on `(84,56)`; the parameter-change law `δ_new = v_s − u_sδ_old`
(derived here from `π = (z−q(γ))γ^{−v_s}`, `t_new = y^{1/u_s}`) gives `11/4, 39/16` on
`(64,48)` against the printed `−1, 1/4`; and Def 5.1(3) with an assumed third descended
exponent `M_3'` has no integer solution for `V_3'`. Rows with identical originals but
different `V_2` give different `δ_1'` (`(75,50)`: `1/2` vs `4/3`), so `δ'` does depend
on `V_2`.

**Typed residue of `OPEN[DESCENT-POLYGON]`: 2 columns × 5 rows = 10 rational numbers.**
Note that a printed `δ_1` column of the *undescended* p.202 table is already a proved
erratum (`box/moh_skeleton_full.py` `control_1`: `(75,50) V_2=2` prints `1/3` where
Def 5.1(3) gives `2/3` and `1/3` is attained by no `(1)–(7)` skeleton at `(75,50)`), so
"misprint" is a live hypothesis for some of the ten, but this lane does not claim it.
This residue is what blocks task (3) (see §4.3).

### 3.5 `OPEN[DESCENT-CLOSURE]` — partial answer (PROVED-HERE)

With `M_i' = M_i/d_s`, `d_i' = d_i/d_s`, `V_i' = V_i`, `n' = n/d_s`, `m' = m/d_s`
(all for `u_s = 1`):

| Moh condition | descends? | why |
|---|---|---|
| (2),(3),(5) — gcd / definition of `d_j` | **YES** | `gcd` is homogeneous of weight 1: `d_{j+1}/d_s = gcd(n/d_s, M_1/d_s,…)` |
| (7) windows `V_{i+1}d_i/d_{i+1} ≥ V_i > d_i/(n−M_i)` | **YES** | `d_i/d_{i+1}` invariant, `d_i/(n−M_i)` invariant, `V_i' = V_i` |
| **`M_2 > m`** | **YES, both directions** | `M_2 > m ⟺ M_2/d_s > m/d_s`. The predicate is *exactly* preserved. |
| (4) `M_s = n−2` | **NO** | Moh's own first descended row has `M_2' = 13`, `n'−2 = 14` |
| (6) `3 ≤ s ≤ 5`, `d_s ≥ 4` | **`d_s ≥ 4` yes, `s ≥ 3` NO** | `s' = s−1`; all of Moh's descended rows have `s' = 2` (`d_2' = 4,7,5 ≥ 4`) |
| (8)–(13) (`A_j` increments) | **OPEN** | they are functions of `δ_j`, and `δ'` is the §3.4 residue |

The `M_2 > m` line is the sharpest: it says the descent **cannot** be used to prove
`M_2 > m` by induction (the predicate is invariant, not improved), and conversely that
the two D = 105 problems inherit `M_2' ≤ m'` verbatim (`4 ≤ 10`, `8 ≤ 14`) — see §4.3.
`PROVED-HERE / UNREVIEWED`.

## 4. Task (3) — the two descended D = 105 problems

### 4.1 The descended data (gate-checked)

`box/m2descent-drivers-20260903/descent_table.py`, same code path as the p.207 gate:

```text
  M=[-70, 40, 103] V={2:1,3:4} : u_s=1 v_s=4 d_s=5 -> (n',m')=(21,14) M_2'=8 V_2'=1 Jac=X^2  N=[9]
       pi-degree tower {g:21, T1:14, T2:20}   d_2'=7  d_3'=1   M_2'>m'? False      [G3]
  M=[-70, 28, 103] V={2:1,3:5} : u_s=2 v_s=5 d_s=7 -> (n',m')=(30,20) M_2'=4 V_2'=1 Jac=X^2  N=[6..12]
       pi-degree tower {g:30, T1:20, T2:32}   d_2'=5  d_3'=1   M_2'>m'? False      [G1, conditional]
  M=[-70, 28, 103] V={2:1,3:6} : u_s=1 v_s=6 d_s=7 -> (n',m')=(15,10) M_2'=4 V_2'=1 Jac=X^4  N=[9]
       pi-degree tower {g:15, T1:10, T2:16}   d_2'=5  d_3'=1   M_2'>m'? False      [G2]
```

G2 and G3 have `u_s = 1`, so Prop 6.4 supplies `δ*_{s−1} ≥ v_s` and Prop 6.3 applies
unconditionally. G1 has `u_s = 2`: Prop 6.3 needs `δ*_2 ≥ v_s/u_s = 5/2`, which is
**not** automatic; if it holds, G1 descends to a `(30,20)` pair with Jacobian `X^2`,
otherwise Moh's p.209 minor-disc dichotomy is required (`OPEN[MINOR-DICHOTOMY]`,
untouched by this lane).

### 4.2 CONTROL — Moh's `(15,10; M_2 = 11, V_2 = 3; X^2)` reproduced, with an erratum

Driver `moh_1510_control2.py` (sympy 1.12, one core, < 20 s, < 200 MB). Inputs taken
verbatim from pp.210–211 (`SOURCE-READ`):

```text
(5)  h = (y^2 - x^2 + a1 y + a2 x + a3) y^3 + (a4 x + a5) y^2 + (a6 x + a7) y + a8
       = A y + a8 = B y^2 + (a6 x + a7) y + a8
(6)  beta = a9 A + a10 y + a11 x + a12
(2)  beta^2 = alpha h + gamma ,      deg_y gamma < deg_y h = 5
(3)  beta^3 = (3 gamma + a) h^2 + eps h + delta ,   deg_y eps, delta < 5
(4)  (1/2) eps = b f^{4/10} + c(x^3 + d*) y + a powerseries in y^{-1} ,  b != 0, c != 0
(7)  deg_y gamma <= 2                [from deg_y beta^3 <= 12, deg_y h^2 = 10]
```

Results:

```text
   deg_y h = 5 , deg h = 5 , h monic in y : True ;  deg_y beta = 4
   beta^2 - alpha*h - gamma == 0 : True
   printed alpha = a9^2 B + 2 a9 a10 reproduced : True
   printed gamma (coefficient of B = -a9^2*a10) : reproduced = False
   audited gamma (coefficient of B = -a9^2*a8 ) : reproduced = True
```

**`ERRATUM[APPII-GAMMA-B]` (PROVED-HERE).** Moh p.211 prints
`γ = [(a_9^2a_6+2a_9a_{11})x + (a_9^2a_7+2a_9a_{12})]A − a_9^2a_{10}B + (a_{10}y+a_{11}x+a_{12})^2 − 2a_8a_9a_{10}`.
The `B`-coefficient is `−a_9^2 a_8`, not `−a_9^2 a_{10}`. Direct derivation:
`h = Ay + a_8 = By^2 + (a_6x+a_7)y + a_8` gives `A^2 ≡ (a_6x+a_7)A − a_8 B (mod h)` and
`Ay ≡ −a_8 (mod h)`, whence
`β^2 ≡ [(a_9^2a_6+2a_9a_{11})x+(a_9^2a_7+2a_9a_{12})]A − a_9^2a_8 B + (a_{10}y+a_{11}x+a_{12})^2 − 2a_8a_9a_{10}`.
Moh's `α = a_9^2B + 2a_9a_{10}` is correct.

Consequence for his equations. `deg_y A = 4`, `deg_y B = 3`, so `deg_y γ ≤ 2` forces the
`A`-bracket to vanish identically in `x` and the `B`-coefficient to vanish:

```text
    a9*(2*a11 + a6*a9) = 0        <- Moh's 1st, reproduced
    a9*(2*a12 + a7*a9) = 0        <- Moh's 2nd, reproduced
    a9*(2*a1*a12 + a1*a7*a9 - a8*a9) = 0   ==>  a8*a9^2 = 0
    a1*a9*(2*a11 + a6*a9) = 0     (redundant)
```

so the third equation is **`a_8a_9^2 = 0`**, where Moh prints `a_9^2a_{10} = 0`.

*Case 1 (`a_9 = 0`)* — unchanged and reproduced: `α = 0`, `β = a_{10}y+a_{11}x+a_{12}`,
`γ = β^2`, `deg_y β^3 ≤ 3 < 5`, so in (3) both `3γ+a = 0` and `ε = 0`; but (4) with
`b ≠ 0` forces `deg_y ε = 4`. Contradiction.

*Case 2 (`a_9 ≠ 0`)* — **Moh's printed reasoning does not close.** The audited
equations give `a_8 = 0` (not `a_{10} = 0`), `a_6 = −2a_{11}/a_9`, `a_7 = −2a_{12}/a_9`,
whence `γ = (a_{10}y + a_{11}x + a_{12})^2`, of `y`-degree **2** when `a_{10} ≠ 0` —
exactly the degree (3) requires. Moh's stated contradiction ("`γ = (a_{11}x+a_{12})^2`
must be of `y`-degree 2. A contradiction.") is unavailable.

*Case 2, closed one step later (PROVED-HERE).* Take the `h`-adic expansion
`β^3 = c_2h^2 + c_1h + c_0` (`deg_y c_1,c_0 < 5`). Equation (3) says `c_2 − 3γ = a ∈ k`.
Computing `c_2` under the audited Case-2 substitution and subtracting `3γ` leaves five
non-constant monomials, each of which must vanish:

```text
      x^2 y^0 :  -3*a11^2 - a9^3 = 0
      x^1 y^1 :  -6*a10*a11      = 0
      x^1 y^0 :  -6*a11*a12 + a2*a9^3 = 0
      x^0 y^2 :  -3*a10^2 + a9^3 = 0
      x^0 y^1 :  a1*a9^3 - 6*a10*a12 = 0
   saturated Groebner basis at a9 != 0 (Rabinowitsch T*a9 - 1, lex) : EMPTY (1 in ideal)
```

By hand: `a_9^3 = 3a_{10}^2 = −3a_{11}^2` and `a_{10}a_{11} = 0`, so one of
`a_{10}, a_{11}` vanishes, forcing `a_9^3 = 0`, i.e. `a_9 = 0` — contradiction.
**`SATURATED-EMPTY`.**

*FALLACY-v2 `sat()` discipline.* The ideal is generated in `Q[a_1..a_{12}, T]` with the
generator order declared above; saturation at `a_9` is implemented by the Rabinowitsch
generator `T·a_9 − 1` (not by `sympy`'s `sat`); the object returned is the Gröbner basis
`[1]` of that *component*, in `Q[a_1..a_{12},T]` with lex order. Controls run
(`moh_1510_controls_pm.py`):

```text
  MAIN     : saturate all 5 at a9!=0 -> EMPTY  [1]
  POSITIVE : drop (2,0)  -> NON-TRIVIAL (5 gens)     drop (1,1) -> NON-TRIVIAL (5 gens)
             drop (0,2)  -> NON-TRIVIAL (5 gens)     drop (1,0) -> EMPTY [1]
             drop (0,1)  -> EMPTY [1]
  NEGATIVE : consistent toy system a9=1,a10=2,a11=3  -> NON-TRIVIAL (4 gens)  [expected]
```

so the emptiness is not an artefact of the wrapper (a consistent system in the same
ring returns a non-trivial basis), and the kill uses exactly the three equations
`(2,0), (1,1), (0,2)` — which is the hand argument above.

**Verdict on the control: PASSES.** Moh's `(15,10; M_2 = 11, V_2 = 3)` case is empty —
his conclusion is right, his printed `γ` and his printed Case-2 argument are not. This
is a genuine (small) defect in Appendix II found by re-running it, and it is the sort
of defect that a machine-checked descent engine is for.

### 4.3 The two problems, written out — and why they are typed COUNTING-BOUND

**Normal form (PROVED-HERE).** Let `(f, g)` be a descended pair: `f, g ∈ k[x,y]` monic
in `y`, `deg f = deg_y f = m'`, `deg g = deg_y g = n'`, `J_{x,y}(f,g) = c x^k`. Put
`K' = gcd(n',m')`, `e' = n'/K'`, `d' = m'/K'`, and let `h` be the `d'`-th approximate
root of `f` (`deg_y h = m'/d' = K'`). Then, in characteristic `0`,

* `f = h^{d'} + 2β` for `d' = 2` (resp. `f = h^{d'} + β_2h^{d'-2}+…` in general), with
  `deg_y β ≤ K'−1`;
* `g = h^{e'} + G_{e'-2}h^{e'-2} + … + G_0` with `deg_y G_i ≤ K'−1`, `G_{e'-1} = 0`;
* **(Lemma 2.1 for a monomial Jacobian, PROVED-HERE)** writing
  `g = η̃^{-n'} + Σ_{j>-n'} g_j(x)η̃^j` with `η̃ = f^{-1/m'}`,
  `J(f,g) = c x^k ⟺ g_j(x) ∈ k` for all `j < m'−1` **and** `deg_x g_{m'-1} = k+1`.
  *Source check:* Moh p.208–210 for the `(15,10; X^2)` row writes
  `g = η^{-15} + aη^5 + bη^6 + c(x^3+d)η^9 + …` — `a, b` constants, and the `η^9 = η̃^{m'-1}`
  coefficient of `x`-degree `3 = k+1` with `k = 2`. **Exact match**, `SOURCE-READ`.
* **(exponent dictionary, PROVED-HERE)** if `N := min{ j : g_j ≠ 0, K' ∤ j }` in the
  `η̃`-expansion, then `M_2 = N + (n'−m')` in the `η = g^{-1/n'}`-expansion — from
  `f = η̃^{-m'} = η^{-m'}(1+U)^{-m'/n'}` with `U = Σ g_jη̃^{j+n'}`, so the correction
  exponents are `j + n' − m'`. For `e' − d' = 1` (both D = 105 problems and Moh's row)
  this is `M_2 = N + K'`. *Source check:* Moh's `(15,10)` row has `N = 6` (his
  `b`-term) and prints `M_2 = 11`; `6 + 5 = 11` ✓.

**G2 — the `(15,10; γ^4)` problem.** `n' = 15, m' = 10, K' = 5, e' = 3, d' = 2`,
`k = v_s−u_s−1 = 4`, `M_2' = 4`, hence `N = M_2' − K' = −1`; `V_2' = 1`, `d_2' = 5`,
`u' = d_2' − V_2' = 4`, so `deg_x g = u'n'/d_2' = 12`, `deg_x f = 8`, `deg_x h = 4`.
Explicitly: find `h, β, G_1, G_0 ∈ Q[x,y]` and `c ∈ Q^*` with

```text
   h   monic in y, deg_y h = 5, deg h = 5, deg_x h <= 4
   f   = h^2 + 2*beta ,               deg_y beta <= 4, deg f = 10, deg_x f <= 8
   g   = h^3 + G_1*h + G_0 ,          deg_y G_i <= 4,  deg g = 15, deg_x g <= 12
   J_{x,y}(f,g) = c*x^4                                              [4 x^k-Jacobian]
   g_j(x) in k for j < 9 ,  deg_x g_9 = 5                            [Lemma 2.1, monomial]
   g_j = 0 for j in {-14..-11, -9..-6, -4,-3,-2} ,  g_{-1} != 0      [M_2' = 4]
```

The Jacobian condition expands, using `J(h,h)=0` and the derivation property, into the
`h`-adic identity

```text
J(f,g) = 2h^2*J(h,G_1) + h*[2 J(h,G_0) + 6 J(beta,h)] + [2 G_1 J(beta,h) + 2 J(beta,G_0)]
```

whose `h`-adic components give one equation `≡ c x^4 (mod h)` and two vanishing
equations, each a polynomial identity of `y`-degree `< 5`.

**G3 — the `(21,14; γ^2)` problem.** `n' = 21, m' = 14, K' = 7, e' = 3, d' = 2`,
`k = 2`, `M_2' = 8`, `N = M_2' − K' = 1`; `V_2' = 1`, `d_2' = 7`, `u' = 6`, so
`deg_x g = 18`, `deg_x f = 12`, `deg_x h = 6`, `deg_y h = 7`, `deg_y β ≤ 6`,
`deg_y G_i ≤ 6`, and `g_j ∈ k` for `j < 13`, `deg_x g_{13} = 3`, `g_j = 0` for the
non-multiples of `7` in `(−21, 1)`, `g_1 ≠ 0`.

**Counts (shape-free normal form, G2).**

```text
   h      : monomials x^i y^j, i+j <= 5, i <= 4, minus the monic leader      19
   beta   : j <= 4, i+j <= 10, i <= 8                                        42
   G_1    : j <= 4, i+j <= 10, i <= 12                                       45
   G_0    : j <= 4, i+j <= 15, i <= 12                                       65
   c                                                                          1
   TOTAL unknowns                                                           172
   (G_2 = 0: the h^{e'-1}-coefficient vanishes by definition of the approximate root)
   equations: 3 h-adic Jacobian identities of y-degree < 5 over Q[x],
              plus 12 vanishing conditions g_j = 0 and one non-vanishing g_{-1} != 0.
```

**Why the lane stops here.** Moh reduces the *same* `(15,10)` problem from 202
coefficients to **22 [15 or 13]** before computing, and every step of that reduction
consumes the descended disc data: p.210, *"The datum `δ_1 = 1/2` implies that the
polynomials `h(x,y)` and `β(x,y)` must be of the following form (cf. the beginning of
this Appendix)"* — followed by shapes (5) and (6), which cut `h` from 20 free
coefficients to 8 and `β` to 4. Those shapes are read off `δ_1'`, the subdisc split
(`"in the major disc D_2 there are precisely three subdiscs which contains 2, 2, 6 of
roots f"`), and `V_2'`; and `δ_1'` for a descended pair is exactly the quantity §3.4
could **not** reproduce (10 unresolved rationals). Without it the G2 system stands at
172 unknowns — far outside the stated desk budget (< 30 min, 1 core, < 6 GB) for an
exact Gröbner computation. **Per the charge, the systems are emitted with counts and
the lane stops.**

**Typed outcome.**

```text
   G2 (15,10; X^4; M_2'=4, V_2'=1, d_2'=5)  :  COUNTING-BOUND only  (172 unknowns emitted)
   G3 (21,14; X^2; M_2'=8, V_2'=1, d_2'=7)  :  COUNTING-BOUND only  (system emitted)
   G1 (30,20; X^2) conditional on delta*_2 >= 5/2 : NOT REACHED (OPEN[MINOR-DICHOTOMY])
   CONTROL (15,10; X^2; M_2=11, V_2=3)      :  SATURATED-EMPTY  (reproduces Moh, §4.2)
```

Neither `SURVIVES` nor `SATURATED-EMPTY` is claimed for G2/G3. In particular **no**
positive signal above `D = 100` is asserted, and **no** kill of `D = 105` is asserted.
The planted-automorphism positive control was not run (it is only meaningful once the
solver stage exists), so the pipeline's `SURVIVES` branch is **uncalibrated**; the
`SATURATED-EMPTY` branch is calibrated by §4.2.

**The single cheapest unblock**: recover `δ_1'` for one descended row. Two desk routes,
half a day each: (a) read Moh pp.176–182 (Prop 5.1–5.4, the derivation of Def 5.1(3))
for the definition of the radius of a disc in terms of the pair, and apply it to a
pair with monomial Jacobian; (b) *measure* it — take Moh's own `(15,10)` shapes (5),(6)
with a random admissible `a_1..a_{12}`, form `f = h^2+2β`, `g = h^3+3βh+(3/2)α`, and
read the disc radii off the `π`-roots numerically; the answer must be `δ_2' = −1`,
`δ_1' = 1/2`. Route (b) is a genuine control and needs only the engine already built.

## 5. Task (4) — reading: is "sieve + typed descent recursion" an all-degree mechanism?

**What Moh's program is** (`SOURCE-READ`, p.207): *"A simple computer program shows
that the only possible counter-examples … are of degrees (64,68) [erratum for (64,48)],
(84,56), (75,50) and (99,66) with some special data attached."* The program is the
`(1)–(13)` sieve; Appendix II is hand case-work *after* it, and its engine is
uniform in form: **descend by Prop 6.3/6.4 to a monomial-Jacobian pair of degrees
`(n/d_s, m/d_s)`, then test polynomiality of the quasi-approximate-root expansion at
the major and the minor π-root.**

**What the recursion terminates in.** Iterating Prop 6.3 while `u_s = 1` divides the
degree by `d_s ≥ 4` at each step — but the descended pair is **not** a Keller pair, and
§3.5 shows the tower does not regenerate: `s' = s−1`, so after one step `s' = 2` and the
data for a *second* descent are the descended pair's own `(d_2', V_2, d_2'−V_2)`. The
recursion is therefore **at most `s−1 ≤ 4` steps deep**, terminating in a
monomial-Jacobian pair with `s' = 2` — exactly the objects of APPROACHES row 1
(`[P,Q] = x^k`). It is a **finite reduction, not a well-founded recursion**: the depth
is the tower height, which does not grow with `D`. `DESCENT-RECURSION` therefore gives a
uniform reduction to one problem class, not an induction on degree.

**The theorem that would make it a proof.** Exactly one statement is needed:

> **(T)** *For every `k ≥ 0` and every `(n', m')` arising as `(u_s n/d_s, u_s m/d_s)`
> from a `(1)–(13)` skeleton, there is no pair `P, Q ∈ k[γ,π]`, monic in `π` of
> `π`-degrees `n', m'`, of total degrees `n', m'`, with `J_{γ,π}(P,Q) = cγ^k`, `c ≠ 0`,
> and with the inherited characteristic data `{M_i/d_s, d_i/d_s}` and `V_i' = V_i`.*

(T) plus the descent plus `OPEN[MINOR-DICHOTOMY]` for the `u_s > 1` branch is a
complete proof of the Jacobian conjecture along Moh's line. (T) is a statement about
monomial-Jacobian pairs of *bounded tower height* (`s' = 2`) but *unbounded degree*, so
it is not obviously easier than the original; what it buys is that the coefficient
count drops by a factor `d_s^2 ≥ 16` and that the "one place at infinity" data is
`(n', m', M_2', V_2')` — four integers.

**The single cheapest next experiment.** Not the trio, and not the interpolation
engine. It is: **measure `δ_1'` on Moh's own `(15,10)` shapes** (route (b) of §4.3,
half a day of one seat, no new theory). It closes the last column of
`OPEN[DESCENT-POLYGON]`, unlocks the Appendix-II reduction for arbitrary descended
rows, and turns §4.3's 172-unknown systems into ~20-unknown systems of exactly the size
the control in §4.2 solved in 20 seconds. Everything else in the descent programme
(the engine of Fable §5, the trio, the 28-row residue, the `D = 108` pair) is
downstream of that one number.

**Disposition of Fable's recommendations, revised.** `M2-ABOVE-M` as a filter: **do not
use** (§2). The descent engine: **build, but gate it on `δ_1'`** — without the radii
the engine can emit descended data (it is a two-line transformation) but cannot decide
anything, so it is a bookkeeping tool, not a discriminator. Row 1 (GGV corner
families, `[P,Q] = x^k`): **RAISE**, unchanged — it is the receiver in (T), and (T) is
now stated. Row 5 (JvdK degree descent) retyped as monomial-Jacobian descent:
**agreed**, with the correction that the recursion is depth-bounded by `s−1`, so it is
a reduction, not an induction.

## 6. Bounded quantities and OPEN accounting

OPENS RAISED

* `OPEN[DESCENT-RADII]` — compute the logarithmic radii `δ_i'` of the Prop 6.3-descended
  pair from the tower data of the original, so that Def 5.1 and conditions (8)–(13) can
  be evaluated on the descended pair and the Appendix-II shape reduction can be
  automated. **Bounded quantity: 10 rational numbers** (the `δ_2', δ_1'` entries of the
  five `u_s = 1` rows of Moh's p.207 table), of which at least 0 and at most 10 are
  misprints. This is the residue of `OPEN[DESCENT-POLYGON]` after §3.3.
* `ERRATUM[APPII-GAMMA-B]` — Moh p.211: the `B`-coefficient of `γ` is `−a_9^2a_8`, not
  `−a_9^2a_{10}`; consequently his Case-2 argument for `(15,10; M_2=11, V_2=3)` must be
  replaced by the `c_2 − 3γ ∈ k` computation of §4.2. **Bounded quantity: 1 coefficient;
  the conclusion (impossibility) is unchanged.** `PROVED-HERE`.
* `ERRATUM[PROP63-JAC-SIGN]` — Moh p.198, last display of the Prop 6.3 proof, prints
  `−u_s/(bγ^{v_s−u_s−1})` where statement (3) and the p.207 table require
  `−(u_s/b)γ^{v_s−u_s−1}`. **Bounded quantity: 1 sign of an exponent.** `SOURCE-READ`.

OPENS ANSWERED / SHARPENED

* `OPEN[M2-ABOVE-M]` — **ANSWERED NEGATIVE in the form charged** ("a theorem for Keller
  pairs in Moh's gauge"): refuted by 12 witnesses, §2.2–§2.3, of which 4 also satisfy
  `d_s ≥ 4`. **Residual form**: whether `(1)–(13)` + the minimal-counterexample
  hypotheses imply `M_2 > m`. **Bounded quantity for the residual: 564 rows / 54 classes
  at `n ≤ 100` with `M_2 ≤ m`, of which 293 rows / 33 classes survive the integral
  `N ≥ 6` pin and 243 have `u_s = 1`.** Smallest: `n=45, m=30, M=[−30,10,43], V={2:1,3:4}`.
* `OPEN[DESCENT-POLYGON]` — **degrees CLOSED** (§3.2–§3.3): `deg_π P = deg_x g = u_s n/d_s`,
  total degree `= π`-degree, `deg_γ P = u'n'/d_2'`, leading form `y^{n v_s/d_s}z^{u_s n/d_s}`,
  and `u_s + v_s = d_s`. **Radii OPEN**, re-raised as `OPEN[DESCENT-RADII]` above.
* `OPEN[DESCENT-CLOSURE]` — **partially closed** (§3.5): (2),(3),(5),(7) and `M_2 > m`
  descend; (4) and the `s ≥ 3` half of (6) do not. **Bounded residue: conditions
  (8)–(13), i.e. 6 conditions**, blocked on `OPEN[DESCENT-RADII]`.
* `OPEN[MINOR-DICHOTOMY]` — untouched (G1 not reached).
* `OPEN[DESCENT-LIFT]` — not reached (no descended solution set was produced).
* `OPEN[MOH-PROGRAM]` — **NOT sharpened by this lane.** Fable's conditional sharpening
  to 28 rows rests on `M_2 > m`, which §2 refutes as a theorem; the banked bound
  (652 excess rows at `n ≤ 100`) stands.

**FALLACY-v2 check.** No exit price is asserted anywhere in this report, so no
`charge_basis` line is required and none is given. No cv-flag / physical-place / cover-
series identification occurs. No per-ray or exit-set charge is made. `REPRESENTATIVE`
vs `FULL_ACTUAL_EXIT` does not arise. No pole identity is used. **Floor/attainment**:
§2.2 is an existence statement with printed witnesses (attainment, not a floor); §3.2
(P1),(P2) are equalities proved from the monic-in-`π` normalisation, and each is
confirmed against a printed source instance; §3.3's total-degree statement is
`SOURCE-READ` (Moh's own count), *not* proved here, and is typed as such. **`sat()`
wrapping**: §4.2 declares the ring `Q[a_1..a_{12},T]`, the generator order, lex order,
the Rabinowitsch saturation generator, and both controls; the returned object is the
Gröbner basis `[1]` of the *component*, not a `sat()` wrapper. **Raw remainder degree**:
all divisions in §4.2 are exact `sympy.div` in `y` by a polynomial monic in `y`
(`h` is monic in `y`, verified), so no leader vanishes and no branch is needed; the
identity `β^2 − αh − γ = 0` is checked. **Variable/ring map**: Moh's Appendix II reuses
`x, y` for the descended pair's variables and `γ` for a *polynomial coefficient*; this
report writes the Prop 6.3 variables as `(γ, π)` and the Appendix-II variables as
`(x, y)`, and never identifies the two `γ`'s — §4.2's `γ` is the Appendix-II remainder
polynomial, §3 `γ` is `θ^{1/u_s}`. **Prime label/derivative**: `'` in `M_i', d_i', n', m',
δ_i', V_i', u'` is a *label* for the descended datum, never differentiation; `f_i'(x)`
and `g_j'(x)` in Lemma 2.1 and its monomial-Jacobian analogue **are** derivatives, as
Moh defines them (p.151). **Merge-free/M-descent** and **target/arrival index** do not
arise. `N_min = 6` is read from the frontier line and never re-derived. No `D ≤ C(N)`
is inferred.

## 7. Typed block

```text
LANE         m2-descent-opus5-20260903 (Opus 5)
SOURCE       Moh 1983 read at 300 dpi: pp.148-151, 179, 196-199, 207-212 (SOURCE-READ)
REPRODUCED   Fable's M_2>m measurement, exactly (6/6 printed; 658->94; 1189->179->63/59;
             (75,50) residue; D=105 has no N-alive group under the filter)
PROVED-HERE  M_2 > m is FALSE for Keller pairs in Moh's gauge (12 automorphism witnesses,
             one printed in full; 4 witnesses also have d_s >= 4) -> H1, H2 dead as posed
PROVED-HERE  deg_pi P = deg_x g = u_s n/d_s ; z-leading coeff of gbar = y^{n v_s/d_s} ;
             u_s + v_s = d_s ; deg_gamma P = u' n'/d_2'   [twice source-confirmed]
PROVED-HERE  DESCENT-CLOSURE: (2),(3),(5),(7) and M_2>m descend; (4) and s>=3 do not
PROVED-HERE  Moh's (15,10; M_2=11, V_2=3) case is SATURATED-EMPTY; his printed gamma has
             an erratum and his printed Case 2 does not close -- the kill is one step later
SOURCE-READ  descended total degree = pi-degree (Moh's counts 244/373/202 = C(n'+2,2)+C(m'+2,2))
NOT CLAIMED  any kill or any survival of G2, G3, G1; any realisation; D_min >= 108;
             the 28-row sharpening of OPEN[MOH-PROGRAM]; delta_2', delta_1' of the p.207 table
OPEN RAISED  OPEN[DESCENT-RADII] (10 rationals), ERRATUM[APPII-GAMMA-B], ERRATUM[PROP63-JAC-SIGN]
NEXT         measure delta_1' on Moh's own (15,10) shapes (half a day) -- it is the single
             gate in front of the whole descent programme
```

## 8. Drivers

```text
box/m2descent-drivers-20260903/etaexp.py             exact eta-expansion / characteristic data
box/m2descent-drivers-20260903/repro_m2_filter.py    fail-closed reproduction of the M_2>m cut
box/m2descent-drivers-20260903/repro_degrees.py      48<=D<=120 sweep + the D=105 trio
box/m2descent-drivers-20260903/autoscan.py           automorphism population, Moh gauge
box/m2descent-drivers-20260903/autoscan2.py          wider scan + printed witness
box/m2descent-drivers-20260903/candidates.py         the M_2<=m candidate skeletons
box/m2descent-drivers-20260903/descent_table.py      Prop 6.3 descent + p.207 gate + closure table
box/m2descent-drivers-20260903/moh_1510_control.py   Appendix II control, first pass
box/m2descent-drivers-20260903/moh_1510_control2.py  Appendix II control, audited + saturation
box/m2descent-drivers-20260903/moh_1510_controls_pm.py  positive/negative controls on the saturation
  page images: not kept (34 MB of derived PNGs deleted after reading).  Reproduce with
  for p in 9 10 11 12 40 57 58 59 68 69 71 72; do pdftoppm -r 300 -f $p -l $p -png \
      refs/moh1983_jram340_configurations_of_roots.pdf pages/p$((p+139)); done
  (journal page N = PDF page N-139; pages read: 148-151, 179, 196-199, 207-212)
```

## COLLISIONS

status: EMPTY

- `OPEN[DESCENT-RADII]` (report:698): NONE

<!-- BODY-END -->
