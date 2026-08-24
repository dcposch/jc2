# SHEET6-R1 — Redesigned R1 Experiment (Coefficient-Level Test of the Two-Pole Template)

> **SUPERSEDING EVIDENCE ERRATUM (2026-08-23).** Every msolve 0.10.1
> characteristic-zero `-g` output cited below as `GB=[1]` printed the basis at
> the first machine prime; it is not a rational Gröbner basis or cofactor
> certificate.  Accordingly the ZU/UZ leaf upgrades (§§15.3, 15.7), Q0
> family/control upgrade (§18.1), and Q2 l13 upgrade (§19.2) are
> modular/trace-grade, not proof-tier over Qbar.  The old `(1,2)` kill (§18.2)
> was already retracted for an independent level-slip.  Exact point and
> identity certificates, finite-field verdicts, and the exact Direction-B
> zero-tail theorem are unaffected.  The l13 characteristic-zero stratum and
> all Q-level downstream uses of it are open pending an exact rational
> certificate.

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

Fold incident (14:13): the first 12-way fold launch was killed by the
task harness ~1 h in (workers at g2 36/42) with per-prime results
unsaved. Fix: per-STAGE checkpoints added inside phase_foldv (vf3/vg2
pickles, load-if-present — numeric path unchanged) and the 16-worker
driver relaunched DETACHED (nohup, /tmp/r1full/run_folds.sh) so a
harness kill cannot reap the workers; restart 14:14.

### 9.4 Farm handoff — deferred chain content (sizing, refines 8.10)

(2,5) level-2 band slots 16..26 (ties r = 4..12 even + quotient r = 14
vs pq46 = eta (t-a1)^7 (t-a2)^7 (t-b)): interior W_G^2 pairs with
per-slot expanded-term counts (467/1.5k/3.4k/10.8k/26.3k/54.7k/134.1k/
~164k at slots 6/8/10/12/14/16/18/20) give ordered-pair costs:
r=4 (8,8) 2.2e6; r=6 2(8,10) 1.0e7; r=8 2(8,12)+(10,10) 4.3e7;
r=10 2(8,14)+2(10,12) 1.5e8; r=12 2(8,16)+2(10,14)+(12,12) 4.6e8;
r=14 2(8,18)+2(10,16)+2(12,14) 1.3e9 — total ~2.0e9 term-pairs, i.e.
a few CPU-h per prime pointwise-z + ~16-32 CRT primes (coefficient
squares ~1e130 => ~2x the prime family; capacity per prime ~8.7
digits) — squarely the 8.10 farm estimate. All slot-6 factors reduce
via cL (only pairs with both slots >= 8 are genuinely quadratic).
Level 3 (both chains): h3 = h2^6 - s2 f^l2 band at deg 195/42 resp.
267/42 needs generator depth >= 84 and the h2 object to ~30+ slots:
the 8.10 "10-100x this build" sizing stands; the collapse DATA
(s2' = H^6, residual q^6 - H^6 P^10, ODE-pinned b, a1a2) is already
engine-verified scalar-side (R6 4.1-4.2) and imposes no local rows.

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

### 10.3 Run ledger, reduced core (msolve 0.10.1, -g 2, timeout 1200 s)

Fixed suite (mirrors the 8.20 protocol, reduced encodings):
| system | vars | char | result |
|---|---|---|---|
| r1_reduced_core.ms (char 0, radicals as vars) | 63 | 0 | TIMEOUT 1200 s |
| r1_reduced_core_p105337.ms | 63 | p | TIMEOUT 1200 s |
| r1_reduced_core_p105673.ms | 63 | p | TIMEOUT 1200 s |
| r1_reduced_core_wfree_p105337.ms | 58 | p | TIMEOUT 1200 s |
| r1_reduced_core_wfree_p105673.ms | 58 | p | TIMEOUT 1200 s |

Multi-prime sweep (10 random primes in [2^15, 2^17], seed 61,
radicals-as-variables encoding, per the 10.0 pre-registration):
| p | result | | p | result |
|---|---|---|---|---|
| 40427 | TIMEOUT 1200 s | | 77377 | TIMEOUT 1200 s |
| 49531 | TIMEOUT 1200 s | | 89591 | TIMEOUT 1200 s |
| 56453 | TIMEOUT 1200 s | | 114691 | TIMEOUT 1200 s |
| 71011 | TIMEOUT 1200 s | | 115079 | TIMEOUT 1200 s |
| 76631 | TIMEOUT 1200 s | | 129529 | TIMEOUT 1200 s |

Under the 10.0 pre-registration: NO per-prime verdict (neither EMPTY
nor NONEMPTY was certified anywhere); the sweep's calibration signal is
the DIFFICULTY itself -- even after exact halving (49 rows/63 vars,
32.6k terms) the mod-p GB does not finish in 1200 s at any of 12
primes tried in either encoding. All runs in runs/r1_reduced_*.out,
runs/r1_reduced_sweep.log. Extended-budget probes next (10.4).

### 10.4 Depth calibration + elimination frontier completeness

- FRONTIER COMPLETE: after the 19 pivots, a full rescan of the reduced
  system finds ZERO further admissible pivots (every remaining var
  either occurs at x-degree >= 2 somewhere, or all its linear
  occurrences carry x- or W-loaded coefficients, which are not units).
  The exact linear pre-reduction is maximal for the sound pivot class.
- F4 shape probe (msolve -v 2, p = 40427, radicals-as-vars, 300 s):
  basis passes 16k+ elements mid-flight, elimination matrices reach
  3.7M x 18.4M at step degree 8 with the run still expanding => the
  mod-p GB is genuinely deep; no near-verdict was cut off by the
  1200 s budget line. (/tmp/r1red/v2probe.log)
- Extended probes launched (3900 s, -t 4): p in {40427, 56453, 76631}
  radicals-as-vars + the wfree p=105337 encoding; results in 10.5.

### 10.5 Extended-budget probes (3900 s, -t 4)

| system | p | encoding | result |
|---|---|---|---|
| r1_reduced_core_p40427 | 40427 | radicals as vars | TIMEOUT 3900 s |
| r1_reduced_core_p56453 | 56453 | radicals as vars | TIMEOUT 3900 s |
| r1_reduced_core_p76631 | 76631 | radicals as vars | TIMEOUT 3900 s |
| r1_reduced_core_wfree_p105337 | 105337 | wfree branch | TIMEOUT 3900 s |

(runs/r1_reduced_sweepx_p*.{out,log}, runs/r1_reduced_wfreex_*.)

### 10.6 Verdict under pre-registration + recommendation

VERDICT (sec-1 table): NOT TRIGGERED, either clause -- no [1]/[-1] and
no basis/dimension certificate on any faithful encoding within budget
(char 0: 1200 s; mod p: 12 primes x 1200 s + 4 probes x 3900 s). The
sweep's pre-registered EMPTY/NONEMPTY calibration produced NO per-prime
verdict; no inflation. The mandated 2-solution back-map spot-check is
VACUOUS (no solver returned points); soundness rests on guard E's exact
identity certification (4 point/prime combos, all pivot+dropped rows
vanish under back-map, survivors match).

RECOMMENDATION on the ultramem char-0 run:
1. RETARGET, do not keep as-is: r1_reduced_core.ms is verdict-
   equivalent to r1_full_core.ms (certified bijection x A^46) at 63 vs
   128 vars, 56 vs 105 eqs, 0.9 vs 18.1 MB, 32.6k vs ~420k terms.
   Every F4 step operates in half the variables; days already sunk in
   the 128-var ring are strictly dominated. Restart on the reduced
   core (same pre-registered object, same sec-1 table).
2. CALIBRATE BEFORE BURNING WALL CLOCK: bank ONE mod-p verdict first
   (farm, reduced core, a few primes, multi-hour budgets). EMPTY at
   several primes => char-0 kill plausible, the long run is justified;
   NONEMPTY at the first prime => the branch is likely realizable,
   char-0 GB-emptiness is the wrong spend, pivot to the R2-R5 ladder /
   J-closure obligations instead.
3. The F4 shape (16k+ basis, 10^7-col matrices at degree 8, mod p,
   REDUCED core) says this GB is deep at any characteristic; if 2.
   also stalls, the next accelerator is structural (W case split
   W_i = 0 vs W_i unit -- which unlocks the W-loaded quasi-linear
   pivots barred here -- or slot-band staging), not more budget.

Engine: cases/r1_reduce.py (phases analyze/incidence/selftest/
eliminate/emitred/guards/msolve/sweep/sweep1/sweepw1); all additions
additive; prior emissions byte-identical (git: only SHEET6-R1.md +
new files). State: /tmp/r1red (reduced.pkl = rows+banked
substitutions+dropped list; sweep/*.ms regenerable via sweep1).

## 11. Chain-core first verdicts (parent session, 2026-08-10)

Fold/CRT pipeline completed; BYTE-IDENTICAL gate passed (re-emission
reproduces r1_full_core.ms exactly); both chain cores accepted (guards
A-D PASS each).

**(2,5)-chain core: NONEMPTY at p=105337 AND at char 0** (local msolve,
minutes; runs/r1/r1_25chain_core.out = reduced GB, 487 elements, char 0,
12.4 MB — a substantive variety, and guard C shows the origin does NOT
satisfy the system, so this is not vacuous). Pre-registered reading:
the branch's formal candidate DEEPENS. Scope: the core carries 25/37
banked rows (12 deferred to deg >= 3), so this is "not killed by the
subset", not consistency; remaining obligations = deferred rows, higher
ladder, J-closure.

(2,3)-chain core (110 eqs, 9.7 MB): queued on ultramem behind the
reduced minimal-branch queue (follow-on runner).

## 12. (2,5) EXTENDED core: deferred rungs r <= 10 (2026-08-10)

### 12.0 Plan + pre-registration (banked before build)

Decision target (SHEET6-R1-25LOCUS SS6.3, pre-registered): core (all 44
eqs of r1_25chain_core.ms) + the SYMBOLIC deferred tie rows for rungs
r = 4..10 (W_G^2 slots S = 16..22; r = S-12). If msolve returns [1]
(char 0 OR 2 good primes with coefficients REDUCED into [0,p)), the
(2,5) branch DIES at level 2. If NONEMPTY: the surviving V* is the
campaign's candidate locus; extract/verify a point, report dimension;
remaining: rungs r = 12, 14 (quot vs pq46, qL), level-3 ladder,
J-closure.

Construction (engine-exact, additive to cases/r1_fullcore.py):
- F5 = f^5 exact truncation-first fold extended to dg = 11 (slots
  0..10; chainF.pkl has 0..2). Guards: slots 0..2 == chainF.pkl,
  slot-0 == S_M^5 P^10, odd slots empty (grading), and specialization
  at the locus point mod 105337 == /tmp/F5_point.pkl (independent).
- W_G^2 slot S (16..22) = sum over ordered pairs (sa,sb), sa+sb = S,
  6 <= sa,sb <= 20 (census CLOSED for S <= 26: odd/out-of-window/
  below-6/slot-0 partners die structurally, 9.1 note). Slot-6 factors
  reduced via the banked quot rows WG(.,6) = cL*p5 (ideal membership,
  same variety): contribution 2*cL*(p5 conv WG(.,S-6)). Genuinely
  quadratic pairs computed exactly from xWG.pkl: (8,8); (8,10);
  (8,12),(10,10); (8,14),(10,12) — measured ~3.8e7 exact K3
  term-pair products (bench: conv(8,10) = 1.58e6 pairs -> 115k
  monomials, 29 s; heavy collision => manageable emission).
- Rows: (W_G^2)[n,S] - s1*F5[n,S-12] = 0, labels C25-h2-tie-r<r>;
  any nonzero F5 content at odd/uncovered slots 2 < r' <= 10 gets a
  row -s1*F5 (s1 != 0 forces it; expected empty by grading — assert).
- Emission: expanded integer monomial sums only, no parens (AUDIT);
  p-variants FULLY reduced into [0,p) incl. radical rows (4b hazard).
- Artifacts: systems/r1/r1_25chain_ext.ms (+ _p105337/_p105673 +
  wfree variants), rows.txt each.

Guards (all must pass BEFORE any verdict): A paren sweep; B
independent-parser round-trip at 2 primes on the REDUCED p-variants;
C origin/constant census (origin must NOT satisfy the system; exactly
1 constant row t1*s1-1); D residual non-degeneracy (no emitted row
identically zero at 6 point/prime combos); E (NEW, point-validation)
at the banked locus point /tmp/full_point_p105337.pkl: (i) the
specialized r<=10 rows must reproduce the locus fiber rows
/tmp/fiber_rows.pkl (per-row match up to nonzero scalar, labels
S=16..22), (ii) msolve on the specialized r<=8 fiber != [1]
(consistent — extended rows CAN vanish at the point for suitable
interior values), (iii) msolve on the specialized r<=10 fiber == [1]
(the observed rung-10 kill — rows genuinely discriminating).
Regression gate: re-emission of the unextended core stays
byte-identical to the banked r1_25chain_core.ms.

Run discipline: reduced p-screens first (2 good primes, timeout
3000 s each), then char 0 (timeout 3000 s). msolve -g 2. Nothing
silent > 3 min; every phase checkpointed under /tmp/r1full.

### 12.1 Build log

Engine additions (cases/r1_fullcore.py, ADDITIVE — nothing above the
chain section touched; flags --chainF5ext, --conv25[-one=i],
--chain25ext): phase_chainF5ext (F5 to dg=11), phase_conv25 (exact
interior-pair convolutions, per-pair checkpoints conv25_sa_sb.pkl),
chain25_ext_rows, emit_ext_files (streamed one-pass char-0 + 2
fully-reduced p-variants from the SAME integer term lists),
reduce_eq_str (radical rows also reduced into [0,p)), guards_ext
(A-D), guard_E (point validation), phase_chain25ext (driver with
byte-identical core regression gate).

Exact interior convolutions (from xWG.pkl, measured; heavy monomial
collision confirms the farm-sizing was a safe overestimate):
| pair | term-pair products | result monomials | time |
|---|---|---|---|
| (8,8)   | 6.56e5  | 41,229    | 12 s |
| (8,10)  | 1.58e6  | 114,984   | 32 s |
| (10,10) | 3.81e6  | 198,516   | 77 s |
| (8,12)  | 6.00e6  | 540,087   | 126 s |
| (8,14)  | 1.19e7  | 964,775   | 254 s |
| (10,12) | 1.45e7  | 1,240,661 | 304 s |
Total 3.85e7 exact K3 term-pair products -> 3.10e6 quadratic-pair
monomials (+ the linear-in-cL slot-6-reduced parts + s1*F5 parts);
6-way parallel, all checkpointed.

F5 to dg=11: the block^5-then-fold order (phase_chainF at dg=3) is
pathological at dg=11 (>15 min stuck in one 670x670 product); the
FOLD-FIRST order (F1 = fold of slot<11-truncated blocks, then
F5 = ((F1^2)^2)F1; exact — slots >= 0, additive, truncation-first)
lands in 85 s: F5 = 3323 vkeys, 122 keys, slots {0,2,4,6,8,10} (odd
EMPTY — grading), slot-0 == S_M^5 P^10 re-verified, slots 0..2 ==
chainF.pkl EXACTLY.

Extended system r1_25chain_ext: **132 rows** = 44 core eqs (7 radical
+ 37 rows; first 44 eqs of the .ms BYTE-IDENTICAL to the banked
r1_25chain_core.ms modulo the continuation comma) + 95 deferred rows
(r=4: 23, r=6: 24, r=8: 24, r=10: 24); vars = 9 radicals + 29 core-x
+ 54 new interior (matches the 25LOCUS slot-16 cumulative census) +
s1, cL, t1. Exactly 1 constant row (t1*s1-1). Emitted files:
r1_25chain_ext.ms 287.9 MB (char 0), _p105337/_p105673.ms 135.5 MB
each (ALL coefficients incl. radical rows reduced into [0,p)),
_wfree_p105337/_wfree_p105673.ms 56.5 MB each (134 eqs, 86+4 vars).

### 12.2 Guard table (all PASS, 2026-08-10 17:21-17:25)

| guard | result |
|---|---|
| regression gate (core re-emission) | PASS — BYTE-IDENTICAL to banked r1_25chain_core.ms (guards A-D re-passed on the core en route) |
| A paren sweep | PASS — 0 parens in all 5 emitted files (streamed) |
| B independent-parser round-trip, REDUCED files | PASS — 132/132 rows match at p=105337 AND p=105673 (random point, all rows nonzero) |
| C origin/constant census | PASS — 131/132 rows vanish at x=0, the t1*s1-1 row does NOT => origin excluded; exactly 1 constant row |
| D residual non-degeneracy | PASS — no emitted row identically zero (6 point/prime combos) |
| E(i) point-validation vs locus data | PASS — all 93 nonzero specialized rows at the banked point (mod 105337) MATCH /tmp/fiber_rows.pkl up to per-row scalar (2 of the 95 symbolic rows specialize to 0 there) |
| E(ii) r<=8 sub-fiber | PASS — msolve GB nonempty (69 rows CAN vanish at the point: emission consistent with the banked r<=8 verdict) |
| E(iii) r<=10 fiber | PASS — msolve GB = [1] (the observed rung-10 kill is REPRODUCED by this emission at the point) |

Note guard E is a STRONG cross-validation: the locus fiber rows were
assembled by an independent implementation (point-specialized xWG
entries, mod-p arithmetic throughout); matching all 93 rows term-by-
term validates the exact convolutions, the cL-reduction of slot-6
pairs, the F5 extension, and the s1-tie assembly simultaneously.

### 12.3 Run ledger (msolve 0.10.1 local, -g 2 -t 4)

| run | budget | result |
|---|---|---|
| ext_p105337 + ext_p105673 parallel | 3000 s | both KILLED silently ~13 min in (macOS memory sweep: a 13-GB unrelated redcheck msolve + 2 x 2 GB jobs; the redcheck job died too) — no verdict, relaunched solo |
| ext_p105337 solo | 3000 s | **TIMEOUT** (RSS to ~16 GB, 100% CPU throughout; no partial output — msolve writes only at completion). The extended GB is FAR heavier than the core's 487-elt/55 s: the 95 deferred rows carry real load |

## 13. Chart decomposition of the reduced core (2026-08-11)

Engine: cases/r1_decompose.py (ADDITIVE; parses the guard-certified
artifact systems/r1/r1_reduced_core.ms; prior emissions untouched).
Motivation: the monolithic wfree p-screen died at 34 h / 1.5 TB ulimit
with no verdict; 10.6 rec. 3 named the W case split as the next lever.

### 13.0 Structural finding (banked BEFORE any leaf run) + design

Occurrence census of the 49 rows / 32,600 terms: 5,496 terms W1-loaded,
5,496 W2-loaded (exact 1<->2 symmetry), 0 mixed, 21,608 W-free; every
row touches both W-sides; NO row has an x-free W-free term. Therefore
the point (all x = 0, W1=HW1=W2=HW2=0, any etale point) kills EVERY
term of EVERY row: it lies on V(reduced core) EXACTLY, in char 0 and
every p (verified mod p=105337: 49/49 rows vanish). Consequence: the
monolithic wfree p-screen could never return EMPTY -- its variety
contains this point; 34 h + 1.5 TB were spent toward a foredoomed,
undiagnostic NONEMPTY. Diagnosis: the emitted core is a RELAXATION --
it carries only the tie 2HW_i^2 = 3W_i^2 and DROPS the E5 quartic
w_i^4 = k_i alpha_i^2 (k_i != 0: stage-0 gate "E5 solvable: a_i-b != 0
(w_i^4 pinned nonzero)", cases/r1_experiment.py:1032; the 7c w-branches
were subsumed as embeddings, so no quartic row exists in the core).
On the INTENDED locus w_i is a unit; W_i = 0 is relaxation-only.

DESIGN (the (72,108) two_chart pattern, lib/chartelim.py, generalized
to the pivot-blocking variables W1, W2): split V(reduced core) by the
vanishing pattern of (W1, W2) into 4 leaves ZZ, ZU, UZ, UU (Z: W_i = 0
substituted, and HW_i = 0 with it -- sound on the variety since
HW_i^2 = (3/2)W_i^2 + ideal; U: Rabinowitsch uWi with uWi*W_i - 1
adjoined). U-charts make every W-monomial coefficient invertible
(HW_i^{-1} = (2/3) HW_i uWi^2 via the quadric), unlocking the
quasi-linear pivots r1_reduce.py had to bar: census says W1-unit
unlocks clean pivots for x11,13,15,55,57,59 (+ deg-2 vars x7,9,51,53),
W2-unit the mirror set x24,26,28,68,70,72 (+ x20,22,64,66). Per-leaf:
chart substitution, then the 10.1-sound elimination cascade with the
enlarged unit class (pivot coeff = single W-monomial x certified etale
unit; explicit inverse; banked back-map), then emission (expanded
monomial sums; p-variants coefficient-reduced into [0,p)) + guards
A-E + calibration (msolve -g 2 -t 4, 900 s).

PRE-REGISTERED INTERPRETATION (fixed BEFORE any leaf solve): the four
leaves partition V(core) by a boolean tautology, so (all leaves EMPTY)
<=> core EMPTY, and any leaf point maps to a core point. ZZ is
NONEMPTY a priori (witness above; it will be re-verified mechanically,
not discovered by msolve). Z-pattern leaves are RELAXATION-DEGENERATE
content (off the intended locus, where w_i are units). The DIAGNOSTIC
p-screen verdict for the minimal branch is the UU leaf's verdict:
UU EMPTY at p => the intended-locus p-screen is EMPTY at p (strong
evidence tier per the 10.0 pre-registration, not a char-0 proof);
UU NONEMPTY at p => the relaxed-with-units screen survives at p
(evidence toward realizability; still short of the quartic tie).
The composite relaxed-core verdict (NONEMPTY via ZZ) is reported
alongside but is NOT branch-diagnostic. No inflation of any leaf
verdict beyond this table.

### 13.1 Build results (phase build; state /tmp/r1dec/leaves.pkl)

Chart kill + per-leaf cascade (every pivot coefficient = single
W-monomial x etale part, unit-certified by min-poly; explicit inverse
uses HW_i^{-1} = (2/3)HW_i uWi^2; each pivot's coeff*inv == 1 asserted
mechanically):
| leaf | chart | rows | x-vars | terms | elim'd | dropped-as-zero |
|---|---|---|---|---|---|---|
| ZZ | W1=0, W2=0 | 49 | 50 | 21,608 | 0 (no W-pivots) | 0 |
| ZU | W1=0, W2 unit | 42 | 36 | 12,877 | 7 (x20,22,24,26,28,65,67) | 0 |
| UZ | W1 unit, W2=0 | 42 | 36 | 12,877 | 7 (x7,9,11,13,15,52,54) | 0 |
| UU | both units | 5 | 0 | 20 | 16 | 28 |

UU COLLAPSE: on the intended chart the cascade eliminates 16 x-vars
(x7,9,11,13,15,20,22,24,26,28,50,52,54,63,65,67 -- banked invertible
substitutions), drops 28 rows as identically zero, and frees the other
38 x's (absent from every survivor; absorbed by the back-map). The 5
surviving rows are the five quotient rows eq47-eq51 (WG-quot n =
1,4,7,10,13, slot 20) and are PROPORTIONAL over Q (factors -8, 8, -4,
1/3 of eq47's reduction; asserted exactly): residual rank 1. The single
surviving constraint is

  E:  (9 + 5 r3) A1 W1^4 + (9 - 5 r3) A2 W2^4 = 0.

So V(UU leaf) = V(radical relations, uWi Wi = 1, E) x A^38, i.e. the
ENTIRE minimal-branch G_m terminal core, restricted to the intended
chart w1 w2 != 0, is equivalent to the one E5-shaped quartic relation E.

E5 CONSISTENCY IDENTITY (exact, banked): on the intended locus the
dropped quartic tie w_i^4 = k_i alpha_i^2 (sec-3.0, k_i =
-(4/3)H_M(a_i-b)/(243 s0 S_M^3 (a1-a2)^4 a_i^3)) turns E into
(9+5r3)k1 a1 + (9-5r3)k2 a2 = 0, in which H_M, S_M and the constant
factors CANCEL, leaving (9+5s)(a1-4)/a1^2 + (9-5s)(a2-4)/a2^2 with
s = sqrt3, a_i = 3 +- s. Exact Q(sqrt3) arithmetic: the two terms are
+s/3 and -s/3 -- the sum is IDENTICALLY ZERO. The G_m core's only
surviving constraint on the intended chart is exactly the E5 quartic
consistency identity, and the intended fourth-root data satisfies it
identically. (Fraction-exact; reproducible via phase e5check, which
also asserts the rank-1 proportionality and row40 == -81*E -- PASS.)

### 13.2 Emission, guard table, cover certificate

EMITTED (systems/r1/leaves/, all expanded monomial sums, no parens;
wfree p-variants coefficient-reduced into [0,p), '+'-joined):
leaf_{ZZ,ZU,UZ,UU}.ms (char 0, radicals as vars, chart rows included:
Z-side W/HW eliminated, U-side quadric + uWi*Wi-1 Rabinowitsch) +
leaf_*_wfree_p{105337,105673}.ms (etale gens specialized at the banked
radical point; W-side + x vars free) + per-leaf .rows.txt provenance
(elim bank with |s| and pivot rows; free-x list; row map). Sizes:
ZZ 0.56/0.21 MB, ZU = UZ 0.42/0.14 MB, UU 0.003/0.0003 MB.

GUARDS (phase guards; all PASS, log 01:33 2026-08-11):
| guard | ZZ | ZU | UZ | UU |
|---|---|---|---|---|
| A paren sweep (3 files each) | PASS | PASS | PASS | PASS |
| B round-trip 2 primes, char0 AND wfree vs internal eval | 49/49 | 42/42 | 42/42 | 5/5 (all nonzero at random chart point) |
| C x=0 at generic chart point | 49/49 vanish: ORIGIN-SATISFIABLE (the 13.0 witness) | 35/42 | 35/42 | 0/5 (origin excluded) |
| D residual non-degeneracy (6 pt/prime combos) | 0 id-zero | 0 | 0 | 0 |
| E soundness/back-map, 2 primes x 2 pts | 49 surv == orig | 7 pivot rows vanish; 42 surv == orig | same | 16 pivot + 28 dropped rows vanish; 5 surv == orig |

COVER CERTIFICATE. Claim: V(reduced core) = U_pat pi(V(leaf_pat)),
pat over {Z,U}^2, pairwise disjoint by the W-vanishing pattern.
Argument: (a) tautology -- any point has W1 = 0 or W1 != 0, and W2 = 0
or W2 != 0, exactly one pattern (mechanical: 500 random (W1,W2)
samples, exactly one pattern each, PASS); (b) Z-side: the quadric at
W_i = 0 reads 2HW_i^2 = 0, so HW_i = 0 on the variety (char != 2) --
the substitution W_i = HW_i = 0 loses no points; (c) U-side: uWi :=
W_i^{-1} exists and is unique (field), so the point lifts uniquely to
the Rabinowitsch chart; (d) within each chart, the elimination bank is
an invertible substitution chain (every pivot coefficient = certified
etale unit x W-monomial, invertible on the chart; coeff*inv == 1
asserted per pivot at build), so V(chart system) = V(leaf) x A^{free}
-- certified numerically by guard E in BOTH directions (pivot/dropped
rows vanish under back-map; survivors match). Conversely any leaf
point maps to a core point by forgetting uWi and restoring W_i = 0
(Z-sides) + back-substituting the elim bank (guard E). Hence
EMPTY on all leaves <=> core EMPTY, and any leaf witness lifts.

### 13.3 Calibration ledger + composite verdict

Runs: msolve 0.10.1, -g 2 -t 4, timeout 900 s, local (12-core/32 GB);
runs/leaf_*.out, runs/r1_leaves_calibrate.log. EVERY leaf returned a
VERDICT in ~1 s at <2 MB RSS -- nothing ships to ultramem:

| leaf | wfree p=105337 | wfree p=105673 | wall | RSS |
|---|---|---|---|---|
| ZZ | GB != [1] NONEMPTY | GB != [1] NONEMPTY | 1 s | <2 MB |
| ZU | GB = [1] EMPTY | GB = [1] EMPTY | 1 s | <1 MB |
| UZ | GB = [1] EMPTY | GB = [1] EMPTY | 1 s | <1 MB |
| UU | GB != [1] NONEMPTY (15-elt GB) | GB != [1] NONEMPTY | 1 s | <1 MB |
| UU char 0 (leaf_UU.ms, radicals as vars) | GB != [1]: 121-elt reduced GB over Q | - | 1 s | <1 MB |

COMPOSITE VERDICT (under the 13.0 pre-registration + cover cert):
1. Relaxed-core p-screen at BOTH banked primes: NONEMPTY =
   ZZ-stratum (explicit witness x=0, W=0; cover (iii)) UNION
   UU-stratum (15-elt GB). ZU/UZ EMPTY: every core point mod p has
   W1, W2 BOTH zero or BOTH nonzero. The minimal-branch G_m terminal
   core is NOT killed at p. No EMPTY trigger; no inflation.
2. DIAGNOSTIC (intended-chart) verdict: UU NONEMPTY at both primes
   AND in char 0 (121-elt reduced GB over Q => V NONEMPTY over Qbar;
   with guard E + sec-10.2 guard E, V(full core) NONEMPTY over Qbar).
   The pre-registered decisive object (char-0 core emptiness, sec
   8/10) is DECIDED: NO KILL. Per sec-1: the formal candidate
   DEEPENS; R1's terminal G_m core imposes, on the intended chart,
   EXACTLY the constraint E -- which the E5 fourth-root data
   satisfies identically (13.1). Remaining obligations unchanged:
   full-degree F_s band (farm, 8.5), R2-R5 ladder, J-closure.
3. The 34 h/1.5 TB monolith run and the queued multi-day char-0
   ultramem run are OBSOLETE: the verdict they sought is banked
   above at ~1 s/leaf. RETIRE the reduced-core monolith from the
   ultramem queue.

### 13.4 Explicit intended-chart witness (strongest certificate)

Phase witness (banked 01:58): at BOTH banked primes an EXPLICIT
rational point of the FULL terminal core with W1, W2 != 0 was
constructed and verified end-to-end on the EMITTED artifacts with the
INDEPENDENT parser (r1_fullcore.parse_eval):
- solve E for W1 with W2 = 1 (4th root exists at the om^0 A-embedding
  at both primes; Tonelli twice), HW_i = sqrt(3/2) W_i, uWi = W_i^{-1},
  free x's = 0, then back-substitute the 16 leaf-UU subs AND the 19
  sec-10 subs;
- p=105337: W1=32284; p=105673: W1=90918; in both cases ALL 56 eqs of
  r1_reduced_core.ms AND ALL 105 eqs of r1_full_core.ms evaluate to 0.
This upgrades the UU NONEMPTY from GB-certificate to explicit-point
certificate on the intended chart, through both banked back-maps --
simultaneously an end-to-end validation of the whole 10.x + 13.x
elimination pipeline. The sec-10.6 mandated back-map spot-check (then
vacuous: no solver points) is now DISCHARGED with these 2 points.

### 13.5 Engine + state

cases/r1_decompose.py (ADDITIVE; phases stats | build | emit | guards
| cover | e5check | calibrate | psweep | witness). State:
/tmp/r1dec/leaves.pkl (per-leaf rows + banked substitution chains +
dropped lists). Repo changes: SHEET6-R1.md + the new engine only
(systems/, runs/ are gitignored-regenerable; leaves re-emittable via
build + emit from r1_reduced_core.ms). Prior emissions byte-untouched.

### 13.6 Multi-prime confirmation + engine bug note

Phase psweep: all 4 leaves re-emitted + solved at 6 FRESH primes with
full radical points (good_primes walk: 109537, 165313, 177409, 188833,
200257, 225961; ~1 s each). Verdict pattern IDENTICAL at all 6 (and at
both banked primes -- 8 primes total, no exception):
ZZ NONEMPTY / ZU EMPTY / UZ EMPTY / UU NONEMPTY.
Under the 10.0 calibration table this is the strong-evidence tier for
the char-0 readings in 13.3 (which are additionally PROVEN in char 0
for ZZ -- exact witness -- and UU -- 121-elt GB over Q + the two
explicit mod-p points of 13.4; ZU/UZ char-0 emptiness stays
evidence-tier only). BUG NOTE (banked): r1_reduce.sweepw_primes is
UNUSABLE -- its candidate pool is the ~1,170 values (2^15..2^17 on the
84-grid), of which only ~1-2 admit full radical points, and None
results are uncached => effectively infinite loop at n >= 2. Any
future wfree sweeps must use the good_primes walk (r1_decompose.
phase_psweep does).

## 14. Minimal-branch EXTENDED system: UU-chart core + F_s-band rungs r <= 4 (2026-08-11)

### 14.0 Design + rung choice + pre-registration (banked BEFORE build)

Mission: the minimal-branch analogue of the (2,5) rung-extension (sec
12), mandated by sec 13: the core alone is non-discriminating (UU chart
collapses it to the identically-satisfied relation E; all
discriminating content is DEFERRED -- F_s band, R2-R5, J-closure).

SYSTEM = core + chart + deferred F_s rungs:
- CORE PART: r1_full_core.ms VERBATIM (105 eqs; regression gate:
  byte-identity). The UNREDUCED core is required for soundness: the
  F_s rows re-engage bf_18/bf_24/bf_30 (= emitted x37/x43/x49), which
  the sec-10 pre-reduction ELIMINATED (pivot rows deleted); combining
  the reduced core (or the UU leaf) with raw F_s rows would leave
  those vars unconstrained-as-fresh, losing their determination. The
  full core carries the same variety with zero substitution machinery.
- CHART ROWS: uW1*W1-1, uW2*W2-1 (Rabinowitsch). Per sec 13 the
  extension lives in the UU chart: ZU/UZ are EMPTY at 8/8 primes, ZZ
  is the relaxation artifact (x=0, W=0), and the intended locus has
  w_i units. Adjoining the inverses to the FULL core is sound: the
  sec-10 equivalence is chart-independent (etale-unit pivots).
- F_s ROWS: W_F band rows WF[(n,s)] = 0, W_F = gF^2 - fF^3 in the F_s
  window at FULL var-degree, slot-truncated at 25 (truncation-first is
  exact for kept slots). Labels ("Fs-band", n, s), rung r = s/6.

RUNG CHOICE (mirrors sec 12): the minimal-branch F_s rung ledger (secs
3, 8.5) is the W_F cancellation band on the 6-grid, 1/7-slots r = s/6:
in-window rungs r = 1..6 (stages m = 18..48, the pass-1 ledger's first
deferred stages, ~127-140 deferred rows each) + the 18->8 quotient
(H_F^3 = s1 S_F^4) at r = 10, which needs depth 84 = farm-only (8.5).
CHOSEN: r = 1..4 (slots 6, 12, 18, 24) --
(i) the FIRST band expected to bite (lowest deferred stages), exactly
    the (2,5) pattern: 4 lowest rungs of the band, stopping short of
    the quotient tier ((2,5) took r = 4..10 of its 4..14 ladder);
(ii) s <= 24 is the natural w-free sub-window: the w_i pins sit at
    level 37 = F_s slot 25, so rungs 5-6 (slots 30, 36) are the first
    to carry the E5 quartic coupling -- that is the NEXT tier, exactly
    as the (2,5) quotient rungs r = 12, 14 were deferred there;
(iii) slot-s rows carry weight-s monomials: s <= 24 is locally
    feasible; the full band s <= 36 is the 8.5 farm-scale object.
New variables (beyond the core's 119): uW1, uW2 + the F_s-window vars
absent from W_G -- uf30, bf_31..36, bg42_31..36, bg21_32..36 (x119..,
compact enumeration continued in registry order).

PRE-REGISTERED INTERPRETATION (sec 1 discipline, fixed before any
solve): verdict object = the emitted extended system on the UU chart.
EMPTY (guard-passed, both wfree p-screens GB = [1]; ZU/UZ already
empty and ZZ artifact per sec 13) => the minimal branch DIES at the
first F_s rung tier. NONEMPTY => the branch survives to the next tier
(r = 5, 6, then the r = 10 quotient at depth 84); report surviving
locus dimension if computable. Char-0 run only if both p-screens
finish fast (< 300 s); local budget 900 s / 4 threads; on local
timeout the emission ships to box01 (NOTE: box01 currently runs the
(2,5) ext at 16 threads -- the minimal ext would QUEUE behind it).
GUARDS (all must pass before any verdict): A paren sweep; B two-prime
round-trip char0 + p-variant + wfree vs internal VExpr eval; C
origin/constant-term plausibility; D residual non-degeneracy (6
combos); E witness validation (sec 13.4 points, both primes): the
banked full-core witnesses MUST satisfy all 105 core + 2 chart rows of
the EMITTED extension (validates emission), and the F_s rows must NOT
all vanish there (else the extension is vacuous at the witness ->
pre-registered fallback: go one rung deeper).
Build anchors (hard asserts): f/g slot-0 == p21^6/p21^9 (stage-0
identities); E1: WF slot-0 identically zero; F_s grading s == 12n
(mod 42) => 6-grid-only rows; no HIVAR (VDEG_CAP = 999); sequential
linear-factor fold == fs_jet (rep-then-image path) at slot cap 7,
exact dict equality, f AND g.
Engine: cases/r1_minimal_ext.py (ADDITIVE; phases fsjets | wf | emit |
guards | run; state /tmp/r1mext). AUDIT rules: expanded integer
monomials, no parens; p-variants FULLY coefficient-reduced into [0,p)
incl. radical rows (FC.reduce_eq_str, the sec-12 4b fix -- NOTE the
banked r1_full_core_p*.ms used the older signed-digit reduction; the
ext p-variants are fully reduced).

### 14.1 Build log

Engine: cases/r1_minimal_ext.py (new, ADDITIVE; prior emissions and
engine files byte-untouched; runtime-only monkey-patch of R1.rnorm).

Fold-shape measurements (orbit B, slot cap 13, banked before the full
build; extends the 8.12 lesson to the F_s window):
- rnorm memo (rnorm(key,c) is EXACTLY linear in c; key-part cached;
  300-sample A/B against the unpatched rnorm asserted at patch time):
  prerequisite for every path below.
- sequential linear-factor fold (dense x sparse): 184 s.
- "fixed-j 7-direction group" reassociation: 2276 s -- WRONG IDEA,
  banked: the fixed-j group is NOT C_7-stable (k = 6 -> 7 wraps the
  twist index c = k+7j into the j+1 suborbit), so no early phase
  aggregation happens and the grouped partials are DENSER. Mid-fold
  partials in every ungrouped order carry ~456 un-aggregated (n,s)
  keys that collapse to 19 only at the last factors.
- fs_block (the engine's suborbit-Newton path: power sums aggregate
  the zeta^{7js} phases by selector BEFORE any eta-product): 31.4 s,
  6x the linear fold, ~70x the naive order. CHOSEN.
Cross-checks: fs_block == fs_jet == sequential fold at slot cap 7
(all 9 orbits, exact dict equality); fs_block == sequential fold for
orbit B at slot cap 13 (exact dict equality). fs jets carry NO W
content at slot <= 24 (w-pins sit at slot 25) -- asserted at emission.

Grading correction (banked): the true F_s jet grading, measured on the
banked orbit folds and asserted on all jets and W_F, is
12n + s == 0 (mod 42) (sec-3's prose "s = 12n (mod 42)" has the sign
flipped; the 6-grid-only consequence -- the rung ledger -- is
unaffected). First chain run tripped the wrong-sign assert; fixed and
re-asserted: 0 violations on f (91 keys), g (136 keys), WF (216 keys).

Build numbers (chain complete 04:19, state /tmp/r1mext):
- orbit folds (SCAP 25): P/G-side pole orbits ~ 6-15 s each; B and
  GB42 (42-orbits, 24 tail vars) 31 keys / 9,792 terms each, ~21 min
  CPU each (3 parallel workers); GB21 11 s.
- jets: f-jet 91 keys / 45,564 terms; g-jet 136 keys / 153,935 terms
  (65 s incl. anchors + 3-way cap-7 cross-check).
- W_F: f^2 112 s, f^3 351 s, g^2 999 s; E1 anchor (slot-0
  identically zero) PASS; off-6-grid content: NONE (asserted).
- rows: 54 rows per rung x 4 rungs = 216 F_s-band rows; terms/rung:
  r=1: 1,346; r=2: 11,798; r=3: 73,838; r=4: 375,044 (n in [2..377],
  n mod 7 fixed per slot by the grading).

### 14.2 Emission + guard table

EMITTED (systems/r1/): r1_minimal_ext.ms (323 eqs = 105 core VERBATIM
+ 2 chart + 216 F_s rows; 146 vars = 9 radicals + uW1,uW2 + x0..x118
banked map + x119..x134 new (uf30, bf_31..36, bg42_31..36,
bg21_32/34/36 -- compact enumeration continued in registry order);
38.1 MB) + _p105337/_p105673.ms (28.6 MB each, ALL coefficients
reduced into [0,p) incl. radical rows) + _wfree_p*.ms (318 eqs, 141
vars, 18 MB each: banked wfree core rows verbatim + uW rows + F_s
rows specialized at the banked radical points) + .rows.txt (labels +
full var map). F_s rows are W-FREE (w-pins sit at slot 25 > 24).

| guard | result |
|---|---|
| regression gate | PASS -- first 105 eqs BYTE-IDENTICAL to r1_full_core.ms |
| A paren sweep | PASS -- 0 parens, all 5 files |
| B round-trip | PASS both primes -- char0 vs p-variant exact (323 rows); F_s rows exact vs internal VExpr eval (216/216, and all nonzero at random points); wfree core rows via 2-point cross-ratio (banked wfree emission is unscaled; char-0 is content-normalized -- per-row scalar allowance, sec-12 E(i) style) |
| C origin/constants | 10/323 rows nonzero at x=0 (exactly the slot-20 quotient family) -> origin excluded; F_s rows carry NO constant terms (in-window pins {0,20,25} cannot sum to a 6-grid slot: band is prefix-exact, as in 8.4) |
| D residual | PASS -- 0 identically-zero rows (6 point/prime combos, all vars random) |
| E witness (13.4, both primes) | core+chart: ALL 107 rows vanish -- emission validated end-to-end through both banked back-maps. F_s rows: 0/216 nonzero -> VACUOUS AT THE WITNESS (see 14.3) |

### 14.3 The witness result: extension vacuity at the intended point,
### and why "one rung deeper" is provably undiagnostic

Guard E outcome (both primes): the sec-13.4 intended-chart witnesses
satisfy ALL 323 equations of the emitted extended system -- core (105),
chart (2), AND every F_s-band row (216).  The extended p-screen verdict
is therefore decided by explicit point BEFORE msolve: NONEMPTY at both
banked primes.  msolve runs below are confirmation only.

MECHANISM (measured, banked): the witness sets all free x's to 0 and
back-maps the 35 eliminated ones; the only NONZERO back-mapped values
are x15, x18, x28, x31 = tf1_47, tf1_52, tf2_47, tf2_52 -- F_s slots
35 and 40.  Every F_s-window variable at slot <= 36 is ZERO at the
witness (incl. the re-engaged x37/x43/x49 = bf_18/24/30, measured 0).
Since no in-window W_F row carries a constant term (guard C), every
F_s row evaluates to 0 there.

ESCALATION ANALYSIS (the 14.0 pre-registered fallback, discharged
mechanically WITHOUT the multi-hour slot-31/37 rebuild -- the sec-13.0
foredoomed-run lesson applied BEFORE spending the compute): rung 5
(slot 30) and rung 6 (slot 36) rows have term var-slot sums in
{30,10,5} resp. {36,16,11} (pins: 20 = a_i, 25 = w_i).  The witness's
nonzero slots {35, 40} cannot participate: 35, 40 > 30; for a slot-36
sum, 35 needs a slot-1 partner, which is zero at the witness.  So
EVERY term of EVERY rung-5/6 row contains a zero factor: the witness
identically satisfies the ENTIRE in-window F_s band (r <= 6, depth
54), not just r <= 4.  Going one rung deeper cannot change any
verdict at the banked primes; the guard-E vacuity flag would fire
again, provably.  BANKED as the tier finding: the in-window F_s band
is NON-DISCRIMINATING against the minimal-branch core's surviving
locus at the banked primes -- the free-x directions the core leaves
open let the whole band be satisfied trivially (the F_s analogue of
the 13.0 relaxation diagnosis).

The first F_s object that CAN bite the witness is the depth-84
quotient tie (1/7-slot 10, the 18->8 cancellation quotient,
H_F^3 = s1 S_F^4): like the G_m slot-20 quotient family (the 10
origin-excluding rows of guard C), it is CONSTANT-BEARING, so it
cannot be satisfied by zeroing tails.  It is farm-scale (8.5 sizing:
degree <= 36 objects at depth 84, 10^7-10^8 monomials) -- goes to
box01 WITH the note that box01 currently runs the (2,5) ext at 16
threads and this job would QUEUE behind it.

### 14.4 Run ledger + verdict

Runs (msolve 0.10.1, -g 2 -t 4, timeout 900 s, local; runs/
r1_minimal_ext_runs.log):

| run | result |
|---|---|
| wfree p=105337 (318 eqs, 141 vars, 18 MB) | TIMEOUT 900 s, RSS 13.1 GB, no output |
| wfree p=105673 | TIMEOUT 900 s, RSS 13.3 GB, no output |
| char 0 (38.1 MB) | NOT RUN (pre-registered gate: p-screens must finish < 300 s) |

The GB confirmation therefore ships to box01 (sizes above; NOTE:
box01 currently runs the (2,5) ext at 16 threads -- this job QUEUES
behind it).  The msolve timeouts do NOT leave the tier undecided:

VERDICT (under the 14.0 pre-registration; sec-1 discipline):
1. EMPTY trigger: NOT FIRED -- and PROVABLY unfireable at the banked
   primes: the sec-13.4 witnesses are explicit points of the emitted
   extended system (guard E, both primes, independent parser).  The
   minimal-branch extended p-screen is NONEMPTY at p = 105337 and
   105673 by explicit-point certificate (a strictly stronger
   certificate than the deferred GB).
2. => the minimal branch SURVIVES the first F_s rung tier; by the
   14.3 slot-census argument the SAME witnesses survive every
   in-window rung (r <= 6, depth 54), so the branch survives the
   ENTIRE locally-buildable F_s band.  Surviving-locus dimension: NOT
   computable locally (GB timeout); positive-dimensionality note: the
   68 x-vars absent from every F_s row (all tf/tg tails, levels >=
   38) do not appear in the added rows at all, so the extension
   changes nothing in those directions -- the surviving locus fibers
   over the F_s-window vars exactly as the core did.
3. Char-0 emptiness of the extended system: OPEN (deferred to box01
   char-0 + the depth-84 quotient tier).  No inflation: the witness
   certificate is mod-p; the char-0 verdict remains governed by the
   10.0 calibration tiers.
4. REMAINING OBLIGATIONS for the minimal branch (updated ladder):
   (i) depth-84 F_s quotient tie (H_F^3 = s1 S_F^4, constant-bearing,
   the first object that can exclude the witness; farm/box01, 8.5
   sizing); (ii) R2-R5 ladder; (iii) J-closure.  Unchanged from
   sec 13.3 except the in-window F_s band is now DISCHARGED as
   non-discriminating (this section).

### 14.5 Deliverables + state

systems/r1/r1_minimal_ext.ms (+ _p105337/_p105673, _wfree_p105337/
_wfree_p105673, .rows.txt); engine cases/r1_minimal_ext.py (ADDITIVE:
new file; runtime-only rnorm memo patch, A/B-tested at import; no
prior file touched; prior emissions byte-identical -- regression gate);
state /tmp/r1mext (orbit checkpoints, fsjets.pkl, wf.pkl); runs/
r1_minimal_ext_runs.log + .ms.out stubs.  Phases: orb <name> | fsjets
| wf | emit | guards | run (chain script /tmp/r1mext/chain.sh).

## 15. (1,2) sibling 4-leaf decomposition + depth-84 quotient-tier sizing (2026-08-11)

### 15.0 Part-A plan + pre-registration (banked BEFORE any build/solve)

Mission: apply the sec-13 chart decomposition to the (1,2) sibling core
systems/r1/r1_12branch_core.ms (8.19: 105 eqs = 7 radical + 98 rows
[B12-WG-band 37, B12-h2-tie 50, B12-h2-quot 11]; vars = 9 radicals +
x0..x118 + s1 tie; 22.1 MB). Engine: cases/r1_12_decompose.py, ADDITIVE
(imports r1_decompose/r1_reduce functions; minimal-core leaves stay
byte-identical -- sha256 regression gate on systems/r1/leaves/ before
vs after). s1 is carried internally as x119 (r1_reduce.parse_poly
asserts x-names) and re-named s1 at emission.

Design deltas vs sec 13 (mechanical): (i) input = the RAW (1,2) core
(no sec-10 pre-reduction exists for it); leaf_eliminate SUBSUMES it --
etale W-free pivots are chart-independent members of its pivot class;
guard E certifies soundness directly against the 98 original rows.
(ii) cover-cert part (iii) is REPLACED: the (1,2) core has 10
constant-bearing rows (8.19; NOT origin-satisfiable), so no a-priori
ZZ witness; instead the per-leaf origin/constant census is banked (a
ZZ-origin finding would be a 13.0-style relaxation artifact IFF the
constants are W-loaded and die at W=0 -- measured, not assumed).
(iii) if leaf emission is heavy, it is staged per leaf (bank each).

PRE-REGISTERED INTERPRETATION (fixed BEFORE any leaf solve; sec-1
discipline; R1 is PER-BRANCH on {minimal, (1,2), (2,3), (2,5)} per
SHEET6-R6 4.3): the 4 leaves partition V(core) by the (W1,W2)
tautology; cover cert (i),(ii),(iv back-map) as in 13.2. Verdicts:
- ALL FOUR leaves EMPTY (GB=[1]) at both banked primes => (1,2) core
  p-screen EMPTY (strong-evidence tier per 10.0 calibration; char-0
  GB=[1] on every leaf upgrades to proof) => the (1,2) branch DIES at
  its terminal core.
- UU EMPTY + some Z-leaf NONEMPTY => intended-chart kill: (1,2)
  survives only as relaxation-degenerate (some W_i = 0) content, off
  the intended locus (w_i units); diagnostic verdict = intended-chart
  EMPTY (13.0 tier language).
- UU NONEMPTY => (1,2) survives its terminal core on the intended
  chart; bank the surviving relation(s); remaining obligations = its
  F_s band, R2-R5, J-closure (per-branch ladder).
- No inflation beyond this table. msolve -g 2 -t 4, timeout 900 s per
  leaf, local; timeouts ship to box01 with sizes.
Guards A-E exactly as 13.2 (paren; 2-prime round-trip char0+wfree;
origin census; residual; soundness/back-map). 13.4-style witness only
if the UU residual collapses to cheaply-solvable relations (<= 2
low-degree rows); else banked deferred with reason.

Part B (depth-84 quotient tier) = sizing + staging plan ONLY (no full
build); free-closure analysis first (the 14.3 slot-census argument
generalized); sections 15.4+.

### 15.1 (1,2) census + build results (phase stats/build; state
### /tmp/r1dec12/leaves.pkl)

Census (98 rows, 497,969 terms): W1-loaded 9,980 = W2-loaded 9,980
(exact 1<->2 symmetry again), 0 mixed, 478,009 W-free; 58 rows touch
each W-side.  The 10 constant-bearing rows are rows 87-96 (B12-h2-quot
slot-20 family) and their constants are W-LOADED -- they die at
W = 0, so the ZZ pattern is again relaxation-artifact-prone (13.0
mechanism; measured in cover (iii') below).  s1 appears in 41 rows,
max degree 1 (never a clean pivot: its coefficients F2(n,r) carry x's).

Build (chart kill + per-leaf cascade, W-monomial x etale-unit pivots,
coeff*inv == 1 asserted per pivot; ~40 s/leaf):
| leaf | rows | x-vars | terms | elim'd | dropped-as-zero |
|---|---|---|---|---|---|
| ZZ | 48 | 50 | 21,536 | 20 (all etale W-free) | 30 |
| ZU | 32 | 34 | 8,305 | 28 | 38 |
| UZ | 33 | 36 | 12,621 | 27 | 38 |
| UU | 5 | 0 | 20 | 35 | 58 |

UU COLLAPSE, SAME TERMINAL RELATION AS THE MINIMAL BRANCH: the 5
survivors are rows 87-91 (B12-h2-quot, slot 20), rank 1 (factors
-16, 16, -8, 2 of row 87; asserted exactly), and row 87 ==
-(3363432789843/2) * E with EXACTLY the sec-13.1 relation

  E: (9 + 5 r3) A1 W1^4 + (9 - 5 r3) A2 W2^4 = 0.

(9/5 coefficient ratio verified exactly; 3363432789843 = content.)
Consequence: the 13.1 E5 consistency identity applies VERBATIM -- the
intended fourth-root data (w_i^4 = k_i alpha_i^2, sec-3.0 k_i)
satisfies the (1,2) core's entire UU residual identically, and the
13.4 witness construction (solve E for W1 at W2 = 1, back-map) ports
unchanged.  The (1,2) delta content (extra staged G_m level, P^4
quotient) is entirely absorbed by the cascade: discriminating
content on the intended chart = E, as in the minimal branch.

### 15.2 Emission, guards, cover certificate, explicit witness

EMITTED (systems/r1/leaves/, minimal-core leaf_* files BYTE-UNTOUCHED
-- sha256 gate below): leaf12_{ZZ,ZU,UZ,UU}.ms + _wfree_p{105337,
105673}.ms + .rows.txt.  Sizes: ZZ 0.56/0.21 MB (53 eqs/55 vars char-0;
48/50 wfree), ZU 0.23/0.08 (39/42; 34/37), UZ 0.38/0.14 (40/44;
35/39), UU 0.003/0.0003 (14 eqs/11 vars; 9/6).  s1 survives only in
ZZ/ZU/UZ headers (eliminated nowhere; FREE in UU -- absent from every
survivor).

GUARDS (all PASS, log 06:07-06:08):
| guard | ZZ | ZU | UZ | UU |
|---|---|---|---|---|
| A paren (3 files each) | PASS | PASS | PASS | PASS |
| B round-trip 2 primes char0+wfree | 48/48 | 32/32 | 33/33 | 5/5 |
| C x=s1=0 at chart point | 48/48 vanish: ORIGIN-SATISFIABLE | 25/32 | 26/33 | 0/5 (origin excluded) |
| D residual (6 combos) | 0 id-zero | 0 | 0 | 0 |
| E soundness/back-map 2x2 | 20 piv + 30 drop vanish; 48 surv == orig | 28+38; 32 | 27+38; 33 | 35+58; 5 |

COVER: (i) 500-sample tautology PASS; (ii) Z-side HW forcing (char !=
2); (iii') REPLACED per 15.0: origin census on the RAW core at both
primes -- ZZ pattern: 0/98 rows nonzero => (x = s1 = 0, W = 0) is an
EXACT point (char-0 exact too: every x-free term is W-loaded, 15.1
census) = the 13.0-style relaxation artifact; ZU/UZ/UU patterns: rows
87-96 nonzero (the W-loaded quotient constants) -> origin excluded.
Back-maps certified by guard E in both directions => EMPTY on all
leaves <=> core EMPTY; any leaf witness lifts.

EXPLICIT WITNESS (phase witness, banked 06:08): since the UU residual
is EXACTLY c*E, the 13.4 construction ports verbatim; at BOTH banked
primes the explicit intended-chart point (p=105337: W1=32284, W2=1;
p=105673: W1=90918, W2=1; om^0 A-embedding; free x's = 0, s1 = 0;
35 UU subs back-mapped -- single back-map layer) satisfies ALL 105
emitted (1,2)-core eqs under the INDEPENDENT parser.  The (1,2)
p-screen NONEMPTY verdict is therefore explicit-point-certified
BEFORE msolve; calibration runs are confirmation only.  (Same W1
values as 13.4 -- forced: same E, same radical points.)

### 15.3 Calibration ledger + composite (1,2) verdict

Runs (msolve 0.10.1, -g 2 -t 4, timeout 900 s, local;
runs/leaf12_*.out, runs/r1_12leaves_calibrate.log):

| leaf | wfree p=105337 | wfree p=105673 | char 0 |
|---|---|---|---|
| ZZ | GB!=[1] NONEMPTY 188 s / 14.8 GB (concordant) | SKIPPED by policy | NOT RUN by policy: NONEMPTY proven by the exact origin point (15.2 cover iii'), char-0-exact |
| ZU | GB=[1] EMPTY 1 s | GB=[1] EMPTY 1 s | first-prime `[1]` trace 77 s / 7.3 GB -- **not a Qbar proof** |
| UZ | GB=[1] EMPTY 1 s | GB=[1] EMPTY 1 s | TIMEOUT 900 s / 13.5 GB -- stays evidence-tier |
| UU | NONEMPTY 1 s | NONEMPTY 1 s | NONEMPTY: 121-elt reduced GB over Q, 1 s |

CORRECTED EVIDENCE TIER: the leaf12_ZU char-0-header `[1]` is a
first-prime trace, not a proof of ZU emptiness over Qbar.  ZZ still has an
exact origin point.  The successful non-unit UU run is not affected by the
unit-specific short circuit: its 121-element basis was rationally
reconstructed and retains its Qbar-nonemptiness meaning within engine trust.
Thus ZZ and UU are decided in characteristic zero, while neither mixed-leaf
emptiness claim has an exact rational certificate.

MULTI-PRIME SWEEP (13.6 protocol, good_primes walk; same 6 fresh
primes 109537, 165313, 177409, 188833, 200257, 225961; ~1 s each):
verdict pattern IDENTICAL at all 6 -- ZU EMPTY / UZ EMPTY / UU
NONEMPTY -- and at both banked primes: 8 primes total, no exception
(strong-evidence tier per the 10.0 calibration for the char-0
readings; ZU additionally char-0-PROVEN above).

COMPOSITE VERDICT (under the 15.0 pre-registration; sec-1 discipline;
R1 per-branch):
1. ALL-FOUR-EMPTY trigger: NOT FIRED -- and PROVABLY unfireable: ZZ
   carries the exact origin point (relaxation artifact) and UU
   carries the explicit intended-chart witnesses (15.2) at both
   banked primes AND a char-0 GB.
2. DIAGNOSTIC (intended-chart) verdict: UU NONEMPTY at both primes
   and in char 0 => the (1,2) branch SURVIVES its terminal core on
   the intended chart.  Its entire discriminating content there is
   the single relation E -- THE SAME E as the minimal branch (15.1)
   -- which the intended E5 fourth-root data satisfies identically
   (13.1 identity, ports verbatim).
3. ZU/UZ EMPTY (char-0-proven on ZU): every core point has W1, W2
   both zero or both nonzero -- the same two-stratum structure as the
   minimal branch (13.3).
4. REMAINING OBLIGATIONS for the (1,2) branch (per-branch ladder):
   its own F_s band + quotient tier, R2-R5, J-closure.  MEASURED
   (06:15): the (1,2) witness back-map has the SAME nonzero support
   {tf1/2_47 (slot 35), tf1/2_52 (slot 40), s1 = 0} as the minimal
   witness, so the 15.5 mod-5 free closure applies VERBATIM to any
   slot-graded (1,2) F_s rung with slot not representable by
   {20,25,35,40} -- the (1,2) F_s ladder inherits the 15.6 staging
   plan (exact rung ledger for its 12/21-window: future work).

### 15.4 PART B -- depth-84 F_s quotient tier: structure + counts
### (sizing only; NO build, per the 15.0 scope)

Object (secs 3 C2, 8.5, 14.3): the F_s ladder's terminal tier -- the
18->8 cancellation quotient at 1/7-slot r = 10 (6-grid slot s = 60,
stage m = 72, needs series depth 84), H_F^3 = s1F S_F^4 with s1F a
fresh tie scale; row shape per 3 C2 "quotient == c * p21^8" (exact
engine formulation to be fixed at the Q0 gate with anchors, 8.4-style).
Rungs r = 5..9 (slots 30..54) are band rows (= 0); r <= 6 are
in-window at depth 54 and already DISCHARGED as witness-vacuous (14.3).

COUNTS (mechanical, from the banked grading + registry + measured
rungs; scripts inline, 2026-08-11 06:10):
- Rows: grading 12n + s == 0 (mod 42) with n in [2..377] (n = eta
  degree, set by orbit sizes 3x126 = 2x189 = 378 -- DEPTH-INDEPENDENT,
  so rows/rung stays ~54 at depth 84): slot 42: 53 rows (n == 0 mod
  7); 48: 54 (n == 3); 54: 54 (n == 6); 60 QUOTIENT: 54 (n == 2);
  66: 54 (n == 5).  Depth-84 tier proper (r = 7..10): 215 rows
  (+ 54 if r = 11 is carried; + 108 for the unemitted in-window
  r = 5, 6).
- New unknowns: registry tails at levels 37..72 (bf/bg42/bg21 from
  level 37 = slot 25; tf/tg from level 54 = slot 42) beyond the 135
  banked emitted vars: 198 (bf 36, bg42/bg21 54, tf1/tf2 44, tg 64)
  + s1F = 199.  Through r = 11 (levels <= 78): 244.
- Degrees/terms: slot-s rows carry weight-s monomials; min var slot 1
  (bf_13) => var-degree up to 60 at the quotient.  Measured terms/rung
  at SCAP 25 (14.1): 1,346 / 11,798 / 73,838 / 375,044 (r = 1..4;
  ratios 8.8, 6.3, 5.1).  Decaying-ratio extrapolation: r = 7 ~2e7,
  r = 8 ~6e7, r = 9 ~2e8, r = 10 ~6e8 exact ring terms; full tier
  ~8e8 terms ~ 30-60 GB emitted text.  SYMBOLIC emission of the tier
  is NOT feasible as one object on any tier of our hardware (and, per
  15.5-15.6, NOT NEEDED for the decisive question).

### 15.5 FREE CLOSURE FOUND: mod-5 slot obstruction (the 14.3
### slot-census argument, generalized to the whole ladder)

The banked witnesses' nonzero coordinates sit at F_s slots
{0 (leads/etale units), 20 (a_i pins), 25 (w_i pins), 35 (tf1/2_47),
40 (tf1/2_52)} (14.3 measurement) -- every nonzero slot is == 0
(mod 5).  Slots are ADDITIVE under the jet product, so for the
ZERO-EXTENDED witness (all new depth-84 tails = 0, a legitimate
extension point):
(a) any row at slot s !== 0 (mod 5) has, in EVERY term, a factor at a
    slot not in 5Z -- zero at the witness => the row vanishes
    identically there (slots 36, 42, 48, 54, 66);
(b) for s == 0 (mod 5) a term survives only if s = 20a + 25b + 35c +
    40d is solvable; mechanical scan (banked 06:10): slot 30 has NO
    representation; slot 60 has EXACTLY THREE:
    a^3 (3,0,0,0) | a * tf_52 (1,0,0,1) | w * tf_47 (0,1,1,0).
CONSEQUENCE (free closure, no depth-84 computation): every band row of
the ENTIRE remaining F_s ladder (r = 5..9 and r = 11) is identically
satisfied by the zero-extended witnesses at both banked primes.  The
band CANNOT kill the branch at the banked primes; the ONLY depth-84
object that can bite is the r = 10 quotient family -- sharpening 14.3
("first that can bite") to "the ONLY one in the ladder".  The a^3
representation is the pin-only ring-constant shape behind 14.3's
constant-bearing reading; whether its coefficients actually survive
the selector/phase aggregation (cf. the uf30 cancellation, 8.7) is a
MEASURED anchor at Q0, not assumed.

TWO STRUCTURAL BONUSES (slot-budget facts; corrected 06:20 -- note
the new vars include bf/bg42/bg21_37..53 at slots 25..41, NOT only
slot >= 42 tails):
(i) slot-60 rows have new-tail degree <= 2 (three new tails need
    slot >= 3 x 25 = 75 > 60); new tails at slots >= 42 appear only
    LINEARLY (a pair touching one needs >= 42 + 25 = 67 > 60).
(ii) at the witness (old vars frozen at their values) the
    participating new tails are EXACTLY 39 (enumerated mechanically,
    06:20): the 9 level-72 (slot-60) tails linearly with lead
    cofactors; bf/bg42/bg21_52 (slot 40, x a-pin); bf/bg42_47 (slot
    35, x w-pin); bf/bg42_37 (slot 25, x tf_47); and the slot-25..35
    band bf/bg42/bg21_37..47 through PAIRS t1 + t2 = 60.  The
    witness-restricted quotient tier is a 54-row system in <= 40
    unknowns (39 tails + s1F) of degree <= 2 over GF(p) -- msolve
    territory measured in SECONDS, no farm.

### 15.6 Staging plan, placement, kill/survive semantics

- Q0 (FIRST DECISIVE SUB-BLOCK; local, ~seconds-minutes; engine
  addition ~100 lines reusing fs_orbit_fold + a specialization hook):
  witness-specialized quotient evaluation.  Specialize each orbit
  series at the witness (P_i: slots {0,20,25,35,40}; Gp_i: {0,20,25};
  B/GB/G0: leads only, PLUS the 39 participating new tails of
  15.5(ii) carried SYMBOLICALLY), fold mod p at slot cap 61 (<= 5
  numeric slots + sparse symbolic tails per factor => small), read
  WF(n,60)|witness for the 54 n's, form the rows WF - s1F*(pattern
  c_n).  By 15.5(ii) this is a 54-row degree-<= 2 system in <= 40
  unknowns; msolve mod both banked primes (seconds) decides the
  witness family's depth-84 fate -- no farm.  Zero-extension check
  first (all 40 unknowns = 0 vs the constants) is pure evaluation.
  Anchors: specialized fold must reproduce the banked slot-35/40 jet
  values and E1/grading on the kept keys.
- Q1 (only if Q0's system is inconsistent): multi-witness sweep --
  the other A-embeddings/4th-root branches (9 x Tonelli choices,
  13.4 machinery) and fresh primes (13.6 walk); same Q0 evaluation
  per witness.  Still local.
- Q2 (only if all witnesses die): quotient-only KILL screen.
  Soundness: EMPTY(core + chart + quotient) => EMPTY(full tier)
  (adding band rows only shrinks the variety), so a kill never needs
  the band.  But symbolic slot-60 rows are ~6e8 terms => do NOT emit
  raw.  Q2 = LEAF-COMPRESSED emission: substitute the UU-leaf
  parametrization (13.1: core == E x A^38 on the chart; invertible
  back-map) into the quotient rows, re-expressing them over the ~40
  surviving directions + 199 new vars; sizing to be MEASURED first
  (gate: projected <= 10^7 terms -> box01, 16 threads; else redesign).
  ultramem reserved for a char-0 GB upgrade only if a p-kill appears
  (10.0 tier discipline).
- VERDICT SEMANTICS (pre-registered now, sec-1 discipline):
  * Q0/Q1 consistent (witness survives) => the minimal branch
    SURVIVES depth-84 at the banked primes by explicit point; the
    F_s ladder is EXHAUSTED (band 14.3/15.5, quotient by point);
    remaining obligations: R2-R5 ladder, J-closure, char-0
    confirmation per 10.0.  The branch = the campaign's strongest
    near-candidate; next build = R2 window.
  * all witnesses die AND Q2 p-screens return GB = [1] at both
    primes => the minimal branch DIES at the F_s quotient tier
    (strong-evidence tier; char-0 GB upgrades to proof).  With R6
    closed, the residue-A two-pole exclusion then rests on the
    sibling ladders ((1,2) -- now at the SAME E-core, sec 15.1-15.2
    -- plus (2,3), (2,5)) and the single-pole book of 4.
  * witnesses die but Q2 NONEMPTY => partial: the intended E5
    fourth-root data is incompatible with the depth-84 tie, but the
    relaxed locus survives; bank surviving-locus data; next
    discriminator = R2-R5 on that locus.  No inflation beyond this
    table.

### 15.7 Historical ZU/UZ char-0 claim (demoted to first-prime trace)
### + deliverables/state

Prompted by the (1,2) ZU char-0-header result (15.3), the MINIMAL branch's
banked leaves were rerun in char 0 (runs/leaf_{ZU,UZ}.ms.char0.out,
ledger runs/r1_leaves_calibrate.log): leaf_ZU.ms GB = [1] EMPTY,
leaf_UZ.ms GB = [1] EMPTY, ~1 s / <2 MB each.  **2026-08-23
correction:** both are first-machine-prime traces, so the former
evidence-tier reading remains in force.  The mixed leaves are not proved
empty over Qbar and the minimal-branch composite is not fully
characteristic-zero-decided by these runs.

DELIVERABLES (this section): engine cases/r1_12_decompose.py
(ADDITIVE; phases stats | build | emit | guards | cover | calibrate |
psweep | witness; reuses r1_decompose/r1_reduce functions; s1 carried
as x119, emitted as s1); systems/r1/leaves/leaf12_* (12 files);
runs/leaf12_*.out, runs/leaf_{ZU,UZ}.ms.char0.out, ledgers
runs/r1_12leaves_calibrate.log + r1_leaves_calibrate.log (sweep
lines); state /tmp/r1dec12 (core.pkl parse cache + leaves.pkl).
Minimal-core leaf emissions BYTE-IDENTICAL (sha256 gate, 16/16 OK).
Part B produced NO new emissions (sizing/plan only, 15.4-15.6);
depth-84 engine work starts at the Q0 gate.

## 16. Q0 gate: depth-84 slot-60 witness-specialized quotient block
## (2026-08-11)

### 16.0 Plan + pre-registration (banked BEFORE build; 15.6 semantics
### govern, no inflation)

ENGINE: cases/r1_q0_gate.py (NEW file, ADDITIVE; reuses r1_experiment
registry/build_generators at depth 84, r1_fullcore mod-p machinery
pjmul/ring_modp, r1_minimal_ext witness_point + rnorm memo).
Regression gate: sha256 of all 44 banked systems/r1 emissions taken
BEFORE any work (/tmp/q0_regression_baseline.sha); must be unchanged
after.  New emissions: systems/r1/r1_q0_p{105337,105673}.ms + .rows.txt.

CONSTRUCTION (per banked prime): depth-84 registry (reset_vars +
build_generators(84)); witness values transported by registry NAME
(banked 135 emitted vars via r1_full_core.rows.txt map + sec-14 ext
vars; radical/Tonelli data = witness_point(p), the sec-13.4 point);
every UNBANKED registry var at level <= 72 carried SYMBOLICALLY (no
hand-pruning to the 15.5(ii) 39 -- participation is MEASURED, and
matching the banked 39-count is an anchor); orbit series specialized,
folded mod p at slot cap 61 by TWO independent paths (sequential
linear-factor fold and suborbit-Newton fs_block, both mod-p ports of
the sec-14-cross-checked routines; exact dict equality per orbit
required); f = P1 P2 B, g = 6-orbit product, W_F = g^2 - f^3; rows =
WF(n,60) - s1F*c_n over the 54 slot-60 keys.  PATTERN (pre-registered):
c_n = coeff of T^((n-2)/7) in ((T-1)^2 (T-B))^8, T = eta^7, B = 3/2 --
the unique eta-shift of p21^8 compatible with the measured grading
12n + s == 0 (mod 42) at s = 60 (n == 2 mod 7); shift correctness is
anchor-checked against the measured row support.

ANCHORS (8.4-style, ALL must pass before any row is trusted; failures
stop the gate for formulation repair, banked either way):
- A1 jet regression: the specialized fold truncated to slots <= 24
  must equal the banked sec-14 fsjets.pkl f/g jets evaluated at the
  witness (per-key mod p, both primes; no symbolic content below slot
  25 -- tails live at slots >= 25).  End-to-end validation of the
  specialization hook against guard-passed banked objects, incl. the
  slot-35/40 tf jet values (the only nonzero witness tails).
- A2 E1: specialized WF slot-0 identically zero.
- A3 grading + census: all WF keys obey 12n + s == 0 (mod 42), slots
  == 0 (mod 6); slot-60 support = 54 keys, n == 2 (mod 7), n <= 377
  (15.4 count reproduced).
- A4 free closure (15.5) measured: band rows s = 30..54 have ZERO
  constant part at the witness (zero-extended witness satisfies the
  whole in-ladder band mechanically, not just by the slot argument).
- A5 participation: the set of symbolic tails occurring in the 54
  emitted rows must be EXACTLY the 15.5(ii) 39 (9 slot-60 linear;
  bf/bg42/bg21_52 x a-pin; bf/bg42_47 x w-pin; bf/bg42_37 x tf_47;
  slot-25..35 pair band), new-tail degree <= 2, slot->=42 tails linear.

Q0 SYSTEM (verdict object, fixed now): the 54 rows in the measured
unknowns (39 tails + s1F expected), emitted expanded-monomial mod-p
([0,p) coeffs, no parens), msolve -g 2 -t 4, timeout 600 s, both
banked primes.  Zero-extension pre-check (pure evaluation, banked
first): constants of all 54 rows == 0 <=> witness zero-extends with
s1F = 0; else constants proportional to c_n <=> zero-tail point with
s1F = ratio.  SURVIVE claims additionally re-verify the explicit point
against the emitted rows via the independent parser AND against the
symbolic band rows s = 30..54 of the same fold (so "survives the
TIER", not just the quotient, is certified by point).  VERDICT under
the 15.6 pre-registered table verbatim; Q1 (multi-witness Tonelli sweep)
only if Q0 inconsistent; Q2 (leaf-compressed p-screen) only if all
witnesses die.

### 16.1 Anchor table (both primes 105337/105673; identical results)

| anchor | result |
|---|---|
| A1 jet regression (slots <= 24) | PASS -- specialized fold == banked sec-14 fsjets at the witness, exact per-key (f 19, g 28 keys); no symbolic content below slot 25 |
| A1b exact-ring regression (slots <= 40; ADDED during the gate: A1 cannot see the slot-25 w-pins or slot-35/40 tf values) | PASS -- specialized fold == R1.fs_block (exact ring arithmetic, the sec-14 guard-passed engine) on the depth-84 series at cap 41, all 6 pole orbits, FULL cofactor comparison incl. symbolic tails (~20 s per 42-orbit) |
| A2 E1 | PASS -- WF slot-0 identically zero at the witness |
| A3 grading + census | PASS -- 12n+s == 0 (mod 42) on all 324 WF keys; slot-60 support = 54 keys, n == 2 (mod 7), n = 2..373 (15.4 count reproduced) |
| A4 free closure measured | PASS -- band rows s = 6..54 carry ZERO constant part at the witness (15.5 argument reproduced by direct evaluation) |
| A5 participation | PASS with a VERIFIED REFINEMENT: measured participation = 36 tails, not 39 -- bf_52/bg42_52/bg21_52 (slot-40 B-side) are BARRED by the per-orbit selector grading (a lone off-6-grid tail cannot survive its own orbit's 7-direction aggregation; its cheapest same-orbit companion, slot >= 25, overshoots cap 60; the 15.5(ii) a-pin partner sits in ANOTHER orbit, which the slot-sum enumeration missed).  Each absence proved two ways: per-orbit fold grading census + perturbation (random value for the tail leaves EVERY W_F key unchanged, both primes -- the 8.7/uf30 methodology).  Degree <= 2 and slot->=42-tail linearity confirmed.  System = 54 rows, 37 unknowns (36 tails + s1F) |
| A6 cap-67 extension | PASS -- 54 slot-66 (r = 11) rows also carry ZERO constant part at the witness (15.5(a) measured, not just argued); slot-60 rows identical between cap-61 and cap-67 builds (truncation exactness) |

Internal cross-check throughout: every orbit folded by TWO independent
mod-p paths (sequential linear-factor fold vs suborbit-Newton port of
fs_block), exact dict equality asserted per orbit at caps 61 and 67.

### 16.2 Q0 construction + the decisive measurement

Engine cases/r1_q0_gate.py (NEW, ADDITIVE; phases gate [p] | emit |
run; state /tmp/r1q0/gate_p*.pkl).  Depth-84 registry = 414 vars; 198
unbanked at levels 37..72 carried symbolically (no hand-pruning).
Witness support re-measured at load: nonzero banked vars = EXACTLY
tf1/2_47, tf1/2_52 (sec-14.3 reproduced).  Pattern c_n = coeff of
T^((n-2)/7) in ((T-1)^2(T-B))^8, B = 3/2 (eta^2-shifted p21^8, the
unique grading-compatible shift; support n = 2..170, 25 nonzero
coefficients).  Emitted: systems/r1/r1_q0_p105337.ms, _p105673.ms (54
eqs, 37 vars, 16.5 kB each, coeffs in [0,p), no parens) + .rows.txt
(row labels with per-n c_n values + var map q0..q35 -> registry names,
s1F).

DECISIVE MEASUREMENT (both primes): the constant parts of ALL 54
slot-60 quotient rows VANISH at the witness -- 0/54 nonzero.  The
15.5(b) constant-bearing candidates (a^3, a*tf_52, w*tf_47) cancel
under the selector/phase aggregation, resolving the question 15.5
explicitly left open ("MEASURED anchor at Q0, not assumed") in favor
of cancellation -- the F_s analogue of the 8.7 uf30 cancellation.
CONSEQUENCE: the zero-extended witness (all 37 unknowns = 0, s1F = 0)
satisfies the entire Q0 block by pure evaluation, BEFORE msolve.

### 16.3 Run ledger + certificates (msolve 0.10.1 local, -g 2 -t 4,
### timeout 600 s; runs/r1_q0_runs.log, .ms.out)

| run | result |
|---|---|
| r1_q0_p105337.ms (54 eqs, 37 vars) | GB != [1] NONEMPTY, wall 1.0 s, RSS 1.1 MB; reduced GB = 4 elements: [s1F, one linear, two quadratics] |
| r1_q0_p105673.ms | GB != [1] NONEMPTY, wall 1.0 s, RSS 0.6 MB; same 4-element shape |

Certificates beyond the GB (both primes):
- explicit point: all-37-zero satisfies 54/54 EMITTED rows via the
  independent parser (FC.parse_eval on the .ms files);
- residual guard: 0 identically-zero rows (3 random points/prime);
- tier point-certificate: the same zero-extension satisfies every
  depth-84 band row -- s = 30..54 by A4 and s = 66 by A6 (measured
  constants, not only the 15.5 slot argument), s <= 24 banked in 14.3;
- regression gate: 44/44 prior systems/r1 emissions byte-identical
  (sha256 vs the pre-work baseline).
Structural finding (banked): the reduced GB contains s1F itself, so
s1F == 0 on the ENTIRE Q0 variety -- the depth-84 tie closes with
H_F = 0 on the witness family (codim 4 in the 37 unknowns, origin
included); the tie scale is not a free direction there.

### 16.4 VERDICT (15.6 pre-registered table, first row; no inflation)

Q0 witnesses CONSISTENT at BOTH banked primes -- by explicit point
(zero-extension), confirmed by msolve GB != [1].  Q1 does not fire
(pre-registered trigger: Q0 inconsistent).  Q2 not built
(pre-registered trigger: all witnesses die).  Therefore:
- the minimal branch SURVIVES depth-84 at p = 105337 and 105673 by
  explicit point: the sec-13.4 witnesses, zero-extended to the 198
  depth-84 tails with s1F = 0, satisfy the quotient tier (this
  section) and every band rung r = 5..9, 11 (A4/A6 measured + 15.5);
- the F_s ladder is EXHAUSTED: in-window band r <= 6 (14.3), deferred
  band r = 5..9, 11 (15.5 + A4/A6), quotient r = 10 (Q0, by point);
  no F_s tier remains that could bite these witnesses at the banked
  primes;
- the minimal branch remains the campaign's strongest near-candidate;
  remaining obligations, unchanged from 15.6: (i) R2-R5 ladder --
  next build = R2 window (16.5); (ii) J-closure; (iii) char-0
  confirmation per the 10.0 tier discipline (the witness certificate
  is mod-p; char-0 F_s status stays OPEN pending box01 + the
  J-closure program).

### 16.5 Next-tier spec: the R2 window build (one paragraph, banked)

R2 (template-lift residual ledger, notes night-7; LT-REVIEW
sequencing item (c); sec-5 item 3) = the x-side h-Newton budgets with
the LROOT LR2 pin merged -- the one data side the entire y-side
program (secs 3-16) has never modeled, and the prerequisite for
expressing the J(f,g) closure (R5), which sec 4 records as
"NOT expressible from y-side data alone".  The R2 window build needs:
(1) an x-side data model mirroring the y-side orbit model -- the
single x-cluster at x0 = 0 with lead pin A_126 = S_R x^42, S_R = G_R
= 1 (LR2, gauges already banked in 3.0), kappa_G = 1, unsplit below
R = 3, with x-side dead-stretch/tail unknowns appended to the
registry in level order; (2) the h-Newton budget conditions (the
h1 ~ f^{4/3} approximate-root tower (2,3)->(3,4), h1-corner (168,56))
staged as window rows co-graded with the banked y-side core, x-side
analogue of the C2 bands, lowest stages first; (3) the Q0
witness-specialization hook UNCHANGED (banked vars by name, unbanked
tails symbolic, zero-extension evaluated first), with 8.4-style
anchors: x-side stage-0 lead identities (LR2 slope law, kappa_G = 1)
+ regression of any shared y-side keys against the banked jets;
(4) a 15.6-style kill/survive pre-registration banked BEFORE the
build (future sec 17).  Sizing expectation: one 42-series window,
O(10^2) rows/stage, local; the merge then unlocks the J(f,g) row
family for R5.

### 16.6 Deliverables + state

Engine cases/r1_q0_gate.py (NEW file, ADDITIVE; no prior file
touched; phases gate [p] | emit | run | all; ~470 lines: mod-p
two-path fold + witness specialization hook + anchors A1-A6 + emit +
msolve driver).  Emissions systems/r1/r1_q0_p105337.ms,
r1_q0_p105673.ms + .rows.txt (var maps: q0..q35 = the 36 measured
tails bf/bg42/bg21_37..47-band, bf/bg42_47, bf/bg42_37, 9 level-72
tails, + s1F).  Runs runs/r1_q0_p*.ms.out + runs/r1_q0_runs.log.
State /tmp/r1q0/gate_p*.pkl (rows, pattern, symbolic census, band
rows s = 30..54 in symbolic form for future reuse).  Regression gate
44/44 prior emissions byte-identical (sha256, baseline
/tmp/q0_regression_baseline.sha).

## 17. RETRACTION of the §16 survival verdict (SHEET6-R1-LADDER-REVIEW.md)

The §16 "survives depth-84 / F_s ladder exhausted" reading is REFUTED
(review front 2): the witness has s1F = 0, but its own w != 0 data pins
a nonzero H_M via the (relaxation-dropped) E5/E6 tie, forcing s1F != 0
on any template-conform extension. Adjoining s1F*t - 1 (Rabinowitsch)
gives GB = [1] at BOTH primes: correctly read, Q0 KILLS the
intended-locus witness family at depth 84 mod p (strong-evidence tier).
The same s1 = 0 artifact affects the (1,2) witness (§15). All ladder
computations were CONFIRMED clean (fronts 1,3,4,6); the error was
interpretive — the ZZ-leaf lesson repeating one level up, as the review
was designed to catch. Standing rule: every verdict object must
SATURATE all template-forced-nonzero scales (Rabinowitsch rows baked
in) and carry the deferred tie rows; anchors must include a
pattern-positive test (front 5 weakness).

## 18. SATURATED rebuild of the two-pole branch verdicts (2026-08-11,
## per SHEET6-R1-LADDER-REVIEW R2 mandates 1-4)

Engines: cases/r1_q0_gate.py EXTENDED ADDITIVELY (phases satemit |
satrun | a7 | a7pert | fam | famemit | famrun | famctl; nothing above
the sec-16 code changed -- original `emit` re-run reproduces
r1_q0_p*.ms BYTE-IDENTICALLY) + cases/r1_12_sat.py (NEW; phases
e5port | emit | run | minsat).  Regression gate: 82/82 pre-existing
systems/r1 emissions byte-identical (sha256, /tmp/r18_baseline.sha,
checked before AND after).  msolve 0.10.1, -g 2 -t 4, timeboxed
1200 s (every run below finished in ~1 s).

### 18.0 Scale inventory (mandate 1): every template-forced-nonzero
### scale, from the genome (TEMPLATE 1b/2c), with dispositions

Gauged to explicit nonzero constants (sec 3.0; no saturation needed --
they never appear as unknowns): sigma = 6, A = 1, s0 = 1, S_R = G_R =
1, S_F = 1, B = 3/2, b = 4, b2 = 9/2; c0 drops out of every emitted
row (y-translation covariance, asserted at stage 0).  Determined
nonzero by gauges + E6 unit transports (enter rows only as explicit
nonzero ring constants): G_F (G_F^2 = s0 S_F^3 = 1), S_M = 7^12/2^6,
G_M = -7^18/2^9, lam_i, m_i (pole leads, unit multiples of S_M/G_M
powers; m_i^2 = s0 lam_i^3 automatic).  Etale generators r3, z, A1,
A2, EB: nonzero on the whole radical variety (their minimal polys
r3^2 = 3, A_i^3 = 3 -+ r3 != 0, 2EB^7 = 3, Phi42(z) have no zero
root); no Rabinowitsch row needed -- justification: a zero value
would contradict the minimal-poly row at any point, char != 2,3,7.

FORCED-NONZERO scales that DO appear as unknowns in verdict objects:
| scale | where forced nonzero (genome) | verdict-object handling |
|---|---|---|
| w_1, w_2 (= W_i) | TEMPLATE 2c-E5: w_i^4 pinned nonzero (a_i != b); stage-0 gate r1_experiment.py:1032 | uW_i*W_i - 1 rows (UU chart) -- present in every sec-18 system |
| HW_i | HW_i^2 = (3/2)W_i^2, so nonzero IFF W_i nonzero | automatic from uW rows (char != 2,3) |
| H_M (G_m h1-lead) | 1b: lead of forced-degree pattern p_h1,Gm (deg 16); E5 pins it against w_i^4 | RESTORED as variable HM + E5 rows; nonzero automatic from uW + E5 (and from E6 tie + s1F-saturation) |
| H_F = s1F (F_s quotient lead) | 1b: H_F^3 = s1 S_F^4, lead of p_h1,Fs (deg 168); tower alive at F_s (2c-E2) | s1F*tSAT - 1 row + E6 cube tie 2^24 HM^3 = 7^48 s1F^3.  NAMING FIX (review nit 5): s1F is the LEAD (linear); the cube-tie scale is s1 = H_F^3/S_F^4 -- fixed in all sec-18 rows.txt |
| s1 (minimal tower constant) | Prop 4.2: tower constant of h2 = h1^3 - s1 f^4; = H_F^3 under the gauges | equivalent to s1F != 0 (cube); covered by the s1F saturation |
| s1 ((1,2) tie scale) | Prop 4.2(iii) at k1 = 1: h1+ = s1(f+)^2; review front 2 consequence 4 | s1*t12 - 1 row + the E5-12 port rows (18.2) |
| s1, cL ((2,5) ext) | its level-2 tie + level-1 quotient lead | ALREADY saturated in the banked ext (eq21 = s1*t1 - 1; eq20 ties cL^2 to s1) -- no correction needed |
| new band/quotient TAILS (36 q's; dead-stretch coeffs) | NOT forced -- free template parameters (1c; review front 2, consequence 1) | carried free, no saturation row (justified) |

### 18.1 MINIMAL branch: the Q0 chain under saturation (mandate 3a)
### + the deferred tie rows (mandate 2)

Q0-SAT (witness-specialized): systems/r1/r1_q0_sat_p{105337,105673}.ms
= the banked 54 Q0 rows VERBATIM + the two E5-quartic rows with HM
restored (4(a_i-b)HM + 729 S_M^3 (a1-a2)^4 a_i^2 alpha_i W_i^4 = 0;
review-verified formula -- the E5-pinned HM = 71495 / 19010
reproduces the review's front-2 values, pole-consistent, NONZERO) +
the E6 cube tie + s1F*tSAT-1.

FAMILY OBJECT (Q1 subsumed; char-0 leg): systems/r1/r1_q0_fam.ms
(+ _p*.ms) -- the SAME quotient tier rebuilt by EXACT-RING fold over
the whole sec-13.4 witness family: free x = 0 section, W1/W2/HW/uW
SYMBOLIC on relation E, radicals as variables => EVERY 4th-root
branch, Tonelli choice and A-embedding is covered at once (this is
Q1's sweep, made exhaustive).  Build: symbolic back-map of the banked
UU + sec-10 substitution chains at free-x = 0 over the exact ring
(support EXACTLY {tf1/2_42, tf1/2_47, tf1/2_52, tg1/2_42}; the
slot-30 values are E-multiples -- zero AT the banked witnesses but
NOT identically: the mod-p gate could not see them, the family build
carries them); fs_block exact folds at cap 61 (~35 s total); anchors:
E1 slot-0 identically zero IN THE RING, grading, occ == gate occ
(36), and the decisive REGRESSION: the exact family rows reduce mod p
at the banked witnesses to the banked gate rows EXACTLY (54/54, both
primes).

| run | verdict |
|---|---|
| r1_q0_sat_p105337.ms (58 eqs, 39 vars) | **GB = [1] EMPTY**, 1 s |
| r1_q0_sat_p105673.ms | **GB = [1] EMPTY**, 1 s |
| r1_q0_fam_p105337.ms / _p105673.ms (68 eqs, 50 vars) | **GB = [1] EMPTY**, 1 s each |
| r1_q0_fam.ms **CHAR-0 HEADER** | first-prime **GB = [1]** trace, 1 s; no Q certificate |
| ctlA = relaxed family (no tie/sat rows), char 0 | GB != [1] NONEMPTY (the relaxed survival is real, family-wide) |
| ctlB = saturation only (no E5/E6 rows), char-0 header | first-prime GB = [1] trace -- supports the finite-field finding only; **no Q-level forcing certificate** |
| r1_minsat.ms = leaf_UU + E5(HM) + HM*tH-1, char 0 | GB != [1] NONEMPTY -- core-level saturation does NOT kill the minimal branch (the 13.1 consistency identity is real) |

CORRECTED VERDICT (minimal branch, sec-1 + 15.6 semantics with the saturation
standing rule): the intended-locus witness family is killed at the F_s
quotient tier at both banked primes.  The characteristic-zero-header `[1]`
runs do not upgrade that result over Qbar.  The modular mechanism is exactly
the review's: the quotient rows force s1F = 0 over the recorded finite fields,
while E5+E6 force s1F != 0 at any w != 0 point.  SCOPE: this is the free-x = 0 section
of the UU core (the pre-registered Q0/Q1 object).  Q2 -- the
quotient screen over the FULL UU locus (free-x directions open) --
remains the residual object for an unconditional branch kill at this
tier; its leaf-compressed sizing plan (15.6) stands, WITH the
saturation rows now mandatory.

### 18.2 (1,2) branch: core-level saturated verdict (mandates 3b, 2, 5)

The banked (1,2) survival rests on a witness with s1 = 0; the
template forces s1 != 0.  Saturation alone does NOT kill it (s1 is
free on the UU chart -- controls below), so the honest verdict needs
the dropped tie: the E5-QUARTIC PORT for the k1 = 1 tower
(cases/r1_12_sat.py e5port, exact K3): at G_m the (1,2) legality is
h1+ = s1(f+)^2, so p_h1,Gm = s1 S_M^2 P^4 (mult 4 at c_i); the St
3.9(ii) merge-edge transport against the branch-independent pole
pattern -(3/4)s0 lam_i^3 w_i^4 (eta^2 - (4/3)w_i^2) gives

    81 * S_M * a_i * alpha_i * W_i^4 + s1 = 0        (i = 1, 2),

the identity closing EXACTLY at (a1-a2)^2 = 12 with no slack.
METHOD VALIDATION (banked, exact): the same pipeline on the minimal
branch reproduces the 13.1 bracket sum (9+-5r3)(a_i-b)/a_i^2 == 0
IDENTICALLY, and the row constant 243*7^12 = 3363432789843 is
exactly the content factor the (1,2) core's own row 87 carries
(15.1) -- two independent corroborations.  The (1,2) bracket is
sum (9+-5r3)/a_i == 4 != 0: relation E (the (1,2) core's entire UU
residual) and the E5-12 rows are JOINTLY inconsistent at ANY s1 != 0
-- and on the UU chart the tie itself forces s1 != 0 (W_i units).

| run (r1_12sat*) | verdict |
|---|---|
| r1_12sat.ms = leaf12_UU + E5-12 + s1*t12-1, **CHAR-0 HEADER** | first-prime **GB = [1]** trace, 1 s; no Q certificate |
| r1_12sat_p105337.ms / _p105673.ms (wfree) | **GB = [1] EMPTY**, 1 s each |
| r1_12sat_ctl_p*.ms (saturation, NO tie rows) | GB != [1] NONEMPTY both primes (the kill is the TIE, not the chart/saturation) |

HISTORICAL VERDICT ((1,2) branch): this claimed a characteristic-zero
terminal-core kill from the printed `[1]` and the ZU/UZ traces.  It has no
rational certificate and, more decisively, was retracted in §19.3 because the
E5-12 transport premise has a level slip.  CONTINGENCY as originally stated:
the kill rests on the E5-12 transport port derived THIS session
(unreviewed); it is validated against the review-confirmed minimal
chain at every shared step, but an adversarial check of the k1 = 1
transport (one Taylor-coefficient computation) is the single point
of failure and should be on the next review's front sheet.

### 18.3 (2,5) advisory (mandate 3c; box01 decider NOT touched)

r1_25chain_ext carries its tie scales HONESTLY (s1 saturated by
eq21 = s1*t1-1; cL tied to s1 by eq20): no correction needed there.
EXPOSURE FOUND: W1/HW1/W2/HW2 are free variables (70 of 134 rows
W-loaded, wfree header has NO uW rows) and the E5 quartic for its
chain reading is not emitted -- the SAME W_i = 0 relaxation the
review flagged.  Consequence for the running decider:
- EMPTY at both primes: VALID AS-IS (saturation only shrinks the
  variety; the kill would stand a fortiori) -- no re-run needed.
- NONEMPTY: NOT branch-diagnostic until re-run with uW_i rows + the
  (2,5)-ported E5 quartic (its own G_m h1-lead transport, to be
  derived as in 18.2); any witness must be checked for W_i != 0 and
  tie-conformance before a survival is claimed.

### 18.4 Anchor upgrade A7 (mandate 4) + engine/state ledger

A7 (phases a7 | a7pert; runs on the banked gate state, both primes):
(a) VALUE -- every c_n equals the coefficient of T^((n-2)/7) in
((T-1)^2(T-B))^8 recomputed by an INDEPENDENT binomial-expansion +
Fraction-convolution path; (b) ALIGNMENT -- support = {7m+2} =
2..170, c_2 = B^8, monic top c_170 = 1, min index == min MEASURED
WF slot-60 support; (c) POSITIVITY -- the T-polynomial assembled
from the EMITTED c_n has roots of multiplicity EXACTLY 16 at T = A
and EXACTLY 8 at T = B (synthetic division), deg 24, and the
condition matrix has corank exactly 1 (Fraction rank 24 of 25), so
c_n is THE Prop-8.1 quotient pattern up to scale.  Deliberate
perturbations (review front-5 suite: B -> -3/2, index shift n -> n+7,
global sign flip, single-coefficient corruption): ALL CAUGHT (banked
a7pert output); a FORMULATION-level wrong-B (reference sharing the
error) is caught by (c) alone, since the root data comes from the
independently-banked template constants.

New emissions (systems/r1/): r1_q0_sat_p*.ms + rows.txt,
r1_q0_fam.ms + _p*.ms + rows.txt, r1_12sat.ms + rows.txt +
_p*.ms + _ctl_p*.ms, r1_minsat.ms.  Runs: runs/r1_q0_sat_runs.log,
r1_q0_fam_runs.log (+ ctlA/ctlB outs), r1_12sat_runs.log,
r1_minsat_runs.log + .ms.out files.  State: /tmp/r1q0/fam.pkl.
Engines: r1_q0_gate.py (+~420 lines, additive), r1_12_sat.py (new).
Prior emissions: 82/82 byte-identical; original phases re-run
byte-identically.

### 18.5 The net two-pole picture under the standing rule

| branch | core level (saturated) | depth-84 / ext tier | status |
|---|---|---|---|
| minimal (3,4) | survives (r1_minsat NONEMPTY; 13.1 identity) | witness-family KILL, char 0 + 2p (18.1) | DEAD on the entire banked witness family; residual: Q2 full-locus quotient screen (saturated), then R2-R5/J only if something survives it |
| (1,2) | **DEAD, char 0 + 2p (18.2)** | not needed | DEAD at core (E5-12 port contingency noted) |
| (2,3) | chain core queued (sec 11) | -- | untouched this session; same saturation advisory as (2,5) applies to any future ext build |
| (2,5) | core NONEMPTY (sec 11) | ext decider running on box01 | advisory 18.3: EMPTY valid as-is; NONEMPTY needs saturated re-run |

The residue-A two-pole configuration now rests on: the minimal
branch's Q2 residual object, and the two chain branches' deciders --
with the saturation standing rule (17) binding on all three.

## 19. Q2: the full-locus depth-84 screen + the E5-port review fallout
## (2026-08-11; review half in SHEET6-R1-Q2E5.md)

### 19.0 Pre-registration (banked BEFORE the Q2 runs; 15.6 semantics
### + sec-17 saturation rule govern; no inflation)

Object (engine cases/r1_q2_screen.py, NEW, ADDITIVE): per banked prime,
the UU-chart depth-84 slot-60 quotient screen with W1/W2 SYMBOLIC
(Laurent W-part canonical mod the quadrics, uW_i chart rows, relation
E) and the free core directions OPEN above a stratum cutoff: free
core vars at slot < LCUT are 0, at slot >= LCUT symbolic; LCUT = 1 is
the FULL UU chart.  Rows: quadrics + uW + E + 3 defining rows
(bf_18/24/30 kept as variables carrying their composed back-map
polynomials -- the 15.6 "leaf-compressed" substitution, redesigned
after MEASUREMENT showed raw substitution EXPANDS the fold; review
sec 3) + quotient rows WF(n,60) - s1F*c_n for n <= 44 + E5-quartic
(HM restored, W symbolic) + E6 cube tie + s1F*tSAT-1.  Etale radicals
at the banked point (wfree methodology).  SOUNDNESS of the two
restrictions, pre-registered: (a) row subset: ideal(subset) c
ideal(full tier), so V(subset) contains V(full tier) and EMPTY(subset)
=> EMPTY(full tier) -- valid for KILLS only; the n <= 44 subset is
MEASURED sufficient on the banked family object (7 rows kill it;
n <= 16 does not; probes banked).  (b) stratum: EMPTY at cutoff L
kills every UU-chart point whose free dead-stretch/tail coefficients
below slot L vanish; the FULL kill needs L = 1.  VERDICT TABLE:
- EMPTY at both primes at LCUT = 1 => the ENTIRE minimal-branch UU
  chart dies at the F_s quotient tier depth 84 (strong-evidence tier;
  char-0 upgrade = ultramem candidate per 10.0).
- EMPTY at both primes at LCUT = L > 1 only => partial: every
  depth-84 survivor needs a nonzero free coefficient at slot < L;
  bank the surviving-locus characterization; full object ships per
  the sizing table.
- NONEMPTY at some prime => the relaxed-full-locus screen survives
  there; characterize vs the killed family (which frees/tails load
  the survivor; is s1F != 0 attainable); NOT a branch survival claim
  (band rows s = 30..54 and rows n > 44 not imposed).
- Controls: ctlA (no tie/sat) MUST be NONEMPTY (the killed family's
  zero-extension lives on it -- emission sanity); ctlB (sat only,
  no tie) EMPTY iff s1F == 0 is forced on the whole stratum (the
  16.3/18.1 mechanism's reach).
Anchors gating trust: A-Q2-1 (witness specialization == banked gate
rows EXACTLY), A-Q2-2 (free-x = 0, W SYMBOLIC == banked exact fam
rows mod p), E1 slot-0, grading, two-path fold equality, A7 pattern
suite, and phase pert (deliberate value-corruption + slot-shift
perturbations must be CAUGHT by the anchors) -- all PASS required
before any run is read.

### 19.1 Sizing measurements (the 15.6 gate, exercised mechanically)
### + anchor/perturbation record

Back-map measurement (the review's design audit, Q2E5 sec 3): the 35
banked UU+sec-10 substitutions composed symbolically over the 84 free
directions give values of 1-3 terms EXCEPT bf_18/bf_24/bf_30 (24/348/
3552 terms, x-degree 4/12/18, at slots 6/12/18) -- raw substitution
would EXPAND the fold (bf_30^3 alone reaches slot 54), so the three
deep values ride as VARIABLES with defining rows (their restrictions
to each stratum; sizes logged per lcut).  Fold sizes at p = 105337
(cap 61, eta-degree cap 44, W symbolic, two-path-verified):

| lcut (free slots open) | quotient-row terms (7 rows) | build wall |
|---|---|---|
| 26 | 1,879 | 9 s |
| 19 | 2,295 | 12 s |
| 13 | 5,139 | 22 s |
| 8 | 34,739 | 94 s |
| 4 | (sec 19.2) | |
| 1 = FULL locus | (sec 19.2) | |

All builds pass E1 slot-0, grading, and the 7 rows n = 2..44 are all
nonvacuous.  ANCHOR RECORD (lcut = 13, p = 105337): A-Q2-1 witness
regression PASS (Q2 rows specialize to the banked gate rows EXACTLY,
key-for-key); A-Q2-2 family regression PASS (free-x = 0 rows with W
SYMBOLIC == the banked exact-ring fam rows mod p, key-for-key -- the
W-symbolic path validated against the char-0-proven family object);
two-path fold equality PASS on all 9 orbits; A7 pattern suite re-run
at both primes, all 4 deliberate pattern perturbations CAUGHT; phase
pert: 2/2 deliberate BUILD perturbations (value corruption tf1_42;
slot shift 47->48) CAUGHT by A-Q2-1 (the front-5 upgrade discharged
at formulation level).  Row-subset sufficiency probes banked
(/tmp/q2e5_review/fam_sub_*.ms + .out): fam + rows n<=44 GB=[1],
n<=16 NONEMPTY, n>170 NONEMPTY, all 54 GB=[1].

### 19.3 RETRACTION of the 18.2 (1,2) core kill (SHEET6-R1-Q2E5.md
### review, front: the E5-12 port)

The 18.2 contingency fired: the k1 = 1 E5-quartic port is WRONG -- a
LEVEL SLIP, mechanically pinned (review sec 1; /tmp/q2e5_review/
e5_12_review.py, both primes).  The port applied the St 3.9(ii) lead
transport to h1 across the merge edge with pattern mult 4, but 3.9(ii)
presupposes the 3.9(i) count equality, which FAILS there (deg
p_h1,P_i = 2 < 4; the pole pattern is (2,3)-branch-local); the
d-arithmetic (St 3.9(iii), 5 steps at 1/42) lands the mult-4
transported content at level 4/42 = 2 d_f@P -- it is s1*(f+)^2 pole
content, the k1 = 1 legality ONE LEVEL BELOW the pole top 6/42 the
port equated it to.  Equating content at different levels produced
the spurious s1-row and the spurious kill.  R6 4.3 had this right all
along: "NO exclusion exists in print; the condition is an R1-tier
series constraint" (it constrains s1 against pole TAIL data -- a
depth-tier row family for the (1,2) ladder, not a core row).  The
count-EXACT transport at the (1,2) pole edge is the FIRST DEAD MEMBER
h2 = h1 - s1 f^2 (P q pattern, deg 16, mult 2 = deg, lands 6/42
EXACT): its row is the minimal-branch E5 row with H_M -> H12, and its
E-bracket is the 13.1 identity == 0.  CORRECTED OBJECTS
(cases/r1_12_sat.py phase corr; r1_12sat_corr.ms + _p*.ms):

| run | verdict |
|---|---|
| r1_12sat_corr.ms = leaf12_UU + E5-12corr(H12) + H12*tH12-1 + s1*t12-1, CHAR 0 | GB != [1] NONEMPTY, 1 s |
| r1_12sat_corr_p105337 / _p105673 | GB != [1] NONEMPTY, 1 s each |

RESTATED (1,2) VERDICT: the branch SURVIVES its terminal core under
saturation with the corrected tie (exact mirror of r1_minsat; s1
occurs in NO core row -- its saturation is vacuous there, banked
openly).  Its remaining obligations are the 15.3 list (own F_s
band/quotient tier -- where the level-4/42 s1-condition lives --
R2-R5, J-closure).  The banked r1_12sat*.ms kill files are RETRACTED
as verdict objects (historical artifacts of the wrong rows).  The
prior 18.2 "method validation" validated the pipeline only in the
count-exact regime; the review culture's one-slip-per-layer streak
continues: ZZ leaf (13.0), Q0 s1F (17), E5-12 port (here) -- all
three are constraints attached to the WRONG OBJECT.

### 19.2 Q2 verdicts (runs ledger runs/r1_q2_runs.log; engine
### cases/r1_q2_screen.py; emissions systems/r1/r1_q2_*)

Stratum coverage: lcut = 13 opens 54/84 free directions (all slots
>= 13) + W-pair symbolic + 36-tail budget + ext-16 + fresh depth-84
tails; lcut = 8 opens 67/84; lcut = 4 opens 77/84 (only bf_13/14/15,
bg42_13/14/15, bg21_14 -- slots 1..3 -- zeroed); lcut = 1 = the FULL
UU chart (84/84).

| object (19 eqs each + controls) | p=105337 | p=105673 |
|---|---|---|
| r1_q2_l13 (146 vars, 130 kB) | **GB=[1] EMPTY**, 1 s | **GB=[1] EMPTY**, 1 s |
| r1_q2_l13_ctlA_relaxed | NONEMPTY by EXPLICIT POINT (witness zero-extension, independent parser, 19/19 rows vanish) | (same certificate) |
| r1_q2_l13_ctlB_satonly | **GB=[1] EMPTY**, 1 s | **GB=[1] EMPTY**, 1 s |

ctlB reading (pre-registered semantics): sat-only EMPTY at both primes
= s1F == 0 is FORCED on the whole lcut=13 stratum by the quotient rows
alone (no tie needed) -- the 16.3/18.1 mechanism reaches the stratum.
Note ideal(ctlB) c ideal(main), so ctlB EMPTY also re-derives the main
kill a fortiori.  CORRECTION (resume audit): the ctlA relaxed object
has 15 rows (19 minus E5 x2/E6/SAT), so the certificate is 15/15 rows
vanishing, not 19/19; re-verified by a fresh independent-parser run
(/tmp/r1q2/ctl_cert.py, both primes; bf_18/24/30 solved from their
truncated defining rows -- all 0 on the stratum -- and s1F = 0, i.e.
the zero-extension lies on the relaxed locus with the quotient scale
OFF, matching ctlB's s1F == 0 forcing).  [Dedupe note, concurrent-
session merge: the ctlB row above is the single banked copy; the l8
verdicts live in the l8 tier table below -- the "msolve crash" reading
of the 0-byte p105673 out is superseded there (the process was killed
externally in resume cleanup, then re-run t12: TIMEOUT).]

ctlB EMPTY at BOTH primes = **s1F == 0 is FORCED on the entire
54-direction stratum variety** (quotient subset + chart alone, no tie
rows): the 16.3/18.1 witness-family mechanism extends verbatim to
every UU-chart point with free support in slots >= 13.  With the E5/E6
tie + saturation, the whole stratum DIES -- the l13 EMPTY rows.  ctlA
(relaxed) is NONEMPTY by EXPLICIT POINT at both primes (independent
parser; the ctlA GB runs timed out / were killed -- annotated in the
ledger); mechanism check on the EMITTED file: at the witness
zero-extension exactly rows {E5 x2, SAT} fail, all 16 others vanish.

SIZING TABLE COMPLETED (phase sz, banked /tmp/r1q2/sizing.pkl + log):
lcut 26/19/13/8: rows 1,879 / 2,295 / 5,139 / 34,739 terms (9/12/22/94
s); lcut 4: 960,688 terms (1,279 s; jets f 345,891 + g 1,142,214);
lcut 1 (FULL locus): **SIZING ABORT -- block B alone exceeds the 2e7
budget** (1,499 s in; the banked ~6e8 raw estimate confirmed in
kind).  The 15.6 gate verdict: lcut <= 4 runs and the lcut = 1 build
are BOX01/ULTRAMEM objects (compiled or higher-budget fold + >= 32 GB
msolve headroom; the l8 local attempt cost 14.5 GB before timeout).
State shipped: /tmp/r1q2/build_p*_l{13,12,8}.pkl + sizing.pkl; the
engine rebuilds any stratum deterministically (phase build L).

lcut = 8 tier record (resume leg; 67/84 free directions, 175 vars,
1.10 MB, quotient rows 34,739 terms).  Build + anchors at BOTH primes:
A-Q2-1, A-Q2-2, E1 slot-0, grading, two-path fold equality all PASS
(/tmp/r1q2/l8.log).  ctlA_relaxed: NONEMPTY by EXPLICIT POINT at both
primes (ctl_cert.py: witness zero-extension on the stratum, 15/15 rows
vanish, s1F = 0, bf_18/24/30 = 0 forced by the truncated defining
rows) + corroborated by an actual GB != [1] at p = 105337, 37 s.

| l8 object | p=105337 | p=105673 |
|---|---|---|
| r1_q2_l8 (main, t12 re-run) | TIMEOUT 1200 s / 12.0 GB (t12; t4 first pass 14.4 GB) | TIMEOUT 1200 s / 5.2 GB (t12) |
| r1_q2_l8_ctlB_satonly | TIMEOUT 1200 s (t4) | not run (harness chain died post-p105337; symmetric wall expected; box01 queue) |
| r1_q2_l8_sub16 (rows n<=16 only; kill-sound subset) | TIMEOUT 1200 s / 6.8 GB | not run (p105337 wall settles it) |

l8 tier verdict: UNRESOLVED at the 1200 s local budget -- main (t4 +
t12), ctlB, AND the 3-quotient-row kill-sound subset (n <= 16, 13.7k
terms) all wall out, so the l12/l13 GB cliff is NOT a row-mass
artifact: the obstruction is the opened slot-8..12 directions
themselves.  Subset probes sub16/23/30 are emitted at both primes
(systems/r1) for the box01 queue.  No verdict claim at l8 beyond ctlA
NONEMPTY (explicit point); l13 is the deepest stratum resolved at the
recorded finite fields, while its characteristic-zero status is open.

FRONTIER MEASUREMENT (l12 = stratum with uf24 + the slot-12
directions added; emissions r1_q2_l12_p*.ms banked, anchors PASS):
r1_q2_l12_p105337.ms TIMEOUT 1200 s / 6.6 GB; p105673 SYMMETRIC
(TIMEOUT 1200 s / 6.1 GB, landed in-session); further box01-tier
ledger lines append to runs/r1_q2_runs.log as they finish.  The local GB-resolution cliff sits EXACTLY between stratum
13 (GB = [1] in 1 s at both primes) and stratum 12; l8 timed out at
-t 4 AND at the -t 12 retry (12 GB).  Strata 12/8 emissions are
banked and queued for box01 (>= 64 GB / long timebox); stratum 4 is
now BUILT + emitted (below); stratum 1 alone still needs the
higher-budget BUILD (sizing table above).

lcut = 4 tier record (77/84 free directions -- only bf_13/14/15,
bg42_13/14/15, bg21_14 at slots 1..3 zeroed; 198 vars, 43.5 MB,
quotient rows 960,682 terms).  Build + anchors at BOTH primes: A-Q2-1,
A-Q2-2, E1 slot-0, grading, two-path fold equality all PASS
(/tmp/r1q2/l4_build_p*.log); build pickles + emissions + ctl objects
banked (systems/r1/r1_q2_l4_*).  ctlA_relaxed: NONEMPTY by EXPLICIT
POINT at both primes (ctl_cert.py: 15/15 rows vanish, s1F = 0,
bf_18/24/30 = 0).

| l4 object | p=105337 | p=105673 |
|---|---|---|
| r1_q2_l4 (main, t12) | TIMEOUT 1200 s / 15.4 GB | TIMEOUT 1200 s / 14.1 GB |
| r1_q2_l4_ctlB_satonly | not run locally (l12/l8 wall governs a fortiori; emitted for box01) | (same) |

l4 tier verdict: UNRESOLVED at the 1200 s local budget (expected from
the l12 cliff); the tier's value is the BANKED BUILD -- the fold, the
anchors, and the 43.5 MB emissions ship box01-ready, so the deep-
strata queue is now l12/l8/l4 emitted + l1 build-gated.

### 19.4 The net G_m two-pole picture (supersedes 18.5)

| branch | core level (saturated) | depth-84 tier | status |
|---|---|---|---|
| minimal (3,4) | survives (r1_minsat NONEMPTY; 13.1 identity) | witness-family and UU-chart slots>=13 kills at the recorded primes; the char-0-header family/l13 traces are not Q certificates | modularly dead on every UU-chart locus so far reached; characteristic-zero status open; residual = strata 12/8/4 (emitted, box01) and 1 (build-gated) |
| (1,2) | **ALIVE at core** (19.3 retraction; r1_12sat_corr NONEMPTY char 0 + 2p) | not built (its own per-branch ladder; the k1=1 s1-tie is a series-tier row at pole level 4/42) | 18.2 kill RETRACTED; obligations = 15.3 list |
| (2,3) | chain core queued (sec 11) | -- | untouched; 18.3-style saturation advisory binds |
| (2,5) | core NONEMPTY (sec 11) | ext decider on box01 | advisory 18.3 unchanged |

The residue-A two-pole exclusion now rests on: the minimal branch's
deep-strata Q2 residue (box01 queue) + its R2-R5/J ladder on anything
that survives; the REOPENED (1,2) branch's own series ladder; and the
two chain deciders.  Standing rules in force: sec-17 saturation, the
  19.2 ledger-hygiene rule (0-byte .out != NONEMPTY), the 2026-08-23
  evidence correction (char-0-header `-g` output is first-prime trace), and the Q2E5
lesson -- St 3.9(ii) transports require the 3.9(i) count equality,
checked per member per edge.  NEXT BUILD (banked directive): the
(2,3)/(2,5) chain gates, built SATURATED FROM BIRTH per the sec-17/18
standing rule (tie + Rabinowitsch rows in the first emission, never
retrofitted), so their core verdicts land at the same evidence tier
as r1_minsat/r1_12sat_corr; then the (1,2) branch's own F_s
band/quotient ladder (where the level-4/42 s1-condition lives).

CHAR-0 LEG (phase x; the 15.6 char-0-upgrade path, brought local):
r1_q2_l13.ms EMITTED (24 eqs, 151 vars, 315 kB): the EXACT-ring twin
of the stratum-13 object -- radicals as variables (every A-embedding
at once), W symbolic on E, same defining rows/quotient subset/tie/
saturation, W-Laurent cleared per row.  Its rows REDUCE TO THE BANKED
MOD-P BUILDS EXACTLY at both primes (cross-engine regression, exact
ring vs the independent mod-p fold -- the strongest anchor in the Q2
net).  Its msolve verdict line appends to runs/r1_q2_runs.log
  (an exact rational cofactor here would upgrade the stratum-13 kill to a
  proof over Qbar, subsuming both p-screens and every A-embedding; printed
  `-g [1]` alone does not).

**CORRECTED CHAR-0 EVIDENCE TIER:** `r1_q2_l13.ms` produced a `[1]`
first-prime trace in 663 s / 6.8 GB (`jc72108/runs/r1_q2_l13.ms.out`),
not a rational unit-ideal certificate.  Together with the two explicit
p-runs it gives strong modular evidence that the 54-direction stratum dies,
uniformly across the encoded embeddings, but the Qbar stratum remains open.
Consequently the claim that every characteristic-zero survivor carries a
nonzero free coefficient below slot 13 is withdrawn; that implication is
valid only over the recorded finite fields.  The 1200-s local GB
budget resolves nothing below that cliff (l12/l8/l4 all wall out at
both primes, incl. kill-sound row subsets), so the F_s-route
exclusion CLAIM stays at the stratum, not the full chart.

### 19.5 l8 leaf decomposition: first-nonzero cascade over the 13
### opened directions (2026-08-13; design + census banked BEFORE runs)

MOTIVATION. The l8 monolith (r1_q2_l8_p*.ms, 243-corrected) is
structurally GB-dead: 1200 s/12-15 GB locally (19.2) and a Box02
2 TB attempt died at ~1.65 TB RSS / 11 h with no verdict -- the sec-13
precedent (monolith death -> leaf verdicts in seconds) mandates a
chart decomposition.  This is the INDEPENDENT second route on the
residue-A obligation (confirmation for the Box02 nolog screens if
they return EMPTY; fallback if they wall).  Engine:
cases/r1_q2_l8_leaves.py (ADDITIVE; consumes the banked, anchored
/tmp/r1q2/build_p*_l8.pkl builds; parent emissions untouched).

CENSUS (banked BEFORE design lock; both primes identical).  The l8
stratum opens EXACTLY 13 free core directions absent from l13 (slot =
level-12 in [8,13)): slot 8: bf_20, bg42_20, bg21_20; slot 9: bf_21,
bg42_21; slot 10: bf_22, bg42_22, bg21_22; slot 11: bf_23, bg42_23;
slot 12: uf24, bg42_24, bg21_24.  (bf_24 sits at slot 12 but is
KEEPX = kept back-map VARIABLE with a defining row at every lcut --
NOT stratum-gated; this reconciles the 19.2 54->67 direction count.)
Occurrence census of the 34,739 quotient-row terms: every direction
carries 3,013-6,358 terms (uf24 heaviest 6,358; bg21_22 lightest
3,013) -- the mass is FLAT: no small dominating pivot set exists, so
the sec-13 4-leaf pattern does NOT transfer (zeroing even the top-2
directions leaves 23,821/34,739 terms in the LIGHTEST of its 4
leaves).  The right split is the FIRST-NONZERO (lex-prefix) cascade.

DESIGN (pivot order fixed by census: ascending slot, then descending
occurrence): d_1..d_13 = bf_20, bg42_20, bg21_20, bf_21, bg42_21,
bf_22, bg42_22, bg21_22, bf_23, bg42_23, uf24, bg42_24, bg21_24.
leaf k (k = 1..13): d_1..d_{k-1} = 0 substituted (term-drop in every
row incl. the bf_18/24/30 defining rows -- the same per-stratum
restriction semantics the parent uses), d_k != 0 via Rabinowitsch row
u<d_k>*d_k - 1 adjoined, d_{k+1}..d_13 + all slot->=13 content OPEN.
Zero leaf (all 13 = 0): IDENTICAL to the banked l13 object --
verified EXACTLY (dict-equality of quotient rows AND defining rows
against build_p*_l13.pkl at BOTH primes) -- whose kill is established at
those same primes, not over Qbar (19.2).  The base of the finite-field
cascade needs no additional run.  Per-leaf masses (quotient-row terms surviving the prefix zero,
p=105337): 34,739 / 29,258 / 24,058 / 21,108 / 17,912 / 15,248 /
13,356 / 11,834 / 10,935 / 9,747 / 8,848 / 6,815 / 5,878 (l13 =
5,139).  Emissions: cases/r1_q2_l8_leaf{k}_p{105337,105673}.ms (main,
20 eqs: the 19 parent rows prefix-restricted + pivot saturation) +
_ctlB_p*.ms (E5/E6 dropped, both saturations kept: the 16.3/18.1
mechanism probe, ideal(ctlB) c ideal(main) so ctlB EMPTY => main
EMPTY a fortiori); E6 literal 16777216 reduced into [0,p) per the
AUDIT standing rule (parent files carry it unreduced -- flagged
obligation there; value-preservation pinned by guard B').

PRE-REGISTERED INTERPRETATION (fixed BEFORE any leaf run).  COVER:
V(l8 stratum) = V(l13) u U_k pi(V(leaf_k)), pairwise disjoint by the
boolean tautology on the 13-tuple (d_1..d_13): each point either has
all 13 zero (-> the l13 component, dead at the recorded primes) or a unique least
nonzero index k (-> leaf k; u = d_k^{-1} exists uniquely, field);
zero-side substitution is exact closed-pattern restriction (free
polynomial coordinates -- no quadric forcing subtlety, SIMPLER than
sec-13's Z-side); no elimination cascade is attempted, so leaf rows
are the stratum rows under the pattern substitution VERBATIM (guard
B/B').  Hence: ALL 13 leaves EMPTY at p <=> l8 stratum EMPTY at p
(the l13 base being banked), and any leaf witness lifts to the
stratum by forgetting u<d_k>.  PROGRESSIVE SEMANTICS (ascending-slot
order): leaves 1..3 EMPTY => every l8 point has all slot-8 directions
zero (stratum reduces to l9); + leaves 4..5 => l10; + 6..8 => l11;
+ 9..10 => l12; + 11..13 => l13 => with the banked l13 kill the
ENTIRE l8 stratum dies at that same prime.  Each verdict prefix is a bankable
partial statement in the 19.0 lcut semantics.  NONEMPTY at some leaf
= the relaxed screen survives with its first nonzero opened direction
pinned at d_k (characterize; NOT a branch survival claim -- band rows
s=30..54 and n>44 still unimposed).  No inflation beyond this table.

GUARDS (phase guard + cover, log 17:23 2026-08-13; ALL PASS, both
primes, all 13 leaves, main + ctlB = 52 files):
| guard | check | result |
|---|---|---|
| A | paren sweep + EVERY integer token < p ([0,p) rule) | 52/52 files PASS |
| B | independent-parser round-trip (FC.parse_eval) == internal VExpr eval, quotient + defining rows, 2 random pts/prime | PASS |
| B' | leaf rows == PARENT ARTIFACT rows (systems/r1/r1_q2_l8_p*.ms bytes) at the same point with the zeroed prefix imposed -- pins prefix-restriction soundness AND E6 [0,p) value-preservation in one shot | 19/19 rows x 13 leaves x 2 pts x 2 primes PASS |
| C | satisfiability smoke: constant-bearing rows are EXACTLY the 4 saturations (uW1, uW2, s1F, pivot); no bare-constant row | PASS |
| D | residual non-degeneracy: no emitted quotient row identically zero at generic points | PASS |
| cover (i) | 500 random 13-tuples: each matches exactly one pattern (l13 or unique first-nonzero leaf) | PASS |
| cover (ii) | l8 build rows+defs with ALL 13 dirs zeroed == banked l13 build DICT-EXACT | PASS at BOTH primes |
| cover (iii) | unit lift u = d_k^-1 unique (field); zero side closed-pattern restriction; rows verbatim (B') -- back-map = forget u<d_k> | stated + mechanical |

LAUNCH RECORD (Box02, x2idn.32xlarge 2 TB; ops/FLEET.md orphan-safe
self-recording pattern; ~/res32/lanes.log; NO local msolve).
Monolith provenance: Box02 q2b2.log shows r1_q2_l8_p105337 start
07:10:36 -> FAILED, p105673 start 18:12:15 (the ~11 h / ~1.65 TB RSS
death; no verdict line -- 0-byte-out hygiene rule).  Wave 1 launched
2026-08-14 00:24 UTC (box time), 26 lanes CONFIRMED as 26 running
msolve processes (39 with the 13 standing lanes), each:
  nohup sh -c "ulimit -v <fence>; timeout 43200 msolve -g 2 -t 8
    -f X.ms -o out/X.out; echo LANE X: rc/size/time >> lanes.log" &
- leaf1..3 MAIN p105337 (34.7k/29.3k/24.1k quot terms): fence 150 GB.
- leaf1..3 ctlB p105337 (mechanism probes): fence 25 GB.
- leaf4..13 MAIN at BOTH primes (21.1k..5.9k terms): fence 25 GB.
Fence budget worst-case 1,025 GB against 1,338 GB free at launch --
the standing DECISIVE nolog screens (residue-A route 1) keep >300 GB
growth headroom; a fence-killed lane records rc!=0 and re-runs after
the standing queue drains.  STAGED on the box, deliberately NOT yet
launched (second wave, post-drain): leaf1..3 main p105673, leaf1..3
ctlB p105673, leaf4..13 ctlB both primes (all 52 files + md5-verified
scp; launcher launch_l8_leaves.sh in ~/res32).  READING RULE: 0-byte
.out != verdict; only lanes.log "LANE r1_q2_l8_leaf*" lines with
rc=0 and a GB-bearing .out are verdicts (19.2 hygiene).  Third prime
200257: NOT emitted -- no banked Q0 gate/fam anchor state at that
prime (A-Q2-1/A-Q2-2 are per-prime trust gates, 19.0); the two banked
primes match the entire Q2 tier's verdict basis.  Engine + emissions:
cases/r1_q2_l8_leaves.py + cases/r1_q2_l8_leaf{1..13}[_ctlB]_p*.ms +
per-leaf .rows.txt provenance.  CONTINGENCY (pre-registered): if
leaf1 (full-mass + saturation) also walls at 43200 s / 150 GB, its
own sub-split is by the pattern of d_2.. within the leaf (same
machinery, zset seeded with nothing, pivot cascade over the
remaining 12) -- second-generation leaves, same cover argument.

### 19.5a Wave-1 autopsy: the cliff is CERTIFICATE-side; restructure
### to the l12 3-chart cover (2026-08-14; design only, NO launches)

FIELD REPORT (coordinator + lanes.log): 23/26 wave-1 lanes died
rc=139 (malloc at fence) in ~40 min each; the 3 survivors are the
150 GB heavies (leaf1-3 main p105337, 79-87 GB RSS at +32 min and
climbing); the fences HELD -- the standing nolog screens were never
touched.  A 30 s foreground parse of leaf1 is clean: pure F4 growth.
DECISIVE NEGATIVE DATA, banked: (i) the ctlB lanes died too -- ctlB
contains NO E5/E6/HM rows, so the deep tie block is EXONERATED: the
driver sits in the quotient + chart + saturation rows alone.  (ii)
leaf13, the MINIMAL object of the entire family (l13 + the single
direction bg21_24: +8 header vars, +739 terms), exceeds 25 GB where
l13 itself is 1 s at <1 GB: a PER-DIRECTION cliff.

DIAGNOSIS (size-proxy table, measured from the artifact bytes;
n = header vars, D = max row total degree, powOPEN = max pure power
of an opened direction, proxy = log10 C(n+D,D) = Macaulay frame at
the input degree):
| object | n | D | powOPEN | proxy |
|---|---|---|---|---|
| l13 (1 s, <1 GB, dead at two recorded primes; Qbar open) | 146 | 11 | 0 | 16.4 |
| leaf13 = l12-chart-3 (>25 GB) | 154 | 11 | 5 | 16.6 |
| leaf12 = l12-chart-2 (>25 GB) | 155 | 11 | 5 | 16.7 |
| leaf11 = l12-chart-1 (>25 GB) | 156 | 11 | 5 | 16.7 |
| leaf7 (>25 GB) | 164 | 11 | 6 | 16.9 |
| leaf1 = l8+sat (>=87 GB, running) | 176 | 11 | 6 | 17.3 |
| l8 monolith (~1.65 TB death) | 175 | 11 | 6 | 17.2 |
The INPUT side is FLAT: D = 11 everywhere, proxy within one decade
across the family, term mass down 83% at leaf13 -- yet the wall does
not move.  So the blow-up is NOT input-volume: it is CERTIFICATE-
side.  At l13 the s1F-forcing mechanism (16.3/18.1) hands F4 the
unit at low working degree; ANY open slot-<=12 direction breaks the
near-linear forcing (pure powers d^5..d^7 -- impossible for slot>=13
directions inside the slot-60 window -- create self-coupled content),
pushing the emptiness certificate (or the surviving staircase) into
degree tiers whose Macaulay frames are the ~10^16-column objects the
proxy prices.  CONSEQUENCE for the coordinator's options: (a) NO
finer input-side split can work at l8 granularity -- every
vanishing-pattern refinement bottoms out at a single-direction
object, and that minimum (= leaf13) is already >25 GB: option (a)
below l12 is CLOSED by measurement.  (b) -e block orders: REJECTED
honestly -- no provable intermediate-basis bound exists for block
elimination in F4 (block orders generally cost >= DRL; the verdict
is order-independent, only the cost moves); claiming such a bound
would violate the trust discipline.

SOL CONVERGENCE (xmodel/sol-probability.md branch 8) + IDENTITY.
Sol independently proposes decomposing the exact l13->l12 cliff:
l12 = l13 + the low triple (uf24, bg42_24, bg21_24) + six level-60
highs, covered by the settled origin chart + three nonzero charts.
VERIFIED MECHANICALLY: (i) hdr(l12) \ hdr(l13) = exactly the 3 lows
+ 6 level-60 tails tg1_60, tg2_60, tg01_60, tg02_60, bg42_60,
bg21_60 (slot-48 content that enters the slot-60 window only through
an opened slot-12 partner) -- Sol's object description is exact.
(ii) build(l8) with the 10 slot-8..11 directions zeroed == the
banked l12 build DICT-EXACT (rows AND defs, BOTH primes).  Therefore
Sol's three charts ALREADY EXIST inside the 19.5 cascade: they ARE
leaf11 (uf24 != 0), leaf12 (uf24 = 0, bg42_24 != 0), leaf13 (both
zero, bg21_24 != 0), with origin chart = l13 discharged only at the
recorded finite fields -- emitted, guard-PASSED (19.5 table covers all
6 files), md5-verified on Box02.  Field pricing corrects Sol's
1-2-day estimate: all six lanes died rc=139 at the 25 GB fence, so
the charts are >25 GB objects; they remain the LIGHTEST members of
the family (proxy 16.6-16.7 vs l13's 16.4, the smallest measured
gap to a solved object) and the only GB route not yet priced above
150 GB.

RECOMMENDATION (design bank; NO lanes launched, NO commit):
1. RETIRE leaves 1-10 (l8 granularity) as INFEASIBLE-AT-TIER: the
   monolith's ~1.65 TB death + the flat proxy + 23 rc=139 price
   every refinement; let the 3 running 150 GB heavies exhaust their
   43200 s cap (already launched -- not a new spend) and bank
   whatever they return; l4/l1 GB attempts are retired A FORTIORI.
2. ADOPT the l12 3-chart cover = the EXISTING leaf11/12/13 emissions
   at BOTH primes as the surviving GB route: re-run at raised fences
   (350-500 GB, <= 3 lanes concurrent, sequenced AFTER the nolog
   screens drain; coordinator's launch call).  Verdict semantics:
   all 3 charts EMPTY at p + banked l13 => the l12 stratum dies at p
   (19.5 progressive semantics, prefix 11..13); the slots-8..11
   residue then rides the STRUCTURAL row-family routes (n > 44 band
   rows, R2-R5 ladder, 15.3/19.4) -- not GB force.
3. FALLBACK, pre-registered: if any chart walls at 500 GB, the
   Q2-l8/l12 GB tier verdict is INFEASIBLE and the residue-A
   second-route confirmation rests on the plain
   directionb_residual32 lanes at p105673/p200257 (+ ctl0 controls)
   already standing on Box02 -- same residual object, independent
   lanes and primes.
REPORTING RULE (Sol's wrong-object warning, STANDING): every Q2
stratum verdict is a QUOTIENT-WINDOW statement -- UU chart, depth-84
slot-60 window, row subset n <= 44, named stratum/chart -- NEVER a
bare "residue-A survives/dies".  Q2 and the J/nolog families are
DIFFERENT necessary row systems on the same coefficients; individual
survival protects no intersection (Sol branch 8').

## 20. SATURATED chain terminal gates: (2,3)->(6,17) and (2,5)->(6,23)
## (2026-08-11; the 19.4 banked directive executed)

### 20.0 Pre-registration + scale inventory (banked BEFORE build)

BASE objects (sec 9/11, guard-certified, UNSATURATED): r1_23chain_core
(115 eqs = 7 radical + 74 band + 7 quot + 6 quot-deg + s1-tie + s1-inv
+ 12 h2-quot + 6 h2-quot-deg + qL-inv; vars x0..x118 + s1,cL,t1,qL,t2)
and r1_25chain_core (44 eqs = 7 radical + 11 quot + 2 quot-deg +
s1-tie + s1-inv + 22 h2-tie; x0..x28 + s1,cL,t1).  Both carry the
sec-17/18 W-exposure: W1/HW1/W2/HW2 free, NO uW rows (18.3).

SCALE INVENTORY (mandate-1 analogue, from the chain genomes R6 4.2):
| scale | forced nonzero by (genome) | gate handling |
|---|---|---|
| s1 (level-2 tie h2 = h1^2 - s1 f^l1) | Prop 4.2(iii) tower constant | t1*s1-1 IN BASE from birth |
| cL (level-1 G_m lead; rows WG(n,s1st) = cL*P^l1[n]) | p_h1@Gm = (-)P^l1 deg 18|30 EXACT is forced tower data (R6 4.2 B'); also cL^2 = S_M^l1 s1 (s1-tie) + s1 != 0 | NEW explicit row tcL*cL-1 (standing-rule explicitness; redundant given tie, harmless) |
| qL ((2,3) only; h2-quot lead, q's content H*S_M-power absorbed) | deg p_h2@Gm = 34 EXACT forced; q deg-10 shape feeds level 3 | t2*qL-1 IN BASE from birth |
| W_1, W_2 | pole pattern p_h1@P = -(3/4)s0 lam_i^3 w_i^4 (eta^2-(4/3)w_i^2) NONZERO deg 2 (R6 post-review (D): d_h1@P = 1/7 rests on no level drop; w_i = 0 kills the lead), axis poles excluded (St 7.2) | NEW uW_i*W_i-1 rows (the 18.3 exposure CLOSED at birth) |
| HW_i | HW_i^2 = (3/2) W_i^2 | automatic from uW (char != 2,3) |
| s2 (level-3 tie; W2-collapse pins s2' = H^6, R6 4.2 RUNG) | Prop 4.2 tower constant | (2,3): H absorbed in qL => covered by t2*qL-1; (2,5): H lives in the DEFERRED r=14 farm quotient (9.4) -- no local carrier; kills valid a fortiori, any survival carries the obligation |
| s1F/s2F analogues (F_s leads; tower ALIVE at F_s, m_Fs >= 3) | 1b at F_s | NOT in the G_m-window gate: the chain's own F_s band/quotient ladder (obligation list) |
| etale r3, z, A_i, EB | minimal polys have no zero root | no row (18.0 justification verbatim) |
| interior/tail x-vars | NOT forced (free template parameters, 1c) | carried free, justified |

TIE-ROW DERIVATION (mandate 2, with the Q2E5 lesson applied: St
3.9(ii) lead transports REQUIRE the 3.9(i) count equality, checked
per member per edge).  Count scan at the chain pole edges (m_P = 0),
mult(p@Gm, c_i) vs deg p@P: f: 2 == 2 COUNT-EXACT; g: 3 > 2; h1:
l1 (3|5) > 2; h2: 2mu2-1 (5|7) > 2k1 = 4; h3: 12(mu2-1)+6 (30|42) >
24.  So: (a) the ONLY count-exact member is f, whose transport is the
E6-analogue unit pin lam_i = 9 S_M c_i^4 (a1-a2)^2, m_i^2 = s0 lam_i^3
-- already RING CONSTANTS inside the shared W_G fold (no row to add);
(b) NO count-exact dead member exists at either chain pole edge: the
E5-quartic analogue set is EMPTY BY DERIVATION (not omission) -- any
ported h-row would repeat the 19.3 level slip; the leaks are St
3.11(i)-legal (R6 4.2 C'/D').  (c) The in-window E6-tie analogue at
G_m is the legality row S_M^l1 s1 = cL^2 -- IN BASE from birth.
Mechanical verification of (a)-(c) = engine phase `inventory` (exact
K3), gating emission.  NET: saturated gate = base core VERBATIM +
uW1/uW2 + tcL rows; nothing else is derivable at this tier in print.

GATE LEDGER (pre-registered): per chain X in {23, 25}:
- r1_Xsat.ms (char 0) = base core rows byte-VERBATIM + uW1*W1-1 +
  uW2*W2-1 + cL*tcL-1;  r1_Xsat_p{105337,105673}.ms = base wfree rows
  VERBATIM + the 3 rows reduced into [0,p).
- r1_Xsat_ext retrofit ((2,5) only): banked ext wfree + same 3 rows --
  the 18.3-mandated saturated re-emission of the box01 decider (E5
  port question now settled: vacuous by derivation); EMITTED for the
  fleet, not run locally (its unsaturated twin walled at 3000 s).
- ctlA_relaxed_p*.ms = base wfree MINUS its constant rows (s1-inv,
  qL-inv), NO additions: MUST be NONEMPTY (origin zero-point; guard-C
  census) -- emission sanity; certified by independent-parser explicit
  point, GB only if cheap.
- ctlB_satonly_p*.ms = level-1 subsystem ONLY (radical-HW + band +
  quot + quot-deg) + uW1/uW2 + tcL, NO level-2 rows (s1-tie, s1-inv,
  h2-*, qL-inv): DIAGNOSTIC -- EMPTY <=> the level-1 window alone
  refuses an alive slot-s1st pattern with W-units and cL != 0 (death
  already at level 1); NONEMPTY <=> level-2 ties carry the load.

ANCHORS (pattern-positive, mandate 4, all PASS required before any
run is read): A-C-1 pattern suite -- P^3, P^5 (eta-deg 18/30) and
pq34 = eta(t-a1)^5(t-a2)^5(t-b) recomputed by an INDEPENDENT
Fraction+r3 convolution path (not the engine's eta_poly_ref/
k3poly_pow_pattern); value + alignment (deg/monic/lattice n mod 3) +
positivity (synthetic division: root mult EXACTLY l1 at both a_i;
pq34: 5/5/1 with b = 4 the ODE pin).  A-C-2 row-level: in the rebuilt
VExpr rows, coefficient-of-cL in every level-1 quot row == -P^l1[n]
EXACTLY (sees every pattern coefficient incl. monic top), no cL key
in band/quot-deg rows; (2,3) h2-quot rows: coefficient-of-qL ==
-pq34[n], none in h2-quot-deg; s1-tie row keys == {(cL,cL): +1, (s1,):
-S_M^l1} with S_M^l1 independently recomputed.  PERTURBATION SUITE
(must ALL be caught): reference-side wrong-b (4 -> -4), index shift
(n -> n+3, lattice-preserving), global sign flip, single-coefficient
corruption; build-side: corrupt one row's cL coefficient, shift one
row's n.  Emission->VExpr closure: FC.guards on the BANKED core files
against the state-rebuilt rows (guards A-D incl. independent-parser
round-trip at both primes) -- the banked artifact, the state, and the
anchor all tied together.

VERDICT SEMANTICS (sec 1 + sec 17 saturation rule; no inflation):
- GB = [1] at BOTH primes on r1_Xsat_p* => the branch DIES at its
  terminal core mod p (strong evidence).  On `r1_Xsat.ms`, an msolve `-g`
  `[1]` with a characteristic-zero header is only `FIRST-PRIME-EMPTY`, not a
  Qbar verdict; PROOF-tier requires a verified rational Gröbner basis or an
  exact identity `1 = sum h_i f_i` -- the honest reading the unsaturated
  sec-11 (2,5) NONEMPTY could never license.  ctlA must be NONEMPTY
  first, else emission error: HALT, no verdict.
- NONEMPTY => characterize (GB size; dim/degeneracy strata if cheap;
  explicit point only if cheap) and state next-tier obligations:
  (2,5): saturated ext decider (retrofit above) + farm rungs r=12,14
  + level-3 ladder + F_s tier + J-closure; (2,3): level-3 band (deg
  195 rung, farm) + F_s tier + J-closure.
- Runs 1200 s local, -g 2 -t 4; TIMEOUT => bank emission + size for
  the fleet; 0-byte .out != NONEMPTY (19.2 hygiene).  p-screens
  first; char 0 only if p-screens resolve fast.
Regression gate: sha256 of all 137 pre-existing systems/r1 emissions
(/tmp/r20_baseline.sha) unchanged after the session; engine = NEW
ADDITIVE file cases/r1_chain_sat.py (r1_fullcore.py untouched).

### 20.1 Build log

Engine: cases/r1_chain_sat.py (NEW, additive; phases inventory |
anchor | emit | run).  Phase inventory PASS (exact K3): E6 f-transport
pin lam_i = 9 S_M c_i^4 (a1-a2)^2 verified a K3-unit with m_i^2 =
s0 lam_i^3 solvable (m_i = 648 sqrt3 G_M a_i^2; 648^2*3 = 729*1728,
G_M^2 = S_M^3); count scan CONFIRMS the 20.0 derivation -- leaks
(g,3,2),(h1,l1,2),(h2,2mu2-1,4),(h3,12(mu2-1)+6,24) for both chains,
f alone count-exact => E5-quartic analogue set EMPTY BY DERIVATION;
base rows carry s1-tie/s1-inv (+ qL-inv for 23) and NO uW rows (18.3
exposure confirmed present in the base, closed by this gate).

Phase anchor PASS (11:31): A-C-1 independent-convolution patterns ==
engine patterns coefficient-for-coefficient (p3/p5/pq34), root mults
(3,3)/(5,5)/(5,5,1@b=4) by synthetic division; A-C-2 row-level
pattern-positivity -- (2,3): 7 quot rows cL-part == -P^3[n], 12
h2-quot rows qL-part == -pq34[n]; (2,5): 11 quot rows == -P^5[n];
band/deg rows lead-free; s1-tie == {cL^2: +1, s1: -S_M^l1} with
S_M^l1 independently recomputed.  Perturbation suite 6/6 CAUGHT
(wrong-b, n->n+3 shift, sign flip, coeff corruption, build-side value
+ slot).  Both BANKED core .ms files re-certified against the
state-rebuilt rows: guards A-D PASS (round-trip 108/108 resp. 37/37
at both primes; origin census 106/108 resp. 36/37 -- only the
constant rows survive at x=0).  W-LOAD MEASUREMENT (banked openly):
the (2,5) core rows carry NO W-monomials (uW saturation VACUOUS at
its core tier -- the W-load enters at ext rungs r >= 4: 70/134 ext
rows W-loaded), while the (2,3) core has 66 W-loaded rows (uW
BINDING at core).  The uW rows stay in both gates (standing rule);
the vacuity is recorded, mirroring 19.3's s1-vacuity precedent.

### 20.2 Emission ledger (all guards PASS both primes; regression
### gate: 137/137 baseline sha256 unchanged after emission)

| object | eqs | vars | note |
|---|---|---|---|
| r1_25sat.ms (char 0) | 47 | 44 | base 44 VERBATIM + uW1/uW2/tcL |
| r1_25sat_p105337/_p105673.ms | 42 | 39 | wfree base 39 VERBATIM + 3 reduced |
| r1_25sat_ctlA_relaxed_p*.ms | 38 | 36 | s1-inv dropped; NONEMPTY certified (origin, 38/38 rows vanish, indep. parser) |
| r1_25sat_ctlB_satonly_p*.ms | 18 | 39 | level-1 (radical-HW + quot/quot-deg) + 3 sat rows |
| r1_23sat.ms (char 0) | 118 | 136 | base 115 VERBATIM + 3 (39.6 MB) |
| r1_23sat_p105337/_p105673.ms | 113 | 131 | wfree base 110 VERBATIM + 3 reduced |
| r1_23sat_ctlA_relaxed_p*.ms | 108 | 128 | s1-inv/qL-inv dropped; NONEMPTY certified (origin, 108/108 vanish) |
| r1_23sat_ctlB_satonly_p*.ms | 92 | 131 | level-1 (radical-HW + band/quot/quot-deg) + 3 sat rows |
| r1_25sat_ext_p105337/_p105673.ms | 137 | 93 | 18.3-mandated SATURATED re-emission of the box01 ext decider (56.5 MB each); FLEET object, not run locally |

Guard C both primes both gates: origin fails EXACTLY the constant
rows (4 = s1-inv + uW1/uW2/tcL for 25; 5 = + qL-inv for 23) -- the
gates exclude the zero point and carry no other constant row.  Paren
sweep + [0,p) reduction asserts PASS on every emitted p-file; char-0
gates carry the base rows byte-identically (asserted in-emitter).

### 20.3 Run ledger (msolve 0.10.1 local, -g 2 -t 4, timeout 1200 s;
### logs runs/r1_25sat_runs.log, r1_23sat_runs.log)

| run | p=105337 | p=105673 |
|---|---|---|
| r1_25sat_p* (MAIN, saturated) | GB != [1] NONEMPTY, 1 s (24-elt GB) | GB != [1] NONEMPTY, 1 s |
| r1_25sat_ctlA_relaxed_p* | NONEMPTY by EXPLICIT POINT (origin; indep. parser cert, 20.2) | (same) |
| r1_25sat_ctlB_satonly_p* | GB != [1] NONEMPTY, 1 s | GB != [1] NONEMPTY, 1 s |

| r1_23sat_p105337 (MAIN, saturated; FIRST-EVER run of the (2,3) core) | TIMEOUT 1200 s / 15.0 GB rss | (see below) |
