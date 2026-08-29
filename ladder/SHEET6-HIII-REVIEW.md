# SHEET6-HIII-REVIEW.md — Adversarial review + composition of SHEET6-H3 (048f2d9) and SHEET6-III (e5d42e7)

## Controlling supersession (2026-08-28)

This review remains evidence for the local chart arithmetic, E5 discrepancy,
and gcd calculations, but it is **not** the current root-survivor census.
Three later corrections control:

1. The `H3-psi` arithmetic is sound, while its global inequality is now
   proved through actual cluster weights (`c253bd12...`, hostile gate
   `727f5850...`) and disjoint singleton first-separation exit sets.  It is
   not a consequence of the printed `(22)`/literal-`Y` ledger alone.
2. Corrected Proposition 8.4 is nonroot only.  At `(0,y)`, `M=1` is allowed
   and Statement 8.5 gives divisibility only.
3. The composed `td=6 residual = 0`, `13 ext`, and `SF1 -> 1` counts below
   came from capped pre-root-aware engines and are withdrawn as exhaustive
   claims.  The later case-I theorem excludes the enumerated all-`M=1`
   root layer analytically (so the old `l=98` case-IV diagnostic is not a
   legal root meet in that layer), while post-jump/off-axis root/SF1 sectors
   remain open.

The separate corrected Section 9 packet `2763d970...` / `0729a576...`
review-closes only `counterexample => td>=6`.  It does not exclude `td=6`.

Historical reviewer: Claude (adversarial pass, 2026-08-07). Status: COMPLETE.
Scope: two parallel unreviewed results on the sheet-6 campaign; neither saw
the other. Tasks: (A) refute each; (B) compose the kill sets and produce the
definitive residual table. Ground truth: refs/sigray_full.pdf read on-page
(pp. 8-12, 16-19, 27-32, 39-45, 48-60). Cross-check engine:
cases/hiii_compose.py (new, additive; both existing engines re-run).

Historical verdicts (subject to the controlling supersession above):
- Front 1 (psi-budget derivation, H3-psi): **CONFIRMED**
- Front 2 (§5b consistent exhibit / blanket-H3 FALSE): **CONFIRMED, with
  rider: witness dies under the other result's E5 bound (WEAKENED as a
  chain, intact as a printed-thesis claim)**
- Front 3 (E5 lambda-bound + H5b reading): **CONFIRMED (+ new p. 53
  corroborating slip found)**
- Front 4 (N1 gcd theorem, H5a): **CONFIRMED**
- Front 5 (COMPOSITION): **td=6 sanctioned residual = 0; total sanctioned
  residual = 2 (td=5 r10/M4); 13 AF3-superset classes; SF1 -> 1**
- Front 6 (SF1 case-I root-termination gap): **CONFIRMED real; 28 -> 2 by
  composition -> 1 by new psi-at-root lemma (ext-only)**

## 1. Front 1 — psi-budget derivation (Result 1's core kill)
Current verdict: **CONFIRMED AFTER GLOBAL-LEDGER REPAIR** (the chart/psi
transport is re-derived from printed statements; the budget inequality uses
the later actual-weight/first-separation repair, not printed `(22)`)

- All chart ingredients read on-page and verbatim: Thm 6.1's proof (p. 28)
  prints "k_f = d_{(0,x)} and l_f = deg(p_{(0,x)})"; Prop 6.5's proof (p. 32)
  prints "d_{(0,x)} = deg(p_{(0,y)}) and deg(p_{(0,x)}) = d_{(0,y)}" (cited to
  St 3.12, itself verified p. 16). So k_f = deg(p_{(0,y)}), l_f = d_{(0,y)}
  are printed EQUALITIES (H3-psi needs only >= on the k_f side). St 3.17
  (p. 18, no M=1 hypothesis) at the terminal step G = (0,y)+c gives
  deg(p_G) = mult(p_{(0,y)},c) <= deg(p_{(0,y)}) = k_f; 9.3(k)'s d_F is
  d_{(0,y)} = l_f. Hence k_f/l_f >= R := deg(p_G)/d_F > 1 by (l).
- psi := ceil(R)-1 satisfies psi >= 1 and psi < R, so psi*l_f < R*d_F =
  deg(p_G) <= k_f STRICTLY — exactly St 9.4's hypothesis "psi in N,
  psi l_f < k_f" (p. 49, verbatim, with proof; (25) is genuinely a
  one-parameter family, (26) = psi=1 specialization). Applying (25) to
  F_0..F_n: pairwise-different membership in V_a cap T_a^searrow is printed
  in Prop 8.4's proof (Props 6.7/6.8, p. 45); (0,y) in V_a (Def 3.4) and in
  T_a^searrow (Thm 6.1); St 9.5's printed proof applies 9.4 to the whole
  sequence. No gap was found in the arithmetic/sequence part.  The printed
  Section 7 derivation of the global budget was later found invalid and has
  been replaced by the reviewed actual-weight theorem.
- Suspected flaw #1 (chart orientation): checked — transported Thm 6.1 reads
  d_{(0,y)} < deg(p_{(0,y)}), SAME direction as (l); the repaired argument
  uses no sign clash, only the magnitude transport, which this review
  re-derived from p. 28 + p. 32 independently of the H3 doc's §2a chain.
  Suspected flaw #2 (budget family): kill tests use td-1-psi with the
  certified psi, not (26). Both suspicions negative.
- §5a kill instances re-verified by hand (exact): 9.7(iii) R = 21j'/7j' hm
  = deg p_G/d_F = 3j'/j' = 3, psi=2, printed lambda>=2 (9.6(iii), p. 51):
  2 > 4-1-2. 9.8(iii): R=4, psi=3, 2 > 0. E2-family M=2 copy: (m)-test
  M(rho+nu-kap)/nu = 2(s+3/4)/(4s+3) = 1/2 not in N — case IV impossible.
- Row-4/G2 closure re-checked against pp. 51-58: all four printed IV
  terminals (9.7(iii)/9.8(iii)/9.9(iii)/9.10(iii)) have R in {3,4}, psi in
  {2,3}; every route from row 4 to them passes a printed lambda>=2
  annotation (9.6(ii)-(iv) p. 51; 9.11(ii)-(iv) p. 58; E2-E4 additions are
  lambda=0 loops that only sit after those). G2 is closed in the corrected
  reconstruction using the actual-weight/first-exit budget (AF2 is not
  needed for row 4); the printed thesis alone does not prove that budget.
- Historical capped engine h3_check.py re-run (2026-08-07): reproduced §5 table
  (r4: 0 SURV; r10/M2: 0; r10/M4: 15 classes/134 pairs; r2,r3: 0; r8/M2,
  r9/M3: all-dead by (m); r6/M3: 6; r11/M5: 22; grand total 1477 (shape,s)
  pairs; SF1 = 28). These are no longer exhaustive counts. The psi-kill uses
  recorded exit-charge minima (a lower bound, terminal's
  lambda_{F_n} omitted) — a fortiori sound.
- Residual conditionality (correctly flagged in the doc): engine-lambda
  minima = AF2; possibility-completeness of the propagation surface = H1/H2/
  H4/AF3. The repaired singleton psi-budget theorem itself is unconditional
  on those campaign enumeration hypotheses.

## 2. Front 2 — the §5b consistent exhibit (blanket-H3-false witness)
Verdict: **CONFIRMED as stated** (every PRINTED constraint holds; blanket H3
is false relative to the printed thesis) — **but WEAKENED by composition**:
the witness chain dies under Result 2's E5 lambda-bound (see §5), so the
exhibit certifies H3-falsity only under the mixed (pre-E5) reading of Prop
9.3(III).

- Terminal data audit (exact, re-done): (j) 3<5; (k) d_F = 8j(1/2+5-3)/5 =
  4j in N; (l) 4j<8j; (m) 4j*2/8j = 1 in N*. Root: l_f = 4j, k_f = 8j
  (single root), Thm 6.1 4j<8j ok; (k_g,l_g) = (5/4)(8j,4j) = (10j,5j) in
  N^2, type (4,5): k_f/k_g = 4/5 (Lemma 2.1(ii)), k_g/k_f = 5/4 not in N*
  ((iv)), l_f <= k_f ((iii)); Prop 6.1 at (0,y): 4j != 8j; St 9.2 data
  consistent; root M free per printed terminals "for some M in N" (9.7(iii)
  p. 53, 9.8(iii) p. 55, 9.9(iii)/9.10(iii) pp. 56-57); corrected Prop 8.4
  is inapplicable at the root, and Statement 8.5 gives only divisibility.
  Thus psi_max = 1 (k_f/l_f = 2), and the repaired exit inequality allows
  Sum lambda = 2 <= 3. Chain
  arithmetic (F0->F1 III mu4: 36/33 = 12/11; F1->F2 IIa_0 s=1: kap=2,
  D/i=5, M=3, lam=0; F2->F3 III mu3: 8/6 = 4/3, lam=1) all re-verified.
  No printed constraint located that the exhibit violates — concurring
  sweep of Lemma 2.1, Prop 6.1, Thm 6.1, Prop 6.5, St 3.12/3.17, St 9.2,
  Prop 8.4 (M>=2 Bezout run lands exactly on (m), verified against the
  p. 44-45 proof structure).
- THE RIDER: both III steps of the exhibit are computed under the engine's
  mixed reading (printed (g)/(h) with nu_F free). Under E5/H5a/H5b the first
  step F0=(1,4,4,9) --III mu=4--> costs lambda >= ceil(mu(kap-rho)/nu_G) =
  ceil(4*8/4) = 8 > 3 = td-2 budget; the E5 child data also differ
  (kap_F = 88, not 11). So the specific witness is NOT consistent under
  Result 2's extraction; H3-falsity-by-witness is reading-dependent. What
  remains true unconditionally: the NEGATIVE half (no printed statement
  contradicts a case-IV terminal per se; the Bezout root argument with
  M >= 2 yields (m), not a contradiction) — so blanket H3 stays FALSE as a
  claim about the printed thesis, but the CONSISTENCY REGION shrinks
  drastically under H5 (composition, §5).

## 3. Front 3 — E5 lambda-bound + the nu_F = nu_G reading (H5b)
Verdict: **CONFIRMED** (discrepancy real; bound follows under either coherent
reading; NEW corroborating thesis slip found on p. 53) — with the AF2
conditionality correctly flagged by the doc.

- Printed (e)-(h) read on-page (pp. 50-51): "Let nu := nu_F", (e) u = v -
  n/(nu kappa_G), (g)/(h) denominators nu_F. The
  printed PROOF (p. 51) derives (c)/(d) via kappa_F = kappa_G/nu_G and says
  "The remaining Statements can be proved the same way as above." Reviewer
  re-derivation: with (e)'s step v-u = n/(nu_F kappa_G) and St 3.17(ii),
  printed (g)/(h) hold iff kappa_F = kappa_G. Under Not 3.4/3.5 the only
  values available at a case-III vertex are kappa_G/nu_G (P-value) and
  nu_F kappa_G/nu_G (jump/Q-value, = H5a); kappa_F = kappa_G forces
  nu_F = nu_G under the Q-value and is impossible under the P-value
  (nu_G >= 2 since v = alpha_j is a genuine Def-3.1 jump). E5 diagnosis
  CONFIRMED: printed (g)/(h) are coherent only with nu_F = nu_G.
- The "other coherent reading" (printed-literal + nu_F = nu_G forced) is NOT
  incoherent — but reviewer re-derivation confirms it yields gap =
  mu(kap_G-rho)/(k nu_F) = mu(kap_G-rho)/(k nu_G), i.e. the SAME bound
  Lambda = mu(kap_G-rho)/nu_G. E5-corrected reading: solved (f) exactly
  ((mu+k nu_F)(nu_F kap_G+n) = mu(1+k nu_F)(nu_F rho+n) => n k(mu-1) =
  mu(kap_G-rho) + k nu_F(kap_G-mu rho)), gap = D_F/i - kap_F =
  mu(kap_G-rho)/(k nu_G); closed forms rho_F = mu(kap_G-rho)/(k(mu-1)nu_G),
  kap_F = rho_F(1+k nu_F), D_F/i = rho_F(mu+k nu_F) re-derived and match
  SHEET6-III §3 (the doc states them for locked nodes; they hold generally).
  Only the MIXED reading (printed formulas, nu_F free) — the pre-extraction
  engine — escapes the bound, and it corresponds to no Not-3.5 value.
- NEW EVIDENCE (this review): St 9.6's proof, p. 53 top, prints the case-II
  update "kappa_F(1-pi(F)) = ((1-pi(G))kappa_G + n)/nu_F = 5" but the value
  plugged in is nu = 3 = nu_G of the parent (j,2j,3,2,5) (child nu_F = 7,
  which would give 15/7*3). The thesis demonstrably writes nu_F for nu_G in
  exactly this formula family — strong independent support for reading
  (g)/(h)'s denominators as the same subscript slip (E5).
- Thesis's own case-III uses checked (pp. 52-54, 57-58, 60): mu=2 M_F=1
  (patterns + Prop 8.1(v), no (e)-(h) arithmetic) and lambda >= 1 via
  "there exists c* in C*" (p. 54) — E5 changes neither; no printed
  computation discriminates the readings, as the doc says. The p. 54 c*-line
  also corroborates (S2) (thesis asserts the nonzero root exists).
- Conditionality audit: Lambda-bound needs AF2's lambda >= k*max(1,
  ceil(gap)) (flagged); k>=1/mu>=2 parts are thesis-solid ((S1)/(S2) from
  Def 3.1 + Not 3.8 + St 3.17/3.18 — derivations verified sound, including
  the common-grid identity and the exact-denominator-nu_F argument).
  tails3 re-run reproduces §4 verbatim (32 pairs: 23 KILLED, 9 SURVIVE;
  sanctioned 10/13; r5, r10/M2 closed).

## 4. Front 4 — N1 derivation (H5a dependence)
Verdict: **CONFIRMED as a theorem under H5a**; H5a itself is the only reading
that keeps the thesis's own data well-formed (so the dependence is mild and
honestly flagged).

- Derivation re-done from Def 3.1 + Not 3.4/3.5 (pp. 10-12, read verbatim):
  at G = I_Q(alpha_j) with nu_G = e_{j-1}/e_j >= 2, kappa_G = kappa/e_j
  (Not 3.5, index j at u = alpha_j), kap-bar_G = (kappa - beta_j)/e_j. Since
  e_j = gcd(e_{j-1}, beta_j) divides both, and e_{j-1} | kappa (divisor
  chain e_i | e_{i-1} | ... | e_0 = kappa): gcd(kappa - beta_j, e_{j-1}) =
  gcd(beta_j, e_{j-1}) = e_j, hence gcd(kap-bar_G, nu_G) =
  gcd(kappa-beta_j, e_{j-1})/e_j = 1. Exact; case-agnostic; nu=1 vertices
  trivial. SOUND.
- H5a dependence: the computation uses the jump-realizing (Q-)value of
  Not 3.5 at doubly-realized vertices. Reviewer checks: (a) the P-value
  gives kap-bar with exact denominator nu_F >= 2, contradicting the
  integrality the thesis itself uses (St 9.4's proof line
  "kappa_G(pi(G)-1) in N", p. 49; every printed Q-datum in 9.6-9.11 has
  integer kap-bar); (b) Not 3.8's F*c and the next step's Prop 9.3
  hypotheses need the jump root. So H5a is forced by coherence, though
  Not 3.5 as printed is genuinely P-ambiguous ("for some P") — correctly
  logged as an interpretation, not a theorem. (Same ambiguity family
  infects Not 3.4's nu at multiply-jump-realized vertices — worth one
  sentence in SHEET6-III §5 but changes nothing here.)
- Sanity vs the thesis's own possibility lists (all pass, N1 only REFINES):
  9.6(iii) gcd(5,7)=1; 9.6(iv) gcd(4,5)=1; 9.6(v) gcd(3s+3,2s+1)=3 iff
  s == 1 mod 3 (kills that residue); 9.7(iv)/9.10 node gcd(2s+2,3s+2) = 2
  iff s even (odd s only); 9.9 node gcd(3s+3,4s+3) = 3 iff s == 0 mod 3.
  Row-3 td=6 entry (nu=2, kap-bar = D+D_g = 10): killed outright —
  consistent with (and now redundant to) r3's psi-budget exclusion.
- The tails3 N1 kills ((4/3,6s+2,3,8s+4) all s; four odd-s restrictions)
  re-run and reproduced.

## 5. Front 5 — HISTORICAL COMPOSITION (not a definitive current residual table)
Verdict: **COMPUTED FOR THE CAPPED 2026-08-07 ENGINE, WITHDRAWN AS
EXHAUSTIVE** (new engine cases/hiii_compose.py, additive; internal
gate reproduces tails3's cong_survivors witnesses from the E5 closed forms;
campaign gate untouched and PASS; frontier=0 at depth cap everywhere, so the
exclusions are cap-clean). Composed semantics: BFS with (i) case-III steps
replaced by E5 arithmetic (rho_F = mu(kap_G-rho_G)/(k(mu-1)nu_G), kap_F =
rho_F(1+k nu_F), lambda >= k*max(1,ceil(mu(kap_G-rho_G)/(k nu_G))), nu_F
enumerated as complete residue families, n>=1 window certified), (ii) N1
filter on entries and children (dropped only when gcd>1 identically), (iii)
case I/II branches inherited unchanged, (iv) IV terminals classified by
(j)/(k)/(l)/(m) + psi-budget (h3_check.iv_dispositions).

HISTORICAL RESULT (exact for that 2026-08-07 run, not for the root-aware
unbounded state space):
- td=3: 0. td=4: 0 — G2 stays closed under composition; row 5 fully closed.
- td=5: r10/M2 fully closed. **r10/M4 (SANCTIONED): 2 residual classes**
  (down from Result 1's 15): both reached by a single IIb mu=4 k=1 step
  (engine lambda=1, the thesis-printed lambda>=1 floor):
  R1. (1/3,7,3,5)@lam=1 — St 9.7's own hypothesis shape; IV = 9.7(iii);
      R=3, psi=2, (m)=1. psi-kill needs Sum lambda >= 3, has 1.
  R2. (2/3,3s+2,3,2s+2)@lam=1, odd s only (N1) — 9.10's shape; R=3, psi=2.
- **td=6 SANCTIONED: 0 residual classes — the sanctioned td=6 book is
  EMPTY.** r2: psi-killed. r3: entry killed by N1. r6/M3, r9/M3, r11/M5,
  r8/M2: zero IV survivors, zero opens, zero frontier. In particular
  Result 1's 6+22 sanctioned IV-survivors all die (their routes ride
  E5-priced III steps: e.g. r10/r11-entry III costs ceil(mu*kap-ish) = 2mu
  .. 10 > budget) and Result 2's sanctioned residual classes all resolve
  (r8/M2's child (1/3,nu_F,2,(nu_F+1)/3) is (m)-impossible at IV and
  budget-stuck; r11's (1/2,4s+3,4,2s+2)-child (2/3,nu_F,3,...) is
  psi-killed at Sum lambda=4 > 3; r11's (1/3,3s+2,3,s+1) tail is no longer
  reachable once its mixed-III route is E5-priced).
- td=6 AF3-superset (ext entries r8/M6, r9/M2, r9/M6 — vanish if AF3's
  sanction is proved): **13 classes**:
  (1/2,2s+3,2,s+2)@lam2,3 R2; (1/2,4s+3,4,2s+2)@2 R2; (1/2,4s+5,2,2s+3)@2
  R2; (1/3,7,3,5)@2[r9/M2],3[r8/M6] R3; (1/4,5,4,4)@2 R4 (boundary: 2 =
  td-1-psi); (1/5,2,5,1)@3 R5/3; (1/5,7,5,3)@1 R5/3; (2/3,3s+2,3,2s+2)@2,3
  R3; (2/5,5s+4,5,2s+2)@1 R5/3; (3/4,4s+3,4,3s+3)@2 R4 (boundary).
- SF1 composed: 28 -> 2, both on r8/M6 ext ((1/2,1,2,1)@3, (1/3,1,3,1)@4);
  see §6 — one of them dies by this review's psi-at-root extension.

WHAT WOULD CLOSE THE 2 SANCTIONED RESIDUALS (both td5 r10/M4): any one of
(a) AF2-audit outcome pricing IIb's k extra orbits like I/IIa_k/III (the
same St 9.3/6.2 mechanism prices the k=1 orbit at max(1,ceil(gap)) = 7 > 3:
both die; even the mult-count floor k+1 = 2 leaves them at the boundary
2 <= 2); (b) lambda_{(0,y)} >= 1 at the terminal (kills R1/R2 at psi=2);
(c) a printed-statement exclusion of IIb k>=1 at pole entries. NOTE both
shapes are the thesis's OWN St 9.7/9.10 hypothesis shapes at td=5 — row 10
remains externally covered (Orevkov/Domrina/Zoladek, RECON), so this is an
independent-reproof residue, not a JC-risk.

## 6. Front 6 — SF1 (case-I root-termination) reality + historical composed coverage
Verdict: **CONFIRMED REAL** (the gap exists in the printed thesis and in both
legacy engines' modeling).  The old claim that composition plus a
psi-at-root lemma reduced `28 -> 2 -> 1` is a capped historical count, not
an exhaustive present census.

- Reality: (0,y) in V_{2,a} is possible — St 3.1's forms (3)/(4) include the
  j=0 coefficient, so two roots with c_0 != c_0* have O(P,P*) = 0 and
  I_P(0) = (0,y) in V_{2,a} (Defs 3.2/3.4, pp. 10-11). Then Prop 9.3 puts
  the terminal step in case (I) (its (IV) hypothesis "F not in V_{1,a} cup
  V_{2,a}" fails), where the thesis's proofs treat F as a continuing vertex
  (lambda >= 1) and print no root-data possibility. (0,y) in V_{1,a} is
  impossible (alpha_j = beta_j/kappa > 0), so root-termination is exactly
  {case IV (modeled), case I (SF1)}. Result 1's framing and its 28-hit scan
  are accurate; row 4/td<=5 unaffected (no (nu,kap)=(1,1) shape in the
  printed row-4 lists — re-checked pp. 51-60).
- Composed coverage: the 28 mixed-engine hits shrink to 2 (both r8/M6 ext):
  (1/2,1,2,1)@lam=3 and (1/3,1,3,1)@lam=4. All sanctioned SF1 candidates
  (r10/M4 td5, r9/M6, r11/M5 routes) die because their routes rode
  E5-priced III steps.
- NEW (this review, closes half the residue): the psi-budget transports to
  root-terminations of ANY case. At F_n = (0,y): D = d (St 9.2(i)), and the
  printed equalities k_f = deg(p_{(0,y)}), l_f = d_{(0,y)} (pp. 28/32) give
  rho_root = D/deg p = l_f/k_f EXACTLY, so psi := ceil(1/rho_root) - 1 >= 1
  is certified (Thm 6.1) and St 9.4 (25) forces Sum lambda <= td - 1 - psi
  — no case-IV condition needed. Applied: (1/3,1,3,1)@4: psi = 2, 4 > 3
  KILLED. (1/2,1,2,1)@3: psi = 1, 3 <= 4 survives. SF1 residual after
  composition + psi-at-root: **1 class, ext-only; sanctioned SF1 = 0.**
- Remaining SF1 modeling debt (unchanged): a case-I (0,y)-terminal at
  psi-consistent budget is killed by NO located statement (same §4b logic
  as IV survivors); and the engines still model such nodes as CONT — the
  count above reads (nu,kap)=(1,1) children as terminal candidates.

## 7. Hypothesis-set interactions (H1-H4 vs H5a/H5b)

- No circularity found. Result 1's psi-budget theorem uses printed
  statements only (+AF2 for engine-lambda minima); it nowhere assumes
  H5a/H5b. Result 2's N1/E5 use Def 3.1/Not 3.4/3.5/3.8 + H5a/H5b (+AF2 for
  the lambda bound); they nowhere assume H3 — H3 appears only in Result 2's
  ENTRY-level verdict labels ("EXCLUDED mod H3+H5"), and composition
  replaces it by Result 1's proved H3q, so those labels upgrade cleanly.
- One-way contamination DOES exist and matters: Result 1's survivor book
  (the 43 classes) and its §5b witness are computed on the MIXED-reading
  chain graph that Result 2 proves is not a theorem of the thesis's
  definitions (the printed-(g)/(h)-with-nu_F-free reading). Result 1's
  TESTS ((l)/(m)/psi) are pointwise and reading-independent; only its
  reachable set was too big. Symmetrically, Result 2's tails3 budgets
  (B = 4 - lambda_spent) were computed along mixed routes; E5-lambda >=
  mixed-lambda at every III step exactly when nu_F >= nu_G (true in all
  solved instances), and the composed BFS recomputes routes from scratch,
  superseding both books.
- Engine asymmetry surfaced by the composition (pre-existing, inherited by
  BOTH results): sheet6_campaign prices IIb's k extra orbits at flat
  lambda=1 (the thesis's printed lambda>=1 practice) while I/IIa_k/III get
  k*max(1,ceil(gap)) [AF2]. Both sanctioned td5 residuals and several
  td6-ext ones ride exactly such IIb k=1 steps. The AF2 audit (campaign §6
  item 5) should now explicitly decide IIb pricing; it is the single
  highest-leverage open item left on the sanctioned board.
- Historical stack for the composed verdicts: H1, H2, H4, AF2,
  AF3(sanction), H5a, H5b, + Result 1's H3q (now justified globally by the
  actual-weight/first-exit repair), + engine
  fidelity of hiii_compose.py (gated against tails3's witnesses; frontier
  0; PIT asserts on every emitted E5 family).

## 8. Overall verdict

The local results survived the 2026-08-07 adversarial review.  Their numeric
residual composition is historical and not a current exhaustive book.

- SHEET6-H3 (048f2d9): Fronts 1-2 CONFIRMED. The psi-budget theorem is
  correct after the actual-weight/first-exit global repair; G2 closure
  stands in the corrected reconstruction; blanket-H3-FALSE
  stands relative to the printed thesis. WEAKENED item: the §5b witness and
  the 43-class survivor book are mixed-reading artifacts — under H5a/H5b
  the witness chain is inconsistent (its first III step costs lambda >= 8)
  and the book shrinks to 2 sanctioned classes. Recommend PROMOTE with the
  survivor book re-labeled "superseded by composition".
- SHEET6-III (e5d42e7): Fronts 3-4 CONFIRMED (E5 discrepancy real, with new
  corroborating evidence: p. 53 prints /nu_F but computes with nu_G = 3;
  N1 a clean theorem under H5a, which is coherence-forced). Its 9-class
  residual book is also superseded: under composition every sanctioned
  tail-child dies ((m)-impossible IV, psi-kill, or route removed).
  "EXCLUDED mod H3+H5" labels upgrade to "mod H3q+H5" (H3 discharged).
  Recommend PROMOTE.
- HISTORICAL COMPOSED HEADLINE — **WITHDRAWN AS AN EXHAUSTIVE CURRENT
  CLAIM**: the capped engine reported `td=6` single-pole sanctioned entries
  fully excluded conditional on {H1, H2, H4, AF2, AF3-sanction, H5a, H5b} +
  the proved H3q — no case survives at td=6 on the thesis's own M-menu.
  THE residual after composition: **2 sanctioned classes, both td=5
  r10/M4** ((1/3,7,3,5)@lam1 and (2/3,3s+2,3,2s+2)@lam1 odd-s, both R=3,
  psi=2, both riding a thesis-priced IIb lambda>=1 step), **13 AF3-superset
  td=6 classes** (r8/M6, r9/M2, r9/M6), and **1 SF1 class** ((1/2,1,2,1)@3,
  r8/M6 ext; the other SF1 hit dies by the new psi-at-root lemma, §6).
  Out of scope and still open: the two-pole (3,3) configuration (campaign
  §6 item 4).
- Historical next actions (superseded by root-aware exact recensus): (1) AF2 audit deciding IIb extra-orbit
  pricing (kills both sanctioned residuals if it extends the per-root
  rule); (2) AF3 sanction proof (kills the 13 ext classes + last SF1);
  (3) lambda_{(0,y)} >= 1 lemma (independent kill of both residuals);
  (4) two-pole analogue.

Artifacts: cases/hiii_compose.py (additive; gate PASS + internal
witness-gate PASS; frontier 0; exact arithmetic; ~40s). Engines re-run:
h3_check.py and sheet6_campaign.py gate/tails3 all reproduce their docs.
