# SHEET6-R1 — Redesigned R1 Experiment (Coefficient-Level Test of the Two-Pole Template)

Status: FULL-DEGREE TERMINAL CORE BUILT, GUARDED, AND RUN LOCALLY
2026-08-09 (sec 8; supersedes the retracted sec 6): the exact 98-row
minimal-branch G_m core (C1-Gm proven vacuous; 10 constant rows carry
the E5 load; all four review guards PASS) is emitted to
systems/r1/r1_full_core.ms with mod-p / w-free variants and the
(1,2)-sibling core; msolve local: no [1] on any faithful encoding
within 1200 s (char 0 + 2 primes + 2 w-free screens) => NO verdict-
table row triggered; partial clause applies; decision = FARM run of
the banked core. Engine: cases/r1_experiment.py + cases/r1_fullcore.py.
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

## 8. Rebuilt terminal core — build log (2026-08-09, per SHEET6-R1-REVIEW mandates)

Mission: full-degree discriminating G_m core for the minimal branch,
review fixes 1-4 (expanded emission, cancellation-proof sentinels,
[1]-plausibility + round-trip + residual guards, verdict discipline).

### 8.0 Plan (banked before work)

1. Sizing: monomial-count combinatorics for the full-degree G_m window
   (slot budget 20 => var-degree <= 20; no cap needed if counts feasible).
2. Engine fixes: (a) absorbing sentinel (vadd/vscal never cancel
   (HIVAR,) keys); (b) block-refactored G_m jets: f^3 and g^2 built as
   products of per-(orbit,k) block cubes/squares (avoids the quadratic
   jmul(f^2,f) blowup; slot truncation is order-independent since slots
   are nonnegative and additive); (c) new emitter: fully expanded
   integer monomials, no parens, per-row denominator clearing, radical
   relations expanded; (d) guards: paren sweep, independent-parser
   mod-p round-trip vs state rows, constant-term census + explicit
   origin check, random-point residual (identically-zero rows dropped
   and logged), radicals-only msolve sanity run.
3. Full-degree build (VDEG_CAP effectively off) of jfG, jgG, f^3, g^2,
   W_G at depth 54 (dG = 21: band slots 1..19, quotient at 20); numeric
   mod-p validation of the block fast path against the direct
   126/189-factor product at a random point (full-degree analog of the
   deg<=2 gate).
4. F_s band at best feasible cap with sound sentinels (exact rows only,
   lossy census logged); W_R likewise or skipped with log.
5. Emit systems/r1/r1_full_core.ms (char 0, radical gens as vars) +
   char-p radical-specialized screen variant; run guards; msolve local
   (mod-p screen, then char 0, timeout 1200 s); bank outputs to runs/.
6. Verdict strictly under the sec-1 table; sibling-branch emission only
   if the delta-spec is genuinely cheap (review F6), never blocking.

A-priori note (guard 3b anticipated): every band row is prefix-relative
with zero constant term UNLESS the prefix fails a window condition; if
the constant census comes back all-zero, the origin + any radical point
satisfies the core, msolve UNSOLVABLE is impossible for the intended
math, and any [1] is a pipeline error by construction.

### 8.1 Engine fixes DONE (cases/r1_experiment.py)

- Sentinel soundness: (HIVAR,) is now ABSORBING in vadd/vscal (kept at
  RONE, never scaled or summed => cancellation impossible; vmul already
  absorbing). The F2 mechanism (g^2/f^3 sentinel-count cancellation) is
  closed by construction.
- Emission: ring_to_poly (parenthesized) REPLACED by poly_terms /
  emit_expanded — fully expanded monomial sums, integer coefficients
  (per-row denominator clearing), signs inline, no parens; sqrt3 via r3
  variable; RAD_EQS = expanded radical relations incl. A1^3-3-r3,
  A2^3-3+r3, Phi42 as literal string. emit_core / emit_gm_core rewired.
- Selftests PASS. Grammar check: radicals-only file in the new format ->
  msolve -g 2 reduced GB is FAITHFUL and non-[1]: [3W2^2-2HW2^2,
  3W1^2-2HW1^2, r3^2-3, A2^3+r3-3, A1^3-r3-3, 2EB^7-3, Phi42 with
  correct signs] — the F4 parser artifact is gone (review guard 1 PASS).

Sizing (combinatorial, before build): weight<=20 multiset counts:
f-pool 50.8k monomials, g-pool 158.6k (upper bounds; true counts lower
by the 6-grid Delta restriction). Full-degree G_m build is feasible via
per-(orbit,k) BLOCK products (f^3 = product of block cubes, g^2 = of
block squares — never jmul(f^2,f) all-pairs). Strategy: exact blocks
(small), then folds; mod-p specialized fold first (sizing + screen),
exact fold if timing allows. Driver: cases/r1_fullcore.py (next).

### 8.2 Full-degree build driver (cases/r1_fullcore.py)

New driver module reusing the engine (VDEG_CAP=999 — in the G_m window
var-degree <= slot <= 20, so full degree is EXACT, no sentinel can
fire; asserted at build). Per-(orbit,k) blocks: through-d0 factors
exact (one block per A-orbit), Delta suborbit-Newton blocks else —
byte-mirrors gm_jet2's verified math. f^3 = tree-fold of block cubes,
g^2 = of block squares (slot truncation order-independent). Round-trip
primes p = 105337, 105673 (both 1 mod 84; full consistent radical
points found and verified incl. Phi42(z) = 0, A_i^3 = 3 +- r3,
2EB^7 = 3, HW_i = sqrt(3/2)W_i).

- --blocks DONE: 21 f-side + 42 g-side exact blocks, 83 s, 189 vars
  registered (in-window subset will be smaller). No sentinel fired.
- --check (running): mod-p full-degree comparison of the block-fold jet
  against an independently coded DIRECT per-factor 126/189-product at a
  random point, both primes — the full-degree analog of the deg<=2 gate.

### 8.3 Full-degree structure (mod-p fold first; then exact)

Validation: --check PASS — block-fold jet == independently coded DIRECT
per-factor 126/189-product, all (n,s) keys, both primes, both sides.
Sizing (mod-p, full degree): jf 29.3k entries / jg 93.9k / f^3 106.6k /
g^2 203.3k / W_G 297.9k entries over 99 (n,s) keys. Fold time ~1 s
mod-p => exact fold tractable locally.

STRUCTURAL FINDINGS (full degree, mod-p; exact confirmation pending):
1. G_m-jet GRADING: every jet key obeys s == 2n (mod 6) (suborbit
   phase-sum selector: d0-blocks 6 | 32(n7-n_b)+s_b, Delta-blocks
   e-slots on the 6-grid with eta at t^20). Verified on all jf/jg/WG
   keys: 0 violations. Since 2n is even, ODD slots are IDENTICALLY
   ZERO: the C1-Gm fractional family is VACUOUS BY CONJUGACY at full
   degree — same mechanism as the F_s C1 finding (sec 3). The cap-2
   census's "84+54 lossy C1-Gm rows" were PHANTOM sentinel rows (their
   entire content phase-cancels; the conservative cap flagged them).
   Note qpat = eta(e3-a1)^2(e3-a2)^2(eta^3-b) has support n == 1 mod 3
   — exactly the slot-20 lattice 2n == 20 (mod 6). Full consistency.
2. True full-degree G_m row census: 98 rows = WG-band 87 (even slots
   1..19 on the lattice) + WG-quot 5 (n = 1,4,7,10,13; n = 16 cancels
   identically as it must) + WG-quot-deg 6 (n = 19..34 lattice).
3. TEN rows have CONSTANT (var-free ring) terms — all 10 are the
   quotient-family rows at slot 20. The prefix does NOT identically
   satisfy slot-20-proportionality as a ring identity: these rows
   constrain the RADICAL generators (the E5/H_M load, as the review
   predicted). => the system does NOT contain the origin; guard 3b's
   "trivially satisfiable" degeneration does NOT apply; a kill is
   a-priori possible for this core. Screen emitted:
   systems/r1/r1_full_core_modp.ms (98 eqs, 119 vars, 6.5 MB, char p).

### 8.4 XCHECK + screen run + slot-20 diagnosis

- XCHECK PASS: folded f^3 == (jet f)^3, g^2 == (jet g)^2 numerically.
- mod-p SCREEN (radicals SPECIALIZED to a random branch point, x-vars
  only, char p = 105337): msolve -g 2 => GB = [1] in ~1 s
  (runs/r1_full_core_modp.ms.screen.out). INTERPRETATION UNDER GUARD
  DISCIPLINE: this is NOT a verdict — in the screen the w_i were fixed
  at RANDOM GF(p) values, not on the E5 quartic locus; the 10
  constant-bearing quotient rows are precisely w-loaded (E5) content,
  so [1] here is consistent with "random w's are inconsistent with the
  quotient rows", exactly the review's "E5 discriminating load moves to
  the quotient rows". The char-0 core (radicals as VARIABLES) is the
  pre-registered decisive object.
- qcheck (INDEPENDENT direct 126/189-factor product, prefix x=0, both
  primes): (i) band slots 1..19 vanish identically at prefix —
  consistent with the review's float rebuild, now exact-mod-p on two
  primes; (ii) slot-20 prefix is NOT proportional to qpat: mismatch at
  n = 1,4,7,10,13 (lattice n < 16) and n = 19,22,25,28,31 (beyond
  deg qpat = 16, where the template demands 0); (iii) folded-WG
  constant parts == direct-product values with 0 mismatches. So the 10
  constant rows are REAL structural content of the minimal-branch
  genome at slot 20 (w-loaded pattern defect), not a pipeline artifact.

### 8.5 Exact fold + F_s sizing decision

- Exact (char-0 ring) folds running (tree-fold, per-level checkpoints
  /tmp/r1full/x*.ck; ~1.2 GB RSS steady). Exact ring arithmetic is
  ~10^2-10^3 x the mod-p fold cost; projected 1-3 h total. All exact
  objects will be re-validated mod-p against the already-verified
  mod-p folds before emission (structural equality of supports +
  coefficient reduction check).
- F_s band at FULL degree: slot-s W_F rows carry weight-s monomials
  (bf13^s etc.), so full-degree F_s = degree <= 36 objects at depth 54
  (in-window band slots 6..36; the 18->8 quotient at 1/7-slot 10 needs
  depth 84). Combinatorial sizing (N_g(36)-scale, 10^7-10^8 monomials)
  => FARM-scale; NOT built locally. The local deliverable = the G_m
  terminal core (98 rows), which is the banked sec-3 terminal family;
  F_s-band full-degree emission goes to the farm list with this sizing.
- (1,2) sibling branch: emission phase written (--branch12) per the
  SHEET6-R6 4.3 delta-spec — reuses the SAME exact W_G object: band
  slots 1..11, h2-tie rows WG(n,12+r) - s1*F2(n,r) (r = 0..7, s1 fresh
  tie-scale variable, F2 = fold of f-block squares — cheap), slot-20
  quotient vs qpat after s1-subtraction. Lattice consistency checked:
  qpat support n == 1 mod 3 at slot 20; P^4 support n == 0 mod 3 at
  slot 12; both match the s == 2n (mod 6) jet grading. Runs after the
  minimal-branch emission completes; chains (6,17)/(6,23) get a sizing
  note (deeper G_m window + h2^6 jets; not one-pass).

### 8.6 Exact-fold pivot: ring-mod-p CRT path

The direct exact fold (Fraction ring dicts) projects to multiple hours
(level-1 of the f-jet alone ~4 min; f^3/g^2 dominate). PIVOT (exact
fold kept running as gold-standard backup): fold with ring-monomial
keys SYMBOLIC and only the K3 Fraction pairs reduced mod p (rnorm
semantics reimplemented mod p: hw^2->3/2w^2, alpha^3->3+-r3 as (3,+-1)
pairs, eB^7->3/2, Phi42 z-reduction via ZRED mod p) — a few seconds
per prime at 2^29-scale primes. CRT over 7 primes + holdout-prime
structural verification + consistency vs the (direct-product-verified)
scalar fold, then Wang rational reconstruction per coefficient => the
EXACT char-0 W_G. Note: C1-Gm vacuity means the core needs W_G only.

### 8.7 uf30 finding + parallel CRT folds

- uf30 (the 15/21-grid dead-stretch var, Delta-slot 18) is ABSENT from
  every W_G row. Verified NOT a pipeline bug: the direct-product jets
  DO depend on uf30 (keys (n,18)/(n,20)), but in W_G = g^2 - f^3 the
  dependence cancels EXACTLY at random tails (independent direct-path
  test, keys all equal). uf30 is a free direction of the G_m core (it
  must be pinned elsewhere — F_s band / deeper content), consistent
  with the g-side sharing f's dead-stretch arcs (E7).
- 8 ring-mod-p prime folds (2^29-scale) running in parallel (~2.7 GB
  total RSS on 32 GB); per-prime ~4-10 min projected.

### 8.8 Pipeline pre-test + housekeeping

- Emission+guard pipeline pre-tested end-to-end on a surrogate exact
  object (two B-Delta blocks): paren sweep PASS, independent-parser
  round-trip PASS on both fresh primes (105337/105673 — disjoint from
  the 2^29-scale CRT primes), origin + residual scans behave. Pipeline
  is ready for the real W_G.
- Stale cap-2 artifacts renamed r1_gmband_core.{ms,vars.txt}.RETRACTED
  (AUDIT standing rule: retracted emission must not sit in msolve-
  consumable namespace; superseded by r1_full_core*).
- Exact-Fraction foldx killed (superseded by the CRT path with holdout
  + scalar-fold verification); 8 parallel per-prime folds at ~100% CPU
  each on 12 cores; post-fold chain armed (CRT -> emit+guards ->
  w-free screens).

### 8.9 Screen self-guard

Band-only subsystem of the mod-p screen (87 rows, no constant terms —
contains the origin by construction): msolve does NOT return a quick
[1] (240 s, no output) — as REQUIRED (a band-only [1] would have been
a pipeline error under guard 3b). The screen's [1] therefore hinges on
the 10 constant-carrying quotient rows, consistent with the E5-load
reading. (Quotient-only subsystem also does not give a quick [1] at
300 s; the kill needs band+quotient jointly, i.e. genuine structure,
not a single garbage row — unlike the retracted cap-2 artifact whose
[1] came from 3 mangled rows.)

### 8.10 Chain-branch ((2,3)->(6,17), (2,5)->(6,23)) sizing — deferred

Per review F6 the emission machinery transfers, but the chains are NOT
one-pass-cheap: they need (i) h2 = W_G^2 - s1 F3 (W_G^2 is a >= 10^6-
entry object per prime), (ii) the h3 = h2^6 - s2 f^l level-3 G_m band
at depth 195/42 resp. 267/42 with residual P^{24|36}(q^6 - H^6 P^10) —
a G_m window 2-3x deeper than the minimal branch's 21 slots, hence
generator depth >= ~84, an in-window unknown pool ~2x, weight budget
40-60, and monomial counts 10-100x this build. Estimated farm cost:
~2-10 CPU-h per prime x ~8-12 CRT primes per chain with the current
(verified) block+CRT machinery. DEFERRED to the farm with this sizing;
the (1,2) sibling IS emitted locally (8.11) since it reuses this
build's exact W_G and a cheap F2 fold.

### 8.11 Fold performance fix (restart)

First-generation ring-mod-p folds hit the dense-partial bottleneck
(ring dicts fill toward 12 z-keys; final f^3/g^2 products ~10^8
reduction calls => ~1-2 h/prime). Fix: (a) memoized c-independent
raw-key reduction in rmul_p (rnorm chain + Phi42 z-reduction cached
per raw monomial key — hit rate is huge since raw keys repeat), (b)
smallest-first pairing in tree_fold. Folds restarted with the new
code; correctness remains guarded downstream by the CRT holdout-prime
check and the scalar-fold consistency check (both hard asserts in the
armed chain).

### 8.12 Fold shape lesson (banked for the farm/chain builds)

Tree-folding the per-(orbit,k) power-blocks is the WRONG shape for the
ring-mod-p fold: pairing two grown partials multiplies dense x dense
ring dicts (10^8+ entry-pairs x high z-density => 10^10 reductions).
The RIGHT shape is the engine's own seed-chaining: sequential
dense x sparse (partial x one low-density block), which keeps one side
at ring-density ~1-3. Implemented as fold_seq; 12 parallel prime folds
(insurance against the measured coefficient growth |num| ~ 2.7e23 on
4-block partials, den <= 1024: 11 use-primes give reconstruction bound
~1e47) restarted 04:37:51; first 11/21 f-blocks in 8 s.

### 8.13 Pointwise-z representation (final fold path)

Third representation iteration: evaluate the z-dimension at all 12
Phi42 roots mod p (p == 1 mod 42; roots via x^((p-1)/42) sampling, no
scans) — ring coefficients become {tail7: 24-int vectors} with
POINTWISE z-multiplication (no convolution, no ZRED); converted back
to the za-basis by inverse Vandermonde at fold end, so cWG.<p>.pkl
format and the CRT+holdout+scalar verification stack are unchanged.
Entry counts agree with the pair representation at every checkpoint
(19263 @ 11/21, 106592 @ 16/21 and 21/21). f^3 fold: 606.7 s/prime
(vs pair-rep unfinished at 20+ min). 12 primes (new family, == 1 mod
42, ~2^29) running in parallel since 05:01.

### 8.14 First exact-prime fold landed

cWG.536870923.pkl: 297,930 entries — EXACTLY the scalar-fold entry
count (8.3), structural agreement across representations. Per-prime
wall 31.5 min (pointwise-z, 12 parallel). Remaining 11 primes land
within ~10 min; CRT chain armed on the 8th.

### 8.15 Vandermonde orientation bug + repair (fixz)

The first CRT attempt failed en masse: pv_to_zbasis had a TRANSPOSED
Vandermonde (stored (V^-1)^T V c instead of c). Caught by the
holdout-prime verification exactly as designed (guard did its job).
Repair applied in place per prime: c = V^-1 V^T stored (phase_fixz,
self-tested on synthetic vectors per prime; 12/12 repaired). After the
fix the pointwise path passes DIRECT tests against exact engine ring
arithmetic (roundtrip + product MATCH), and mini-CRT verifies
coefficients up to 5.6e34/32 (true magnitudes are enormous — sums over
~10^5 phase-product paths — vindicating the 12-prime insurance;
11-use-prime capacity ~1e47). Full CRT + emit + guards chain running.

### 8.16 Capacity extension

11-use CRT left 4,279 unreconstructed coefficients, ALL concentrated
at slots 18-20 (quotient keys (n,20) dominate) — the deep B-tail
multiplicity content; largest verified coefficient so far 5.6e34/32.
Four additional primes (13-16; dedup bug in crt_primes_v fixed — the
repeat-call cache appended duplicates, silently no-opping the extra
folds) now folding; 15-use capacity ~2e65. Emitter upgraded with
per-row content (gcd) removal so emitted integers stay minimal; the
round-trip guard mirrors the same scaling.

### 8.17 EXACT CORE BUILT + ALL GUARDS PASS (06:07)

- CRT over 15 use-primes + holdout: xWG banked, 297,930 entries/99
  keys; holdout prime 536873947: 0 mismatches; consistent with the
  (direct-product-verified) scalar fold. Reconstruction failures: 0.
- EMITTED systems/r1/r1_full_core.ms — the pre-registered full-degree
  minimal-branch G_m terminal core: 7 expanded radical eqs + 98 rows
  (WG-band 87, WG-quot 5, WG-quot-deg 6), 119 engine vars + 9 radical
  gens, 18.1 MB, integer coefficients, content-normalized, NO parens.
  Also r1_full_core_p{105337,105673}.ms (same system, coefficients mod
  p, radicals still variables) and r1_full_core_wfree_p*.ms (z, r3,
  A1, A2, EB specialized; W1/HW1/W2/HW2 FREE variables).
- GUARDS: (A) paren sweep PASS. (B) round-trip vs an INDEPENDENT
  parser at two fresh primes disjoint from the CRT set: 98/98 match;
  98/98 nonzero at a random point. (C) origin check: 88/98 vanish at
  x=0; the 10 quotient-family constant rows do NOT => the variety does
  NOT contain the origin; a [1] would be a legitimate verdict here,
  NOT auto-spurious. (D) residual: 0 identically-zero rows (none
  dropped). Row labels: r1_full_core.rows.txt.

### 8.18 msolve runs (first results)

- wfree screen p=105337 (W1/HW1/W2/HW2 free, other radicals branch-
  specialized, char p): TIMEOUT 1200 s — NO quick [1]. Contrast: the
  all-specialized screen (w RANDOM) gave [1] in ~1 s. Freeing the w's
  removes the fast contradiction => the cap-level "kill" at random w
  was indeed the E5/w-load of the quotient rows, not a shallow death
  of the branch. The satisfiability question is genuinely deep in the
  w-coupled system.

### 8.19 (1,2) sibling core EMITTED

Exact F2 (f^2 fold) recovered via the same pointwise-z CRT stack
(11 use-primes, holdout 0 mismatches, consistent with a scalar fold at
p=105337): 68,254 entries / 93 keys. (1,2)-branch core emitted per the
SHEET6-R6 4.3 delta-spec: systems/r1/r1_12branch_core.ms — 105 eqs
(7 radical + 98 rows: B12-WG-band 37 [slots 1..11 vanish], B12-h2-tie
50 [WG(n,12+r) = s1*F2(n,r), r = 0..7; r=0 is the printed legality
h1+ = s1(f+)^2; s1 a fresh tie variable], B12-h2-quot 11 [slot-20
proportionality vs qpat after s1-subtraction]), 119+9+1 vars, 22.1 MB,
paren sweep PASS, 10 constant-bearing rows (again the slot-20 family:
the (1,2) core is also NOT origin-satisfiable => genuinely
discriminating). Row labels: r1_12branch_core.rows.txt.

### 8.20 Run ledger (msolve 0.10.1 local, -g 2, timeout 1200 s each)

| system | vars | char | radicals | w's | result |
|---|---|---|---|---|---|
| r1_full_core_modp.ms (screen) | 119 | p | specialized | RANDOM point | [1] in ~1 s (E5-load diagnostic, NOT a verdict — w-point not on quartic locus) |
| band-only subset of screen | 119 | p | specialized | random | no quick [1] at 240 s (origin-satisfiable subsystem behaves correctly) |
| r1_full_core_wfree_p105337.ms | 123 | p | z,r3,A1,A2,EB specialized | FREE | TIMEOUT 1200 s (no [1]) |
| r1_full_core_wfree_p105673.ms | 123 | p | specialized | FREE | TIMEOUT 1200 s (no [1]) |

| r1_full_core_p105337.ms | 128 | p | VARIABLES | free | TIMEOUT 1200 s (no [1]) |
| r1_full_core.ms (PRE-REGISTERED) | 128 | 0 | VARIABLES | free | TIMEOUT 1200 s (no [1], no basis) |

| r1_full_core_p105673.ms | 128 | p | VARIABLES | free | TIMEOUT 1200 s (no [1]) |

(All outputs in runs/r1_full_core*.out.)

### 8.21 VERDICT under the pre-registered table (sec 1)

- "R6 window empty AND R1 staged system UNSOLVABLE => template DIES":
  **NOT TRIGGERED.** The correct full-degree minimal-branch core
  produced NO [1] on any faithful encoding within the 1200 s local
  budget (char 0, two full-p reductions, two w-free branch screens).
  The only [1] observed (all-specialized screen at a RANDOM w-point)
  is excluded from verdict use by guard discipline: the w-point is not
  on the E5 quartic locus, and the failing content is exactly the
  w-loaded quotient family.
- "R1 SOLVABLE => formal candidate deepens": **NOT TRIGGERED.** No GB
  or dimension certificate was obtained within budget; satisfiability
  is NOT established (and is no longer a priori: the 10 constant rows
  exclude the origin).
- => **partial clause applies; the decision now rests on a FARM run of
  the banked, guard-certified core.** What IS established (new, exact,
  guarded): (i) the true full-degree minimal-branch G_m terminal core
  is 98 rows / 119+9 vars (not 368 rows / 109 vars — the C1-Gm family
  is vacuous by the s == 2n (mod 6) jet grading, proven mechanically
  and verified on two independent evaluation paths); (ii) the core is
  NOT origin-satisfiable: the slot-20 quotient family carries 10
  var-free w-loaded constants — the prefix genome VIOLATES exact
  slot-20 proportionality to qpat (mismatch at n = 1,4,7,10,13 and
  19..31, two primes, independent direct product) — the E5 load is now
  EXPLICIT in the emitted system; (iii) a random-w branch point is
  mod-p INCONSISTENT with the core ([1] in 1 s) while w-free encodings
  show no fast contradiction: the w's are genuinely constrained by the
  band+quotient jointly; (iv) uf30 drops out of W_G identically (free
  direction of this core). The kill-or-candidate decision is exactly
  the farm-scale GB of r1_full_core.ms (and its mod-p reductions
  first), plus the F_s-band full-degree extension (farm sizing in 8.5).

Deliverables: systems/r1/r1_full_core.ms (+.rows.txt, char-0
pre-registered core), r1_full_core_p{105337,105673}.ms (mod-p
reductions, radicals as variables), r1_full_core_wfree_p*.ms (w-free
branch screens), r1_full_core_modp.ms (all-specialized diagnostic),
r1_12branch_core.ms (+.rows.txt, (1,2)-sibling core per the 4.3
delta-spec, guard-passed), r1_gmband_core.ms.RETRACTED (quarantined);
engine fixes in cases/r1_experiment.py; builder cases/r1_fullcore.py;
run logs runs/r1_full_core*.out; state /tmp/r1full (16 CRT primes,
exact xWG/xF2 with holdout + scalar-fold verification).

## 9. Chain-branch terminal cores ((2,3)->(6,17), (2,5)->(6,23)) — build log (2026-08-10)

### 9.0 Plan + in-window structure (banked before build)

State loss: /tmp/r1full did NOT survive (host cleaned /tmp since 8.17).
Rebuild via the verified machinery (deterministic seeds => byte-identical
re-emission of the minimal core is the regression gate): --blocks (DONE
13:12, 21+42 blocks / 189 vars — matches 8.2), pointwise-z microtest of
the in-code path (roundtrip + product vs exact engine rmul: PASS => the
post-8.15 REPAIRED Vandermonde orientation is in code), --foldp (DONE:
WG 297,930 entries / 99 keys, census 98 rows / 10 constants — matches
8.3; re-emitted r1_full_core_modp.ms BYTE-IDENTICAL to the banked copy),
--check (PASS: block fold == direct 126/189-factor product, both
primes), 16 per-prime pointwise-z folds (12-way parallel, running),
then --crt, --emit + byte-diff vs runs/r1chain_prebuild_snapshot/.

Chain in-window structure (units: W_G slot = 1/42 of d; slot-s pattern
deg = 36 - s; jet grading s == 2n mod 6 => odd slots vacuous).
Level 1 (h1 = W_G, the SAME exact object as the minimal branch):
- (2,3): d_h1 = 18/42, p_h1 = (-)P^3 (deg 18, NO b-orbit: b relocated
  to level 2 per R6 sec 1.1): band slots 1..17 (live = 6..16 even: the
  exact W_G object has NO keys below slot 6 — slots 1..5 identically
  zero for every branch — and odd slots are vacuous by grading),
  slot-18 quotient == cL*P^3 with cL a fresh lead var (linear-in-cL
  encoding; eliminating cL recovers the cross-mult form), deg rows
  n > 18.
- (2,5): d_h1 = 30/42, p_h1 = (-)P^5: band slots 1..5 ALL identically
  zero (vacuous — the level-1 band contributes no rows; the level-1
  content is the slot-6 quotient family alone): slot-6 quotient
  == cL*P^5, deg rows n > 30.
Level 2 (h2 = h1^2 - s1 f^l1, tie at 2 d_h1 = l1 d_f): W_G^2 slot S
aligns with f^l1 slot r = S - 2(36 - deg p_h1). On the level-1 variety
each needed W_G^2 slot reduces via WG(n, s1st) = p_h1[n]*cL (ideal
membership a-b, c-d in I => ac-bd in I: emitted generators have the
SAME VARIETY as the unreduced ties; msolve decides the variety).
- (2,3): tie r=0 => S_M^3 s1 = cL^2 (f^3 slot-0 = S_M^3 P^6, ASSERTED
  from the F3 fold, not hardcoded); r=1 vacuous (odd); r=2 = QUOTIENT
  (d_h2 = 34/42): R(n) = 2 cL (P^3 conv WG(.,20))[n] - s1 F3(n,2) must
  be == qL*(P^4 q)[n], pattern eta (t-a1)^5 (t-a2)^5 (t-b) deg 34
  monic (q = H eta P (eta^3-b), H absorbed in qL); deg rows n > 34.
  FULL in-window level-2 content captured (window floor = quotient
  slot, exactly as in the minimal branch).
- (2,5): tie r=0 => S_M^5 s1 = cL^2 (f^5 slot-0 = S_M^5 P^10); r=2 tie
  rows 2 cL (P^5 conv WG(.,8))[n] = s1 F5(n,2) (slot pair (6,8) only);
  r = 4..12 ties + the r=14 quotient (d_h2 = 46/42) involve interior
  pairs (8,8),(10,10),(12,12),(8,18),(10,16),(12,14),... = products of
  10^4-10^5-term vexes with NO cL-reduction => 10^8+ monomial rows,
  NOT locally emittable: DEFERRED to the farm per the 8.10 sizing. The
  local (2,5) core = level 1 + r=0 legality + r=2 tie: every row a true
  consequence of the chain genome (necessary-condition core).
Legality/scale data (chain-specific): s1 != 0 (Prop 4.2(iii) tie) via
the Rabinowitsch row t1*s1 - 1 = 0 => cL != 0 => the core does NOT
contain the origin (guard C target). Since the minimal-branch prefix
has WG(.,s)|_{x=0} = 0 for all s <= 19 (8.4 qcheck), a chain solution
must make slot 18 resp. 6 ALIVE with exact P^3/P^5 pattern while the
band stays dead — the discriminating load. Level 3 ((6,17)/(6,23)):
h3 = h2^6 - s2 f^l2 tops at 6 d_h2 = 204/42 resp. 276/42, far outside
the depth-54 window; its 3-coeff W2-collapse (residual q^6 - H^6 P^10,
s2' = H^6, t^19/t^18 conditions == the Prop 8.1(iv) ODE pin
b = (2/3)(a1+a2), a1 a2 = (a1+a2)^2/6 — identically satisfied by the
gauged moduli a_i = 3 +- r3, b = 4) adds NO in-window polynomial rows
on the genome unknowns; the level-3 band goes to the farm with the
ladder data deg p_h3@Gm = 195 = 144+51 resp. 267 = 216+51, mu3 = 103/6
resp. 139/6. Fresh vars per chain core: s1 (tie scale), t1 (its
inverse), cL (level-1 pattern lead), qL ((2,3) only: level-2 quotient
lead). Emission: expanded integer monomial sums only (engine
emit_expanded, AUDIT rule); guards A-D on both cores; w-free mod-p
screens per the minimal-branch naming convention.

### 9.1 Additive engine extension + chain-local objects DONE

cases/r1_fullcore.py additions (nothing above the chain section
touched; regression gate = byte-identical minimal re-emission, 9.2):
chain_patterns (p3/p5/p6/p10, pq34/pq46 via the engine's eta_poly_ref/
k3poly_pow_pattern; SELF-CHECKED: conv identities p3*p3 = p6,
p5*p5 = p10 exact over K3 — this is precisely the algebra behind the
reduced legality row — plus degree/monic asserts and an INDEPENDENT
mod-p evaluation vs the factored form at both round-trip primes:
PASS); phase_chainF (exact truncation-first folds F3 = f^3, F5 = f^5
at dg = 3 — all the in-window chain rows need; slots >= 0 and
additive => truncation-first is exact): F3 = 37 entries, F5 = 61,
slot-1 EMPTY (grading), slot-0 asserted == S_M^l * P^{2l} with the
constant read FROM the fold: S_M^3 = 7^36/2^18, S_M^5 = 7^60/2^30 —
St 3.9(ii)'s S_M = 7^12/2^6 transported through the l-th powers
exactly; chain_rows / emit_chain_core / emit_chain_wfree / phase_chain
(flags --chainF/--chain23/--chain25). Fresh var ids nvars+10..13
(sort last, mirror --branch12's s1 convention).

Key-lattice census (scalar fold pWG, verified): W_G keys live ONLY at
even slots 6..20 with n == 2s mod 3... i.e. s == 2n mod 6 (13/12 keys
per slot, n <= 36); prefix (var-free) content ONLY at slot 20
(n = 1..31) — the 8.4 qcheck facts reproduced. All chain lattices
align: p3 conv WG(.,20), F3(.,2), pq34 all n == 1 mod 3; p5 conv
WG(.,8), F5(.,2) both n == 1 mod 3. Full pipeline DRY-RUN on a
synthetic lattice-correct miniature W_G (throwaway outdir): row
families exactly as designed — C23: band 74 + quot 7 + quot-deg 6 +
h2-quot 12 + h2-quot-deg 6 + s1-tie/inv 2 = 107 rows; C25: quot 11 +
quot-deg 2 + h2-tie 22 + s1-tie/inv 2 = 37 rows (tie rows on synthetic
support; real counts may differ) — guards A-D all PASS mechanics,
origin census = exactly 1 constant row (t1*s1 - 1) per core. Post
dry-run soundness upgrade: qL != 0 also enforced for (2,3)
(C23-qL-inv row t2*qL - 1; deg p_h2@Gm = 34 EXACT is forced tower
data, R6 4.2 B', and q's exact deg-10 shape feeds the level-3 rung)
=> 2 constant rows for the (2,3) core.

COMPLETENESS note (stronger than 9.0 anticipated): the emitted level-2
rows are EXACT genome conditions with NO window truncation. W_G^2
slot-38 a priori sums ordered pairs (s_a, s_b), s_a + s_b = 38, over
ALL slots incl. out-of-window s >= 21; on the emitted variety every
pair except (18,20)/(20,18) dies because one factor is either banded
(rows, slots 6..16), odd (vacuous by grading, incl. all odd s >= 21),
below slot 6 (W_G identically zero there — structural), or slot 0
(E1). Same census closes slot 36 = (18,18) only and, for (2,5),
slot 12 = (6,6), slot 14 = (6,8)/(8,6) only.

## 10. Acceleration: exact linear pre-reduction + multi-prime sweep (2026-08-10)

Engine: cases/r1_reduce.py (ADDITIVE; parses the guard-certified
emitted artifact systems/r1/r1_full_core.ms, not the pickles; all
prior emissions untouched).

### 10.0 Pre-registered interpretation of the multi-prime sweep
(written BEFORE any sweep run)

A char-0 point of the core specializes to a point mod almost all p
(all p not dividing the denominators/leading data of the point's
coordinates). Therefore, for independent random primes p_1..p_k:
- GB = [1] (EMPTY over closure of GF(p)) at MANY independent primes is
  STRONG EVIDENCE for char-0 emptiness (not proof: the exceptional
  prime set of a char-0 point is finite but unknown).
- Nonempty (any GB != [1], or a dimension/degree certificate) at ALL
  primes tried is STRONG EVIDENCE the branch is realizable in char 0
  (not proof: mod-p points need not lift).
- Mixed outcomes: undiagnostic (bad primes exist); report per prime.
Sweep verdicts are BANKED AS EVIDENCE ONLY; the pre-registered sec-1
table triggers ONLY on char-0 certificates. The sweep's purpose is to
calibrate whether the multi-day char-0 ultramem run is worth its wall
clock. Primes: random in [2^15, 2^17], radicals-as-variables encoding
(GB emptiness is over the algebraic closure, so no p == 1 mod 84
constraint is needed for faithfulness).

### 10.1 Linearity analysis of the emitted core (phase analyze/incidence)

- NO row of the 98 is fully linear in the 119 x-vars: every row mixes
  degree-1 terms with higher-degree tails (max x-degree 19). The
  "mostly linear rows" premise is FALSE for this core; the correct
  exact pre-reduction is QUASI-LINEAR VARIABLE elimination.
- 66 of 119 x-vars are quasi-linear (x-degree <= 1 in EVERY row).
- 36 vars have >= 1 clean pivot row (coefficient of the var in that
  row is x-free and W/HW-free, i.e. a candidate UNIT of the etale
  algebra E = Q[r3,z,A1,A2,EB]/(r3^2-3, Phi42, A1^3-3-r3, A2^3-3+r3,
  2EB^7-3); dim_Q E = 1512). W/HW-loaded coefficients are NEVER
  pivots: W_i = 0 lies on the radical locus (2HW_i^2 = 3W_i^2), so
  dividing by them would break the solution-set bijection.
- Soundness scheme (fixed before running): eliminate (v, A) only when
  deg_v(A) = 1 and u = coeff_v(A) is a certified unit (min-poly of u
  over Q has nonzero constant term => invertible, inverse polynomial;
  a_0 = 0 would certify a zero-divisor => pivot rejected). Then
  v = -u^{-1} rest_A is an explicit invertible substitution; solution
  sets biject. Banked in order for the back-map.

### 10.2 Elimination result + guard results (cases/r1_reduce.py eliminate/emitred/guards)

Greedy elimination (cost-capped 3e6, power guard: no substitution into
occurrences of degree > 3): 19 pivots executed, every pivot coefficient
UNIT-CERTIFIED by min-poly (constant term != 0; degrees 1-7). During
substitution 30 rows became IDENTICALLY ZERO (exact rank deficiency of
the quasi-linear structure, verified below) and 46 further x-vars
dropped out of every surviving row (free directions, uf30-style; incl.
x32-x48, x98-x118 blocks -- the P_2/B-side tails are absorbed by the
back-map). Survivors: 49 rows / 54 x-vars, 32,600 terms (vs 98 rows /
119 x-vars, ~420k terms). EMITTED:
- systems/r1/r1_reduced_core.ms (char 0, 56 eqs, 63 vars, 0.9 MB)
- r1_reduced_core_p{105337,105673}.ms (mod p, radicals as variables)
- r1_reduced_core_wfree_p{105337,105673}.ms (z,r3,A1,A2,EB specialized,
  W/HW free, 58 vars)
- r1_reduced_core.rows.txt (provenance: per-pivot bank + row map)
Guards: (A) paren sweep PASS. (B) independent-parser round-trip at 2
fresh primes: 49/49 match, 49/49 nonzero at a random point. (C) origin:
40/49 vanish at x=0; 9 quotient-family rows do NOT => reduced core NOT
origin-satisfiable (discriminating content preserved). (D) residual: 0
identically-zero survivor rows. (E) SOUNDNESS IDENTITY (2 primes x 2
random points, incl. random values for the 46 free vars): all 19 pivot
rows AND all 30 dropped rows vanish under the banked back-map, and all
49 surviving original rows evaluate EQUAL to their reduced forms =>
V(original) bijects with V(reduced) x A^46 (eliminated vars determined
by the recorded invertible substitutions). Satisfiability is preserved
in both directions.
