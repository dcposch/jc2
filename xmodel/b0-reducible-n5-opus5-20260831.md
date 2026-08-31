# B0-REDUCIBLE at N=5: component-incidence enumeration and ramified-cover gates

Lane: OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS]
Date: 2026-08-31 · Model: Opus 5 · Desk-scale exact reasoning only

## 0. Input verification and consumption typing

Verification was the first action. All four charged inputs hash as declared:

```text
621f1356b3b5290e32c2f2bf689b4d9a49412cb852066886a34b580366cb1652  b0-all-n-eta-criticality-sol56-20260831.md
f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46  b0-all-n-hostile-review-grok46-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Below **ALLN**, **REV**, **C19**, **CNA** denote them in that order. Two primary
PDFs were opened and rehashed; both agree with the custody values recorded in
ALLN §1 and REV §0:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf         (Orevkov, Math. USSR-Izv. 29 (1987))
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

One further primary source was opened, hashed, and is newly consumed here:

```text
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
```

(N. V. Chau, *Non-proper value set and the Jacobian condition*, arXiv:math/0305088v1,
6 May 2003; Theorem 1 and Corollaries 1–2 on printed pp. 1–2.)

No CAS was run; nothing of uncertain duration was executed. No canonical ledger,
no charged file, and no part of `jc2-lean` was touched.

**Typing convention.** `[P]` = consumed at a promoted scope (C19 §1, CNA §1, or
ALLN/REV items the coordinator promoted). `[D]` = derived in this report from
`[P]` items plus hashed primary sources. `[L]` = primary literature consumed
here. `[O]` = typed OPEN. `[A]` = audit finding against a consumed item.

**Standing scope.** `F` is a noninvertible plane Keller map of geometric degree
`N = 5`; `A_F` is its non-proper value set; `A_F = D_1 ∪ … ∪ D_m` with `m ≥ 2`
(REDUCIBLE); at least one affine-image dicritical has `mu = 1` (a *trivial*
dicritical). Everything below is inside that scope. Nothing here is an
attainment claim: no configuration is asserted to be realized by a Keller map.

## 1. Promoted budget recalled, and its N=5 instantiation

### 1.1 The promoted budget and the four bookkeeping objects

For an affine-image dicritical `l` with parametrized source `l'`, target
component `D = D_{tau(l)}`, `phi_l : l' -> D`, `s_l = deg phi_l`,
`mu_l` the dicritical multiplicity and `corr_l = sum_x (mu_x - mu_l) >= 0`:

- **(G1) Orevkov budget** `[P]` (ALLN (1.1), C19 §1.3): `Σ_l (mu_l + corr_l) = N − 1 = 4`.
- **(G2) Generic fibre, per component** `[P]` (ALLN (1.3), componentwise):
  `a_i + W_i = N`, where `W_i := Σ_{l → i} s_l mu_l` and `a_i ≥ 1`.
- **(G3) Normalization factorization** `[P]` (ALLN (2.1)–(2.2), REV §1):
  `phi_l = eta_i ∘ h_l` with `h_l : l' → D~_i` finite surjective of degree `s_l`,
  defined at *every* source point. This is the universal property of `eta_i`
  and is intrinsically componentwise: it never compares two components.
- **(G4) Pointwise jump law** `[P]` ([Z-6.5(b)], ALLN (1.4)):
  `mu_x > mu_l  ⟺  d phi_l = 0` at the corresponding parametrization point;
  `mu_l = 1 ⟹ corr_l = 0` and `d phi_l ≠ 0` everywhere.
- **(G5) Local multiplicity floor** `[P]` (ALLN (4.3), REV §4.2):
  `M_t ≥ e_t mu_l`, i.e. `k_t := M_t − e_t mu_l ≥ 0`, where `e_t` is the local
  degree of `h_l` at `t` and `M_t = mu_{pi(t)} f^*`. **The proof of (G5) uses
  only Orevkov Lemma 3.1 and the §4 multiplicity definition — it does not use
  immersivity of any `eta`.** That is what makes it usable on components with
  no trivial dicritical.
- **(G6) Affine-line source** `[P]/[L]` (Orevkov Lemma 2.1, PDF p. 2; degree-free):
  `l' ≃ A^1` for every affine-image dicritical, and `pi|_{l'}` identifies no two
  finite points, with no extra finite `L_C`-fibre points.

FALLACY-v2 flag/place/series: the four objects — a point `t ∈ l'`, its collapsed
image `pi(t)`, the normalization place `z = h_l(t) ∈ D~_i`, and the physical
point `eta_i(z) ∈ D_i` — are kept distinct throughout; no identification is made
anywhere below.

### 1.2 Lemma A (every component is a polynomial curve) `[D]`

> **Lemma A.** Let `D` be any component of `A_F` and `l` any affine-image
> dicritical with image `D`. Then `D~ ≃ A^1`, `D` has exactly one place at
> infinity, and `h_l : A^1 → A^1` is a degree-`s_l` polynomial map whose finite
> ramification satisfies `Σ_t (e_t − 1) = s_l − 1`.

*Proof.* By (G6), `l' ≃ A^1`; by (G3), `h_l : A^1 → D~` is finite surjective of
degree `s := s_l`. Let `D~^c` be the smooth projective model of `D~`, of genus
`g`, and `B = D~^c \ D~` its (nonempty, since `D~` is affine) set of places at
infinity. Extend to `h^c : P^1 → D~^c`, still of degree `s` and surjective. No
finite point of `A^1` maps into `B`, because `h_l(A^1) ⊆ D~`; and every point of
`B` has a preimage. Hence `B = {h^c(∞)}` is a single place and `∞` is its only
preimage, so `e_∞ = s`. Riemann–Hurwitz gives
`−2 = s(2g − 2) + (s − 1) + R_fin` with `R_fin = Σ_{finite}(e_t − 1) ≥ 0`. If
`g ≥ 1` the right side is `≥ 0`; hence `g = 0`, and then `R_fin = s − 1`. So
`D~^c ≃ P^1`, `|B| = 1`, `D~ ≃ A^1`. ∎

Lemma A answers the charge's question *"does Orevkov 2.1 force `A^1`
normalization per component at N = 5 as it did at N = 4?"* — **yes, and
unconditionally**: no trivial dicritical, no `mu = 1`, and no degree hypothesis
is used. ALLN/REV obtain `D~ ≃ A^1` only through the trivial dicritical
(`mu_0 = 1 ⟹ h_0` étale ⟹ `s_0 = 1`); the Riemann–Hurwitz step above shows the
étale input is needed only for `s_0 = 1`, not for `D~ ≃ A^1`. This matters
here: at `N ≥ 5` reducible, the components *without* a trivial dicritical get
`A^1` normalization for free, which is exactly what the componentwise
common-`eta` argument could not supply.

Independent confirmation `[L]`: Chau (arXiv:math/0305088), p. 1, records that
each irreducible component of `A_f` is parameterizable by a nonconstant
polynomial map `C → C^2` (attributed there to Jelonek), and Theorem 1 /
Corollary 2 (p. 2) prove that for a Keller `f` the whole set `A_f`, if nonempty,
is *a curve with one point at infinity*, every component carrying a
parametrization `ξ ↦ (Aξ^{md} + …, Bξ^{me} + …)` with one fixed coprime pair
`(d,e)`. Lemma A is the campaign-internal derivation of the first statement;
Chau's is the stronger global statement that **all components of `A_F` pass
through one common point of `L_∞`**, recorded here as `[L]` and used only for
structure typing in §5.

### 1.3 Lemma B (cover-ramification floor) `[D]`

> **Lemma B.** For every affine-image dicritical `l`:
> `corr_l = mu_l (s_l − 1) + K_l` with `K_l := Σ_t k_t ≥ 0`.
> In particular `corr_l ≥ mu_l (s_l − 1)`, hence `s_l ≤ 1 + corr_l / mu_l`.

*Proof.* By (G6) `pi` separates the finite points of `l'`, so
`corr_l = Σ_{t ∈ l'} (M_t − mu_l)`. By (G5) each summand is `≥ 0` and equals
`(e_t − 1) mu_l + k_t`. By Lemma A, `Σ_t (e_t − 1) = s_l − 1`. ∎

Lemma B is a **floor, not an attainment**: it bounds `s_l` from above and says
nothing about which germ realizes equality. It is the reducible-case workhorse,
because unlike the promoted transfer ("correction support = ramification support
of `h_l`", C19 §1.3) it does **not** require `eta` to be immersive, and therefore
applies on components carrying no trivial dicritical. Note the immediate
corollary, which recovers a promoted item without étaleness:
`mu_l = 1 ⟹ corr_l = 0 ⟹ s_l = 1`.

### 1.4 Local fibre identity and the aggregate identity `[D]`

Summing Orevkov's constant-multiplicity equation at an arbitrary point
`p ∈ A_F`, with `r_{i,p} := |eta_i^{-1}(p)|` the number of branches of `D_i` at
`p` (zero if `p ∉ D_i`) and `K_p := Σ_l Σ_{t ↦ p} k_t`:

```text
(LOC)    a_p + Σ_i r_{i,p} W_i + K_p = N          for every p in A_F.
```

For `p` generic on `D_i` this is (G2). Two consequences are used repeatedly:

- **(LOC-1) branch cap.** `r_{i,p} ≤ (N − K_p)/W_i`, since `a_p ≥ 0` and all
  terms are nonnegative.
- **(LOC-2) incidence cap.** If `D_i ∩ D_j ≠ ∅` then `W_i + W_j ≤ N`.

The aggregate Euler identity of ALLN generalizes as follows. Take
`Σ := Sing(A_F) ∪ {p : K_p > 0}` (finite), `sigma = |Σ|`, `sigma_i = |Σ ∩ D_i|`,
`nu_i = Σ_p (r_{i,p} − 1)`. With `D~_i ≃ A^1` (Lemma A),
`chi_c(D_i \ Σ) = 1 − nu_i − sigma_i`, and the covering/stratification argument
of ALLN §4.1 gives `Σ_i W_i chi_c(D_i \ Σ) = N − 1 − N·sigma + A_Σ`. Summing
(LOC) over `Σ` and substituting collapses everything to

```text
(AGG)    Σ_i W_i + K_tot = N − 1,        K_tot := Σ_{p in A_F} K_p.
```

Cross-check: in the irreducible case `(AGG)` reads `K_tot = a − 1`, which is
ALLN (4.6). Moreover `Σ_i W_i = Σ_l s_l mu_l`, so `(AGG)` is *identically*
(G1) + Lemma B. **Finding `[D]`: the aggregate Euler identity carries no
information beyond the Orevkov budget together with the local fibre identities.**
It is therefore not an independent gate in the reducible case, and no profile
below is killed by it. This is a load-bearing negative: it tells us where not
to spend the budget.

## 2. The reducible partition enumeration (m >= 2)

### 2.1 Cost multisets

A dicritical costs `mu_l + corr_l ≥ 1`. By (G4), `mu_l = 1 ⟹ corr_l = 0`, so a
trivial dicritical costs exactly 1. The budget (G1) is 4, and at least one
dicritical is trivial by scope. Hence the number `k` of affine-image dicriticals
satisfies `k ≤ 4`, and the remaining budget after the distinguished trivial is 3.

At least one dicritical has `mu ≥ 2`. *Reason* `[D]`: the meridian of `D_i` acts
on the 5 sheets with cycle type `1^{a_i} Π_{l→i} mu_l^{s_l}` (Lemma C, §3.3); if
every `mu_l = 1` every meridian is trivial, and since `pi_1(C^2 − A_F)` is
generated by meridians (Zariski–van Kampen) the covering
`C^2 \ F^{-1}(A_F) → C^2 \ A_F` would be trivial, forcing `N = 1`. This is the
Zariski–Nagata form of the promoted branch-locus nonemptiness (ALLN:190–211,
C19 §1).

Partitioning the residual 3 subject to `mu = 1 ⟹ corr = 0`:

| Profile | cost multiset | `k` | dicritical data `(mu, corr)` |
|---|---|---|---|
| **P1** | `3 + 1` | 2 | `(2,1)` and `(1,0)` |
| **P2** | `3 + 1` | 2 | `(3,0)` and `(1,0)` |
| **P3** | `2 + 1 + 1` | 3 | `(2,0)`, `(1,0)`, `(1,0)` |

`(1,2)` is excluded pointwise by (G4); `(2,0)+(1,1)` likewise; `(1,0)^{×4}` is
excluded by branch-locus nonemptiness. This reproduces exactly the list (5.3)
of ALLN §5.2 and REV §6.2, which was left with "target-component incidence and
cover degrees still undetermined". Those are now determined.

### 2.2 Cover degrees are forced

Lemma B gives `s_l ≤ 1 + corr_l / mu_l` for every dicritical, hence:

- P1: trivial `s = 1`; the `(2,1)` carrier has `2(s − 1) ≤ 1`, so **`s = 1`** and
  `K_l = corr_l − mu_l(s_l − 1) = 1`.
- P2: `(3,0)` gives `3(s − 1) ≤ 0`, so **`s = 1`**; `K_tot = 0`.
- P3: `(2,0)` gives **`s = 1`**; all three have `s = 1`; `K_tot = 0`.

So **every dicritical in every `N = 5` reducible profile carrying a trivial
dicritical has `s_l = 1`** `[D]`. Consequence: by Lemma A each `h_l` is an
isomorphism, `phi_l` is a birational parametrization of its component, and the
promoted *ramified-nonprimitive escape* — the exact residue that leaves
`OPEN[B0-H2-N>=20/…]` alive in the irreducible case — **cannot occur at `N = 5`
in the reducible case at all.** The `N ≥ 5` reducible gap is therefore not a
ramified-cover gap at `N = 5`; it is purely a component-incidence and
`pi_1`-representation gap. (At `N ≥ 6` the floor stops forcing `s = 1`: the
first reducible profile with a ramified carrier is `(2,2)+(1,0)` at `N = 7`,
`s = 2`, `K = 0`.)

Consistency with (AGG): P1 `Σ W_i = 2 + 1 = 3`, `K_tot = 1`, total 4 ✓;
P2 `3 + 1 + 0 = 4` ✓; P3 `2 + 1 + 1 + 0 = 4` ✓.

### 2.3 Incidence: which component owns the trivial dicritical

Each component is the image of at least one dicritical (promoted "distinct owners
per component"), so the assignment `tau` is onto `{1,…,m}` and `2 ≤ m ≤ k`.
Enumerating all surjections up to relabelling of like dicriticals:

| ID | profile | `m` | ownership | `(W_i, a_i)` per component |
|---|---|---|---|---|
| **P1** | `(2,1)+(1,0)` | 2 | `D_A ← (2,1,s=1)`, `D_B ← (1,0,1)` | `(2,3)`, `(1,4)` |
| **P2** | `(3,0)+(1,0)` | 2 | `D_A ← (3,0,1)`, `D_B ← (1,0,1)` | `(3,2)`, `(1,4)` |
| **P3a** | `(2,0)+(1,0)+(1,0)` | 3 | `D_A ← (2,0,1)`; `D_{B1}`, `D_{B2}` one trivial each | `(2,3)`, `(1,4)`, `(1,4)` |
| **P3b** | same | 2 | `D_A ← (2,0,1)`; `D_B ← both trivials` | `(2,3)`, `(2,3)` |
| **P3c** | same | 2 | `D_1 ← (2,0,1)+(1,0,1)`; `D_2 ← (1,0,1)` | `(3,2)`, `(1,4)` |

That is the complete list: with `k = 2` a surjection onto `m = 2` forces the two
dicriticals onto distinct components (P1, P2); with `k = 3` and `m = 3` we get
P3a, and with `m = 2` the only two partition shapes are `{A}{B1,B2}` = P3b and
`{A,B1}{B2}` = P3c (the relabelled `{A,B2}{B1}` is the same configuration).
All entries satisfy `a_i ≥ 1`.

**Structural corollary `[D]` (unique branched component).** In every row above
exactly one component has a dicritical with `mu ≥ 2`, hence exactly one
component has nontrivial meridian. *Reason*: a second branched component would
need a second `mu ≥ 2` dicritical, costing `≥ 2`, and `1 + 2 + 2 = 5 > 4`.
So at `N = 5`, in the reducible-with-trivial scope, **the branch locus of the
covering is irreducible**. Every profile therefore reduces to a `pi_1` question
about one irreducible polynomial curve — the same shape as `OPEN[PI1-S4]`, and
not a genuinely multi-component representation problem. This is the single most
useful structural fact produced by this lane.

## 3. Per-component eta-criticality and the normalization question

### 3.1 Which components inherit immersivity

The promoted transfer ("every correction is ramification of `h_l`"; C19 §1.3)
is derived from `d phi_l = d eta ∘ d h_l` **plus** immersivity of `eta`, and
immersivity of `eta_i` is obtained from a trivial dicritical *over `D_i`*
(ALLN §2). In the reducible case this is available only componentwise. Here is
the exact inheritance at `N = 5`, using §2.2 (`s_l = 1` everywhere):

- If `corr_l = 0` for some `l → D_i` with `s_l = 1`, then `h_l` is an
  isomorphism and (G4) gives `d phi_l ≠ 0` everywhere, so `d eta_i ≠ 0`
  everywhere: **`eta_i` is immersive, every branch of `D_i` is smooth, and every
  singular point of `D_i` is multibranch.**
- If `corr_l > 0` with `s_l = 1` (the single case P1, `corr = 1`), then
  `h_l` is an isomorphism, so the criticality forced by (G4) has nowhere to go
  except `d eta_i`: **`eta_i` is critical at exactly the correction parameters,
  and `D_i` carries exactly that many singular branches.**

So at `N = 5` the reducible case *inverts* the irreducible all-degree picture:
because the floor kills every ramified carrier, `eta`-criticality is not
scope-corrected away — it is exactly right, as it was at `N = 5` irreducible
(REV §5). The promoted transfer correction is consumed here only as the
statement that it is vacuous at this degree.

### 3.2 The normalization question, answered

Lemma A settles the charge's per-component normalization question outright: at
`N = 5` (indeed at every degree) every component of `A_F` has `A^1`
normalization and one place at infinity, i.e. is a **polynomial curve** in the
PI1-S4 sense; with `s_l = 1` (§2.2) each is moreover *birationally* parametrized
by its dicritical, so `eta_i = phi_i ∘ (h_i)^{-1}` is a proper polynomial
parametrization `t ↦ (p_i(t), q_i(t))`. Consequently every promoted result whose
hypothesis class is "irreducible polynomial curve, normalization `A^1`, one
place at infinity, affine singularities of prescribed type" is *directly*
applicable to the `N = 5` reducible residual — in particular Corollary N-A-RES
and the (M-INF) cluster identity (CNA §1.2–1.3). That transferability is the
main leverage this lane hands to the row machinery.

### 3.3 Lemma C (meridian dictionary) `[D]`

> **Lemma C.** Let `p` be a point of `D_i` and `gamma_i` a meridian of `D_i`.
> Then `gamma_i` acts on the 5 sheets with cycle type
> `1^{a_i} Π_{l→i} mu_l^{s_l}`. Locally at any `p ∈ A_F`, writing `G_p` for the
> image of `pi_1(B_p \ A_F)`,
> `#Fix(G_p) = a_p + (number of 1-cycles at infinity over p)`,
> and the sheets not fixed are exactly those in the clusters counted by (LOC).

*Proof.* Over a small transversal disc at a generic point of `D_i`, the `N`
sheets split as: `a_i` affine preimages, at each of which `F` is a local
isomorphism (Keller), hence fixed 1-cycles; and, for each `l → i` and each of
the `s_l` points of `phi_l^{-1}(p)`, one cluster of `mu_l` sheets permuted
cyclically by the local model `f^*(z,w) = (z + O(w), w^{mu_l}·unit)` of Orevkov
Lemma 3.1. For the local statement at special `p`: an affine preimage `x` gives
a component of `F^{-1}(B_p \ A_F)` mapped isomorphically (again since `F` is
étale at `x`), i.e. a fixed letter; the remaining fixed letters are 1-cycles
belonging to clusters at infinity, which by the same local model occur exactly
when some `mu_l = 1`. ∎

Two immediate `N = 5` gates:

- **(M-1)** A component all of whose dicriticals have `mu = 1` has trivial
  meridian; killing those meridians, the monodromy factors through
  `pi_1(C^2 − D_br)` where `D_br` is the unique branched component (§2.3).
- **(M-2)** `Im(pi_1(C^2 − A_F) → S_5)` is transitive, because
  `C^2 \ F^{-1}(A_F)` is the complement of a curve in `C^2`, hence connected,
  and it is the total space of the covering.

## 4. Gates applied: profile-by-profile kill sheet

### 4.1 Gate AMS: a smooth branched component is a coordinate line

> **Gate AMS `[D]`.** Suppose the branched component `D_br` has
> `corr_l = 0` for all `l → D_br` and `W_br ≥ 3`. Then `D_br` is smooth,
> `eta_br` is a closed embedding, `D_br` is a coordinate line of `C^2`
> (Abhyankar–Moh–Suzuki), `pi_1(C^2 − D_br) = Z`, the monodromy image is cyclic,
> and by (M-1)+(M-2) it must be transitive on 5 letters — impossible, since a
> cyclic group generated by a permutation of type `1^{a} Π mu^s` with `a ≥ 1` has
> a fixed letter. **The profile dies.**

*Detail.* `corr = 0` and `s = 1` give `eta_br` immersive (§3.1), so every branch
is smooth; by (LOC-1) with `K_p = 0`, `r_{br,p} ≤ 5/W_br < 2`, so `D_br` is
unibranch at every point, i.e. `eta_br` is injective and immersive, hence a
closed embedding of `A^1`. AMS (Abhyankar–Moh 1975; Suzuki 1974 — classical,
consumed without a local hashed PDF and flagged as such in §8) makes it a
coordinate line, whose complement is `C^* × C`.

**KILL P2.** `W_A = 3`, `corr_A = 0`: Gate AMS applies verbatim. (Its meridian
type would have been `1^2 3`, a 3-cycle; the surviving cyclic image `Z/3` fixes
two letters.) A cross-check without AMS: `deg D_A ≥ 2` from Gate TG below, while
Gate AMS forces degree 1.

**KILL P3c.** `D_1` carries `(2,0,1)` and `(1,0,1)`, so `W_1 = 3`, all
`corr = 0`: Gate AMS applies verbatim. Its meridian type is
`1^{a_1} · 2^1 · 1^1 = 1^3 2`, a transposition; the cyclic image `Z/2` is
intransitive on 5 letters. The presence of the second component `D_2` does not
help: killing its (trivial) meridians only moves the surjection to
`pi_1(C^2 − D_1)`.

Gate AMS is exactly the `N = 5` reason why **the trivial dicritical cannot share
its component with the `mu ≥ 2` dicritical**: sharing pushes `W` to 3, which
starves the fibre so hard that the component must be smooth.

### 4.2 Gate LOC on the surviving branched component

For the survivors `W_br = 2`, `a_br = 3`, and (LOC) at `p ∈ D_br` reads
`a_p = 5 − 2 r_{br,p} − Σ_{j≠br} W_j r_{j,p} − K_p`. With `a_p ≥ 0`:

- `r_{br,p} ≤ 2`: **`D_br` has no point of three or more branches.** In
  particular the promoted `(6,4)` counterexample curve of CNA §1.3 (`beta_h = 15`
  via an *ordinary triple point*) is out of class here for the same reason it was
  out of class at `N = 4`.
- at a 2-branch point with `K_p = 0`: `a_p = 1`;
- at a 2-branch point with `K_p = 1`: `a_p = 0`;
- at a point of `D_br ∩ D_j` (`W_j = 1`): `a_p = 5 − 2r_{br,p} − r_{j,p} − K_p`,
  so (LOC-2) permits the intersection and no incidence is excluded.

**Finding `[D]`: component incidence is not an obstruction at `N = 5`.** Every
incidence pattern allowed by (LOC-2) is arithmetically consistent; the charge's
"component-incidence" half of the OPEN name is answered negatively — the gap is
entirely in the `pi_1` half.

### 4.3 Gate TG: the transversal-genus identity

> **Gate TG `[D]`.** Let `L ⊂ C^2` be a generic line in the target,
> `S_i := Σ_{l→i} s_l`, and let `Σ_∞ := Σ_j sigma_j` where the sum is over the
> divisor components at infinity mapping *onto* `L_∞`, with degrees `sigma_j`
> and multiplicities `nu_j` (so `Σ_j sigma_j nu_j = N`, whence `1 ≤ Σ_∞ ≤ N`).
> Then, with `g` the genus of the smooth model of `F^{-1}(L)`,
>
> ```text
> 2g + Σ_∞  =  2 − N + Σ_i (deg D_i) · Σ_{l→i} s_l (mu_l − 1).
> ```

*Proof.* `F^{-1}(L)` is smooth (`F` is étale) and connected: by Zariski's
hyperplane-section theorem `pi_1(L \ A_F) ↠ pi_1(C^2 − A_F)` for generic `L`, so
the monodromy on `L` is still transitive by (M-2), making `F^{-1}(L \ A_F)`
connected and dense in `F^{-1}(L)`. Multiplicativity of `chi_c` over the
`N`-sheeted covering plus the fibre counts gives
`chi(F^{-1}(L)) = N(1 − Σ_i deg D_i) + Σ_i a_i deg D_i = N − Σ_i W_i deg D_i`
(a generic `L` meets `D_i` in `deg D_i` points, all generic on `D_i`). The
places at infinity of `F^{-1}(L)` are: over each of the `deg D_i` points of
`L ∩ D_i`, one branch at each of the `S_i` points of the dicritical fibre — one,
not more, because the local model `f^*(z,w) = (z + O(w), w^{mu} · unit)` pulls a
transversal back to `z = const + λ^{-1} w^{mu}(…)`, a single smooth branch; plus,
over the generic point `q_∞ = L̄ ∩ L_∞`, one branch at each of the `Σ_∞` points
of the fibre of the `L_∞`-dicriticals. Generic `L` avoids the finitely many
image points of contracted components. So `b = Σ_i S_i deg D_i + Σ_∞`, and
`chi = 2 − 2g − b` closes the identity. ∎

*Control.* For `N = 1` (an automorphism, `A_F = ∅`, one `L_∞`-dicritical with
`sigma = nu = 1`) the identity reads `0 + 1 = 2 − 1 + 0` ✓, and `chi = 1` ✓.

At `N = 5` with all `s_l = 1` and a single `mu ≥ 2` dicritical over `D_br`:

```text
(deg D_br) · (mu_br − 1) = 3 + 2g + Σ_∞ ≥ 4.
```

So for the survivors (`mu_br = 2`): **`deg D_br = 3 + 2g + Σ_∞ ≥ 4`**, in *any*
coordinate system, hence also `d_min ≥ 4` in the sense of the promoted
D1-DEGREE typing (CNA §1.4; raw-degree phrasings are barred, so the payoff is
stated for `d_min` as well as for the ambient degree).

**Independent confirmation of `deg ≥ 4` `[D]`.** By Zariski's theorem
`pi_1(C^2 − D_br)` is generated by the `d = deg D_br` meridians of a generic
line; their images are transpositions generating a transitive subgroup of `S_5`,
so the graph on 5 vertices whose edges are those transpositions is connected and
needs `≥ 4` edges. Hence `d ≥ 4`. Two structurally independent routes (Euler
characteristic vs. generation) give the same bound; at `N = 4` the same two
arguments give `d ≥ 3`, consistent with the promoted `S_4` survivor list which
begins at `(4,3)`.

### 4.4 Gate N-A-RES (transfer of the promoted row machinery)

Corollary N-A-RES (CNA §1.2) is a statement about a curve, not about `N`: for
`D` an irreducible polynomial curve all of whose singularities are double points
of two smooth branches, `M_∞ + 2T ≤ 3d − 3` implies `pi_1(C^2 − D) = Z`. By
§3.2 the surviving branched component of P3a/P3b is exactly in that class, so:

> **Gate N-A-RES at `N = 5` `[P]`.** Whenever the promoted gate fires,
> `pi_1(C^2 − D_br) = Z`, the image is cyclic, and transitivity on 5 letters
> fails. The profile dies.

Standing correction consumed: use `4T` rather than `2T` as the tangential charge
until `OPEN[NORI-BC-SELF-TANGENT-COEFF]` settles (CNA §3); at `T = 0` the gate
is verbatim (M-INF), which is the promoted-as-corrected cluster identity
`M_emb = mult + beta_h − 1`. What does **not** transfer is every ROW-SWEEP kill
that consumed the `S_4` Main Theorem — specifically the two degree-six
tangential kills `(6,3)-(7,4)` and `(6,3)-(8,3)`, which reduce to a *coprime*
row and then invoke "no surjection onto `S_4` with transposition meridians".
There is no promoted `S_5` analogue, so **at `N = 5` the coprime stratum is
wide open** even where it was closed at `N = 4`. The `N = 5` residual is
strictly larger than the `N = 4` residual, not smaller.

### 4.5 Kill sheet

| profile | gate | verdict |
|---|---|---|
| `(1,0)^{×4}` (no `mu ≥ 2`) | Zariski–Nagata / (M-2) | KILLED |
| `(2,0)+(1,1)`, `(1,2)` | (G4) pointwise | KILLED |
| any `s_l ≥ 2` | Lemma B floor | EXCLUDED (no such profile exists at `N = 5`) |
| two branched components | budget (§2.3) | EXCLUDED |
| **P2** `(3,0)+(1,0)` | Gate AMS (`W = 3`, `corr = 0`) | **KILLED** |
| **P3c** `(2,0)+(1,0)` on one component | Gate AMS (`W = 3`) | **KILLED** |
| **P1** `(2,1)+(1,0)`, `m = 2` | survives all gates | **SURVIVOR S1** |
| **P3a/P3b** `(2,0)+(1,0)+(1,0)` | survives all gates | **SURVIVOR S2** |
| S2 rows with `M_∞ + 2T ≤ 3d − 3` | Gate N-A-RES `[P]` | KILLED row-by-row |

## 5. Survivors, fully typed (the N=5 residual cage)

Two configurations survive every gate. Both have the same shape: **one branched
component `D_br` with `(W, a) = (2, 3)` and meridian a transposition, plus one
or two unbranched polynomial-curve components carrying the trivial
dicritical(s).** They differ only in whether the branched component carries a
correction.

### 5.1 Survivor S1 (from P1) — the cuspidal cage

| item | value |
|---|---|
| dicriticals | `l_A = (mu, corr, s) = (2, 1, 1)` over `D_A`; `l_B = (1, 0, 1)` over `D_B` |
| components | `m = 2`; `(W_A, a_A) = (2, 3)`, `(W_B, a_B) = (1, 4)` |
| corrections | `K_tot = 1`, all of it at one parameter `t_0 ∈ l'_A` |
| meridians | `gamma_A` of type `1^3 2`; `gamma_B` trivial |
| `D_A` | polynomial curve, `D~_A ≃ A^1`, one place at infinity, birationally parametrized; `eta_A` critical at exactly one parameter `t_0` |
| the special point | `p_0 = eta_A(t_0)`, `M_{t_0} = e·mu + k = 2 + 1 = 3`; the branch at `p_0` is **singular** |
| other singularities of `D_A` | double points of two smooth branches only (`r ≤ 2` by (LOC-1)), each with `a_p = 1` |
| `D_B` | polynomial curve, `eta_B` immersive, all branches smooth, `a_p = 5 − r_{B,p}` off `D_A` |
| degree | `deg D_A = 3 + 2g + Σ_∞ ≥ 4` (Gate TG); `deg D_B ≥ 1` |

Sub-cases at `p_0`, from (LOC) with `K_{p_0} = 1`:

- **S1a** `r_{A,p_0} = 1` (unibranch cusp): `a_{p_0} = 2` if `p_0 ∉ D_B`, and
  `a_{p_0} = 2 − r_{B,p_0}` if `p_0 ∈ D_B`. In both cases Lemma C gives
  `#Fix(G_{p_0}) = 2` exactly.
- **S1b** `r_{A,p_0} = 2` (the singular branch shares `p_0` with a smooth
  branch of `D_A`): `a_{p_0} = 0`, `#Fix(G_{p_0}) = 0`, cluster sizes `3 + 2`.

**Why this is genuinely new relative to `N = 4`.** The `N = 4` residual
(C19 §1, ALLN §5.2) had `corr = 0` on both dicriticals, so its branched
component had only double points of smooth branches. At `N = 5` the budget is
one unit larger and P1 spends it on a correction, which — because Lemma B
forbids a ramified cover here — is forced onto `d eta_A`. So **S1 is a
cuspidal-curve residual with no `N = 4` analogue**, and it sits *outside* the
hypothesis class of the promoted Theorem N-A / Corollary N-A-RES, which require
every singularity to be a double point of two smooth branches. No promoted gate
reaches S1.

### 5.2 Survivor S2 (from P3a/P3b) — the PI1-S5 cage

| item | value |
|---|---|
| dicriticals | `l_A = (2, 0, 1)` over `D_A`; two trivials `(1, 0, 1)`, on two distinct components (P3a) or both on one (P3b) |
| components | `m = 3` or `m = 2`; `(W_A, a_A) = (2, 3)`; trivial-owner components have `W = 1, a = 4` (P3a) or `W = 2, a = 3` (P3b) |
| corrections | `K_tot = 0` — every `eta_i` immersive, every branch of every component smooth |
| meridians | `gamma_A` of type `1^3 2`; all others trivial |
| `D_A` | irreducible polynomial curve, one place at infinity, **all affine singularities double points of two smooth branches (tangency allowed)**, `a_p = 1` at each |
| degree | `deg D_A = 3 + 2g + Σ_∞ ≥ 4` |

`D_A` is in *exactly* the promoted PI1-S4 residual class, with `S_5` in place of
`S_4`. Every gate in that class transfers except those that consumed the `S_4`
Main Theorem (§4.4).

### 5.3 Delta budget and the shared point at infinity

Both survivors obey, with `δ := deg D_br`,

```text
δ_∞ + δ_aff = (δ − 1)(δ − 2)/2,     δ = 3 + 2g + Σ_∞ ≥ 4,
δ_aff = Σ_{double points} k_p        (S2),
δ_aff = δ_{p_0} + Σ_{other double points} k_p   (S1),
```

where `k_p ≥ 1` is the contact order of the two smooth branches at `p` and
`δ_{p_0} ≥ 1` is the delta invariant of the singular germ at `p_0`. At the
minimum `δ = 4` the whole affine budget is `3 − δ_∞`. No promoted datum bounds
`δ` from above; consistently with the promoted D1-DEGREE typing (CNA §1.4),
degree payoffs are stated for `d_min`, and Gate TG gives `d_min ≥ 4`.

Chau `[L]` (Theorem 1, Corollary 2, arXiv:math/0305088 pp. 1–2) adds two
structure pins that hold for both survivors and have no analogue in the charged
inputs: (i) every component of `A_F` is parametrized as
`ξ ↦ (A ξ^{m_i d} + …, B ξ^{m_i e} + …)` with one fixed coprime pair `(d, e)`
independent of the component, so all component degrees are multiples of a common
`max(d, e)` and the ratio `deg p_i / deg q_i` is the same for every component;
(ii) `A_F` has **one point at infinity** — the branched component and every
unbranched component meet `L_∞` at the *same* point, each with a single place
there, with Newton–Puiseux `u = c v^{d/e} + …`. So the reducible cage is not
"several unrelated curves": it is a bouquet of polynomial curves, pairwise
tangent to one common direction at one common point of `L_∞`, of which exactly
one is branched.

## 6. S_5 monodromy typing of the survivors

The cover is 5-sheeted and the monodromy `rho : pi_1(C^2 − A_F) → S_5` is
transitive (M-2) and generated by meridians. Per profile, from Lemma C:

| profile | `D_br` meridian | other components | image |
|---|---|---|---|
| P1 (S1) | `1^3 2` — transposition | `1^5` | `S_5` |
| P2 | `1^2 3` — 3-cycle | `1^5` | cyclic `Z/3` ⇒ killed |
| P3a/P3b (S2) | `1^3 2` | `1^5` | `S_5` |
| P3c | `1^3 2` | `1^5` | cyclic `Z/2` ⇒ killed |

**Global typing of the survivors `[D]`.** In both S1 and S2 all meridians of
`D_br` are conjugate transpositions, the meridians of every other component die,
and `rho` factors through `pi_1(C^2 − D_br)`. A transitive subgroup of `S_5`
generated by transpositions is `S_5`, so `rho` is a **surjection onto `S_5` with
every meridian a transposition** — the exact `N = 5` analogue of the promoted
`OPEN[PI1-S4]` statement. There is no second monodromy class to consider: the
`N = 4` campaign had to close an `A_4` class and a transposition class
separately, whereas at `N = 5` the budget forces the transposition class alone.

**Local typing at each singular point of `D_br`.**

- *Double point of two smooth branches (S1 and S2).* `a_p = 1`, no 1-cycles at
  infinity over `p` (both places carry a `mu = 2` cluster), so `#Fix(G_p) = 1`
  by Lemma C. The two branch meridians commute (they commute for a node, and
  for a tacnode the relation `(τ_1τ_2)^k = (τ_2τ_1)^k` forces commuting images
  among transpositions unless they share a letter, which is excluded next).
  Two commuting transpositions in `S_5` are equal (3 fixed letters) or disjoint
  (1 fixed letter); sharing a letter gives 2 fixed letters. Only **disjoint**
  matches `#Fix = 1`. This is verbatim the `N = 4` disjointness constraint, with
  fixed-letter count 1 instead of 0.
- *The extra singular point `p_0` of S1a.* `#Fix(G_{p_0}) = 2`, so `G_{p_0}`
  moves exactly 3 letters with no fixed letter among them; hence the 3 moved
  letters form a single orbit and `G_{p_0} ≅ S_3` acting naturally. The germ at
  `p_0` is unibranch, so its link is an algebraic knot `K` and the requirement is
  a surjection of the local knot group onto `S_3` with meridian ↦ transposition,
  i.e. an irregular dihedral 3-fold cover; classically this exists iff
  `3 | det(K) = |Δ_K(−1)|`. Desk verification on `T(2,n)` germs (`y^2 = x^n`),
  where the local group is `⟨a, b | aba… = bab…⟩` with `n` letters on each side:
  with `a = (12)`, `b = (23)` the relation holds iff `(n−1)/2 ≡ 1 (mod 3)`, i.e.
  iff `3 | n`. So the ordinary cusp `(2,3)` is admissible, `(2,5)` and `(2,7)`
  are **excluded**, `(2,9)` is admissible; the `(3,4)` germ (`det = 3`) is
  admissible. This is a real, cheap, `N = 5`-specific gate on the S1 cage.
- *The extra singular point `p_0` of S1b.* `#Fix(G_{p_0}) = 0`, cluster sizes
  `3 + 2`; the germ is two branches, one singular one smooth, and the local
  group has no fixed letter. Orbits are unions of clusters, so the orbit
  partition is `{5}` or `{3, 2}`; the second forces the same `S_3` dihedral
  condition on the singular branch plus a disjoint transposition for the smooth
  one.

**Generation floor.** The images of the `δ = deg D_br` meridians of a generic
line form a connected graph on 5 vertices, so at least 4 distinct transpositions
occur, and `δ ≥ 4` (§4.3). In S1 the cuspidal point contributes only the 3
letters of an `S_3`, so at least one further double point is needed to reach the
remaining 2 letters: **S1 with no other singularity is impossible.** In
particular the cuspidal cubic `y^2 = x^3` — whose complement group is the
trefoil/braid group `B_3`, image at most `S_3` — is excluded, consistent with
`δ ≥ 4`.

## 7. Decision questions (PI1-S4 style)

Stated in the same shape as `OPEN[PI1-S4]`, so that a decision lane can consume
them directly. All four are decision questions, not claims.

> **DQ-1 `OPEN[PI1-S5-NODAL]`.** Let `D` be an irreducible polynomial curve
> (normalization `A^1`, one place at infinity, `deg D ≥ 4`) every affine
> singularity of which is a double point of two smooth branches (tangency
> allowed). Does there exist a surjection `pi_1(C^2 − D) ↠ S_5` sending every
> meridian to a transposition, with the two local meridians at each double point
> **disjoint** transpositions? A negative answer kills Survivor **S2**.

> **DQ-2 `OPEN[PI1-S5-CUSP]`.** Same question for `D` with, in addition,
> exactly one singular *branch*, at a point `p_0` where the local monodromy group
> is `S_3` moving exactly 3 letters (S1a: `p_0` unibranch, germ link with
> `3 | det`; S1b: `p_0` a two-branch point, one branch singular, no fixed
> letter, clusters `3 + 2`), the correction budget being `M_{t_0} = 3` exactly.
> A negative answer kills Survivor **S1**. Note that **no promoted gate reaches
> this class**: Theorem N-A, Corollary N-A-RES and the whole (M-INF) cluster
> assume every singularity is a double point of two smooth branches. The
> cheapest sub-question: *does the `S_3` dihedral condition at `p_0` plus
> disjointness at every other double point already over-determine the
> `(δ, n)` row?*

> **DQ-3 `OPEN[N5-DEGREE-CAP]` — highest leverage.** Is there a valid bound of
> Jelonek type `deg A_F ≤ N − 1` (or any bound `≤ 4` at `N = 5`) for the
> non-proper value set of a Keller map? If so, both survivors die immediately:
> `m ≥ 2` and Gate TG give `deg A_F ≥ deg D_br + 1 ≥ 5 > 4`, closing the whole
> reducible-with-trivial case at `N = 5` in one line. **UNVERIFIED**: no hashed
> source for any such bound was obtained in this lane, and none of the four
> charged inputs contains one. Chau's Corollary 1 (`[L]`, hashed) does bound the
> shape of `R_0(u,v)` but in terms of `deg P`, `deg Q`, not of `N`; it is not a
> substitute. This is typed as a literature-custody question, not as a gate.

> **DQ-4 `OPEN[ROW-TRANSFER-S5]`.** Which of the promoted row results survive
> the replacement `S_4 → S_5`? Confirmed transferable here: Corollary N-A-RES
> and the corrected cluster identity `M_emb = mult + beta_h − 1` (curve-level,
> `N`-free). Confirmed **not** transferable: the two ROW-SWEEP degree-six
> tangential kills, and the entire coprime-stratum closure, both of which consume
> the `S_4` Main Theorem. Question: is there an `S_5` coprime-stratum theorem, or
> does `S_5` genuinely admit transposition tuples where `S_4` did not (the fork
> in the promoted Theorem A was order-3/order-4 specific)? Until this is
> answered, **the `N = 5` reducible residual is strictly larger than the `N = 4`
> one**, and the `N = 4` survivor row list must not be reused.

## 8. OPEN items and lane status

**What this lane settled** (all `[D]` from promoted inputs plus hashed primary
sources, none an attainment claim): every component of `A_F` is a polynomial
curve at every degree (Lemma A); `corr_l ≥ mu_l(s_l − 1)` on every component,
without immersivity (Lemma B); hence at `N = 5` reducible-with-trivial every
`s_l = 1`, so the ramified-nonprimitive escape is absent at this degree; the
aggregate Euler identity is equivalent to the budget plus the local fibre
identities and is not an independent gate; the branch locus is irreducible;
component incidence obstructs nothing; two profiles die (P2, P3c) by Gate AMS;
`deg D_br = 3 + 2g + Σ_∞ ≥ 4` by two independent routes; and the residual is the
two cages S1, S2 with the `S_5` typing of §6.

**`OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS]` after this
lane.** At `N = 5` the name is now inaccurate in both halves: incidence is not
an obstruction and there are no ramified covers. The residual is
`OPEN[PI1-S5-NODAL]` (DQ-1) and `OPEN[PI1-S5-CUSP]` (DQ-2), plus the custody
question DQ-3 and the transfer question DQ-4. `N ≥ 6` is untouched here; the
first reducible profile with a ramified carrier is `(2,2)+(1,0)` at `N = 7`
(`s = 2`, `K = 0`), so the ramified half of the OPEN name first becomes live at
`N = 7`, and `N = 6` should be run next as a bounded repeat of §2 with budget 5.

**`[A]` AUDIT-1 — a gap in the consumed `N ≤ 19` chain (irreducible lane, not
this one).** ALLN (4.6) reads `Σ_{p ∈ Σ} K_p = a − 1` with `Σ = Sing D`, and
REV §4.3 confirms it. The identity derived here, `(AGG)`, gives
`Σ_{all p} K_p = a − 1`. The two agree only if `K_p = 0` at every *smooth* point
of `D`. But ALLN §3.2 and REV §3.2 both explicitly allow a critical point of
`h_l` over a smooth point (`eta` immersive, `h_l(t) = u_0 + t^e`, reduced image
smooth) and call it "the escape". If such a point exists, then either `Σ` must
be enlarged to contain it — and then `nu ≥ sigma` fails, so the term
`(N − a)(nu − sigma)` in (4.1) is no longer nonnegative and the `2a > N` step
breaks — or (4.6) becomes a strict inequality and `a − 1 ≤ dR` (4.7) no longer
follows, since a smooth-point bound is `K_p ≤ a`, not `K_p ≤ d`. Typed
**GAP-CANDIDATE**, not REFUTED: the `N ≤ 19` conclusion may well survive via a
proof that every correction image is singular, which would be a clean repair.
Recommended routing: the irreducible lane, with the repair target *"every
critical point of every correction-bearing `h_l` maps to a singular point of
`D`"*. **Nothing in this report depends on (4.6), (4.7), or `2a > N`**; at
`N = 5` reducible the issue is vacuous, since `R = 0`.

**`[A]` AUDIT-2 — classical citations consumed without a local hashed PDF**, and
therefore flagged rather than promoted: Abhyankar–Moh (1975) / Suzuki (1974)
(Gate AMS); Zariski's hyperplane-section theorem for a generic line (Gate TG and
the generation floor); Fox's dihedral-cover criterion `3 | det(K)` (§6, whose
`T(2,n)` instance was verified at desk here by direct braid-relation
computation). Each is standard, but a custody lane should hash them before any
of the three is promoted.

**Provisional/unreviewed status.** Everything typed `[D]` in this report is
UNREVIEWED and should be routed to a different-model hostile gate before
promotion — in particular Lemma A, Lemma B, Gate TG and the `(AGG)` collapse,
which are the four items that carry the lane. No exit-price basis line is declared, because no
new exit price is asserted anywhere above.

**FALLACY-v2 self-check.** Flag/place/series: the four objects `t`, `pi(t)`,
`z = h_l(t)`, `eta(z)` are never identified (§1.1). Carrier/attainment: S1 and
S2 are necessary cages, not witnesses; no Keller map is claimed to realize
either. Floor/attainment: Lemma B, `deg ≥ 4`, and `Σ_∞ ≥ 1` are floors, used
only in the direction that tightens the cage. Pole/interior, `sat()`, raw
remainder, variable/ring map, merge-free, target/arrival: not in play. No gap
was filled by cap or analogy; DQ-3 is typed UNVERIFIED rather than consumed.


<!-- BODY-END -->
