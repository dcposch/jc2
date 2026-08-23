# SHEET6-REVIEW.md — Adversarial review of SHEET6-CAMPAIGN.md (commit 4835b13)

Reviewer: Claude (adversarial pass, 2026-08-07). Status: COMPLETE.
Verdicts: 1 CONFIRMED (E2+E3+E4), 2 CONFIRMED (G2), 3 CONFIRMED (G3),
4 CONFIRMED (14 rows), 5 CONFIRMED (spot-checked), 6 CONFIRMED (honest).
Overall: SHEET6-CAMPAIGN.md stands; one cosmetic count slip (r10/M4: 5 not
4 tails). Ground truth for thesis content: refs/sigray_full.pdf read
directly (pages cited per front).

## 1. Errata E2, E3, E4 (St 9.8 / 9.9 / 9.10 "no solution" claims)
Verdict: CONFIRMED (all three; printed claims located on-page, quoted, and
refuted by explicit families; NO excluding side condition found in §§3-8)

- Ground truth established first: Prop 8.1(v) (p. 41 end of proof) is verbatim
  "M_F = gcd(deg(p), deg(q))"; St 8.2 (p. 41) side condition deg(q)mult(p,c) >
  deg(p) holds for all three families (mu(nu+1) > mu*nu); St 8.4 (p. 42)
  mult(p,c) | M_G holds (2|4, 4|4, 3|3). Patterns match St 9.6's own usage.
- E2 (St 9.8, p. 55, mu=2 branch, verbatim): "In the case l = 0 from (v) of
  Proposition 8.1 we obtain M_F = 1" and "The above Diophantic equation has no
  solution with the conditions n = 5m+1 and l > 0". The l>0 half is TRUE
  (reviewer proof: RHS>1 needs n>=4, LHS<1 for l>=1; n=1 forces nu=1; plus
  brute sweep l<60, nu,n<3000: zero l>0 hits). The l=0 half is FALSE:
  15nu = 4n+1, n=5m+1 => 3nu=4m+1, family nu=4s+3, n=15s+11 (200 sweep hits,
  all in family), and M_F = gcd(2nu, nu+1) = 2 for odd nu — by the SAME
  gcd the thesis itself computes correctly in St 9.6's proof (p. 53: "M_F = 2
  if and only if l is even and nu is odd"). Missing possibility verified:
  Q(F) = ((12s+9)j,(16s+12)j,4s+3,2,3s+3) — thesis (iv)'s numbers with M=2.
- E3 (St 9.9, pp. 56-57, verbatim twice): mu=2 eq (4m+1)/(2m+2) and mu=4 eq
  (4m+1)/(m+1), each "The above Diophantic equation has no solution." BOTH
  FALSE: l=0, nu=4t+3, m=3t+2 solves both (checked t=0: 6/4=9/6 and 12/4=9/3;
  sweeps: 125 hits each, all in family). M_F = 2 (mu=2) resp. 4 (mu=4).
  Reviewer verified the mu=4 child shape is (3/4, 4t+3, 4, 3t+3) for EVERY
  parent s (exact Fractions) — a genuine lambda=0 self-loop as claimed.
- E4 (St 9.10, pp. 57-58, verbatim): mu=3 eq (3m+1)/(m+1) "has no solution" —
  FALSE: l=0, nu=3t+2, m=2t+1 (166 sweep hits, all in family; t=0: 6/3=4/2),
  M_F = gcd(3nu,nu+1) = 3, child shape (2/3, 3t+2, 3, 2t+2) = parent shape
  for every s (verified exactly): lambda=0 self-loop. Also confirmed: 9.10's
  printed possibility (iv) (the 9.8(iv) row) is derived NOWHERE in its proof
  body (proof yields only (i)-(iii) + the falsely-killed branch).
- Side-condition hunt (the likeliest refutation) came up EMPTY: nu>=2 ok,
  n>=1 ok, l=0 in N ok, regularity (other roots simple) consistent with the
  patterns, St 8.2/8.4 satisfied, and the campaign's reading of (b)/(d) of
  Prop 9.3 (p. 50) reproduces the thesis's own printed reduced forms
  ((4m+1)/(2m+2) etc.) exactly. Caveat retained: the errata live INSIDE the
  thesis's own case frame (H1/H4); they are errata of the thesis relative to
  its own machinery.
- Note: E2/E3/E4 change possibility LISTS (benign for td<=5 only because
  exits from the new loops/rows are covered elsewhere) — campaign's "benign
  for td<=5, lists incomplete as printed" framing is accurate.

## 2. G2 — St 9.12 kill set cannot kill its own case-IV terminals (H3 load-bearing)
Verdict: CONFIRMED (no alternative route exists in the printed thesis)

- St 9.12 proof (p. 60), quoted in full: "From Statements 9.6, 9.7, 9.8, 9.9,
  9.10 and 9.11 we obtain that either the characteristic sequence has an
  element F_j with M_{F_j} = 1, or (26) does not hold. The first case
  contradicts Proposition 8.4, the second contradicts Statement 9.4." That IS
  the entire kill set. Campaign's quote accurate.
- Reviewer re-derivation of the escaping chain (td=4, budget (26) = 2):
  row 4 = (2,3),(2,3),(4,6),nu=3 => Q(F0) = (2,4,3,2,5) = St 9.6's (j,2j,3,2,5)
  at j=2, M=2 (M=2 is the thesis's own hypothesis in 9.6, so no AF3 dependence).
  9.6(iii): Q(F1) = (7j,21j,7,3,5), lambda_F1 >= 2 — statement permits = 2.
  F1 matches St 9.7's hypothesis (j',3j',7,3,5) exactly (j' = 7j). 9.7(iii):
  F2 = (0,y), Q = (j',3j',1,M,1), "for some M in N" — M free, and Prop 8.4
  itself (if it applies to (0,y) at all) forces M != 1, i.e. AWAY from the
  M=1 kill. Sum lambda = 2 <= 2: (26) HOLDS. No element has M = 1 (2, 3,
  M>=2). Neither stated mechanism fires. Same escape via 9.6(iii)->9.7(iv)
  [no lambda stated]->9.10(iii). Checked: none of the four case-IV
  possibilities (9.7(iii), 9.8(iii), 9.9(iii), 9.10(iii)) carries any lambda
  or M annotation that could kill it.
- Hunt for the "other route": (a) the only root-vertex argument in the thesis
  is inside Prop 8.4's PROOF (pp. 44-45: reach (0,y), build (k,l), k=1,
  "Therefore l in N. This, however contradicts Theorem 6.1 [l_f < k_f]") —
  it is stated only under the all-M=1 hypothesis and St 9.12 cites only the
  STATEMENT of 8.4; (b) St 9.4's stronger form (25) with psi >= 2 would shrink
  the budget to 1 and kill the chain, but Thm 6.1 gives only psi = 1; (c) St
  9.2 gives (0,y) data (D=d, nu=1, kappa-bar=1) with no kill; (d) grep of the
  whole text for "cannot/impossible" finds no other terminal statement. So
  the printed proof is genuinely incomplete without an unstated root-kill;
  campaign's H3 framing (and its Thm-6.1/9.3(l) candidate: d_F < deg(p_G) vs
  l_f < k_f) is the right diagnosis and honestly hypothesis-flagged.
- Bonus check: Prop 9.3(k) reproduces the printed terminals 9.7(iii)
  (d_F = (j+(7-5)3j)/7 = j), 9.9(iii) ((4s+3)^2 j/(4s+3)), 9.10(iii)
  ((3s+2)^2 j/(3s+2)) — campaign's 0a claim verified. (Thesis's own proof
  line "d_F = D_F = 7j" on p. 54 contradicts its statement (iii)'s j —
  yet another slip, statement side is the consistent one.)

## 3. G3 — thesis §9 silence on rows 1,5,7,10 (td≥6 incompleteness as printed)
Verdict: CONFIRMED (maximal-skepticism sweep of §§5-9 found no hidden coverage)

- Structure verified on-page: Thm 9.1's proof (p. 60) is one line, "By
  Propositions 9.1 and by Statement 9.12 one has td(f,g) >= 6", and St 9.12
  kills exactly ONE table row ("type (3)", read as row 4 per G1: its proof
  says td=4 and St 9.6's Q-hypothesis matches row 4 and no other row — G1's
  label-slip reading independently confirmed; row 3 has Lambda=6).
- Under Prop 5.8 (p. 28, td = sum of Lambda over pole vertices) + Prop 5.7
  (Lambda >= beta >= 3, proof read on p. 27): td <= 5 forces a single pole
  vertex with Lambda = td, i.e. exactly rows {1,4,5,7,10} (Lambda 3,4,4,5,5).
  Two poles force td >= 6, so multi-pole silence is benign for td <= 5.
- Hidden-coverage hunt, all negative: (i) §9 is pp. 45-60 in full view —
  St 9.1-9.5, Props 9.2/9.3 are generic machinery, St 9.6-9.11 hypotheses
  are the five Q-shapes (j,2j,3,2,5)/(j,3j,7,3,5)/(j,4j,5,4,4)/9.9/9.10
  families — NONE matches the entry data of rows 1 ((1,1)-shape rho=1,nu=2,
  kap=5), 5 (nu=3,kap=7), 7 (nu=2,kap=7), 10 (nu=4,kap=9), so the printed
  lemma set cannot even START a characteristic-sequence bash for those rows;
  (ii) full-text grep "cannot|impossible|type (" — the only kill statement in
  the thesis is St 9.12; (iii) "FP_{kappa,a,pole}" in St 9.12 is garbled
  notation (only F_P^* := I_P(u) is defined, p. 24/1305) and encodes no extra
  hypothesis that could restrict to row 4 — and if it did, Thm 9.1 would be
  incomplete for the excluded configurations instead; (iv) §§7-8 (pp. 36-44
  read) contain budget/number-theory only, no type restrictions; (v) the
  intro (p. 45) cites [O 2],[D-O],[D] for td < 5 ONLY, and claims "a new
  proof for these known results" — so even on the most charitable
  known-results reading, rows 7,10 (td=5, beyond O-D's range) are required
  and absent; Zoladek is not invoked.
- Campaign's finer split verified by engine reproduction (bash5, this
  machine): rows 1,7 close mechanically (EXCLUDED, iv=0, open=0 — H3 not
  even needed); row 5 leaves 1 III-tail (2,3s+2,3,6s+6)@lam0, row 10 leaves
  III-tails + IV-terminals (M2: 1 tail + 4 IV; M4: see nick below). So
  "rows 5,10 need the same III-tail closure as td=6" is accurate, and the
  demotion of the thesis's td>=6 to incomplete-as-printed STANDS. The
  campaign's own qualification (td<=5 safe via Orevkov/Domrina/Zoladek
  independently) is correctly stated.
- NICK: campaign §5 table says r10/M=4 has "4 III-tails" — reviewer re-run
  dedups to 5 distinct shapes (bash5 prints only open[:4]; the 5th,
  (2,4s+3,4,8s+8)@lam0, was dropped in transcription). Cosmetic; §6.2's
  "~15 distinct shapes" estimate absorbs it.

## 4. Λ ≤ 7 leaf table = 14 rows
Verdict: CONFIRMED (independent hand recount agrees exactly; 20-30 estimate dead)

- Reviewer re-derived the Lambda=7 stratum from the stated constraints
  WITHOUT the engine: types (alpha,beta), 1<alpha<beta<=7, gcd=1; St 5.2(i)
  scaling (D,Dg)=a(alpha,beta), (P,Pg)=b(alpha,beta); St 5.2(ii) nu-rule
  [nu|alpha and nu|Pg-1] or [nu|beta and nu|P-1] (pilot verified this rule
  verbatim vs §5 and vs all 18 case-lines of Prop 9.1's proof; my read of
  pp. 46-48 concurs); Lambda = Dg*P/nu, with Prop 5.7 Lambda >= beta.
  (a) No old type (beta<=6) admits Lambda=7: alpha*beta*ab = 7nu has no
  solution with nu <= beta (7 coprime to alpha*beta, nu too small). (b) New
  types: Lambda=7 forces nu = alpha*ab; nu|alpha branch => ab=1, nu=alpha,
  needing alpha | 7*1-1 = 6: alpha=2 (2|6 yes), 3 (yes), 4 (4|6 NO), 5 (NO),
  6 (6|6 yes); nu|7 branch => alpha*ab = 7 or 1: impossible. Exactly three
  new rows (2,7)nu2, (3,7)nu3, (6,7)nu6; (4,7),(5,7) admit none. 11+3 = 14.
- Engine `table` phase run: prints exactly these 14 rows. Campaign's
  amendments to SHEET6.md (Lambda=6 count 6 not 7; 14 not 20-30; 6 single-
  pole entries + 1 double for td=6) all check: the Lambda column of table
  (23) as printed (p. 46) has six 6's, and Lambda>=beta>=3 kills all
  partitions of 6 except 6 and 3+3.

## 5. Engine fidelity vs Prop 9.3 (case split + s-free reduction PIT)
Verdict: CONFIRMED on the spot-checked surface (3+ branches, 1 PIT by hand);
lambda-rule remains reverse-engineered (AF2) as the campaign itself flags

- Prop 9.3 read on pp. 50-51. Branch checks against the engine:
  (I) thesis F in V_2a\V_1a, pattern (eta-c)^mu(eta-c_1)...(eta-c_k),
  q with l=0 by St 8.2 => degs (k+mu, k+1); engine 'I' identical, M_F =
  gcd(mu-1,k+1), mu=2 => 1 (thesis p. 52 gcd(k+2,k+1)=1). MATCH.
  (III) thesis p pattern eta^mu(eta^nu-c_1^nu)...(eta^nu-c_k^nu),
  q = eta(...) (p. 53/p. 60) => degs (mu+k nu, 1+k nu), M_F=1 at k=0; ratio
  from (f),(h): (h) forces nu_F | n (n = nu m), giving mu(rho+m)/(kap+m) —
  engine's RATIO_III derived correctly from the thesis's own (f)/(h). MATCH.
  (IIa/IIb) degree shapes ((k+mu)nu, (k+l+1)nu+1) and ((k+mu)nu+1,(k+1)nu+1)
  match 9.6/9.11's printed patterns and printed gcds; k>0 => l=0 via St 8.2
  as in thesis; IIb mu=2 M_F=1 matches 9.11's printed gcd((k+2)nu+1,
  (k+1)nu+1)=1. MATCH. (IV) engine gates ONLY on 9.3(j) kap<nu — a strict
  superset of the thesis's (i)-(m); conservative in the safe direction (can
  only over-report IV-terminals, which are all H3-conditional anyway), and it
  reproduces the thesis's IV-pattern exactly: no IV at 9.6/9.11, IV-all-s at
  9.7/9.8, IV-some-s (s>0) at 9.9/9.10 (engine is even finer than the
  thesis, whose 9.9(iii)/9.10(iii) omit the s>0 proviso).
- PIT certificate hand-check (St 9.9 node, mu=2, style II): lf_mod_reduce
  gives n0 = s (= thesis's n = s + m(4s+3)); the four linear forms
  A=(32,24), B=(8,6), C=(16,12), E=(16,12) share direction (4,3), quotients
  (8,2,4,4), content 2 => (4m+1)/(2m+2) — EXACTLY the thesis's printed
  reduced form on p. 56. Hand-verified the asserted identity at (s,m)=(1,1):
  2(3/4+8)*(2m+2) = 70 = (4m+1)*14. The 6x4-sample assert is far beyond the
  degree-1 forms involved. Sound.
- Validation run (this machine): `validate` reproduces 9.6 (iii),(iv),(v)
  with lambdas 2,2,0 and NO (75,51); 9.7(iv); the E2 M=2 family; both E3
  self-families; the E4 self-loop — i.e. the engine independently re-derives
  every corrected thesis lemma plus the errata content. Gate/bash5/report
  all reproduce the campaign's §0/§5 numbers (one nick: r10/M4, Front 3).
- Not certified here (open, as campaign states in §6): AF2 lambda-rule
  derivation from St 9.3, AF3 entry-M menu, III structural admissibility.

## 6. Gate honesty (does `gate` re-derive or string-compare?)
Verdict: CONFIRMED (genuine re-derivation, two independent code paths)

- Read sheet6_campaign.py gate() + sheet6_pilot.py. prop91() is a real
  bounded enumeration (beta<=60, a,b<=40 oversweep with the St 5.2 filters;
  Lambda-integrality and Lambda>=beta asserted, not assumed) compared against
  the stored THESIS_TABLE — stored values appear only as the comparison
  TARGET, which is what a gate is for. stmt96_knonzero() genuinely solves
  the ratio equation with an in-code completeness certificate ((k nu+2) |
  9(k+2) => nu<=25, k<=8) plus a 2000x2000 oversweep assert; gate applies
  the thesis's own n=3m+1 filter and asserts pairs == {(20,16),(21,15)} AND
  that the raw solution set contains (1,25,12) (the corrected row exposing
  erratum E1). Then, separately, gate runs the generic campaign engine
  (step() on Node(1/2,3,2,5)) — reduce_ratio/solve_pattern/child_from, a
  different algorithm — and asserts the three corrected 9.6 child shapes
  with lambdas (2,2,0). So the pilot result is re-derived twice.
- Caveats (minor): both paths share primitives (Fraction/gcd) and one file
  imports the other, so this is two algorithms, not two implementations;
  expected shapes are hardcoded strings, but they are compared against
  computed output, not against other strings. No dishonesty found.

## Overall verdict

SHEET6-CAMPAIGN.md SURVIVES adversarial review. All three headline errata
(E2, E3, E4) are REAL: the printed kill claims in St 9.8/9.9/9.10 are false
by the thesis's own equations (Prop 8.1(v) gcd + Prop 9.3(b)/(d), all read
on-page), the counterexample families satisfy every side condition I could
locate (St 8.2 inequality, St 8.4 divisibility, nu>=2, n>=1, regularity),
and the missing possibilities/self-loops are exactly as stated. G2 and G3
are both CONFIRMED against the PDF: St 9.12's printed dichotomy demonstrably
fails on its own case-IV terminals (explicit escaping chain re-derived), and
§9 kills only row 4 of the five Lambda<=5 rows — the thesis's td>=6 theorem
is incomplete as printed, exactly as the campaign claims, with the campaign's
own H3/known-results qualifications being accurate rather than overclaimed.
The 14-row table is independently re-proved by hand. Engine case split
matches Prop 9.3 on every branch checked; gate is honest.

Defects found (none load-bearing): (1) §5 table r10/M=4 lists 4 III-tails,
actual distinct count is 5 (transcription from a truncated open[:4] print);
(2) the campaign's "EXCLUDED" verdicts remain conditional on the flagged
hypothesis stack H1-H4 + AF2/AF3 — the doc says so, but any promotion of
"EXCLUDED mod H3" rows into prose should keep the full conditionality
visible; (3) cosmetic thesis-side finds worth adding to §7 errata if desired:
St 9.7-9.10 possibility (i) prints "M_G = 1" for what the proofs derive as
M_F = 1, and 9.8(iv)/9.10(iv) print "Q(G)" for Q(F).

WEAKEST LINK of the campaign (unchanged by this review, and correctly
self-reported): H3 — every td=6 "EXCLUDED mod H3" verdict and the G2 repair
hang on the unproven root-vertex kill, and AF2's lambda-rule is still
reverse-engineered. Those are the right next targets, not this document's
claims. Recommendation: PROMOTE the campaign's findings (errata E2-E4 and
gaps G2/G3 are publishable-grade observations about the thesis, pending the
§§2-4 foundations audit the campaign already lists); DEMOTE nothing.

Reviewer artifacts: brute-force sweeps + shape checks run in-session
(2026-08-07, exact integer/Fraction arithmetic; E2 sweep l<60, nu,n<3000;
E3/E4 sweeps 500^2 per mu); engine phases gate/table/validate/bash5/report
all re-run on this machine, outputs matched against the doc.
