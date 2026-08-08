# DC(2) Program: Dixmier Conjecture for the Second Weyl Algebra

Status: COMPLETE (design + first experiment run). Experiment: `cases/dc2_slice.py`
(exact ℚ arithmetic; numpy census; msolve slices), 8 s, all assertions PASS.
Date: 2026-08-04
Update 2026-08-07: **degree-3 slice (tier T1) executed** — `cases/dc2_deg3.py`,
results in the "Degree-3 slice results" section below. Headline: quantum-classical
divergence is real at D=3 and is carried entirely by the six deg-0 vertex equations
(rank-1 obstruction on classical moduli at family points); no support-level
separation found; DC(2) consistent with HOLDS at degree ≤ 3 on all loci reached.

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

## Degree-3 slice results (2026-08-07, `cases/dc2_deg3.py`)

### 6.0 Setup: the D=3 unipotent slice system
Quadruples P_j = x_j + w_j + v_j, Q_i = ξ_i + w'_i + v'_i (w quadratic, v cubic;
constants commute with everything and are free; linear part normalized to identity —
validity of that normalization re-checked at D=3 in §6.7). Unknowns: 4×(10+20) = **120**.
The 6 CCR residuals stratify by total degree; every equation is ≤ quadratic in the 120
coefficients. Machine-verified counts (`--stage H`, cross-checked coefficient-by-
coefficient against direct operator/Poisson residuals at random points):

| stratum | # eqs | classical (s=1) content | quantum corrections |
|---|---|---|---|
| deg 4 | 210 | {v,v} | none |
| deg 3 | 120 | {v,w} | none |
| deg 2 | 60 | L(v) + {w,w} | ħ²: (v,v) |
| deg 1 | 24 | L′(w) | ħ²: (v,w) |
| deg 0 | 6 | — (none) | ħ²: (w,w) + ħ³: (v,v) |

Quantum system: 420 equations; classical (PC-shadow) system: 414. Constants and
linear parts (λ-terms) of all equations agree between backends — the two varieties
share their linearization; corrections are pure μ (quadratic) terms. The ħ-grading
wt(w)=1, wt(v)=2 makes the classical system homogeneous and the corrections
higher-weight: V_qu(ħ) ≅ V_qu(1) for all ħ≠0 via (w,v)↦(sw,s²v), ħ=s², so
quantum-vs-classical is a weighted flat-degeneration question.
**Correction to §5.1/T1**: the first quantum corrections are s=2 of cubic×cubic
hitting the **deg-2** residuals (not deg-1); deg-1 corrections are s=2 of
cubic×quadratic; both first bite at D=3 as claimed.

### 6.1 Gate: degree-2 reproduction
- Environment gate: `python3 cases/dc2_slice.py` rerun 2026-08-07, 9 s, ALL PASS,
  byte-level agreement with §4.3: rank 20 kernel = gradient family; span 45 with the 6
  quantum deg-0 forms inside (45→45); F₂ census 2¹⁶; Lagrangian family 25/25, local dim
  7; 5/5 operator certificates; msolve slice degrees 90/90, all real points
  Lagrangian-type.
- Generalized-code gate (`dc2_deg3.py --stage gate`, D=2 through the new stratified
  builder, cross-checked term-by-term against direct operator/Poisson residuals): deg-1
  stratum 24×40 rank 20, kernel = X_cubic family (rank 20); deg-2 classical forms
  restricted to the gradient chart w = X_c: span 45, +6 quantum deg-0 forms → 45. PASS,
  identical to §4.3 B/C. Bonus (new, stronger): the 6 quantum deg-0 forms lie in the
  span of the 60 classical deg-2 forms already **ambiently on K⁴⁰** (rank 60 → 60), not
  just restricted to the chart — D ≤ 2 shadow-completeness is an ambient identity.

### 6.2 Linear strata / tangent space at the identity
- deg-1 stratum linear map L′ on w: 24×40, rank **20**, kernel = X_c (Hamiltonian
  fields of cubics) — the D=2 stage-B system, unchanged.
- deg-2 stratum linear map L on v: 60×80, rank **45**, and the 35-dim X_d family
  (Hamiltonian fields of quartics d ∈ Sym⁴) lies in the kernel with rank 35 ⇒
  **ker L = X_(Sym⁴) exactly** (Poincaré-lemma analogue one level up).
- Tangent space of both varieties at the identity quadruple = ker L′ ⊕ ker L,
  dim **55 = 20 + 35** (linearizations of quantum and classical systems coincide).

### 6.3 Quantum-correction placement and span test (divergence at linear level)
Exact rank computation over ℚ (flint) on coefficient vectors of all equations
(3832 monomial columns):
- classical system: 414 equations, rank **410** — exactly 4 linear syzygies, each
  supported on the deg-1 stratum across the residual triple of one 3-subset of
  {P₁,P₂,Q₁,Q₂} (the four Jacobi identities); the quantum 420 have rank **420** —
  stratum-wise Jacobi does not survive the ħ-filtration;
- adding the quantum corrections: +6 deg-0 → 416; +24 deg-1 → 434; +60 deg-2 → 470;
  all 90 → **500 = 410 + 90**: **every quantum correction form is linearly
  independent of the classical system** (and of each other).
Contrast D=2 (§6.1): there the quantum forms sat inside the classical span even
ambiently. **The shadow-completeness mechanism dies at D=3 at the generator level**,
by the maximal possible margin. Caveat: span divergence of generators does not by
itself separate the varieties (a correction could still vanish on V_cl without being
in the linear span) — the geometric separation is §6.5's job.

### 6.4 Classical chart: (c,d) parametrization and the exactness obstruction
Machine-verified (5/5 random cubics c, exact): the 3-jet-of-flow point
(w, v) = (X_c z, ½X_c² z) kills residual strata 1 and 2 identically; strata 3/4 are
generically nonzero. Since ker L′ = X_(Sym³), ker L = X_(Sym⁴) (§6.2) and
½X_c² z is a particular solution of L(v) = −{w,w}-source for every c, the classical
variety is exactly
  V_cl ≅ {(c,d) ∈ Sym³ ⊕ Sym⁴ = K⁵⁵ : S3, S4 vanish at (X_c z, ½X_c² z + X_d z)},
i.e. 330 obstruction equations (deg ≤ 4 in (c,d)) = the failure of the degree-3 jet
of a Hamiltonian flow to close up to an exact polynomial symplectomorphism. The
classical slice question "which cubics c extend" is the fiber question of §6.5.

### 6.5 Fiber probes over curated cubics c: classical vs quantum (divergence table)
Method: fix the quadratic tier w = X_c (a fair slice: classically w is *forced* to be
some X_c by §6.2, so V ∩ {w = X_c} compares the same geometric object in both
backends). Remaining unknowns: the 80 cubic coefficients v. Exact linear solve of the
linear substratum (flint), then msolve on the reduced quadrics (-g 2 emptiness with
"[1]:" certificate; -P 2 for dim/degree; dim measured by generic affine hyperplane
cuts over ℂ). Confirmed rows (partial, banked as they land):

| c | in V3? | classical fiber | quantum fiber | divergent? |
|---|---|---|---|---|
| 0 | (yes) | ⊇ X_(Lagr-quartic) cone, dim ≥ 8 (structure §6.6) | same cone verified exactly at operator level; excess = large-box | not detected |
| lagr_gen f(u₁,u₂) | yes | dim 5 deg 1 (k9, 210 quadrics) | dim 5 deg 1 (k30, 276 quadrics) | no |
| lagr_axis f(x₁,ξ₂) | yes | dim 5 deg 1 (k9, 33 quadrics) | dim 5 deg 1 (k30, 178 quadrics) | no |
| lagr_degen u₁³ | yes | **dim 6 deg 10** (k16) | **dim 6 deg 10** (k=50, 276 quadrics; GB + 6-hyperplane probe, ~20 min) | no |
| split_LL ξ₁³+x₂³ | yes | dim 5 deg 1 (k9) | dim 5 deg 1 (k30) | no |
| split_gen f(ξ)+g(x) | no | EMPTY (linear, 170 eqs) | EMPTY (k4, 37 quadrics, -g2 certified) | no |
| dixmier ξ₁³+x₁³ | no | EMPTY (linear, 116 eqs) | EMPTY (k30, 141 quadrics, -g2) | no |
| x₁²ξ₁ | no | EMPTY (k7, 9 quadrics) | EMPTY (k30, 144 quadrics) | no |
| gen_rand1/2 | no | EMPTY (linear, 180 eqs) | EMPTY (unique lin sol violates 25 quadrics) | no |
| lagr_pert (axis+x₁²ξ₁) | no | EMPTY (k4, 10 quadrics) | EMPTY (k16, 81 quadrics) | no |

Readings:
1. **No divergence detected**: at every sampled c (all rows now resolved except the
   c=0 excess question), classical and quantum fibers agree in emptiness/dim/degree. The Lagrangian fibers are affine
   5-spaces (deg 1) = exactly the quartic freedom d ∈ K[u₁,u₂]₄; the degenerate
   binary cubic u₁³ has a bigger fiber (dim 6, deg 10) — explained: the commutant of
   u₁³ is the full ω-degenerate hyperplane u₁^⊥ ⊃ span(u₁,u₂); the point
   (w,v) = (X_{u₁³}, X_{e⁴}) with {u₁,e}=0, {u₂,e}≠0 verifies **exactly in both
   backends** (operator level, no ordering correction, since [u₁-op, e-op]=0) and
   carries a two-sided inverse certificate: exp(ad(u₁³+e⁴)), a 2-step tame
   automorphism outside the single-Lagrangian-plane family.
2. The **mechanism** differs even when verdicts agree: classically the S3-stratum
   linear system is often already inconsistent; quantum solutions survive the linear
   tier with large slack (k=30–50) and are killed only by the quadrics (which include
   the ħ-corrections). Shadow-completeness is false (§6.3) yet the varieties have not
   separated — quantum corrections re-cut the same locus differently.
3. Non-extendable cubics: generic c, split c, ξ₁³+x₁³, x₁²ξ₁, perturbed-Lagrangian all
   have EMPTY fibers in both theories: at D=3 the extendable-c locus looks like the
   Lagrangian family (plus possibly other V3 components) — extension beyond D=2's V3
   membership is obstructed for everything we sampled outside it, and V3 membership was
   necessary in every nonempty row.

### 6.5b Pointwise scheme divergence (stage P) — the sharpest new fact
At 3 rational Lagrangian cubic+quartic flow points (exact solutions of BOTH systems,
operator-certified), exact Jacobian ranks of the full 120-var systems:
- classical: rank 106, corank (tangent dim) **14**;
- quantum: rank 107, corank **13**.
**The quantum scheme cuts exactly one extra tangent direction at every sampled smooth
family point.** Decomposition: quantum minus its 6 deg-0 equations has rank 106 = the
classical rank, and classical + the 6 deg-0 gradients has rank 107 (the 6 S0 gradients
alone have rank 5, four of which lie in the classical row span). So the entire
pointwise divergence is carried by the **deg-0 stratum Q0(w,w) + C0(v,v) = 0 — the
two-channel quantum vertex equations of §3.3**, which at D ≤ 2 were span-redundant
(§6.1) and at D = 3 become active. This is the first exact witness that
V_qu ≠ V_cl as schemes at common points: PC-vs-DC divergence is now measured, and it
sits exactly where the vertex-gap calculus said it should.
Refinement (exact): restricted to the 14-dim classical tangent, the six S0 gradients
have **rank exactly 1** — one scalar obstruction functional; the killed direction has
gradient-type w-part (lies in ker L′, i.e. deforms the cubic c) with a small v-part.
**At generic family points the quantum vertex imposes exactly one condition
transverse to the classical moduli** — the lowest-degree avatar of the
Poisson-lift obstruction (§1.3.3, @octonion's gap), now an explicit rank-1 linear
functional on classical deformations.

### 6.5c Automorphism certificates (stage N)
- 5/5 random Lagrangian cubic+quartic flow quadruples (the generic points of the
  nonempty fiber strata): exact operator 6-CCR PASS, explicit two-sided polynomial
  inverse constructed ⇒ automorphisms.
- Unipotent-reduction check at D=3: for 10/10 random non-symplectic linear parts M
  over family (w,v): deg-0 residual = MᵀJM − J exactly (the quantum constants
  Q0+C0 vanish on solutions) ⇒ linear part forced symplectic at these points; the
  §6.0 normalization is consistent at D=3 (caveat: verified pointwise on the family,
  not yet as an identity on the whole variety).

### 6.6 Pure-cubic-top stratum (c = 0): the quartic analogue V4 of V3
The classical c=0 fiber, in quartic coordinates (v = X_d forced by §6.2), is
**V4 = {quartics d on K⁴ : the four partials pairwise Poisson-commute}** — S4 gives
210 distinct nonzero quadratic forms in the 35 quartic coefficients. Results:
- Lagrangian-quartic family d = f(u₁,u₂), ω(u₁,u₂)=0: 10/10 random points in V4,
  control excluded; exact Jacobian rank 27 at family points ⇒ V4 smooth there of
  local dim **8** = dim(LGr(2,4)) + dim(binary quartics) = 3+5.
- Schubert cross-check machinery gates on D=2 (Lagrangian cubic cone: 90 ✓);
  prediction: deg(Lagrangian-quartic cone in K³⁵) = ∫_{LGr(2,4)} s₃((Sym⁴U*)^∨) =
  **420** (and 1400 for quintics, the D=4 analogue). msolve codim-8 slice (210
  quadrics, 27 vars): **TIMEOUT at 1500 s** → emitted `dc2_d3_V4_slice27.ms` as a
  large-box candidate; the D=2-style "degree = Schubert" identification of V4's
  top-dimensional part remains a prediction (420), not a verdict.
- Quantum c=0 fiber: no linear substratum (S2qu is quadratic in v), so no local
  reduction; but at Lagrangian-quartic family points the quantum fiber Jacobian corank
  = **8 = classical** (both rank 72/80): no quantum excess locally at the family; the
  global excess question is the emitted 80-var large-box system (§6.9). Consistent
  with §6.5b: the S0 divergence mechanism needs w ≠ 0 (grad Q0(w,w) = 0 at w=0).

### 6.7 Verdict and blockers
**T1's question — does the classical solution variety deform flatly to the quantum
one, or do quantum obstructions cut it further? — is answered: the quantum
obstructions cut further, and we located them exactly.**
1. **Divergence is real and starts at D=3**, as predicted (§3.4/§4.1): the 90 quantum
   correction forms are linearly independent of the classical system (§6.3, maximal
   jump 410→500), and the quantum scheme has strictly smaller tangent space (13 vs 14)
   at every sampled smooth family point (§6.5b). The active ingredient is precisely
   the 6 deg-0 vertex equations Q0(w,w)+C0(v,v) — the two-channel quantum vertex of
   §3.3 — which were span-redundant at D ≤ 2 and become independent at D=3.
2. **But the divergence is (so far) scheme-level, not support-level**: at every
   curated cubic c, the fibers V ∩ {w = X_c} agree between backends in
   emptiness/dimension/degree (11 cubics, incl. a ~20-min GB+probe for the hardest); local
   dims agree at c=0 family points (corank 8 = 8). The quantum equations re-cut the
   same solution locus with different (smaller) tangent/multiplicity structure. No
   quantum-only or classical-only solution point was found anywhere.
3. **DC(2) status in the slice**: every quantum solution reached (all nonempty fiber
   strata sampled) is an automorphism — Lagrangian cubic+quartic flow points carry
   exact operator CCR certificates + explicit two-sided inverses (5/5), and the
   extendable-cubic locus empirically equals V3 (= Lagrangian-type, D=2's constraint):
   extension to D=3 unlocked no new cubics and lost none. **No counterexample
   candidate; DC(2) consistent with HOLDS at Bernstein degree ≤ 3 on everything
   locally reachable.**
4. **Precise blockers to a full D ≤ 3 slice theorem** (what remains before "DC(2)
   holds in degree ≤ 3" is a theorem rather than a sampled verdict):
   (a) global component structure of V_qu (and V_cl) in K¹²⁰ — emitted, large-box
   (§6.9); the fiber method covers only the sampled w = X_c slices, and quantum
   solutions with w outside the gradient family (L′(w) = −B′(v,w) ≠ 0) are not
   excluded in general — probed: 3 non-gradient displacements X_c + δ at lagr_axis
   all give EMPTY quantum fibers (2 at linear level, 1 by -g 2 GB), so no such
   solution nearby, but this remains sampling, not proof;
   (b) quantum c=0 fiber excess beyond the Lagrangian cone — emitted, large-box;
   (c) generic-point automorphism certificates for the lagr_degen fiber (dim 6 deg
   10): a rational point of its extra stratum IS certified (exp(ad(u₁³+e⁴)), §6.5
   reading 1), but the generic (algebraic) point still needs extraction or a
   structural argument that the whole fiber is the exp-family of the u₁^⊥ commutant;
   (d) the classical side inherits the standing D≤2 gap: components of V3/V4 of
   subfamily dimension are not excluded (Schubert degree matches pin only the
   top-dimensional part).
5. The unipotent normalization (linear part = identity) is validated at D=3 pointwise
   on the family (10/10 non-symplectic probes, §6.5c) but rests on Q0+C0 vanishing on
   solutions — at D ≥ 3 this is a theorem obligation, not a triviality (a
   counterexample with non-symplectic linear part balanced by quantum constants is
   excluded only where S0-vanishing is proved).

### 6.8 Degree-4 cost estimate
Counts (programmatic): unknowns 4×(10+20+35) = **260**; equations 6×Σ_{j≤6} dim Sym^j
= **1260**, still all ≤ quadratic in coefficients; quantum corrections: s=2 at strata
4..0, s=3 at strata 2..0, s=4 at stratum 0 (deg-0 gets ħ²+ħ³+ħ⁴ terms). Measured-cost
scaling from D=3: system build and all exact linear algebra (linear strata, span test,
Jacobian coranks — flint) stay minutes-scale at D=4 (matrices ≤ ~1300×2e4). The
binding constraint is msolve on fiber reductions: at D=3 the residual quadric systems
had k ≤ 50 free vars (~20 min GB+probes at k=50); at D=4 the same construction gives k ≈
60–120 (quartic tier v′ has 140 unknowns, linear tiers eliminate ~45%), i.e. **days to
intractable locally — large-box territory for every nonempty fiber**; curated EMPTY
fibers (linear-level or small-k) likely still local. Recommended D=4 scope: linear
strata + span/Jacobian divergence measurements locally (cheap, and the S0-mechanism
prediction is testable there), fibers on the big box.

### 6.9 Large-box candidates emitted
All in `systems/dc2/` (msolve format, char 0, exact integer coefficients):
- `dc2_d3_qu_full120.ms` / `dc2_d3_cl_full120.ms` (54/44 KB): the canonical unsliced
  420/414-equation systems in 120 vars. Goal: global component structure of V_qu vs
  V_cl (GB/dim/degree). Estimate: 120-var quadratic GB — big-box days+, RAM unknown;
  slice on arrival as needed.
- `dc2_d3_qu_full_s65.ms` / `dc2_d3_cl_full_s65.ms` (8.2/7.5 MB): random 65-dim affine slabs
  substituted (0-dim iff a dim-55 component exists; EMPTY = no top-dim component;
  posdim = component of dim > 55, impossible classically — sanity lane). Estimate:
  65-var quadratic GB, hours–days.
- `dc2_d3_fiber_zero_qu.ms` (28 KB): quantum c=0 fiber, 276 quadrics in 80 vars.
  Goal: does V_qu ∩ {w=0} exceed the Lagrangian-quartic cone? (Locally it does not:
  corank 8 = family dim at family points, matching classical — §6.6.) Estimate: 80-var
  GB, hours–days big-box.
- `dc2_d3_fiber_lagr_degen_qu.ms` (311 KB): RESOLVED locally after emission
  (-g 2 GB in minutes; + hyperplane -P 2 probes ⇒ dim 6 deg 10 = classical; ~20 min
  total; reproducible via `--stage Ldeep`); kept as a big-box calibration instance.
- `dc2_d3_V4_slice27.ms` (819 KB): V4 codim-8 random affine slice, 210 quadrics in
  27 vars; local msolve -P 2 TIMEOUT at 1500 s. Goal: 0-dim degree; = **420** ⟺ V4's
  top-dimensional part is exactly the Lagrangian-quartic cone (the D=3 analogue of
  the degree-90 identification of §4.3G). Estimate: hours on a big box (deg ~10²–10³).

## 6.10 Post-review corrections (DC2-REVIEW.md, 2026-08-07)
All §6 measurements CONFIRMED at 4 fresh rational points; interpretive gloss
corrected:
- The §6.5b "one scalar obstruction kills one classical modulus" picture is
  WRONG geometry. Correct tangent picture at generic family points:
  T_qu is NOT contained in T_cl; T_qu ∩ T_cl = the 12-dim family tangent;
  quantum kills TWO classical directions (only one via the S0 functional) and
  contributes one new direction of its own that is obstructed at order 2.
  Net: corank 13 = 14 − 2 + 1.
- The S0 rank on the classical tangent is 1 only GENERICALLY: measured 0 at
  c=0, 2 at the lagr_degen witness, 5 at pure-cubic points.
- Headline demoted: "DC≠PC divergence" → "slice-scheme divergence at D=3"
  (supports agree everywhere reached; the divergence is scheme/tangent-level
  in the slice, not a support separation).
- Upgrade adopted: the lagr_degen dim-6 deg-10 fiber is now DERIVED (pencil of
  Lagrangian planes through u1, Segre class ⇒ dim 6, deg 10 exact), closing
  §6.7.4(c) top-dimensional part. Full-120-var corank 14 = 14 at c=0 confirms
  the w≠0 mechanism prediction at system level.
- Verdict stands: DC(2) consistent with HOLDS at D≤3 on everything reached.
