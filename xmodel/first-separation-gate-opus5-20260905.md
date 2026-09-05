# Hostile gate: FIRST-SEPARATION (Sol) and SOURCE-SUPPORT (Astra)

**Lane:** `first-separation-gate-opus5-20260905` · **Date:** 2026-09-05

**Verdict summary.**

| item | claim | verdict |
|---|---|---|
| G1.1 | log-radius `−1` | **CONFIRMED** |
| G1.2 | no-simultaneous-drop ⇒ Moh p.194 setup; minimality used where Moh uses it | **CONFIRMED** |
| G1.3 | char 0, algebraically closed suffices | **CONFIRMED** (uses itemised below) |
| G1.4 | `(FS)` from `M_s=n−2` | **CONFIRMED** (verbatim p.194) |
| G1.5 | `v_s>u_s≥1` | **CONFIRMED** |
| G1.6 | "(1)–(13)" is a *bounded-search* list with `n≤100` in (1), `s≤5` in (6) | **CONFIRMED** (quoted below) |
| G2.a | ultrametric mean / outermost common disc contains all `P`,`Q` roots | **CONFIRMED-WITH-FIX** (fix: name `Q=T_1^ψ`) |
| G2.b | `δ_s=−(ℓ+1)/(n′−M_s−1)`; general for every licensed descendant | **CONFIRMED-WITH-FIX** (fix: cite Prop 5.1 re-run, not the printed remark) — validated 4/4 against Moh's own printed table |
| G2.c | division preserves the weight bound, incl. vanished leaders | **CONFIRMED** |
| G2.d | the OLD caps were unjustified | **CONFIRMED-WITH-FIX** — and materially sharpened: Moh *does* impose a total-degree bound in Appendix II, and it is *false* in exactly 4 of 12 h-inventories, not 12 |

No new exit-price assertion is made, so no `charge_basis` line is applicable.

## 0. Custody

A manifest was built mechanically with `awk` by joining `charged_input_<i>_basename=` and
`charged_input_<i>_sha256=` from `xmodel/first-separation-gate-opus5-20260905.run.v2` under
`lane_inputs_dir`. `sha256sum -c` returned `OK` for all five frozen files. Manifest retained at
`box/first-separation-gate-20260905/inputs.sha256`. No content mismatch. No ledger, `jc2-lean`, or
`ideation-*` file was edited. All page evidence below was read from the frozen PDF at 190–210 dpi;
printed page `N` is PDF page `N−139`. Reproduction scripts and page renders are in
`box/first-separation-gate-20260905/`.

## 1. G1 — Lemma A, step by step against the printed pages

### 1.1 The radius is `≥ −1`

Sol's elementary Newton-polygon step is valid, and the hypothesis it silently needs is printed.
For `g = y^n + a_1(x)y^{n-1}+…` with `deg a_j ≤ j`, a root of `t`-order `α < −1` makes `y^n`
strictly lowest (`−j+(n−j)α − nα = −j(1+α) > 0`), so no cancellation is possible. That argument
needs `deg = deg_y` **for `T_1^ψ` too**, which is not in Lemma 5.3's hypothesis — but Moh asserts it
on printed p.185: `deg T_1^ψ(f(x,y),g(x,y)) = deg_y T_1^ψ = −M_1 ∉ (n)`. So the step stands.

Moh's own route is independent and stronger: the proof of Prop 5.4 (printed p.183) computes

> `δ_i = 1 − (n−M_i)/(n−M_i−1) = −1/(n−M_i−1)`

as a chain of equalities from Definition 5.1(3), and the Definition–Remark on printed p.174 removes
`M_h = n−1` from the effective data ("The 'effective' characteristic pairs exclude `M_h` if
`M_h = n−1`. The last effective characteristic pair is denoted by `M_s`"). Hence `M_i ≤ M_s ≤ n−2`,
`n−M_i−1 ≥ 1`, and `δ_i ∈ [−1,0)` unconditionally. **CONFIRMED.**

### 1.2 From "no simultaneous drop" to the p.194 setup

Printed Prop 5.4 (p.183): "*Moreover if `δ_i > −1` then either `k[x,y]=k[T_1^ψ,g]=k[f,g]` or there
exists an automorphism of `k[x,y]` which reduces the degrees of `T_1^ψ(f(x,y),g(x,y))`, `g(x,y)` and
`f(x,y)` simultaneously.*" Prop 5.4 carries **no** minimality hypothesis; it is a disjunction. Sol
kills the first disjunct with non-coordinateness and the second with no-simultaneous-drop. That is
exactly where Moh uses his own hypothesis: his bounded-search item (3) reads "*`J_{x,y}(f,g)=1` and
the degrees of `f(x,y)` and `g(x,y)` can not be reduced simultaneously*". The degree drop is real:
p.185 exhibits the automorphism `x → x + a^{-l}y^l`, shows `deg g` drops by at least 1, says "similar
arguments work for `T_1^ψ`", and concludes "*if both degrees of `g(x,y)` and `T_1^ψ` drops, then the
degree of `f(x,y)` must drop too*". Minimality of `deg f + deg g` therefore excludes it, because a
source automorphism preserves `J ∈ k*` and properness of `k[f,g]`.

One point to record explicitly: the pair is first replaced by `(T_1^ψ(f,g), g)` (Prop 2.2). Minimality
transfers because p.185 gives `deg T_1^ψ(f,g) = −M_1 = deg f`, so the degree sum is unchanged.
**CONFIRMED.**

### 1.3 Hypotheses actually needed

Only "algebraically closed, characteristic zero". Char 0 enters at: Prop A.5 (printed p.207,
`D(m,n,p,q)=c ⇒ p·q` has simple roots — a Wronskian identity); the `l`-th-root-of-unity Galois
argument on p.184 and p.201 (needs `char ∤ A_{r−1}`); Newton–Puiseux itself; and divisions by `n`, `q`,
`N`. Algebraic closure enters at: Puiseux expansion, and the generic linear change realising
`deg = deg_y` for both polynomials at once (needs `k` infinite). Nothing else — no properness,
smoothness, or degree bound. **CONFIRMED.**

### 1.4 `(FS)` and `v_s > u_s ≥ 1`

Lemma 5.3 (printed p.185, verbatim): "*the smallest disc which contains all roots of `g(y)T_1^ψ(y)` is
of logarithmic radius `−1` iff `M_s = n−2` and the highest homogeneous form of `g(x,y)` has two roots
with one root having a multiplicity `(n/d_s)v_s` where `v_s` satisfies `d_s > v_s > d_s/2`*".

Printed p.194, verbatim: "*As pointed out in Proposition 5.4 and Lemma 5.3 we shall only consider the
case `M_s = n−2` and the highest homogeneous form `g(x,y)` equals `[(y−ax)^{v_s}(y−bx)^{u_s}]^{n/d_s}`
for `a ≠ b` where `u_s = d_s − v_s`.*"

Two checks the report leaves implicit and that hold: the second multiplicity is
`n − (n/d_s)v_s = (n/d_s)u_s`, and the top form cannot acquire an `x` factor because `deg g = deg_y g`
makes it monic in `y` — so there are exactly two distinct linear factors and hence exactly two
distinct **points** at infinity. Sol's refusal to call them places is correct (FALLACY-v2 flag/place).
From `d_s > v_s > d_s/2`: `u_s = d_s−v_s ∈ (0, d_s/2)`, so `1 ≤ u_s < d_s/2 < v_s`. **CONFIRMED.**

## 2. G1 — the "(1)–(13)" correction: the printed lines

Sol's correction #1 is exactly right, and here are the lines. Printed p.200 carries a **Theorem** whose
hypotheses/conclusions are numbered **(1)–(7)**: "(1) `deg f(x,y) = deg_y f(x,y) = m`,
`deg g(x,y) = deg_y g(x,y) = n`, (2) the associated characteristic data are `{M_i,d_i}` for
`i = 1,…,h`, (3) the number `M_s` is the largest one `≤ n−2`", then (4)–(7) on the tower and subdiscs.
Lemma A supplies (3) via `M_s = n−2`.

**After that theorem's proof the numbering restarts.** Printed p.200: "*One application of the theorem
and the propositions of this article is to solve the Jacobian conjecture for all polynomials of degrees
less than 100. For this purpose we consider a pair of polynomials `f` and `g` with the nonrestrictive
assumption that `f = T_1^ψ`. We shall search for the sequences of integers `{n,M_1,…,M_s}` with*

> *(1)  `deg f(x,y) = m = −M_1 < deg g(x,y) = n ≤ 100`,*
> *(2)  `m ∤ n`, `M_s = n−2`,*
> *(3)  `J_{x,y}(f(x,y),g(x,y)) = 1` and the degrees of `f(x,y)` and `g(x,y)` can not be reduced simultaneously,*"

and printed p.201: "*Note that it follows from Corollary 6.1 that `d_s ≥ 4`. A simple computation
shows that `s ≤ 5`. Combining this with Proposition 5.5 we conclude*

> *(6)  `3 ≤ s ≤ 5`,  `d_s ≥ 4`.*"

So `n ≤ 100` is literally item (1) and `s ≤ 5` is literally item (6). The dependence is not incidental:
`d_{r+1}` is a proper divisor of `d_r` and `d_s ≥ 4`, so `d_2 ≥ 2^{s−2}d_s ≥ 2^s`, while `d_2 = gcd(n,m)`
divides `n` properly, giving `2^s ≤ n/2 ≤ 50` — i.e. `s ≤ 5` **is** the `n ≤ 100` cap. A cap-free census
cannot cite item (6). **CONFIRMED**, and `OPEN[CENSUS-COVERAGE-ALL-DEGREE]` is correctly typed.

Sol's transcription of (4)–(13) matches the print, including the internal inconsistency it flags: item
(4) reads "*`{n,M_1,…,M_s}` is the part of characteristic data of `(f,g)` which are less than `n−2`*",
which cannot sit beside item (2)'s `M_s = n−2`. Leaving it unrepaired is the right call.

## 3. G2 — the source-support theorem

### 3.a Ultrametric mean and the outermost common disc — CONFIRMED-WITH-FIX

Printed p.179, immediately after Definition 5.1: "*Note that Proposition 5.1, which has been proved,
implies that the minimal disc `D_s` which contains all roots of `g(y)∏_{i=1}^h T_i^ψ(y)` satisfies the
criteria (1),(2),(3) and (4).*" So `D_s` does contain **all** roots of `g` and of every `T_i^ψ` — the
containment Astra needs, and at the outermost (weakest, hence safest) radius `δ_s`.

The centre question is a non-issue: in an ultrametric every point of a disc is a centre. `η ∈ k[x]`
because `Q` is monic in `y`; `η − A = N^{-1}Σ(ρ_j − A)` has `ord ≥ δ_s` since `ord N = 0` in char 0;
hence `ord(ρ−η) ≥ δ_s` for every root `ρ` of `P` and of `Q`. `φ=(x,y+η(x))` has determinant 1, preserves
polynomiality, `y`-monicity, both `y`-degrees, `J = cx^ℓ`, and all pairwise root contacts (hence all
disc radii and all characteristic data). This is a genuine group element, as FALLACY-v2 requires.

**Fix.** The claim "`Q` is in the product `g·∏T_i^ψ`" is used but not named. It is Moh's own
nonrestrictive normalisation `f = T_1^ψ` (printed p.200), which is Jacobian-free of cost since
`J(P, Q+p(P)) = J(P,Q)`. It should be stated as a hypothesis of the theorem, because the chart's `h` is
built from *this* `Q`. All twelve campaign rows are consistent with it: every class datum has
`M_1′ = −m′` (e.g. `(24,16; −12,−2,5)` is `M′ = (−16,−12,−2,5)`), which is precisely the assertion
`deg_y T_1^ψ = m′`.

### 3.b The terminal equation — CONFIRMED-WITH-FIX, plus a 4/4 printed validation

Printed p.171 Remark, verbatim: "*With a verbatim proof, for a slightly general Jacobian condition of
the following form (cf. Appendix II) `J_{x,y}(f(x,y),g(x,y)) = x^l`, **Proposition 4.6** is still valid
with the condition (3) replaced by the following: (3)\* `λ = (−1−l+δ)/(n−m_r) < (−1−l+δ)/(n−m_i)`.*"

The remark licenses **Prop 4.6**, not Prop 5.1. Astra's `δ_s = −(ℓ+1)/(n′−M_s−1)` is obtained by
re-running Prop 5.1's proof (printed p.174, which invokes Props 4.4 and 4.6) under (3)\*. That is a
sound but *unprinted* step and must be cited as such — Prop 5.1(2) as printed gives only the `ℓ=0`
instance `δ_h = −1/(n−M_h−1)`.

**It is nevertheless validated 4/4 against Moh's own printed numbers.** Appendix II, printed p.207,
tabulates descendants with `u_3 = d_3 − v_3 = 1`:

| `n′` | `m′` | `M_2` | `V_2` | printed `δ_2` | `−(ℓ+1)/(n′−M_2−1)` | Jacobian |
|---|---|---|---|---|---|---|
| 16 | 12 | 13 | 3 | `−1` | `−2/2 = −1` ✓ | `x` |
| 21 | 14 | 16 | 2 | `−1/2` | `−2/4 = −1/2` ✓ | `x` |
| 21 | 14 | `[18]` | `[5]` | `[−1]` | `−2/2 = −1` ✓ | `x` |
| 15 | 10 | 11 | 3 | `−1` | `−3/3 = −1` ✓ | `x²` |

All four entries match exactly (`box/first-separation-gate-20260905/verify_gate.json`). This is a
printed, independent confirmation that the `ℓ`-generalised terminal formula is Moh's.

**Generality.** The theorem *is* general, not fibre-specific. `ℓ ≥ 0` gives `ℓ+1 ≥ 1`; the p.174
Definition–Remark forces `M_s ≤ n′−2`, so `n′−M_s−1 ≥ 1`; and an effective terminal always exists
because `M_1 = −m′ < 0 < n′−1`. Hence `δ_s ≤ −(ℓ+1)/(n′−1) < 0` for **every** licensed descendant, at
every degree. The only per-row inputs are `(n′, M_s′, ℓ)`.

### 3.c Division preserves the weight bound — CONFIRMED

With `w(x^b y^a) = b + d·a`, "`deg_x[y^a]F ≤ ⌊d(L−a)⌋` for all `a`" is equivalent to `w`-deg `F ≤ dL`,
and `y^L` attains it. Monic division by `h` (`w`-deg `≤ dK`): a leading term `L_r(x)y^r`, `r ≥ K`, gives
a quotient term of weight `≤ (dL−dr) + d(r−K) = d(L−K)`, whose product with `h` has weight `≤ dL`;
subtraction cannot raise the weight and strictly drops the `y`-degree. Since `h` is monic in `y` there is
**no** vanishing leader to branch on — the specialisation worry FALLACY-v2 raises is structurally absent,
and a vanished `L_r` simply advances to the next `y`-degree. Iterating gives `w`-deg `α_i ≤ i·dK` from
`P = h^e + Σα_i h^{e−i}`, i.e. exactly `G_i`.

The approximate-root induction is also right: matching `y^{qK−j}` in `Q − h^q` gives
`qH_j = [y^{qK−j}]Q − (\text{products } H_{i_1}\!\cdots H_{i_r}, Σi_k = j)`, and
`Σ⌊d i_k⌋ ≤ ⌊dΣi_k⌋ = ⌊dj⌋`, so `deg_x H_j ≤ ⌊dj⌋`, i.e. `G_1`. `β_1 = 0` follows from
`deg_y(Q−h^q) < (q−1)K`. Division by `q` is by a unit in char 0. **CONFIRMED.**

Soundness of the delivered chart: `S_i = D_i ∪ G_i ⊇ G_i ⊇` the true (translated) support, so the union
is a valid over-approximation and a kill on it is a kill. Note this makes `D_i` decorative — the proved
chart is `G_i` alone, which for five of the six classes is *smaller* than `D_i`.

### 3.d The old caps — CONFIRMED-WITH-FIX, and sharpened

The negative control reproduces exactly. `h = y(y−x²)³ = y⁴ − 3x²y³ + 3x⁴y² − x⁶y` has weights
`(9, 19/4, 1/2, −15/4)` at `δ₁ = 9/4` and `(2, −1/2, −3, −11/2)` at `δ₁ = 1/2`; minima `−15/4` and
`−11/2` are precisely the two printed `B_safe` values, while its total degree is 7 > 4 = K, and `x²y³`
is D1-allowed on both. So "monic + D1 order floor ⇒ total degree ≤ K" is **refuted**. Astra's own caveat
that this is not a realised Jacobian pair is correct and necessary.

**The gate's extra question has a positive answer: Moh does impose a total-degree bound, in Appendix II,
and the gate missed it.** Printed p.207 states the reduced coefficient counts as 244, 373, 202 for the
descendants `(16,12)`, `(21,14)`, `(15,10)`. Those are exactly
`\binom{n′+2}{2} + \binom{m′+2}{2}`: `153+91 = 244`, `253+120 = 373`, `136+66 = 202` — three exact hits.
The same model reproduces the source counts `(64,48) → 3370` and `(84,56) → 5308` exactly, and Moh's own
introduction range "3370 to 7328" (`(99,66) → 7328`); the Appendix's `4352` and `7348` are digit slips
for `4252` and `7328`, and its "(64, 68)" is a slip for `(64,48)`, since `(64,48)` is what both `3370`
and the `(16,12)` descendant require. So Moh counts descendant coefficients under `total degree = y-degree`.

That bound is not an assumption in his three rows — it is a *theorem*, by exactly Astra's own argument:
`d = −δ_s = 1` in rows 1 and 3, and `1/2` in row 2, so `deg_x[y^a]F ≤ ⌊d(L−a)⌋ ≤ L−a`. The campaign's
error was importing `d = 1` (and the p.194 source picture "`(n/d_s)v_s` roots of `ord ≥ 0`,
`(n/d_s)u_s` roots of `ord = −1`", printed p.194 eqs (8),(9)) onto descendants whose own outer radius is
`−d ≠ −1`. Indeed `deg_x[y^a]h ≤ min(K−a, K−V_2)` is *precisely* what "`V_2` roots of `ord ≥ 0` and
`K−V_2` roots of `ord ≥ −1`" yields — the two old caps are that one unproved two-radius hypothesis.

**How much is actually wrong.** Independent recomputation of `d = (ℓ+1)/(n′−M_s′−1)` and of `G_1` from
the class data alone reproduces Astra's `support-completion.json` on **12/12 fibres**, for both `d` and
`|G_1|`. Testing `G_1 ⊆ {b+a ≤ K, b ≤ max(K−V_2,0)}` per fibre:

| class `(n′,m′; M′; ℓ; s′)` | `K` | `d` | `\|G_1\|` | fibres with `G_1 ⊄` old caps |
|---|---|---|---|---|
| `(16,12; 6,13; 3; 3)` | 4 | **2** | 24 | **all 3** (V1_1, V1_3: 11 escapees; V4_3: 20) |
| `(18,12; 2,9; 2; 3)` | 6 | 3/8 | 11 | none |
| `(24,16; −12,−2,5; 1; 4)` | 8 | 1/9 | 8 | none |
| `(24,16; 12,17; 1; 3)` | 8 | 1/3 | 17 | none |
| `(24,18; −15,14; 1; 3)` | 6 | 2/9 | 8 | none |
| `(24,18; 9,20; 1; 3)` | 6 | 2/3 | 18 | **V4_9 only** — `(3,0),(4,0),(3,1)` |

So at the `h` block the old caps are *false* in 4 of 12 fibres, and in the other 8 they are a sound (if
unproved) over-approximation of the proved-necessary `G_1`. The two caps fail for different reasons:
`b+a ≤ K` fails exactly when `d > 1`, i.e. `ℓ+1 > n′−M_s′−1` — only the `(16,12; 6,13; ℓ=3)` class here;
`b ≤ K−V_2` has no outer-disc derivation at all and fails additionally at `9_20/V4_9`, where `d = 2/3 ≤ 1`.
This refines Astra's blanket "REPAIRED ×11" into a checkable regression list. It does **not** clear the
other 8 fibres, because the `α`/`β` blocks were not tested here and Astra reports α/β additions on every
fibre but the `s′=4` control (e.g. `m15_14/V1_9` gains `a2/b1` with an unchanged `h`).

## 4. Residual OPENs after this gate

- `OPEN[PROP51-ELL-EXTENSION]` (new, small): write out Prop 5.1's proof under p.171's (3)\*. Currently
  a re-run claim with a 4/4 printed numerical check, not a printed theorem.
- `OPEN[Q-IS-T1]` (new, small): record `Q = T_1^ψ(P)` as a hypothesis of the source-support theorem;
  it is what puts `Q`'s roots inside `D_s`. Consistent with all 12 rows (`M_1′ = −m′`) but unproved
  for a generic licensed descendant.
- `OPEN[OLD-CAP-REGRESSION-αβ]` (new): repeat the `G_i ⊆ old` test on the `α_i`/`β_i` blocks. Only then
  is the set of regressed banked kills determined; the `h`-block answer is the 4 fibres above.
- Sol's `OPEN[CENSUS-COVERAGE-ALL-DEGREE]`, `OPEN[SKELETON-DECORATION]`,
  `OPEN[SPLIT-WINDOW-CLASSIFICATION]`, `OPEN[SPLIT-TO-JOINT-MAP]`, `OPEN[U-NEGATIVE-CHART]`,
  `OPEN[DESCENT-STATE-S>2]`, `OPEN[K4-SHAPE-AND-UNIFORM-KILL]` stand as typed. This gate touches none
  of them; Lemma A closes only the one-point-at-infinity leak, and the source-support theorem closes
  only the support obligation, on a chart family whose computational verdict remains `0/6 killed`.

## 5. What may now be cited

Lemma A may be promoted as stated, with the two additions of §1.1 and §1.2 (the p.185 `deg T_1^ψ`
identity; the degree-sum invariance of the `f → T_1^ψ` replacement). Its "(1)–(13)" caveat is exactly
right and must travel with it.

The source-support theorem may be promoted as a **general, all-degree** necessary-support theorem for
licensed descendants, once `Q = T_1^ψ` is named as a hypothesis and the Prop 5.1 `ℓ`-extension is
written out. Its chart `S_i = D_i ∪ G_i` is a sound over-approximation; `G_i` alone is the proved part.
Astra's "the old caps are unjustified" is upheld as a *derivability* claim, and is now pinned as a
*truth* claim to 4 of 12 `h`-inventories, with Moh's Appendix II counts identified as the printed place
where the total-degree bound does appear — legitimately there, because those three descendants have
`d ≤ 1`.

## References consumed

- T. T. Moh, *J. Reine Angew. Math.* **340** (1983) 140–212: printed pp. 171, 173–174, 179, 183–186,
  194, 197, 200–201, 207 (PDF pages `N−139`), read as rendered page images.
- `first-separation-lemma-sol56-20260905.md` §§0–3, 8.
- `moh-hsupport-gate-astra-20260905.md` §§1–5, 8.
- `prop54-minimality-opus5-20260905.md` (`δ_i = −1/(n−M_i−1)` unconditional; two-point minimal
  counterexample).
- `FALLACY-v2.md` — flag/place, floor/attainment, variable/ring map, raw remainder degree.
- Recomputation: `box/first-separation-gate-20260905/verify_gate.py`, `verify_gate.json`,
  `inputs.sha256`, page renders `pg*.png`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19299`.
- Body SHA-256:
  `6144f7cc3688d1fe3a997d05f8b6046e91b4bb858be35d8a307d4182c106ddb3`.
- Frozen basis: `c551228927d8693614b68b8f9685b5c6ce3778d5`.
