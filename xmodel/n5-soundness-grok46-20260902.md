# N5-SOUNDNESS — is geometric degree 5 soundly closed?

Lane: Card III of `ideation-20260902T0022Z-grok46.md` (synthesis-adopted).
Date: 2026-09-02. Model: Grok 4.6. Desk literature only; no CAS; no census.

**Headline.** Geometric degree 5 is soundly closed. Żołądek Theorem 6.12 does not route through the GGV-gapped Lemma 4.10. Independently, Sigray’s `td=5` slice dies by a pole-`M=1` pin that never enters the gapped Section 9 transitions. DET-LINF does not repair 4.10. No N=5 census is launched from this lane. The residual after H2 is reducible `A_F`.

---

## 0. Custody

Charged ideation, byte-exact:

```text
83319c5e0ddbdb2bfa43b983aae28c57474703205e244cda6e1460942e5809b9  ideation-20260902T0022Z-grok46.md
```

Three charged PDFs, hashed before opening, byte-exact against the Card III custody values:

```text
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60  refs/guccione_valqui2017_ja471_shape_counterexamples.pdf
```

Żołądek is *Topology* 47 (2008) 431–469 (39 PDF pages, printed pp. 431–469). Sigray is the 2008 ELTE thesis *Jacobian trees and their applications* (66 pages). GGV is *J. Algebra* 471 (2017) 13–74, arXiv:1401.1784v3.

Firewall (FALLACY-v2): Newton edge `I_2` is not the dual-graph subgraph `L̃_∞`; a dicritical is not a Puiseux place of `D`; `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`; a floor is not an attainment. No `charge_basis` line: this lane asserts no new exit price. Packages `(F1)/(F2)/(S1)/(S2)/(S4)` are not rederived. Bare `G2` is not used. No other `20260902T0022Z` lane report was opened as a source.

Banked consumers read only after the PDFs: DET-LINF (`domrina-gap-repair-opus5-20260901.md`, hostile-confirmed), Sigray §8–§9 audits, CAGE-N-R2 at `N=5`. Corroboration, not substitutes.

Geometric degree, topological degree, and field-extension degree `[C(x,y):C(f,g)]` are the same integer `N`. GGV’s `B = min gcd(deg P, deg Q)` is a *total-degree* gcd. The two are not identified.

---

## 1. The GGV objection, pinned

### 1.1 Exact words

GGV, *J. Algebra* 471 (2017), introduction p. 2, citing Żołądek as [15]:

> We also found [15, Theorem 4.12] from which `B ≠ 2p` follows. But the proof relies on [15, Lemma 4.10], which has a gap, since it claims without proof that `I₂ ⊂ (1/m)Γ(f₂)`, an assertion which cannot be proven to be true. The same article claims to have proven that `B > 16`, and the author claims to have verified that `B > 33`, but it relies on the same flawed argument, so `B ≥ 16` remains up to the moment the best lower limit for `B`.

GGV’s [15] is Żołądek, *Topology* 47 (2008), 431–469 (bibliography item [15], p. 70 of the journal PDF). The inclusion is not in Lemma 4.10’s *statement*. It is the first sentence of the *proof*, printed p. 447:

> **Lemma 4.10.** When the inverse slope `γ = l/k < 1` and `k ≤ 6` for some right edge in `0₀`, then `gcd(α, β)` is a product of at least two primes.

> **Proof.** By Lemma 4.9 we can assume that it is the first right edge `I₁` with the chart `θ₁` and the next chart `θ₂` on a road to transit has depth 2. So we have to show that `θ₂` cannot be transitory. `θ₂` is associated with an edge `I₂ ⊂ (1/m) 0(f₂)` with vertices in the lattice `(1/k)ℤ × ℤ`. It follows that `p₀(θ₂) = p(θ₂)/m ∈ (1/k)ℤ` and is `≥ 1/k`. We have then the inequality
>
> `p(θ₂) + q(θ₂) + γ(θ₂) > (m+n) p₀(θ₂) + γ ≥ 5 · (1/k) + (1/k) = 1`,
>
> whereas for a transitory chart we should have `p + q + γ − 1 = 0` (Definition 3.13).

GGV writes `Γ(f₂)` for Żołądek’s Newton polygon/diagram of the Puiseux polynomial `f₂` produced by Algorithm 2.10 after the first right chart. The unsupported claim is exactly that inclusion-plus-lattice: vertices of the successor edge lie in `(1/k)ℤ × ℤ` after a `(1/m)`-scaling of `0(f₂)`, which is what feeds `p₀(θ₂) ≥ 1/k` and the comparison with `(m+n) ≥ 5` (the Abhyankar pair `(m,n)=(3,2)`). GGV do not assert a counter-model to the *conclusion* of 4.10; they assert that this lattice step is not proved and “cannot be proven to be true.” This lane does not fill that gap by cap or analogy. Typed:

```text
GGV-OBJECTION[I2-SUBSET-(1/m)0(f2)]  = EXACT, IN-PROOF-OF-LEMMA-4.10
LEMMA-4.10-AS-PRINTED                = GAP (unsupported lattice inclusion)
```

The `(1/m)` scaling mixes the web diagram `0₀ = (1/m)0(f)` of the original pair with the Newton diagram of the *substituted* Puiseux polynomial `f₂` from Algorithm 2.10 (printed pp. 437–438). Support of `f₂` lives in the lattice of that substitution, whose denominators are those of `γ₁ = l/k`, not a free `(1/m)`-shrink of `0(f₂)`.

### 1.2 What consumes Lemma 4.10

Direct citations of Lemma 4.10 in the official PDF, and only these:

| Consumer | Printed | How 4.10 is used |
|---|---|---|
| Theorem 4.12 | p. 448 | `gcd(α,β) ≠ 2`. At `p₀=1` one has `t=l=1`, `k=2 ≤ 6`, “we can use Lemma 4.10.” |
| Lemma 4.13 | p. 448 | `α ≠ 3`. The leftover pair `(α,β)=(3,6)` has `l=1`, `k=3 ≤ 6`, “see Lemma 4.10.” |
| Lemma 4.15 | p. 449 | If `α/β = 3/2` then `α>6`. For `α≤6`, “`gcd(α,β)` is a prime; hence Lemma 4.10 holds.” |

Theorem 4.16 (`α+β > 16`, p. 449) consumes 4.13 and 4.15, hence is infected through those lemmas. Its remaining case `(α,β)=(4,12)` *refuses* 4.10 (“we cannot apply Lemma 4.10 because `gcd(α,β)=2·2`”) and switches to Proposition 5.11 + Theorem 5.13. So 4.16 is only partially infected; the `(4,12)` branch is a different argument.

Lemma 4.14 (`β=2α ⇒ α>7`) never cites 4.10, but writes a cousin lattice estimate for `k=7`. Same species, not a citation; typed `OPEN` as infection, not merged.

Not consumers of 4.10 (citation graph on the official text):

- Theorem 4.7 (Appelgate–Onishi `gcd(α,β)≠1`): Lemma 4.6 + Theorem 3.2.
- Lemma 4.9, Lemma 4.11 (`α≠2`): 4.9 and Proposition 4.2, not 4.10.
- Theorem 5.13 (`gcd(α,β)=η₁⋯η_{N-1}`): Section 5 quasi-Puiseux; Section 4 *uses* 5.13, not conversely except in the `(4,12)` branch of 4.16.
- Proposition 6.5 (Orevkov Riemann–Hurwitz), Corollary 6.6 (`td=2,3`), Proposition 6.7, 6.9, 6.10, Corollary 6.11, Theorem 6.12.

The paper’s own plan (printed p. 433, restated p. 444) splits the two chapters: Theorems 4.7, 4.12, 4.16 are the Appelgate–Onishi / Heitmann *total-degree* improvements; Theorem 6.12 is the Domrina–Orevkov *topological-degree* improvement. GGV object only to the first chapter.

### 1.3 The low-topological-degree chain does not route through 4.10

Section 6 skeleton, with every Section-4 citation checked:

- Definition 6.1–6.3, Lemma 6.2: non-properness set from Theorem 3.14.
- Proposition 6.5: Orevkov; Riemann–Hurwitz on the squeezed map `ẽP: Z̃ → Ỹ`.
- Corollary 6.6: `td=2,3` die; `td=4` (resp. 5) has at most 2 (resp. 3) non-properness divisors. Input: 6.5 only.
- Proposition 6.7: `μ_D = l−k` from `Jac θ̃ = v^{l-k-1}`. No Section 4.
- Proposition 6.9–6.10: `td` is a sum over transitory charts.
- Corollary 6.11: four explicit `(φ,ψ)` forms for `td=4,5` (Cases 1–4). Inputs: 6.10, Proposition 3.15(c), Theorem 3.2. No 4.10.
- Theorem 6.12: “Any Jacobian map `P` with `degtop P ≤ 5` is invertible.” Proof A–M, printed pp. 461–465. Inputs named in the proof: Corollary 6.11, Proposition 6.9, Corollary 6.6, Proposition 5.11, Lemma A.7, Proposition 6.7, Proposition 6.5, Theorem 3.2, Definition 3.13. **Lemma 4.10, Theorem 4.12, and Theorem 4.16 are not cited, and no quantity they produce (`gcd(α,β)≠2`, `α+β>16`) is used.**

Terminals of Cases 1–4 (Corollary 6.11) are slope or degree excesses (`degtop ≥ 5`, `γ₁ < 0`, `1−γ₁ > 1`), not lattice inclusions of `I₂`.

This lane did **not** line-replay every displayed fraction in A–M. GGV raise no objection to 6.12. Typed:

```text
THM-6.12-DEPENDS-ON-4.10     = NONE
THM-6.12-PRINTED-ARITHMETIC  = NOT-LINE-REPLAYED
                             OPEN[ZOLADEK-6.12-ARITHMETIC]
                             as a campaign-standard replay, not as a GGV gap
LOW-TD-CHAIN-THROUGH-5       = COR-6.6 → COR-6.11 → THM-6.12
                             (Sections 3, 5, 6, Appendix; not Section 4 gcd)
```

Absence of a citation is a dependency fact. It is not a line-by-line proof of 6.12. The two are not merged.

### 1.4 What the 4.10 gap actually costs

Infected, and only these, as *Żołądek claims*:

- `gcd(α,β) ≠ 2` (Theorem 4.12), i.e. Żołądek’s `B ≠ 2p` route.
- `α+β > 16` (Theorem 4.16), i.e. Żołądek’s `B > 16` / `deg P > 48` route, except possibly the `(4,12)` branch.
- The unverified `α+β ≤ 34` desk check (Remark 4.17).

GGV independently prove `B ≥ 16` (§6) and `B ≠ 2p` (Corollary 7.9) over any characteristic-zero field. Those are total-degree firewalls. They do not decide geometric degree 5.

---

## 2. DET-LINF retyped; not a repair of 4.10

### 2.1 Named objects, Domrina source

Banked Lemma DET-LINF (hostile-confirmed): `det L̃_∞ ≤ 0`, unconditionally, from properness of `F^{-1}(C²) → C²` plus Hodge index plus Grauert. Floor, not strictness. Determinant convention `det(−A_Q)`.

Named triple:

| Slot | Name | Source |
|---|---|---|
| Ambient | `X̃` | Domrina II, pp. 1–2: compactification of the source plane; `F: X̃ → X` extends the Keller map. |
| Boundary | `L̃ = X̃ \ C̃²` | Tree of nonsingular rational curves; `Pic(X̃)` freely generated by its components. |
| Dicriticals | `g̃₁, g̃₂` | Leaves of `L̃`; Proposition 1.2: `F` non-constant on each. Two-dicritical N=4 shape. |
| Subgraph | `L̃_∞ := L̃ − g̃₁ − g̃₂ = F^{-1}(L)` | Dual graph of components mapping to the target line at infinity. |
| Form | intersection form of `X̃`, signature `(1, ρ−1)` | Hodge index; restriction to `span(L̃_∞)` has at most one positive eigenvalue. |

### 2.2 The same lemma on a Żołądek infinity tree

Żołądek’s compactification (Notations p. 432, Definition 3.3, Definition 6.3):

| Slot | Name | Source |
|---|---|---|
| Ambient | `Z` | `π: Z → X = CP²`, resolution of indeterminacies of `P̂`. |
| Boundary | `A(P)` | Intersection graph of exceptional divisors plus the line at infinity; N–P graph `N(P)` is the chart-encoding of a subtree. |
| Dicriticals | non-properness divisors `D ∈ A(P)` | Theorem 3.14 / (6.1): image is `S(P)`. Żołądek reserves “dicritical” for one polynomial; “non-properness” is the map-level object. |
| Subgraph | `A_∞(P)` | Divisors sent to `Y_∞` (the squeezed point `[Y_∞]` in `Ỹ`). Complement in the boundary of the non-properness components. This is the Żołądek name of `L̃_∞`. |
| Pic | `Pic(Z)` generated by `A(P)` | Same Hodge-index setup once `Z \ A(P) ≅ C²`. |

DET-LINF retyped: `det A_∞(P) ≤ 0` (Domrina sign). The proof uses affineness of `P^{-1}(C²)`, connectedness of `A_∞(P)` after deleting leaves, and Grauert — not N=4, and not that there are exactly two dicriticals (Corollary 6.6 allows three at `td=5`). `A_∞(P)` is the complement of *all* non-properness components. Domrina vertex names are not exported onto `N(P)`.

### 2.3 Sigray’s tree is the wrong ambient

Sigray §3: `T_a^*` is the Eggers–Wall tree of the compactified fibre `R̄_a`, two components `T_{a,x}^*`, `T_{a,y}^*`, vertices `V_a = V_{1,a} ∪ V_{2,a} ∪ {(0,x),(0,y)}`, poles `T_{a,pole} ⊂ T_a^+`. This is a combinatorial Puiseux tree of a *curve*, not a dual graph of a *surface* compactification of `C²`. Sigray never defines `Pic` of an ambient surface, never writes an intersection matrix, never names a determinant of a subgraph.

Identifying `T_a \ T_{a,pole}` with `L̃_∞` would mix a fibre-Puiseux flag with a surface dual graph. No surface model is in the thesis. Typed:

```text
DET-LINF-ON-SIGRAY-TREE  = OPEN
```

Not a gap in DET-LINF. Not filled by treating `T_a` as `L̃`.

### 2.4 Comparison at the 4.10 instance

The 4.10 instance is: first right edge of `0₀` with inverse slope `l/k < 1` and `k ≤ 6`; successor chart `θ₂` of depth 2; claimed `I₂ ⊂ (1/m)0(f₂)` with vertices in `(1/k)ℤ × ℤ`.

| | DET-LINF | Lemma 4.10 inclusion |
|---|---|---|
| Object | sign of an intersection form on a dual graph of curves on a surface | containment of a Newton-diagram edge in a scaled lattice |
| Lives on | `A_∞(P)` / `L̃_∞` | support of the Puiseux polynomial `f₂` after one chart |
| Quantifier | all Keller maps (unconditional floor) | right edges with `k ≤ 6` |
| Output | `det ≤ 0` | `p₀(θ₂) ≥ 1/k`, hence `θ₂` not transitory, hence `gcd(α,β)` has two prime factors |

Different categories: Hodge index on `A_∞(P)` does not produce the Newton denominator `k`. The 4.10 inequality `p+q+γ > 1` compares with the transitory relation `p+q+γ=1` (Definition 3.13), not a determinant. Equivalence is false. DET-LINF ⇒ 4.10 has no typed path.

```text
DET-LINF-VS-4.10  = ORTHOGONAL
DET-LINF-REPAIRS-4.10  = NO
```

Card III’s “if yes, the literature N=5 repairs at that lemma” is a no. N=5 is not repaired *at 4.10*. It does not need to be: 6.12 and the Sigray `td=5` pin do not use 4.10.

---

## 3. Sigray Theorem 9.1 at geometric degree 5 only

### 3.1 Printed theorem: GAP

Sigray, printed p. 60:

> **Theorem 9.1.** Assume that `(f,g)` is a counterexample of the Jacobian conjecture. Then `td(f,g) ≥ 6`.
>
> **Proof.** Since the topological degree is invariant under composition with automorphisms, we may assume that `(f,g)` is a normalized. By Propositions 9.1 and by Statement 9.12 one has `td(f,g) ≥ 6`.

Proposition 9.1 is the multiplicity-data table (23), not a kill. Statement 9.12 is the (misnumbered) row-4 exclusion. The one-liner does not select the `td=5` rows, does not pin `M` at a pole, and does not apply Proposition 8.4. The introduction’s phrase “extend it to the topological degree 6” (p. 45) overclaims: Theorem 9.1 only asserts `td ≥ 6`, and Section 9 does not exclude `td=6` (single-pole rows 8, 9 and the two-pole `3+3` survive the entry pin). Printed Theorem 9.1 is **GAP**.

Banked §9 audit is consumed only as a map of printed defects. The `td=5` argument below does not use Statements 9.3–9.12, Notation 9.3, E2–E4, or the local-exit budget.

### 3.2 The `td=5` pole pin, replayed

Stand on Sections 5 and 8 plus the `Λ=5` slice of table (23). Geometric degree 5 is `td(f,g)=5` (Definition 5.1 / Sigray p. 5: topological degree is the field-extension degree).

**One pole.** Proposition 5.8: `td(f,g) = Σ_{F ∈ T_{a,pole}} Λ(F)`. Proposition 5.7: a pole of a normalized counterexample of type `(α,β)` has `Λ(F) ≥ β`. Abhyankar–Sigray type has `1 < α < β` and `gcd(α,β)=1`, so `β ≥ 3`. Thus `td ≤ 5` forces a unique pole, and `td=5` forces `Λ(F)=5`, hence `β ≤ 5`.

**Possible types.** `1 < α < β ≤ 5`, `gcd=1`: `(2,3)`, `(2,5)`, `(3,4)`, `(3,5)`, `(4,5)`.

Statement 5.2(i): `(deg p_F, deg p_{g,F})` and `(D_F, D_{g,F})` are positive-integer multiples `b(α,β)` and `a(α,β)`. Proposition 5.6 / (19): `Λ(F) = D_{g,F} deg(p_F) / ν_F = ab αβ / ν`. Statement 5.2(ii): either `ν | α` and `ν | (bβ−1)`, or `ν | β` and `ν | (bα−1)`. Solve `ab αβ / ν = 5`.

- `(2,3)`: `6ab = 5ν` ⇒ `5 | ab` and `6 | ν`. Then `ν | 2` or `ν | 3`, impossible.
- `(3,4)`: `12ab = 5ν` ⇒ `5 | ab` and `12 | ν`. Then `ν | 3` or `ν | 4`, impossible.
- `(3,5)`: `3ab = ν`. If `ν | 3`, then `ν=3`, `ab=1`: `ν | (bβ−1)=4` fails and `ν ∤ β`. If `ν | 5`, then `ν=5` gives `3ab=5`, impossible.
- `(2,5)`: `2ab = ν`. The only solution compatible with 5.2 is `a=b=1`, `ν=2`: `ν | α=2` and `ν | (5−1)=4`. This is table (23) row 7: type `(2,5)`, `(D, D_g)=(2,5)`, `(deg p, deg p_g)=(2,5)`, `ν=2`, `Λ=5`.
- `(4,5)`: `4ab = ν`. The only solution is `a=b=1`, `ν=4`: `ν | α=4` and `ν | (5−1)=4`. This is row 10: type `(4,5)`, `(4,5)`, `(4,5)`, `ν=4`, `Λ=5`.

No other `Λ=5` row exists. (The first printed “6” in table (23) is row 5, type `(3,4)`, `Λ=4`; a label error, not a missing `Λ=5` row. Hostile review of the table’s eleven numerical rows is used only as corroboration of completeness *up to `Λ≤6`*; the `Λ=5` slice is re-enumerated here.)

**Pole is a nonroot vertex of `T_a^↘`.** Proposition 5.3(i): a pole is not `(0,x)` and not `(0,y)`. Proposition 5.1: at `F=F_P^*` one has `m_F=0`, and `ρ(v) := d_{F_v} + d_{g,F_v} + v − 1` vanishes at the pole, so `d_F + d_{g,F} = 1 − π(F)`. Definition of `T_a^↘` (`T_a&`): `d_F < (1−π(F)) deg(p_F)`. Substitute: `d_F < (d_F + d_{g,F}) deg(p_F)`. For rows 7 and 10, `deg(p_F) ∈ {2,4} ≥ 2` and `d_F > 0` (Proposition 5.3(ii)), so the inequality holds. The pole lies in `T_a^↘ ∩ (V_a \ {(0,y)})`.

**`M_F = 1` at both rows.** Proposition 5.1 gives `m_F=0` at a pole; Proposition 4.2 puts `h_0 = g`; Notation 8.1 then gives `M_F = gcd(deg p_F, deg p_{g,F})`. Row 7: `gcd(2,5)=1`. Row 10: `gcd(4,5)=1`.

**Nonroot Proposition 8.4 kills `M=1`.** Printed Proposition 8.4 (p. 44): a normalized counterexample with singleton pole has `M_F ≠ 1` for every `F ∈ T_a& ∩ V_a`. The printed proof descends `F_0 = F`, `F_{j+1} = F_j^∘` until `(0,y)`, sets `H = F_{n-1}`, propagates `M_H=1` by Proposition 8.3, and contradicts Theorem 6.1 (`l_f < k_f`) on the axis. That descent requires `n ≥ 1`, i.e. the starting vertex is not already the root. Poles are not roots, so the *pole instance* of 8.4 is exactly the printed nonroot argument. The documented root-clause gap of 8.4 (undefined `F_{n-1}` when `F=(0,y)`) is not used.

Therefore neither row 7 nor row 10 can occur. There is no normalized counterexample with `td=5`.

```text
SIGRAY-9.1-PRINTED              = GAP
SIGRAY-9.1-AT-GEOMETRIC-DEGREE-5 = SOUND
  trust = {Prop 5.1–5.8, St 5.2, Prop 4.2, Not 8.1, Prop 8.3,
           printed nonroot Prop 8.4, Thm 6.1, table (23) Λ=5 slice}
  not used = St 9.3–9.12, Not 9.3, E2–E4, local-exit budget,
             root clause of Prop 8.4, any td=6 campaign result
```

This is not a promotion of the thesis as a refereed theorem. It is a typed `td=5` closure along an Eggers–Wall route whose only Section-9 input is the `Λ=5` slice of table (23). The full repaired `td<6` assembly (row 4, Statement 9.12, transitions) is not required.

### 3.3 Comparison with Żołądek 6.12

Two independent routes to “no Keller map of geometric degree 5”:

1. Żołądek Theorem 6.12, refereed, 4.10-free, four transitory forms, arithmetic not line-replayed in this lane.
2. Sigray pole-`M=1` pin at `Λ=5`, unrefereed, repaired only at a nonroot pole, fully replayed above.

Either is enough to refuse an N=5 census launched as a *Keller-existence* screen. A future line-replay gap in 6.12 would still leave the Sigray pin. A future objection to Sigray §§4–5 would still leave 6.12’s citation skeleton 4.10-free. They are not identified.

---

## 4. The free screen

### 4.1 Prime `N` forces primitivity of the monodromy

Let `F: C² → C²` be a dominant polynomial map of topological degree `N`, equivalently `[C(x,y):C(f,g)] = N`. Let `D ⊂ C²` be a curve containing the non-proper value set `A_F` and the discriminant of `F` (for a Keller map, `Jac F = 1` on the source affine plane, so finite ramification is empty and `D` may be taken as `A_F`). The restriction

```text
F : C² \ F^{-1}(D)  →  C² \ D
```

is a finite unramified covering of degree `N`. The fibre functor on the generic point gives a homomorphism

```text
ρ : π₁(C² \ D)  →  S_N
```

whose image `G` is *transitive*: the function field `C(x,y)/C(f,g)` is a field, so the cover of the generic point is connected.

A transitive subgroup of `S_N` is imprimitive if and only if it preserves a partition of `{1,…,N}` into `N/b` blocks of equal size `b` with `1 < b < N`. Then `b` divides `N`. If `N` is prime, no such `b` exists. Hence `G` is primitive.

Block-size obstruction: transitivity plus primality of the degree. No transposition hypothesis; Keller is used only as the covering degree.

### 4.2 The only primitive subgroup of `S_5` containing a transposition is `S_5`

Let `G ≤ S_n` (`n ≥ 2`) be primitive and contain a transposition, say `(a b)`. Define a relation on `{1,…,n}` by `x ∼ y` if and only if `x=y` or `(x y) ∈ G`.

- Reflexive and symmetric are immediate.
- Transitive: if `(x y), (y z) ∈ G` then `(x z) = (y z)(x y)(y z) ∈ G`.
- `G`-invariant: `g(x y)g^{-1} = (g(x) g(y))`, so classes are permuted.

The equivalence classes are therefore blocks of a `G`-invariant partition. Transitivity of `G` makes all classes the same size. The class of `a` has size at least 2, so the partition is nontrivial. Primitivity forces a single class. Thus `G` contains every transposition, hence `G = S_n`.

Specialise to `n=5`. (The argument never used `n=5` except as the ambient symmetric group of the monodromy.)

Independently, the transitive subgroups of `S_5` are, up to conjugacy,

```text
C_5,     D_5 ≅ C_5 ⋊ C_2,     AGL(1,5) ≅ C_5 ⋊ C_4,     A_5,     S_5.
```

All five are primitive, as 4.1 already forces. Cycle types:

| Group | transpositions? | typical odd/even types |
|---|---|---|
| `C_5` | no | 5-cycles |
| `D_5` | no | 5-cycles; double transpositions `(2,2)` (reflections) |
| `AGL(1,5)` | no | 5-cycles, 4-cycles, `(2,2)` |
| `A_5` | no | 3-cycles, `(2,2)`, 5-cycles |
| `S_5` | yes | all types |

So the transposition criterion is sharp at `N=5`: it kills every transitive image except `S_5`.

A transitive subgroup generated by transpositions is likewise `S_5` (connected support graph). CAGE-N-R2 clause 6 is the all-transposition pin; at prime `N` one transposition already forces `S_N`.

### 4.3 What this collapses in the N=5 representation space

Write `ρ: π₁(C² \ A_F) → S_5` for a hypothetical Keller map of geometric degree 5.

- Transitivity is free (`(M-2)` / connected cover).
- Primitivity is free (`N=5` prime). The N=4 campaign’s imprimitivity / block-system residue has no analogue.
- The five candidate images collapse to one as soon as *any* meridian is a transposition.

H2 has already killed the N=5 trivial dicritical. CAGE-N-R2 at `N=5` leaves three profiles in two classes, all `b=1`, no ramified rows; each branched meridian has moved type `1^3 2`. The image is `S_5`.

The N=4 split into an `A_4` class and an `S_4` transposition class has no analogue: no `A_5`, no `C_5`, no `AGL(1,5)`, once a transposition meridian is present. The representation space is

```text
{ ρ : π₁(C² \ D) ↠ S_5  |  some (in the H2-residual, every branched)
                            meridian is a transposition },
```

i.e. connected transposition graphs on five letters with the CAGE-N local-orbit constraints (disjoint transpositions at a node; cycle type `1^{a_i} ∏ μ_ℓ^{s_ℓ}` on component `i`). It is not a census of transitive subgroups of `S_5`.

Cheap filter after H2, not a total-degree ceiling, not an N=4-suite clone. The all-degree `d₂=2` sandwich is not consumed.

---

## 5. Typed verdicts (no census)

```text
GGV-OBJECTION                         = PINNED
  I_2 ⊂ (1/m)0(f_2) is the first sentence of the proof of Lemma 4.10
  (printed p. 447), consumed by Thm 4.12 and, through 4.13/4.15, by
  Thm 4.16. Not a statement-gap; a proof-gap.

LEMMA-4.10                            = GAP
THM-4.12 (gcd ≠ 2)                    = INFECTED
THM-4.16 (α+β > 16)                   = INFECTED (except possibly (4,12))
GGV B≥16 AND B≠2p                     = TOTAL-DEGREE, INDEPENDENT REPAIR
                                      of the infected chapter; not geometric
                                      degree 5

THM-6.12-DEPENDS-ON-4.10              = NONE
LOW-TD-CHAIN-THROUGH-5                = DOES-NOT-ROUTE-THROUGH-4.10
THM-6.12-ARITHMETIC                   = OPEN as campaign line-replay
                                      NOT a GGV gap

DET-LINF at Żołądek A_∞(P)            = RETYPED (ambient Z, Pic generated
                                      by A(P), subgraph A_∞(P))
DET-LINF at Sigray T_a                = OPEN (no surface Pic, no det)
DET-LINF ⇒ 4.10 INCLUSION             = NO (orthogonal categories)
LITERATURE-N5-REPAIRS-AT-4.10         = NO

SIGRAY-9.1-PRINTED                    = GAP
SIGRAY-9.1-AT-GEOMETRIC-DEGREE-5      = SOUND
  (pole-M=1 pin on table rows 7 and 10; nonroot Prop 8.4 as printed;
   Section 9 transitions not used)

PRIME-N-FORCES-PRIMITIVE              = PROVED
PRIMITIVE-PLUS-TRANSPOSITION-IS-S_n   = PROVED (n=5 included)
N=5-REP-SPACE                         = COLLAPSES TO S_5
  as soon as one transposition meridian exists; H2-residual profiles
  already have moved type 1^3 2

GEOMETRIC-DEGREE-5                    = SOUNDLY CLOSED
  by Żołądek 6.12 (4.10-free, refereed, arithmetic not line-replayed)
  and independently by the Sigray td=5 pole pin (unrefereed, replayed)

N=5-CENSUS                            = DO-NOT-LAUNCH
H2-RESIDUAL                           = reducible A_F (Path 1 / CAGE-N-R2
                                      N=5: three profiles, all S_5)
```

Card III stop: first typed closure of degree 5. Stop. Faithfulness remains mandatory for any later Groebner job on a reducible residual; that is Path 1’s client, not this lane. No conductors, no rank-four copy, no Domrina vertex-name export, no identification of `B ≥ 16` with geometric degree 5.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `25588`.
- Body SHA-256:
  `f45b48956431601536fbbdd1d3b2f36e547a79a7db2416540408409e7ada2c36`.
- Frozen basis: `4cd85aa7ab79e86a104152668ca1a3b79571ad96`.
