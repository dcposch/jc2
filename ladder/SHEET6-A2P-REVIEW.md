# SHEET6-A2P-REVIEW.md — Adversarial review of SHEET6-AF2 (2934a2d) and SHEET6-2POLE (284d847)

Reviewer: Claude (adversarial pass, 2026-08-07). Status: COMPLETE.
**2026-08-28 supersession.**  This dated review correctly found the local
AF2 pricing and the interior two-pole witness.  It did not prove printed
equation (22), and literal `Y(F)` is nested.  Actual-weight Corollary 7.1 is
now review-closed, and MFE supplies the global selected-exit union with a
shared suffix counted once (`c74fc0f9...`).  This does not restore printed
`(22)` or a full literal `sum lambda` equality.  Corrected Proposition 8.4
is nonroot only.  The mixed-root edge theorem plus MP1+MP4+MP5/D5 now
excludes the `td=6,m=2` pole-chain root-meet branch analytically, while
broader root routes behind earlier `M>=2` jumps and off-axis/SF1
completeness remain open.
Scope: the two unreviewed load-bearing results (AF2-IIb pricing + two-pole
configuration). Ground truth: refs/sigray_full.pdf read on-page this
review (pp. 16-19, 24-35, 38-47, 48-60 — every formula quoted below
re-read from the page images, independently of the docs under review).
Engines re-run: sheet6_campaign.py gate (PASS), hiii_compose.py baseline
+ iib, twopole_check.py, PLUS one new cross-run (twopole under derived
IIb pricing, §7). L1 explicitly out of scope (separate thread).

Verdicts:
- Front 1 (E6, sign of (24)): **CONFIRMED — printed sign is wrong, the
  campaign's fix is right** (proof's own false middle identity + all three
  p. 53 usages compute the minus version)
- Front 2 (lambda_IIb derivation): **CONFIRMED** (every step re-derived
  from printed statements; no free reading exists; NEW corroboration:
  9.8-9.10 print "In the case lambda_F = 0 ... p = (eta^nu-c^nu)^mu",
  i.e. the thesis itself equates lambda=0 with k=0)
- Front 3 (gap=7 arithmetic): **CONFIRMED** (recomputed from thesis
  definitions; the (nu,n) = (7,11) cell is the UNIQUE solution of its
  Diophantine, so the kill closes the whole mu=4 k=1 branch)
- Front 4 (shared budget): **CONCLUSION CONDITIONAL ON MULTIPOLE
  DISJOINTNESS**. Cor 7.1 is one global inequality, but the union of two
  chains may be summed only after their first-exit flags are proved pairwise
  distinct with the shared suffix deduplicated. Printed (22) is not a basis.
- Front 5 (merge legality / 8.4 entry points): **CONFIRMED** (8.4's proof
  audited line-by-line: singleton enters ONLY via the two Prop 8.3
  invocations; no statement forbids the lambda=0 merge; St 8.5 explicitly
  exempts V_{2,a})
- Front 6 (exhibit + sweep): **CONFIRMED** (full hand re-chase passes;
  52389/50097/1373/336/3/9/0 all reproduce; one cosmetic slip: "96.6%"
  is actually 95.6% of solved, 96.7% of killed)
- Front 7 (cross-consistency): **WEAKENED (bookkeeping only)** — the
  two-pole run used LEGACY IIb pricing (flag never set): under the
  AF2-derived rule the book drops 3 residues/9 IV classes -> 2 residues/
  6 IV classes (verified by re-run: A' repriced out, B loses both
  Sigma=3 classes); plus a new sharper-AF3 observation
  (M_pole = gcd(deg p, deg p_g)) that would kill residue B at entry and
  makes r10/M4 vacuous — kill-direction only, exhibit A untouched.

## 1. Front 1 — E6: the sign of (24) decided independently

Verdict: **CONFIRMED**. Read before anything else, as instructed; the
printed sign is refuted by the thesis's own proof and all of its own uses.

- St 9.3 statement (p. 49) verbatim-matches the AF2 doc's quote, including
  the misprints it reports ("=>=" in the proof display; "mult(p_F,c_1)"
  for "mult(p_F,c*)"). One additional sub-slip the doc did NOT list: the
  proof display's final term is printed "kappa_H(pi(F)-1)" (H for F) —
  same benign family.
- The proof chain (p. 49): "kappa_H(w-1) >= kappa_F(w-1) = kappa_F(w-u) -
  kappa_F(u-1) >= kappa_F d_F/mult(p_F,c*) - kappa_F(u-1)". The middle
  identity is FALSE: kappa_F(w-u) - kappa_F(u-1) = kappa_F(w+1-2u) !=
  kappa_F(w-1) unless u = 1. The true decomposition w-1 = (w-u)+(u-1)
  gives kappa_F(w-1) = kappa_F(w-u) - kappa_F(1-u), and with kappa_F(1-u)
  = kap-bar_F the conclusion is D_F/mult(p_F,c*) - kap-bar_F: the MINUS
  version. The printed statement's "- kappa_F(pi(F)-1)" = +kap-bar_F is
  exactly the propagated error. (kap-bar > 0 on all relevant vertices:
  St 9.1, St 9.2(iii), every printed Q-datum.)
- All three quantitative usages (p. 53) instantiate the minus version, as
  claimed: (A) lambda_F >= 2 with D_F/i = 7j/j = 7, kap-bar = 5: 7-5 = 2;
  (B) lambda_F >= 3 = 9-6; (C) per-root 1 = 5-4, "Since k = 2, lambda_F
  >= 2". The plus version gives 12, 15, 9 — incompatible with the printed
  possibility lists (9.6(iii)/(iv)).
- E7 also re-verified on-page: 9.6's (a)/(b) print (eta^nu-c^nu)^2 inside
  q, while the SAME proof computes deg q = (k+1)nu+1 (p. 52-53) and
  9.7/9.8's printed q-patterns carry the c-orbit to power 1 with the eta
  factor. Cosmetic, as filed.
- Conclusion: E6 stands exactly as filed (statement AND proof, sign
  family "(pi(F)-1)" for "(1-pi(F))"). The campaign's "fix" is NOT the
  error; the AF2 derivation does not invert. And §4's kill is
  sign-robust anyway (17 > 3 under the printed literal), so no verdict
  in either doc hangs on E6.

## 2. Front 2 — the lambda_IIb derivation, step by step

Verdict: **CONFIRMED**; the "no free reading" claim survives an explicit
hunt, and is now BETTER supported than the doc itself states.

- (R1) corrected: St 3.18 supplies the realizable microstep `E=F*_kappa
  (eps*c)`, while Prop 3.2 separately names the next vertex `F+c`; they need
  not coincide.  Prop 6.7 gives `E in T_a+` (`deg p_F=36j>1`).  If the raw
  sign is down, repaired Prop 6.8 transports that microstep to the next down
  vertex on the same branch.  This Prop 6.7/6.8 composition (`c3d6ff92...`,
  sweep correction `581219e0...`) replaces the earlier microstep/vertex
  conflation and is different-model review-closed (`eb37373b...`, mandatory
  correction `050ccddd...`; Lemma 6.1 R2/review/correction
  `2fdbbee9...`/`5193e7b0...`/`607e0dcf...`).
- (R2) re-verified after that repair: the exact microstep calculation is the
  same inequality as St 6.2; multiplying by kappa_F > 0 turns it into
  `gap(c*)<0`.  Regularity forbids a down alternative next vertex, and
  Statement 6.1 forbids equality, so every alternative gap is positive and
  its microstep climbs with no further regularity input. Independent
  cross-check: St 8.2 (p. 41) is a second printed form of the same test
  (its proof shows sign(d_F - (1-pi)mult) = sign(deg p - deg q * w)); on
  the IIb grammar dp - dq = (mu-1)nu > 0, so the 0-root and all simple
  extras climb in EVERY solved IIb cell — i.e. inside IIb the max(1,.)
  floor and its H4 crutch are never even engaged. A strict tightening
  beyond AF2 §2 R2.
- (R3) re-verified locally: St 7.3 supplies H on the alternative subtree;
  that subtree first separates at F, so H belongs to F's repaired exit set.
  Corrected (24) prices gap(c*), and
  gap(0)/nu_F for c* = 0 (mult(p_F, .) = i*w by Prop 8.1(i), whose proof
  prints deg(p) = deg(p_F)/i = M*_F).
- (R4) absorption hunt (the strong local claim): the repaired
  `lambda_F^exit` sums the flags owned at this first separation, so the only
  free reading would be
  H(0-branch) = H(c_1-branch) as tree vertices. Blocked: branches
  separate at F, contact pi(F) < 1 < pi(H) (St 7.1, p. 35), so the two
  cv vertices are distinct members of the exit set. Other candidate readings all
  fail on printed text: 0 cannot be the searrow continuation in (b)
  (mu >= 2 = mult(p,c), and p. 54 prints "In the case (b) F + 0 in
  T_a^nearrow, therefore lambda_F >= 1" — verbatim, as quoted); the k
  extras cannot be dropped (the cell's own ratio equation contains them);
  they cannot be searrow (previous bullet).
- NEW corroboration (this review): 9.8, 9.9 and 9.10's proofs (pp. 55-57)
  all derive the k=0 pattern FROM lambda_F = 0: "In the case lambda_F =
  0, by Statement 3.18 we obtain p(eta) = ⊖(eta^nu - c^nu)^mu" — the
  thesis itself treats extra orbits as incompatible with lambda = 0,
  which is precisely the contrapositive of the per-orbit floor AF2
  derives. There is no reading of these proofs under which (b)'s extras
  are free.
- Perimeter as claimed: the §4 kill uses integer bounds only (no ceil, no
  floors); the general rule's ceil rides the printed St 9.4-proof line
  "kappa_G(pi(G)-1) in N" (p. 49) and the floors ride H4 — both
  pre-existing items, correctly localized.

## 3. Front 3 — the gap=7 kill, recomputed from the thesis (not the engine)

Verdict: **CONFIRMED**, and strengthened: the cell is the unique solution
of its Diophantine, so the exclusion covers the entire branch.

- Entry: table (23) row 10 (p. 46) + St 9.1 (p. 48): Q(G) = (4j,4j,4,4,9),
  rho = 1. IIb mu=4 k=1 grammar dp = (k+mu)nu+1 = 5nu+1, dq = (k+1)nu+1 =
  2nu+1 — this is the thesis's OWN (b)-arithmetic at mu=2 ("gcd((k+2)nu+1,
  (k+1)nu+1)", pp. 53/59) generalized, as the doc honestly flags.
- Prop 9.3(b): (5nu+1)/(2nu+1) = 4(1+n)/(9+n) gives n = (37nu+5)/(3nu+3);
  hand-enumeration: the ONLY nu >= 2 with n in N are nu = 7 (n = 11) and
  nu = 31 (n = 12, killed by (d)-integrality: 12 !≡ -9 mod 4). So
  (nu,n) = (7,11) is the whole mu=4 k=1 family. n = 11 ≡ 3 ≡ -9 mod 4 ✓.
- Child via (c)/(d) + 8.1(i) + 3.17(i): kap-bar_F = (9+11)/4 = 5; D_F =
  (4j + 11·4j)/4 = 12j; i = deg(p_G)/mu = j; deg p_F = 36j; M_F =
  gcd(36,15) = 3; Q(F) = (12j,36j,7,3,5) = St 9.7's own hypothesis shape.
- gap = D_F/i - kap-bar_F = 12 - 5 = 7; gap/nu_F = 1. Climb: 12 < 5 FALSE
  (St 6.2), cross-checked via St 8.2 (15·1 < 36); both the c_1-orbit and
  the 0-root climb with no regularity input. Price (corrected (24)):
  lambda_F >= 7 + 1 = 8 > 3 = td-2 (St 9.5/(26), F sits on the
  characteristic sequence). Printed-literal (24): >= 12+5 = 17 > 3.
- R2 = (2/3,3s+2,3,2s+2) is 9.7(iv)'s lambda=0 child of R1 (p. 54,
  verbatim (iv)), so both residual classes ride the one killed step; the
  baseline engine trace shows exactly this route (ENTRY (1,4,4,9) --mu=4
  IIb k=1 nu=7--> (1/3,7,3,5)@lam1 --mu=3 IIa_0--> (2/3,3s+2,3,2s+2)).
- Engine reproduction (this review): gate PASS (flag off); baseline GRAND
  td5: 2, td6: 13, SF1: 2 = HIII-REVIEW §5 verbatim; `iib` GRAND td3: 0,
  td4: 0, td5: 0, td6: 4, SF1: 0 = AF2 §5 verbatim; r10/M4 iv_hits 7->4,
  SURV 2->0; the 4 td6 classes match AF2's list ((1/3,7,3,5)@2,
  (1/4,5,4,4)@2, (2/3,3s+2,3,2s+2)@2, (3/4,4s+3,4,3s+3)@2 on r9/M2 and
  r9/M6, R in {3,4}). The r8/M6 SF1-killing step also re-checked by hand:
  child (1/5,7,5,3) has gap = 10-3 = 7, lambda >= 8 > 4.

## 4. Front 4 — is the two-pole budget shared?

Current verdict: **CONDITIONAL PASS.** A shared sum is the strongest valid
form once the two chains' first-exit flags are globally deduplicated; that
multipole disjointness lemma is not supplied by the singleton Section 9
repair.

- The reviewed actual-weight theorem `c253bd12...` / `727f5850...` gives
  `td >= 1 + Sigma kappa_F(pi(F)-1)` over any **pairwise distinct** set of
  cv flags.  This no longer rests on printed Prop 7.5 (22) or literal
  `delta_a`. Nothing in the resulting inequality is
  per-pole; td is never split between poles except in Prop 5.8's (20),
  which is a statement about pole ORDERS (Lambda), not lambda-budgets.
- If the union `C_1 union C_2` is replaced by globally defined first-exit
  sets and the shared suffix is counted once, a proof of cross-chain
  distinctness would let Cor 7.1 apply directly and give
  `Sigma lambda^exit <= td-1-psi = 5-psi` shared.  That distinctness proof
  is presently owed. A per-pole <=4-each reading is a
  strictly weaker corollary (apply 9.4 per chain); a per-pole-2-each
  reading has NO printed basis. The 2POLE doc used the strongest
  constraint available — adversarially safe.
- Exhibit budget re-verified: psi = 2 is certified (psi*l_f = 84 < 126 =
  k_f), budget 3, Sigma lambda = 2, slack 1.
- The old H2 rider is now resolved only for a singleton chain.  Under the
  LITERAL Not 9.3
  ("exists P: F = I_P(u) and H = I_P(pi(H))") a cv vertex charged at F_j
  also lies on branches through every lower chain vertex, so literal
  Y-sets are nested-overlapping.  The singleton first-separation theorem
  replaces this reading convention.  Its multipole cross-chain analogue is
  the remaining condition in this front.
- lambda_{pole} = 0 re-verified as printed-supported: Prop 5.5 (p. 26,
  g(P) = infty iff the branch meets T_{a,pole}) + St 3.15(ii) (d_g = 0
  gives g(P) in C*) + St 7.2: a branch through a pole vertex cannot carry
  a cv vertex, so Y(P_i) is empty. (Load-bearing for Sigma lambda = 2;
  any contrary reading would equally break the thesis's own single-pole
  chains at td <= 5.)

## 5. Front 5 — merge legality; Prop 8.4's proof line by line

Verdict: **CONFIRMED for nonroot starting vertices and the interior merge
analysis.**  The root is excluded from corrected Proposition 8.4.

- Corrected Prop 8.4 proof (pp. 44-45), full inference inventory, starts at
  a **nonroot** down vertex: (1) sequence
  F_0..F_n descends and lands at (0,y) — Props 6.7/6.8, unconditional;
  (2) "From Proposition 8.3, and by induction we have M_H = 1" — the ONLY
  consumer of the singleton hypothesis, via 8.3's regularity hypothesis;
  (3) Bezout representation of M_H = 1 — St 8.1, unconditional; (4) the
  (k,l) transport — Cor 6.1 + Prop 6.3, unconditional; (5) k = 1 uses
  deg = mult at (0,y), i.e. 8.3(iii)'s one-root p_{(0,y)} — the SAME
  entry point (last induction step); (6) l in N contradicts Thm 6.1.  If
  the starting vertex itself is `(0,y)`, the sequence has length zero and
  this proof does not start.
  NO second entry point exists. Notably the printed proof never justifies
  8.3's hypothesis at all — singleton => regularity is supplied by 2POLE
  §1b's Prop 6.8 subtree argument, which this review re-derived and
  finds sound (incomparable predecessors, deg p >= 2 by St 3.16, a pole
  weakly above each by 6.8, disjoint subtrees => two poles).
- Prop 8.3's hypothesis as printed ("for any H ... G != H°") contradicts
  its own setup (H = F); the regularity reading (H != F => H° != G, =
  Not 9.2 p. 48) is the unique coherent one. 2POLE reports this
  correctly; it is effectively one more erratum of the E5/E6 family.
- Merge-forbidding hunt (does ANYTHING kill the lambda=0 merge?):
  - St 8.5 (p. 42) — the M-transport — explicitly assumes G not in
    V_{2,a}: the thesis's own M-machinery is fenced off merge vertices.
  - St 8.4: mult(p,c) | M_G holds edge-wise (1 | M_{P_i}) — no kill.
  - St 8.2: both tests pass (10·1 > 6 both edges; != holds).
  - Prop 5.3(v) (squarefree at poles) only shows G_m is not a pole —
    used by the doc, no kill.
  - Prop 9.3's case list covers V_{1,a} cap V_{2,a} vertices via (II);
    (a)-(d) apply; no exclusion.
  - The single-orbit conclusions in 9.6-9.11 are all derived "From
    Statement 6.2 and FROM THE REGULARITY ASSUMPTION ... mult(p,c*) <
    mult(p,c)" (printed pp. 52, 55, 56, 57, 58) — at G_m regularity fails
    by construction, so the second searrow orbit contradicts nothing
    printed. M(G_m) = gcd(dp,dq) = gcd(6,10) = 2 by Prop 8.1(v)
    (unconditional). The mu=1 auto-kill (gcd(nu, n nu+1) = 1) is indeed
    broken exactly there.
  - St 3.16's structure p_F = eta^l p~(eta^nu) (p. 17) is CONSISTENT
    with the merged two-orbit pattern but does not prove the q-side
    per-root rule — M-PAT remains a genuine flagged hypothesis, correctly
    tiered with H1/H4 in §8. The searrow-orbit-uncharged rule is sound:
    St 9.3 requires F + c* in T_a^nearrow, and searrow directions are
    not in T_a^nearrow (St 6.1); q-only orbits give no direction at all
    (St 3.18: directions <-> roots of p).
- Also verified: 9.12 (p. 60) carries its own "T_{a,pole} = {F}"
  hypothesis and the final Thm 9.1 chain (9.1 + 9.12) covers only the
  singleton case — 2POLE §7.2's "fourth structural gap" description of
  the printed td=6 ambition (§9 intro p. 45 announces the extension to
  td 6) is accurate: no §9 statement addresses a second pole.

## 6. Front 6 — the exhibit re-chased; the sweep re-run

Verdict: **CONFIRMED** (one cosmetic percentage slip).

- Configuration layer re-derived: td = 6 with two poles forces Lambda =
  3+3 (Prop 5.8 (20), p. 28), Lambda >= beta (Prop 5.7, p. 27) forces
  beta <= 3, so (alpha,beta) = (2,3) and row 1 is the unique Lambda=3 row
  of (23) (p. 46: (2,3),(2,3),(2,3),nu=2). Q(P_i) = (2,2,2,·,5) with
  kap-bar = 5 by St 9.1; p = eta^2 - c^2 (5.3(v) + 5.4).
- Merge step (every datum recomputed): edge equation (b) mu(rho+n)/
  (kap+n) = 6/10 = dp/dq with n = 5 ≡ -5 mod 2; (d): kap_m = (5+5)/2 = 5
  in N; (c): D = 6; i_0 mu_i = 2 = deg p_{P_i} (St 3.17(i)), i_0 = 2
  realized absolutely; M = gcd(6,10) = 2 (8.1(v)); searrow both edges
  (8.2); lambda_merge = 0 (k = 0; the l=1 orbit lives in q only — no
  direction, no charge). Q(G_m) = (6,12,3,2,5).
- Suffix: Q(G_m) is LITERALLY the 9.6 hypothesis shape (j,2j,3,2,5) at
  j = 6, and the step to (42,126,7,3,5) is the thesis's own case (A)
  (dp/dq = 21/15, n = 10, lambda >= 2 printed at 9.6(iii)); terminal
  checks (j) 5<7, (k) 294/7 = 42, (l) R = 3, (m) 42·3/126 = 1; root
  (k_f,l_f) = (126,42), (k_g,l_g) = (189,63) in N^2, k_g/k_f = 3/2 not
  in N* (Lemma 2.1(iv)), Thm 6.1 ok; psi = 2; Sigma lambda = 2 <= 3,
  slack 1 — robust to lambda_root >= 1, as claimed.
- Sweep reproduction (this review's run): phase 1: 163 shapes, 5 OPEN
  III-kinds; phase 2: 52389 solved, kills 50097 (restored-8.4) + 1373
  (suffix DEAD) + 336 (N1), residue = 3 classes (A, A', B) with 9
  deduped IV classes (engine prints 10 rows; (2/3,3s+2,3,2s+2)@3 is
  shared by A' and B — dedup 9, matching §6b); phase 3: 0 root merges.
  COSMETIC SLIP: 50097/52389 = 95.6% (or 96.7% of the 51806 kills) —
  the doc's "96.6%" matches neither; absolute counts all exact.
- Hand spot-checks: survivors — residue A (fully, above) and residue B's
  merge (mu = (2,2): 2(1+5)/(5+5) = 6/5 = 30/25, M_m = gcd(30,25) = 5,
  kap = 5, gap = 6-5 = 1, lambda_m = 1; its self-IV data (j) 5<6, (k)
  36/6 = 6, R = 5, (m) 1, psi = 4, 1 <= 1 boundary). Kills — (i) the
  mu=(1,1) l=0 family: n = 8nu-1 (parity ok) solves for every nu and
  every child has M = gcd(2nu, 2nu+1) = 1: restored-8.4, the 96%-bucket;
  (ii) A-child at Sigma-lambda = 2: every IV route needs lambda >= 2
  more, 4 > 3 = psi-budget: suffix-DEAD (consistent with A' existing
  only at Sigma <= 1); (iii) root merges: mu_i = 1 fails 8.2 at the
  I-like root pattern (mu_i(k+2) > mu_1+mu_2+k forces mu_other < 1) and
  mu = (2,2) needs two kap<nu M>=2 parents at cost 3+3 > budget —
  engine's 0 raw hits consistent. Root-merge code note: the first `ok =`
  assignment is dead (immediately overwritten by the correct
  `tot <= 5 - psi`); harmless.
- lambda_root >= 1 narrowing re-checked: boundary classes (R4 at slack 0,
  R5@1, @3 R3) die, leaving A's two R3@2 classes — as stated.

## 7. Front 7 — consistency across the two results

Verdict: **WEAKENED (bookkeeping only; no verdict flips)**. Three items:

- (a) No double-counting: the single-pole books (AF3-ext 4, SF1 0) and
  the two-pole book sit on disjoint configuration hypotheses
  (|T_{a,pole}| = 1 vs 2). The reappearance of the same terminal shapes
  ((1/3,7,3,5)@2 etc.) in both books is shape-coincidence, not an
  accounting error. AF2 §5's "what remains" list correctly names both
  books; 2POLE §7.1 correctly restates AF2's headline as single-pole.
- (b) REAL missed interaction: twopole_check.py never sets IIB_DERIVED,
  so its suffix ran under the legacy flat-1 IIb price that AF2 had just
  deprecated (the two commits are 35 minutes apart; neither doc notes
  it). Residue B's two Sigma-lambda=3 classes ride a "mu=5 IIb k=0"
  suffix step whose derived price is max(1, ceil(gap/nu_F)) =
  ceil((16s+12)/(4s+3)) = 4, not 1. Re-run this review with
  sc.IIB_DERIVED = True: the effect is LARGER than the suffix alone —
  phase 1 shrinks 163 -> 133 shapes (pre-merge IIb steps repriced too),
  merges 52389 -> 47970 (kills 46337 restored-8.4 / 745 DEAD / 336 N1),
  and the residue book drops to **2 classes, 6 IV classes**: A' vanishes
  entirely (its asymmetric parent (1,3,1,7) reprices 1 -> 4: its own
  mu=2 IIb k=1 pre-merge step has gap 3, so lambda = 3+1; any A'-merge
  then busts the suffix budget), B loses both Sigma=3 classes exactly as
  computed and
  keeps only its two boundary R5@1 classes; A keeps its 4 classes @2.
  The exhibit (residue A) is IIb-free and untouched. RECOMMENDATION:
  make the derived pricing the twopole default and reprint §6b with the
  6-class book (A: (1/3,7,3,5)@2 R3, (2/3,3s+2,3,2s+2)@2 R3,
  (1/4,5,4,4)@2 R4, (3/4,4s+3,4,3s+3)@2 R4; B: (1/5,6,5,5)@1 R5,
  (4/5,5s+4,5,4s+4)@1 R5).
- (c) NEW observation (kill-direction only; for the AF3 thread, campaign
  §6 item 6): Not 8.1 (p. 39) includes h_0 = g in the M-family, and
  Prop 5.1(iii) (p. 24) gives m_F = 0 at pole vertices, so at every pole
  M_F = gcd(deg p_F, deg p_{g,F}) — computable from table (23): row 1
  gcd(2,3) = 1, row 4 gcd(4,6) = 2 (matches 9.6's M = 2), row 8
  gcd(6,15) = 3, row 9 gcd(6,10) = 2, row 10 gcd(4,5) = 1, row 11
  gcd(5,6) = 1. Consequences if adopted: (i) r10/M4 — the carrier of
  the two td5 sanctioned residuals — is VACUOUS at entry (AF2's kill
  becomes doubly covered, its verdict unchanged); (ii) r11/M5 vacuous,
  r8 reduces to M3 (already 0 under iib), r9/M2 stays live so the td6
  book stays 4; (iii) row-1 poles have M = 1, so 2POLE §2c's "both M_i
  in {1,2} live" narrows to M = 1: residue B (mu = (2,2) needs
  mu | M_{P_i} = 2) dies AT ENTRY, and phase 1's M=2 trees are spurious;
  the exhibit (mu = (1,1)) is unaffected. Under (b)+(c) together the
  two-pole book is residue A ALONE (4 IV classes; 2 after
  lambda_root >= 1). Not adjudicated here — it refines a flagged
  hypothesis, does not contradict either result, and every consequence
  is a kill.
- SF1: the dated scan found no interaction, but its global zero count is not
  exhaustive after root-signature `M=1` was restored; AWS rerun pending.

## 8. Overall verdict

Both results SURVIVE adversarial review. Neither is refuted; the two-pole
residue book needs a one-flag refresh.

- SHEET6-AF2 (2934a2d): **local pricing CONFIRMED with the first-exit
  replacement.** E6 is real (front 1); the derivation is review-closed with
  actual-weight Corollary 7.1 rather than printed (22) (front 2, with two
  bonus tightenings found: gap > 0 is automatic inside solved IIb cells,
  and 9.8-9.10's lambda=0 => k=0 lines corroborate the pricing); the
  r10/M4 kill is exact, unique-cell, sign-robust (front 3); the
  historical nonroot/IV recomposition reproduces bit-for-bit (td<=5: 0,
  td6: 4 AF3-ext); the SF1 zero awaits root-aware replay.
- SHEET6-2POLE (284d847): **CONFIRMED on its mathematical core**
  (nonroot 8.4 anatomy front 5; exhibit front 6), **CONDITIONAL on the
  shared-budget disjointness and root recensus, and WEAKENED on
  bookkeeping**: suffix priced under
  the superseded IIb rule (book 9 -> 8 under the derived rule, re-run
  verified), "96.6%" should read 95.6%, and the pole M=2 labels are
  contradicted by the Not 8.1 + Prop 5.1(iii) computation (residue B
  additionally dies at entry under it). None of this touches the
  headline: the lambda=0 mu=(1,1) merge with M(G_m) = 2 and the
  (6,12,3,2,5) -> (42,126,7,3,5) suffix passes every located printed
  constraint with slack 1. Recommend PROMOTE after: (1) IIB_DERIVED
  default in twopole_check, §6b reprinted (6 classes, or 4 citing (c));
  (2) percentage fix; (3) a §2c note on M_pole = gcd(P, P_g).
- CURRENT SUPERSEDING STATE. (a) td <= 5 is review-closed by the corrected
  Section 9 theorem — the last two classes
  (r10/M4) are excluded by a derived, sign-robust, regularity-free
  lambda-bound (and independently vacuous under §7(c)). (b) Single-pole
  td6: historical nonroot/IV book 4 classes (all r9, R in {3,4}); root/SF1
  recensus pending. (c) Two-pole td6: NOT excluded at Q-level; residue book after
  this review's composition (derived IIb): residue A (the exhibit,
  Sigma-lambda 2, slack 1; 4 IV classes, 2 robust to lambda_root >= 1)
  + residue B's two boundary R5@1 classes (which die under either
  lambda_root >= 1 or the §7(c) M_pole computation) — everything robust
  rides the mu=(1,1), l=1 first-step merge to (6,12,3,2,5). L1
  (merged-pattern inadmissibility, out of scope here) remains the single
  lemma that would close the whole book; the exhibit remains the
  distinguished counterexample template.

Artifacts: no engine changes needed for this review (one diagnostic
re-run of twopole under IIB_DERIVED=True, command in §7b). Engines all
reproduce their docs; gate PASS.
