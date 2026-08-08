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

PENDING.

## 3. R1 Staged System

### Stage ledger (banked incrementally as each stage completes)

PENDING.

## 4. Verdict Under Pre-Registration

PENDING.

## 5. Next Step

PENDING.
