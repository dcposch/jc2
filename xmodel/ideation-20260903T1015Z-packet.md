# Sealed ideation packet — round 20260903T1015Z

Frozen 2026-09-03T10:08:28Z. Basis f5aa1cafd1d848b1b3ccb6b3370972b737f98628 (campaign tree
clean; the excluded jc2-lean worktree is outside the boundary). Prior full
round: 20260902T1608Z (COMPLETE, 5/5; synthesis in
ideation-20260902T1608Z-synthesis.md). This packet is identical for every
blind submitter. Do not read other lanes' submissions for this round.
Coordinator: Opus 5, cloud seat (handoff from the Fable 5.1 laptop
coordinator at 08:33Z; notes.md LIVE STATE — HANDOFF and the 09:59Z
acknowledgment). Round trigger: the 12 h floor (04:55Z) was missed across
the handoff, AND significant events — integration #17 deltas (d)–(h): the
campaign's census was a superset of Moh's search space; the true (1)–(13)
space is now implemented and measured; and (1)–(13) as printed is provably
NOT the whole of Moh's program.

## Mission posture (DC, standing; reaffirmed today)

Resolve JC2 — proof or counterexample. Resolution-first (COORDINATION.md,
2026-09-02 section): one different-model hostile review still gates
promotion; no re-hardening of promoted foundations; up to 5 Opus seats at
the frontier; AWS up to quota (1,920 Std + 548 X vCPU); formalization
non-blocking. DC's words for this round: "be bold, creative, and act with
urgency". The round contract still REQUIRES genuinely new avenues and
cross-connections; endorsed paths narrow nothing.

## Where the campaign stands (direct)

1. N <= 5 is closed, unconditionally (not H2). The frontier is N >= 6.
2. THE BOUNDARY COMPUTES N EXACTLY, AND THE VALUE IS O(1). Reviewed and
   promoted (integration #17 + deltas (a), (c), (f)): JAC-FIBRE
   (ord f + ord g_y = -1 on every branch of a generic fibre of g);
   FRONTIER-EXACT (N = sum over roots of g of (1 - delta^0)^+, a function
   of the g-tree alone — the f-tree is slaved); D1-PIN
   (N = sum_B V_2(B) q(B) over the bottom-major discs B, with
   q = (1 - delta_1) d e / (d + e); floor = ceiling exactly at r = 1);
   D1-STAR; the Phi-lemma; the EXACT-N window L <= N <= U with L/U = V_2/u;
   PIN-NOT-CEILING (min V_2 q = 3/112 at D <= 200, no growth: NO D <= C(N)
   follows from the boundary, for any C); ORTHO-DEFECT
   (2 d e N = sum_nu (e m_nu - d m'_nu)^2). The one-directionality of
   integrations #14–#16 was a property of the contact functional on a FREE
   joint tree only (UPPER-ONLY[CONTACT]); the Jacobian condition does not
   allow the joint tree to be free.
3. THE BOTTOM STAR IS A DESSIN. BOTTOM-ODE d p_f p_g' - e p_g p_f' = kappa
   is exactly the leading-order interpolation condition at one bottom disc
   and is equivalent to (p_f, p_g) being a Davenport–Stothers / ABC-extremal
   pair (STAR-ABC); it is ALWAYS realisable (15/15 triples tested); Moh's
   Prop 4.6 + A.5 already force the squarefree bottom (STAR-REALISABILITY
   closed with ZERO kills). TF-0 (both families squarefree) and the
   TF-DESSIN passport are promoted; existence of the dessin for every
   (d, e, V) is a GAP (the cubic-map construction is (2,3) only).
   NO-RESIDUE ([x^-1] of 1/g_y(x, tau) = 0 on every branch of every fibre)
   is promoted and is a COEFFICIENT-level condition on g alone.
4. THE CENSUS TRUTH (delta (h), reviewed where stated). The day's
   enumerator (box/moh_skeleton_N.py, d1floor.py, general.py) implemented
   Moh's (1)–(7) and the Def 5.1(2) windows only. Moh's search conditions
   (8)–(13) were recovered verbatim from p.201 (box/moh_skeleton_full.py):
   A_{r-1} = reduced denominator of L delta_{r-1}, L = lcm of the reduced
   denominators of delta_s..delta_r; the division (9)
   V_r d_{r-1}/d_r = (triangle) A_{r-1} + (square); (10) V_{r-1} <= triangle
   for a factor pi - a, a != 0; (11) V_{r-1} = j A_{r-1} + square for the
   factor pi; (12)/(13) the A_1 divisibility alternatives at r = 2 (which
   are EQUIVALENT to the proved Galois congruence (10)_1: eV_2 = 0 or 1
   mod A_1, by Moh's p.188 identity A_1 | (n* + m*)V_2 - 1). The true
   (1)–(13) space at 48 <= D <= 120: 1,692 V-assignments / 1,189 groups
   (the calibration lane's 329/287 omitted branch (11): a 4.1x undercount).
   Rebased pinned-N programme (N = sum_B V_2 q, N in Z, N >= 6): 670 groups
   alive; 589 (UNI) / 648 mixed in [6,16]; D = 48 EMPTIED (integrality);
   D = 66, 78 carry no (1)–(13) skeleton; NO D > 100 EMPTIES; D = 105 -> 3
   groups; D = 117 -> 4; D <= 200: 14,016 groups, nothing empties; s <= 5
   FAILS above D = 120 (first s = 6 at n = 192). Moh's six rows pass
   (1)–(13) (fail-closed control). ALL earlier "no degree emptied / 60%
   killed" numbers (#17 A.7, deltas (a)–(e), (g)) are about the (1)–(7)
   SUPERSET — never quote them as Moh's space.
5. DECISIVE NEGATIVE — OPEN[MOH-PROGRAM] (bounded: 652 excess rows, 59
   excess (n,m) classes at n <= 100). (1)–(13) as printed leaves 658 rows
   in 63 classes at n <= 100 where Moh's p.202 table (claimed complete
   output of his program) has 6 rows in 4 classes. Every stricter reading
   of (8)–(13) tried kills printed rows (A_j = den(delta_j) kills 4 of 6).
   Automatic on the census, hence NOT the missing filter: d_s does not
   divide M_s; gcd(d_{s+1}, n-1) = 1; lambda_j < 0 and mu_j integral;
   integrality of the Def 5.1(1) root counts; s <= 5; the minor-disc
   clauses of Theorem p.200 (4)–(7). Not separating: u_s = 1, V_2 >= 2,
   A_1 > 1, delta_1 >= 1/2, e - d = 1, s = 3. The Prop 5.6 numerical
   shadow NOT-ALL-(11) cuts 1,189 -> 969 and empties nothing
   (OPEN[PROP-5.6-SHADOW], 220 groups). At (75,50) the missing elimination
   must cut M_2 in {5, 10, 40, 60} and keep the rows (55,73)/V_2 in {2,3}.
   Candidates named by the rebase lane: Prop 5.3's construction of p(pi)
   (pp.181–185) linking V_{r-1} to the MULTIPLICITY structure of the
   bottom polynomial; a semigroup condition on {M_i} ([A-M.1] p.68,
   [M.3]); Moh's minor-branch Props 6.1–6.4 enforced numerically; and
   Appendix II itself (Moh's own case-by-case endgame for the six rows).
   His extra eliminations are exactly the endgame the campaign needs in
   UNIFORM form.
6. THE INSTRUMENT (delta (f), reviewed): f is the Lagrange interpolant of
   the n values F_i = ±∫ dx / g_y(x, tau_i) at the n roots tau_i of
   g - c_2, and must be a POLYNOMIAL of y-degree m < n. The n - m
   degree-killing relations and the polynomiality of every coefficient
   mix ALL discs and all levels of the tree: the LOCAL version at one
   disc (LOCAL-KELLER) is only necessary, its resonance set was refuted
   (mu·{0,1,2,3}, not mu Z), and its order-2 recurrence was wrong. A Sol
   framework lane (global-interpolation, running) is writing the exact
   global conditions and an order-by-order algorithm with a counting
   function. First targets: the three D = 105 groups (all m = 70,
   K = 35, (d,e) = (2,3)): M = [28,103] V_s = 5 (q = 1/2, N in 6..12);
   M = [28,103] V_s = 6 (q = 9/13, N = 9); M = [40,103] V_s = 4
   (q = 9/17, N = 9). The two earlier D = 105 targets — the STAR row
   (105, 70, (-70,-63,103), V = (1,4,1), N = 6) and the mixed-branch packet
   (105, 42, (-14,103), 5, N = 10) — are DEAD under (8)–(13).
7. REDUCIBLE BRANCH (delta (g), review running): the exact machinery is
   H2-FREE; N_min = 6 on both branches; every datum distinguishing A_F
   reducible from irreducible lives in the NON-PROPER block, which
   contributes exactly zero to N; NONPROPER-COUNT = e(K - sum V_2);
   the census + pinned-N filter is ONE program for both branches.
8. AUXILIARY: box01 Keller-cluster census (legacy-inclusive, D <= 200,
   fail-closed merge, 425 cells missing at the 12 h cap): smallest D with
   a numerical cluster — N = 2, 3: none in [2,200]; N = 4: 8; N = 5: 10;
   N = 6: 8; N = 7: 10; N = 8: OPEN_INCOMPLETE. A numerical cluster is
   not a map.
9. INSTRUMENTS on disk: box/moh_skeleton_full.py (the (1)–(13) census,
   D <= 200 in seconds; survivors listed in full in
   box/censusrebase-drivers-20260902/survivors-D48-120.txt);
   box/d1sub-drivers-20260902/d1floor.py (pinned-N knapsack);
   box/tfe-drivers-20260902/bottomode.py and
   box/tfcal-drivers-20260902/bottom_star.py (BOTTOM-ODE / star
   Nullstellensatz); box/preflight.py (hard gate before any realisation
   job at N >= 6); ops/open_collision.py (OPEN contract).

## State deltas since round 20260902T1608Z (reviewed unless noted)

- (a) ORTHO-DEFECT / ORTHO-FLOOR / ORTHO-DIV / DESCENT-DEGREE promoted;
  NO-CEILING retyped [SINGLE-CLASS].
- (b) STAR-REALISABILITY closed, zero kills; Prop 4.6/A.5 source correction.
- (c) EXACT-N rigidity, Phi-lemma, floor L, NO-RESIDUE promoted; "max L =
  3.32" refuted (165/31 at D = 176; no kill either way).
- (d) [unreviewed as a whole; its (10)_1 and reconstructed (10) reviewed
  and confirmed in (h)] the census omission; TF-0, TF-DESSIN, TF-NOTAME,
  TF-EXH.
- (e) [unreviewed] DELTA-DENOM: the raw denominator test refuted; the
  signal is Moh's (10)–(13); (12)/(13) transcription agrees with (h).
- (f) BOTTOM-ODE, STAR-SIMPLE, STAR-RESIDUE (corrected), STAR-SUM,
  STAR-ABC promoted; the flagship's global framing, its resonance set,
  its order-2 recurrence and "D = 105 survives orders 1–2" REFUTED/GAP.
- (g) [review running] the reducible reprice, item 7 above.
- (h) the census truth and the decisive negative, items 4–5 above; p.202
  n = 75 bracket is an erratum (DELTA75 closed).
- Systems: the coordinator seat moved to a Linux cloud box; ops/lane.sh
  now sandboxes with bubblewrap on Linux (regression PASS);
  ops/lane_systemd.sh detaches lanes. The Moh 1983 PAGE IMAGES ARE NOT
  ON THIS MACHINE at freeze time (refs/ is not synced): use the verbatim
  transcription in census-rebase §1 and the OCR text
  box/depth-drivers-20260902/moh.txt (display formulas dropped). If
  refs/moh1983_jram340_configurations_of_roots.pdf (sha256 6c8847a8...)
  is present when you run, you may read it and must say so.

## THE QUESTIONS OF THIS ROUND (challenge them, reframe them, or answer them)

Q1 — MOH'S MISSING ELIMINATION, IN UNIFORM FORM. What restriction did
Moh's program apply beyond the printed (1)–(13)? Discriminator: it must
kill 652 of the 658 (1)–(13) rows at n <= 100 — in particular
M_2 in {5, 10, 40, 60} at (75,50) — and keep his six printed rows. Then:
what is its ALL-DEGREE form? Is it a theorem that empties every D (the
proof), an arithmetic sieve that leaves an infinite family (then the
family is the counterexample-side target list), or genuinely case-by-case
(then the campaign needs a different uniform mechanism)? Name the
mechanism, the cheapest test on the census, and what each outcome means.

Q2 — THE D = 105 TRIO: REALISE OR KILL. Using the global interpolation
conditions (item 6) and NO-RESIDUE, what is the cheapest EXACT
discriminator for each of the three groups? Give the order-by-order
unknown/condition count you expect and the first order at which a kill
by counting is possible; or, if you believe one is realisable, the
construction (which branch data, which dessin, which gluing). Say plainly
what a kill of the trio buys (D_min >= 108 only) versus what a uniform
theorem buys, and whether the trio is therefore worth a flagship seat.

Q3 — IS SKELETON REALISABILITY THE RIGHT ALL-DEGREE FRAME? Fresh eyes
wanted. The boundary computes N; nothing on the boundary bounds D. The
remaining program is arithmetic + realisability of an infinite census
(14,016 groups at D <= 200, growing with the divisor structure of D).
Candidate reframings the coordinator sees, none tried in exact form:
 (a) the interpolation identity as a statement about ONE differential
     operator: f = Lagrange-interpolant(∫ dx/g_y) is a D-module /
     differential-Galois / Picard–Fuchs statement on the pencil g = c_2;
     polynomiality of f is a monodromy/regularity condition at infinity
     — is there a cofinal invariant (rank, irregularity, exponents at the
     places at infinity) that grows with D and must be bounded by N?
 (b) the LATTICE identity 2 d e N = sum (e m_nu - d m'_nu)^2 together
     with the dessin structure at the bottom: the Belyi maps p_f^e / p_g^d
     at the k bottom discs are conjugate under the tower's Galois group;
     is there a rigidity theorem for a Galois-orbit of Davenport–Stothers
     pairs glued through a Puiseux tower (a "dessin tower") that forces
     k = 1 or bounds V_2?
 (c) characteristic p: reduce the interpolation identity mod p for p not
     dividing d e K; the Lagrange interpolant over F_p is a finite object
     and NO-RESIDUE becomes a Cartier-operator statement; does a
     p-curvature/Cartier argument bound the y-degree of the interpolant
     from below by data of the g-tree?
 (d) the semigroup at infinity: Moh's tower is the Abhyankar–Moh
     semigroup of the curve g = c_2 at its place(s) at infinity; is
     OPEN[MOH-PROGRAM]'s missing filter a semigroup/conductor condition
     (Bresinsky-type or the "approximate roots" structure) that is
     already a theorem in the AM literature and was silently used?
 (e) a counterexample-side construction: take a surviving group (a
     D = 105 or D = 108 row), fix its dessin at the bottom, and try to
     solve the interpolation system numerically to high order (Newton
     over Puiseux series / lifting mod p); a numerical solution to a
     large order at one skeleton would be the first positive signal the
     campaign has had above D = 100.
 (f) a theorem that the census never empties: if (1)–(13) + integrality +
     interpolation admit infinitely many skeletons, say so and what
     that implies for the proof side (a uniform theorem must use a
     datum not in the skeleton).

Q4 — SOFTWARE. The (1)–(13) census runs in seconds to D = 200. What
instrument turns "(1)–(13) + integral pinned N + interpolation to order
k" into an ALL-DEGREE filter run by machine — an order-by-order exact
linear-algebra engine over Puiseux data with a counting bound typed per
skeleton? Specify the smallest version worth building this week, its
gates, and the negative control that would catch a vacuous pass.

Also answer directly: which SINGLE lane would you launch first with a
frontier seat, and why.

## Current lanes (continue / redesign / stop wanted)

global-interpolation-sol56-20260902 (Sol; the exact global conditions +
algorithm, relaunched 10:02Z after the laptop copy died unsealed);
reducible-branch-review-grok46-20260903 (hostile review of delta (g));
websweep-20260903T1010Z-grok46 (external sweep). QUEUED on the Moh page
images: census-rebase second-reader review (OPEN[MOH-PROGRAM], pp.200–202
+ Appendix II) and branch-orbits v2 on the (1)–(13) space. QUEUED on the
Sol framework: DISC-COUPLING relaunch (GLOBAL-COUPLING) on a D = 105
survivor. Box01 idle after the cluster census; Box03 stopped.

## Submission contract (per COORDINATION.md, full-spectrum section)

Deliver ALL of: a disposition vector over the 46 APPROACHES.md rows
(changes only, with reasons) AND over Q3's candidates (a)–(f) and the
queued fronts (unchanged / raise / lower / reopen / retype, with reasons);
reranked proof and disproof bottlenecks; at least one genuinely NEW
avenue or mechanism; at least one new cross-connection; the strongest
proof attack; the strongest counterexample attack; one software
acceleration or decisive experiment; a campaign-systems check (UPGRADE
card with the smallest useful test, or NO_CHANGE with evidence); at most
three detailed idea cards (dependencies, cheapest discriminator,
interpretation of each outcome, stop condition, expected information
gain); continue / redesign / stop for each current and queued lane.
Blind: cite only this packet and the repository's banked reports
(xmodel/, AUDIT.md, APPROACHES.md, notes.md, PROGRESS.md); do NOT read
any ideation-20260903T1015Z-* submission, and do NOT read the in-progress
reports of the three running lanes (their .md files may be partial).
State the bounded quantity of every OPEN you raise (ops/open_collision.py
contract). Where you rely on a Moh page you cannot see, say so and type
the claim SOURCE-UNVERIFIED.
