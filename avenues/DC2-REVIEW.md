# Adversarial review of the DC(2) degree-3 slice (commit 1eb53b0)

Charge: refute the load-bearing claims of DC2-PROGRAM.md §6.0–6.9 and
`cases/dc2_deg3.py`. Verdicts: CONFIRMED (survives attack) / REFUTED /
WEAKENED, per front. Reviewer code written from scratch where independence
is claimed (own Weyl product via operator action on polynomials, own
Poisson bracket, own Jacobian/syzygy linear algebra, own seeds/points);
the repo builder is used only where explicitly noted and only after being
cross-checked against the independent kernel. Scripts: /tmp/revdc2/rev*.py;
logs /tmp/revdc2/*.log. Environment: this machine, python3 + flint +
msolve 0.10.1, 2026-08-07.

## Front 1 — The headline (§6.3/§6.5b): 90 independent corrections;
## corank 13 vs 14; rank-1 obstruction on classical tangent.
## Verdict: measurements CONFIRMED at fresh points; the §6.5b geometric
## gloss ("cuts exactly one extra tangent direction / kills one classical
## modulus") REFUTED as stated; headline interpretation WEAKENED.

First, a reproducibility gap: commit 1eb53b0's `stage_P` computes ONLY the
two coranks. The entire §6.5b decomposition (rank 106/107, S0-rank-5,
4-in-classical-span, rank-1-on-classical-tangent, killed-direction
description) has **no committed code**. Reviewer re-derived all of it
independently (/tmp/revdc2/rev23.py, rev4_tangent.py).

(a) Apples-to-apples: YES. Both systems live on the same K¹²⁰ in identical
coordinates, built by one builder differing only in the bracket backend;
constants and λ-parts agree key-by-key (asserted in H; structurally forced
— Front 3 shows linear×anything brackets carry no correction); both coranks
are Jacobian coranks of each theory's own presented ideal at the *same*
rational points, which are exact solutions of both. Two honest caveats:
(i) corank compares the two PRESENTED schemes — if either ideal is
non-radical the tangent dims say nothing direct about moduli of actual
solutions; (ii) the classical side has no deg-0 equations at all (0=0), so
"quantum has 6 more equations" is inherent, and the doc's rank
decomposition correctly locates the corank drop there: reviewer confirms
rank(qu\S0) = 106 = rank(cl), rank(cl+S0grads) = 107, rank(S0grads) = 5
with dim(spanS0 ∩ spancl) = 4 — every §6.5b number.

(b) Genericity: rank-1 CONFIRMED at 4 fresh reviewer points (own seeds,
own isotropic pairs, varied binary coefficients — the repo's 3 stage-P
points all share ONE coefficient vector [1,-1,2,1]/[2,1,-1,1,3], only the
plane varies; reviewer's points vary everything): corank 13/14 and
S0-on-T_cl rank 1 at all 4. BUT the rank is NOT uniform over the reached
locus, only generic: reviewer measured S0-on-T_cl rank **5** at a
pure-cubic flow point (d=0; coranks 24 qu / 29 cl — divergence 5, not 1),
rank **2** at the lagr_degen witness (X_{u1³}, X_{e⁴}) (coranks 17/19),
rank **0** at pure-quartic c=0 points (coranks 14/14 — equal, confirming
at full-120-var level the §6.6 prediction that the S0 mechanism needs
w ≠ 0; this reachable check was missing from the doc). "At generic family
points" is literally honest but the 0/1/2/5 non-uniformity is unreported.

(c) THE GEOMETRIC GLOSS IS WRONG. §6.5b: "The quantum scheme cuts exactly
one extra tangent direction", "the entire pointwise divergence is carried
by the deg-0 stratum", "one scalar quantum obstruction kills one classical
modulus" (commit message). Reviewer measured, at a generic fresh family
point (rev4_tangent.py):
  rank(J_qu ∪ J_cl) = 108, so dim(T_qu ∩ T_cl) = **12** = the family
  tangent (family tangent independently computed: 16 parameter-derivative
  generators, rank 12, contained in both);
  dim(T_cl ∩ ker S0) = 13, and **T_qu ⊄ T_cl** (2 of 13 quantum tangent
  basis vectors are not classical-tangent; 4 of 14 classical basis vectors
  are not quantum-tangent); rank(qu\S0 rows + cl rows) = 108 ≠ 106.
So the truth is: T_cl = family ⊕ 2 extra classical directions, T_qu =
family ⊕ 1 extra QUANTUM-ONLY direction; the quantum scheme kills BOTH
extra classical directions (one via the S0 functional, the second via the
ħ² strata-1/2 corrections tilting the deg-1/2 rows) and contributes one
new infinitesimal direction of its own that is NOT tangent to V_cl. The
corank arithmetic 13 = 14 − 1 is a numerical coincidence of −2+1, and
"the entire divergence is carried by S0" is false: without S0 the row
spans already differ (106/106 but union 108). The rank-1 functional is
real; the picture "quantum = classical minus one modulus" is not.
Also: "the killed direction has gradient-type w-part (lies in ker L′)" is
vacuous — EVERY classical tangent vector has w-part in ker L′ (the deg-1
classical rows ARE L′; reviewer verified all 14 basis vectors).
Second-order probes (rev4c): the S0-killed classical direction IS
integrable to 2nd order inside V_cl, and so is the second killed classical
direction (the one with S0·t = 0 but J_qu·t ≠ 0, which the S0 story cannot
see) — so BOTH killed directions are classically viable at order 2, and
neither is proven to be a modulus (no actual curve produced). The
quantum-only excess direction is OBSTRUCTED at 2nd order inside V_qu —
embedded/nonreduced fat, consistent with (and mildly supporting) the
"no quantum-only solution point" support-level claim.
Same-point closure (rev4b): at fresh0 the independently-built family
tangent (16 parameter derivatives, isotropy-constrained) has rank 12, is
contained in both tangents, and EQUALS T_qu ∩ T_cl. Summary of the true
local picture at generic family points:
  T_cl = T_fam ⊕ ⟨t₁, t₂⟩ (2 classical-only), T_qu = T_fam ⊕ ⟨t₃⟩
  (1 quantum-only, order-2 obstructed), S0 kills t₁ (rank-1 functional),
  the ħ² strata-1/2 corrections kill t₂ and create t₃.

Also on wording: §6.5b's "at every sampled smooth family point" — these
are smooth points of the FAMILY, but demonstrably NOT smooth points of
V_cl: the family through them has dim 12 while T_cl = 14 (and T_qu = 13),
so unless an unseen ≥13-dim component passes through every sampled point,
both schemes are SINGULAR (or nonreduced) exactly where the divergence is
measured. Tangent-dim comparison at singular points is maximally sensitive
to scheme structure — the right caveat for "kills one classical modulus".

(c′) Truncation-artifact assessment. What the measurement DOES show: the
degree-≤3 unipotent quantum CCR scheme and its Poisson shadow differ as
schemes at common smooth-family points (tangent spaces differ; corank 13
vs 14). This is a real, exactly-measured fact about the D≤3 slice, and
§6.7.2's "scheme-level, not support-level" sentence states its limit
correctly. What it does NOT show: (i) any Poisson solution that fails to
quantize, or any quantum rigidity of an actual classical family — supports
agree everywhere sampled; (ii) anything about DC(2) vs PC(2) as
conjectures: both varieties consist (so far) of automorphism points, and a
classical deformation "killed" inside the D≤3 ansatz could perfectly well
lift to a quantum deformation with degree-4 tails, which the slice cannot
see by construction. The divergence is measured *within a fixed jet
truncation*; calling it "first measured DC≠PC divergence" (commit,
notes.md, §6.5b "PC-vs-DC divergence is now measured") without the
qualifier "at the level of degree-3 slice schemes" overstates. It is
exactly the object §3.4 said to probe — but §3.4's own criterion for a
meaningful exclusion ("must use the correction terms" on a
*Poisson-consistent configuration that then dies*) has not been met by a
tangent-space count at points where both theories agree. The doc's §6.7.1
phrasing ("the quantum obstructions cut further, and we located them
exactly") survives only in the corank sense, not the located-tangent
sense, per (c).

## Front 2 — Syzygy counts (414 cl / rank 410, exactly 4 Jacobi syzygies;
## 420 qu / rank 420). Verdict: CONFIRMED (and mechanism derived)

Independent recount (/tmp/revdc2/rev23.py: own row vectorization over the
3832 coefficient columns, own left-kernel computation; builder first
re-cross-checked against direct residuals at 2 fresh reviewer points):
- counts: qu {0:6, 1:24, 2:60, 3:120, 4:210} = 420, cl = 414 (no deg-0). ✓
- rank(cl) = **410**, rank(qu) = **420** (no quantum syzygies). ✓
- Localization is forced, not just observed: rank(cl minus its 24 deg-1
  rows) = 390 = full, and the deg-1 rows are the *only* classical rows
  touching the w-λ columns, so every syzygy is supported on the deg-1
  block. Its left kernel has dim 4; for each 3-subset of {P1,P2,Q1,Q2} the
  12 rows of its residual triple ({4,0,1},{4,2,3},{0,2,5},{1,3,5}) carry a
  within-triple kernel of dim exactly 1, and the 4 vectors span. ✓
- WHY they are Jacobi: reviewer built the predicted syzygy from scratch —
  the deg-0 component of the linearized Jacobi identity Σ_cyc [A_a,[A_b,A_c]]
  = 0, i.e. λ_{(bc,m)} = ±{g_a, z^m} — and it kills the classical deg-1
  rows identically, 4/4 triples. ✓ (derivation, not label-matching)
- WHY quantum has none: the same 4 combinations applied to the *quantum*
  deg-1 equations cancel in the λ-parts (linearizations agree, Front 3)
  but leave a NONZERO μ-residue from the ħ²(v,w) corrections, 4/4. The
  quantum Jacobi identity still holds, but its compensating terms
  [w_a+v_a, R_bc] are unknown-dependent (the ħ-filtration mixes strata),
  so they are not constant-coefficient row relations. Measured: rank 420.
- Span sequence: per-stratum 410+6=416, 410+24=434, 410+60=470 (matches
  §6.3's per-stratum reading); reviewer's cumulative 416→440→500 and
  rank(qu+cl)=500 confirm **all 90 corrections mutually independent** of
  the classical span and of each other — the §6.3 headline number stands.

## Front 3 — Correction-degree bookkeeping (ħ² (v,v)→2, (v,w)→1,
## (w,w)+ħ³(v,v)→0; §5.1 slip). Verdict: CONFIRMED

Independent kernel first (/tmp/revdc2/rev1_weyl.py): the repo product `wmul`
was checked against a from-scratch operator-action model (x_i = mult,
∂_i = differentiation on K[x1,x2], composition of actions, no shared code
path): 30 random deg-≤4 pairs, all monomial inputs up to x^8y^8 — ALL MATCH.
`pbr` matches an independently written Poisson bracket (50 random pairs;
{ξ1,x1} = +1 convention consistent with [∂1,x1] = 1).

Bookkeeping, checked on **every** basis pair (not one per claim):
- (w,w) = quad×quad, all 100 pairs: wbr−pbr supported in degree {0} only;
  witness [x1²,∂1²] − {x1²,ξ1²} = −2 (ħ²→deg-0). ✓
- (v,w) = cubic×quad, all 200 pairs: correction degrees ⊆ {1}; realized
  (witness [x1∂1², x1²∂1] has corr 2·x1∂1). ✓ ħ²→deg-1.
- (v,v) = cubic×cubic, all 400 pairs: correction degrees ⊆ {0,2}, both
  realized; witness [x1³,∂1³] − {·,·} = −18x1∂1 − 6 (ħ²→deg-2 AND
  ħ³→deg-0 in one pair). ✓
- (linear, anything): wbr == pbr exactly on all 4×30 generator×basis pairs
  ⟹ the two systems' linearizations (λ-parts) must agree — the §6.0
  "linearizations identical" assertion is structural, not accidental.
The §5.1 slip is real and the §6.0 correction is right: cubic×cubic s=2
lands at 3+3−4 = deg 2 (not deg 1); deg-1 corrections are cubic×quad.
Stratum law deg A + deg B − 2s verified in every observed case.

## Front 4 — Gate honesty (D=2 re-derivation; ambient K⁴⁰
## shadow-completeness power). Verdict: CONFIRMED (see caveats)

- Read the code: `stage_gate` **re-derives**, it does not compare stored
  values. It rebuilds the D=2 system through the new stratified builder
  (`build_system(2,·)`, both backends), cross-checks every equation
  coefficient-by-coefficient against direct operator/Poisson residuals at 3
  random integer points *including a completeness direction* (every monomial
  of every direct residual must be a key of the built system), then
  recomputes rank 20 / kernel=X_cubic rank 20 / chart span 45→45 from
  scratch and asserts them against the §4.3 constants. Reviewer rerun:
  PASS, 0.2 s (the "~11 s" folklore figure is stale — gate alone is 0.2 s).
- `dc2_slice.py` itself rerun by reviewer 2026-08-07: 8 s, ALL PASS, every
  §4.3 number reproduced (rank 20; span 45→45; 2¹⁶ F₂ census; 25/25 family,
  local dim 7; 5/5 operator certificates; msolve slice degrees 90/90 with
  10/10 + 14/14 real points Lagrangian-type). §6.1 bullet 1 is accurate.
- Ambient claim on K⁴⁰: reviewer rerun confirms 60 classical deg-2 forms
  have rank **60** ambiently and stay 60 after adding the 6 quantum deg-0
  forms. Power analysis: the 6 forms are provably nonzero (empty equations
  are dropped by the builder and `len(qu0)==6` is asserted), and the
  vectorization (upper-triangular μ-keys) is identical for both row sets,
  so a failure would print "ambient jump" with rank up to 66 and fail
  nothing silently — the check can distinguish. Note the ambient statement
  is strictly stronger than what §4.3C needs (chart-restricted 45→45);
  failure of the ambient version would NOT have broken D≤2
  shadow-completeness on V₃, so its role is bonus evidence, honestly
  labeled "Bonus (new, stronger)".
- Caveat: the gate exercises the builder only at D=2, where quantum
  corrections live solely in (w,w)→deg-0. The D=3-specific correction
  channels (v,v) and (v,w) are gated by stage H's own crosscheck (2 random
  points, both backends, per-coefficient + completeness) — reviewer
  re-verified with fresh points, see Front 1/2.

## Front 5 — Support/fiber claims (11 fibers agree; lagr_degen dim-6
## deg-10 explanation; inverse certificates). Verdict: CONFIRMED
## (and the lagr_degen story upgraded from mechanism to derivation)

- Reruns (/tmp/revdc2/rev5a.log; msolve selftest included in stage L): all
  reproduced against the §6.5 table, byte-level on the diagnostics:
  split_gen EMPTY/EMPTY (cl linear 170 inconsistent; qu k4, 37 quadrics),
  dixmier EMPTY/EMPTY (cl 116; qu k30, 141), x1sq_xi1 EMPTY/EMPTY (k7/9;
  k30/144), lagr_axis NONEMPTY dim 5 deg 1 BOTH (k9/33; k30/178),
  lagr_degen CLASSICAL dim 6 deg 10 (k16, 210 quadrics). The V3-membership
  flags of all 11 curated cubics match the table's "in V3?" column
  (recomputed via direct residuals). The ~20-min quantum lagr_degen deep
  probe (`Ldeep`) was NOT rerun (timebox); its classical twin and the
  witness point were checked instead, see below.
- lagr_degen "u₁^⊥-commutant" explanation: as committed it is a mechanism
  story with one certified witness, and §6.7.4(c) admits the structural
  derivation is missing. The reviewer DERIVED the numbers: quartics q with
  {u₁³, q} = 0 ⟺ {u₁, q} = 0; the isotropic 2-planes inside u₁^⊥ are
  exactly the Lagrangian planes through u₁ (ω|_{u₁^⊥} has radical ⟨u₁⟩),
  a pencil P¹ = P(u₁^⊥/u₁); each member W contributes the exp-certifiable
  family h = u₁³ + f, f ∈ Sym⁴W (ops commute, ad² = 0). Predicted cone:
  dim = 1 + 5 = **6** ✓; degree = ∫_{P(Sym⁴U*)} ξ⁵ = s₁((Sym⁴U*)^∨) over
  P¹ with U* = O ⊕ O(1): Chern roots {0,h,2h,3h,4h}, c₁ = 10h ⟹ deg
  **10** ✓ — same Segre convention that msolve-validated 90 at D=2.
  Both numbers match both backends' measurements, so the measured deg-10
  top-dimensional part of the fiber IS the pencil family (degree pins it),
  and its generic point is exp(ad(u₁³ + f(u₁,e))) — a certified
  automorphism family. **Blocker §6.7.4(c) can be closed** (top-dim part;
  the standing lower-dim caveat (d) remains). Witness re-verified with a
  reviewer-chosen e ([2,-2,-3,-1], ω(u₁,e)=0, ω(u₂,e)≠0): exact solution
  of BOTH backends (rev23 lagr_degen row).
- Caveat kept: fiber dim measurement uses random small-coefficient
  hyperplane cuts (non-generic planes could in principle mis-measure);
  both backends share the method, and the independent 6/10 prediction
  now corroborates it at the one fiber where it was load-bearing.
- Certificates: stage N reproduced (5/5 flow quadruples CCR + two-sided
  inverse; 10/10 non-symplectic probes give deg-0 residual = MᵀJM − J).
  The repo's `try_invert` check is sound by construction (final equality
  tests are exact and truncation-free). Independently, the reviewer
  verified one two-sided inverse BY MULTIPLICATION in the from-scratch
  operator-action model (no `wmul` anywhere): ψ = exp(−ad h) satisfies
  ψ∘φ = φ∘ψ = id on all four generators, actions compared on all 121
  monomials up to x¹⁰y¹⁰ (determines operators of the relevant ∂-order):
  PASS (/tmp/revdc2/rev5c.log). Stage M's cheap parts also reproduce (V4:
  210 quadrics, 10/10 family, rank 27 ⟹ local dim 8; Schubert 90/420
  with the 90 gate matching D=2's msolve value).

## Front 6 — Verdict wording ("consistent with HOLDS at D≤3 everywhere
## reached"). Verdict: CONFIRMED with listed gaps (delimitation honest;
## two reachable-but-unchecked items found, both now checked and benign)

§6.7.4(a)-(d) + §6.7.5 delimit the unreached region accurately: global
component structure emitted-not-run (a,b); non-gradient-w quantum
solutions excluded only by 3 sampled displacements at ONE cubic
(lagr_axis) — correctly called "sampling, not proof"; lagr_degen generic
point (c — now closable, Front 5); D≤2 subfamily-dim components (d);
unipotent normalization pointwise-only at D=3 (§6.7.5 — genuinely
important, since the S0 equations are exactly where the divergence lives,
and their vanishing is what kills non-symplectic linear parts). The V4
degree-420 identification is honestly labeled prediction, not verdict.

Reachable-but-unchecked items the doc missed, now checked by reviewer:
1. Full-120-var coranks at pure-quartic (c=0) family points: **14 = 14**,
   S0-on-T_cl rank 0 — confirms the §6.6 "S0 needs w≠0" mechanism at full
   system level (doc only had the 80-var fiber Jacobian).
2. Coranks at reached degenerate points: pure-cubic (d=0) 24 qu / 29 cl
   with S0-rank 5; lagr_degen witness 17/19 with S0-rank 2. Divergence is
   NOT uniformly rank-1 over the reached locus — "at generic family
   points" is doing unstated work; the doc reports no divergence numbers
   at any non-generic point it itself certifies.
3. dim(T_qu ∩ T_cl) was computable in seconds and overturns §6.5b's
   geometric reading (Front 1) — the sharpest reachable omission.
Remaining honestly-open sampling gaps (unchanged by this review): fibers
only over 11 curated cubics; stage-P family points all share one
coefficient shape (reviewer added 4 varied ones); s65 slabs and 120-var
systems unrun. With Front 1's rewording, "consistent with HOLDS at D≤3 on
everything locally reached" is accurate: every quantum point reached is a
certified automorphism, and no support-level separation was found
anywhere, including by this review's fresh probes.

## Overall verdict

**Every number in the commit that the reviewer could recompute,
reproduced** — system counts, the 410/420/500 rank story with per-stratum
sequence, the four syzygies (localized, per-triple, and DERIVED as the
deg-0 components of the linearized Jacobi identities, with the quantum
μ-residue exhibited as the reason quantum has none), coranks 13/14 robust
at 4 fresh reviewer points with varied coefficients, the §6.5b rank
decomposition, the fiber table, the gate, the D=2 baseline. The Weyl
kernel itself survived a from-scratch operator-action verification. No
computation was refuted.

**What is refuted is §6.5b's geometric reading of its own numbers.** At
generic family points the truth is: T_qu ∩ T_cl = the 12-dim family
tangent; the classical scheme has TWO excess tangent directions, of which
the S0 vertex functional kills one and the ħ² strata-1/2 corrections kill
the other (invisible to the S0 story: rank(qu\S0 + cl) = 108 ≠ 106); the
quantum scheme carries ONE excess direction of its own, not tangent to
V_cl and order-2 obstructed. Corank 13 = 14 − 1 is the net of −2 + 1, not
a single scalar cut; T_qu ⊄ T_cl. The measurement points are singular
points of V_cl (tangent 14 > family 12), and no killed direction is a
proven modulus. "The quantum scheme cuts exactly one extra tangent
direction", "the entire pointwise divergence is carried by the deg-0
stratum", and the commit's "one scalar quantum obstruction kills one
classical modulus" all need rewriting; "first measured DC≠PC divergence"
should say "first measured divergence of the D≤3 slice schemes
(tangent/multiplicity level; supports agree everywhere sampled)".
Reproducibility note: the §6.5b decomposition has no committed code
(stage_P computes only the two coranks); reviewer scripts fill the gap.

**Single weakest claim:** §6.5b's rank-1/one-modulus sentence — right
functional, wrong geometry, and its rank is 1 only generically (measured
0 at c=0, 2 at the lagr_degen witness, 5 at pure-cubic points).

**Upgrades found:** (1) the lagr_degen dim-6 deg-10 fiber is now DERIVED
(pencil of Lagrangian planes through u₁; Segre class gives dim 6, deg 10
exactly), closing blocker §6.7.4(c) for the top-dimensional part with
exp-certified generic points; (2) full-120-var corank equality 14 = 14 at
c=0 confirms the doc's own w≠0 mechanism prediction at system level.

**Recommendation:** keep "DC(2) consistent with HOLDS at D≤3 on
everything reached" (promotes cleanly once §6.5b is reworded); demote the
divergence headline from "DC≠PC divergence" to "slice-scheme divergence";
commit the decomposition + tangent-intersection code; add the −2/+1
tangent picture and the S0-rank non-uniformity (0/1/2/5) to §6.5b; adopt
the pencil derivation into §6.5/§6.7.
