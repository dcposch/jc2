# SHEET6-R1-Q2E5.md — Adversarial review: the (1,2) E5-quartic port (§18.2) + the Q2 full-locus screen design (§19)

Reviewer: Claude (adversarial pass, 2026-08-11). Status: COMPLETE.
Scope: (i) the k1 = 1 E5 pole-edge port derived in SHEET6-R1.md §18.2 and
implemented in cases/r1_12_sat.py (the single point of failure §18.2
itself flagged: "an adversarial check of the k1 = 1 transport (one
Taylor-coefficient computation) is the single point of failure"); (ii)
the Q2 full-locus screen build (SHEET6-R1.md §19) — pre-run design
review, sizing-gate audit, and the §18 minor flag (control inputs).
Ground truth: SHEET6-TEMPLATE.md §2a (St 3.9(i)-(iii)/3.11(i)/8.3(ii)
recap) + §2c-E5; SHEET6-R6.md §4.3 + layer-2/post-review corrections;
the banked artifacts in systems/r1/.  Review-owned tools (no r1_12_sat
import): /tmp/q2e5_review/e5_12_review.py (exact Taylor/d-ladder
verification at both banked primes), fam_sub_*.ms row-subset probes.

Verdicts:
- E5-12 port (§18.2 / r1_12_sat e5port): **WRONG — LEVEL SLIP FOUND.**
  The arithmetic is clean; the MECHANISM application is not. The §18.2
  "(1,2) branch DIES at its terminal core" verdict is **RETRACTED**;
  corrected objects are NONEMPTY (char 0 + both primes): the (1,2)
  branch SURVIVES its terminal core, mirroring the minimal branch.
- The predicted one-slip-per-layer: found, and it is the same GENUS as
  the two before it (ZZ leaf, Q0 s1F): a constraint transported to the
  wrong object — this time to the wrong LEVEL of the right vertex.
- §18 minor flag (ctlA/ctlB inputs not banked): FIXED (inputs now in
  systems/r1/, re-run verdict-identical).
- Q2 design (§19): sizing gate honored mechanically; row-subset
  soundness argument verified; see §3 below.  OUTCOME: stratum-13
  (54/84 free directions + W symbolic) killed at both primes AND in
  CHAR 0 (GB = [1] over Q, 663 s -- PROOF-tier over Qbar, all
  A-embeddings; cross-engine regression exact vs both mod-p builds);
  strata 12/8 emissions banked, local msolve TIMEOUT (box01 queue);
  strata 4/1 build-gated by the 15.6 budget (measured).

## 1. The E5-12 port: re-derivation from the printed mechanism

### 1.1 What the port did (r1_12_sat.py e5port, §18.2)

At G_m the k1 = 1 legality (Prop 4.2(iii)) makes h1 ALIVE with the
pure-power pattern p_h1,Gm = s1 S_M^2 P^4 (deg 24, d = 12/21; R6 §4.3's
banked (1,2) delta data). The port applied St 3.9(ii) to h1 across the
merge edge G_m -> P_i: [4th Taylor coeff of s1 S_M^2 P^4 at c_i] ==
[lead of the deg-2 pole pattern -(3/4) s0 lam_i^3 w_i^4 (eta^2 -
(4/3)w_i^2)], giving 81 S_M a_i alpha_i W_i^4 + s1 = 0, which is
jointly inconsistent with relation E at any s1 != 0 (bracket
sum (9±5r3)/a_i = 4 != 0) — the banked GB = [1] kill.

### 1.2 The slip: the two sides live at DIFFERENT levels

St 3.9 as recapped in TEMPLATE §2a is a package: (i) mult(p_{h,F}, c)
= deg(p_{h,F*c}); (ii) lead transport; (iii) d drops by mult/kappa per
elementary step. (ii) presupposes (i). For (1,2)-h1 at the merge edge,
(i) FAILS: mult(p_h1,Gm, c_i) = 4 (P^4), but deg p_h1,P_i = 2 — the
pole pattern is branch-LOCAL (top of g^2 - s0(f-a)^3, the shared (2,3)
base; the z^2-cancellation identity of TEMPLATE E5 forces deg 2
regardless of the incoming mult). Only St 3.11(i) monotonicity holds
(2 <= 4, slack 2) — and R6 §4.3 recorded exactly this: "two simple
roots, not a square — the hoped-for killer ... simply NOT constrained
... NO exclusion exists in print; the condition is an R1-tier series
constraint."

The d-arithmetic (St 3.9(iii); verified mechanically at both banked
primes, /tmp/q2e5_review/e5_12_review.py) pins the slip sharply.
Merge edge = 5 steps at 1/42 (TEMPLATE 1c); pole-side levels are
branch-local: d_f@P = 2/42, d_g@P = 3/42, pole h1-top at 2 d_g = 6/42:

| member | d@Gm (/42) | mult at c_i | transported level | pole top | |
|---|---|---|---|---|---|
| f (both branches) | 12 | 2 | 12-10 = 2 | 2 | EXACT |
| g (both) | 18 | 3 | 18-15 = 3 | 3 | EXACT |
| h1 minimal | 16 | 2 | 16-10 = 6 | 6 | EXACT (the E5 row) |
| h2 (1,2) | 16 | 2 | 16-10 = 6 | 6 | EXACT (the correct row) |
| h1 (1,2) | 24 | 4 | 24-20 = **4** | **6** | **MISMATCH** |

The mult-4 transport of s1 S_M^2 P^4 lands at level 4/42 = 2 d_f@P —
it IS s1·(f^+)^2 localized at the pole (s1 lam_i^2 (eta^2 - w_i^2)^2;
the Taylor factor (3c_i^2)^4 (a1-a2)^4 = (transport of S_M P^2)^2,
verified exactly). The pole's PATTERN top sits at 6/42. The port
equated a level-4/42 quantity with a level-6/42 quantity. The correct
content of the mult-4 transport is: h1's level-4/42 pole-series
coefficient (SUB-top; free g/f tail data at core tier) equals
s1 lam_i^2 (eta^2 - w_i^2)^2 — precisely R6 §4.3's "R1-tier series
constraint", constraining s1 against pole TAIL unknowns, not w_i. It
is not a core-level pattern row, and no print statement makes it one.

### 1.3 Why the port's own validations did not catch it

- The minimal-branch pipeline check reproduces 13.1 because the
  minimal case is count-EXACT (mult 2 = deg 2): it validates the
  pipeline only inside St 3.9's domain. The (1,2) application (mult 4,
  leak 2) is outside it — the one case the validation could not reach.
- The port also switched OBJECTS between branches: for minimal it
  transported the first-dead-member pattern (P·q form, deg 16); for
  (1,2) it transported the alive pure power (P^4). The like-for-like
  object exists in BOTH branches: the (1,2) first dead member is h2 =
  h1 - s1 f^2, whose G_m data is byte-identical to minimal h1 (P·q,
  deg 16, d = 8/21, R6 §4.3) with its own lead H12, mult 2 at c_i —
  count-EXACT, landing at 6/42 EXACTLY. Its St 3.9(ii) row is the
  minimal E5 row with H_M -> H12; substituted into E it gives the 13.1
  bracket sum (9±5r3)(a_i-b)/a_i^2 == 0 IDENTICALLY. No kill.
- The "row constant == 15.1 row-87 content 243·7^12" corroboration is
  misattributed: rows 87-91 are the (1,2) core's h2-stage (B12-h2-quot)
  G_m quotient rows — evidence about the h2-stage normalization, i.e.
  about the CORRECTED transport object, not about the mult-4 h1 rows.
  (The port's own row constant is 81·7^12, not 243·7^12.)

### 1.4 Row-by-row implementation check (r1_12_sat.py)

Given its premise, the implementation is CLEAN — the slip is entirely
in the premise:
- e5_12_rows_char0 pole 1 (hand-verified): 81 S_M a_1 alpha_1 W_1^4 +
  s1 = 0, S_M = 7^12/2^6, cleared by 2^6: (3·81·7^12) A1 W1^4 +
  (81·7^12) r3 A1 W1^4 + 64 s1 — coefficients match a_1 = 3 + r3
  exactly; pole 2 carries the conjugate sign (the earlier "+-"
  malformation is fixed in the banked file; run-log note verified).
- e5_12_rows_modp (hand-verified at p = 105337): c = 81·7^12·a_i·A_i
  mod p, row c·W_i^4 + 64 s1 — consistent specialization of the
  char-0 rows at the banked radical point.
- e5port internal identities all re-verified exactly ((a1-a2)^2 = 12;
  minimal bracket == 0; (1,2) bracket == 4; (3/4)·729·12 = 6561).
- phase_minsat rows (minimal E5, HM restored, x 2^18): coefficients
  12cW ± 6cW r3 (= cW a_i^2), ∓/±2^20 HM (= 4(a_i-b)·2^18) —
  hand-verified against TEMPLATE 2c-E5. Correct.

### 1.5 Fix + rerun (cases/r1_12_sat.py phase corr; ADDITIVE)

r1_12sat_corr.ms = leaf12_UU verbatim + corrected h2-transport rows
(729 S_M^3 (a1-a2)^4 a_i^2 alpha_i W_i^4 + 4(a_i-b) H12 = 0, cleared
to Z) + H12·tH12 - 1 + s1·t12 - 1 (s1 occurs in NO row: its core
saturation is vacuous — banked as a fact, not hidden). p-variants on
leaf12_UU_wfree_p*.

| run | verdict |
|---|---|
| r1_12sat_corr.ms (char 0) | GB != [1] **NONEMPTY**, 1 s |
| r1_12sat_corr_p105337.ms / _p105673.ms | GB != [1] **NONEMPTY**, 1 s |

RESTATED (1,2) VERDICT (honest): the §18.2 core-level kill is
RETRACTED. Under saturation + the CORRECT tie transport, the (1,2)
branch SURVIVES its terminal core exactly as the minimal branch does
(r1_minsat NONEMPTY; same E, same identity, H12 in place of H_M). The
prior banked r1_12sat*.ms files are historical artifacts of the
retracted rows. The (1,2) branch's honest status: ALIVE at core;
its kill, if any, lives in its own per-branch series ladder (F_s
band/quotient tier, where the k1 = 1 s1-tie DOES become a genuine
series constraint — the level-4/42 relation above — plus R2-R5/J),
none of which is built yet. The §15.3 obligations list stands.

## 2. §18 minor flag: control inputs banked

phase_famctl wrote ctlA_relaxed/ctlB_satonly INPUTS to /tmp only.
Fixed (r1_q0_gate.py, path -> systems/r1/); re-run: ctlA NONEMPTY,
ctlB EMPTY — verdict-identical to §18.1's table. Inputs now banked as
systems/r1/r1_q0_fam_ctlA_relaxed.ms / r1_q0_fam_ctlB_satonly.ms.

## 3. Q2 build design review (the §19 screen; pre-run bank)

- SIZING GATE (15.6) audited mechanically BEFORE any build: the
  full-locus (84 free directions) UU chart has 42 free B-side/g-side
  dead-stretch coefficients at slots 1..17; the raw depth-84 fold's
  slot-60 content over them is the banked ~6e8-term object, and
  LEAF-COMPRESSION CANNOT SHRINK IT (measured: the three deep back-map
  values bf_18/24/30 EXPAND to 24/348/3552-term polynomials at slots
  6/12/18 — substituting them multiplies fold content instead of
  reducing it). The 15.6 "else redesign" branch fires; design deltas:
  (a) bf_18/24/30 kept as VARIABLES with their composed defining rows
  adjoined (exact, fold-size-independent); (b) row subset n <= 44
  (eta-degree cap), MEASURED sufficient: on the banked family object
  the kill survives restriction to rows n <= 44 (7 rows; n <= 16 does
  NOT kill — fam_sub probes, both banked in /tmp/q2e5_review/); subset
  soundness: a row-subset ideal is contained in the full ideal, so
  EMPTY(subset) => EMPTY(full tier) — kills only, never survivals;
  (c) stratum parameter LCUT (free directions at slot < LCUT zeroed),
  sizing measured per LCUT, largest feasible stratum run at both
  primes; LCUT = 1 = full locus. KILL SEMANTICS pre-registered in
  SHEET6-R1.md §19.0 BEFORE the runs.
- W is NOT specialized anywhere in the Q2 object (Laurent W-part
  canonical mod the quadrics, uW_i on the chart, relation E carried);
  etale radicals at the banked point = the wfree p-screen methodology.
- Anchors: A-Q2-1 (witness specialization == banked gate rows,
  key-exact), A-Q2-2 (free-x = 0 with W SYMBOLIC == the banked
  exact-ring family rows mod p, key-exact — validates the W-symbolic
  path against the char-0-proven fam object), E1/grading, two-path
  fold equality, A7 pattern anchor (independent binomial c_n +
  perturbation suite), and phase pert: deliberate formulation
  perturbations (value corruption; slot shift) must be CAUGHT by the
  regression anchors before any run is trusted (front-5 discipline).
  EXECUTED: clean anchors PASS at both primes; A7 4/4 pattern
  perturbations CAUGHT (both primes); phase pert 2/2 build
  perturbations CAUGHT by A-Q2-1 — the anchor net is
  formulation-positive, discharging the front-5 weakness for Q2.

Results of the Q2 runs: SHEET6-R1.md §19 (engine cases/r1_q2_screen.py).
Gate outcome, recorded: the full-locus (LCUT = 1) build ABORTS the 2e7
budget inside the B block alone (1,499 s in) -- the banked ~6e8 raw
estimate confirmed in kind; strata <= 4 are box01/ultramem objects.
The local kill frontier and its mechanism (s1F == 0 forced, ctlB EMPTY
both primes at stratum 13) are SHEET6-R1.md 19.2's content.  Ledger
hygiene: msolve-crash/kill lines annotated INVALID in
runs/r1_q2_runs.log (a 0-byte .out parses as "NONEMPTY" -- flagged as
a runner weakness for the next engine pass; every NONEMPTY line must
be checked against its .out size before being read as a verdict).

Artifacts of this review: /tmp/q2e5_review/ (e5_12_review.py + output,
fam_sub_*.ms subset probes); repo: this file, SHEET6-R1.md §19,
cases/r1_12_sat.py (additive corr phase), cases/r1_q0_gate.py (famctl
path), cases/r1_q2_screen.py (new), systems/r1/r1_12sat_corr*,
r1_q0_fam_ctl*, r1_q2_* emissions + runs/ logs.
