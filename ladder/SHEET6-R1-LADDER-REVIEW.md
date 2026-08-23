# SHEET6-R1-LADDER-REVIEW.md — Consolidated adversarial review of the R1 tier ladder (secs 13–16, e8839bb..3913087)

Reviewer: Claude (adversarial pass, 2026-08-11). Status: COMPLETE.
Scope: the four unreviewed tier results SHEET6-R1.md §13 (4-leaf
decomposition + relation E), §14 (323-eq minimal ext + r<=6 slot
closure), §15 ((1,2) leaves + mod-5 free closure + depth-84 plan), §16
(Q0 gate; "minimal branch SURVIVES depth-84 by explicit point; F_s
ladder EXHAUSTED"). Ground truth: SHEET6-TEMPLATE.md 1b, 2c (E5, E6);
r1_experiment.py stage-0 gate; the ORIGINAL banked artifacts in
systems/r1/. Tools: review-owned evaluator (no FC.parse_eval;
/tmp/ladder_review/f12_witness.py, f3_slots.py), msolve 0.10.1, full
engine re-runs (r1_decompose, r1_12_decompose, r1_minimal_ext guards,
r1_q0_gate both primes), deliberate-perturbation runs. Repo emissions
untouched: 44/44 sha256 vs /tmp/q0_regression_baseline.sha before AND
after this review.

Verdicts:
- Front 1 (the witness itself): **CONFIRMED.** Independent re-verification
  by evaluation at both banked primes.
- Front 2 (zero-extension legitimacy / s1F): **SURVIVAL INTERPRETATION
  REFUTED.** The Q0 "survival" is exactly an s1F = 0 relaxation
  artifact — the ZZ-leaf lesson one level up. Computations correct;
  verdict object mis-specified. Mechanical kill certificate banked
  (saturated Q0 GB = [1] at both primes).
- Front 3 (slot/grading arguments): **CONFIRMED** (re-derived + 462k-term
  audit).
- Front 4 (cover certificates + char-0): **CONFIRMED** (one open caveat
  correctly labeled in §15.3: leaf12_UZ char-0 stays evidence-tier).
- Front 5 (anchors): **WEAKENED.** Discriminating for fold errors;
  provably blind to the Q0 row formulation (pattern c_n) — and the Q0
  verdict is c_n-independent, so the "quotient tie by point" content is
  weaker than stated.
- Front 6 (engines): **CONFIRMED reproducible** end-to-end.

**NET: "F_s ladder EXHAUSTED, minimal branch survives depth-84 by
explicit point" DOES NOT STAND as an intended-locus statement. The
relaxed ladder survives; the TEMPLATE-CONFORM (intended) witness family
is KILLED at the depth-84 quotient tier at both banked primes** (proof
below, sec 2). No arithmetic or soundness flaw was found anywhere in
the four tiers — the pipeline is clean; the failure is a verdict-object
mis-specification: the tie scale s1F was carried as a free unknown with
no nonvanishing side-condition, although the template forces it
nonzero, and the banked GB itself contains s1F (§16.3 recorded
"s1F == 0 on the ENTIRE Q0 variety" as a structural finding without
drawing the inference).

## 1. Front 1 — the §13.4 witness vs the ORIGINAL artifacts: CONFIRMED

Review-owned parser/evaluator (written for this review, no engine
evaluation code), both primes p = 105337 / 105673, witness from
ME.witness_point (W1 = 32284 / 90918, W2 = 1, banked values match):

| artifact | p=105337 | p=105673 |
|---|---|---|
| r1_full_core.ms (ORIGINAL 105 eqs, char-0) | 105/105 vanish | 105/105 vanish |
| r1_full_core_p*.ms (p-variant) | 105/105 | 105/105 |
| r1_reduced_core.ms (56) | 56/56 | 56/56 |
| r1_minimal_ext.ms (323 = 105+2+216) | 323/323 | 323/323 |
| r1_12branch_core.ms (105, s1 = 0) | 105/105 | 105/105 |

The §14.2 guard-E vacuity claim (0/216 F_s rows nonzero at the witness)
is independently reproduced, and STRUCTURALLY: every one of the 462,026
monomials of the 216 F_s rows contains at least one variable that is
zero at the witness (no cancellation involved; f3_slots.py (d)). The
ladder is not vacuous at the certificate level: the witness is a
genuine point of every emitted system. What it is a point OF is the
front-2 question.

## 2. Front 2 — zero-extension / s1F = 0: THE SURVIVAL IS AN ARTIFACT

The template requires the tie scale to be NONZERO on the intended
locus. Chain, all printed/banked:
- TEMPLATE 1b: H_F is the LEAD of p_h1 at F_s (deg 168 = 8·21 pattern
  H_F·p21^8); leads of forced-degree patterns are nonzero (E2/E3
  leak-free counts 16 = 16, deg p_h1,Fs = 168 forced).
- TEMPLATE 2c E5: w_i^4 = -(4/3)H_M(a_i-b)/(243 s0 S_M^3 (a1-a2)^4
  a_i^2 c_i), "pins w_i^4 (nonzero, solvable: a_i != b)";
  r1_experiment.py:1032 stage-0 gate asserts exactly this. So w_i != 0
  <=> H_M != 0 on the intended locus.
- TEMPLATE 2c E6: H_M = H_F · 7^16 A^21 c_m^5/2^8 (unit factor):
  H_M != 0 <=> H_F != 0 <=> s1 = H_F^3/S_F^4 != 0 (S_F = 1 gauged).

The witness has W1, W2 != 0 (that is the POINT of the UU chart). Its
own w-data therefore pins, through the E5 relation the §13.0 diagnosis
itself identified as dropped by the relaxation, a NONZERO H_M — and I
computed it: the E5-implied H_M agrees between the two poles (as it
must, since E is exactly the consistency combination — 71495 at
p=105337, 19010 at p=105673) and is NONZERO at both primes; the
E6-implied H_F and s1 = H_F^3 are nonzero at both primes
(f12_witness.py). A template-conform depth-84 extension of THIS witness
must have s1F != 0.

The banked Q0 result says the opposite is forced: the reduced GB at
BOTH primes contains s1F as a basis element (runs/r1_q0_p*.ms.out:
first element "1*s1F^1") — s1F == 0 on the ENTIRE Q0 variety. Decisive
mechanical certificate, banked this review: adjoining the Rabinowitsch
row s1F*tSAT - 1 to the emitted r1_q0_p*.ms gives **GB = [1] (EMPTY) at
both primes** (/tmp/ladder_review/q0_sat_*.out, ~1 s each).

Consequence table:
1. The zero-extension (all 37 unknowns = 0, s1F = 0) is a legal point
   of the RELAXED variety only. Setting the fresh band/quotient TAILS
   to 0 is legitimate (they are free template parameters; no dropped
   row forces them nonzero). Setting s1F = 0 is NOT: the dropped
   E5-quartic/E6-transport tie forces s1F != 0 at any w != 0 point.
2. Q0 in fact PROVES (mod both banked primes): the sec-13.4 witness
   family admits NO template-conform depth-84 extension — H_F = 0 is
   forced on all of it. Correctly read, Q0 is a KILL of the intended
   locus over this witness family, not a survival.
3. The §15.6/§16.4 pre-registered semantics conflated "Q0 consistent"
   with "witness survives". The operative row should have been the
   third bullet ("the intended E5 fourth-root data is incompatible with
   the depth-84 tie, but the relaxed locus survives") — whose own
   trigger ("witnesses die") never fired only because the verdict
   object omitted the nonvanishing. Q1 (multi-witness sweep) and Q2 are
   therefore NOT discharged; both must run under saturation semantics.
4. Same artifact one level down, already banked without comment: the
   (1,2) witness (§15.2) sets s1 = 0 in its OWN core — the h2-tie
   scale, which the template forces nonzero by the identical E4/E6
   chain. The (1,2) survival certificate carries the same caveat.
5. Naming nit: the Q0 rows use s1F LINEARLY as the quotient lead
   (s1F = H_F); the rows.txt comment calls it the cube-tie scale
   (H_F^3 = s1F S_F^4). Harmless here (0 = 0 either way), but the R2
   emission should fix the name before a nonzero tie value matters.

What survives front 2: the RELAXED-ladder statements — "no F_s band or
quotient row can exclude the relaxed witness at the banked primes" —
are true and now doubly verified. §13's own E5-consistency finding
(the intended data satisfies E identically) is untouched. What dies is
the inflation to "the branch survives depth-84 / F_s ladder exhausted".

## 3. Front 3 — slot/grading arguments: CONFIRMED

(f3_slots.py, both label-level and term-level.)
- Grading 12n+s == 0 (mod 42) (the §14.0 sign correction): holds on
  all 216 Fs-band labels, all 91+136 banked fsjet keys, all 216 wf.pkl
  rows, all 324 depth-84 WF keys (gate re-run). Hand checks: (n,s) =
  (3,6): 42; (2,18): 42; (5,24): 84 — all == 0 (mod 42). Per-slot
  residues n mod 7 = {6: 3, 12: 6, 18: 2, 24: 5}, and at depth 84
  {42: 0, 48: 3, 54: 6, 60: 2, 66: 5} — matches §15.4 exactly (solve
  2n == -s/6·3 (mod 7)).
- Term-level: every monomial of every emitted F_s row has var-slot sum
  (slot = level - 12; radicals 0/20/25) EXACTLY equal to the row slot
  s — 462,026/462,026. Slots are genuinely additive: the 15.5 premise
  is sound. No pins (A_i, W_i) occur in the r <= 4 rows (W-free claim
  confirmed).
- §14.3 r <= 6 closure: witness-nonzero x-slots are {35, 40} only
  (re-measured); possible x-sums {0, 35, 40, 70, 75, 80, ...} never
  hit the required rung-5/6 residual sums {30, 10, 5} / {36, 16, 11}.
  Correct.
- §15.5 mod-5 obstruction: brute force over 20a+25b+35c+40d: s in
  {30, 36, 42, 48, 54, 66} have NO representation; s = 60 has exactly
  the three claimed ((3,0,0,0), (1,0,0,1), (0,1,1,0)). Correct — and
  A4/A6 verify the conclusion by direct measurement anyway.

## 4. Front 4 — cover certificates + char-0 claims: CONFIRMED

- Cover (i)/(ii)/(iii): re-run (both engines): tautology PASS; Z-side
  forcing is sound (2HW_i^2 = 3W_i^2 at W_i = 0 gives HW_i = 0, char
  != 2); ZZ origin points verified EXACTLY by the review evaluator:
  minimal reduced core 0/49 rows nonzero at (x = 0, W = HW = 0), (1,2)
  core 0/98 at (x = s1 = 0, W = HW = 0), both primes; (1,2) W-loaded
  constant census reproduced (rows 87–96 nonzero iff some W != 0).
- Guard tables §13.2/§15.2/§14.2: re-run, all PASS, values match.
- Char-0 claims re-run from the banked artifacts: leaf_ZU GB = [1],
  leaf_UZ GB = [1] (§15.7 upgrade), leaf12_ZU GB = [1] — all over Q,
  ~1 s / 77 s; leaf_UU and leaf12_UU both 121-elt reduced GB over Q.
  leaf12_UZ char-0: NOT re-attempted past timeout — §15.3 correctly
  keeps it evidence-tier (the one honest gap in the char-0 table).
- Leaf p-screens: all reproduce the banked pattern (minimal ZZ 36-elt
  GB / ZU [1] / UZ [1] / UU 15-elt at both primes; leaf12 ZU/UZ [1],
  UU 15-elt at both primes). Exception: the leaf12_ZZ wfree GB run
  (banked 188 s / 14.8 GB) did not finish within this review's 600 s
  cap under parallel load — immaterial: leaf12_ZZ NONEMPTY is exactly
  proven by its origin point, verified above by direct evaluation at
  both primes, which is §15.3's own primary certificate.
- leaf_UU.ms and leaf12_UU.ms are byte-identical files; the 5 rows are
  literally ±E — the "(1,2) shares the identical terminal core"
  headline is exact at artifact level. The §13.1 E5-consistency
  identity re-derived in exact Q(sqrt3) arithmetic: terms +sqrt3/3,
  -sqrt3/3, sum identically 0.

## 5. Front 5 — anchor discrimination: WEAKENED

Deliberate-perturbation tests (perturbed COPIES under /tmp; repo
untouched):
- Sign flip in W_F (g^2 + f^3): **caught** — anchor A2 (E1 slot-0)
  assertion fires.
- Slot-index off-by-one (pin series entries shifted lv -> lv+1):
  **caught** — the two-path fold equality (linear vs suborbit-Newton)
  fails before any anchor is even reached.
- A5's absence-verification methodology (perturb the barred tail,
  assert W_F unchanged) re-ran clean at both primes; the 39 -> 36
  refinement is genuine and correctly reasoned.
- BUT the pattern c_n — the actual "quotient == c·p21^8" formulation
  content — is outside the anchor net: c_n enters only at phase_emit,
  AFTER all anchors. Perturbing it with a WRONG SIGN (B = -3/2) and a
  WRONG INDEX SHIFT (n -> n+7) produced byte-different Q0 systems with
  the IDENTICAL verdict (4-elt GB, s1F in GB, NONEMPTY) and no anchor
  or guard fires. §16.0's "shift correctness is anchor-checked against
  the measured row support" is NOT discharged: all 54 measured
  constants vanish at the witness, so there is no support to check the
  shift against. The 6 anchors validate the FOLD (thoroughly — A1b's
  full-cofactor exact-ring comparison is strong work); they validate
  nothing about the verdict object, and the verdict is provably
  c_n-independent. This is the anchor-level shadow of front 2: a Q0
  whose PASS is insensitive to its own pattern was never testing the
  quotient tie — only whether the witness's slot-60 content vanishes.
  It does; that is the H_F = 0 kill signal.

## 6. Front 6 — engines: CONFIRMED reproducible

All re-run this review, byte/value-identical to banked results:
r1_decompose guards + cover + e5check + witness (rank-1 factors,
row40 = -81E, witnesses both primes); r1_12_decompose guards + cover +
witness; r1_minimal_ext guards A–E (incl. the 0/216 vacuity flag);
r1_q0_gate gate at BOTH primes (~95 s each; regenerated rows/cn/occ ==
banked gate_p*.pkl exactly; zero-extension constants 0/54 nonzero);
Q0 msolve runs (4-elt GB, s1F first element, both primes); 44/44
emission sha256 vs the pre-Q0 baseline. Scope note: the 44-file
baseline covers systems/r1/*.ms|rows.txt only — the leaves/ tree is
guarded separately by r1_12_decompose's own 16/16 sha gate (re-ran
clean). No stale-state discrepancy found anywhere.

## 7. THE CALL + R2 mandates

The four tiers are computationally sound, and §13's structural content
(4-leaf cover, relation E, E5-consistency identity, ZU/UZ char-0
emptiness, ZZ as artifact) plus the §14/§15 band closures stand as
RELAXED-system results. The headline does not: **the survival at
depth-84 is an s1F = 0 artifact of exactly the shape §13.0 diagnosed
in the ZZ leaf** — the relaxation dropped the E5-quartic/E6-transport
tie, the only constraint linking the (nonzero) witness w-data to the
F_s quotient scale, and the "surviving" point violates it. Correctly
read, Q0 shows the intended-locus witness family DIES at the depth-84
quotient tier at both banked primes (saturated GB = [1]); the F_s
ladder is NOT exhausted for the intended locus, because Q1/Q2 never
ran and their triggers were mis-specified.

R2 build (and any Q1/Q2 re-run) MUST incorporate:
1. SATURATION DISCIPLINE (standing rule candidate): every template
   quantity the print forces nonzero (tie scales s1/s1F, leads
   H_M/H_F, w_i, the E5 k_i) carries an explicit Rabinowitsch
   nonvanishing row in ANY verdict object; "GB != [1]" and explicit
   points are template-meaningless without it. This is now the SECOND
   same-shape artifact (ZZ leaf; Q0) — a third is preventable.
2. Emit the deferred E5 quartic rows (w_i^4 = k_i alpha_i^2 with H_M
   restored as a variable, or equivalently the E6 tie linking the
   banked G_m-window quotient scale to s1F) into the ladder — the
   dropped constraint that makes the zero-extension illegal.
3. Q1 re-scoped: multi-witness Tonelli/embedding sweep asking the
   RIGHT question — does any UU witness family admit s1F != 0 at
   depth 84? (The E5/E6 chain predicts NO for every w != 0 witness;
   confirming that mechanically = a genuine mod-p kill of the minimal
   branch at the F_s quotient tier, a much stronger result than the
   current claim.) Q2 (leaf-compressed quotient p-screen) saturated
   at s1F.
4. A pattern-positive anchor for any future quotient gate: a synthetic
   H_F != 0 control point must reproduce WF(n,60) = H_F·c_n — the
   current anchors cannot see c_n at all (front 5).
5. (1,2): the same saturation caveat applies to its banked s1 = 0
   witness; its "survives core" verdict needs the s1-saturated re-run
   before the shared-terminal-core symmetry is leaned on.
6. Minor: fix the s1F naming (lead vs cube-tie scale) in the Q0
   emission comment before nonzero values matter.

Artifacts of this review: /tmp/ladder_review/ (f12_witness.py,
f3_slots.py, q0_sat_*.out saturation certificates, q0_sign.py /
q0_slot.py / pattern-perturbation outputs, char-0 and wfree leaf
re-run outputs, r1q0_backup/). Repo: this file only; no emission
touched (sha-verified).
