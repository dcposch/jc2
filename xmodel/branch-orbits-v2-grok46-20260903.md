# BRANCH-ORBITS v2 — (UNI) is not a theorem; one Galois orbit of bottom-major discs has size the product of Moh's increment denominators `A_j` on the `(10)` levels, and the orbit-aware knapsack on the true (1)–(13) census

Lane BRANCH-ORBITS v2 (Grok 4.6), 2026-09-03. Relaunch of the killed
`branch-orbits-grok46-20260902` lane (NO-REPORT), now on the rebased (1)–(13)
census. Charged inputs verified 8/8 SHA-256 against the frozen copies in
`/tmp/jc2-lane.GqI4QH/inputs` (mismatch would have stopped the lane):

```text
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  d1-subtree-review-grok46-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  d1floor.py
47f59906927ff9d2b38b25b11c2e46cef3c472b3d8db300f12c12f22906848e1  survivors-D48-120.txt
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
```

Source pages rendered at 300 dpi with `pdftoppm -r 300 -png` and read as images
(journal p.`N` = PDF page `N−139`): p.150 (Ω-symmetry), pp.168–171 (Props 4.4,
4.5, 4.6), p.173 (count of subdiscs = deg `q(π)`), p.179 (Def 5.1), p.180
(Prop 5.3), p.188 (Prop 5.6 and the derivation of (12)/(13)), p.194 (Lemma 6.1
and the unique major `D_{s−1}`), pp.200–202 (the Theorem's disc-count bound,
search (1)–(13)). `pdftotext` is not used for display formulae.

No `jc2-lean`, no ideation-20260903T* file, no canonical ledger edit. Desk-scale
CAS, one core, Fractions, no Groebner. No exit-price assertion, so no
`charge_basis` line.

## 0. Headline

1. **(UNI) is not a theorem.** The `u` copies of `L_1` in Moh's gauge
   `H = L_1^u L_2^v` occupy **one** disc `D_{s−1}`, not `u` conjugate discs.
   Below `D_{s−1}` the cluster splits, and Prop 4.6 plus the Galois action
   `t̄ ↦ ω t̄` of order `A_{r−1}` produce **one or several** orbits of
   bottom-major discs, possibly with different lower-`V` data. OPEN[BRANCH-ORBITS]
   remains open as a geometric existence question; its bounded quantity is
   unchanged: the number of Galois orbits of bottom-major discs, an integer in
   `{1,…,u}`, together with the partition of `Σ_B V_2(B) ≤ u` among them.
2. **Orbit size of one bottom disc, PROVED-HERE from the printed Galois.**
   `D_s` has exactly two children (Prop 4.5 + p.200 Theorem (6): `deg q = 2` at
   `δ_s = −1`), one major and one minor, different multiplicities. After the
   Lemma 6.1 coordinate change, `D_{s−1}` is unique and Galois-fixed. Each
   subsequent split `D_j → D_{j−1}` contributes a local orbit size `ω_j = A_j`
   on the `(10)` branch (`π−a`, `a ≠ 0`; free multiplicative action on `ℂ*`)
   and `ω_j = 1` on the `(11)` branch (`π`). Hence
   `|O|(D_1) = ∏_{j=2}^{s−1} ω_j`.
   Moh's `A_1` is **not** an orbit-size of discs: it is the (12)/(13) increment
   of the denominator of `δ_1` inside `D_1`.
3. **Each orbit's `V`-data must satisfy (8)–(13) on its own** (PROVED-HERE).
   Radii, `A_j`, and (12)/(13) are computed from that orbit's tower via Def 5.1(3).
   Joint packing of several orbits is the budget `Σ |O_k| V_2^{(k)} ≤ u`, which
   at `s = 3` is exactly `deg p` at the unique `D_2`.
4. **Compute, fail-closed against census-rebase §6.** On the (1)–(13) space
   `48 ≤ D ≤ 120` (1 189 groups, 1 692 V-assignments, 274 of them `s=3`):
   rebase reproduced to the unit (670 / 589 / 648). Orbit-aware knapsack
   (Fractions, cap never hit). Two packings:
   - **`s=3` exact** (unique `D_2`, NZ unbounded, Z 0–1): **173** alive at
     `N ≥ 6`, **138** in `[6,16]`, of 274 groups (UNI had 187 / 165).
   - **All `s`, both packet types unbounded** (relaxation; upper bound on
     survivors): **681** at `N ≥ 6`, **575** in `[6,16]`. 73 mix-alive groups
     die in `[6,16]` already on this relaxation (18 of them `s=3`).
   **`D = 88` empties in `[6,16]`** (`s=3` exact: `|O|=14`, only `N=18`);
   it lives at the campaign frontier `N ≥ 6`. `D = 48` remains empty;
   `D = 66, 78` have no skeleton; **no `D > 100` empties.** `D = 105` keeps
   its 3 groups in `[6,16]`, all `s=3` exact, each a single NZ packet with
   `N = 9` (the UNI list `[6..12]` on `M=[28,103], V_s=5` shrinks to `{9}`).

---

## 1. What Moh means by "the" branch

### 1.1 The η-tree (p.150) is the wrong Galois group

p.150, image, after introducing `Ω_i(x)=x`, `Ω_i(η)=ω^i η` on `k[x]((η))` with
`η = g^{1/n}`:

> Due to the existence of the automorphisms `Ω_i`, the tree data associated with
> the configuration of the roots of the equation (1) over `k[x]((η))` are
> completely symmetric. Hence the tree data along any root will determine the
> tree data completely. Let the tree data along one root (hence all roots) be
> (reindexed as) `{M_j, d_j}`. We shall call `{M_j, d_j}` the *characteristic
> data* of the pair of polynomials `(f(x,y), g(x,y))` with respect to `x`.

Equation (1) on that page is `∏_{i=1}^n (f − Ω_i f) = 0`, the analytic
factorisation of the defining equation of the rational curve `(f,g)` at
`g=∞`. The Galois group is `η ↦ ωη` on the **η-adic** expansion of the curve
over `k(x)`. Integration #17 delta (h) and the d1-subtree review already
refused to import this as (UNI) for bottom-major discs of the `t`-tree of
`g−c_2`. The refusal stands: different Galois group, different tree. Characteristic
data `{M_j, d_j}` **are** global (one pair `(f,g)` has one characteristic
sequence). The lower-`V` sequence `{V_s,…,V_2}` is **not**.

Moh's own search language on p.201 treats the `V`-sequence as attached to
**a** tower:

> Furthermore we assign a sequence of integers `{V_s, …, V_2}` for a
> hypothetically existing tower of major discs `D_s ⊃ ⋯ ⊃ D_1` (cf. Theorem
> and Definition 5.1)

"A" tower, "hypothetically existing". He never says there is only one.

### 1.2 Def 5.1 / Prop 4.4 / Prop 4.6 / the p.200 Theorem fix the disc counts

**Definition 5.1** (p.179, image). A tower `D_s ⊃ D_{s−1} ⊃ ⋯ ⊃ D_r` with
integers `{V_i : i = r+1,…,s+1}` satisfies:

> (1) In the disc `D_i` the polynomials `g(y)` have precisely `(n/d_{i+1}) V_{i+1}`
> roots. `T_j^ψ(y)` has precisely `(−μ_j / d_{i+1}) V_{i+1}` roots for `j=1,…,i`.
>
> (2) `V_{i+1} d_i / d_{i+1} ≥ V_i > d_i/(n−M_i)` for `i=r+1,…,s`, `V_{s+1}=d_{s+1}`.
>
> (3) logarithmic radii `δ_i` by the printed product (the campaign's formula).
>
> (4) `σ_i = Σ α_j t^j + π t^{δ_i}` is the unique general point in `D_i`; Prop 4.6
> holds for `σ=σ_i`, `δ=δ_i` and `v = V_{i+1}(d_i/d_{i+1})`.

So `D_i` contains `a_i = (n/d_{i+1}) V_{i+1}` roots of `g`. At `i=s`,
`V_{s+1}=d_{s+1}`, hence `D_s` contains **all `n` roots**. At `i=s−1`,
`D_{s−1}` contains `(n/d_s) V_s` roots. Since `u = V_s K / d_s` and `K=d_2`,
`e=n/K`, this is `u e` roots: the entire major pool. At `i=1`, `D_1` contains
`e V_2` roots.

**Proposition 4.4** (p.168, image), nonsplitting: under the seven numerical
hypotheses, `g_σ(π), T_{1,σ}^ψ(π), …, T_{r,σ}^ψ(π)` are **powers of a common
linear polynomial in `π`**. One child direction. This is the criterion that
a disc is *not* a tree-disc (p.142, p.173): all distances strictly less than
the radius, so one shrinks further.

**Proposition 4.6** (p.170, image), splitting, `r≥2`: leading coefficients are
powers of a common `p(π)` of degree `v`; `T_{r,σ}^ψ(π) = p(π)^{…} · q(π)` with
`deg q = v(n−M_r)/d_r`; **`q` has all distinct roots**; every root of `p` is a
root of `q`; `p` is not a power of `q`. p.173, image:

> Proposition 4.6 specifies that the number of subdiscs `D_{1,i_2,…,i_r,j}` is
> the degree of `q(π)`, and the number of roots in those subdiscs are unequal.
> If we choose one of the subdiscs with the number of roots above a certain
> number (cf. Definition 5.1) …

"We choose **one**". That is Moh's "the" branch: among the `deg q` children of
unequal size, follow a major one. Prop 5.2 (p.179, last paragraph) says any
above-average child of `D_s` may be used as `D_{s−1}`; existence is Prop 4.6.

**Proposition 4.5** (p.169) plus the p.200 Theorem pin the top split. Prop 4.5:
if `M_r = n−2` for some `r`, the highest homogeneous forms of `g` and the
`T_i` are powers of a common form with **at most two distinct linear factors,
and the multiplicities are different**. p.194:

> The major disc `D_s` is of logarithmic radius `−1`. It contains a major disc
> `D_{s−1}` and a minor disc `D_{s−1}^*`.

p.200 Theorem (6), image: the number of subdiscs `E_i` of `D_r` is bounded by
`(n−M_r)·V_{r+1}/d_{r+1}`, which is `deg q`. At `r=s`, `n−M_s=2` and
`v=d_s`, so `deg q = 2`. Exactly two children, unequal multiplicities, unique
major child. **The `u` copies of `L_1` sit in this one disc `D_{s−1}`.** They
are not `u` Galois conjugates at the `L_1` point; they are multiplicity-`u` of
one linear factor of the leading form
`g_n = [(y−ax)^{V_s} (y−bx)^{u_s}]^{d_s}` (p.194, `u_s = d_s − V_s`, `a≠b`).

Lemma 6.1 (p.194): `δ_s=−1` implies `δ_{s−1} ≥ 0`. All major roots in `D_{s−1}`
are `y = a t^{-1} + c_j + higher`; one may take `a=0`. After that coordinate
change `D_{s−1}` is 0-centred in the leading form and Galois-fixed (the two
leading factors `L_1, L_2` are distinct `k`-points, not a cyclotomic orbit).

### 1.3 The `u` major branches can split into several orbits with different lower-`V`

Below the unique `D_{s−1}`, Prop 4.6 produces `deg q` distinct children of
**unequal** root-counts. Galois conjugates must carry the same multiplicity
(the action `t̄ ↦ ω t̄` of p.201 permutes factors of `p` and preserves
multiplicity). Unequal sizes therefore mean **more than one Galois orbit**, or
at least a major/minor split inside `D_{s−1}`. Different orbits may take
different `V_{s−1},…,V_2` (different multiplicities of their `p`-factors),
hence different `q`. That is the several-orbits case of OPEN[BRANCH-ORBITS].

Nothing in Def 5.1, Prop 4.4, Prop 4.5, Prop 4.6, Lemma 6.1, or search (1)–(13)
forces those children to be a single orbit. The tower structure forces a unique
`D_{s−1}`, not a unique `D_1`.

(UNI) — "all bottom-major discs carry the same lower-`V` datum" — is therefore:

- **CONFIRMED** inside one Galois orbit (the action is an isometry of the
  `t`-adic metric and preserves `(a_1, δ_1)`), as integration #17 delta (h)
  already typed;
- **NOT a theorem** across orbits;
- **NOT forced to orbit-count 1** by "all `u` copies of `L_1` conjugate" (they
  are not copies in that sense).

---

## 2. Packet structure

### 2.1 Local orbit size at one split (PROVED-HERE)

p.201 (8)–(11), image. `A_{r−1}` is the reduced denominator of `L δ_{r−1}`,
`L = lcm{den δ_s, …, den δ_r}` — the *increment* of the denominator. The
automorphism of `k⟪t̄⟫` over `k⟪t̄^{A_{r−1}}⟫`, `t̄ ↦ ω t̄`, `ω` an
`A_{r−1}`-th root of unity, with `t̄^{L A_{r−1}} = t`, permutes the factors of
`p(π)` at the general point of the parent. `p` has degree
`Q = V_r (d_{r−1}/d_r) = deg p` at `D_{r−1}` (Def 5.1(4)).

- Factor `(π−a)^{V_{r−1}}`, `a≠0`: the action on the `π`-coordinate is
  multiplicative, `a ↦ ω^κ a`. This is free on `ℂ*`, so the orbit has size
  **exactly** `A_{r−1}`, not a proper divisor. Hence
  `A_{r−1} V_{r−1} ≤ Q`, i.e. (10) `V_{r−1} ≤ △_{r−1}`.
- Factor `π^{V_{r−1}}`: the point `0` is fixed, orbit size 1, and the remaining
  degree is a union of free orbits, so `V_{r−1} ≡ □_{r−1} (mod A_{r−1})`, i.e. (11).

Indexing: (9)–(11) at `j = r−1 ∈ {s−1,…,2}` constrain the split
`D_j → D_{j−1}` (child multiplicity `V_j`, Galois order `A_j`). They do **not**
run at the top split `D_s → D_{s−1}` (`V_s` is the global leading-form
multiplicity; census-rebase §1.2). So the product of local sizes from the unique
`D_{s−1}` down to `D_1` is

```text
|O|(D_1)  =  ∏_{j=2}^{s−1} ω_j ,     ω_j = A_j on (10),  1 on (11).
```

If both (10) and (11) hold, both values of `ω_j` are admissible (do not
over-kill: either centre is possible). At most one `(11)`-factor per parent
(`π` is unique); several `(10)`-orbits of the same `V` may coexist (several
cyclotomic residue-orbits of the same multiplicity). The knapsack below treats
`(10)` packets as unbounded and does **not** impose the 0–1 constraint on
`(11)` (a relaxation at `s>3`, where several parents each have their own `π`;
at `s=3` there is one parent `D_2`, so 0–1 is the truth — the run reports
whether this bites).

### 2.2 `A_1` is not an orbit-size of discs

p.188, image: conjugations of `k((t^{1/A}))` over `k((t))`, `A` the reduced
denominator of `δ_1`, act on `g_σ(π)` of degree `n* V_2 = e V_2`. That polynomial
describes the `e V_2` roots **inside** one `D_1` (D1-STAR: they separate at
`δ_1`). (12)/(13) is this internal condition, applied always (both branches).
It is not a second multiplier of `|O|(D_1)`. CONTROL (six published rows):
`(12)` and `(13)` are mutually exclusive unless `A_1=1` (if both, `A_1` divides
`e V_2` and `e V_2−1`, hence divides 1).

### 2.3 Each orbit satisfies (8)–(13) independently (PROVED-HERE)

Def 5.1(3): `δ_i` of a tower depends on that tower's `{V_j : j>i}` only.
Hence `A_j = den(L_j δ_j)` is per-tower, (9)–(11) is per-tower, and (12)/(13)
is a condition on that tower's `A_1`, which depends on that orbit's `δ_1`.
A second orbit with a different lower-`V` datum has a different `δ_1`, a
different `A_1`, and must meet (12)/(13) for *its* `A_1`. The charged enumerator
emits only assignments with `full_ok()`, so every packet used below already
satisfies (8)–(13) on its own.

Joint constraint, not per-orbit: at a shared parent the factors of one `p(π)`
must pack. For `s=3`, `deg p` at the unique `D_2` equals `u` (algebra:
`u = V_3 d_2 / d_3 = Q`). The budget `Σ_k |O_k| V_2^{(k)} ≤ u` **is** that
packing. For `s>3` the same budget is implied by nested packing (each level's
`Σ ω V ≤ Q`) but does not imply it: the flat knapsack is a **relaxation** and
may under-kill. Typed: EXACT at `s=3`, UNREVIEWED-as-exact / conservative at
`s>3`. Bounded quantity of the residue OPEN[NESTED-PACK]: the nested partitions
of `Q_j = V_{j+1} d_j/d_{j+1}` at `j=s−1,…,2`, an integer tuple of length
`s−2` with each part at most `Q_j` and `s ≤ 5` on `D ≤ 120`.

### 2.4 Weight of a packet; how many orbits to fill the major pool

One orbit of type `V_2` with size `|O|` consumes `|O| V_2` of the `u` slots
and contributes `|O| V_2 q` to `N`. To exhaust the major pool one needs
`Σ_k |O_k| V_2^{(k)} = u` (or less, if some major slots sit in discs that are
major at `D_{s−1}` but become minor further down — D1-PIN already uses `≤ u`).
The number of orbits needed is an integer in `{1, …, u}` as charged. (UNI) is
the one-type case `k V_2 ≤ u` with `k` free, i.e. it **forgets** that `k` must
be assembled from copies of `|O|`. Orbit-aware (UNI) is `k ∈ |O| ℤ_{>0}`.
Several types: unbounded knapsack over the packets.

Prop 5.6 (p.188) kills `σ_1 = π t^{δ_1}` (all `α_j` vanish). Census-rebase
OPEN[PROP-5.6-SHADOW] remains: the numerical shadow "all levels take (11)" is
not equivalent to (13), and Moh's own `(75,50)` `V_2=3` row uses (13) while
taking (10) at `j=2`. This lane does **not** fold Prop 5.6 into the knapsack
(that would over-kill a printed row). Bounded quantity of the shadow: the 220
groups at `D≤120` named by census-rebase, untouched.

---

## 3. Compute

Driver `box/branch-orbits-v2-20260903/knapsack.py` (sha256
`aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276`),
charged enumerator `moh_skeleton_full.py` with `full=True`, `Kmin=16`.
Fractions. DP over `(weight used, fractional part)`: bitset when
`lcm(denoms) ≤ 4096`, else Fraction-sets with cap 60 000 (capped ⇒ alive;
**cap never hit**). Wall ~6 s one core, well under 4 GB. Log:
`box/branch-orbits-v2-20260903/run.log`
(`db82870a4c0b0f458fc82a8e6bf84dabc8896025ce43f67bdbb001abfb6c0ecc`).

**Packet.** For each (1)–(13) V-assignment, admissible `|O|` is the product
over `j=2..s−1` of `{A_j}` on (10)-only, `{1}` on (11)-only, `{1, A_j}` if
both. Item `(w,c) = (|O| V_2, |O| V_2 q)`, budget `Σ w ≤ u`. Mixing items
from different assignments of the same group is several orbits. `Q=u` on all
305 (1)–(13) `s=3` assignments (CONTROL Q), so the `s=3` packing is
`deg p` at the unique `D_2`. Two runs:

- **UNB.** NZ and Z both unbounded. Relaxation: several copies of the unique
  `π`-factor. Survivors are an **upper bound**; a kill is still a kill.
- **Z01.** NZ unbounded, at most one Z packet in the group. **Exact at
  `s=3`** (one parent, one `π`). At `s>3` it over-kills (several `D_2` each
  may carry a `π`); Z01 survivors at `s>3` are a **lower bound**.

**Controls, all pass, 336 checks, abort-on-fail.** Six published rows: orbit
`N` in `[6,16]` is `{9}`, `{}`, `{10}`, `{9}`, `{8}`, `{16}`, matching
integration #17 A.8 at `N ≥ 6` (the `(84,56) M_2=72` UNI value 5 is *not*
orbit-admissible: `|O| ∈ {1,4}`, `Z` gives `N=5/2`, `NZ` gives `N=10`).
`s=3 ⇒ Q=u` on 305 assignments. (10)-only ⇒ `A V ≤ Q` on 1 096 levels at
`D ≤ 100`, 0 exceptions. (12) xor (13) at `A_1>1` on all six rows. Census-rebase
§6 reproduced to the unit: 1 189 groups, 670 uni `N≥6`, 589 uni `[6,16]`,
648 mix `[6,16]`, empty mix `{48}`.

### 3.1 Per degree, `48 ≤ D ≤ 120`

Columns `uni>=6 / uni6-16 / mix6-16` are the rebase §6 numbers (reproduced).
`orb>=6 / orb6-16` are this lane. `grp` is (1)–(13) groups. Degrees with no
(1)–(13) skeleton (`66, 78` and every `D` not listed) are omitted, as in §6.

```text
    D    grp   s3  uni>=6  uni6-16  mix6-16  orb>=6  orb6-16
   48      2    1       0        0        0       0        0   emptied (all three)
   54      2    2       2        2        2       2        2
   60     15    7      13       13       13      13       13
   63      2    2       1        1        1       1        1
   64      9    3       7        7        7       7        7
   72     46   11      26       26       26      26       26
   75      5    5       3        3        3       3        3
   80     40   12      23       23       23      17       17   -6 exact-or-valid
   81      2    2       1        1        1       1        1
   84     38   20      21       21       23      21       21
   88      1    1       1        1        1       1        0   EMPTIED [6,16] (s=3)
   90     62   18      36       36       36      36       35
   96    157   19      86       83       90      92       83
   99      7    7       6        4        4       6        4
  100     57   20      32       32       32      31       31
  102      3    3       3        3        3       3        3
  104      3    3       3        3        3       3        3
  105     14   14       7        3        3       7        3
  108    125   28      87       71       76      90       70
  110      3    3       1        1        1       1        1
  112     71   21      33       29       29      29       22
  114      3    3       3        3        3       3        3
  117      7    7       4        4        4       4        4
  120    515   62     271      219      264     284      222
  TOTAL 1189  274     670      589      648     681      575
```

Totals of the UNB run (the table's `orb*` columns): (UNI) 670 / 589 as charged.
Mixed 648 as charged. Orbit UNB **681 / 575**. Killed in `[6,16]`: 600 (UNI) /
541 mixed / **614 UNB-orbit**, of 1 189. Capped: 0.

`s=3` only, Z01 exact (274 groups): UNI 187 / 165, mix 166 in `[6,16]`,
UNB-orbit 182 / 148, **Z01-orbit 173 / 138**. The 10 UNB-minus-Z01 groups at
`s=3` in `[6,16]` are false survivors (several copies of the unique `π`).
All-`s` Z01 is 611 / 493 and is **not** claimed exact at `s>3`.

UNB `orb>=6` can exceed `uni>=6` because several orbits of different `V`-data
hit an integer that no single type hits. `orb6-16` is below both UNI and mix
because Galois-completeness forbids UNI's free `k`.

### 3.2 Special degrees `{105, 108, 112, 117, 120}`

| `D` | grp13 | uni≥6 | uni[6,16] | mix[6,16] | orb≥6 | orb[6,16] | emptied? |
|---|---|---|---|---|---|---|---|
| 105 | 14 | 7 | 3 | 3 | 7 | **3** | no |
| 108 | 125 | 87 | 71 | 76 | 90 | **70** | no |
| 112 | 71 | 33 | 29 | 29 | 29 | **22** | no |
| 117 | 7 | 4 | 4 | 4 | 4 | **4** | no |
| 120 | 515 | 271 | 219 | 264 | 284 | **222** | no |

`D = 117` is all `s=3`. UNB keeps all four rebase survivors; Z01 (exact)
kills the first, which is (11)-only: one `π`-disc, `N = V_2 q = 9/7` not
integral. UNI's `{9}` was seven copies of that unique disc. Three remain:

```text
m=78 M=[13,115]  Vs=8  u=24 |O|=1  (11)-only A2=21  N_uni={9}  UNB={9}  Z01=DEAD
m=78 M=[52,115]  Vs=10 u=30 |O|=7  (10)-only A2=7   N_uni={6,9,12} = N_orb
m=78 M=[52,115]  Vs=11 u=33 |O|=6  (10)-only A2=6   N_uni={6..16}  N_orb={6,9,12,15}
m=78 M=[91,115]  Vs=11 u=33 |O|=7  (10)-only A2=7   N_uni={8} = N_orb
```

The third row is the typical (UNI) over-count: `q=1/2`, `V_2=1`, UNI allows
every integer `k ∈ [6,16]`; Galois forces `k ∈ 6ℤ`, so `{6,9,12,15}`. Still
alive. Degree not emptied. `D = 112` drops 29 → 22 UNB in `[6,16]` (seven
groups, including the three `m=64` rows of census-rebase §7 with UNI `{8}`:
`V_2=2`, `|O|=4`, `k` must be a multiple of 4, `N=4k/3` is integral at `k=6`
which is not a multiple of 4, and `k=8` overfills `u=12`). Z01 further drops
`D=112` to 19 (not claimed exact, `s>3` present).

### 3.3 `D = 105` — complete packet list (`s=3`, exact)

All 14 (1)–(13) groups are `s=3`, so the packing `Σ |O| V_2 ≤ u` is
`deg p` at the unique `D_2` and the list below is the complete realisation
list of the orbit-aware knapsack (not of geometric realisability).

**Alive in `[6,16]` — 3 groups**, the same three as census-rebase §7, all
`m=70`, `K=35`, `(d,e)=(2,3)`, one NZ packet, `N=9`:

```text
m=70 M=[28,103] Vs=5 u=25 V={2:1,3:5}
     δ1=7/12  q=1/2   A2=18 A1=2  (10) not (11)  (13)
     |O|=18  packet w=18 c=9   N_uni={6,7,8,9,10,11,12}  N_orb={9}
     leftover slots 25-18=7 < 18; (11) fails; one orbit fills.

m=70 M=[28,103] Vs=6 u=30 V={2:1,3:6}
     δ1=11/26 q=9/13  A2=13 A1=2  (10) not (11)  (13)
     |O|=13  packet w=13 c=9   N_uni={9}  N_orb={9}  (and 18 at N>=6)

m=70 M=[40,103] Vs=4 u=28 V={2:1,3:4}
     δ1=19/34 q=9/17  A2=17 A1=2  (10) not (11)  (13)
     |O|=17  packet w=17 c=9   N_uni={9}  N_orb={9}
```

The first UNI interval `[6..12]` is `N = k/2` for `k=12..24`; Galois forces
`k=18`, so `{9}` only. All three still live. (13) here is the internal
`g_σ` condition at `D_1` (`A_1=2 ∤ e V_2` typically), **not** a Z-centre of
the `D_2→D_1` split (that split is (10)-only, `|O|=A_2`).

**Alive at `N ≥ 6` but not in `[6,16]` — 4 further groups**, still `s=3`:

```text
m=70 M=[-42,103] Vs=6 u=30 |O|=25  N={24}
m=70 M=[10,103]  Vs=4 u=28 |O|=25  N={18}
m=70 M=[63,103]  Vs=6 u=30 |O|=7   N={24}   (two copies, w=28)
m=84 M=[28,103]  Vs=6 u=18 |O|=13  N={20}
```

The other 7 of the 14 groups hit no integer `N ≥ 6` (UNI and orbit agree).

### 3.4 Emptied degrees; the `D = 88` kill (PROVED-HERE, `s=3`)

- **No (1)–(13) skeleton:** `D = 66, 78` (and every unlisted `D` in `[48,120]`).
- **Emptied by integrality, all three knapsacks:** `D = 48` (2 groups).
- **New, orbit `[6,16]` only:** `D = 88`.
- **No `D > 100` empties**, at `N ≥ 6` or in `[6,16]`.

`D = 88` has one (1)–(13) group, `s=3`, so the kill is exact. Hand check
against Def 5.1(3) and (9)–(11):

```text
n=88 m=66  M=[-33, 86]  V3=9 V2=1
d2=K=22  d3=11  u = 9*22/11 = 18
δ2 = 3/14  (reduced), A2 = den(δ2) = 14
Q = u = 18 = 1*14 + 4,  △=1, □=4
V2=1 ≤ 1  (10)  ;  1 ≡ 4 (mod 14) fails  (11)
|O| = 14,  w = 14,  q = 9/7,  c = 18
UNI: N = k*(9/7) integral for k in 7Z, k V2 ≤ 18 ⇒ k=7 N=9, k=14 N=18
ORB: k in 14Z                ⇒                 k=14 N=18
```

`N=9` is the UNI/mix survivor in `[6,16]`; it is **not** a Galois-closed
packet. The only orbit-admissible integer is `N=18`, outside the H2 window
and inside the campaign frontier `N ≥ 6`. Typed: `D=88` is emptied in
`[6,16]` and **not** emptied at `N ≥ 6`. (MOH-SHARP-2 already has `D ≥ 105`,
so this is not a new degree-floor; it is a new H2 emptying on (1)–(13).)

The other 72 mix-alive/UNB-orbit-dead groups in `[6,16]` do not empty their
degrees. Split: 18 at `s=3` (exact, including `D=88` and six groups at
`D=80`), 39 at `s=4`, 16 at `s=5`. The 55 at `s>3` are kills of a
relaxation, hence valid kills of nested packing too. UNB's 575 survivors
remain an **upper bound** at `s>3` and, after removing the 10 false `s=3`
multi-`π` groups, an upper bound of 565 overall. Z01's 493 is a lower bound
at `s>3` (global 0–1 `π` is too strict when several `D_2` exist). The
theorem-strength count is the `s=3` Z01 column: 138 of 274 in `[6,16]`.

Nineteen UNI-alive groups die at `N ≥ 6` (5 at `s=3`, 14 at `s=4`). Typical
`s=3` pattern: `|O|=A_2` does not divide the UNI `k`, and one copy of the
NZ packet produces `N < 6` or a non-integer, two copies overfill `u`. Example
`D=80`, `m=32`, `M=[52,78]`, `V_s=3`, `u=12`, `V_2=1`, `q=1/2`, `|O|=10`:
UNI `k=12` gives `N=6`; orbit `w=10` gives `N=5`, and `w=20>12`.

Moh's six published rows are untouched in `[6,16]` except that `(84,56)
M_2=64` was already dead at `N ≥ 6`. `(84,56) M_2=72` keeps `N=10` and
loses the UNI `5`.

---

## 4. Hostile checks against the structure claims

- **Could `|O|` be 1 always, making (UNI) a theorem after all?** Only if every
  `(10)`-level has `A_j=1`. Measured on the (1)–(13) census: `A_2=1` on 50 of
  1 692 assignments; the all-`(10)` product equals 1 on 493. The `D=88` kill
  has `A_2=14`. Not a theorem.
- **Could p.150 still force one orbit of `D_1`?** No. Different Galois group
  (η-adic curve vs `t`-adic fibre of `g`). Characteristic data `{M_j,d_j}` are
  symmetric; `{V_2,…,V_{s−1}}` are per-tower.
- **Could Prop 4.4 (nonsplitting) keep the `u` slots in one `D_1`?** Only on
  the nonsplitting branch, which is *not* the tree-disc case (p.173). The search
  constructs a splitting tower down to `D_1` (Prop 5.3). One `D_1` containing
  all `u e` major roots would require `V_2=u`, which is a single assignment,
  not a theorem for every group.
- **Could (12)/(13) couple two orbits?** (12)/(13) is computed from one tower's
  `A_1`. Two orbits with different `δ_1` have different `A_1` and are not
  coupled by (12)/(13). They *are* coupled by packing into one `p` at a shared
  parent; that is the knapsack budget, not a reason to impose (UNI).
- **FALLACY-v2.** Flag/place/series: Moh `n=D` is never mixed with campaign
  `n=deg Ā_F`; the η-tree, the major tower, and the `D_1` sub-tree are kept
  apart. Per-ray: each `g`-root is charged once at its frontier (D1-PIN);
  bottom-major discs are disjoint in `D_{s−1}`. Floor/attainment: the knapsack
  asserts *existence of an integral packet*, not geometric realisation of the
  skeleton (OPEN[STAR-REALISABILITY] untouched). Carrier: Lemma 6.1(8) is a
  coordinate change on major roots, not a full-actual first-separation set.
  Pole/interior: unused. No `sat()`, no Groebner, no cap-fill of OPEN[BRANCH-ORBITS]
  or OPEN[NESTED-PACK]. No exit claim.

---

## 5. Opens

```text
OPEN[BRANCH-ORBITS]  (charged residue, NOT FILLED as a geometric existence
   question).  Number of Galois orbits of bottom-major discs, an integer in
   {1,...,u}, and the partition of Σ_B V_2(B) <= u among them.  What this
   lane fills is the *numerical* orbit-size of one disc in terms of (A_j, (10)/(11))
   and the resulting knapsack.  It does not produce a pair (f,g) realising more
   than one orbit, nor prove that a degree-minimal counterexample has one.

OPEN[NESTED-PACK]  (new; s>3 residue of the flat knapsack).  Nested partitions
   of Q_j = V_{j+1} d_j/d_{j+1} at j = s-1,...,2.  Bounded: an integer tuple
   of length s-2 <= 3 on D<=120, each part in {0,...,Q_j}.  The flat budget
   Σ |O| V_2 <= u is implied by nested packing and does not imply it.

OPEN[PROP-5.6-SHADOW]  (census-rebase; untouched).  220 groups at D<=120.
OPEN[MOH-PROGRAM]      (census-rebase; untouched).  652 excess rows at n<=100.
OPEN[V-FLOOR], OPEN[STAR-REALISABILITY]  (integration #17; untouched).
```

---

## 6. Typed block

```text
LANE          BRANCH-ORBITS v2 (Grok 4.6), 2026-09-03
SOURCE        Moh 1983 JRAM 340 pp.150/168-171/173/179-180/188/194/200-202
              at 300 dpi from 6c8847a8d8374f7d; charged (1)-(13) enumerator
              d20bf0841a1ba2b2.
PROVED-HERE   unique major D_{s-1} (Prop 4.5 + Lemma 6.1 + p.200 Thm (6)
              deg q=2 at D_s); |O|(D_1)=prod_{j=2..s-1} omega_j with
              omega_j=A_j on (10) and 1 on (11); free action on C* so NZ
              orbit size is exactly A_j; (8)-(13) per orbit; A_1 is not an
              orbit-size of discs; s=3 packing is deg p at D_2 = u
              (305/305 assignments); (12) xor (13) unless A_1=1;
              D=88 emptied in [6,16] (s=3 exact, N_orb={18} only);
              s=3 Z01 knapsack is exact (274 groups, 138 in [6,16]).
CONFIRMED     (UNI) inside one local Galois orbit (integration #17 delta (h));
              census-rebase §6 totals 1189/670/589/648 (fail-closed);
              D=48 emptied by integrality; D=66 and 78 have no skeleton;
              Moh six-row N-sets at N>=6; D=105 three groups survive.
REFUTED       (UNI) as a theorem across orbits; "all u copies of L_1 are
              conjugate discs"; using A_1 as |O|(D_1); importing p.150
              Omega-symmetry as (UNI) for the t-tree of g;
              D=105 UNI interval {6..12} on M=[28,103] Vs=5 (orbit {9}).
NOT CLAIMED   geometric realisation of any packet; nested packing at s>3
              as exact (575 is an upper bound there); Prop 5.6 as a
              numerical kill; emptiness of any D>100; any D-ceiling;
              PLACE-LEDGER identification; emptying D=88 at N>=6.
MEASURED      D<=120 (1)-(13): 1692 V-assign / 1189 groups (274 s=3).
              UNB orbit (upper bound) N>=6 : 681; [6,16] : 575
              (killed 614 vs mix's 541).  s=3 Z01 exact: 173 / 138 of
              274 (UNI 187 / 165).  All-s Z01 (s>3 lower bound): 611 /
              493.  mix-alive/UNB-dead [6,16]: 73 (18 s=3, 39 s=4,
              16 s=5).  uni-alive/UNB-dead N>=6: 19.  cap 0.
              D=105 [6,16]: 3 groups, each one NZ packet N=9 (Z01=UNB).
              D=88 [6,16] emptied (s=3 exact), N>=6 lives at 18.
              D=117 Z01 drops 4->3, not emptied.  No D>100 empties.
              Wall ~6 s one core.
OPEN          BRANCH-ORBITS (geometric existence, quantity in {1..u});
              NESTED-PACK (s>3, tuple of length s-2 <= 3);
              PROP-5.6-SHADOW; MOH-PROGRAM; V-FLOOR; STAR-REALISABILITY.
ARTIFACTS     box/branch-orbits-v2-20260903/knapsack.py  aaea3c345b1d53f5
              box/branch-orbits-v2-20260903/run.log      db82870a4c0b0f45
              Enumerator box/moh_skeleton_full.py not modified.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31327`.
- Body SHA-256:
  `519550c4fc6ddffa97e6b0c8397aa57c6da9062f923d1ae215d22a9edce4396b`.
- Frozen basis: `5f576a7a2b50da55200bff83f1bcbcff0c562b70`.
