# SHEET6-R1 — Redesigned R1 Experiment (Coefficient-Level Test of the Two-Pole Template)

Status: PENDING — skeleton banked before any computation (anti-stall discipline).
Date: 2026-08-08

## 0. Spec (per SHEET6-LT-REVIEW.md front 7 R1 GATE: REDESIGN then GO)

Distilled 2026-08-08 (parent session, after 3 subagent stalls; source spans:
LT-REVIEW 277-364, TEMPLATE 57-139 genome, 264-349 residuals+sizing):
- Tower normalization (7b): stage the PRINT-TRUE tower h1 = g^2 - s0 f^3,
  h2 = h1^3 - s1 f^4 (Prop 4.2 T_a^+), OR gauge a = 0; state which in the
  engine. The (f-a) version adds FALSE conditions in band [57,84] at R.
- Order (7c): R6 FIRST. R6 window = m_Gm = 2 with (k1,l1) in {(2,3),(2,5),
  (3,5),(3,7),(3,8),(6,11),(6,13),(6,17)} (changes i_Gm, deg q, the L1c
  layer). If R6 closes: R1 UNSOLVABLE kills the WHOLE residue-A
  configuration; else per-branch labeling.
- Co-stage (7d.1): g sub-top tails are unknowns in the same bands
  (top-coupled by G^2 = s0 S^3).
- x-side lead (7d.2): use LROOT LR2 pin — single x-cluster, kappa_G = 1,
  unsplit below R = 3; A_126 = essentially one scaled factor.
- Discrete choices (7c): ENUMERATE w_i fourth-root + conjugacy-alignment
  branches; never sample one.
- Unknown inventory (TEMPLATE 1b-1c + sizing): scales sigma, A (1
  essential after global scale), c0, w_1, w_2 (pinned to 4th roots by E5),
  7 dead-stretch coefficients (F_s->G_m grid 9/21,12/21,15/21;
  G_m->P_i grid 17/21,18/21), per-level series tails O(3)/level x 50-100
  levels, g-tails co-staged. Constraints: polynomiality of e_j of the 126
  series per (1/42)-level (~168/level) + R1 cancellation depths (R:
  126->56 = 70 kappa-units; F_s: 18->8 quotient = pure power ⊖p21^8;
  G_m: 18/21->8/21 quotient p*q).

Mandated fixes:
- (a) Tower: h1 = g^2 - s0 * f^3 (Prop 4.2 form; gauge a = 0 explicitly). PENDING details.
- (b) Run R6 FIRST (deeper-tower window) so UNSOLVABLE R1 kills the whole template. PENDING details.
- (c) Co-stage g-side unknowns with f; model the x-side lead explicitly. PENDING details.
- (d) Pre-register terminal J-closure BEFORE solving. PENDING details.

## 1. Pre-Registered Interpretation (fixed BEFORE any solve)

- R6 window empty AND R1 staged system UNSOLVABLE => template DIES (two-pole td=6 excluded, theorem-grade).
- R1 SOLVABLE => formal candidate deepens; remaining obligations: R2-R5 ladder (to be listed exactly).
- Partial/degenerate outcome => state precisely what was and was not established.
- A solvable linear stage is NOT a counterexample.

J-closure pre-registration (7d.3): SOLVABLE-at-depth alone proves formal
consistency to depth deg f = 168 (an L2'-tier structure theorem, NOT a
candidate pair). The terminal nonlinear core (expected <= 20 vars; size
must be derived, not assumed) must include the global check
J(f,g) in C^*; only SOLVABLE-with-core-passing = near-counterexample
datum justifying escalation. UNSOLVABLE at any stage (after R6 closes)
= the residue-A two-pole configuration DIES = td=6 exclusion completes
modulo the single-pole book of 4.

## 2. R6 Window Check (run FIRST)

DONE — SHEET6-R6.md status: **CLOSED 2026-08-08, ALL 8 WINDOW CASES DEAD**
(layers 1+2; (2,3),(2,5) die at h2 pole-edge count 2l1 > 2mu2-1; the six
k1 in {3,6} cases die at the merge edge, i_Gm = 6 vs mult 2; premerge
depth-1 escapes closed). Together with the level-0 kills, m_Gm = 2 is
eliminated entirely; m_Gm = 1, (k1,l1) = (3,4) is FORCED. Per the
pre-registration: **R1 is decisive for the whole residue-A configuration.**

## 3. R1 Staged System

### 3.0 Engine formulation (cases/r1_experiment.py; fixed before solving)

Gauges (all declared, print-true tower per 7b): a = 0 (fiber shift);
x-cluster at x0 = 0 (LROOT LR2: A_126 = S_R x^42); S_R = G_R = 1 (f,g
scales) => s0 = 1, tower h1 = g^2 - s0 f^3 EXACT (T_a^+ print-true form);
A = 1 with generator 7th root eta_A = 1 (x-scale + conjugate relabeling);
sigma = 6 (x/y-scale pair normalizes (A, sigma) jointly; det 420 != 0)
=> a1 = 3+sqrt3, a2 = 3-sqrt3, b = 4, b2 = 9/2, B = 3/2. Essential
residual scale = c0 (root direction), which drops out of every
vertex-local jet condition (y-translation covariance) — asserted
mechanically (engine never consumes c0). w_i^4 = k_i alpha_i^2 with
k_i in Q(sqrt3) via E5 (k_i = -(4/3)H_M(a_i-b)/(243 s0 S_M^3 (a1-a2)^4
a_i^3)); s1 derived from the F_s band output (H_F^3 = s1 S_F^4).

Data model: 126 y-series = 3 mu_42-orbit generators (P_1, P_2, B-side),
g co-staged as 3 generators (189 = 63+63+63). Prefix pinned by genome;
unknowns = 7 dead-stretch (grids 9,12,15/21 shared; 17,18/21 per pole)
+ per-level tails + g-tails. Coefficient arithmetic in the finite ring
R_ext = Q(sqrt3)[zeta42, alpha1, alpha2, w1, w2, etaB]/(Phi_42(zeta),
alpha_i^3 = a_i, w_i^4 = k_i alpha_i^2, etaB^7 = B); assembled rows are
asserted MONOMIAL-PURE (then row = Q(sqrt3)-row, verdict uniform over
ALL w-fourth-root/conjugacy-alignment branches = the 7c enumeration,
subsumed as embeddings); mixed rows would be banked as findings and
force per-embedding evaluation (not expected).

Conditions per (1/42)-level m (stages ascend m = 13..M_MAX, default 72):
C1 polynomiality: vertex-jet fractional-slot vanishing (R-jet: e_j
fractional parts; F_s-jet: slots not in (1/7)-lattice; G_m analog).
C2 R1 cancellation bands of h1 = g^2 - f^3: R 126->56 (70 units, j <= 1
at default depth, m = 42), F_s 18->8 with quotient == c * p21^8 (slots
r <= 10 at 1/7 within depth), G_m 18/21->8/21 quotient p*q (full 10-slot
band, m <= 52). C3 pole E5-closure at m = 37 + enumerated-as-embeddings
w-branches. C4 top-coupling G^2 = s0 S^3 (gauged 1 = 1) + g-jet tops.
C5 h2-bands NOT staged (E4/E6 closed them at pattern level; banked).
Stage policy: rows linear in new unknowns; conditions touching >= 2
still-free unknowns nonlinearly => deferred to terminal core. Ledger:
(m, #new, #rows, rank, pinned, nullity, deferred). STOP at first
inconsistent stage (bank small certificate).

### Stage ledger (banked incrementally as each stage completes)

Stage 0 (gate, --stage0): **PASS 13/13** — engine machinery reproduces
the genome lead identities independently: F_s jet slot-0 patterns p21^6
(f, S_F = 1) and p21^9 (g, G_F = 1) from the 21-direction phase product
over K3; E1 top cancellation; E5 z-identity (over R_ext with w free);
E5 automatic m_i^2 = s0 lam_i^3 (= 729 a^4 da^6 (G_M^2 - S_M^3) = 0);
E6 transports G_M^2 = S_M^3, H-ratio; E6 (F_i) both poles over Q(sqrt3);
E5 solvability a_i != b; E7 12 d-drop cells; branch budgets 126/189;
AND the G_m-jet transports MECHANICALLY: the 126- and 189-factor
phase-twisted arc products collapse to S_M (e3-a1)^2(e3-a2)^2 with
S_M = 7^12/2^6 and G_M (e3-a1)^3(e3-a2)^3 with G_M = -7^18/2^9 (sign
included; St 3.9(ii) reproduced), and W_G slot-0 = 0 (E1 transported).
Engine model facts locked at build time: (i) g's branches ride the same
joint-tree arcs => g shares f's 7 dead-stretch unknowns (d_g-ladder
exactness, E7); (ii) B-side modeled as one 42-orbit (f) and 42+21 (g)
per the task's 42-conjugate-orbit spec — larger orbit freedom than any
finer partition, so kills remain genuine (caveat: SOLVABLE would need
partition re-audit); (iii) c0 eliminated by the elementary shift lemma
(e_j of shifted set = triangular integer combos; jets prefix-relative).

Structural finding (engine-derived, banked before the run finishes): in
the exact mu_42-orbit parametrization the C1 polynomiality families are
VACUOUS BY CONJUGACY — e_j of a C_1-stable branch set has slots in 42Z
identically (selector sums), and the F_s jet obeys the grading s = 12n
(mod 42), so no fractional slot ever materializes. This is a FEATURE,
not a gap: the orbit model is the general solution of the polynomiality
conditions (any template-conform branch set is mu_42-stable), so the
spec's "~168 polynomiality conditions/level" are absorbed into the
parametrization, and the DISCRIMINATING staged content is exactly the
R1 cancellation-depth bands (C2: W_F on the 6-grid stages m = 18, 24,
30, 36, 42, 48; W_G dense over m = 33..52 + quotient at 52; W_R at 42)
— i.e. R1's named residual, as pre-registered. G_m-jet families are
NOT graded (fixed direction), hence carry the discriminating load, in
the band LT-REVIEW predicted ("levels 3..10 past F_s").

Stages m >= 13: PENDING (run in flight).

## 4. Verdict Under Pre-Registration

PENDING.

## 5. Next Step

PENDING.
