# PI1S4-(6,4) FOLD-REDUCTION — braid-free kill attempt on the (6,4) row

Lane: OPEN[PI1S4-(6,4)-FOLD-REDUCTION]. Model: Opus 5. Date: 2026-08-31.

## 0. Inputs, hashes, and consumption typing

## 1. The fold: what quantifies over the row, what is witness-specific

### 1.1 Witness data and the fold identity

### 1.2 Row-level quantification of `p = r^2`

### 1.3 Target-automorphism normal form and the fold-existence condition

## 2. Structure of `D' cup D'^-`

### 2.1 The involution and the intersection locus

### 2.2 Intersection number and local types

### 2.3 Behaviour at infinity

## 3. The restriction/cover argument, re-derived

## 4. Two-component machinery

### 4.1 Theorem N-A hypothesis test, component by component

### 4.2 Gap quantification

### 4.3 Alternate routes (aggregate / ZvK on the union / conversion law)

## 5. Verdict

## 6. Typed residuals and successor tasks

*(sections are appended in order; the body is sealed by the standalone marker at the end)*

## 0. Inputs, hashes, and consumption typing

Three charged inputs were hashed with `shasum -a 256` **before any was read**; 3/3 match:

```text
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  pi1s4-64-fixed-tuple-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

No literature was fetched: nothing below needs a hashed source. Every step is either
classical (Bézout; Puiseux; Newton-polygon/toric intersection theory; adjunction;
branched-cover transfer), or promoted, or derived here.

**Typing.**

* `PROMOTED` — integration `126c2d29` §1: **Theorem N-A** (hypotheses: `X` smooth
  projective; `D,E` reduced, no common components; every singular point of `D` a double
  point of two smooth branches of contact `k_p ≥ 1`; `D ∪ E` normal-crossing along
  `D − Sing D`; `E ∩ Sing D = ∅`; conclusion under `C² > 2r₁(C)+4T(C)+T_x(C)` for every
  irreducible `C ⊆ D`: `ker(π₁(X−(D∪E)) → π₁(X−E))` f.g. abelian with finite-index
  centraliser); **Lemma 3.2** (blow-up invariance of that kernel); **Corollary N-A-RES**;
  the corrected **M-INF piece 1** `M_emb = mult + β_h − 1`; **D1-DEGREE** at typed scope.
  Per the lane charge also the **coprime no-`S₄` theorem** (integration §2 row line
  `(6,3)`: a coprime-type one-place nodal polynomial curve admits no
  `π₁(C²−C) ↠ S₄` with meridians ↦ transpositions).
* `PROVISIONAL` — all ROW-SWEEP row data (`Δ=(6,4,3)`, `β₁=15`, `δ_∞=7`, `δ_aff=3`,
  `M_∞=16`), the explicit witness `r,q,p=r²`, and the `(8,4)` equivalence `P=p+q²`.
  Also PROVISIONAL: the FIXED-TUPLE restriction theorem of its §9 (re-derived in §3
  below, so this lane does not depend on it).
* `PROVED-HERE` — everything else, flagged inline.

**Execution disclosure.** No CAS and no job of uncertain duration was run. Three bounded
exact-rational computations in plain Python were run as redundancy checks on hand
computations that are displayed in full: (a) the ROW-SWEEP identity `r ∈ C[p,q]`
(degree-12 polynomial identity, `True`); (b) `q ≡ (t−t²)/3` and `q' ≡ −(8/3)(t+1)
(mod r)`; (c) the Puiseux expansion of the branch of `D̄'` at its point at infinity to
order `U^{39}`. Each is polynomial/series arithmetic over `Q`, instantaneous. None is
load-bearing: (a)–(b) are re-derived by hand below and (c) merely re-confirms a Bézout
count that is proved independently.

## 1. The fold: what quantifies over the row, what is witness-specific

Coordinates: `D ⊂ C²_{x,y}`, `γ(t) = (p(t),q(t))`, `deg p = 6`, `deg q = 4`. The fold is
`ν : C²_{u,y} → C²_{x,y}`, `ν(u,y) = (u²,y)`, and `D' := {(r(t),q(t))}`,
`D'^- := ι(D')` with `ι(u,y) = (−u,y)`.

### 1.1 Witness data and the fold identity

ROW-SWEEP's witness is `r = t³+t+1`, `q = t⁴+⅔t²+⁴⁄₃t`, `p = r²`, together with the
identity `8r/27 = p²−q³−2pq+⅔q²−(16/27)p+(1/9)q−1/9`, verified here as an exact
degree-12 identity over `Q`. Its content is `r ∈ C[p,q]`, hence

```text
   C[p,q] = C[r,q] ,      deg r = 3, deg q = 4, gcd(3,4) = 1.            (1.1)
```

The consequence used throughout: for `t ≠ s`,

```text
   p(t)=p(s) and q(t)=q(s)   ⟺   r(t)=r(s) and q(t)=q(s).               (1.2)
```

(`⇐` is trivial from `p=r²`; `⇒` applies `r = F(p,q)` to both sides.) So `D` and `D'`
have literally the same off-diagonal double-point scheme in the parameter `t`.

### 1.2 Row-level quantification of `p = r²`

This is the first substantive question in the charge, and the answer is favourable:
**the fold is forced by the row label, not by the witness.**

For a one-place-at-infinity polynomial curve with normalisation `A¹`, the degree
semigroup `Γ := deg C[p,q] ⊆ N` satisfies `δ_aff = #(N∖Γ)`, because
`δ_aff = dim_C C[t]/C[p,q]` and `C[p,q]` has a `C`-basis of elements of pairwise
distinct degrees. The `Δ`-sequence of the row is exactly the generator sequence of `Γ`;
`Δ = (6,4,3)` says `Γ = ⟨6,4,3⟩ = ⟨3,4⟩`, whose gap set is `{1,2,5}`, so
`δ_aff = 3` ✓ — the ROW-SWEEP entry, re-derived. Conversely `δ_aff = 3` at `(d,n)=(6,4)`
forces `Γ = ⟨3,4⟩` (the only 3-gap subsemigroup of `N` containing `⟨6,4⟩`).

**Lemma 1.2 (semigroup ⇒ generator).** `Γ = ⟨3,4⟩` gives `ρ ∈ C[p,q]` with `deg ρ = 3`.
Then `C[ρ,q] ⊆ C[p,q]` have equal degree semigroups, hence are equal (induct on degree:
given `h` in the larger ring, pick `h'` in the smaller of the same degree and leading
coefficient; `h−h'` has smaller degree). `[]`

**Theorem FOLD (PROVED-HERE, row-level).** *Let `D ⊂ C²` be irreducible with
normalisation `A¹`, one place at infinity, `(d,n) = (6,4)` and `δ_aff = 3` — i.e. any
member of the residual row `Δ = (6,4,3)`. Then there is a triangular automorphism
`T ∈ Aut(A²)`, `T(x,y) = (x−βy−δ, y)`, with*

```text
   T(D) = { ( r(t)² , q(t) ) },     deg r = 3,  deg q = 4,  gcd = 1.
```

*Proof.* By Lemma 1.2, `C[p,q] = C[ρ,q]` with `deg ρ = 3`. Write `p` as a polynomial in
`ρ,q`. The relation ideal of `(ρ,q)` is principal, generated by the defining polynomial
`g` of the plane curve `{(ρ,q)}`, and `g` is monic of degree 4 in its first slot up to a
nonzero constant (§2.3), so we may reduce and assume `p = Σ_{i≤3} c_{ij}ρ^iq^j`. For
`i ≤ 3` the map `(i,j) ↦ 3i+4j` is injective (`3(i−i') = 4(j'−j)` with `|i−i'| ≤ 3`
forces `i=i'`), so no cancellation of leading terms is possible and
`deg p = max\{3i+4j : c_{ij} ≠ 0\} = 6`. The only `(i,j)` with `i ≤ 3` and `3i+4j = 6`
is `(2,0)`; the ones with `3i+4j < 6` are `(0,0),(1,0),(0,1)`. Hence

```text
   p = c₂₀ρ² + c₁₀ρ + c₀₁q + c₀₀ ,   c₂₀ ≠ 0 .
```

Rescale `ρ` so `c₂₀ = 1` and put `r := ρ + c₁₀/2` (still degree 3, still generating);
then `p = r² + c₀₁q + (c₀₀ − c₁₀²/4)`, and the triangular shear `T` with
`β = c₀₁`, `δ = c₀₀−c₁₀²/4` gives `T(D) = {(r²,q)}`. `[]`

So `p = r²` is **not** witness-specific: every member of the row is a fold, uniformly,
and no genericity is used. (`T` is a target automorphism, so `π₁(C²−D)`, the node count
and the place at infinity are all unchanged.)

### 1.3 The `(8,4)` survivor, without the PROVISIONAL shear

ROW-SWEEP §6 transports `(8,4)` to `(6,4)` by `P = p+q²` (PROVISIONAL). The same
argument gives it directly and unconditionally. For `Δ = (8,4,6,3)` the semigroup is
`⟨8,4,6,3⟩ = ⟨3,4⟩`, so again `C[P,q] = C[r,q]` with `deg r = 3`. Reducing to `i ≤ 3`
and using `3i+4j ≤ 8`:

```text
   P = c₀₂q² + c₁₁rq + c₂₀r² + c₀₁q + c₁₀r + c₀₀ ,   c₀₂ ≠ 0 .
```

Apply the triangular shear `x ↦ x − c₀₂y²`. If `c₁₁ ≠ 0` the image has degree 7, i.e.
type `(7,4)` — **coprime**, one place at infinity, three nodes — and the promoted
coprime no-`S₄` theorem kills it outright. If `c₁₁ = 0` the image has degree 6 and
Theorem FOLD applies. Either way the `(8,4)` row is covered without consuming ROW-SWEEP
§6. This is a strict strengthening of the charged transfer.

## 2. Structure of `D' ∪ D'^-`

Throughout, `D = {(r²,q)}` is any row member normalised by Theorem FOLD, `D' = {(r,q)}`,
`D'^- = ι(D')`. Note `ν^{-1}(D) = D' ∪ D'^-` set-theoretically, since `u² = r(t)²` iff
`u = ±r(t)`, and `ν|_{D'} : D' → D` is a bijection (it is `t ↦ t` on parameters).

### 2.1 The involution and the intersection locus (row-level)

**Lemma 2.1a.** *No affine singular point of `D` lies on `L₀ = {x=0}`.*
*Proof.* Suppose `p(τ)=0`, i.e. `r(τ)=0`, with multiplicity `μ ≥ 1`. Then
`x = r(t)² ∼ c(t−τ)^{2μ}`. If `q'(τ) = 0` the branch `t ↦ (x,y)` at `τ` has both
coordinates of order `≥ 2`, so it is a branch of multiplicity `≥ 2` — excluded, because
in the nodal class every singular point of `D` is a double point of **two smooth**
branches. Hence `q'(τ) ≠ 0`, `y − y₀ ∼ q'(τ)(t−τ)`, and the branch is smooth with
tangent the `x=0` direction. So *every* branch of `D` meeting `L₀` is tangent to `L₀`;
two such branches at a common point would be mutually tangent, never a node. `[]`

**Lemma 2.1b.** *For every row member,*
`D' ∩ D'^- = { (0, q(τ)) : r(τ) = 0 }`, *and the `q(τ)` are pairwise distinct.*
*Proof.* `(u,y) ∈ D'∩D'^-` means `u = r(t) = −r(s)`, `y = q(t) = q(s)`. If `t = s` then
`r(t)=0`. If `t ≠ s`, then `p(t) = p(s)` and `q(t)=q(s)`, so by (1.2) `r(t)=r(s)`; with
`r(t) = −r(s)` this gives `r(t)=r(s)=0`, so `(0,y)` would be a singular point of `D` on
`L₀`, excluded by Lemma 2.1a. The same argument gives distinctness of the `q(τ)`. `[]`

So the cross-locus sits over `{u=0}` exactly, with no fixed-point exceptions and no
genericity hypothesis. Dually, the three nodes of `D` lie off `L₀`; each lifts to a node
of `D'` at `(u_i,y_i)` and a node of `D'^-` at `(−u_i,y_i)`, six distinct points, and
`D'` does not pass through `(−u_i,y_i)`. Hence:

```text
   D' , D'^-  are 3-nodal rational curves of coprime type (4,3);
   Sing(D' ∪ D'^-)  =  3 + 3 self-nodes  ⊔  cross-locus over {u=0}.
```

**Witness check.** `r = t³+t+1` has `disc = −4−27 = −31 ≠ 0`, so three simple roots;
`q ≡ (t−t²)/3 (mod r)` (verified exactly), and `q(τ)=q(τ')` with `τ≠τ'` forces
`τ+τ' = 1`, hence `τ'' = −1` by `e₁ = 0`, but `r(−1) = −1 ≠ 0`. Distinct ✓.

### 2.2 Local types of the cross-points, and their total

Let `τ` be a root of `r` of multiplicity `μ`; by Lemma 2.1a, `q'(τ) ≠ 0`, so near
`N_τ := (0,q(τ))` the branch of `D'` is a graph `u = φ(y)` with `ord_{y−q(τ)} φ = μ`,
and the branch of `D'^-` is `u = −φ(y)`. Both are **smooth**, and

```text
   I(D', D'^-; N_τ)  =  ord( φ − (−φ) )  =  μ .                          (2.2)
```

Hence the cross-point at `N_τ` is an ordinary node iff `μ = 1`, and a tangential
contact of order `μ` (an `A_{2μ−1}` of the union) iff `μ ≥ 2`; and

```text
   Σ_τ I(D',D'^-;N_τ)  =  Σ_τ μ_τ  =  deg r  =  3    for every row member.
```

Three sub-cases exhaust the row: `(μ) = (1,1,1)` — three ordinary nodes, `T_x`-free;
`(2,1)` — one tacnodal cross-point plus one node; `(3)` — one contact-3 cross-point.
For the ROW-SWEEP witness `q'(τ) = −(8/3)(τ+1)` (verified exactly), which vanishes only
at `τ = −1 ∉ r^{-1}(0)`, and `r` is squarefree: **case `(1,1,1)`, three ordinary
transverse nodes**, so `T_x = 0` for the witness. The degenerate cases are *not*
excluded row-level — a double root of `r` gives a smooth point of `D` with contact 4 to
`L₀`, which is consistent with the nodal class — so they are carried below.

### 2.3 Behaviour at infinity

`D̄'` is a quartic (the parametrisation is birational since `gcd(3,4)=1`) with a single
place at infinity at `Q' = [0:1:0]`. There `a = deg q − deg r = 1`, so `Q'` is a **smooth
point** of `D̄'` with `I(D̄',L_∞;Q') = 4`: a *hyperflex* (contact-4 line), not an ordinary
flex. Consequently `δ_∞(D̄') = 0` and `δ(D̄') = (4−1)(4−2)/2 = 3` is entirely affine ✓.

`ι` fixes `Q'` and `L_∞`, so `D̄'^-` has the same picture. In the chart `(U,S)=(u/y,z/y)`
at `Q'`, `L_∞ = \{S=0\}`, `D̄' : S = f(U) = U⁴+…`, and `D̄'^- : S = f(−U)`. Therefore

```text
   I(D̄', D̄'^-; Q')  =  ord_U( f(U) − f(−U) )  =  4 + ord(odd part of f/U⁴),  odd.
```

**Bézout.** `D̄' ∩ D̄'^-` is contained in `Fix(ι) = \{u=0\} ∪ \{[1:0:0]\}` (an
intersection off `Fix` would give an `ι`-pair `P,ι(P)` on `D̄'`, i.e. the excluded case
`t≠s`, `r(t)=−r(s)`, `q(t)=q(s)`), and `[1:0:0] ∉ D̄'`. With §2.2:

```text
   16 = D̄'·D̄'^-  =  3 (affine, by (2.2))  +  I(Q')     ⟹    I(Q') = 13 .   (2.3)
```

**Lemma 2.3 (`β₁ = I(Q') + 2`; PROVED-HERE).** *Write `f = U⁴ε(U)`, `ε(0)≠0`, and put
`m := I(Q') = 4 + ord(ε_odd)`. Then the place of `D̄` at `Q_D = [1:0:0]` has
characteristic pair `(2; m+2)`.*
*Proof.* With `v = y/x`, `w = 1/x` at `Q_D` one has `v = S/U²`, `w = S²/U²`, so along
`D'`: `v = U²ε`, `w = U⁶ε²`. Setting `σ² = v`, i.e. `σ = Uε^{1/2}`, gives `w = σ⁶/ε(U)`.
Put `k := ord(ε_odd) = m−4` (odd). Modulo `U^k`, `ε` is even, `σ` is odd in `U`, hence
`U` is odd in `σ` and `w = σ⁶·(even)`. The first departure comes from `ε^{-1}_{odd}`,
of order `k`, composed with the odd series `U(σ)`: it contributes an odd term of order
`k` to `ε^{-1}`, i.e. a term of order `σ^{6+k}` in `w`; the other correction (the even
part of `U(σ)`, of order `k+1`) enters through the odd series `(ε^{-1})'` and lands at
order `≥ k+2`, so it cannot cancel. Hence the first half-integral Puiseux exponent of
`w` in `v` is `(6+k)/2`, i.e. `β₁ = 6+k = m+2`. `[]`

With (2.3), `β₁ = 15` — an **unconditional re-derivation** of the ROW-SWEEP PROVISIONAL
value, from the fold structure and Bézout alone, valid for every row member (§2.2 pins
the affine total at 3 regardless of the root pattern of `r`). Independently, the exact
series computation of §0(c) gives `f = U⁴ − 2U⁶ + (14/3)U⁸ − (340/27)U^{10} + (329/9)U^{12}
− (8/27)U^{13} + …`: all odd coefficients vanish through `U^{11}` and `c₁₃ = −8/27 ≠ 0`,
so `ord(f(U)−f(−U)) = 13` ✓, matching (2.3) exactly.

**Toric model (used in §4).** Taking `Σ` smooth complete with rays `(1,0),(0,1)` and
`ρ_∞ = (−3,−4)` gives `C²_{u,y} = U_{σ₀} ⊂ X_Σ`. The defining polynomial `g` of `D'`
has `deg_u g = 4` with **constant** leading coefficient (the 4 points of `D'` over any
`y=c` are all finite) and `deg_y g = 3` with constant leading coefficient; the unique
point at infinity forces the degree-4 form to be `c·u⁴`. Hence

```text
   Newt(g) = conv{(0,0),(4,0),(0,3)} ,   Area = 6 ,   #interior lattice pts = 3 .
```

So in `X_Σ`: `C₁² = 2·Area = 12`, `p_a(C₁) = 3` (Khovanskii) `= δ` ✓, the face in
direction `ρ_∞` has lattice length `gcd(4,3)=1` so `C₁·E_{ρ_∞} = 1` and `C₁` is smooth
and transverse to the boundary. Then `C₁·C₂ = 12` and, subtracting the affine 3,
`I(C₁,C₂; P_∞) = 9` in `X_Σ`. The two models agree: `X_Σ` is `P²` blown up at the four
`L_∞`-contact points of `Q'`, and `16−4 = 12`, `13−4 = 9` ✓. The constant-leading-
coefficient statement is what licenses the reduction "`i ≤ 3`" in Theorem FOLD.

## 3. The restriction/cover argument, re-derived

Write `G := π₁(C²−D)`, `Γ := π₁(C²−(D'∪D'^-))`, `L₀ = \{x=0\}`, `L₀' = \{u=0\}`, and
`U := C²−D`, `W := ν^{-1}(U) = C²−(D'∪D'^-)`. The charged FIXED-TUPLE §9 argument is
correct; re-deriving it yields a cleaner and slightly stronger statement.

**Proposition 3 (PROVED-HERE).** *`ν` induces a surjection `n_* : Γ ↠ G` carrying each
meridian of `D'` and of `D'^-` to a meridian of `D`. Consequently every
`φ : G ↠ S₄` with meridians ↦ transpositions pulls back to `ψ := φ∘n_* : Γ ↠ S₄` with
all meridians ↦ transpositions.*

*Proof.* Put `A := π₁(U−L₀)` and `B := π₁(W−L₀')`. Since `ν : W−L₀' → U−L₀` is an
unbranched double cover, `B ⊴ A` with index 2, and `A = B·⟨m⟩` for `m := μ_{L₀}` (whose
`Z/2`-winding class is the nontrivial one). Filling a removed divisor kills its meridian
normally, so `G = A/⟨⟨m⟩⟩_A` and `Γ = B/⟨⟨m²⟩⟩_B` — the exponent 2 because `ν` is
2:1 branched along `L₀'`, so `ν_*(μ_{L₀'}) = m²` (the loop `u = εe^{iθ}` maps to
`x = ε²e^{2iθ}`). Since `⟨⟨m²⟩⟩_B ⊆ ⟨⟨m⟩⟩_A ∩ B`, we get
`Γ ↠ B/(⟨⟨m⟩⟩_A ∩ B) ≅ A/⟨⟨m⟩⟩_A = G`, the isomorphism because `A = B⟨m⟩` and
`m ∈ ⟨⟨m⟩⟩_A`. `ν` is a local biholomorphism at a generic point of `D'`, so meridians
go to meridians. `[]`

Two remarks that matter for the verdict.

**(i) Direction.** The map goes `Γ ↠ G`, so `{S₄`-quotients of `G}` ⊆ `{S₄`-quotients of
`Γ}`. Killing the row through the fold therefore requires proving the **strictly
stronger** statement "`Γ` has no `S₄`-quotient with transposition meridians". This is a
structural cost of the route, not a defect of the argument; it is why §4 must succeed
outright rather than by transporting the downstairs deficit.

**(ii) The recoverable extra hypothesis.** `ψ` is not an arbitrary surjection: since
`ν∘ι = ν`, one has `ψ∘ι_* = c_γ ∘ ψ` for some `γ ∈ S₄`, i.e. `ψ` is `ι`-equivariant up
to inner automorphism. Any kill that uses only "`Γ ↠ S₄`, meridians ↦ transpositions"
discards this; any kill that uses it is, to that extent, re-importing the downstairs
problem. Both options are typed in §4.3.

## 4. Two-component machinery

### 4.1 Theorem N-A hypothesis test

**Warm-up (single component), PROVED-HERE.** In `P²` blow up `Q'` and the three
infinitely near points at which `D̄'` still meets `L̃_∞` (contact 4, §2.3). On the
resulting `X₀`: `C̃'² = 16−4 = 12`; `C̃'` is smooth at infinity and meets
`E := L̃_∞ ∪ E₁ ∪ E₂ ∪ E₃ ∪ E₄` transversally at one smooth point of `E₄`; `Sing C̃'` is
the three affine nodes, disjoint from `E`; `X₀ − E = C²`. N-A applies with
`r₁ = 3, T = 0, T_x = 0`, and `12 > 6` **fires**. Since `π₁(X₀−E) = π₁(C²) = 1`,

```text
   π₁(C² − D')  is f.g. abelian, hence  = Z    (H₁ = Z, D' irreducible).
```

So the charged "promoted coprime Main Theorem gives `π₁(C²−D') = Z`" is recovered here
from promoted N-A alone, for every row member. This is the one place the fold route
delivers unconditionally.

**The union.** Take `D = C₁ ∪ C₂` (`C₁ = D̄'`, `C₂ = D̄'^-`) and `E` the divisor at
infinity. Every singular point of `D` is a double point of two smooth branches ✓ — the
self-nodes (`k=1`), the cross-points over `\{u=0\}` (`k = μ_τ`, §2.2), and `Q'`
(`k = 13`, §2.3). But `Q' ∈ E ∩ Sing D`, so the hypothesis `E ∩ Sing D = ∅` forces
resolution at infinity. Blow up the 13 common infinitely near points of `C₁,C₂` at `Q'`
(Lemma 3.2, blow-up invariance, is promoted). At each stage the strict transform of a
smooth branch meets the newest exceptional curve transversally and away from the older
ones, so on the resulting `X`:

```text
   C₁ ∩ C₂ = the 3 affine cross-points only  (C₁·C₂ = 16 − 13 = 3) ;
   C_i meets E only in E₁₃, transversally, at a smooth point of E ;
   E ∩ Sing D = ∅ ;   D ∪ E  is NC along  D − Sing D ;   X − E = C² .
```

The self-intersection is therefore forced:

```text
   C_i²  =  16 − 13  =  3 .                                              (4.1)
```

**This value is model-independent.** In the toric model `X_Σ` of §2.3 one starts from
`C_i² = 12` and `I(C₁,C₂;P_∞) = 9`, and `12 − 9 = 3` again; `X_Σ` is `P²` blown up at
exactly the four `L_∞`-contact points, so the two computations are the same computation.
Fewer blow-ups are not allowed (with `k < 13` the point `C₁∩C₂` still lies on `E_k ⊆ E`),
and more blow-ups only lower `C_i²`. Enlarging or shrinking `E` cannot help: `E` does
not appear in the N-A inequality.

**The test.** With `r₁(C_i) = 3` self-nodes, `T(C_i) = 0` (no self-tangency), and
`T_x(C_i) = 0` (after (4.1) the components are disjoint at infinity, and in the generic
root pattern `(μ)=(1,1,1)` the affine cross-points are transverse):

```text
   C_i² = 3   vs.   2r₁ + 4T + T_x = 6 .      3 > 6  is FALSE.           (4.2)
```

The verdict is robust to the two live readings of the promoted charge. If `r₁(C)` counts
*all* nodes of `D` on `C` (self plus cross), the bound rises to `12` and the failure
widens. If `T_x` is read as `Σ_p k_p` over tangential cross-points (the reading that
reproduces the promoted sharpness datum "two bitangent conics fail by one unit":
`C² = 4`, `Σk_p = 2+2 = 4`, `4 > 4` false), it is `0` here regardless, because the
components have been separated. In the degenerate root patterns `(μ) = (2,1)` or `(3)`
one may either charge the affine tangential cross-point (`T_x = 2` or `3`) or blow it up
(costing a further `μ` from `C_i²`); both worsen (4.2). **N-A does not fire, in any
admissible configuration, for any member of the row.**

### 4.2 Gap quantification, and the comparison with the direct route

The deficit in (4.2) is exactly `3`. Its meaning is sharpened by recovering the
downstairs gate from the same identity. For an irreducible one-place curve of degree `d`
with infinity multiplicity sequence `(m_i)`, the embedded resolution gives
`C̃² = d² − Σm_i²`, and `Σm_i² = Σm_i(m_i−1) + Σm_i = 2δ_∞ + M_∞` with `M_∞ = Σm_i`
(promoted M-INF piece 1: `M_emb = mult + β_h − 1`). Since `2r₁ = 2δ_aff =
(d−1)(d−2) − 2δ_∞`,

```text
   C̃² > 2r₁   ⟺   d² − 2δ_∞ − M_∞ > (d−1)(d−2) − 2δ_∞   ⟺   M_∞ ≤ 3d − 3 ,
```

which is precisely the promoted (M-INF) gate. For the row, cluster `(2⁷,1,1)`:
`M_∞ = 16`, `Σm_i² = 30`, so downstairs

```text
   C̃² = 36 − 30 = 6 ,   2r₁ = 6 ,   deficit 1   (the known "fails by one unit").
```

Upstairs, by (4.2), the deficit is `3`. **The fold strictly loses ground for N-A:** it
trades one irreducible curve missing the gate by one unit for two curves each missing it
by three. The reason is visible in (4.1): the fold converts the `δ_∞ = 7` unibranch
singularity at `Q_D`, whose resolution costs `Σm_i² = 30` out of `d² = 36`, into a
contact-13 tangency between two quartics, whose separation costs `13` out of `16`. The
`β₁ = I(Q')+2` law of Lemma 2.3 is exactly the exchange rate, and it is unfavourable.

This is a genuine no-go for step 2 of the charge as posed: no choice of `X`, `E`, or
component split recovers the three units, because (4.1) is intrinsic and `E` is inert in
the inequality.

### 4.3 The three alternates named in the charge

**(a) Reducible aggregate machinery — UNAVAILABLE.** Integration `126c2d29` §1 promotes
Theorem N-A with a *per-component* inequality, Lemma 3.1 as corrected, Lemma 3.2, and
Corollary N-A-RES. It promotes no aggregate form (a hypothesis on `D` as a whole rather
than on each `C ⊆ D`), and §1 explicitly records that the naive extensions of N-A were
**REFUTED and binding** — the `B(C)>0` extension by the Zariski sextic, and the
smooth-branch componentwise version by the bitangent conics. Manufacturing an aggregate
variant here would be exactly the barred move. Typed
`OPEN[NA-AGGREGATE-REDUCIBLE]`, not used.

**(b) Direct ZvK on the union — set up, not decidable at desk scale.** The right pencil
is the `u`-projection, not the `y`-projection: `deg_y g = 3`, so `D' → C_u` and
`D'^- → C_u` are 3-fold covers and the union is a **6**-section (versus 8 for `y`).
The discriminant, row-level:

* `2 + 2` simple branch points, where `r'(t) = 0` (for `D'`, at `u = r(t)`; for `D'^-`,
  at `u = −r(t)`) — local braid a half-twist `σ`, relation `g_a = w g_b w^{-1}`;
* `3 + 3` self-nodes, at `u = u_i` and `u = −u_i` — local braid `σ²`, relation
  `[g_a, g_b] = 1`;
* `u = 0`, where all six points collapse in pairs. Near `u=0` the pair over the root `τ`
  of `r` is `y = q(τ) ± c_τ u + O(u²)` with `c_τ = q'(τ)/r'(τ) ≠ 0` (Lemma 2.1a), so the
  local braid is `σ_{i₁}²σ_{i₂}²σ_{i₃}²` — three **disjoint full twists**, i.e. three
  commutation relations, one per cross-node.

For the witness these are `2+2+3+3+1 = 11` distinct values: the branch values are
`±(1 ± 2i/3√3)` (using `t² = −1/3 ⟹ r = 1 + 2t/3`), and `u_i = (σ_i−1)/3` with
`3σ³+4σ−4 = 0`, so `u_i = −u_j` would force `σ_i+σ_j = 2`, hence `σ_k = −2`, but
`3(−8)+4(−2)−4 = −36 ≠ 0`.

So `Γ = ⟨g_1,…,g_6 | 13 relations⟩`. The abelianisation `Z²` forces the four
identification relations to merge `\{g_1,g_2,g_3\}` and `\{g_4,g_5,g_6\}` into two
classes, i.e. two spanning-tree edges on each triple — exactly four, with no slack.
Under `ψ` the nine commutations say: at each of the nine nodes the two transpositions
are equal or disjoint. This is a `B_6` monodromy computation with 11 factors; it is not
desk-scale, and this lane does not attempt it. Typed
`OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]`, with the setup above as its entry data.

**(c) Conversion through the pulled-back `S₄`-cover — consistent, no obstruction.** Let
`Y → C²` be the degree-4 cover from `φ` and `Y' := Y ×_{C²} C²_{u,y}` the pullback
through `ν`, branched over `D'∪D'^-`. Euler characteristics (all `χ_c`): `D` is `A¹`
with three pairs glued, `χ(D) = −2`, so `χ(C²−D) = 3`; upstairs
`χ(D'∪D'^-) = (−2)+(−2)−3 = −7`, so `χ(C²−(D'∪D'^-)) = 8`. Cross-check through the
double cover branched over `L₀ ∖ (L₀∩D) ≅ C − 3` points: `2·3 − (−2) = 8` ✓. With `s_P`
denoting the number of `⟨ψ(μ_1),ψ(μ_2)⟩`-orbits at a node `P` (`3` if the two
transpositions are equal, `2` if disjoint),

```text
   χ(Y)  = 4·3 + 3·(−2−3) + Σ_{3 nodes} s_P      = −3 + Σ s_P  + 6 ,
   χ(Y') = 4·8 + 3·(−7−9) + Σ_{9 nodes} s_P      = −16 + Σ s_P ,   Σ ∈ [18,27].
```

Both are integers in range for every admissible labelling; no parity or positivity
obstruction appears, and the `χ_c(Y) = 3` datum of the charged §6.3 is the case "all
three nodes disjoint". The pull-back therefore adds no numerical kill. (The Galindo
conversion law itself is a `Δ`-sequence ↔ characteristic-exponent dictionary; it is
consumed in §1.2/§2.3 and has no further content here.)

## 5. Verdict

**Decision on `OPEN[PI1S4-(6,4)-FOLD-REDUCTION]`: the row SURVIVES the fold route. The
route is set up completely and fails at a quantified, intrinsic obstruction; it is not
merely unfinished.** Explicitly:

1. **The fold is row-level, not witness-specific (Theorem FOLD, §1.2).** Every member of
   `Δ = (6,4,3)` is, after a triangular target automorphism, `\{(r(t)²,q(t))\}` with
   `deg r = 3`, `deg q = 4`. No genericity, no witness data. The `(8,4)` survivor is
   covered too, and *without* ROW-SWEEP §6: its shear lands either on a coprime `(7,4)`
   curve (killed by the promoted coprime no-`S₄` theorem) or on `(6,4)` (folds). §1.3.
2. **The geometry of `D' ∪ D'^-` is completely determined, row-level (§2).** Two 3-nodal
   rational quartics with hyperflexes at a common point `Q' = [0:1:0]`; cross-locus
   exactly over `\{u=0\}`, one point per distinct root `τ` of `r` with contact `μ_τ` and
   `Σμ_τ = 3` always; and `I(D̄',D̄'^-;Q') = 13` by Bézout. Lemma 2.3 (`β₁ = I(Q')+2`)
   turns this into an **unconditional re-derivation of `β₁ = 15`**, previously
   PROVISIONAL, and the exact Puiseux expansion confirms it independently.
3. **N-A fires for each component separately** and gives `π₁(C²−D') = Z` from promoted
   machinery alone (§4.1) — so the "components separately settled" premise of the charge
   is now proved rather than cited.
4. **N-A cannot fire on the union.** `C_i² = 3` is forced on every admissible surface
   (`P²`-blow-up and toric models agree), against a threshold of `2r₁ = 6`: deficit
   **exactly 3**, robust to both live readings of `r₁`/`T_x` and to all three root
   patterns of `r`. §4.1–4.2.
5. **The fold makes the N-A ledger strictly worse.** The same identity that reproduces
   the promoted (M-INF) gate `M_∞ ≤ 3d−3` gives deficit **1** downstairs
   (`C̃² = 36−30 = 6`, `2r₁ = 6`) against deficit **3** upstairs. Lemma 2.3 is the
   exchange rate and it runs the wrong way. §4.2.
6. **The route also strengthens the goal.** Proposition 3 is a surjection `Γ ↠ G`, so
   ruling out `S₄` for `Γ` is strictly harder than for `G` unless the `ι`-equivariance of
   §3(ii) is re-imported — at which point the fold has bought no independence. §3.

Per FALLACY-v2 (floor/attainment, carrier/attainment): the failure of (4.2) is **not**
evidence that `Γ ↠ S₄` exists. It removes a candidate kill and supplies no floor on
attainment. Nothing here bears on whether `π₁(C²−D) ↠ S₄` exists, and nothing here is a
Keller counterexample.

The residual is a single named computation, `OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]` (§4.3(b)),
whose entry data — 6 strands, 11 discriminant values, the local braid types, and the
forced spanning-tree structure of the four identification relations — is fully typed
above.

## 6. Typed residuals and successor tasks

**`OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` — the highest-leverage successor this lane
produces, and it is downstairs, not upstairs.** §4.2 shows the direct route misses by
exactly one unit, with `C̃² = 2r₁ = 6` and `T = T_x = 0`. The promoted sharpness datum
for N-A is specifically about the **`T_x` coefficient** (two bitangent conics: two
components, `T_x ≠ 0`). It says nothing about whether the strict inequality `C² > 2r₁`
can be relaxed to `C² ≥ 2r₁` when `C` is **irreducible** with `T = T_x = 0` and its only
non-nodal point is the resolved place at infinity. If it can, rows `(6,4)` and `(8,4)`
die on the spot. This should be routed as a literature-and-countermodel task (find a
witness with `C² = 2r₁`, irreducible, nodal, `T=T_x=0`, and non-abelian kernel — or
prove none exists), *not* as a self-serving relaxation; per FALLACY-v2 no gap may be
filled by analogy, so absent such a result the strict form stands and the row lives.

**`OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]`** — the 6-strand braid-monodromy decision for
`Γ = π₁(C²−(D'∪D'^-))` with the `u`-projection, entry data in §4.3(b). Note it decides a
strictly stronger statement than the row needs (§3(i)); a NO kills rows `(6,4)` and
`(8,4)`, a YES decides nothing.

**`OPEN[PI1S4-(6,4)-FOLD-EQUIVARIANT]`** — the sharpened form: decide whether
`Γ ↠ S₄` exists that is `ι`-equivariant up to inner automorphism (§3(ii)). This is
equivalent to the downstairs problem and is the honest statement of what the fold buys;
it is listed so that a future lane does not mistake `OPEN[...-ZVK-U6]` for it.

**`OPEN[NA-AGGREGATE-REDUCIBLE]`** — whether any aggregate (non-componentwise) form of
N-A holds for reducible `D`. Not promoted, not used, and the two promoted countermodels
make a naive version unsafe. §4.3(a).

**Carried, unchanged by this lane.** `OPEN[PI1S4-(6,4)-FACTORIZATION]` remains the
combinatorial successor named by the charged FIXED-TUPLE §9, and this lane's finding (5)
raises its relative priority: the fold gives no shortcut past it.
`OPEN[PI1S4-(6,4)-TRIPLE-COVER]`, `OPEN[ROW-(8,6)-NODAL-REALIZATION]`,
`OPEN[ROW-(9,6)-NODAL-REALIZATION]`, `OPEN[NORI-BC-SELF-TANGENT-COEFF]`,
`OPEN[PI1S4-D1-DEGREE]` are untouched.

**Promotion candidates from this lane** (all independent of the PROVISIONAL row data,
and all row-level): Theorem FOLD (§1.2); the `(8,4)` corollary (§1.3); Lemmas 2.1a,
2.1b, and 2.3 with the unconditional `β₁ = 15` (§2); `π₁(C²−D') = Z` from promoted N-A
(§4.1); the identity `C̃² = d² − 2δ_∞ − M_∞` reproducing the (M-INF) gate, with the
deficit ledger `1` downstairs / `3` upstairs (§4.2). The PROVISIONAL ROW-SWEEP items
consumed anywhere below §1 are the witness polynomials only, and they are used solely
for the illustrative sub-case computations in §2.1–2.2 and §4.3(b); every theorem
above quantifies over the row.

**Status line.** `OPEN[PI1S4-(6,4)-FOLD-REDUCTION]`: **closed as a route, negative.**
The fold reduction is now a complete and row-level geometric description of the residual,
but it does not kill the row: promoted N-A misses by three units on the union against one
unit on the original curve. No exit-price assertion is made, so no `charge_basis` line is
declared.

<!-- BODY-END -->
