# B0 — No trivial dicritical for a Keller map: proof lane report

lane: B0-TRIVIAL-DICRITICAL
model: opus5
date: 20260831
status: NO at N=4 under H2 (proved); OPEN[B0-N4-REDUCIBLE-PI1] without H2; OPEN[B0-GENERAL-N] for N>=5
inputs_verified: 4/4 SHA-256 OK; 5/5 literature PDFs rehashed

## 0. Input custody and hashes

Four charged inputs verified byte-for-byte before any reading (`shasum -a 256`, 4/4 match):

```text
264ddba858b0eb54544fbf612a390c5ded9bd07eb37729b2700965015e369462  trivial-dicritical-literature-registry-grok46-20260831.md
6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb  round1033-sheet-gate-opus5-20260831.md
21bbc70c0cb8007be244d576625119eae55e67fd125b149fc7c15fe87d7a5e1a  round1033-sheet-gate-hostile-review-sol56-20260831.md
69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9  block-descent-a1-mprime-coordinator-integration-fable5-20260831.md
```

Primary literature consumed, hashed at execution in `refs/` (all five agree with
the registry's §2 table, so registry statement IDs R1-R14 are re-usable verbatim):

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf            (Orevkov 1987)
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7  refs/chau1999_apm71_full.pdf
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3  refs/do.pdf              (Domrina-Orevkov)
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

No CAS was run. All arithmetic below is by hand. Page numbers cite the local PDF
page of the hashed file, with the printed journal page where the scan shows one.

<!-- SECTION 0 END -->

## 1. Statement, conventions, and what is consumable

`F=(P,Q):C^2->C^2` is a Keller map (`J:=Jac F ∈ C^*`), not an automorphism,
geometric degree `N=d=[C(x,y):Frac C[P,Q]] >= 2`. `A_F` is Jelonek's
non-properness curve. On a smooth compactification `X` of `C^2` on which `F`
extends to `Phi: X -> P^2`, the boundary splits (Orevkov §2) into `L_∞`
(components sent into the target line at infinity), `L_C` (components on which
`Phi` is constant with finite value) and `L_F` (components on which `Phi` is
non-constant with affine image). Components `l ⊆ L_F` are the **map-dicriticals
with affine image**; `l' := l ∩ Phi^{-1}(C^2)`, `D_l := Phi(l')` a component of
`A_F`, `s_l := deg(l' -> D_l)`, `mu_l` the generic local degree of `Phi` along
`l`. Orevkov's collapsed model is `f*: X~* -> X* = C^2 ∪ {∞}`, a proper
constant-multiplicity branched covering of degree `N` with `(f*)^{-1}(∞)={∞}`;
`mu_x f*` is the local multiplicity at `x ∈ X~*` (Orevkov §4, `refs/jc86.pdf`
p. 6). Write `corr_l := sum_{x ∈ l', mu_x != mu_l} (mu_x f* - mu_l f*) >= 0`.

**Consumed as theorems** (from the charged integration `69970f4d`, §1):
the `Y=Spec B` construction and four boxes (in particular `a_D >= 1` on every
component `D` of `A_F`, and box `(U,e>1)` empty); the covering lemma and
conversion law `a_p=s_p-b_p`; **Lemma 4.2** `e_j = 1 + v_j(dx∧dy)`; the `chi_c`
toolkit and the Euler identity **(E)** `1 = d(1-chi_c(A_F)) + chi_c(F^{-1}(A_F))`;
the dictionary `e_j=mu_l`, `delta_j=s_l`, `a=f(z)` (integration §9). **Not
consumed** (these are what is under proof): `A_F=B`, H2 (`A_F` irreducible),
H3, `b=0`, `f(z)=2`, and any component-wise copy of (M′).

Literature consumed, each re-verified against the hashed PDF at execution:

- **[O-4.2]** Orevkov Lemma 4.2 + Cor 4.3 (`jc86.pdf` pp. 7–8):
  `sum_{l ⊆ L_F} [ mu_l f* + sum_{x ∈ pi(l)-{∞}} (mu_x f* - mu_l f*) ] = N-1`,
  inner terms `>= 0`; equality in `sum mu_l <= N-1` iff every `corr_l=0`.
- **[O-5.2]** Orevkov Lemma 5.2 (`jc86.pdf` p. 8): if `mu_x f* = mu_l f*` at
  `x ∈ l'`, then `f*∘pi` restricted to a neighbourhood of `x` in `l` is a
  **nonsingular embedding**, i.e. it cuts out a smooth branch of `D_l` at
  `f*(x)`. (Proof: knot-group computation + Zariski. This is the load-bearing
  statement the registry recorded only through Żołądek's restatement.)
- **[O-5.3, O-Rem]** Lemma 5.3 and the closing Remark (`jc86.pdf` pp. 9–10):
  no component of `L_F` has `mu_l f* = N-1`.
- **[Z-6.5b]** Żołądek Prop. 6.5(b) (`zoladek2008_official.pdf` p. 457, journal
  p. 457): `mu_{z_0} > mu_D` iff the image is a singular point of the *immersed*
  curve `S`; `mu_D=1` implies `S` smooth (immersive; transverse crossings of
  smooth local components are not counted as singularities). Equivalent to
  [O-5.2] on the nose.
- **[Z-6.7]** Żołądek Prop. 6.7 (`zoladek2008_official.pdf` pp. 458–459): for
  a non-properness divisor with N–P chart `x=a_1y^{-γ_1}+…+uy^{-γ}`,
  `γ_j=l_j/k`, `γ=l/k`, the alteration chart `θ~(u,v)=(a_1v^{l_1}+…+uv^l,v^{-k})`
  has `Jac θ~ = v^{l-k-1}` (up to the unit `-k`), and `mu_D = l-k`.
- **[C-3.1]** Chau 1999 Lemma 3.1 proof (`chau1999_apm71_full.pdf` pp. 293–294):
  `Φ(t,ξ)=(t^{-m_φ}, φ(t^{-m_φ},ξ))`, `F_φ = F∘Φ`,
  `det DF_φ = J·det DΦ = -m_φ J t^{n_φ-2m_φ-1}`.
- **[C-3.6ii]** Chau 1999 Thm 3.6(ii) (p. 296): for a dicritical series,
  `a_φ = b_φ = 0` and `deg P_φ/deg Q_φ = deg P/deg Q`.
- **[C-4.4]** Chau 1999 Thm 4.4 (pp. 304–305): under the Jung normalisation
  `d>e>1`, every component `C_{[φ]}` of `E_f` is singular (AMS).
- **[AMS]** Abhyankar–Moh–Suzuki: a closed embedding `A^1 ↪ A^2` is rectifiable.
  (Used exactly as Orevkov uses it, `jc86.pdf` p. 10.)

<!-- SECTION 1 END -->

## 2. Route 1 — Chart-Jacobian / Newton–Puiseux

### 2.1 The two charts are the same chart; the transformation law

The registry's Route 1 asks for the transformation law relating Chau's
unresolved-chart order to Żołądek's resolved N–P order. It is an identity, not
an estimate, and the two charts coincide after a dictionary.

> **Proposition 2.1 (chart dictionary).** Chau's `Φ(t,ξ)=(t^{-m_φ},
> φ(t^{-m_φ},ξ))` is Żołądek's alteration chart `θ~` with the roles of the two
> coordinates exchanged and
> `(k, l, v, u) = (m_φ, n_φ - m_φ, t, ξ)`.
> Consequently `l - k = n_φ - 2m_φ` and the two multiplicity formulas
> `mu_D = l-k` [Z-6.7] and `ord_t det DF_φ = n_φ-2m_φ-1` [C-3.1] are one
> statement.
>
> *Proof.* Write Chau's series as `y = ⋯ + ξ x^{γ}` with `x=t^{-m_φ}`, so the
> `ξ`-term is `ξ t^{-m_φ γ}`. Then `∂x/∂ξ = 0`, `∂x/∂t = -m_φ t^{-m_φ-1}`,
> `∂y/∂ξ = t^{-m_φγ}`, hence `det DΦ = -m_φ t^{-m_φ-m_φγ-1}`. Comparing with
> Chau's printed `-m_φ t^{n_φ-2m_φ-1}` gives `-m_φγ = n_φ - m_φ`, i.e. the
> `ξ`-coefficient sits in `t`-degree `n_φ-m_φ`. Żołądek's `θ~` has `y=v^{-k}`
> and `u`-coefficient in `v`-degree `l`, and `Jac θ~ = -k v^{l-k-1}`. Matching
> `t ↔ v`, `ξ ↔ u`, `m_φ ↔ k`, `n_φ-m_φ ↔ l` identifies the charts and the
> Jacobian orders. ∎

### 2.2 What the Keller condition buys, exactly

> **Proposition 2.2 (chart form of `mu_l=1`).** Let `l` be a map-dicritical of
> the Keller map `F` with **affine** image, in the chart `Φ` of Prop. 2.1.
> Then `F_φ := F∘Φ` is holomorphic across `{t=0}` ([C-3.6ii]: `a_φ=b_φ=0`) and
> ```
> det DF_φ(t,ξ) = -m_φ J · t^{mu_l - 1},        mu_l = n_φ - 2m_φ = l - k.
> ```
> In particular (i) `mu_l >= 1` is *forced* by holomorphy of `F_φ`, with no
> further input; and (ii) `mu_l = 1` holds **iff** `det DF_φ ≡ -m_φ J`, a
> nonzero constant — i.e. iff the chart map `F_φ` is itself a Keller germ along
> `{t=0}`, hence a local biholomorphism at every point of `{t=0}`.
>
> *Proof.* [C-3.1] gives `det DF_φ = J·det DΦ = -m_φ J t^{n_φ-2m_φ-1}` with `J`
> a nonzero constant. At a generic point of `{t=0}` choose target coordinates
> `(w,τ)` with `D_l = {τ=0}`: since `Phi|_l` is non-constant, `w∘F_φ` has
> non-vanishing `ξ`-derivative there, and by definition of the generic local
> degree `τ∘F_φ = t^{mu_l}·(unit)`. Expanding the wedge,
> `ord_t det DF_φ = mu_l - 1`. Comparing exponents gives `mu_l = n_φ-2m_φ`,
> which is `l-k` by Prop. 2.1, recovering [Z-6.7]. Holomorphy of `F_φ` forces
> `ord_t det DF_φ >= 0`, i.e. `mu_l >= 1`. If `mu_l = 1` the Jacobian is the
> nonvanishing constant `-m_φ J`, so `F_φ` is a local biholomorphism along
> `{t=0}`; conversely a nonvanishing Jacobian gives `ord = 0`, i.e. `mu_l=1`. ∎

Proposition 2.2 is the exact chart-level form of promoted Lemma 4.2
(`e_j = 1+v_j(dx∧dy)`): globally, `ω := dx∧dy = J^{-1}F^*(du∧dv)` is a rational
2-form on `Y=Spec B` with
`div_Y(ω) = sum_j (e_j - 1) B_j`, effective, and supported exactly on the
**nontrivial** dicriticals. A trivial dicritical is a boundary prime along which
`ω` is a nowhere-zero regular 2-form.

### 2.3 Route 1 has no residual: a proved no-go

> **Proposition 2.3 (Route 1 cannot close alone).** The Keller hypothesis
> `J ∈ C^*` is *fully consumed* by the identity of Prop. 2.2: after it, the
> condition `mu_l=1` imposes exactly one integral condition, `n_φ = 2m_φ+1`
> (equivalently `l = k+1`, `γ = 1 + 1/k`), on the chart exponents, and this
> condition is arithmetically unobstructed — `gcd(k+1,k)=1` holds for every
> `k >= 1`, so the normalisation `gcd(l_1,…,l,k)=1` of [Z-6.7] never rules it
> out. No inequality between `l` and `k` other than `l >= k+1` is available from
> the Jacobian, because the Jacobian order is an equality, not a bound.
>
> *Proof.* The chart Jacobian is `-m_φ J t^{mu_l-1}`, an exact monomial times a
> unit; every scrap of information the Keller condition contributes at the
> divisorial valuation `ord_l` is the single integer `ord_l(dx∧dy) = mu_l-1`.
> Given a target integer `mu_l = 1`, the chart datum `(k;l_1,…,l_{d-1},l)` with
> `l=k+1` satisfies all constraints [Z-6.7] imposes. ∎

This upgrades the SHEET-GATE attainability remark (`v(dx∧dy)=0` is attained
among valuations at infinity) from "no *bare* valuative obstruction" to "no
obstruction at all from the one-valuation chart data", and it is consistent with
the Sol gate review's withdrawal of the impossibility claim: a Keller-specific
theorem is not ruled out, but it must be **non-local**. Route 1 is therefore
typed `CLOSED-AS-A-ROUTE (negative)`: it supplies the exact reformulation used
below (Prop. 2.2(ii): the map is a local biholomorphism along a trivial
dicritical) and nothing more. Routes 2 and 3 supply the non-local input.

<!-- SECTION 2 END -->

## 3. Route 2 — Image-singularity / covering split

### 3.1 Standing objects

`q: Y=Spec B -> C^2` is the promoted finite flat degree-`d` normalisation of the
target in `K`, `U=C^2 ⊂ Y` open, `B_Y = Y-U = ∪_j B_j` pure of codimension one,
`e_j = mu_{l_j}`, `delta_j = s_{l_j}`, `q(B_j)=D_{l_j}`. Promoted facts used
verbatim: `sum_{y ∈ q^{-1}(p)} e_y = d` for **every** `p ∈ C^2` (flatness); the
`e_y` are the orbit sizes of the local monodromy `H_p` on the `d` sheets;
`a_p := #(q^{-1}(p) ∩ U)` and `a_D >= 1` on every component `D ⊆ A_F`;
box `(U, e>1)` empty.

> **Lemma 3.1 (branch locus).** Put `Br := ∪_{l : mu_l >= 2} D_l`. Then `q` is
> finite étale over `C^2 - Br`, and `Br != ∅`.
> *Proof.* `q` is étale at every point of `U` (Keller) and at the generic point
> of `B_j` exactly when `e_j=1` (flat + fibre-reduced ⟹ unramified ⟹ étale).
> Hence the branch locus has codimension-one part exactly `Br`; by purity of the
> branch locus (Zariski–Nagata; `C^2` regular, `Y` normal, `q` finite) the branch
> locus is pure of codimension one or empty, so it equals `Br`. If `Br=∅` then
> `q` is finite étale over the simply connected `C^2` with `Y` irreducible, so
> `d=1`. ∎

> **Lemma 3.2 (meridian cycle type).** For `D ⊆ A_F` a component and generic
> `p ∈ D`, the local monodromy generator `g_D` has cycle type
> `{mu_l repeated s_l times : l -> D} ∪ {1^{a_D}}`, and
> `a_D + sum_{l -> D} s_l mu_l = N`. The monodromy
> `rho: pi_1(C^2 - Br) -> S_N` of the étale cover of Lemma 3.1 has **transitive**
> image, and that image is generated by the conjugates of the `g_D`, `D ⊆ Br`.
> *Proof.* First two claims are the promoted orbit/fibre dictionary plus
> flatness. Transitivity: `q^{-1}(C^2-Br)` is `Y` minus a proper closed subset,
> and `Y` is irreducible, hence connected. Generation: `C^2` is simply connected
> and `Br` a curve, so `pi_1(C^2-Br)` is generated by meridians of the components
> of `Br` (van Kampen); meridians of an irreducible component are mutually
> conjugate. ∎

### 3.2 The `mu_l = 1` split by `s_l`, and what `corr_l = 0` forces

By Prop. 2.2(ii) a trivial dicritical is one along which `F` is a local
biholomorphism at *generic* points. [O-5.2]/[Z-6.5b] upgrade this at **all**
points where the local multiplicity does not jump:

> **Lemma 3.3 (smooth branches).** If `corr_l = 0` then for every `x ∈ l'` the
> germ of `Phi|_{l}` at `x` is a nonsingular embedding, so every branch of `D_l`
> at every affine point is smooth. Consequently every `p ∈ Sing D_l` has
> `r_p >= 2` branches, and `nu := sum_{p ∈ Sing A_F}(r_p-1) >= s := #Sing A_F`
> whenever every dicritical has `corr_l=0`.
> *Proof.* [O-5.2] verbatim; the count is then immediate since a unibranch point
> with a smooth branch is a smooth point. ∎

This is where the registry's `s_l`-split resolves. For `s_l = 1` the surviving
configuration named in the brief — a trivial dicritical mapping **birationally
onto a nodal affine curve** — is not excluded by [C-4.4] (which needs a smooth
*embedded* image, and additionally the Jung normalisation `d>e>1`). The
resolution below does not go through the image singularity type at all: it goes
through the *global* topology of the image, and it is insensitive to `s_l`.

### 3.3 The Euler forcing lemma

> **Lemma 3.4 (`A^1`-forcing).** Assume `A_F = D` is irreducible, `N >= 3`, and
> let `a := a_D >= 1`. Assume **either** (i) `D` is smooth, **or** (ii) every
> dicritical has `corr_l = 0` and `2a <= N`. Then `a = 1`, `D` is smooth, and
> `D ≅ A^1`.
> *Proof.* Each `l'` is `P^1` minus `r_l >= 1` points, and `l' -> D` is finite,
> so it factors through the normalisation `D~`, which is therefore `P^1` minus
> `c >= 1` points: `chi_c(D~) = 2-c <= 1`. By the promoted `chi_c` toolkit,
> `chi_c(D) = (2-c) - nu` and `chi_c(D_0) = chi_c(D) - s` with `D_0 = D-Sing D`.
> The promoted covering lemma gives `chi_c(F^{-1}(D_0)) = a·chi_c(D_0)`, and
> `chi_c(F^{-1}(D)) = a·chi_c(D_0) + sum_{p ∈ Sing D} a_p`. Substituting into (E)
> `1 = N(1-chi_c(D)) + chi_c(F^{-1}(D))` and using `chi_c(D)=chi_c(D_0)+s`:
> ```
>   (N-a)·chi_c(D_0) = N - 1 - N·s + sum_p a_p .            (3.1)
> ```
> Expand `chi_c(D_0) = (2-c) - nu - s` and regroup (`-(N-a)s + Ns = as`):
> ```
>   (N-a)(2-c) - (N-a)·nu + a·s = N - 1 + sum_p a_p .       (3.2)
> ```
> `a <= N-1` (some `s_l mu_l >= 1`), so `N-a > 0`. In case (i), `s = nu = 0` and
> the sum over `Sing D` is empty, so (3.2) reads `(N-a)(2-c) = N-1`; with `c>=1`
> the left side is `<= N-a`, forcing `a <= 1`, hence `a=1`, and then `2-c=1`,
> i.e. `c=1`. In case (ii), Lemma 3.3 gives `nu >= s` and `c >= 1` gives
> `(N-a)(2-c) <= N-a`, so `N-a-(N-2a)s >= N-1+sum_p a_p`, i.e.
> ```
>   (a - 1) + (N-2a)·s + sum_p a_p  <=  0 ,                 (3.3)
> ```
> in which all three summands are `>= 0` when `2a <= N` and `a >= 1`. Each
> vanishes: `a=1`; `(N-2)s=0` with `N>=3` gives `s=0`, hence `nu=0` and `D`
> smooth; equality in `(N-a)(2-c) <= N-a` gives `c=1`. In both cases
> `D = D~ ≅ A^1`. ∎

Sanity gates. (i) Orevkov's `N=3` case 3 (`L_F` irreducible, `mu=2`, all
`corr=0`) has `a=1`, `2a=2<=3`: Lemma 3.4 returns `D ≅ A^1`, which is exactly
what Orevkov obtains at `jc86.pdf` p. 10 from his Lemma 5.3 — an independent
re-derivation of a step he proves by a different (separation) argument.
(ii) The surviving `N=4` profile `a=2` with one dicritical of `(mu,corr)=(2,1)`
satisfies neither (i) nor (ii) of Lemma 3.4 — as it must not, since that profile
is not excluded here.

### 3.4 The main irreducible theorem

> **Theorem 3.5.** Let `F` be a noninvertible Keller map of geometric degree
> `N >= 3` with `A_F` **irreducible**, `a := a_{A_F}`. Then neither of the
> following can hold: (i) `A_F` is smooth; (ii) every `corr_l = 0` and
> `2a <= N`.
> *Proof.* Under either hypothesis Lemma 3.4 gives `a=1` and `D := A_F ≅ A^1`,
> a smooth closed curve in `C^2`, so by [AMS] there is `alpha ∈ Aut(C^2)` with
> `alpha(D)` a line; hence `C^2 - D ≅ C × C^*` and `pi_1(C^2-D) ≅ Z`, generated
> by one meridian `gamma`. `Br != ∅` (Lemma 3.1) and `Br ⊆ A_F = D` irreducible,
> so `Br = D` and `q` is finite étale of degree `N` over `C^2-D` with connected
> total space. By Lemma 3.2 the monodromy image `<rho(gamma)>` is transitive on
> `N` letters; a cyclic transitive subgroup of `S_N` is generated by an
> `N`-cycle, so `rho(gamma)` is an `N`-cycle and has no fixed point. But its
> cycle type is `{mu_l^{(s_l)}} ∪ {1^{a}}`, with `a` fixed points, so `a = 0`,
> contradicting the promoted `a >= 1`. ∎

> **Corollary 3.6 (irreducible `A_F` is singular).** For a noninvertible Keller
> map, `A_F` cannot be irreducible and smooth.

This is a normalisation-free strengthening of [C-4.4] in the irreducible case:
Chau's proof that every component of `E_f` is singular runs through
Abhyankar–Moh applied to a *regular embedding* and needs the Jung form
`d>e>1`; Theorem 3.5(i) needs no Jung normalisation and no `deg P/deg Q`
hypothesis. It also independently reproves the promoted "smooth-`A_F` law"
and upgrades it from `a=1` to outright impossibility.

> **Corollary 3.7 (Orevkov's inequality is strict under H2).** If `A_F` is
> irreducible then `sum_{l} mu_l <= N-2`; equivalently `sum_l corr_l >= 1`;
> equivalently (by [Z-6.5b]) `A_F` carries at least one **non-immersive** point,
> i.e. a locally irreducible singularity of some `Phi(l')`.
> *Proof.* Suppose `sum_l mu_l = N-1`. By [O-4.2] Cor. 4.3 this is exactly the
> equality case, so every `corr_l = 0`. All dicriticals map onto the irreducible
> `A_F`, so `a = N - sum_l s_l mu_l <= N - sum_l mu_l = 1` (using `s_l >= 1`),
> and `a >= 1` forces `a = 1` and `s_l = 1` for every `l`. Then `2a = 2 <= N`,
> and Theorem 3.5(ii) applies. ∎

> **Corollary 3.8 (Orevkov's closing Remark, reproved).** No component of `L_F`
> has `mu_l f^* = N-1`.
> *Proof.* If `mu_{l_1} = N-1` then [O-4.2] forces every other term of the budget
> to vanish, so `l_1` is the only dicritical and `corr_{l_1}=0`; hence `A_F` is
> irreducible and `sum_l mu_l = N-1`, contradicting Cor. 3.7. ∎

Corollary 3.8 recovers, with a complete proof, the assertion Orevkov states as
an unproved Remark ("repeating the above arguments…", `jc86.pdf` p. 10) and that
Domrina–Orevkov cite as `[3, remark after 5.3]` (`do.pdf` p. 6). It is a
first-class sanity gate on the machine of §3.

<!-- SECTION 3 END -->

## 4. Route 3 — Unique-versus-mixed at N=4

### 4.1 The complete profile list

By [O-4.2] the budget is an **equality**: `sum_l (mu_l + corr_l) = N-1 = 3`,
each summand `>= 1`. Writing profiles as multisets of pairs `(mu_l, corr_l)`,
the complete list at `N=4` is

| # dicriticals | profile | contains `mu=1`? |
|---|---|---|
| 1 | `(3,0)` | no |
| 1 | `(2,1)` | no |
| 1 | `(1,2)` | **yes** — (c) |
| 2 | `(2,0)+(1,0)` | **yes** — (d) |
| 2 | `(1,1)+(1,0)` | **yes** — (e) |
| 3 | `(1,0)+(1,0)+(1,0)` | **yes** — (f) |

Row `(3,0)` is excluded outright by Cor. 3.8 (Orevkov's Remark, here proved).
Row `(2,1)` carries no trivial dicritical and is the profile that survives all
arguments in this report; it is the promoted `a=2`, `(delta,e)=(1,2)`,
`b=0` row of SHEET-GATE Thm 4.4.

### 4.2 Rows (c), (e), (f): killed by the branch locus

> **Proposition 4.1.** Profiles (c), (e), (f) are impossible.
> *Proof.* In each of them every dicritical has `mu_l = 1`, so `Br = ∅` in the
> sense of Lemma 3.1 — and Lemma 3.1 gives `N = 1`. ∎

This is the numbered replacement the brief asked for. Domrina–Orevkov dismiss the
unique-`mu=1` case (our row (c)) with the sentence "If the ramification order is
1 then `F` is an unbranched covering over `C^2`. This is also impossible."
(`do.pdf` p. 6, §2). As the registry flagged (R12), that sentence is **not** a
verbatim Orevkov theorem: at `N=4` a unique `mu=1` dicritical is forced by
[O-4.2] to carry `corr = 2`, so `f^*` is *not* unbranched over all of `C^2` —
it is unbranched only over the complement of one or two points. Their conclusion
is nevertheless correct, by either of two complete arguments: topologically,
`C^2` minus a finite set is still simply connected, so a connected `4`-fold
covering of it is impossible; algebraically, Prop. 4.1 above, which never
mentions the correction points at all because purity of the branch locus
(Zariski–Nagata) rules out isolated branch points a priori. **The author
inference flagged at R12/Chain C is hereby discharged.**

### 4.3 Row (d): the mixed remainder

Row (d) is the transposition-horn case. Its numerics: one dicritical `l_1` with
`mu_1 = 2`, one `l_0` with `mu_0 = 1`, and `corr_1 = corr_0 = 0`, so [O-5.2] and
Lemma 3.3 apply to **both**: every branch of `Phi(l_1')` and of `Phi(l_0')` at
every affine point is smooth. That is exactly the rigidity the brief asked for:
`corr_l = 0` at a trivial dicritical means the parametrisation `l_0' -> D_0` is
an **immersion with no critical point whatsoever**, so `D_0` has no
locally-irreducible singularity, and likewise for `D_1`.

> **Theorem 4.2 (`N=4` under H2).** Let `F` be a noninvertible Keller map of
> geometric degree `4` with `A_F` **irreducible**. Then `F` has no dicritical
> with affine image and `mu_l = 1`. Consequently `b = 0`, `a = 2`, the boundary
> profile is `(delta, e) = (1,2)`, the meridian is a transposition with
> `G = S_4`, and **(M) holds verbatim at rank four in the transposition class**.
> *Proof.* Rows (c), (e), (f) die by Prop. 4.1. Row (d) with `A_F` irreducible
> has every `corr_l = 0`, hence `sum_l mu_l = 3 = N-1`, contradicting Cor. 3.7.
> Row `(3,0)` dies by Cor. 3.8. Only `(2,1)` survives; over the irreducible
> `A_F`, `a + s_1·2 = 4` with `a >= 1` gives `s_1 = 1`, `a = 2`, `b = 0`. ∎

Theorem 4.2 **refutes the SHEET-GATE Thm 4.4 row `a=1`, `(1,2)+(1,1)`, `b=1`
under H2**, which is the entire content of the charged transposition horn once
`A_F` is known irreducible. It also removes the dependence on the (unproved)
census equality `f(z)=2`: Cor. 4.5 of the SHEET-GATE report is no longer needed.

### 4.4 Row (d) without H2: the residual configuration

If `A_F` is *reducible*, row (d) survives with the two dicriticals over
**different** components. Everything about it can be pinned:

> **Theorem 4.3 (structure of the residual configuration).** Suppose a
> noninvertible Keller map of degree `4` has a dicritical with affine image and
> `mu = 1`. Then, with `D_1 := Phi(l_1')`, `D_0 := Phi(l_0')`:
> 1. `F` has exactly two dicriticals with affine image, `(mu_1,corr_1)=(2,0)`
>    and `(mu_0,corr_0)=(1,0)`; `A_F = D_1 ∪ D_0` with `D_1 != D_0`.
> 2. `s_1 = 1`, `a_{D_1} = 2`; `s_0 ∈ {1,2,3}`, `a_{D_0} = 4 - s_0`.
> 3. `Br = D_1`. `q` is finite étale of degree `4` over `C^2 - D_1` with
>    connected total space, so `pi_1(C^2 - D_1)` surjects onto a transitive
>    subgroup of `S_4` generated by conjugates of one transposition, i.e. onto
>    `S_4`. In particular `pi_1(C^2 - D_1)` is **non-abelian**.
> 4. Every affine branch of `D_1` and of `D_0` is smooth. Every `p ∈ Sing D_1`
>    with `p ∉ D_0` has exactly two branches, `a_p = 0`, and local monodromy
>    generated by two **disjoint** transpositions (cycle type `(2,2)`).
> 5. Writing `D~_1 = P^1 - {r_1 pts}` (`= l_1'`, since `s_1=1`),
>    `D~_0 = P^1 - {c_0 pts}`, `k_p` the number of branches of `D_0` at `p`,
>    `t_p` the number of points of `l_0'` over `p`, and `eps_p >= 0` the number
>    of contracted (`L_C`) fibre points over `p`, the aggregate Euler identity is
>    ```
>      2 r_1 + s_0 c_0 + sum_{p ∈ Sing A_F} (s_0 k_p - t_p) + sum_p eps_p
>          = 1 + 2 s_0 ,
>    ```
>    all displayed summands being `>= 0`. Hence **`c_0 = 1`, i.e.
>    `D~_0 ≅ A^1`**, and `r_1 = 1` (so `D~_1 ≅ A^1`) except possibly when
>    `s_0 = 3`, where `r_1 = 2` (`D~_1 ≅ C^*`) is also numerically admissible.
>
> *Proof.* (1) is the budget plus §4.2. (2): over generic `p ∈ D_1`,
> `a_{D_1} + 2 s_1 = 4` with `a_{D_1} >= 1` forces `s_1 = 1`, `a_{D_1} = 2`;
> over generic `p ∈ D_0`, `a_{D_0} + s_0 = 4`. (3): Lemma 3.1 with `Br = D_1`;
> transitivity and generation from Lemma 3.2; `S_4` is the only transitive
> subgroup of `S_4` generated by transpositions. (4): Lemma 3.3 for smoothness;
> at `p ∈ Sing D_1 - D_0` the fibre relation `2 beta_p + a_p + eps_p = 4` with
> `beta_p >= 2` (two smooth branches, `l_1' ≅ D~_1`) forces `beta_p = 2`,
> `a_p = eps_p = 0`; the local monodromy orbits then have sizes `(2,2)`, and two
> transpositions generating a group with orbit sizes `2,2` are disjoint.
> (5): substitute `chi_i = chi_c(D~_i) - n_i` into the aggregate identity
> `sum_i (4-a_i) chi_i = 3 - 4 s + sum_p a_p` (proved as in Lemma 3.4, with
> `D_i^0 = D_i - Sing A_F`), and eliminate `sum_p a_p` using the three fibre
> relations `2 beta_p + t_p + a_p + eps_p = 4` (`beta_p = 2, t_p = 0` on
> `Sing D_1 - D_0`; `beta_p = 1` on `D_1 ∩ D_0`; `beta_p = 0` on
> `Sing D_0 - D_1`) together with `n_1 = sum_p beta_p`, `n_2 = sum_p k_p`. The
> boundary points over `A_F - Sing A_F` are exactly the `s_l` dicritical points
> by the promoted covering lemma, so `eps_p = 0` off `Sing A_F`. Every term
> `s_0 k_p - t_p` is `>= 0` because `l_0' -> D~_0` has degree `s_0`. The
> stated bounds follow from `r_1 >= 1`, `c_0 >= 1` by inspection of
> `s_0 ∈ {1,2,3}`. ∎

> **Corollary 4.4.** In the configuration of Thm. 4.3, if `r_1 = 1` — which by
> part (5) holds whenever `s_0 ∈ {1,2}`, and in the `s_0=3` case unless
> `D~_1 ≅ C^*` — then `D_1` is **singular**, and `Sing D_1` is a nonempty set of
> double points of two smooth branches at which no affine preimage survives.
> *Proof.* If `D_1` were smooth its normalisation map would be an isomorphism,
> so `D_1 ≅ P^1 - {1 pt} = A^1`, a smooth closed curve in `C^2`; [AMS] would
> rectify it and give `pi_1(C^2 - D_1) ≅ Z`, contradicting Thm. 4.3(3). The
> description of `Sing D_1` is Thm. 4.3(4). ∎

Theorem 4.3 is exactly the "surviving configuration" the registry's Route 2
predicted (`mu=1` onto a curve that is *not* smooth-embedded), sharpened: the
trivial dicritical's own image `D_0` is forced to be a **polynomial curve**
(`D~_0 ≅ A^1`), all of whose affine branches are smooth; and the obstruction has
migrated entirely onto the *other* component `D_1`, where it is a
fundamental-group question and nothing else.

<!-- SECTION 4 END -->

## 5. Results: theorems proved unconditionally

**Answer to B0.** `NO at N=4 under H2`, and `OPEN (one named lemma) at N=4
without H2`. No YES-candidate exists at `N=4`: Thm. 4.3 shows any putative YES
must be a *reducible-`A_F`* configuration with a completely determined numerical
shape, so a YES would have to exhibit an affine plane curve `D_1` with
non-abelian `pi_1(C^2-D_1)` of a very restricted type (Cor. 4.4).

Proved here, all unconditional given only the promoted inputs of §1:

| # | Statement | Scope |
|---|---|---|
| P2.1–2.2 | Chau's and Żołądek's charts are one chart; `det DF_φ = -m_φ J t^{mu_l-1}`, so `mu_l >= 1` is forced and `mu_l = 1` iff the chart map is a Keller germ (local biholomorphism along the dicritical) | all `N` |
| P2.3 | Route 1 has no residual: after the chart Jacobian identity, `mu_l=1` is one unobstructed integral condition `l=k+1` | all `N` |
| L3.1 | branch locus of `q` is exactly `Br = ∪_{mu_l>=2} D_l`, and `Br != ∅` | all `N` |
| L3.4 | `A_F` irreducible + (smooth, or all `corr_l=0` and `2a<=N`) ⟹ `a=1` and `A_F ≅ A^1` | `N>=3` |
| **T3.5** | **no noninvertible Keller map has `A_F` irreducible with (i) `A_F` smooth, or (ii) all `corr_l=0` and `2a<=N`** | `N>=3` |
| C3.6 | an irreducible `A_F` is singular (Jung-free strengthening of [C-4.4]) | `N>=3` |
| **C3.7** | **`A_F` irreducible ⟹ `sum_l mu_l <= N-2`: Orevkov's Cor. 4.3 is strict; equivalently `A_F` has a non-immersive point** | `N>=3` |
| C3.8 | no component of `L_F` has `mu_l = N-1` (Orevkov's Remark, now proved) | `N>=3` |
| P4.1 | at `N=4`, an all-trivial dicritical set is impossible; the R12 author-inference is discharged | `N=4` |
| **T4.2** | **`N=4`, `A_F` irreducible ⟹ no `mu=1` dicritical; `b=0`, `a=2`, `(delta,e)=(1,2)`, (M) verbatim in the transposition class** | `N=4` |
| T4.3, C4.4 | complete structure of the only residual `N=4` configuration | `N=4` |

Two campaign-level consequences beyond the charged question:

> **Corollary 5.1 (weighted component bound under H2).** For `A_F` irreducible,
> `2 m_nt + m_triv <= sum_l mu_l <= N-2`, an improvement of one unit on the
> promoted item-9 bound. With `m_nt >= 1` (Lemma 3.1) this gives at `N=5`
> `m_nt = 1`, `m_triv <= 1`, hence `m <= 2` — the target the brief attached to
> the strong all-degree bound, obtained here under H2 only.

> **Corollary 5.2 (custody).** Thm. 4.2 makes the SHEET-GATE Cor. 4.5 route
> obsolete at `N=4`: `b=0` no longer needs the census equality `f(z)=2`, whose
> promotion status the Sol gate review typed GAP.

<!-- SECTION 5 END -->

## 6. Typed status and residual OPENs

**Route 1 — `CLOSED-AS-A-ROUTE (negative)`, Prop. 2.3.** The transformation law
requested by the registry is an identity (Prop. 2.1) and it consumes the Keller
hypothesis completely. Any closure must be non-local. This is a proved negative,
not an abandonment, and it is consistent with the gate review's withdrawal of
the blanket "no valuative proof" claim: Theorem 3.5 *is* a Keller-specific
theorem about the divisorial data, but it needs the global Euler identity and
`pi_1`, not one valuation.

**Route 2 — `CLOSED at N=4 under H2`; `OPEN` otherwise.** The split by `s_l`
proposed in the registry turns out to be the wrong cut: the argument that works
(Thm. 3.5) is insensitive to `s_l` and to the singularity type of the image,
and runs through `chi_c` + [AMS] + meridian transitivity. The `s_l >= 2`
`pi_1`-of-a-uniruled-complement computation the registry proposed is not needed.

**Route 3 — `CLOSED at N=4 under H2`, Thm. 4.2.** The Domrina–Orevkov
`mu=1` dismissal is now a numbered lemma (Prop. 4.1) with two independent
proofs, and the mixed remainder `(mu=2)+(mu=1)` is settled under H2 (Thm. 4.2)
and completely described without it (Thm. 4.3).

> **`OPEN[B0-N4-REDUCIBLE-PI1]`.** The exact missing lemma is:
>
> *Let `D ⊂ C^2` be an irreducible affine plane curve whose normalisation is
> `A^1` or `C^*` and all of whose affine branches are smooth. Is
> `pi_1(C^2 - D)` abelian?*
>
> A YES closes B0 at `N=4` outright (via Thm. 4.3(3)), hence closes `A_F = B`
> and the transposition horn with no H2 hypothesis. A weaker sufficient form
> also suffices: *no surjection `pi_1(C^2-D) -> S_4` sends every meridian to a
> transposition and the two local meridians at each double point to **disjoint**
> transpositions* (Thm. 4.3(4)).
>
> Status of the literature on this lemma. Deligne–Fulton (Zariski's conjecture)
> gives `pi_1(P^2 - C)` abelian for `C ⊂ P^2` irreducible **nodal**; Nori's
> theorem gives abelianness under `C^2 > 2·#nodes`. Neither is quoted here
> because (a) our `D` has one place at infinity, so `bar D ∪ L_∞` is never
> nodal and the affine complement is not the projective one, and (b) our double
> points are only known to be two *smooth* branches, which permits tangency.
> **Neither PDF was acquired in this lane; nothing above uses them.** This is a
> pure acquisition-and-check item, not a research question.

> **`OPEN[B0-GENERAL-N]`.** For `N >= 5`, B0 is open even under H2. The reason
> is exactly located: Cor. 3.7 needs all `corr_l = 0` to fire, and at `N >= 5`
> the budget leaves room for a trivial dicritical *plus* a correction. Concretely
> at `N=5` under H2, exactly two profiles carrying a trivial dicritical survive
> everything proved here: `(mu,corr) = (2,0)+(1,1)` and `(2,1)+(1,0)`. Relaxing
> Lemma 3.3 to `nu >= s - sum_l corr_l` and rerunning (3.2) gives
> `2a - N - 1 + (N-2a)s + sum_p a_p <= 0` in the one-correction case, which is
> satisfiable; so a genuinely new input is needed, not a sharper count. **The
> strong all-degree bound `2m <= N-1` is therefore NOT established here**;
> only the H2 form of Cor. 5.1.

**No `charge_basis` line is asserted.** Nothing here posits a new exit price;
the report consumes the promoted (E), covering lemma, box audit, and Lemma 4.2
at their promoted scope, and adds literature-sourced theorems.

**Fail-closed audit.** Every literature statement used is pinned by hashed PDF
and page in §1. Two statements the registry listed were *not* used and are not
relied on: [C-4.4] (superseded by Cor. 3.6 in the irreducible case) and the
`s_l >= 2` collapsed-covering idea. Two promoted items I deliberately did not
consume: `A_F=B` and `f(z)=2`. One subtlety was handled rather than ignored:
contracted `L_C` components can add fibre points (`eps_p` in Thm. 4.3(5)); the
promoted covering lemma confines them to `Sing A_F`, and they enter every
identity with a nonnegative sign, so no conclusion depends on their absence.

<!-- SECTION 6 END -->

## 7. Successors

1. **`ACQUIRE-PI1-AFFINE`** (cheapest decisive item in the portfolio). Acquire
   and hash Deligne, *Le groupe fondamental du complément d'une courbe plane
   n'ayant que des points doubles ordinaires est abélien* (Sém. Bourbaki 543,
   1979/80), Fulton, Ann. of Math. **111** (1980) 407–409, and Nori, Ann. Sci.
   ÉNS **16** (1983) 305–344; then decide `OPEN[B0-N4-REDUCIBLE-PI1]`. If it
   resolves YES, B0 closes at `N=4` unconditionally and `A_F=B` is promoted.
2. **`DOMRINA-2000`** (registry acquisition item 8). Domrina, Izv. Math. **64**
   (2000) 1–33 handles precisely the two-dicritical `N=4` case that Thm. 4.3
   isolates; `do.pdf` p. 1 states it as forthcoming. A cross-check against
   Thm. 4.3, not a consumption.
3. **`CORR-BUDGET-N5`**. Attack `OPEN[B0-GENERAL-N]` at the two surviving
   `N=5` profiles by making the *single* correction point explicit: by
   [Z-6.5b] it is a non-immersive point of `A_F`, i.e. a locally irreducible
   singularity, and by [O-5.2] it is the only one. A local classification of
   that germ against the `(2,0)+(1,1)` fibre data is desk-scale.
4. **`T3.5-SHARPEN`**. Theorem 3.5(ii) currently needs `2a <= N`. Deciding
   whether `2a > N` is possible at all for an irreducible `A_F` would upgrade
   Cor. 3.7 to unconditional strictness and is a promising standalone lane.

<!-- SECTION 7 END -->

<!-- BODY-END -->
