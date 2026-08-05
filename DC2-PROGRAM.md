# DC(2) Program: Dixmier Conjecture for the Second Weyl Algebra

Status: COMPLETE (design + first experiment run). Experiment: `cases/dc2_slice.py`
(exact ℚ arithmetic; numpy census; msolve slices), 8 s, all assertions PASS.
Date: 2026-08-04

## 1. Statement and reduction landscape

### 1.1 The object
A_2 = A_2(K), char K = 0 (take K = ℚ or ℂ): the K-algebra on x_1, x_2, ∂_1, ∂_2 with
[∂_i, x_j] = δ_ij, [x_i, x_j] = [∂_i, ∂_j] = 0. Simple, Noetherian, GKdim 4; Bernstein
filtration by total degree; gr A_2 ≅ K[x_1,x_2,ξ_1,ξ_2] with its standard symplectic
Poisson bracket.

**DC(2).** Every K-algebra endomorphism of A_2 is an automorphism.

Since A_2 is simple, every endomorphism is injective (kernel is a two-sided ideal ∌ 1),
so DC(2) = surjectivity; equivalently **A_2 is co-Hopfian**: no proper subalgebra of A_2
is isomorphic to A_2 via a CCR embedding.

### 1.2 Counterexample shape: quadruples, not pairs
An endomorphism φ is exactly a **quadruple** (P_1, P_2, Q_1, Q_2) ∈ A_2^4 satisfying the
six CCRs
  [Q_i, P_j] = δ_ij,  [P_1, P_2] = 0,  [Q_1, Q_2] = 0,
(P_j = φ(x_j), Q_i = φ(∂_i)). A DC(2)-counterexample = such a quadruple whose generated
subalgebra is **proper**.

Caveat on the "pair" phrasing: in A_1, DC(1) ⟺ every pair [Q,P]=1 generates. In A_2 the
pair version is *trivially false and irrelevant*: (P,Q) = (x_1, ∂_1) has [Q,P]=1 and
generates a proper subalgebra. The one-pair intuition survives only as: each (Q_i, P_i) is
a Dixmier pair *inside the centralizer of the other two generators*, and DC(1)-type
rigidity is what one would like to apply there (see §2 for why one can't, yet).

Forced properties of a counterexample quadruple:
- image B ≅ A_2, GKdim B = 4 = GKdim A_2: proper subalgebra of *full* GK dimension;
- for every weight w = (ρ_1,ρ_2,σ_1,σ_2) with ρ_i + σ_i > 0, whenever degrees are not
  degenerate the six w-leading forms pairwise Poisson-commute in K[x,ξ]; four pairwise
  Poisson-commuting polynomials on a 4-dim symplectic space have **trdeg ≤ 2** (max
  Poisson-commutative subalgebras have trdeg n = 2) — so leading data is 2-dimensional,
  the quantum analogue of Dixmier's "leading forms are powers of a common form" in A_1;
- Bernstein-top forms of a deg-≤2 quadruple span an abelian subalgebra of
  (Sym²K^4, {,}) ≅ sp_4(K), whose abelian subalgebras have dim ≤ 3 (Siegel nilradical);
- by §4's slice theorem (verified computationally below): all quadruples of Bernstein
  degree ≤ 2 are automorphisms, so a counterexample needs some generator of degree ≥ 3.

### 1.3 Reduction ladder (per-n, post-July-2026)
Known implications (Tsuchimoto 2005; Belov-Kanel–Kontsevich 2007; Adjamagbo–van den Essen
2007; van den Essen for DC_n ⇒ JC_n):

  JC_{2n} ⇒ PC_n ⇒ DC_n ⇒ JC_n   (every n);  stably JC ⇔ DC ⇔ PC.

Instantiated at n = 2 with current status:

  JC_4 (FALSE, Alpöge 07/2026) ⇒ PC_2 (FALSE, Long/@octonion 07-23, Lean ¬PC2⇒¬JC4,
  consistent contrapositive) ⇒ **DC_2 (OPEN)** ⇒ JC_2 (OPEN);  also JC_2 ⇒ DC_1
  (claimed by Zheglov 2410.06959v5, unrefereed); DC_n FALSE for n ≥ 3 (via ¬JC_n).

Reading of the ladder:
1. Both statements known to be *stronger* than DC_2 (JC_4, PC_2) are now false. DC_2 is
   no longer squeezed from above; nothing known contradicts either truth value.
2. DC_2 ⇒ JC_2 is the strongest surviving *proof* route to the plane Jacobian case
   (RECON §TL;DR-4). A DC_2 **counterexample would NOT refute JC_2** (implication runs
   the other way); it would merely orphan JC_2 and kill this route.
3. ¬PC_2 is a structural warning: the *classical/Poisson shadow* of DC_2 is false. If
   DC_2 is true, quantization must be rigidifying — every Poisson counterexample must
   fail to lift to A_2, order by order in the deformation. @octonion's reported near-miss
   lift of a rank-2 Poisson counterexample is exactly an attack on this gap; the lift
   obstruction tower is a concrete object our experiment family probes from below (§4).
4. Mod-p mechanism behind the ladder (Belov–Kontsevich): A_2 ⊗ F_p has huge center
   Z ≅ F_p[x^p, ∂^p] (2n = 4 variables) carrying a canonical Poisson bracket; an
   endomorphism restricts to a Poisson endomorphism of Z which is Keller. This is the
   only known bridge quantum → commutative, and it consumes JC_4/PC_2 — both dead. Any
   new proof strategy for DC_2 must work natively in A_2 (or find a new bridge).

## 2. Zheglov's DC(1) machinery: what ports to A_2, what breaks

Architecture per ZHEGLOV-SCOPE.md §1: (S2) normal forms A_1 ⊂ D_1 = K[[x]][∂] ⊂ D̂_1^sym,
Schur operator S with SPS⁻¹ = ∂^p, centralizer C(∂^p) ≅ M_p(K[D^p]) "vector form";
(S3) GGV subrectangular reduction of a minimal DC-pair; (S4) head-chopping induction
(T:DC-pairs, distance = p+q−1); (S5) string equation ↔ rank-1 commuting pairs (extended
Schwarz correspondence); (S6) Puiseux-side distinguished-coefficient contradiction.

Port map, piece by piece:

| Zheglov piece (A_1) | Role | A_2 status |
|---|---|---|
| Simplicity ⇒ injectivity | frames DC as surjectivity | **ports verbatim** |
| Directed degrees (ρ,σ), leading forms Poisson-commute | ambient calculus for S3/S4 | **ports** — becomes the ℤ^4-weight symbol calculus of §3 (our turf) |
| GGV minimal-pair ⇒ subrectangular polygon | entry point of whole proof | **missing**: GGV 2014 is intrinsically 2-generator/ℤ²; no minimal-counterexample polytope classification for quadruples in ℤ^4 exists |
| Schur normal form SPS⁻¹ = ∂^p + explicit centralizer | converts [Q,P]=1 into finitely many normal-form coefficients | **BREAKS — first genuine obstruction, see below** |
| Head-chopping induction, distance p+q−1 | well-founded descent | needs the normal-form coordinates; also no single well-founded order measure on bidegree pairs identified |
| String equation ↔ rank-1 spectral pairs (BC/Krichever/Schwarz/Wilson) | transports DC-pair to Puiseux/spectral side | **missing theory**: 2-var analogue = commuting PDOs ↔ spectral *surfaces* + sheaves = the Parshin–Zheglov–Kurke program, incomplete and partly conjectural |
| S6 endgame: 1-var Puiseux series X_{N,n}, distinguished coefficient | the contradiction | needs S5's dictionary; 2-var Puiseux geometry qualitatively harder |

**First genuine obstruction (the headline): collapse of Schur/centralizer rigidity.**
Everything in Zheglov's proof after page 1 runs inside normal forms that exist because of
a one-variable miracle (Schur 1905 / Amitsur): in D_1, any operator P of order p is
conjugate (in the completed ring) to ∂^p, and the centralizer of a nonconstant operator
is *commutative and finite* over K[P] (rank ≤ p; spectral curve data). This is what makes
[Q,P] = 1 a statement about finitely many coefficients: normalize P, then Q lives in the
explicitly coordinatized C(∂^p) ≅ M_p(K[D^p]).

In A_2/D_2 both halves fail at the first move:
- **No normal form**: a single operator in two variables is not conjugate to a
  constant-coefficient model; "normal forms of PDOs" in dim 2 is Zheglov's *own open
  research program* (with Kurke/Osipov), not a tool one can import.
- **Centralizers are huge and noncommutative**: C_{A_2}(x_1) ⊇ K[x_1] ⊗ A_1(x_2,∂_2),
  a full Weyl algebra. Normalizing P_1 leaves the remaining three generators in an
  unclassified noncommutative centralizer — nothing is pinned. The quadruple's mutual
  centralizer C(P_1,P_2) is commutative-of-trdeg-≤2 generically (this survives), but
  there is no structure theory of such "spectral surface" centralizers to induct on.

So the strategy dies not at the hard endgame but at step zero: DC(1) is secretly a
theorem about ODOs on a formal disk, where Sato–Schur theory coordinatizes everything
(Wilson's adelic Grassmannian etc.); the corresponding dim-2 spectral theory does not
yet exist. Porting Zheglov = first *completing* the 2D Schur-pair/Parshin program —
a multi-year prerequisite, not an adaptation.

Secondary obstruction (hit immediately after, if the first were solved): GGV's
subrectangular reduction — the classification of minimal counterexample polygon shapes —
has no ℤ^4 analogue; this is where our polytope/vertex-gap machinery (§3) is the natural
candidate replacement, and is independent of the Schur obstruction.

## 3. Lifting our abelian machinery: quantum Newton polygons, strips, towers, vertex-gap

Our abelian kit (LEMMA.md/SURPLUS.md): pairs P,Q ∈ K[x,y], bracket = Jacobian, Newton
strips along a primitive direction, level-ordered unit-pivot elimination ("towers"),
vertex normalization a_{p0}b_{q0} = ±1 at a unique-decomposition Minkowski vertex,
gap-kill, surplus count 2(w_P−1)−z, PINS-form obstruction ⇒ empty chart (proved in the
(k,d2) = (2,2) cell). The quantum lift:

### 3.1 The quantum coefficient calculus (exact, not just leading-order)
Write elements of A_2 normally ordered: P = Σ a_p x^{p'}∂^{p''}, support in ℕ^4. The
product/commutator has an exact finite expansion: the coefficient of [P,Q] at m ∈ ℤ^4
receives contributions from exponent pairs p + q = m + s_1·u_1 + s_2·u_2, s_1+s_2 ≥ 1,
where u_i = (e_i | e_i) are the two **contraction shifts** (contract ∂_i against x_i).
The s_1+s_2 = 1 stratum carries the slot-wise symplectic determinants — exactly our
abelian det(p,q) split into two pieces landing at two different points m; s ≥ 2 strata
are integer-coefficient corrections strictly deeper along the shift cone.

Consequences:
- For any weight w ∈ ℤ^4 with w·u_1 > 0 and w·u_2 > 0, leading forms are well-defined
  and the top stratum of any bracket is the **Poisson bracket of symbols**: our entire
  abelian leading-form calculus applies verbatim to the top strata.
- The corrections are **triangular** for any level functional ℓ with ℓ(u_i) > 0: each
  quantum equation = abelian equation + terms of strictly lower level. Unit-pivot
  elimination and well-foundedness survive; pivots are the same lattice determinants.
  Quantum tower = abelian tower + a filtered perturbation. (In A_1 this is one shift
  u = (1,1) and ℓ = 2i+j has ℓ(u) = 3 > 0 — our exact setup, perturbed.)

### 3.2 Quantum strips and towers
- **Strips**: in A_1, Poisson-commuting leading forms in 2 commutative variables are
  proportional powers ⇒ polygons are strips along a common direction (Dixmier's lemma =
  the abelian top-edges-through-origin picture). In A_2, trdeg of a Poisson-commutative
  subalgebra ≤ 2 ⇒ the four leading forms at any admissible w are algebraically
  dependent through a 2-dim family: polytope faces of all four generators share a common
  2-dimensional "shadow". The A_2 strip analogue = polytopes thin transverse to a common
  2-face. Making this precise (which 2-faces can occur, after normalizing by tame
  automorphisms) is the A_2 replacement for GGV's subrectangular classification — open,
  and the natural first theorem of the program.
- **Towers**: fix a face pair and a level functional ℓ positive on u_1, u_2; order the
  six CCR coefficient equations by ℓ; eliminate coefficients of Q-side generators by
  unit pivots at saturated corners with unimodular slot-dets. New vs. abelian: blocks
  are 2-dimensional (two shift directions), and the SIX brackets share the same four
  coefficient vectors — the towers are **coupled**, so overdetermination should only
  increase. Good for exclusions.

### 3.3 Quantum vertex-gap
The RHS of [Q_i, P_i] = 1 lives at the origin of ℤ^4. Vertex normalization: the origin
must be the bottom vertex (w.r.t. a generic functional) of the shifted Minkowski sum
N(Q_i) + N(P_i) − u_i, attained by corner pairs q_0 + p_0 = u_1 or u_2 (each slot
separately!) with slot-det a unit — forcing saturated near-origin corners, the exact
analogue of "x^k at the strip's bottom vertex", with k = 0 and TWO competing contraction
channels (a genuinely new feature: the vertex coefficient is a sum over both channels,
so unique-decomposition needs a 2-channel condition, e.g. one channel degree-forbidden).
- **Gap condition**: lattice points of a Q_i-polytope strictly between the origin block
  and the bottom corner ⇒ sub-vertex bracket coefficients that are unit-times-linear in
  the gap coefficients ⇒ gap-kill, as in SURPLUS Prop-style triangular induction, now
  along a 2-dim slab instead of a column ladder.
- **Vertex-gap obstruction** (what a DC(2) exclusion would look like): for a candidate
  polytope shape, the near-origin block has more forced-vanishing coefficients than
  eliminable unknowns; a surplus row back-substitutes to (unit)·(monomial)·b_{q0},
  pinning a saturated corner of one generator to 0 against its own vertex equation ⇒
  that polytope shape supports no counterexample quadruple. Redoing SURPLUS Props A/B
  with two shift directions and coupled brackets — the "quantum (2,2)-cell lemma",
  starting in A_1 where the answer is calibrated against Dixmier's classified low-degree
  pairs — is concrete, laptop-checkable, and is the first new mathematics of the lift.

### 3.4 Relation to the Poisson layer
The s = 1 stratum of every statement above is a theorem about PC_2-type quadruples; the
s ≥ 2 corrections are exactly where DC_2 can differ from the (false) PC_2. A shape
exclusion proved only from the s = 1 layer is evidence about the wrong conjecture;
worthwhile exclusions must use the correction terms (they first act at Bernstein degree
3 — see §4). This is the precise sense in which the @octonion lift near-miss and our
tower calculus probe the same object from opposite ends: he descends from a Poisson
counterexample looking for a lift; we climb from low degree looking for the first shape
where the quantum corrections fail to kill a Poisson-consistent configuration.

## 4. Experiment design: finite-dimensional slice of DC(2)

### 4.1 The slice: Bernstein degree ≤ 2 quadruples (Generator-A analogue)
Target statement, checkable by exact linear algebra plus one small quadratic variety:
**every CCR quadruple with all four generators of Bernstein degree ≤ 2 is an
automorphism** — and the constraint variety has explicit structure.

Stratification (derived, then machine-verified):
1. **deg-2 stratum**: the four quadratic tops pairwise Poisson-commute — an abelian
   4-tuple in (Sym²K⁴, {,}) ≅ sp_4; abelian subalgebras of sp_4 have dim ≤ 3.
2. **deg-0 stratum**: on the variety cut by stratum 1 the quantum (s=2) corrections
   cancel identically, forcing the four **linear parts to be exactly symplectic** (no
   quantum deformation of Sp_4 at this depth). Modulo the tame affine-symplectic group
   the slice reduces to the **unipotent slice** P_j = x_j + p_j + c_j, Q_i = ξ_i + q_i
   + d_i (p, q quadratic, c, d constants free).
3. **deg-1 stratum** (linear algebra, 24 equations / 40 unknowns): solution space is
   exactly the 20-dim gradient family — there is a cubic c ∈ Sym³K⁴ with
   p_j = ∂c/∂ξ_j, q_i = −∂c/∂x_i (infinitesimal Hamiltonian structure).
4. Residual variety: **V₃ = {cubics c on K⁴ : the four partials c_{x_1}, c_{x_2},
   c_{ξ_1}, c_{ξ_2} pairwise Poisson-commute}** — 60 quadratic equations in 20 unknowns.
   Conjecture: V₃ = closure of the **Lagrangian-cubic family** {c = f(u_1, u_2) :
   span(u_1,u_2) ω-isotropic}, dim 3 (LGr(2,4)) + 4 (binary cubic) = 7; each such c has
   ad_C² = 0 on generators, so the quadruple is exp(ad C) — a tame automorphism.

Consequence of 2+4 if verified: DC(2) holds in degree ≤ 2, and the slice is entirely
**Poisson-shadow-complete** — quantum corrections first bite at degree 3, so degree ≤ 2
cannot separate DC(2) from the (false) PC(2); the first quantum-sensitive slice is D=3.

### 4.2 Size estimate
Raw slice: 60 unknowns, 90 quadratic equations. After strata 2-3: V₃ ⊂ K²⁰ with 60
quadratics. Checks: exact ℚ linear algebra (24×40 and 20-dim span comparisons); F_2
exhaustive census of V₃ (2²⁰ ≈ 1.05M points, numpy, minutes); exact Jacobian rank at
family points (local dim); exact operator-level CCR + inverse certificates for sample
points (pure-fraction Weyl kernel). Laptop-scale: **yes — minutes.** IMPLEMENTED:
`cases/dc2_slice.py` (self-contained; numpy for the census only).
Next tiers: D=3 unipotent slice ≈ 4×35 unknowns + first genuine quantum corrections
(msolve territory, days); full D=3 ≈ 140 unknowns (heavy but feasible); graded slices
(Shaska-analogue) cheap per weight.

### 4.3 RESULTS (run 2026-08-04, `python3 cases/dc2_slice.py`, 8 s total, all exact)
- **A (affine)**: the 6 CCR residuals of a general affine quadruple equal, monomial for
  monomial, the six independent entries of MᵀJM − J (20 random M). Deg ≤ 1 slice =
  Sp_4(K) ⋉ K⁴ exactly; all automorphisms. PASS.
- **B (deg-1 stratum)**: 24×40 exact linear system has rank 20; the 20 cubic-gradient
  vectors lie in the kernel and are independent ⇒ kernel = gradient family exactly:
  p_j = ∂c/∂ξ_j, q_i = −∂c/∂x_i for a cubic c. PASS.
- **C (structure of V₃)**: the 60 deg-2 residual forms span a 45-dim space of quadratic
  forms on K²⁰; the 6 quantum deg-0 forms (s=2 contractions) lie **inside that span**
  (rank 45 → 45) ⇒ deg-0 residuals vanish identically on V₃: constants free, and the
  D ≤ 2 slice is **Poisson-shadow-complete** — proved by exact linear algebra, not just
  argued. Quantum corrections first act at Bernstein degree 3. PASS.
- **D (F₂ census)**: 2¹⁶ solutions mod 2 — degenerate: 20/60 forms vanish mod 2, 32/60
  become affine-linear (v² = v); witness x₂ξ₂² ∈ V₃(F₂) \ V₃(ℚ) (residual 4ξ₂²).
  **p = 2 is a bad prime for the quantum tower too** (cf. abelian pivot primes {2,3,5}).
  Census recorded as structural only.
- **E (family + local dim)**: 25/25 random Lagrangian cubics c = f(u₁,u₂), ω(u₁,u₂)=0,
  satisfy all 60 forms; controls x₁²ξ₁, x₁³+ξ₁³, generic f(x₁,ξ₁) all excluded.
  Jacobian rank at 5 generic family points = 13 ⇒ V₃ smooth there of local dim 7 =
  family dim (3 for LGr(2,4) + 4 for the binary cubic).
- **F (automorphism certificates)**: 5/5 family quadruples satisfy all 6 CCRs *exactly
  at operator level* (including s ≥ 2 terms); ad_C² = 0 on generators (C commutes with
  everything in K[u₁,u₂]-op since [u₁,u₂]-op = ω(u₁,u₂) = 0); explicit two-sided inverse
  verified ⇒ **automorphisms** (φ = exp(ad C), tame after a partial Fourier). Probe: with
  non-symplectic linear part M and quadratic part in V₃, deg-0 residual = MᵀJM − J
  exactly (10 random M) ⇒ linear parts forced symplectic. PASS.
- **G (global component check, msolve)**: two independent random codim-7 affine slices
  of V₃: both **0-dimensional** (no component of dim ≥ 8), both of **degree 90**; all
  24 real slice points pass the essential-space test (rank ≤ 2, isotropic): every one is
  Lagrangian-type. Cross-check by intersection theory: deg(Lagrangian-cubic locus) =
  ∫_{P(Sym³U*)} ξ⁶ = ∫_{LGr(2,4)} s₃((Sym³U*)^∨); LGr(2,4) ≅ Q³, Chern roots of U*:
  a+b = h, ab = ℓ, h³ = 2, hℓ = 1 ⇒ c₁³ − 2c₁c₂ + c₃ = (216−132+6)h³ + (−120+30)hℓ =
  90h³ − 90hℓ = 180 − 90 = **90. Exact match** ⇒ the top-dimensional part of V₃ is the
  Lagrangian family and nothing else (degrees are additive over dim-7 components).

**Slice verdict: DC(2) HOLDS in Bernstein degree ≤ 2.** Every deg ≤ 2 CCR quadruple =
(affine symplectic) ∘ exp(ad C), C a Lagrangian cubic — all tame automorphisms. The
constraint variety V₃ is (up to possible components of dim ≤ 6, not excluded by the
slices; the abelian-subalgebra classification of sp₄ + Euler integrability should close
this gap by hand) the cone over a smooth degree-90, dim-6 projective variety — the
DC(2) analogue of Generator A's constraint-variety structure. Caveat honestly recorded:
this depth is Poisson-shadow-complete, so it is evidence about the CCR geometry, not yet
about the quantum/Poisson divergence — that starts exactly at D = 3.

## 5. Honest program assessment

### 5.1 Effort tiers
- **T0 (done, this file)**: kernel + complete D ≤ 2 slice theorem, machine-verified;
  V₃ structure with exact degree cross-check. ~1 day.
- **T1 (1-2 weeks)**: D = 3 unipotent slice — the first quantum-sensitive slice: images
  x_j + (quadratic+cubic), s=2 contractions of cubic×cubic hit deg-1 residuals, so the
  gradient structure acquires genuine ħ-corrections. Deliverable: does the Poisson-level
  solution variety (quartic Hamiltonians etc.) deform flatly to the quantum one, or do
  quantum obstructions cut it further? This is the cheapest place the DC≠PC divergence
  is visible. Plus: finish the V₃ = Lagrangian-family proof (abelian subalgebras of sp₄
  + Euler integrability; short appendix).
- **T2 (2-6 weeks)**: graded DC(2) (Shaska analogue): classify ℤ-graded CCR quadruples
  for every weight pattern; homogeneity makes each weight a small exact computation, and
  a full theorem ("no graded counterexample") is plausibly provable — a publishable
  stand-alone result mirroring the dim-2 graded-Keller theorem.
- **T3 (1-3 months)**: quantum vertex-gap counting (§3.3): redo SURPLUS Props A/B with
  two contraction shifts and coupled brackets; first in A_1 (calibrate against Dixmier's
  classified low-degree pairs and Zheglov's L:Q_p tail shapes on automorphism pairs),
  then A_2 polytope-shape exclusions. Outcome: a growing atlas of excluded counterexample
  polytope shapes — the exact analogue of the (72,108) campaign, aimed at DC(2).
- **T4 (years, research program)**: the Zheglov-route prerequisite — 2D normal
  forms/Schur pairs/Parshin spectral theory strong enough to coordinatize centralizers
  in D_2. Not ours to attempt alone; monitor Zheglov–Guo–Kurke–Osipov.
- **T5 (unknown)**: full DC(2).

### 5.2 The hardest open step
Replacing one-variable Schur/centralizer rigidity with *any finiteness mechanism* for
CCR quadruples. In A_1, [Q,P] = 1 lives inside a commutative, rank-bounded centralizer
after one normalization — that finiteness is what every known DC(1) argument (Dixmier's
low-degree cases, Joseph, Zheglov) ultimately spends. In A_2 nothing bounds the
quadruple: centralizers of single elements contain Weyl subalgebras, polytopes live in
ℤ⁴ with a 2-parameter leading-form family, and the tame normalization group is small
relative to the shape space. No candidate mechanism exists in the literature. Second
hardest: proving quantization rigidity (every PC_2 counterexample fails to lift to A_2)
— currently not even conjecturally structured, but ¬PC_2 makes it exactly the content
of DC_2 minus classical geometry.

### 5.3 What a serious 6-month attempt looks like
Months 1-2: T1 + T2 (D=3 quantum slice; graded theorem). Months 2-4: T3 quantum
vertex-gap atlas in A_1 then A_2; audit and reproduce @octonion's Poisson-lift near-miss
— determine the exact cohomological obstruction that killed his lift, and whether it is
shape-generic (if some lift succeeds, DC(2) is FALSE and everything above becomes the
counterexample-search toolkit). Months 4-6: attempt the first nontrivial infinite
exclusion: "no counterexample quadruple with all polytopes in a fixed thin-slab class"
— the DC(2) analogue of GGV's subrectangular reduction, built from T3's counting.
Deliverables even on failure: 2-3 publishable slices/exclusions + a mapped obstruction
landscape. Probability of full DC(2) inside 6 months: low (< 5%); probability of a
decisive intermediate artifact (graded theorem, D=3 divergence data, first shape
exclusion, or a refutation via lift): moderate (~50%).

### 5.4 Verdict
DC(2) end-to-end is out of reach for current machinery — Zheglov's route needs a
still-nonexistent 2D spectral theory, and the classical shadow (PC_2) is false, so no
commutative-geometry shortcut survives. But the low-degree/polytope program is genuinely
open terrain: nobody has published even the D ≤ 2 slice structure we verified today, the
quantum tower calculus is a controlled perturbation of machinery we already own, and
every increment either accumulates evidence/exclusions or finds the counterexample at
the lowest degree where it can live. Right-sized next action: T1 (D=3 quantum slice).
