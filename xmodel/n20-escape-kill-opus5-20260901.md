# N20-ESCAPE — kill the ramified-nonprimitive-cover packet

Lane: OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]
Model: Opus 5 · Date: 2026-09-01 · Desk-scale exact reasoning, no CAS.

## 0. Provenance and input verification

## 1. Promoted statements consumed (typed inventory)

## 2. The N=20 escape packet, unpacked

## 3. The pointwise dictionary [Z-6.5b], re-derived

## 4. Riemann–Hurwitz for h_l : l' -> D~ and the ramification budget

## 5. The corr_l ceiling: general inequality

## 6. Re-running the N=20 budget

## 7. General-N consequence

## 8. Typed conclusions and OPEN items

## 9. Sources

Frozen inputs hashed with `shasum -a 256` before reading; all three match the
charge exactly:

```text
621f1356b3b5290e32c2f2bf689b4d9a49412cb852066886a34b580366cb1652  b0-all-n-eta-criticality-sol56-20260831.md
f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46  b0-all-n-hostile-review-grok46-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Below **ALL-N**, **REV**, **COORD** denote those three in charge order.

Primary literature fetched from the local `refs/` tree and rehashed at
execution; both agree with the hashes recorded in ALL-N §1 and REV §0:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

Text of Orevkov was read directly with `pdftotext -layout` (pp. 2–9). No CAS,
no computation of uncertain duration, no canonical ledger or charged file
edited, `jc2-lean` not inspected. `FALLACY-v2` in force. No `charge_basis`
line: no new exit price is asserted.

**Verdict up front.** The N=20 packet (4.9) is **DEAD**, and it dies by exactly
the arithmetic the charge anticipated — but at a different place than the charge
guessed. The naive count ("16 units cannot sit on a ramification divisor of
degree 2") is *not* the kill: `corr_l` legitimately contains local-multiplicity
excess that ramification degree does not bound. The kill is a **concentration
theorem**: `corr_l` is supported at *one* point of `π(l)`, namely the image of
the contracted `L_C` chain, and never spreads over two. Packet (4.9) requires
two distinct correction sites carrying 8 each; only one exists, so all 12 units
of excess land on a single physical fibre and violate `K_p ≤ d = 6`. The same
theorem re-runs the whole budget: the ramified-escape frontier moves from
`N ≥ 20` to **`N ≥ 26`**. The lane's prize (B0 under H2 at every degree) is
*not* attained; what remains is typed in §8.

## 1. Promoted statements consumed (typed inventory)

Consumed as promoted, not re-derived:

- **[P1] Orevkov budget.** `Σ_l (μ_l + corr_l) = N − 1`, `corr_l = Σ_x (μ_x − μ_l)`
  (ALL-N (1.1); primary = Orevkov Lemma 4.2 eq. (4), `refs/jc86.pdf` p. 7).
- **[P2] H2 strictness.** `A_F` irreducible ⟹ `Σ μ_l ≤ N − 2`, `Σ corr_l ≥ 1`
  (COORD-lineage, ALL-N (1.2)).
- **[P3] Fibre/flatness count.** `a + Σ_l s_l μ_l = N`, `a ≥ 1` (ALL-N (1.3)).
- **[P4] [Z-6.5b] pointwise dictionary.** `μ_x > μ_l ⟺ dφ_l(x) = 0`; and
  `μ_l = 1 ⟹ dφ_l ≠ 0` everywhere (ALL-N (1.4); Żołądek Prop. 6.5(b)).
- **[P5] Trivial-dicritical package** (ALL-N §2, REV §2, CONFIRMED): if some
  dicritical has `μ_0 = 1` then `s_0 = 1`, `D̃ ≅ A¹` (H3 free), and the
  normalization `η : D̃ → D` is **immersive everywhere**; every reduced branch of
  `D` is smooth and every singular point of `D` is multibranch.
- **[P6] Euler identity + smooth-stratum covering lemma.** `F` restricted to
  `F^{-1}(D − Σ) ∩ A²` is an `a`-sheeted covering of `D − Σ`; hence
  `(N−a)χ_c(D−Σ) = N−1−Nσ+A_Σ` and ALL-N (4.1) (REV §4.1, CONFIRMED).
- **[P7] Constant-multiplicity fibre identity.** `a_p + r_p W + K_p = N`
  (ALL-N (4.5), REV §4.3, CONFIRMED), with `W = N − a = Σ s_l μ_l`,
  `d = 2a − N`, and `2a > N` under [P5] (REV §4.1).
- **[P8] Corrected-correction formula.** `corr_l = μ_l(s_l − 1) + Σ_t k_t`,
  `k_t = μ_t − e_t μ_l ≥ 0`, `k_t = 0` off ramification of `h_l`
  (ALL-N (4.4), REV §4.2, CONFIRMED).

Re-derived here from primary source, **not** consumed from the charged reports:

- **[R1] Orevkov Lemma 2.1** (`refs/jc86.pdf` p. 2, verbatim): each connected
  component `K` of `L_FC` (a) meets `L_∞` at a unique point `p` with
  `f(K − p) ⊂ C²`; (b) has **linear** graph with `p` on an **endpoint**
  component; (c) that endpoint is the unique `L_F` component `l = l_k`, and
  `l_1, …, l_{k−1} ⊂ L_C`. Also from the same page: the components of `L` are
  nonsingular rational curves meeting **transversally and at most pairwise**,
  and the graph of `L` is a **tree**.
- **[R2] Orevkov Lemma 3.1** (`refs/jc86.pdf` p. 4, verbatim): if `g = (u,v)`
  is holomorphic near `0 ∈ C²` with finite fibres, `g(0,0) = (0,0)`,
  `∂(u,v)/∂(x,y) ≠ 0 for y ≠ 0`, and `g({y=0}) ⊂ {v=0}`, then in suitable
  holomorphic coordinates `u = x′`, `v = y′^k`.
- **[R3] Orevkov §4 multiplicity** (p. 6): `μ_x φ` = largest `k` such that every
  neighbourhood of `x` contains `k` points with a common image; `f^* : X̃^* → X^*`
  has constant multiplicity `N`, where `π : X̃ → X̃^*` contracts `L_∞` to `∞` and
  each connected component of `L_C` to a single point. The correction sum in
  [P1] runs over `x ∈ π(l) − {∞}`.

## 2. The N=20 escape packet, unpacked

The packet is the equality stratum of ALL-N (4.8). Its full numeric content,
reconstructed from [P1]–[P8]:

| quantity | value |
|---|---|
| `N` (geometric degree) | 20 |
| `W = N − a = Σ s_l μ_l` | 7 |
| `d = 2a − N = a − W` | 6 |
| `a` (generic affine fibre over `D`) | 13 |
| `R = Σ_l (s_l − 1)` | 2 |
| dicriticals `(μ_l, s_l, corr_l)` | `(1,1,0)` and `(2,3,16)` |
| `Σ_l (μ_l + corr_l)` | `1 + 0 + 2 + 16 = 19 = N − 1` ✔ |

There is one trivial dicritical `l_0` (which by [P5] forces `s_0 = 1`,
`D̃ ≅ A¹`, `η` immersive) and one carrier `l_1` with `μ_1 = 2`, `s_1 = 3`,
carrying the whole correction `corr_1 = 16`.

By [P8], `corr_1 = μ_1(s_1 − 1) + Σ_t k_t = 2·2 + Σ_t k_t`, so the packet needs

```text
Σ_t k_t = 12.
```

REV §4.5 pins the only arrangement compatible with the promoted inequalities:
the cubic `h_1 : A¹ → D̃ ≅ A¹` must have **two distinct simple critical points**
with **distinct critical values**, each landing on a two-branch singular point
`p_i ∈ Sing D` with `r_{p_i} = 2`, `a_{p_i} = 0`, `k_i = 6`, `μ_{t_i} = 10`, and
correction `8` apiece. REV explicitly records the alternative and rejects it:
"A totally ramified cubic (`e=3` at one point, still `R=2`) has only one
critical image and fails (4.7)."

That last sentence is the hinge of this lane. REV rejected total ramification as
*one of two* numerically admissible shapes. §4 below shows it is the **only**
admissible shape — that two distinct critical points on `l'` are geometrically
impossible — and the packet therefore has no surviving arrangement.

### 2.1 The charge's naive count does not close, and why

The charge proposes: `h_1 : l′ ≅ A¹ → D̃ ≅ A¹` of degree 3 has, by
Riemann–Hurwitz on the projective completions, finite ramification of total
degree `Σ_t (e_t − 1) = s_1 − 1 = 2`; so "16 units cannot sit on a ramification
divisor of total degree 2".

This is **not** a valid kill, and the reason is exactly the FALLACY-v2
carrier/attainment separation. `corr_l` is a sum of **local multiplicity
jumps** `μ_x − μ_l`, and `μ_x` is the local degree of `f^*` at `x` in the sense
of [R3] — the number of nearby points with a common image. Ramification of `h_l`
controls only the part `μ_l(s_l − 1)` coming from the collision of `e_t` sheets
of the *parametrization*; the residue `k_t = μ_t − e_t μ_l` counts preimages
supplied by the *surface* germ at `x` (affine branches escaping to infinity
along the contracted configuration), and nothing in Riemann–Hurwitz bounds it.
Indeed a jump of `μ_t = 10` at a point with `e_t = 2`, `μ_l = 2` is not
contradicted by any ramification count: `k_t = 6` is a fibre-budget quantity,
governed by [P7], not by RH.

So the arithmetic route the charge names is genuinely blocked. The correct
attack is not "how many units fit on the ramification divisor" but **"how many
distinct sites can carry a jump at all"** — and the answer, from Orevkov's own
§2–§4, is one per dicritical.

## 3. The pointwise dictionary [Z-6.5b], re-derived

Fix the notation of [R1]/[R3]. `X̃` is the regularizing blow-up, `L = X̃ − C̃²`
its boundary (a tree of nonsingular rational curves, pairwise transversal),
`L_∞ = f^{-1}(P¹×P¹ − C²)`, `L_FC = L − L_∞`, `L_C ⊂ L_FC` the contracted
components, `L_F = L_FC − L_C` the affine-image dicriticals. For a dicritical
`l ⊂ L_F` in the chain `K : l_1 — ⋯ — l_k` of [R1], `l = l_k`, and

```text
l′ := l ∩ f^{-1}(C²) = l_k − {p} ≅ A¹        ( [R1](a),(b) )
```

where `p = K ∩ L_∞` is the unique boundary meeting point. Write `φ_l = f|_{l′}`,
`s_l = deg φ_l`, `φ_l = η ∘ h_l` (ALL-N (2.1)–(2.2), CONFIRMED), and, under
[P5], `η` is immersive at every place.

**The correction sites are the points of `π(l) − {∞}`, and they are of exactly
two kinds.** By [R3], `π` contracts each connected component of `L_C` to a single
point. By [R1](b),(c), the `L_C` part of `K` is the connected linear chain
`l_1 — ⋯ — l_{k−1}`, attached to `l` at the single point `t_0 := l_k ∩ l_{k−1}`.
Hence

```text
π(l) − {∞}  =  ( l′ − {t_0} )  ⊔  {x_0},        x_0 := π(l_1 ∪ ⋯ ∪ l_{k−1}) = π(t_0),
```

and `x_0` is the **only** point of `π(l) − {∞}` at which `X̃^*` can fail to be
smooth (Orevkov, p. 8: "we may assume all points of `π(L_C)` are singular points
of `X̃^*`"). If `k = 1` — no `L_C` part — then `π(l) − {∞} ≅ l′ ≅ A¹` consists
entirely of smooth points.

**Lemma 3.1 (no jump off `x_0`).** *Let `x ∈ π(l) − {∞}`, `x ≠ x_0`. Then
`μ_x f^* = μ_l f^*` and `φ_l` is a nonsingular embedding near `x`; in particular
`e_x = 1` and `k_x = 0`.*

*Proof.* Identify `x` with the corresponding `t ∈ l′ − {t_0}`. By [R1] the
components of `L` meet pairwise and transversally, and by [R1](b) `l_k` meets
`l_{k−1}` only at `t_0` and `L_∞` only at `p ∉ l′`. So `l` is the **only**
component of `L` through `t`: choose local holomorphic coordinates `(x,y)` at
`t` with `l = {y = 0}` and `L ∩ U = {y = 0}` for a small neighbourhood `U`.
Let `(u,v)` be target coordinates at `f(t)` chosen so that `{v = 0}` is the
smooth image branch — legitimate because `η` is immersive at `h_l(t)` by [P5],
so the image germ of `φ_l` at `t` is a smooth curve germ. Then
`g := f|_U = (u,v)` satisfies `g({y=0}) ⊂ {v=0}`.

Fibres of `g` are finite near `t`: the only curve germ through `t` contracted by
`f` would have to lie in `L` (on `C̃²` the map is a local biholomorphism), and
`l` is not contracted.

The Jacobian hypothesis is exactly the Keller condition. On `U − L = U ∩ C̃²`
the coordinate chart `(x,y)` is a biholomorphism onto its image in `C̃²`, so
`∂(u,v)/∂(x,y) = ∂(f_1,f_2)/∂(X_1,X_2) · ∂(X_1,X_2)/∂(x,y)` is a product of two
nonvanishing factors, where `(X_1,X_2)` are the affine coordinates of `C̃²`.
Hence `∂(u,v)/∂(x,y) ≠ 0` for `y ≠ 0` near `t`.

[R2] (Orevkov Lemma 3.1) now applies verbatim and gives coordinates in which
`g(x′,y′) = (x′, y′^k)`. Restricted to `l = {y′ = 0}` this is `x′ ↦ (x′,0)`, a
nonsingular embedding, so `dφ_l(t) ≠ 0` and `e_t = 1`; and the local degree of
`(x′,y′) ↦ (x′, y′^k)` at the origin is `k`, the same value it takes at all
nearby points of `l`, so `μ_t f^* = μ_l f^*` and `k_t = 0`. ∎

This is the sharp form of the promoted `[O-5.2]`/[P4] package. [P4] gives the
equivalence `μ_x > μ_l ⟺ dφ_l(x) = 0`; Lemma 3.1 identifies *where* the right
side can hold. Combining, with `η` immersive so that `dφ_l(x) = 0 ⟺ dh_l(x) = 0`:

> **Corollary 3.2 (concentration).** For every affine-image dicritical `l`,
> ```text
> corr_l = μ_{x_0} f^* − μ_l f^*        (a single jump, at x_0 = π(L_C-chain of l)),
> ```
> and `corr_l = 0` whenever `l` has no `L_C` part. Moreover `h_l` is unramified
> on `l′ − {t_0}`.

Note the direction of the logic: Corollary 3.2 does **not** consume the promoted
"correction support = ramification support of `h_l`" statement and then refine
it; it re-derives the support from [R1]+[R2] and finds it strictly smaller than
that statement allows. The promoted statement is true but not sharp, and ALL-N
§4 and REV §4.5 both budget as if the correction could spread over the whole
ramification support. It cannot.

## 4. Riemann–Hurwitz for `h_l` and the total-ramification normal form

> **Theorem 4.A (rigidity of the correction carrier).** Assume H2, and assume
> some dicritical has `μ_0 = 1` (so [P5] holds: `D̃ ≅ A¹`, `η` immersive). Let
> `l` be an affine-image dicritical. Then exactly one of:
>
> 1. `s_l = 1` (`h_l` an isomorphism) and `corr_l = 0`; or
> 2. `s_l ≥ 2`, `μ_l ≥ 2`, `l` carries a nonempty `L_C` chain, and, after affine
>    coordinate choices on `l′ ≅ A¹` and `D̃ ≅ A¹`,
>    ```text
>    h_l(t) = (t − t_0)^{s_l},
>    ```
>    i.e. `h_l` is **totally ramified at the single point** `t_0 = l ∩ L_C`,
>    with `e_{t_0} = s_l`, and it has no other critical point.

*Proof.* `h_l : l′ ≅ A¹ → D̃ ≅ A¹` is a polynomial map of degree `s_l`
(ALL-N (2.1)–(2.2)). Its critical points are the roots of `h_l′`, a polynomial
of degree `s_l − 1`. By Corollary 3.2 (with `η` immersive, so
`dφ_l = dη ∘ dh_l` and `dh_l(t) = 0 ⟺ dφ_l(t) = 0`), Lemma 3.1 forces
`dh_l ≠ 0` on `l′ − {t_0}`. Hence every root of `h_l′` is `t_0`:
`h_l′(t) = c(t − t_0)^{s_l − 1}`, so `h_l(t) = c′(t − t_0)^{s_l} + z_0`. Absorb
`c′` and `z_0`.

If `s_l = 1` there is no critical point, so by [P4] no jump anywhere, and
`corr_l = 0`. If `s_l ≥ 2` then `h_l` is ramified, necessarily at `t_0`, so
`t_0` exists, i.e. `k ≥ 2` in [R1] and the `L_C` chain is nonempty. Finally
`μ_l = 1` would give, by [P4], `dφ_l ≠ 0` everywhere, hence `dh_l ≠ 0`
everywhere, hence `s_l = 1`; so `s_l ≥ 2 ⟹ μ_l ≥ 2`. ∎

Two remarks fix the scope.

**(i) Where the two-critical-point picture came from.** REV §4.5 derived "two
distinct simple critical points" *backwards*, from the equality conditions in
the budget, and checked only that it was not excluded by the promoted
inequalities. It is excluded by the geometry: two critical points would require
two distinct points of `l′` at which the boundary `L` fails to be smooth, and
[R1](b) supplies exactly one. Neither ALL-N nor REV used [R1](b) at this
strength — both used [R1] only through `l′ ≅ A¹` and through the
"`ε ≡ 0`" fibre-separation statement.

**(ii) An independent cross-check of Lemma 3.1 not using [R2].** The same
conclusion follows from a direct Jacobian computation, which is worth recording
because it exhibits the mechanism. At a boundary-smooth `t ∈ l′` take `(u,v)`
with `l = {v=0}`, target `(x,y)` with the smooth image branch `{y=0}`. Then
`Y := y∘f` vanishes on `l` to order exactly `μ_l` (the generic local degree), so
`Y = v^{μ}B` with `v ∤ B`; and `X := x∘f` satisfies `X(u,0) = u^{e}·unit`
because `η` is immersive. A one-line expansion gives

```text
Jac(X,Y) = v^{μ−1}·G,    G = μ X_u B + v (X_u B_v − X_v B_u).
```

Since `f^*(dx∧dy) = dX_1∧dX_2` on `C̃²` (Keller), `div(Jac)` in this chart is
effective and supported on `L ∩ U = {v=0}`, so `G = v^m·G̃` with `G̃(t) ≠ 0` and
`m ≥ 0`. If `m ≥ 1` then `G|_{v=0} = μ X_u(u,0)B(u,0) ≡ 0`, forcing `v | B`, a
contradiction. So `m = 0`, i.e. `μ X_u(0,0)B(0,0) ≠ 0`, i.e. `X_u(0,0) ≠ 0`,
i.e. `e = 1`. The toy map `(u,v) ↦ (u², v²)` shows the mechanism is sharp: it
has `μ_l = 2`, `e = 2` at the origin, and Jacobian `4uv`, whose extra branch
`{u=0}` is precisely the second boundary component that [R1](b) forbids away
from `t_0`.

**Consequence for the corrected correction formula.** Substituting into [P8],
for every `l` with `s_l ≥ 2`:

```text
corr_l = μ_l (s_l − 1) + k_l,    k_l := k_{t_0(l)} = μ_{x_0(l)} f^* − s_l μ_l ≥ 0,
```

with `k_l` the *only* nonzero `k`-term on `l`. Equivalently
`corr_l = μ_{x_0(l)} f^* − μ_l`: the whole correction of a carrier is one local
jump at one point.

## 5. The `corr_l` ceiling: the general inequality

Throughout: H2, `μ_0 = 1` for some dicritical, hence [P5]; `W = Σ_l s_l μ_l`,
`a = N − W`, `d = 2a − N = a − W > 0` by [P7]. Set

```text
b  = #{ l : μ_l = 1 },        b ≥ 1
q  = #{ l : μ_l ≥ 2 }
q′ = #{ l : s_l ≥ 2 }        (⊆ the μ_l ≥ 2 set, by Theorem 4.A)
```

**(a) At most `q′` correction sites, hence at most `q′` critical images.** By
Corollary 3.2 each `l` carries at most one site `x_0(l)`, and by Theorem 4.A a
site exists only when `s_l ≥ 2`. Let `P = { f^*(x_0(l)) : k_l > 0 }` be the set
of physical images actually carrying excess. Then `|P| ≤ q′`, with equality only
if all `q′` carriers have `k_l > 0` and pairwise distinct images.

**(b) Every point of `P` is a singular point of `D`.** Suppose `p ∈ P` were a
smooth point of `D`. Pick a disc `Δ ⊂ D − Σ` around `p`. By [P6] the map
`F : F^{-1}(Δ) ∩ A² → Δ` is an `a`-sheeted covering, in particular **proper**;
so no affine branch escapes to infinity over `Δ`. But `k_l > 0` means precisely
that the local degree at `x_0(l)` exceeds the `s_l μ_l` contributed by the
`e = s_l` colliding parametrization sheets, and the surplus is realized by
affine preimages of points `q ∈ Δ` lying arbitrarily close to the contracted
configuration — i.e. escaping to infinity as `q → p`. Contradiction. Hence
`P ⊆ Σ = Sing D`, and by [P5] every `p ∈ P` is multibranch: `r_p ≥ 2`.

**(c) Per-image ceiling.** [P7] at `p ∈ P` gives
`K_p = N − r_p W − a_p ≤ N − 2W = d`, using `r_p ≥ 2` from (b) and `a_p ≥ 0`.

**(d) Global excess.** ALL-N (4.6), CONFIRMED at REV §4.3, gives
`Σ_{p∈Σ} K_p = a − 1`. By (b) no excess sits off `Σ`, so
`Σ_{p∈P} K_p = a − 1`.

Combining (a), (c), (d):

> **Theorem 5.A (the corrected budget inequality).**
> ```text
> a − 1  ≤  q′ · d,        i.e.   W + d − 1 ≤ q′ d.          (5.1)
> ```

This replaces ALL-N (4.7)–(4.8), where `q′` was replaced by the strictly larger
`R = Σ_l (s_l − 1)`. The gap between the two is exactly the concentration
theorem: `R` counts ramification *with multiplicity over all critical points*,
`q′` counts *carriers*. Since a carrier with `s_l = 3` has `R`-weight `2` but
only one site, the substitution is not cosmetic.

**(e) The complementary weight bound.** Each `l` with `μ_l = 1` has `s_l = 1`
and weight `s_l μ_l = 1`; each `l` with `μ_l ≥ 2, s_l = 1` has weight `≥ 2`;
each of the `q′` carriers has `μ_l, s_l ≥ 2` and weight `≥ 4`. Hence

```text
W ≥ b + 2(q − q′) + 4q′ = b + 2q + 2q′ ≥ 1 + 4q′       (since b ≥ 1, q ≥ q′),
```

so

```text
q′ ≤ ⌊(W − 1)/4⌋.                                       (5.2)
```

REV §4.4 verified that the analogous most-generous configuration for `R` is
`b = q = 1`, `μ = 2`; the same check applies here, since adding trivial
dicriticals, adding `μ ≥ 2` non-carriers, or raising any `μ_l` all increase `W`
without increasing `q′`, weakening the right-hand side of (5.1) relative to the
left. So (5.1)–(5.2) is used as a **floor on the obstruction**, never as an
attainment claim.

**(f) `q′ = 1` is impossible.** With `q′ = 1`, (5.1) reads `W + d − 1 ≤ d`,
i.e. `W ≤ 1`. But `W ≥ b + 4q′ ≥ 5`. So **any surviving configuration has at
least two distinct correction carriers**, hence (by 5.2) `W ≥ 9`.

This single line is the whole kill of the N=20 packet, and is the structural
statement to remember: a lone ramified carrier can never balance the excess
budget, because it offers only one site and each site is capped at `d`.

## 6. Re-running the N=20 budget: packet (4.9) is dead

Packet (4.9) has `b = 1`, `q = 1`, one carrier `(μ, s, corr) = (2, 3, 16)`,
`W = 7`, `d = 6`, `a = 13`, `N = 20`. Hence `q′ = 1`.

**Kill, form 1 (via §5(f)).** `q′ = 1` gives `W + d − 1 ≤ d`, i.e. `7 + 6 − 1 = 12 ≤ 6`.
False. **Packet (4.9) is refuted.**

**Kill, form 2 (explicit, so the mechanism is visible).** By Theorem 4.A the
cubic `h_1` is totally ramified: `h_1(t) = (t − t_0)³`, one critical point
`t_0 = l ∩ L_C`, one critical value `z_0`, one physical critical image
`p = η(z_0)`. By Corollary 3.2 the whole correction is one jump:

```text
16 = corr_1 = μ_{x_0} f^* − μ_1 = μ_{x_0} f^* − 2   ⟹   μ_{x_0} f^* = 18,
k_1 = μ_{x_0} f^* − e_{t_0} μ_1 = 18 − 3·2 = 12.
```

All 12 units of excess sit over the single physical point `p`, so `K_p = 12`.
By §5(b), `p ∈ Sing D` and `r_p ≥ 2`; [P7] then gives

```text
a_p = N − r_p W − K_p ≤ 20 − 2·7 − 12 = −6 < 0,
```

which is absurd (`a_p` is a cardinality). Equivalently `K_p ≤ d = 6` while the
concentration theorem demands `K_p = 12`. Even the most generous reading
`r_p = 1` — excluded by §5(b), but worth pricing — gives
`a_p = 20 − 7 − 12 = 1 ≥ 0`, so the packet is not killed by fibre positivity
alone; it is killed by `r_p ≥ 2`, which rests on [P5] (branches smooth,
singularities multibranch) plus [P6] (smooth-stratum covering). Both are
promoted and both are already load-bearing for the promoted `N ≥ 20` frontier,
so no new hypothesis is imported here.

**No neighbouring `N = 20` shape survives.** REV §4.4–§4.5 enumerated the `W=7`
shapes: `(1,1) + (2,3)` — just killed — and `(1,1) + (3,2)`, which has `q′ = 1`
and dies by §5(f) as well (it already died under the weaker `R = 1` bound). Any
`N = 20` shape needs `2W + d = 20` with `d ≥ 1`, so `W ≤ 9`; and `q′ ≥ 2`
requires `W ≥ 9`, forcing `W = 9`, `d = 2`, `q′ = 2`, and then (5.1) reads
`9 + 2 − 1 = 10 ≤ 2·2 = 4`, false. So:

> **No configuration at `N = 20` survives.** The first escape does not occur
> at degree 20.

**The same sweep excludes every `N ≤ 25`.** Substituting `W = 4q′ + 1 + ε`
(`ε ≥ 0`) and `N = 2W + d` into (5.1) with `q′ ≥ 2`:

```text
(q′ − 1) d ≥ W − 1 ≥ 4q′   ⟹   d ≥ 4q′/(q′ − 1),
N = 2W + d ≥ 2(4q′ + 1) + ⌈4q′/(q′ − 1)⌉ = 8q′ + 2 + ⌈4q′/(q′−1)⌉.
```

| `q′` | min `W` | min `d` | min `N` |
|---:|---:|---:|---:|
| 1 | — | impossible | — |
| 2 | 9 | 8 | **26** |
| 3 | 13 | 6 | 32 |
| 4 | 17 | 6 | 40 |
| 5 | 21 | 5 | 47 |

The minimum over `q′ ≥ 2` of `2W + d` subject to `W ≥ 4q′+1` and
`(q′−1)d ≥ W−1` is attained at `q′ = 2`, `W = 9`, `d = 8`: increasing `W` above
`4q′+1` costs `2` per unit and saves at most `1/(q′−1) ≤ 1` per unit on `d`, so
the minimum is always at `W = 4q′+1`; and the resulting `8q′ + 2 + ⌈4q′/(q′−1)⌉`
is increasing in `q′` for `q′ ≥ 2`. Hence:

> **Theorem 6.A.** Under H2, if some affine-image dicritical has `μ_0 = 1`, then
> `N ≥ 26`. Equivalently: **H2 admits no trivial dicritical for any `N ≤ 25`**,
> with no H3 hypothesis (H3 is a conclusion, by [P5]).

This supersedes the promoted `N ≥ 19` exclusion of ALL-N Theorem 4.1(4) and
REV §4.4, moving the ramified-nonprimitive frontier from 20 to 26. The
consequences of §5.1 of ALL-N — `b = 0` under H2, hence `2m ≤ N − 2` — now hold
unconditionally for every `N ≤ 25`.

## 7. General-N consequence: the excess vanishes, and the OPEN closes

§§5–6 kill the packet by counting sites. The remaining question — can a site
carry excess `k_l > 0` at all? — is answered by running Orevkov's own §5 link
machinery *without* his no-jump hypothesis.

Fix a carrier `l`, its `L_C` chain `l_1 — ⋯ — l_{k−1}` ([R1](b),(c)), the
contracted point `x_0 = π(l_1 ∪ ⋯ ∪ l_{k−1}) ∈ X̃^*`, and `p = f^*(x_0)`. Let
`B_1 = f^*(l^*)` be the image branch, smooth by [P5]. Let `B` be a small closed
ball at `p`, `B̃` the connected component of `f^{*−1}(B)` containing `x_0`,
`S = ∂B ≅ S³`, `S̃ = ∂B̃`, and

```text
K′ := f^{*−1}(B_1) ∩ S̃,        K := B_1 ∩ S.
```

Orevkov (p. 8–9) establishes for exactly this configuration that `X̃^*` is
analytic at `x_0` and that `B̃` is the cone over `S̃`; so `S̃` is the **link of
the normal surface germ** `(X̃^*, x_0)`, resolved by the chain.

> **Theorem 7.A (no excess).** `k_l = 0` for every affine-image dicritical `l`.

*Proof.* Three inputs.

**(1) `S̃` is a rational homology sphere.** The chain is contracted, hence
negative definite (Grauert/Mumford), hence its intersection matrix is
nondegenerate; `H_1(S̃; Z) = coker` of that matrix is finite, so
`H_1(S̃;Q) = 0` and by Poincaré duality `H_2(S̃;Q)=0`. `S̃` is connected
(normal germ).

**(2) `S̃ − K′ → S − K` is a covering, so `π_1(S̃ − K′) ↪ Z`.** `f^*|_{B̃}` is
proper (`f^*` proper), so `∂B̃ = f^{*−1}(S) ∩ B̃` and `f^* : S̃ → S` is proper.
Every point of `B̃ ∖ f^{*−1}(B_1)` lies in `C̃²` — it is neither on `l^*`
(which maps into `B_1`) nor at `x_0` (which maps to `p ∈ B_1`) — so `f` is a
local biholomorphism there by the Keller condition. Hence
`f^* : S̃ − K′ → S − K` is a proper local homeomorphism, i.e. a covering.
`B_1` is smooth and passes through the centre of `B`, so `K` is an unknot in
`S ≅ S³` and `π_1(S − K) ≅ Z`. Removing the 1-complex `K′` from the connected
3-manifold `S̃` leaves it connected, so `π_1(S̃ − K′)` injects into `Z` and is
therefore trivial or `Z`; in particular `rank H_1(S̃ − K′;Q) ≤ 1`.

**(3) That rank equals the number of components of `K′`.** `K′` is a disjoint
union of `r` embedded circles, one per irreducible branch of the curve germ
`f^{*−1}(B_1)` at `x_0`. Mayer–Vietoris over `Q` with
`A = S̃ − int N(K′)`, `B = N(K′) = r` solid tori, `A ∩ B = r` tori, using
`H_2(S̃;Q) = H_1(S̃;Q) = 0`:

```text
0 → Q^{2r} → H_1(A;Q) ⊕ Q^r → 0        ⟹    rank H_1(S̃ − K′;Q) = r.
```

(Controls: `S̃ = S³` with `r = 1` unknot gives a solid torus, rank 1; with
`r = 2` a Hopf link gives `T²×I`, rank 2.)

So `r ≤ 1`. Since `l^*` is one branch of `f^{*−1}(B_1)` at `x_0`, `r = 1` and
`f^{*−1}(B_1) = l^*` near `x_0`: **no affine branch of `f^{-1}(B_1)` meets the
contracted configuration.** Now count the local degree at `x_0` on a point
`q ∈ B_1` near `p`, `q ≠ p` (conservation of number for the finite germ): the
preimages are the `e_{t_0}` points of `l′` over `q`, each of local degree `μ_l`
by Lemma 3.1's normal form, together with the affine preimages, each of local
degree 1. Hence `μ_{x_0}f^* = e_{t_0} μ_l + k_l` with `k_l` the number of affine
preimages — which is `0`. Carriers with no `L_C` chain have `corr_l = 0` and
`k_l = 0` trivially. ∎

> **Theorem 7.B (B0 under H2 at every degree).** Let `F` be a noninvertible
> plane Keller map of geometric degree `N ≥ 3` with `A_F` irreducible. Then no
> affine-image dicritical has `μ_l = 1`.

*Proof.* Suppose one does. Then [P5] applies. By Corollary 3.2 and Theorem 7.A,
`corr_l = μ_l(s_l − 1)` for every `l`. Substituting into the Orevkov budget [P1]:

```text
N − 1 = Σ_l (μ_l + corr_l) = Σ_l μ_l s_l = W,
```

so `a = N − W = 1`. But [P5] forces `2a > N` (REV §4.1, CONFIRMED), giving
`N < 2`, contradicting `N ≥ 3`. ∎

Two independent cross-checks. (i) `corr_l = μ_l(s_l − 1)` forces
`μ_l | corr_l`. At `N = 5` the unique H2 trivial profile is
`(μ,corr) = (2,1)+(1,0)` (COORD:69–74); `2 ∤ 1`, so it dies — recovering the
promoted `N = 5` kill by a route that never uses the `N = 5` fibre pin.
(ii) Packet (4.9) needs `corr = 16` with `μ = 2, s = 3`, i.e.
`μ(s−1) = 4 ≠ 16`; the §6 arithmetic kill and the §7 divisibility kill agree.

**Typing.** Theorem 7.B closes `OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]`
in the negative and makes `b = 0` under H2 unconditional at every degree, hence
`2m ≤ N − 2` under H2 at every degree (ALL-N §5.1). It is *not* an attainment
claim and does not touch the reducible gap
`OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS]`, which is where
`2m ≤ N − 1` unconditional still lives. The result is `PROVED_PENDING_REVIEW`:
it is new mathematics, not a promoted consumption, and §8 lists precisely where
a hostile reviewer should push.

## 8. Typed conclusions and OPEN items

**Results, in dependency order.**

1. **Lemma 3.1 / Corollary 3.2 (concentration).** `corr_l` is a single local
   jump, at the image of the contracted `L_C` chain of `l`, and vanishes when
   that chain is empty. Re-derived from Orevkov [R1]+[R2] plus [P4]+[P5].
   Status: **PROVED**. This is strictly sharper than the promoted
   "correction support = ramification support of `h_l`".
2. **Theorem 4.A (rigidity).** Either `s_l = 1`, or `h_l(t) = (t−t_0)^{s_l}` is
   totally ramified at the unique boundary node of `l′`. Status: **PROVED**.
3. **Theorem 5.A + §5(f).** `a − 1 ≤ q′ d` with `q′ ≤ ⌊(W−1)/4⌋`; `q′ = 1` is
   impossible. Status: **PROVED** (consumes [P6], [P7]).
4. **§6: packet (4.9) is REFUTED**, and no `N = 20` configuration survives.
5. **Theorem 6.A:** `N ≥ 26` for any ramified escape. Supersedes the promoted
   `N ≥ 20` frontier.
6. **Theorems 7.A / 7.B:** the excess `k_l` vanishes; hence **B0 holds under H2
   at every degree** and `OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]`
   closes negative. Status: **PROVED_PENDING_REVIEW**.

Items 1–5 are independent of item 6: even if the link argument of §7 were
broken on review, §6 stands and the frontier is `N ≥ 26`, not `N ≥ 20`.

**Where a hostile reviewer should push (ranked).**

- **(A) §7 step (2), the covering.** The claim that `f^* : S̃ − K′ → S − K` is
  a covering rests on `f^*` being proper and on `∂B̃ = f^{*−1}(S) ∩ B̃`. Both
  follow from Orevkov's own §5 construction (p. 8, "each connected component of
  `f^{*−1}(B)` contains a unique point of `f^{*−1}(y)`"), but that construction
  is stated there under his no-jump hypothesis; check that nothing in it used
  `μ_x = μ_l`. My reading is that the hypothesis enters only at
  `f^{*−1}(K) = K̃`, which is exactly the conclusion §7 replaces.
- **(B) §7 step (3), `r` = number of branches.** `K′` must be a disjoint union
  of embedded circles, one per irreducible branch. Standard for links of curve
  germs in a normal surface germ, but it should be checked that an affine
  branch through a *node* of the chain, or tangent to a chain component, still
  contributes exactly one circle and does not merge with `K̃`.
- **(C) Scope of [P5].** The unknottedness of `K` — hence `π_1(S−K) = Z` — needs
  `B_1` smooth, i.e. `η` immersive, i.e. the existence of a trivial dicritical.
  Without it, `π_1(S−K)` is a knot group and step (2) yields no rank bound. So
  §7 is genuinely a statement about B0 (trivial dicriticals) and **must not** be
  quoted as a general "no excess" law.
- **(D) `2a > N`.** Theorem 7.B's final contradiction consumes it as promoted
  (REV §4.1). If it were withdrawn, `a = 1` alone is not absurd and 7.B would
  need a replacement closing move.
- **(E) Lemma 3.1's finiteness hypothesis.** [R2] requires finite fibres at `t`;
  I argued no contracted curve germ passes through a boundary-smooth `t ∈ l′`.

**OPEN, unchanged by this lane.**

- `OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS]` — untouched.
  §7 is componentwise in `η`, and H2 strictness is what supplies the correction;
  neither transfers to reducible `A_F`. Unconditional `2m ≤ N − 1` still waits
  on this.
- `OPEN[PI1-S4]` at `N = 4` without H2 — untouched.
- Whether Theorem 7.A can be freed of [P5] (item (C)) — new, and the natural
  successor: it would attack the reducible gap at the same place.

## 9. Sources

- S. Yu. Orevkov, *On three-sheeted polynomial mappings of `C²`*, Izv. Akad.
  Nauk SSSR / Math. USSR-Izv., DOI 10.1070/IM1987v029n03ABEH000984.
  `refs/jc86.pdf`, SHA-256
  `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`.
  Read with `pdftotext -layout`, pp. 2–11. Load-bearing: **Lemma 2.1** (p. 2;
  linear chain, unique `L_F` endpoint, unique `L_∞` meeting point, components of
  `L` nonsingular rational and pairwise transversal, graph a tree);
  **Lemma 3.1** (p. 4; normal form `u = x′, v = y′^k`); **§4** (p. 6;
  multiplicity definition, `π`, constant multiplicity `N`); **Lemma 4.2 eq. (4)**
  (p. 7; the exact budget, inner sum over `x ∈ π(l) − {∞}`); **Lemma 5.2 proof**
  (pp. 8–9; the ball/link construction and the Mumford presentation, from which
  §7 is built). Reference [5] there is D. Mumford, Publ. Math. IHES 9 (1961).
- H. Żołądek, *An application of Newton–Puiseux charts to the Jacobian problem*,
  Topology, DOI 10.1016/j.top.2008.04.001. `refs/zoladek2008_official.pdf`,
  SHA-256 `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad`.
  Proposition 6.5(b) consumed as promoted [P4] via ALL-N (1.4); not re-read
  here.
- Charged inputs ALL-N, REV, COORD as hashed in §0.

**FALLACY-v2 self-check.** Flag/place/series: the four objects — `t ∈ l′`,
`π(t) ∈ X̃^*`, the place `h_l(t) ∈ D̃`, the physical point `f(t) ∈ D` — are kept
distinct throughout; §3 turns on exactly that distinction. Carrier/attainment:
packet (4.9) and the `(W,d,q′) = (9,8,2)` shape are typed necessary-only;
nothing here is a Keller witness. Floor/attainment: `N ≥ 26` is a floor from
(5.1), used only to exclude; Theorem 7.B is a nonexistence statement, not an
attainment. No `sat()`, no CAS, no raw remainder, no ring map. Prime marks:
`l′` is the punctured dicritical, not a derivative; `h_l′` in Theorem 4.A is the
derivative of the polynomial `h_l` and is the only such use. No gap filled by
cap or analogy; every unproved item is typed in §8.

<!-- BODY-END -->
