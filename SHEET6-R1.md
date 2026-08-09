# SHEET6-R1 — Redesigned R1 Experiment (Coefficient-Level Test of the Two-Pole Template)

Status: ENGINE BUILT + PASS-1 RUN COMPLETE 2026-08-09 (gate 15/15; 18
linear stages consistent at depth 54; decisive content = banked
polynomial core, sec 3-4; NO verdict-table row triggered — partial
clause applies). Engine: cases/r1_experiment.py (rerun mechanics in
sec 3.0).
Date: 2026-08-08 (skeleton) / 2026-08-09 (run)

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

Rerun mechanics (checkpointed; state in /tmp/r1_state.pkl): gate =
`python3 r1_experiment.py --stage0` (~15 checks, 10 min). Staged run =
multi-pass with forced-pin substitution between passes; each pass:
`--phase=fs`, `--phase=gm`, `--phase=wf1`, `--phase=wf2`, `--phase=wf3`,
`--phase=solve` (add `--final` on the last pass; `--reset-state` to
start clean; `--depth=N`, default 54). Each phase < 10 min foreground.
Pass k+1 rebuilds jets with pass-k pins inlined (collapses the HIVAR
sentinel rows back into linear rows).

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
Final gate = 15/15: the two production fast paths (fs_jet2: suborbit-
Newton with selector 6[6|12r+s]; gm_jet2: P is C_7-invariant so other-
branch suborbit factors are phase images — per-(orbit,k) Newton) both
match the direct 126/189-factor products exactly on all tracked
(var-degree <= 2) content, with var-degree >= 3 collapsed to a
conservative HIVAR sentinel (affected rows classify nonlinear-deferred,
never linear — kills cannot be manufactured by the cap).
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

Pass-1 ledger (depth 54, VDEG_CAP=1: rows containing any product of two
still-free unknowns defer to the core; 1414 rows, stages m = 18..52):
every stage CONSISTENT. rank 54 / 86 seen unknowns, nullity 32; 0
forced pins; 1136 rows deferred nonlinear; 201 proportionality
split-columns (relaxations, weaken-only); 0 rho-relations; no
certificate. Stage rows: m=18/24/30/36: 163-176 rows each (W_F 6-grid,
~127-140 deferred); m=38..52 even: W_G band 20-22 rows/slot (most
pivots); m=41..51 odd: C1-Gm fractional 41-43 rows (ALL deferred: each
contains u*b-tail products); m=42: +W_R j=1 slice (142 deferred);
m=52: G_m quotient (16/20 deferred).

STRUCTURAL FINDING (pass 1, central): the R1 bands are NOT a staged
LINEAR system over the genome unknowns — every discriminating row is
polynomial (quadratic+) in the 7 dead-stretch + B-side tails, because
band slots aggregate PRODUCTS across branch factors. The spec's
"linear in the O(1) new unknowns per level" holds only against an
already-determined bottom, and the bottom is NOT determined by the
in-window linear residue (nullity stays > 0 at every stage). So R1's
decisive content = a bounded POLYNOMIAL system in the bottom unknowns
(dead-stretch u_18,24,30, v_34,36 x 2, B-tails, co-staged g-bottom,
H_M) — exactly the "terminal nonlinear core" of the pre-registration,
arriving at the BOTTOM of the tower rather than after linear stages.
Sizing: in-window bottom unknowns ~40-70 (B-tails dominate), i.e.
ABOVE the 20-var msolve-easy estimate; the linear stages cannot shrink
it at depth 54.

Terminal core (banked explicit form + sizing, spec item 5 "else"
branch): systems/r1/r1_gmband_core.ms + .vars.txt — the G_m-band
family (C1-Gm fractional slots, W_G band slots 1..19, quotient rows at
slot 20 with H_M eliminated by the lead) over Q with r3^2 = 3,
Phi_42(z) = 0, alpha_i^3 = 3 +- r3, hw_i^2 = (3/2) w_i^2, eta_B^7 =
3/2: **109 engine unknowns + 9 radical generators; 57 rows exact at
tracked degree <= 2; 311 rows require degree >= 3 tracking** (cap-2
build; a full-degree emission needs the per-(orbit,k) sub-checkpointed
build at cap >= 4, ~30-60 min farm CPU). 109 >> 20 vars => local
msolve NOT attempted (per spec guard); the rank-54 linear reduction
can eliminate ~half the variables before a farm run. Independent
cross-check: a subagent reran the final solve on the same state and
reproduced the ledger and 0-pins result verbatim.

## 4. Verdict Under Pre-Registration

Under the section-1 table ONLY:

- "R6 window empty AND R1 staged UNSOLVABLE => template DIES": **NOT
  TRIGGERED.** R6 is closed (window empty), but NO stage of the R1
  linear system is unsolvable: all 18 staged linear systems (1414 rows,
  m = 18..52, depth 54) are CONSISTENT, with no inconsistent row, no
  rho-relation, and no certificate. Every engine relaxation (HIVAR cap,
  proportionality splits, free B-side model) only WEAKENS the system,
  so this "no kill found" is honest but bounded by depth 54 and by the
  deferred-row set.
- "R1 SOLVABLE => formal candidate deepens": **NOT TRIGGERED.** The
  run does NOT establish solvability-at-depth in the pre-registered
  sense, because the staging premise itself fails: the discriminating
  R1 conditions are irreducibly POLYNOMIAL (deg >= 2) in the bottom
  unknowns (7 dead-stretch + B-side + co-staged g-bottom + H_M) and
  defer to the terminal core (1136 of 1414 rows). A solvable linear
  stage is NOT a counterexample (pre-registered), and nullity > 0
  persists at every stage.
- => the **partial/degenerate clause applies.** Established exactly:
  (i) stage-0 gate 15/15 — the engine reproduces the genome lead
  identities (E1/E5/E6/E7, S_M/G_M transports) mechanically over
  Q(sqrt3); (ii) the linear residue of the R1 bands through depth 54
  is consistent (rank 54 / 86 unknowns; ledger sec 3); (iii) R1's
  decisive content at this depth IS the banked terminal core (109
  unknowns + 9 radicals, G_m-band family; 57/368 rows exact at cap 2)
  — the decision (kill or candidate) now rests on that polynomial
  core, not on any further linear stage; (iv) the J(f,g) closure is
  NOT expressible from y-side data alone (needs the x-side / R5-LROOT
  merge) and remains an unfulfilled core member, so no candidate-tier
  claim of any kind is made. The template remains FORMAL-CANDIDATE
  status quo ante; the book of 4 + residue-A configuration are
  UNCHANGED by this run.

## 5. Next Step

1. Full-degree core build: per-(orbit,k) sub-checkpointing at
   unbounded cap (or JC_BACKEND=flint products) to emit ALL 368
   G_m-band rows + the F_s-band rows exactly; substitute the rank-54
   linear relations to eliminate ~half the 109 unknowns; farm msolve
   (mod-p first) on the reduced core. UNSOLVABLE core (with R6 closed)
   = the pre-registered template kill; solvable = near-candidate datum
   gated on the J-closure.
2. Depth 84 (--deep): F_s-band 1/7-slots through 11 (the LT-REVIEW
   predicted kill zone 3..10 fully covered), W_R j = 2, G_m band
   already complete at 54.
3. Merge the LROOT x-side pin to express J(f,g) in the core (R5), the
   one member the y-side window cannot supply.
4. B-side partition audit (42 vs 2x21 etc. for f; 42+21 for g) before
   promoting any future kill certificate that touches B-side unknowns.

## 6. Core verdict (parent session, 2026-08-09)

`systems/r1/r1_gmband_core.ms` (cap-2 G_m-band core: 118 vars incl. 9
radical gens, 64 equations, char 0) run on ultramem-1, msolve -g 2:
**EMPTY — GB = [1]** in ~5 s (runs/r1_gmband_core.out, 759 B, verdict
line present; not a silent death). Since the core is a constraint SUBSET
of the full minimal-branch R1 system, [1] here kills the whole branch —
**the minimal-tower genome is UNSATISFIABLE at coefficient level** —
CONDITIONAL on core-emission faithfulness (under adversarial review; a
spurious over-constraint would fake this). Note the signature: 64
equations in 118 unknowns infeasible = deep structural clash, msolve
found it instantly.

Remaining branches (R6 print-survivors, each needing its own staged
core): (1,2) [delta-spec written], (2,3)-chain (6,17), (2,5)-chain
(6,23). If all four die: the two-pole residue-A configuration is
EXCLUDED and td=6 reduces to the 4 single-pole r9/M2 classes.

## 7. RETRACTION of §6 (per SHEET6-R1-REVIEW.md, 2026-08-09)

The §6 EMPTY verdict is SPURIOUS, on two independent grounds: (a) msolve
0.10.1 silently mis-parses parenthesized input (the shipped file used
parens; 3 mangled band rows alone reproduce [1]); (b) the intended
system was satisfiable a priori (all 57 rows have zero constant term, so
the origin + any radical point solves it — [1] was impossible for the
intended math). Additionally the "57 rows exact at cap 2" claim is
false: all 57 are silent deg<=2 truncations (sentinel counts cancel in
g^2 - f^3); zero discriminating rows were shipped. NOTHING DIED. §4's
partial clause stands; the template remains FORMAL-CANDIDATE. Path
forward (review-mandated): parenthesis-free expanded emission, sentinel
soundness fix, [1]-plausibility guards, then the FULL-DEGREE core build
(machinery reusable across all four branches).
