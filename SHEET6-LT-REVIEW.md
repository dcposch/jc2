# SHEET6-LT-REVIEW.md — Adversarial review of SHEET6-LROOT (c8f8bc8) and SHEET6-TEMPLATE (3f06c21), plus R1 gate

Reviewer: Claude (adversarial pass, 2026-08-07). Status: COMPLETE.
Scope: the two unreviewed endgame results (λ_root refutation + template
lift) and the GO/NO-GO gate on the proposed decisive experiment R1.
Ground truth: papers/sigray_full.pdf re-read on-page this review
(pp. 10-18, 19-20, 23-28, 35-39, 42-43, 48-52). Engines re-run:
lroot_ledger.py (asserts pass), template_lift.py (46 checks, 0 FAIL),
sheet6_campaign.py gate (PASS). Independent sympy/Fraction verifiers
written for this review (disposable, /tmp).

Verdicts:
- Front 1 (λ_root = 0 forced; ledger itemization): **CONFIRMED** (LR1
  reading-robust; itemization complete; pole purity is d-level, E10-free)
- Front 2 (δ-strictness = last kill surface): **CONFIRMED** (no printed
  statement forces δ > 0 anywhere; Prop 7.3 equality clause is mult=1 only)
- Front 3 (16 ≤ 7 kill + tower uniqueness): **CONFIRMED — STRENGTHENED**
  (option A dies three independent ways; (3,4) forced in ONE line from
  Prop 4.2(iii); side theorem printed-tier sound via Cor 6.1)
- Front 4 (W-collapse; L1c match): **CONFIRMED** (forcing re-derived by
  hand, unique; same normalization as L1c — no gauge mismatch)
- Front 5 (pole-lead identities; ladder): **CONFIRMED**, with an emphasis
  correction: kill-chances (i)/(iv) are exponent-trivial, only (ii)/(iii)/
  (v) were genuine
- Front 6 (E10, E11): **E10 CONFIRMED** (core; two filing errors fixed
  here). **E11 REFUTED as erratum** — the St 9.6 step IS derivable from
  print; demote to reading note (and the derivation independently forces
  m_{F_s} = 2)
- Front 7 (R1 GATE): **REDESIGN** — four spec amendments required (f vs
  f−a tower normalization / gauge; UNSOLVABLE-scope caveat vs R6; x-side +
  g co-staging; SOLVABLE endpoint). Sizing 10²-10³ CONFIRMED credible.
  After amendments: GO.

## 1. Front 1 — λ_root refutation (LR1) and the (22) itemization

Verdict: **CONFIRMED**. LR1 re-derived from the page; the itemization of
(22) re-derived from Prop 7.5's proof; both alternate readings probed —
neither resurrects λ_root.

- LR1 re-derivation (Def 3.4/3.2, p. 10-11, re-read): (0,y) ∈ V_{2,a}
  iff some pair P,P* has O(P,P*) = 0. y-side pairs both in form (3) have
  O ≥ 0; conjugation fixes the j = 0 coefficient, so O(P,P*) > 0 for all
  pairs ⟺ all y-side series share c_0 ⟹ p_{(0,y)} = ⊖(η−c_0)^{k_f}
  (Prop 3.1(∗∗) at level 0) ⟹ all rays pass one first vertex, no
  separation AT the root, branch-at-F Y((0,y)) = ∅. Case IV verbatim on
  p. 50: "F = (0,y) and F ∉ V_{1,a} ∪ V_{2,a}". Correctly does NOT use
  St 3.16 (whose root-count iff excludes (0,y) — p. 17 re-read). Two
  reading dependences, both safe: (a) V_{1,a} needs the j ≥ 1 reading of
  Def 3.4 (else α_0 = 0 puts (0,y) ∈ V_{1,a} always and case IV is
  empty) — this is H1-tier, case IV's own existence needs it; (b) E9/H2
  branch-at-F is standing (A3L1 front 8); under the LITERAL Y-reading
  Y((0,y)) = all y-side cv mass — already counted, and (22) charges each
  vertex once (χ(C) Euler count, Prop 7.5 proof p. 38), so no NEW unit
  in either reading. E10-swap independence: LR1 never touches St 3.15.
- Itemization completeness (Prop 7.5/Not 7.3/Cor 7.1 re-read pp. 35-39):
  (22) = one charge κ_F(π(F)−1) per cv vertex of the chosen fiber's tree
  + Σ_a δ_a, δ_a the per-puncture Λ-excess. Partition audited: chain ⊂
  T^+ vs T_a,cv ⊂ T^0 disjoint ✓; pole clusters: Prop 5.3's proof
  (p. 25) shows deg(p_{g,G}) = 0 and d_{g,G} = d_{g,F} > 0 for every G
  above a pole vertex, PLUS 5.3(ix) I_P((u,∞]) ∩ V_a = ∅ — no cv vertex
  (Not 7.1 needs d_g = 0), a d-LEVEL fact, valid under either 3.15
  labeling ✓; x-component pole-free (Prop 5.8 (20) + searrow descent,
  Prop 8.4's proof p. 44) ✓; y-branches at F_i priced by (24); root slot
  empty (LR1). Complete: two components (St 3.3) + vertex separation
  (Def 3.3/Not 3.3) leave nothing else.
- LR2 re-derived: slope law from d_{(0,x)} = k_f, deg p_{(0,x)} = l_f
  gives π ≥ k_f/l_f = R for every x-side cv vertex; κ(π−1) ∈ N printed
  in St 9.4's proof (p. 49); k_f/l_f = k_g/l_g is Lemma 2.1(ii) (p. 8
  re-read) so d and d_g exhaust together; 2ψ > ψ + slack and
  2(R−1) > ψ + slack kill second vertex / κ_G ≥ 2. Ledger rows recomputed
  independently (/tmp/lt_review_check.py): R = 3,4,3,4 exact via Prop
  9.3(k), slacks 1,0,1,0; SP-2 series audit 60 = 30+30, prices 15/3−4 = 1
  (×2), SP-1: 63 = 42+21, price 21/3−5 = 2 — all match.
- Nitpicks (no verdict weight): (i) §2's parenthetical "x-side pairs give
  O = −1" is garbled — x-side pairs give O ≥ 0 but create (0,x) ∈ V_{2,a},
  a different tree point (Def 3.3: cross-component pairs are the O = −1
  case); conclusion unchanged. (ii) The (24)-price D/mult − κ̄ used by the
  ledger is the PROOF's version of St 9.3; the printed (24) has a sign
  slip (−κ_F(π(F)−1) should be −κ_F(1−π(F))) — already standing campaign
  usage ("corrected (24)", A3L1 front 3), fine. (iii) lroot_ledger.py
  line 81: `assert ... == 4 or True` is a vacuous assert (the R = 4 value
  is nonetheless correct: ν/(ρ+ν−κ̄) = 5/(5/4) = 4, re-checked).

## 2. Front 2 — is δ-strictness really the last kill surface?

Verdict: **CONFIRMED** after a genuine hunt. No printed statement forces
δ_a > 0 at any survivor; Prop 7.3's mult ≥ 2 case is exactly where the
printed control stops.

- Prop 7.3 (pp. 36-38) re-read: the inequality Σ_{P∈R*_a} Λ(P) ≥
  κ_F π(F) − κ_F is stated for all c; the equality clause is stated ONLY
  in the special case mult(p_F − a, c) = 1 (then R*_a = {P} and Λ(P) =
  κπ−κ). At mult ≥ 2 nothing sharper than ≥ is printed — its geometric
  proof (preimage count in a small bidisk, p. 37-38) loses nothing but
  proves nothing extra. Prop 7.4: δ_a ≥ 0, = 0 generic. That is the
  complete printed δ-control: δ appears ONLY in Not 7.3 / Prop 7.4 /
  Prop 7.5 / Cor 7.1; §§5, 6, 8, 9 (all statements pp. 23-52 re-read
  this review) contain no Λ-excess or strictness statement — St 9.3/9.4/
  9.5 are budget consumers of Cor 7.1, and 9.6-9.11 are Q-data reach
  chains. Riemann-Hurwitz-type global excess for g is not in the frame
  (Prop 5.5-5.8 count poles only).
- The collision fibers EXIST for every survivor: at the LR2 x-vertex G,
  deg p_G = l_f ∈ {15, 21, 42, ...} ≥ 2, so p_G − a* has a multiple root
  at every critical value a* of p_G; the vertex persists into T_{a*} via
  St 3.14 (patterns preserved — exactly the mechanism Prop 7.3's own
  proof uses). So the kill surface is nonvacuous and correctly located:
  ONE unit of forced Λ-excess at ONE collision fiber kills all four
  slack-0 classes via (22) with a_0 = the carrier fiber (Σδ_a = 0 forced
  there — itemization complete per front 1, so the balance argument is
  valid). Nothing printed decides it; a local excess formula for δ at a
  mult ≥ 2 collision is genuinely new mathematics, as filed.
- Also re-checked that no OTHER printed kill was missed at slack 0: the
  ψ-side cannot be upgraded (St 9.4's proof charges exactly one x-vertex
  with κ(π−1) ≥ ψ, and ψl_f < k_f strict caps ψ at R−1 — sharp by LR1's
  single-root equality); λ-side minima are AF2-standing; St 8.5 at the
  terminal gives divisibility only (A3L1 front 3, unchanged); the
  h₁-branch budget remains outside every printed budget (confirmed: (22)
  charges g-critical-value vertices only).

## 3. Front 3 — template step (a): branch counts and tower uniqueness

Verdict: **CONFIRMED — and STRENGTHENED**: option A dies three
independent ways, and (k1,l1) = (3,4) is forced by a one-line printed
argument that closes the only soft joint I found in E3's scan.

- 16 ≤ 7 recomputed from scratch: option A (m_{F_s} = 1) has M*_{F_s} =
  gcd(126,189) = 63, i = 2, p_red = φ⁶ψ³ (deg 63, mult 6 at c_m), dead
  member h1 with d_{h1} = (μ−1)d + 1 − u = 26/7, deg p_{h1} = 126·(26/7)/6
  = 78 = 63 + 15, so q15 with mult(q,c_m) = 1 (Prop 8.1's root law):
  mult(p_{h1,F_s}, c_m) = 7. deg p_{h1,G_m} = 6 + 10 = 16 (deg q = 10
  from 9.3(b) with i_{G_m} = 2, needing only m_{G_m} ≥ 1 — forced, δ_0 =
  10 > 0). St 3.11(i) composed: 16 ≤ 7 FALSE. KILL VALID (composition
  along the dead stretch is sound: counts nonincreasing per elementary
  step regardless of intermediate coefficients).
- NEW second kill (printed-tier, missed by the doc): St 8.4 (p. 42)
  gives mult(p_red, c_m) | M_{G_m} = 2; option A needs mult = deg
  p_{G_m}/i = 12/2 = 6, and 6 ∤ 2. Immediate contradiction.
- Third route (the doc's corroboration) VERIFIED ON-PAGE: Not 4.1
  (p. 21) defines F ≺ G as F ≼ G and m_F < m_G; Cor 6.1 (p. 32) states
  "F ≺ F′ for any suitable κ" at every F ∈ T^searrow ∩ V_a \ {(0,y)} —
  strict m-jump crossing each searrow V_a vertex — and Prop 6.3's
  searrow clause (G ≼ F) gives m nondecreasing along dead stretches
  (searrow-ness is preserved exactly there: d and (1−π)deg p drop at the
  same rate). Hence m_{G_m} = 1 ⟹ m_{F_s} ≥ 2, printed-tier. The SIDE
  THEOREM (first-step merge in the minimal branch) is the same mechanism
  below G_m — with Prop 5.1(ii) (m ≠ 0 strictly below the pole vertex) —
  and is SOUND.
- (3,4) uniqueness, one line: h1 alive at F_s ⟹ Prop 4.2(iii)
  (h1^+)^{k1} = s1(f^+)^{l1} forces the level match k1·d_{h1,F_s} =
  l1·d_{F_s}, and d_{h1,F_s} = 8 is (k1,l1)-INDEPENDENT (8/21 at G_m
  from the dead-member formula + St 8.3(ii) count exactness at j = 1 ≤
  m_{G_m}, both printed): k1·8 = l1·6, coprime ⟹ (3,4). This closes the
  scan's soft joint: I checked that for l1/k1 > 4/3 the dead-member mult
  formula 2k+1 used by E3 would be wrong (δ_2(F_s) = 42l1/k1 − 26 > 0,
  h2 alive, mult = 12l1, no count contradiction) — but those cells never
  exist because they violate the level match above. E3's conclusion is
  right; its no-cancellation case analysis is superfluous rather than
  load-bearing. Independent wider scan (k1 ≤ 12, l1 ≤ 79, own code):
  unique (3,4) ✓. R6 (m_{G_m} = 2 variants) honestly quarantined; window
  reproduced: (2,3),(2,5),(3,5),(3,7),(3,8),(6,11),(6,13),(6,17).
- St 9.6(iii)(A) cross-check: k=1, n=10, ν=7, deg(p) = 21, deg(q) = 15
  printed on p. 52 — matches the suffix vertex exactly.

## 4. Front 4 — template step (b): the W(t) degree-drop, by hand

Verdict: **CONFIRMED**; forced (not merely sufficient), and the L1c match
is in the SAME normalization — no gauge artifact.

- Hand expansion: W = t(t−b)³ − (t²−σt+π)² has coefficients t⁴: 0
  (identical), t³: 2σ−3b, t²: 3b²−σ²−2π, t¹: 2σπ−b³, t⁰: −π². Degree ≤ 1
  ⟺ the t³ and t² coefficients vanish; the system is TRIANGULAR-LINEAR
  (t³ linear in b, then t² linear in π): b = 2σ/3, π = σ²/6 is the UNIQUE
  solution — forced. Residual W = (σ³/27)t − σ⁴/36 = (σ³/27)(t − 3σ/4):
  automatically degree EXACTLY 1 for σ ≠ 0 (and σ = 0 forces b = π = 0,
  dead upstream), so 39 = 39 leak-free and b2 = 3σ/4 pinned. Coefficient
  formulas verified on a 27-sample exact grid (degrees ≤ 3: pinned).
- The forcing inequality deg p_{h2,G_m} = 36 + 3·deg_t W ≤ 39 =
  mult(p_{h2,F_s}, c_m) is St 3.11(i) (any polynomial h — h2 need not be
  a tower member at G_m); 39 = 2·19+1 with k = 6(25/6 − 1) = 19 checked;
  the bracket factorization P⁶[H_M³η³(η³−b)³ − s1S_M⁴P²] = s1S_M⁴P⁶W(η³)
  re-derived (uses H_M³ = s1S_M⁴, which is 8.3(i)-transport, front 5).
- L1c match: A3L1 front 6's closed forms at ν = 3 are b = σ(ν+1)/(2ν) =
  2σ/3 and π = σ²(ν−1)/(4ν) = σ²/6 — same σ = a1+a2, same monic
  t-quadratic p, same q-slot for b (reduced pair (p,q) in t = η³). The
  two derivations (Prop 8.1(iv) ODE vs branch counting) are genuinely
  independent and agree exactly. No normalization mismatch exists to
  fake the convergence: both live on the SAME reduced patterns of G_m.

## 5. Front 5 — steps (c): pole-lead identities and ladder cells

Verdict: **CONFIRMED** (all identities hold, independently recomputed:
/tmp/lt_review_check.py, own K = Q(√3) arithmetic, no engine code), with
one EMPHASIS CORRECTION about which checks could actually have killed.

- (F_i) identity: 27a_i(a_i−b)³ = σ³(a_i − 3σ/4) verified exactly at
  both poles for five σ-samples (degree-4 identity: pinned), plus the
  value 27a_1(a_1−b)³ = σ⁴(2√3−3)/12. The E6 reduction re-derived by
  hand: lead p_{h2,P_i} = [H_M·9c_i⁵(a_i−a_j)²(a_i−b)]³ vs 6-Taylor of
  p_{h2,G_m} = (σ³/27)H_M³(3c_i²)⁶(a_i−a_j)⁶(a_i−b2); with c_i³ = a_i
  the ratio is exactly (F_i). GENUINE kill chance — held with no slack.
- Pole h1-anatomy: z(z−(3/2)w²)² − (z−w²)³ = −(3/4)w⁴z + w⁶ verified at
  5 samples (degree ≤ 3: pinned); the z²-cancellation is identical, and
  the forced eta² − (4/3)w² pattern + w_i⁴ pin follow. m_i² = s0λ_i³ ⟺
  G_M² = s0S_M³: the Taylor factors are m_i = G_M·27c_i⁶D³, λ_i =
  S_M·9c_i⁴D² and 27² = 9³ — automatic GIVEN the transported tower
  relation, exactly as the doc says ("forced AND automatic").
- EMPHASIS CORRECTION (no error, but §3's "five kill chances" oversells):
  the lead-coherence closures (iv) are exponent-TRIVIAL. All F_s-patterns
  are powers of the single block φ²ψ, so with X := (7c_m⁶)²(−A/2):
  S_M = S_F X⁶, G_M = G_F X⁹, H_M = H_F X⁸, and G²/S³ picks up X¹⁸/X¹⁸,
  H³/S⁴ picks up X²⁴/X²⁴ — identically 1 for ANY leads; "c_m⁷ = A closes
  it" only tidies the closed forms. Likewise (i) is automatic given the
  tower transport (which is St 8.3(i): same global h_j). So the genuine
  kill chances were (ii) W-collapse, (iii) (F_i), (v) the 12 cells —
  three, not five. Verdict unchanged; §3's rhetoric should be toned.
- Ladder spot-checks by hand (4 of 12): suffix/h2 (39 = 39, d-drop
  138/7 − 8/7 = 10·39/21), merge/h1 (2 = 2, 8/21 − 1/7 = 5·2/42),
  merge/g (3 = 3, 3/7 − 1/14 = 5·3/42), terminal/g (189 = 189, 63 − 9 =
  2·189/7). All exact. Free-coefficient grid arithmetic of §1c verified
  (κ-grids: 3 slots at 1/7-grid on the suffix edge, 2 at 1/21-grid per
  merge edge, none on the terminal edge — 7 total; off-grid coefficients
  would create V_1,a vertices and change Q ✓); single-rooted dead-stretch
  patterns transport leads unchanged (k-Taylor of L(η−c)^k at c is L), so
  the free coefficients do not enter any lead identity ✓.
- Engine nits: template_lift.py has two vacuous `True`-literal checks
  (line 251 "h1 pole pattern", line 351 "m-lock") — their content is
  real but proved elsewhere (lines 247-249; front 3's Cor 6.1 chain);
  the headline "46 checks" double-counts these. Cosmetic.

## 6. Front 6 — errata E10, E11 on-page

### E10 (St 3.15 label swap): **CONFIRMED in core, filing needs two fixes**

- The swap is real. Printed (p. 17): (i) d_{h,F} > 0 ⟹ h(P) = 0;
  (iii) d < 0 ⟹ h(P) = ∞. Direct asymptotics: on a form-(3) branch,
  x(P) = ∞ and h ~ x^{d_{h,F}}·p_{h,F}(c) with p_{h,F}(c) ≠ 0 (the
  coprimality hypothesis + c a root of p_{f−a,F}), and the freeze is
  real (mult(p_{h,F}, c) = 0 stops the d-drop for good): d > 0 ⟹
  |h(P)| = ∞. The thesis's own usage agrees: Prop 5.5's proof derives
  "g(P) = ∞ iff F*_P ∈ T_a,pole" from 3.15 + St 5.1 (d_g > 0 there);
  Prop 7.3's proof computes Λ(P) = −κd_{g−b,G} > 0 from d < 0 at a
  puncture where g − b VANISHES; Prop 7.2 would contradict the frozen
  d_g > 0 above pole vertices under the printed labels.
- FILING FIX 1: LROOT §6 cites "Prop 5.2's no-pole conclusion" as
  pro-swap evidence. Wrong way around: Prop 5.2's printed proof
  ("d_g > 0 everywhere... by 3.15 g has no pole") actually READS
  CORRECTLY under the printed labels and BREAKS under the swap. The
  statement survives regardless (it follows from Prop 5.1 alone, whose
  ρ-argument is self-contained), so no downstream damage — but the
  evidence list should swap 5.2 from the pro column to a "casualty
  needing repair via 5.1" note.
- FILING FIX 2: "With the printed labels, Prop 5.2/5.3/7.3 would all be
  false" overclaims: 5.3(ii) (d_{g,F} > 0 at pole vertices) is proved by
  the tower relation without 3.15 and is label-independent; the real
  printed-label casualties are 5.5 (iff), 7.2, 7.3. Core erratum stands;
  no campaign conclusion changes (only 3.15(ii) was ever load-bearing).

### E11 (St 9.6's i = deg(p_G)/M_G): **REFUTED as an erratum — demote to reading note**

- The step IS derivable from print. In St 9.6's proof (p. 52) the line
  "Assume mult(p,c) = 2. Then i = deg(p_G)/M_G = j" sits inside the
  branch where mult(p,c) = 2 = M_G (St 8.4 gives mult(p,c) | M_G = 2 and
  the mult = 1 case was dispatched first). Prop 8.1(i) (p. 40, re-read)
  gives p_F = ⊖p^i with deg p = M*_F, so St 3.17(i) gives deg p_G =
  mult(p_F, c) = i·mult(p, c) = i·M_G: i = deg(p_G)/M_G. QED from four
  printed statements — not "never justified in print".
- Silver lining (keeps TEMPLATE's substance): the same chain FORCES
  m_{F_s} = 2 from print: i = 6 ⟹ M*_{F_s} = 126/6 = 21 ≠ 63 =
  gcd(126,189) ⟹ the gcd family must contain deg p_{h1} — tower alive to
  depth 2 (equivalently: i = 2 would need mult = 6 ∤ M_G = 2). So
  TEMPLATE §5.2's claim "provable via the h1-branch count, only" is
  wrong about ONLY — but the count argument survives as an independent
  corroboration, and the m_{F_s} = 2 datum it feeds on is even firmer
  than claimed. Ledger action: strike E11; keep a reading note that St
  9.6's proof compresses a four-statement derivation into one equation.

## 7. R1 GATE — the staged linear system

**Verdict: REDESIGN** (then GO). The idea is right, the sizing is
credible, and the discriminating power is real — but the spec as written
has one outright bug and three underdeterminacies, any of which could
make the run either spuriously UNSOLVABLE (false kill) or vacuously
SOLVABLE. Fix on paper first; the fixes are cheap.

### 7a. What the spec gets right

- Naive sizing ruled out correctly: 127·43 + 190·64 = 17621 ≈ 17.6k
  unknowns — genuinely past any msolve envelope.
- Staged-linear structure is credible: the 126 y-side series are
  42-conjugate orbits of ~3 punctures (P_1, P_2, B-side), so each
  (1/42)-level adds O(3) new coefficient unknowns; each level imposes
  ~deg-many polynomiality conditions. ~50-100 levels × O(3) + tails +
  the 7 dead-stretch slots + scales ⟹ 10²-10³ unknowns over Q(√3):
  CONFIRMED credible, and each stage is massively overdetermined — an
  inconsistency (the interesting outcome) should appear early, at the R1
  depths (first sub-top bands past F_s), exactly as claimed.
- Working over Q(√3) is sound FOR LINEAR STAGES: solvability of a linear
  system over the coefficient field ⟺ over C, so an UNSOLVABLE stage is
  a genuine kill of whatever the pinned structure is (given 7c/7d).

### 7b. BUG — f vs (f−a) in the tower (must fix; false-kill risk)

Prop 4.2 (p. 19, re-read) defines the T_a^+ tower with h_{j+1} =
h_j^{k_j} − s_j·f^{l_j} — powers of f, NOT (f−a) (only the T_a^− tower,
Prop 4.3, uses f−a). SHEET6-L1 §7 had it right ("h_1 = g² − s_0f³");
SHEET6-TEMPLATE writes (f−a) throughout (§2c-E1, R1). Pattern-level
checks are unaffected (tops agree on T^+), but R1 constrains SUB-TOP
bands, where they differ: at R, g² − s0(f−a)³ = h1 − 3as0(f−a)² − ... ;
the (f−a)² term sits at level 84, so the (f−a)-version has d = 84
AUTOMATICALLY and imposing "cancellation 126 → 56" on it adds FALSE
conditions in the band [57, 84] (they force a·(stuff) = 0-type
equations). Outcomes if run as written: spurious inconsistency (false
kill) or, if the implementer stops at 84, an under-constrained band
(vacuous pass). FIX (either): (1) stage the print-true tower h1 =
g² − s0f³, h2 = h1³ − s1f⁴; or (2) fix the shift gauge a = 0 for the
distinguished fiber (f ↦ f − a), which makes the two towers coincide —
then say so in the spec and in the engine.

### 7c. Scope of UNSOLVABLE (state it; else the conclusion overclaims)

UNSOLVABLE kills ONLY the minimal-tower genome: m_{G_m} = 1 +
(k1,l1) = (3,4) + first-step merge + the L1c/suffix coefficients + the
chosen w_i fourth-root and conjugacy-alignment branches (finite: the
driver must ENUMERATE the discrete choices, not sample one). It does NOT
kill the two-pole residue-A configuration class (Q-level), because the
R6 window is open: m_{G_m} = 2 with (k1,l1) ∈ {(2,3),(2,5),(3,5),(3,7),
(3,8),(6,11),(6,13),(6,17)} changes i_{G_m}, deg q, and hence the L1c
layer itself. RECOMMENDED ORDER: run the R6 recursion (the E3-E6
mechanism one tower level up — paper-only, same shape) BEFORE R1; if R6
closes, R1 becomes decisive for the whole configuration; if not, R1's
verdict must be labeled per-branch.

### 7d. Underdetermined ingredients (spec must pin before coding)

1. g must be CO-STAGED: the tower-depth conditions are conditions on
   (f,g) jointly; the spec stages "f−a from its pinned branch data" and
   never says where g's series unknowns live. (They are top-coupled by
   G² = s0S³, but sub-top g-tails are new unknowns entering the same
   bands.)
2. x-side model: the polynomiality conditions on the y-side symmetric
   functions involve the y-lead A_{126}(x) (e_j = A_{126−j}/A_{126} is
   NOT polynomial by itself); the spec waves at "x-side tail data". Use
   the LROOT LR2 pin (single x-cluster, κ_G = 1, unsplit below R = 3):
   it makes A_{126} essentially one scaled factor — the spec should say
   exactly this (it is also R3's merge, already flagged there).
3. SOLVABLE endpoint: define the terminal nonlinear core. Without a
   final closure check (J(f,g) ∈ C* on the reconstructed pair, R5),
   SOLVABLE proves only "the genome is formally consistent to depth
   deg f" — a real theorem (an L2'-tier structure result) but NOT a
   candidate pair. With the J-check included in the ≤ 20-var core, a
   SOLVABLE outcome is a bona fide near-counterexample datum and would
   justify escalation; the spec's "expected size ≤ 20" is plausible but
   currently unsubstantiated — derive it when pinning the core.

### 7e. Gate summary

GO criteria after redesign: (i) tower normalization fixed per 7b (gauge
a = 0 recommended); (ii) conclusion template written down in advance:
UNSOLVABLE ⟹ minimal-tower genome dead (book unchanged at 8; R6 branch
inherits the configuration), SOLVABLE ⟹ formal candidate to stated
depth + terminal core outcome; (iii) discrete-choice enumeration in the
driver; (iv) g co-staged and x-side lead modeled. With those, the
experiment is cheap, decisive for its branch, and worth the compute —
GO. Without them: NO-GO (either failure mode wastes the run).

## 8. Overall verdict

Both results SURVIVE adversarial review on their mathematical content.

1. SHEET6-LROOT (c8f8bc8): **PROMOTE with corrections.** λ_root = 0
   forced at every case-IV terminal — CONFIRMED, reading-robust (neither
   the E10 swap nor the literal-E9 reading resurrects it); book stays 8;
   LR2's x-side pin and the slack-0 total rigidity (δ_a = 0 ∀a) stand;
   δ-strictness at mult ≥ 2 collisions is genuinely the last printed-
   adjacent kill surface. Required edits: E10 filing fixes (front 6),
   the two §2 wording nitpicks and (24)-sign note (front 1), and the
   vacuous assert in lroot_ledger.py line 81.
2. SHEET6-TEMPLATE (3f06c21): **PROMOTE as FORMAL-CANDIDATE with
   corrections.** The lift, the forced tower (2,3),(3,4), the h2-collapse
   re-derivation of L1c, the (F_i) identities, and the leak-free ladder
   all hold under independent recomputation; option A is dead three ways;
   the side theorem is printed-tier sound. Required edits: strike E11
   (front 6 — demote to reading note; keep the m_{F_s} = 2 forcing, now
   printed-tier); tone §3's "five kill chances" to three (front 5); note
   the one-line (3,4) forcing via Prop 4.2(iii) (front 3); FIX the f vs
   (f−a) tower normalization in §2c-E1/R1 or pin gauge a = 0 (front 7 —
   this one is load-bearing for R1); two vacuous engine checks.
3. R1 GATE: **REDESIGN, then GO** (front 7: 7b bug + 7c scope + 7d
   pins). Recommended sequencing: (a) close or open the R6 window on
   paper (same E3-E6 mechanism, one tower level up — cheapest); (b) run
   redesigned R1 on the minimal branch; (c) x-side/R2 Newton budget with
   the LR2 pin merged. Independent of R1, the sharpest THEORY target is
   unchanged: a local δ-excess formula at mult ≥ 2 collisions would kill
   all four slack-0 classes and cut the book 8 → 4.

Canonical book unchanged: td ≤ 5: 0; td = 6: 4 single-pole r9/M2 + 4
two-pole residue-A IV classes (2 robust R3 @slack 1, 2 boundary R4
@slack 0 each side), the two-pole ones now carrying the strictly rigider
FORMAL-CANDIDATE genome.

Artifacts: no engine changes made (review-only); independent verifier at
/tmp/lt_review_check.py (disposable, own Q(√3)/polynomial code, 40+
checks, ALL OK); engines re-run bit-identical (lroot_ledger asserts
pass; template_lift 46/46; campaign gate PASS).
