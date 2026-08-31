# Hostile review: FOLD-REDUCTION (Opus 5)

**Reviewer:** Grok 4.6
**Date:** 2026-08-31
**Mode:** Different-model gate; default to refutation
**Charged inputs (frozen, hash-verified):**
- `pi1s4-64-fold-reduction-opus5-20260831.md`
- `pi1s4-64-fixed-tuple-opus5-20260831.md`
- `block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md`

**Scope.** Gate Theorem FOLD, the (8,4) shear dichotomy, §2 geometry (hyperflexes, cross-locus, Bezout, Lemma 2.3, unconditional β₁=15), §3 restriction/cover, §4 N–A deficit, §5 verdict, §6 successor typings. Desk-scale exact reasoning only. FALLACY-v2 in force.

---

## 0. Hash verification and reading protocol

Frozen copies were hashed with `shasum -a 256` **before any was read**; 3/3 match the charge:

```text
8529de8ec1b11450a95481ffdf19f6e5116129aeef2ea2c27579b4e4fcc93a74
  .../inputs/pi1s4-64-fold-reduction-opus5-20260831.md
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8
  .../inputs/pi1s4-64-fixed-tuple-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286
  .../inputs/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Primary literature fetched and hashed (not a campaign artifact):

```text
1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45
  4546575 bytes, https://www.numdam.org/item/10.24033/asens.1450.pdf
  M. V. Nori, Zariski's conjecture and related problems,
  Ann. Sci. Éc. Norm. Sup. (4) 16 (1983), 305–344.
  Consumed: Proposition 3.27 (p. 331), the strict bound C² > 2r(C);
  Definition 3.25 / Remark at 3.26 (B(C)=C²−2r(C) for nodal C);
  WLT(C) (p. 330): deg φ ≤ B²/(B²−2r(B)), denominator vanishes at equality.
```

No CAS, no job of uncertain duration, no `jc2-lean`, no charged file or canonical ledger edited. Witness polynomial identities used illustratively by the charged report were re-checked by hand (not by machine): for `r=t³+t+1`, `disc=−4−27=−31≠0`; on `r=0` one has `q≡(t−t²)/3` and `q′≡−(8/3)(t+1)`. Neither is load-bearing for a row-level claim.

Typing of consumed promoted items follows the charged integration `126c2d29`: Theorem N-A at the corrected scope, Lemma 3.2, Corollary N-A-RES, M-INF piece 1 `M_emb=mult+β_h−1`, and the coprime PI1-S4 Main Theorem as promoted in the N≤19 integration (irreducible, one place, `gcd(d,n)=1`, affine singularities double points of two smooth branches, tangency allowed). ROW-SWEEP numerics remain PROVISIONAL except where re-derived here.

## 1. Theorem FOLD — re-derivation: why Δ=(6,4,3) forces p a square

**Verdict: HOLDS, with a parenthetical repair.** The theorem as stated for the row label `Δ=(6,4,3)` is correct. The uniqueness sentence used in the converse is false as a claim about numerical semigroups and must not be promoted.

Setup. `D⊂C²` irreducible, normalisation `A¹`, one place at infinity, coordinates `γ(t)=(p(t),q(t))` with `(d,n)=(6,4)`. Write `Γ=deg C[p,q]⊆ℕ`. The Abhyankar–Moh δ-sequence of the row is the generator sequence of `Γ`. The label `Δ=(6,4,3)` **means** `Γ=⟨6,4,3⟩`. Since `6=2·3`, this is `Γ=⟨3,4⟩`, whose gaps are `{1,2,5}`, so `δ_aff=#(ℕ∖Γ)=3`. That direction is tautological from the row label, and it matches the ROW-SWEEP entry.

**Repair.** The charged converse — “`δ_aff=3` at `(d,n)=(6,4)` forces `Γ=⟨3,4⟩` (the only 3-gap subsemigroup of `ℕ` containing `⟨6,4⟩`)” — is **false** as semigroup theory. The complete list of genus-3 numerical semigroups is four:

| semigroup | gaps | contains `⟨4,6⟩`? | symmetric? |
|---|---|---|---|
| `⟨4,5,6,7⟩` | `{1,2,3}` | yes | no |
| `⟨3,5,7⟩` | `{1,2,4}` | no | no |
| `⟨3,4⟩` | `{1,2,5}` | yes | yes |
| `⟨2,7⟩` | `{1,3,5}` | yes | yes |

Three of them contain `⟨4,6⟩`. The parenthetical is therefore not a proof. What *does* isolate `⟨3,4⟩` in this lane is the δ-sequence calculus: the only length-3 sequence `Δ=(6,4,c)` with `c` odd, `c<6`, and `δ_aff=3` is `c=3` (the competitors `c=5` and `c=1` give genus 4 and 0 respectively). Equivalently: the affine coordinate ring is a plane complete intersection, hence Gorenstein, so `Γ` is symmetric; the only symmetric 3-gap semigroups are `⟨3,4⟩` and `⟨2,7⟩`; and `2∈Γ` would put a degree-2 element in `C[p,q]`, whence `C(p,q)⊆C(ρ)` with `[C(t):C(ρ)]=2`, contradicting birationality of a genuine `(6,4)` type. Either of those repairs is acceptable; the charged sentence is not.

**Lemma 1.2, re-derived.** `Γ=⟨3,4⟩` supplies `ρ∈C[p,q]` with `deg ρ=3`. Then `C[ρ,q]⊆C[p,q]`. The coprime pair `(deg ρ,deg q)=(3,4)` has value semigroup `⟨3,4⟩` (the unique relation is at degree 12, `ρ⁴∼q³`, and does not fill `{1,2,5}`). Equal filtered semigroups inside `C[t]` plus inclusion give equality: given `h` in the larger ring of `t`-degree `n`, take `h′` in the smaller with the same leading term, and induct on `deg(h−h′)`. The rings are filtered, not graded; leading-term subtraction is still valid. So `C[p,q]=C[ρ,q]`.

**Square after a triangular target automorphism.** The relation ideal of `(ρ,q)` is principal. Because `t` is integral over `C[q]` (`deg q=4`) and `ρ∈C[t]`, the element `ρ` satisfies a monic degree-4 polynomial `g∈C[q][u]`. Reduce and write `p=∑_{i≤3} c_{ij} ρ^i q^j`. For `i≤3` the map `(i,j)↦3i+4j` is injective: `3(i−i′)=4(j′−j)` with `|i−i′|≤3` forces `4∣(i−i′)` (since `gcd(3,4)=1`) hence `i=i′`. No cancellation of leading terms is possible, so `deg p=max{3i+4j:c_{ij}≠0}=6`. The only pair with `i≤3` and `3i+4j=6` is `(2,0)`; the pairs with `3i+4j<6` are `(0,0)`, `(1,0)`, `(0,1)`. Thus

```text
p = c₂₀ ρ² + c₁₀ ρ + c₀₁ q + c₀₀ ,   c₂₀ ≠ 0.
```

Rescale `ρ` so `c₂₀=1` and complete the square by `r:=ρ+c₁₀/2` (still degree 3, still a generator). Then `p=r²+c₀₁ q+(c₀₀−c₁₀²/4)`. The triangular shear `T(x,y)=(x−c₀₁ y−δ,y)` with `δ=c₀₀−c₁₀²/4` yields `T(D)={(r²,q)}`. Target automorphisms preserve `π₁(C²−D)`, the affine double-point scheme, and the place at infinity of the original embedding type only up to the explicit change of first coordinate; here `deg(r²)=6` still, so the normalised pair remains `(6,4)`. No genericity is used.

**What is witness-specific.** The explicit identity `8r/27=p²−q³−⋯` and the polynomials `r=t³+t+1`, `q=t⁴+(2/3)t²+(4/3)t` are a single member of the row. They are not an ingredient of Theorem FOLD. Identity (1.2) — `p(t)=p(s)` and `q(t)=q(s)` iff `r(t)=r(s)` and `q(t)=q(s)` — follows row-level once `r∈C[p,q]` is supplied by Lemma 1.2, because after the shear the rings coincide.

**Promotion.** Promote Theorem FOLD at the stated scope (`Δ=(6,4,3)`, one-place, normalisation `A¹`), with the uniqueness parenthetical deleted or replaced by the δ-sequence / Gorenstein repair above. Do not promote the converse as written.

## 2. The (8,4) shear dichotomy

**Verdict: HOLDS.** The algebraic dichotomy is row-level and does not consume ROW-SWEEP §6. The coprime landing is inside the promoted Main Theorem.

For `Δ=(8,4,6,3)` the semigroup is `⟨8,4,6,3⟩=⟨3,4⟩`, so again `C[P,q]=C[r,q]` with `deg r=3`. Reduce `i≤3`. The pairs with `3i+4j≤8` are `(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)`; injectivity again forbids cancellation, and the unique degree-8 pair is `(0,2)`. Hence

```text
P = c₀₂ q² + c₁₁ r q + c₂₀ r² + c₀₁ q + c₁₀ r + c₀₀ ,   c₀₂ ≠ 0.
```

The triangular shear `x↦x−c₀₂ y²` is an automorphism of `A²`. Two exhaustive cases:

- `c₁₁≠0`. Leading term `c₁₁ r q` has degree 7. The image is type `(7,4)`, `gcd(7,4)=1`, hence one place at infinity. Target automorphisms preserve the affine double-point scheme, so `δ_aff=3` and the three nodes survive. The promoted coprime PI1-S4 Main Theorem (N≤19 integration §1.1: irreducible, one place, `gcd=1`, affine singularities double points of two smooth branches) forbids a transposition-valued `S₄` quotient. Scope matches. (The `(7,4)` entry on the Theorem A small-case survivor table is not the Main Theorem; it is an intermediate braid-level list, killed later in the same package. The same distinction was already recorded on the `(6,3)→(4,3)` kill.)
- `c₁₁=0`. The image has degree 6 and Theorem FOLD applies.

Either way the `(8,4)` row is covered without the PROVISIONAL identity `P=p+q²`. The strengthening claim is correct.

Caveat, not a refutation: the sheared `(7,4)` curve has `δ_∞=pa(deg 7)−δ_aff=15−3=12`, much fatter at infinity than a standard coprime `(3;7)` cusp (`δ_∞=6`). The Main Theorem does not restrict `δ_∞`, so this is only a reminder that the landing is not the “generic” coprime `(7,4)` type.

## 3. Geometry of D' ∪ D'⁻ (§2)

Throughout, `D={(r²,q)}` is any FOLD-normalised row member, `D′={(r,q)}`, `D′⁻=ι(D′)` with `ι(u,y)=(−u,y)`, and `ν(u,y)=(u²,y)`. Set-theoretically `ν⁻¹(D)=D′∪D′⁻`. The restriction `ν|_{D′}:D′→D` is a bijection on parameters.

### 3.1 Hyperflex claims

**Verdict: HOLDS, row-level.**

`gcd(3,4)=1`, so `t↦(r(t),q(t))` is birational and `D̄′` is an irreducible quartic. As `t→∞`, `[r:q:1]∼[t³:t⁴:1]→[0:1:0]`, so the unique point at infinity is `Q′=[0:1:0]`. Multiplicity at `Q′` is `deg q−deg r=1`: a smooth point. Bézout against `L_∞={z=0}` plus uniqueness of the infinite place gives `I(D̄′,L_∞;Q′)=4`. The unique tangent at a smooth point of intersection multiplicity 4 with a line is that line, so `L_∞` is a hyperflex of `D̄′`. Consequently `δ_∞(D̄′)=0` and `δ(D̄′)=(4−1)(4−2)/2=3` is entirely affine, matching three nodes.

`ι` fixes `Q′` and `L_∞`, so `D̄′⁻` has the same picture. The two hyperflexes sit at a common point, with a common hyperflex line. No genericity.

### 3.2 Cross-locus over {u=0}

**Verdict: HOLDS, including the three root patterns and the sum `Σμ=3`.**

**Lemma 2.1a.** No affine singular point of `D` lies on `L₀={x=0}`. If `p(τ)=0` then `r(τ)=0` and `x=r(t)²∼c(t−τ)^{2μ}` with `μ≥1`. If also `q′(τ)=0`, both coordinates of the branch have order `≥2`, so the branch has multiplicity `≥2`, excluded in the nodal class. Thus `q′(τ)≠0`, the branch is a smooth graph over `y`, and `dx=0` at `τ`, so the tangent is `L₀`. Two such branches at a common point are mutually tangent, never an ordinary node. Hence `D` has no node on `L₀`.

**Lemma 2.1b.** `D′∩D′⁻={(0,q(τ)):r(τ)=0}`, and the values `q(τ)` are pairwise distinct. An intersection point is `u=r(t)=−r(s)`, `y=q(t)=q(s)`. If `t=s` then `r(t)=0`. If `t≠s` then `p(t)=p(s)` and `q(t)=q(s)`, so (1.2) gives `r(t)=r(s)`, hence `r(t)=0`, and `(0,y)` would be a singular point of `D` on `L₀`, forbidden. Distinctness of the `q(τ)` is the same argument.

The three nodes of `D` therefore lie off `L₀`. At each, `ν` is a local biholomorphism (`u_i≠0`), so each node of `D` lifts to a node of `D′` at `(u_i,y_i)` and a node of `D′⁻` at `(−u_i,y_i)`, six distinct points, and `D′` does not pass through `(−u_i,y_i)`. Thus `D′` and `D′⁻` are 3-nodal rational curves of coprime type `(4,3)`, and

```text
Sing(D′ ∪ D′⁻) = 3+3 self-nodes  ⊔  cross-locus over {u=0}.
```

**Local types.** At a root `τ` of `r` of multiplicity `μ`, Lemma 2.1a gives `q′(τ)≠0`, so `y` is a local parameter and the branch of `D′` is a graph `u=φ(y)` with `ord_{y−q(τ)} φ=μ`. The branch of `D′⁻` is `u=−φ(y)`. Both are smooth, and `I(D′,D′⁻;N_τ)=ord(φ−(−φ))=μ`. Ordinary node iff `μ=1`; `A_{2μ−1}` iff `μ≥2`. Summing, `Σ_τ I=Σ_τ μ_τ=deg r=3` for every row member, independent of the root pattern.

The three exhaustive sub-cases `(μ)=(1,1,1)`, `(2,1)`, `(3)` are correctly listed. A multiple root of `r` is a smooth point of `D` (one branch) with contact `2μ` to `L₀`, compatible with the nodal class, and is *not* excluded row-level. For the ROW-SWEEP witness, `r` is squarefree and `q′(τ)=−(8/3)(τ+1)` vanishes only at `τ=−1∉r⁻¹(0)`, so that witness is `(1,1,1)`; this is illustrative, not a row-level exclusion of the degenerate patterns.

### 3.3 Bézout `I(Q′)=13`

**Verdict: HOLDS, row-level.**

In `P²`, `D̄′·D̄′⁻=16`. The involution `ι:[u:y:z]↦[−u:y:z]` has fixed locus `{u=0}∪{[1:0:0]}`. An intersection off `Fix(ι)` would be an `ι`-pair `P,ι(P)` on `D̄′`, i.e. the excluded case `t≠s`, `r(t)=−r(s)`, `q(t)=q(s)`. The point `[1:0:0]` is not on `D̄′` (unique infinite place `Q′=[0:1:0]`; `L_∞` meets `D̄′` only there). Affine intersections are the cross-locus of §3.2, total multiplicity 3. Therefore `16=3+I(D̄′,D̄′⁻;Q′)`, so `I(Q′)=13`. The count does not depend on the root pattern of `r`.

Chart check, not a second proof: in `(U,S)=(u/y,z/y)` at `Q′`, one has `L_∞={S=0}` and `D̄′: S=f(U)=U⁴ε(U)` with `ε(0)≠0` (because `U=r/q∼t⁻¹`, `S=1/q∼t⁻⁴`). Then `D̄′⁻: S=f(−U)`, and `I(Q′)=ord_U(f(U)−f(−U))=4+ord(ε_odd)`, necessarily odd. Bézout forces the odd integer to be 13.

### 3.4 Lemma 2.3 and the unconditional `β₁=15` claim

**Verdict: HOLDS. This is the load-bearing upgrade. Gate passed.**

**Lemma 2.3 re-derived.** Write `f=U⁴ε(U)`, `ε(0)≠0`, and `m:=I(Q′)=4+k` with `k:=ord(ε_odd)` odd. Affine coordinates of `D` at `Q_D=[1:0:0]` are `v=y/x`, `w=1/x`. The two charts are related along `D′` by `v=S/U²`, `w=S²/U²`: indeed `S=1/y`, `U=u/y`, `x=u²` give `S/U²=y/u²=y/x` and `S²/U²=1/u²=1/x`. Substituting `S=U⁴ε` yields `v=U²ε`, `w=U⁶ε²`. Set `σ²=v`, i.e. `σ=U ε^{1/2}` (a choice of sheet of the fold). Then `w=σ⁶/ε(U)`.

The place of `D` at `Q_D` has multiplicity `a=2`, so a single characteristic pair `(2;β₁)` with `β₁` the first odd exponent of `w` as a series in `σ`. If `ε` were even then `U` would be odd in `σ` and `w` would be even in `σ`, hence a series in `v`. The first odd term of `ε^{-1}(U(σ))` produces the first odd term of `w`.

Let `ε=ε_even+ε_odd` with `ord(ε_odd)=k`. Then `σ=Uη(U)` with `η=ε^{1/2}` has odd part of order 1 and even part of order `k+1`. Inverting, `U(σ)=U_odd+U_even` with `ord U_even=k+1`. Expand `ε⁻¹(U_odd+U_even)=ε⁻¹(U_odd)+(ε⁻¹)′(U_odd)·U_even+O(U_even²)`. The odd part of `ε⁻¹∘U_odd` has order exactly `k` (odd∘odd, leading coefficient `c_k α^k≠0`). The correction `(ε⁻¹)′(U_odd)·U_even` is odd of order `≥k+2`. The quadratic remainder has even order `2k+2`. No cancellation at order `k`. Hence the first odd exponent of `w` is `6+k`, i.e. `β₁=6+k=m+2`.

With (2.3), `m=13`, so `β₁=15`. The affine total in (2.3) is 3 for every root pattern, so this is **row-level and does not consume the PROVISIONAL ROW-SWEEP value**. Multiplicity `a=2` is the FOLD form (`deg r²=6`, `deg q=4`), and `15>6` places the germ in the `a∣d` regime of a single pair `(2;15)`. The witness Puiseux `ord(f(U)−f(−U))=13` is an independent check on one member, not an ingredient.

FALLACY-v2 (pole/interior; floor/attainment). The characteristic-pair identification uses the vertex class `a=2` and the source hypotheses of FOLD; it is not a pole identity applied off-class. The equality `β₁=15` is an identity, not a floor.

**Toric model (used in §4, not in `β₁`).** `Newt(g)=conv{(0,0),(4,0),(0,3)}` for the defining polynomial of `D′`: `deg_u g=4` monic (integrality of `r` over `C[q]`), `deg_y g=3` with constant leading coefficient (unique infinite place, degree-4 form `c u⁴`). Area 6, interior lattice points 3 (Pick: `B=4+3+gcd(4,3)=8`, `I=6−4+1=3`). The identification `X_Σ` as `P²` blown up at the four infinitely-near `L_∞`-points of the hyperflex, with `C₁²=12` and `I(C₁,C₂;P_∞)=9`, is consistent with `16−4=12` and `13−4=9`. This is supporting bookkeeping, not a second derivation of `I(Q′)`.

**Promotion.** Promote Lemmas 2.1a, 2.1b, the identity `I(Q′)=13`, Lemma 2.3, and the row-level value `β₁=15`. This upgrades a PROVISIONAL ROW-SWEEP datum to a theorem of the fold structure. FIXED-TUPLE numerics that were conditional only on `β₁=15` (in particular `e(ι)=10−β₁=−5`) become unconditional on that scalar; they remain conditional on whatever else they used.

## 4. Restriction / cover argument (§3)

**Verdict: HOLDS.** Proposition 3 is a surjection `Γ↠G` carrying meridians to meridians. The direction cost is correctly identified. The `μ`-null-homotopy of FIXED-TUPLE §9 is the same map, written from downstairs.

Notation. `G=π₁(C²−D)`, `Γ=π₁(C²−(D′∪D′⁻))`, `U=C²−D`, `W=ν⁻¹(U)`, `L₀={x=0}`, `L₀′={u=0}`, `A=π₁(U−L₀)`, `B=π₁(W−L₀′)`.

`ν: W−L₀′→U−L₀` is the unbranched Galois double cover `u↦u²` (Lemma 2.1a: `L₀` is not a component of `D`). Thus `B⊴A` of index 2 and `A=B·⟨m⟩` with `m=μ_{L₀}` the nontrivial `ℤ/2` winding class.

Filling a removed divisor kills its meridian normally. A generic point of `L₀` lies in `U` (finitely many intersections with `D`), so a small transverse disk at such a point lies in `U` and `m` is null-homotopic in `U`. Hence `G=A/⟨⟨m⟩⟩_A`. Upstairs, `ν_*(μ_{L₀′})=m²` (the loop `u=ε e^{iθ}` maps to `x=ε² e^{2iθ}`), and `m` itself does not lift to a closed loop, so as subgroups of `A` one has `μ_{L₀′}=m²∈B`. Filling `L₀′` in `W` kills that element: `Γ=B/⟨⟨m²⟩⟩_B`.

The inclusion `⟨⟨m²⟩⟩_B ⊆ ⟨⟨m⟩⟩_A ∩ B` gives `Γ↠ B/(⟨⟨m⟩⟩_A ∩ B)`. The second isomorphism theorem with `A=B⟨m⟩` and `m∈⟨⟨m⟩⟩_A` identifies the target with `A/⟨⟨m⟩⟩_A=G`. So `n_*:Γ↠G`. At a generic point of `D′` the map `ν` is a local biholomorphism, so meridians of `D′` and of `D′⁻` go to meridians of `D`. Every transposition-valued `S₄`-quotient of `G` therefore pulls back to one of `Γ`.

**Direction.** The map is `Γ↠G`, so `{S₄`-quotients of `G} ⊆ {S₄`-quotients of `Γ}`. Killing the row through the fold requires the strictly stronger statement that `Γ` has no such quotient. This is a structural cost, not a defect.

**ι-equivariance.** `ν∘ι=ν` gives `n_*∘ι_*=n_*`. With basepoints not fixed by `ι`, the identification of `π₁` at `w₀` and at `ι(w₀)` conjugates: `ψ∘ι_*=c_γ∘ψ`. Any kill that uses only “`Γ↠S₄`, meridians↦transpositions” discards this; any kill that uses it re-imports the downstairs problem. Both options are correctly typed.

**FIXED-TUPLE §9.** That argument starts from `φ(μ_{L₀})=e` (null-homotopy in `C²−D`) and the splitting `π₁(U°)=π₁(W°)·⟨μ_{L₀}⟩`. It is the same surjection, written from downstairs. The charged report’s claim to re-derive it is accurate; the “slightly stronger” wording is the explicit recording of `ι`-equivariance, which FIXED-TUPLE left implicit.

No promotion issue. The argument is classical covering-space algebra and does not consume PROVISIONAL data.

## 5. N–A union deficit (§4)

Promoted N-A (integration §1; Nori 3.27 as the nodal core): `X` smooth projective; `D,E` reduced, no common components; every singular point of `D` a double point of two smooth branches of contact `k_p≥1`; `D∪E` NC along `D−Sing D`; `E∩ Sing D=∅`; if every irreducible `C⊆D` has `C²>2r₁(C)+4T(C)+T_x(C)`, then `ker(π₁(X−(D∪E))→π₁(X−E))` is f.g. abelian with finite-index centraliser. The inequality is **strict**. Nori p. 331 writes `C²>2r(C)`; WLT(C) on p. 330 divides by `B²−2r(B)`, which vanishes at equality. Strictness is load-bearing in the sourced proof.

### 5.1 `C_i²=3` on every admissible surface

**Verdict: HOLDS.**

**Warm-up, single component: `π₁(C²−D′)=ℤ`.** Blow up `Q′` and the three infinitely-near points of the hyperflex (contact 4, curve already smooth, so each blow-up drops self-intersection by 1). On the resulting `X₀`: `C̃′²=16−4=12`; `C̃′` meets `E=L̃_∞∪E₁∪E₂∪E₃∪E₄` transversally at one smooth point of `E₄`; `Sing C̃′` is the three affine nodes, disjoint from `E`; `X₀−E=C²`. N-A applies with `r₁=3`, `T=T_x=0`, and `12>6`. Then `π₁(X₀−E)=1`, so `π₁(C²−D′)` is f.g. abelian. For an irreducible affine plane curve, `H₁=ℤ`, and an abelian group equal to its abelianisation is `ℤ`. This is row-level (degenerate roots of `r` do not create self-singularities of `D′`). It recovers the charged “coprime Main Theorem ⇒ `π₁(C²−D′)=ℤ`” from promoted N-A alone. **Promote this.**

**The union.** Now `D=C₁∪C₂` with `C₁=D̄′`, `C₂=D̄′⁻`, and `E` the divisor at infinity. Singular points of the union are: self-nodes (`k=1`), affine cross-points (`k=μ_τ`), and `Q′` (`k=13`). The last lies on `E`, so `E∩ Sing D=∅` fails until one blows up the 13 common infinitely-near points of two smooth branches of contact 13. Lemma 3.2 (blow-up invariance of the kernel) is promoted. After 13 blow-ups: `C₁∩C₂` is the 3 affine cross-points only; each `C_i` meets `E` only in `E₁₃`, transversally, at a smooth point of `E`; `E∩ Sing D=∅`; `D∪E` is NC along `D−Sing D`; `X−E=C²`. Each blow-up is at a smooth point of `C_i`, so `C_i²=16−13=3`.

Fewer blow-ups leave a point of `C₁∩C₂` on `E_k⊆E`. More blow-ups only lower `C_i²`. The toric model of §2.3 starts at `C_i²=12` with `I(P_∞)=9` and again yields `12−9=3`; it is `P²` blown up at the four hyperflex points, the same computation. `E` does not appear in the N-A inequality. On any surface obtained from `P²` (or from `X_Σ`) by further blow-ups that make the N-A hypotheses hold, `C_i²≤3`.

### 5.2 Threshold `2r₁=6` and deficit-3 robustness

**Verdict: HOLDS.** N-A does not fire on the union, for any member of the row, in any admissible configuration.

Readings of the promoted charge, most favorable first.

Nori 3.27, applied to a nodal union after the 13 blow-ups, asks `C²>2r(C)` per irreducible component. Here `r(C)` is the number of singular points of that component (self-nodes): the affine cross-points are smooth points of each `C_i`. So `r₁=3`, `T=0`, and after separation at infinity `T_x=0` in the generic pattern `(μ)=(1,1,1)` (transverse cross-points are ordinary nodes of the union, not extra contact). The inequality is `3>6`, false. Deficit exactly 3.

If `r₁` is read as *all* nodes of `D` on `C` (self plus cross), the right-hand side rises to 12 and the failure widens. If `T_x` is read as `Σ_p k_p` over tangential cross-points — the reading that reproduces the promoted sharpness datum of two bitangent conics (`C²=4`, `T_x=2+2=4`, `4>4` false; Nori p. 331 plus the independently sourced `π₁=ℤ*ℤ/2`) — then `T_x=0` here because the components have been separated at infinity. In the degenerate patterns `(μ)=(2,1)` or `(3)` one may either charge the affine tangential cross-point (`T_x=2` or `3`) or blow it up (costing a further `μ` from `C_i²`); both worsen `3>6`.

The most favorable reading already fails. **N-A does not fire.** This is a route-failure, not a theorem that `Γ` has an `S₄` quotient (FALLACY-v2, floor/attainment). The charged report says so.

### 5.3 Exchange-rate / deficit 1 downstairs

**Verdict: HOLDS**, as an identity comparison. The fold strictly loses ground for N-A.

Embedded resolution of a one-place degree-`d` curve: `C̃²=d²−Σ m_i²`, and `Σ m_i²=Σ m_i(m_i−1)+Σ m_i=2δ_∞+M_∞` with `M_∞=Σ m_i` (promoted M-INF piece 1). For the nodal residual, `2r₁=2δ_aff=(d−1)(d−2)−2δ_∞`. The `2δ_∞` terms cancel, and

```text
C̃² > 2r₁  ⟺  d² − M_∞ > (d−1)(d−2)  ⟺  M_∞ < 3d−2,
```

i.e. `M_∞≤3d−3` integrally, the promoted (M-INF) gate. For this row, characteristic pair `(2;15)`, multiplicity sequence `(2⁷,1,1)`: `M_∞=16`, `Σ m_i²=7·4+1+1=30=2δ_∞+M_∞=14+16`. Downstairs `C̃²=36−30=6` against `2r₁=6`: deficit 1 (the known miss). Upstairs, deficit 3. The fold trades one irreducible curve missing the gate by one unit for two curves each missing it by three.

The exchange identity: `a=2` gives `δ_∞=(β₁−1)/2` and `M_emb=β₁+1`, so `Σ m_i²=2β₁`. Lemma 2.3 says `I(Q′)=β₁−2`. Downstairs one spends `2β₁=30` out of `d²=36`; upstairs one spends `β₁−2=13` out of `16`. That is the “wrong way” comparison. It is not a new theorem about `π₁`; it is a correct numerical diagnosis of why N-A cannot be rescued by the fold.

**§4.3(a)–(c), briefly.** (a) Refusing to manufacture an aggregate N-A is mandatory: the integration records the Zariski-sextic and bitangent-conic countermodels as REFUTED and binding. `OPEN[NA-AGGREGATE-REDUCIBLE]` is correctly typed and unused. (b) The `u`-projection 6-section setup is plausible at desk scale (4 simple branches + 6 nodes + 3 disjoint full twists at `u=0` = 13 relations on 11 discriminant values); deciding it is not desk-scale. `OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]` is correctly typed. (c) Euler characteristics of the pulled-back `S₄`-cover: `χ_c(C²−D)=3` and `χ_c(C²−(D′∪D′⁻))=8` re-derive. The displayed formula for `χ(Y)` writes `−3+Σ s_P+6` where the parallel expansion `4·3+3·(−2−3)+Σ s_P` equals `Σ s_P−3`. The extra `+6` is an **arithmetic slip**. The `Y′` line is consistent (`Σ−16`). FIXED-TUPLE §6.3’s value `χ_c(Y)=3` is the case of three disjoint nodes (`s_P=2`, `Σ=6`), matching `Σ−3` not `Σ+3`. The slip is not load-bearing: no parity kill was claimed, and none appears after the repair. Do not promote the displayed `χ(Y)` line.

## 6. Verdict logic (§5) and successor typings (§6)

### 6.1 §5 verdict: fold route fails intrinsically

**Verdict: CONFIRMED as a route-closure, with the charged caveats intact.**

The lane was a braid-free kill attempt: fold the row, apply two-component N-A to `D′∪D′⁻`. Items (1)–(6) of the charged §5 are, after the repairs of §§1–5 above:

1. FOLD is row-level (repaired uniqueness parenthetical, theorem intact); `(8,4)` is covered by the shear dichotomy.
2. Geometry of the union is row-level, including `I(Q′)=13` and `β₁=15`.
3. N-A fires on each component separately and gives `π₁(C²−D′)=ℤ`.
4. N-A cannot fire on the union: `C_i²=3` against `2r₁=6`, deficit 3, robust.
5. The fold makes the N-A ledger worse (deficit 1 downstairs, 3 upstairs).
6. Proposition 3 strengthens the goal (`Γ↠G`).

The conclusion “the row SURVIVES the fold route; the route is set up completely and fails at a quantified, intrinsic obstruction” is the right statement for *this* route. It is not a claim that every upstairs argument fails: ZvK-U6 and the equivariant form remain OPEN, as the charged report types. “Intrinsic” means: no choice of the promoted N-A’s `X` and `E`, among surfaces obtained by blowing up `P²` or `X_Σ` until the hypotheses hold, recovers the three units. That is accurate for N-A as promoted. An exotic compactification not dominated by those blow-ups would be a different theorem and is not claimed.

FALLACY-v2 is respected: failure of (4.2) is not evidence that `Γ↠S₄` exists, supplies no floor on attainment, and is not a Keller counterexample. No `charge_basis` line is declared; none is warranted.

**Decision on `OPEN[PI1S4-(6,4)-FOLD-REDUCTION]`: closed as a route, negative.** Confirmed.

### 6.2 OPEN[NA-R1-SHARPNESS-IRREDUCIBLE] and other successor types

**`OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`: correctly posed. Do not relax.**

The question is whether `C²>2r₁` can be weakened to `C²≥2r₁` when `C` is irreducible, `T=T_x=0`, and the only non-nodal point is the resolved place at infinity. Downstairs that is exactly `6≥6`, equivalently `M_∞≤3d−2=16`, which is the unique residual miss.

Why the question is legitimate. Promoted sharpness is about the *`T_x` coefficient* (bitangent conics, two components, `T_x≠0`). It says nothing about strictness of the `r₁` term for an irreducible nodal curve. Nori’s own proof does not reach equality: WLT(C) divides by `B²−2r(B)` (p. 330), and Proposition 3.27 is stated with `>`. So equality is a genuine boundary, not a clerical strictness.

Why it must not be filled by analogy or by this residual. FALLACY-v2 (floor/attainment; no gap by cap or analogy): a lower bound is not exact. Using the `(6,4)` curve itself as a countermodel for the relaxed inequality would assume a nonabelian kernel, which is the residual question. The charged typing — literature-and-countermodel task, *not* a self-serving relaxation — is exactly right. Absent a theorem or a witness with `C²=2r₁`, irreducible, nodal, `T=T_x=0`, and nonabelian kernel, the strict form stands and the row lives.

The OPEN is downstairs, not upstairs, and is the highest-leverage successor only in the sense that a YES would kill `(6,4)` and `(8,4)` on the spot. It is not a new geometric handle on the fold. Routing it as literature-and-countermodel, with a negative control (the bitangent conics remain the `T_x` sharpness witness and are out of scope), is correct.

**Other successor types, checked.**

- `OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]`: correctly typed. A NO kills `(6,4)` and `(8,4)`; a YES decides nothing for `G` (direction cost of §3). Entry data (6 strands, 11 discriminant values, local braid types, forced spanning-tree of four identification relations) is set up, not decided. Not desk-scale, correctly refused.
- `OPEN[PI1S4-(6,4)-FOLD-EQUIVARIANT]`: correctly distinguished from ZvK-U6. It is equivalent to the downstairs problem. Listing it prevents a future lane from mistaking the stronger upstairs decision for the residual.
- `OPEN[NA-AGGREGATE-REDUCIBLE]`: correctly unused; the two promoted countermodels make a naive aggregate unsafe.
- Carried OPENs (`FACTORIZATION`, `TRIPLE-COVER`, `(8,6)/(9,6)` nodal realisation, `NORI-BC-SELF-TANGENT-COEFF`, `PI1S4-D1-DEGREE`): correctly untouched. The observation that FOLD-REDUCTION raises the relative priority of FACTORIZATION is a priority comment, not a mathematical claim.

## 7. FALLACY-v2 audit

- **Flag/place/series.** Not invoked. No cv-flag / physical-place / cover-series identification occurs.
- **Per-ray/exit-set.** No exit-price assertion. No `charge_basis` line; none should be added.
- **Carrier/attainment.** A `ρ_∞`-fixed tuple (FIXED-TUPLE) and a failed N-A inequality are both treated as floors / removed kills, never as `FULL_ACTUAL_EXIT` or as a homomorphism `π₁(C²−D)↠S₄`. Compliant.
- **Pole/interior.** Lemma 2.3 uses the characteristic pair `(2;β₁)` only after `a=2` is read off the FOLD form and the residual vertex class. Compliant.
- **Floor/attainment.** Deficit 3 is a failure of a strict inequality, not an exact value of a π₁-invariant. The charged report does not convert it into an attainment. The sharpness OPEN is typed so as not to fill the one-unit downstairs miss by relaxing the theorem. Compliant.
- **`sat()` wrapping / raw remainder degree / variable/ring map.** No computational remainder in this lane. The witness identity `r∈C[p,q]` is not used as a proof of FOLD; the semigroup argument is. Compliant.
- **Prime label/derivative.** `D′` is a label (fold transform), `q′` is a derivative. Mild overload, not an ambiguity that changes a count. Noted, not charged.
- **Merge-free/M-descent; target/arrival index.** Not invoked. Target automorphisms are distinguished from source maps throughout.

No silent cap. Residuals that are not proved are typed OPEN.

## 8. Item-by-item verdicts and promotion recommendation

| Item | Charged claim | Gate |
|---|---|---|
| Theorem FOLD | every `Δ=(6,4,3)` member is `{(r²,q)}` after a triangular target automorphism | **HOLDS** (delete/replace the “only 3-gap semigroup” sentence) |
| `(8,4)` shear dichotomy | lands on coprime `(7,4)` (Main Theorem) or on `(6,4)` (FOLD) | **HOLDS** |
| Hyperflexes at a common point | both quartics, `Q′=[0:1:0]`, contact 4 with `L_∞` | **HOLDS** |
| Cross-locus over `{u=0}` | one point per root of `r`, contact `μ_τ`, `Σμ=3` | **HOLDS** |
| Bézout `I(Q′)=13` | `16=3+I(Q′)` | **HOLDS** |
| Lemma 2.3, `β₁=I(Q′)+2` | characteristic pair `(2;m+2)` | **HOLDS** |
| Unconditional `β₁=15` | row-level, upgrades PROVISIONAL | **HOLDS** — promote |
| `π₁(C²−D′)=ℤ` from N-A | single-component, `12>6` | **HOLDS** — promote |
| Prop. 3, `Γ↠G` | meridians to meridians; direction cost | **HOLDS** |
| `C_i²=3` on every admissible surface | 13 blow-ups, toric agrees | **HOLDS** |
| Deficit exactly 3, robust | even the most favorable reading `3>6` fails | **HOLDS** as a route-failure |
| Exchange rate; deficit 1 downstairs | `C̃²=6=2r₁`; fold loses ground | **HOLDS** as identities |
| `χ(Y)` display in §4.3(c) | `−3+Σs_P+6` | **ERRATUM** (`Σs_P−3`); not load-bearing |
| §5 verdict, route closed negative | fold does not kill the row | **CONFIRMED** |
| `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` | pose strict-vs-nonstrict for irreducible `T=T_x=0` | **CORRECTLY POSED**; do not relax |
| ZvK-U6 / equivariant / aggregate OPENs | typed, unused as kills | **CONFIRMED** |

**Promotion recommendation.**

Promote, at written (repaired) scope, independently of the PROVISIONAL witness polynomials:

- Theorem FOLD (§1), with the uniqueness parenthetical deleted or replaced by the δ-sequence / Gorenstein isolation of `⟨3,4⟩`.
- The `(8,4)` shear dichotomy (§1.3).
- Lemmas 2.1a, 2.1b; `I(Q′)=13`; Lemma 2.3; the row-level identity `β₁=15`.
- `π₁(C²−D′)=ℤ` from promoted N-A.
- Proposition 3 (`Γ↠G`).
- The identities `C_i²=3`, downstairs `C̃²=2r₁=6`, and the (M-INF) rewriting `C̃²>2r₁ ⇔ M_∞≤3d−3`.

Do **not** promote: the uniqueness-of-semigroup sentence; the displayed `χ(Y)` line; any statement that `Γ` (or `G`) does or does not admit an `S₄` quotient; any relaxation of N-A to `C²≥2r₁`.

The lane `OPEN[PI1S4-(6,4)-FOLD-REDUCTION]` is closed as a route, negative. The fold is now a complete row-level geometric description of the residual, and it does not kill the row by promoted N-A. Highest-leverage remaining combinatorial successor remains `OPEN[PI1S4-(6,4)-FACTORIZATION]`; the new geometric successor of substance is `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`, to be attacked as literature-and-countermodel, never as a self-serving weakening.

Default-to-refutation balance: one charged uniqueness sentence is false; one Euler display is wrong; every load-bearing geometric and N-A claim re-derived. The β₁ upgrade is real. The route-failure is real. The sharpness OPEN is honestly typed.

<!-- BODY-END -->

