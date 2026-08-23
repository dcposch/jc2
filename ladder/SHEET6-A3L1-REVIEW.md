# SHEET6-A3L1-REVIEW.md — Adversarial review of SHEET6-AF3 (cec5b3b) and SHEET6-L1 (62335cc)

Reviewer: Claude (adversarial pass, 2026-08-07). Status: COMPLETE.
Scope: the two coupled unreviewed results (AF3 entry-M pin + L1 merged-
pattern lemma; L1a leans on the AF3 pin). Ground truth: refs/
sigray_full.pdf re-read on-page this review (pp. 17-19, 23-34, 38-58 —
every load-bearing formula re-read from the page images, independently of
the docs). Engines re-run: sheet6_campaign.py gate (PASS), hiii_compose.py
pin (PINNED GRAND td3 0, td4 0, td5 0, td6 4 — byte-matches AF3 §3),
twopole_check.py phases 1-4 (all counts byte-match L1 §6), l1_ode_check.py.
PLUS an independent Fraction-exact verifier written for this review
(/tmp/l1_frac_check.py; full-η identities, two gauges, own interpolation
+ poly-gcd — no shared code with the engines).

Verdicts:
- Front 1 (the pin): **CONFIRMED** (airtight from four printed statements;
  no scope leak; nothing uses |T_a,pole|)
- Front 2 (8 rows entry-dead): **CONFIRMED** (all 11 gcds recomputed from
  table (23) by hand; row 4 = St 9.6's own M=2)
- Front 3 (4 r9/M2 survivors): **CONFIRMED** (every chain re-derived by
  hand, each first-step Diophantine has a UNIQUE cell; kill-hunt negative)
- Front 4 (L1a propagation): **CONFIRMED** (mu=(1,1), k=0, lam=0 at every
  merge depth; one derivation gap in the "eta law" phrasing, closed here
  in the kill direction)
- Front 5 (L1b + ZCH emptiness): **CONFIRMED** (independent linear algebra
  reproduces the Wronskian kernel exactly: s = p^{l/2}, ct = 0 forced)
- Front 6 (L1c explicit solution): **CONFIRMED** (closed forms re-derived
  by hand, unique given sigma; sigma = 0 branch fatal; full-η identity
  verified at two gauges; a1/a2 = 2+sqrt3 exact; no printed kill found)
- Front 7 (merged-child uniqueness + book): **CONFIRMED** (first-step
  closed forms re-derived; (nu,l,n) = (3,1,5) unique IIa cell; B, A'
  deaths structural; book = A + 4 IV classes)
- Front 8 (cross-consistency, E7/E8/E9): **CONFIRMED** (all three errata
  verified on-page; the coupling is exactly the pin, which holds)

## 1. Front 1 — the pin M_F = gcd(deg p_F, deg p_g,F), re-derived

Verdict: **CONFIRMED**. Chain re-read on-page, attacked at both suggested
joints; neither gives.

- Not 8.1 (p. 39) verbatim: "Set F ∈ T_a, m = m_F, h_i = h_{i,F}
  (i = 0,...,m) (cf Proposition 4.2). Define M_F := gcd(deg p_F,
  deg p_{h_0,F}, ..., deg p_{h_m,F})." Prop 4.2 (p. 19) opens "Set
  h_0 = g" — h_0 IS g by definition, so p_{h_0,F} = p_{g,F} literally;
  no degree-preservation issue exists (the attack dissolves: there is no
  identification to preserve, only an identity).
- "Every pole vertex vs only F_P*": Not 5.2 (p. 25) DEFINES T_a,pole :=
  {F_P* : P ∈ R̄_a \ R_a} ∩ T_a^+, and Not 5.1 defines F_P* := I_P(u)
  with u as in Prop 5.1, whose (i) is m_F = 0. So every pole vertex is an
  F_P* with m = 0 by construction; the (iii) u* ≥ u clause is not even
  needed. With m = 0 the Not 8.1 family is {h_0} = {g}: M_F =
  gcd(deg p_F, deg p_{g,F}). ∎ Scope: Prop 4.2 needs F ∈ T_a^+ —
  guaranteed by Not 5.2's ∩ T_a^+.
- Cardinality audit: Prop 4.2 is per-vertex, Prop 5.1 per-P, Not 8.1
  per-vertex — nothing in the pin uses |T_a,pole|, confirming the
  transport to both configurations. The KILL needs Prop 8.4 (p. 44,
  hypothesis "T_a,pole = {G}" re-read) — correctly localized by AF3 §1.
- Entry = pole vertex: Prop 9.2 (p. 50) starts the characteristic
  sequence at "F_0 := F" with F ∈ T_a,pole — verbatim. And Prop 8.4
  applies AT F_0: pole vertices are always searrow (this review): d_F > 0
  (Prop 5.3(ii) prints d_g,F > 0 and d_g,F = (k_f/k_g)d_F) and d_F +
  d_g,F = 1−u (Prop 5.1's ρ ≡ 0 at F_P*), so d_F < (1−u)·deg p_F holds
  since deg p_F ≥ 2 (5.3(iv) + St 3.16). V_a membership is 5.3(iv).
- E8 confirmed: Prop 5.1's proof (p. 24) cites "Proposition 8" twice;
  no such proposition exists; "(8)" of Prop 4.1 (p. 18) is what the
  monotone-ρ argument uses. Cosmetic, as filed.

## 2. Front 2 — the row table recomputed from (23)

Verdict: **CONFIRMED**. Table (23) (p. 46) re-read cell by cell (its
column order is (D_F, D_g,F), (deg p_F, deg p_g,F), ν, Λ; note the
printed table mislabels row 5 as a second "6" — pilot numbering is the
sane one). Hand gcds of the degree pairs:
r1 (2,3)→1, r2 (2,3)→1, r3 (2,3)→1, r4 (4,6)→**2**, r5 (3,4)→1,
r6 (3,4)→1, r7 (2,5)→1, r8 (6,15)→**3**, r9 (6,10)→**2**, r10 (4,5)→1,
r11 (5,6)→1 — identical to AF3 §2 and to the engine's PIN_EXPECT (whose
keys/Λ-values also match (23)'s Λ column: 3;6;6;4;4;6;5;6;6;5;6). Row-4
cross-check: St 9.6's hypothesis (p. 51) is Q(G) = (j,2j,3,2,5); at
j = 2 this is (D,degp,ν,M,κ̄) = (2,4,3,2,5) = row 4's pinned entry with
κ̄ = D+D_g = 5 (St 9.1, p. 48) — the thesis's own printed M = 2 IS the
pin value. AF3-refutation arithmetic: r8 gcd(D,P) = gcd(2,6) = 2 ≠ 3,
r9 gcd(3,6) = 3 ≠ 2, r4 gcd(2,4) = 2 = gcd(4,6) coincidence — all check.
No resurrection: the 8 dead rows stay dead.

## 3. Front 3 — the four survivors, chased end to end by hand

Verdict: **CONFIRMED**; no missed kill found after a genuine hunt.

- Entry r9: Q = (3,6,5,2,8) (κ̄ = 3+5, St 9.1). Step transport re-derived
  from Prop 9.3(b)/(d) alone (μ(ρ_G+n)/(κ̄_G+n) = dp/dq; κ̄_F =
  (κ̄_G+n)/ν_G ∈ N — form matches the printed instantiations on pp. 52-53
  exactly).
- Class 1 route μ=2 IIa k=1: 3ν/(2ν+1) = (1+2n)/(8+n) ⇒ n = (22ν−1)/(ν+2)
  ⇒ ν+2 | 45; the mod-5 test kills all but ν=7, n=17 (UNIQUE). Child
  (21,63,7,3,5), M = gcd(21,15) = 3. Class 2 route k=2: n = (29ν−1)/
  (2(ν+1)) ⇒ ν+1 | 30; unique ν=5, n=12; child (15,60,5,4,4).
- s-families: 9.7(iv) and 9.8(iv) (pp. 54-56) re-read verbatim; both are
  the λ = 0 children as claimed. Terminals via Prop 9.3(k)/(l)/(m): (k)
  gives d_F = j(3s+2) resp. (4s+3)j (perfect-square collapse (3s+2)²,
  (4s+3)² — checked symbolically), (l) strict, (m) = 1 in all four. R = 3
  resp. 4; ψ = 2 resp. 3 (sharp: case IV's (0,y) ∉ V_1,a ∪ V_2,a plus
  St 3.16's explicit exclusion of (0,y) from the root-count iff — p. 17
  re-read — blocks any printed ψ-upgrade); budgets 3/3/2/2 vs Σλ = 2:
  slacks 1,1,0,0. λ-pricing at the k≠0 steps re-derived from corrected
  (24): per-orbit price D_F/i − κ̄ = 7−5 = 2 (class 1: one orbit ⇒ 2) and
  15/3−4 = 1 (class 2: two orbits ⇒ 2) — matches the engine's λ≥2, and
  9.6(iii)/(C) print the same numbers in the row-4 analog.
- Kill attempts (all negative, AF3 §5 re-audited): ψ-upgrade blocked by
  St 3.16's (0,y)-exclusion (on-page); λ_root already charged — St 9.4's
  proof (p. 49) prices the T_a,cv ∩ T_a,x vertex AS ψ via Cor 7.1
  (re-read; the ψ-budget is that charge, not an extra); St 8.5 at the
  terminal gives M_{(0,y)} | M_F only divisibility. One NITPICK: AF3 §4's
  "Prop 8.4 forbids M_{(0,y)} = 1" needs (0,y) ∈ T_a^searrow, which no
  printed statement supplies — but this is a consistency remark, not a
  kill or a survival condition; no verdict touched.
- Entry realizability (AF3 §4): verified exactly. Prop 5.4 (p. 26) parity
  (ii) is forced (6 ≡ 1, 10 ≡ 0 mod 5); with p = η(η⁵−A), p_g =
  B(η¹⁰−(5/3)Aη⁵+(5/9)A²): 3pp_g′−5p′p_g = (25/9)A³B verified by exact
  arithmetic (A=3, B=9 → 675 ✓); squarefree (disc (5/9)A² ≠ 0) and
  coprime (values at t=0, t=A nonzero) — Prop 5.3(iii)/(v)/(vi) all hold.

## 4. Front 4 — L1a pin propagation

Verdict: **CONFIRMED** at every vertex and every merge depth.

- (a) Both poles row 1, M = 1: Λ = 3+3 forced (Prop 5.8 (20) + 5.7,
  pp. 27-28, re-read); row 1 is (23)'s unique Λ=3 row; pin gives
  gcd(2,3) = 1. Same chain as front 1 — no |T_a,pole| dependence.
- (b) The induction re-audited step by step. St 8.4 (p. 42, proof
  re-read: the Bezout-transported p* = p^i argument is sound):
  mult(p_H, c) | M_{previous} = 1 ⇒ chain orbit simple. Any second root
  of the reduced p (orbit or η): its child exists (St 3.18), is searrow
  (St 8.2 iff: deg q·mult ≥ deg q > deg p — the chain edge already
  forces deg q > deg p), and has deg p = i·mult ≥ 2 since i = full
  pattern degree of the pole-ward chain vertex (St 3.17(i)) ≥ 2 always
  (row-1 pole starts at 2); Prop 6.8 (p. 34, "deg(p_F) ≠ 1" hypothesis
  checked) then manufactures a third pole. So p = single simple orbit;
  q ≡ 1 mod ν (see below) gives M = gcd(ν, nν+1) = 1 — verbatim the
  thesis's own mult(p,c) = 1 case (St 9.6's proof, p. 52, re-read). λ = 0:
  no non-chain direction exists to be nearrow (St 9.3 needs one), and
  pole branches carry no cv vertex (A2P front 4's Prop 5.5 + St 3.15(ii)
  chain, standing). Interior chain-at-0 vertices cannot exist (mult(p,0)
  = 1 forces p_red = η alone ⇒ single-rooted full pattern ⇒ not in
  V_1,a ∪ V_2,a by St 3.16): the 0-direction materializes only AT a merge
  (ZCH) — the doc's careful clause is exactly right.
- (c) At G_m: μ_i = mult(p,c_i) | M_{H_i} = 1 both chains, at ANY depth;
  distinct orbits by St 3.18's one-continuation-per-orbit; k = 0 and no
  η extra by the same third-pole argument (i₀ ≥ 2 holds: i₀ = full
  pattern degree of the last pre-merge vertex, ≥ 2 even for immediate
  merges). Three shapes exhaustive. ✓
- DERIVATION GAP (closed here, kill-direction): §1a's "ν-equivariance
  makes e0 ≡ 1 mod ν" overstates — equivariance alone only makes q's
  exponents constant mod ν. What actually forces grade-1 purity is the
  graded decomposition of 8.1(iv): L(q_j) has grade j−1, RHS ⊖p grade 0
  (IIa), so q_j for j ≠ 1 solves the homogeneous equation, whose only
  polynomial solutions are c·p^{1/ρ} — a non-polynomial unless 1/ρ ∈ N,
  and in THAT resonant case no grade-1 inhomogeneous solution exists at
  all (its top can never cancel: dq ≡ 0 ≢ 1 mod ν), so the cell is EMPTY
  rather than differently-shaped. Either way dq ≡ 1 mod ν and the three-
  family menu is exhaustive; every enumerated cell is unaffected. The
  printed anchor is St 8.5's proof (p. 43): "p_G(η) = p̃(η^ν), by
  Proposition 4.6, one gets p_{h,G}(η) = ηr(η^ν)" — same inference,
  thesis's own words, for the non-merge case. ZCH grading (p grade 1)
  gives the same conclusion, with in-grade resonance possible exactly
  when ν+1 | l — reproducing the (2,3) degeneracy found in front 5.
- Engine note: phase 4's zch_children PRE-MERGE nodes (p_red = η, ν=1)
  are not legitimate V_a vertices (previous bullet); pure over-generation
  — harmless, since it only adds parent candidates and all in-caps pairs
  landed on the same cells. Worth a comment in the code, nothing more.

## 5. Front 5 — L1b and the ZCH cell

Verdict: **CONFIRMED**, and the two mechanisms agree beautifully.

- Equivalence re-derived by hand: q = ps ⇒ ρps′ + (ρ−1)p′s = ⊖, ρ =
  2/(2+l) ⇒ 2ps′ − lp′s = c′ ⇒ (s/p^{l/2})′ = (c′/2)p^{−(l+2)/2} (exact).
  Residue at t = a_1 for l = 2: −2/(a_1−a_2)³ (hand-checked; matches the
  doc's value); for general even l the residue is ±binom(2m−2,m−1)
  (a_1−a_2)^{−(2m−1)} ≠ 0, m = (l+2)/2. Log terms ⇒ c′ = 0 ⇒ contradicts
  ⊖ ≠ 0. Odd l has M = 1 (restored 8.4) — nothing left over. The e0 = 1
  variants are the same q = ps form with s(0) = 0 and are covered by the
  same argument (the doc's separate cell checks are belt-and-braces).
- Independent full-η linear algebra (this review, own code, gauge
  p = (t−1)(t−4)): l = 2 forces s = p exactly, ct = 0; l = 4 forces
  s = p² exactly, ct = 0 — i.e. the solver lands precisely on the log
  argument's kernel s ∝ p^{l/2} with vanishing constant. Root law +
  ⊖ ≠ 0 both violated: EMPTY. ✓
- ZCH: reach closed form re-derived by hand from the entry edge equation:
  n = ((4−l)ν+4)/(lν), n odd ⇒ cells (2,1,5) [M = gcd(3,1) = 1, dead]
  and (2,3,1) [M = 3] only — matches doc §4b. The (2,3) cell: my full-η
  solve (gauge c = 1) forces s = t(t−1)² AND ct = 0: s(0) = 0 (η-mult 2
  in q), s(1) = 0 (chain orbit squared), constant zero — triple
  violation, independent of the engine. Its child (1/3,2,3,3) is also
  suffix-DEAD (engine, 276/276). The locally-solvable (ν odd, l = 2)
  cells: n = 1 + 2/ν ∉ N for odd ν ≥ 3 — unreachable, confirming the
  doc's reach claim.

## 6. Front 6 — the (3,1) solution, recomputed from scratch

Verdict: **CONFIRMED**, uniqueness and all.

- The reduced-in-t equation ρ·pt·s + νρ·t·pt·s′ + (ρ−1)ν·t·pt′·s = ⊖ was
  re-derived from 8.1(iv) by substituting p = pt(η^ν), q = η·pt·s(η^ν)
  and dividing by pt — it is the correct reduction (same for the ZCH and
  C forms; all three re-derived).
- Hand solution of the general-ν l=1 system: t³ auto-cancels iff ρ =
  2ν/(3ν+1) (= Cor 6.1, consistent); t²-row ⇒ 2νb = σ(ν+1); t¹-row ⇒
  2π(ν+1) = σb(ν−1). Triangular ⇒ UNIQUE given σ: b = σ(ν+1)/(2ν), π =
  σ²(ν−1)/(4ν), c̃ = −ρπb = −σ³(ν−1)(ν+1)/(4ν(3ν+1)) ≠ 0. σ = 0 branch:
  forces b = 0 AND π = 0 — both fatal (η-mult 2 in q; zero orbit) — so
  no second family hides there. At ν = 3: a_{1,2} = (σ/2)(1 ± 1/√3),
  a_1/a_2 = (√3+1)/(√3−1) = 2+√3, b = 2σ/3 — all exact.
- Full-η verification (own Fraction code): identity ρpq′ − p′q = c̃p
  HOLDS exactly at σ = 3 (c̃ = −9/5, matching the engine) AND at the
  independent gauge σ = 5 (c̃ = −25/3, matching my closed form); wrong b
  fails at degree level. ALL of 8.1(iv)'s demands checked: the identity
  itself, ⊖ ≠ 0, (v) M = gcd(6,10) = 2, root law (each p-root simple in
  q, extra b-orbit simple, η exactly 1), roots distinct/nonzero, b not a
  root, b ≠ 0.
- No further printed constraint kills it: St 3.16 structure ✓ (p =
  p̃(η³), l = 0); St 3.17/3.18 ✓ (two orbits, one continuation each);
  St 8.2 ✓ both edges (10·1 > 6); St 8.4 ✓ (1 | 1); St 8.5 exempts
  V_2,a; Prop 9.3(b)/(d) are the reach equations themselves; the l = 0
  printed arguments (9.6-9.11, "by Statement 8.2, l = 0") all route
  through regularity forcing non-searrow siblings — re-read at 9.6's
  proof: the siblings must be NEARROW for 8.2 to cap deg q, and at G_m
  regularity fails by construction (both chains are legitimate searrow
  °-preimages), which is L1 §3's blind spot, verified verbatim. St 9.8's
  proof kills l > 0 at single-pole vertices by DIOPHANTINE reach, not by
  any local bound — corroborating that no local l-bound exists in print.
- Suffix rigidity: family C ((42,126,7,3,5), ρ = 21/15, p = (t−A)²(t−B),
  q = η(t−A)(t−B)): full-η identity holds at B = (3/2)A with c̃ = 21/10;
  my own interpolation of the residuals as B-polynomials + poly-gcd gives
  gcd = (B − 3/2): B = (3/2)A is the UNIQUE solution over C. Four wrong-B
  spot checks fail. (Engine's family C output independently reproduced.)

## 7. Front 7 — the funnel and the final book

Verdict: **CONFIRMED**.

- Engine reproduction (this review's runs): phases 1-3: 133 shapes /
  47970 merges = 46337 + 745 + 336 + 552 / residues A@0 (4 IV) + B@1
  (2 IV) / 0 root merges — byte-identical to L1 §6 and to A2P front 7's
  derived-IIb rerun. Phase 4: 26 pre-merge shapes (all M=1, λ=0) / 18427
  = 17199 M=1-killed + 601 ν=1 (325 on child (1,1,2,4) + 276 on
  (1/2,1,2,3), both L1b-dead) + 276 ZCH (suffix-DEAD) + 351 residue pairs
  — ALL 351 landing on the single child (1/2,3,2,5)@0 = Q(G_m) =
  (6,12,3,2,5), with the same 4 IV classes.
- First-step closed forms re-derived by hand from (1+n)/(5+n) = dp/dq:
  IIa: n = ((8−l)ν−1)/(lν+1), n odd ⇒ ν+1 | 8 at l=1 ⇒ (3,1,5) UNIQUE
  (ν=7 gives even n); l ≥ 2 all fail (2ν+1 | 8 etc.); I: n = 8/l − 1 ⇒
  (1,2,3), (1,4,1) [L1b-dead]; ZCH: (2,1,5) [M=1], (2,3,1) [§5-dead].
  Uniqueness of the merged child datum within caps: CONFIRMED, at every
  merge depth (the 2POLE §7.3 "immediate merge" correction stands).
- B and A' deaths: structural, from front 4 — B's μ=(2,2) needs
  2 | M_pole = 1; A's Σλ=1 sibling A' needs a charged pre-merge step and
  all are λ-free. Legacy 12 → 4 verified line by line against the phase
  1-3 output; promoted book unchanged: **residue A alone, 4 IV classes
  (2 robust R3 @slack 1, 2 boundary R4 @slack 0)**.

## 8. Front 8 — coupling, errata, independence

Verdict: **CONFIRMED**.

- Coupling: L1a(a) uses only the pin at ROW 1 (gcd(2,3) = 1), which needs
  Not 8.1 + Prop 5.1 + Not 5.1/5.2 + table (23) row 1 — all confirmed at
  front 1 independent of AF3's row-8/9 content. Were fronts 2-3 somehow
  wrong, L1 would be untouched; were front 1 wrong, BOTH results fall —
  but it is the single most solid item in either doc (four printed
  statements, one definition-unfold).
- No double-counting: single-pole book (4 classes) and two-pole book
  (A + 4 IV) sit on disjoint hypotheses |T_a,pole| = 1 vs 2; the shared
  terminal shapes are shape-coincidence (A2P front 7(a) note extends).
- E7 upgrade: root law re-derived from (iv) by order counting (mult n ≥ 2
  at a common root makes LHS order ≥ m+n−1 > m; n = 0 makes it m−1 < m;
  away-roots: order n−1 vs 0 ⇒ simple) — and 9.6(II)(b) as printed
  (p. 52) has q ∝ (η^ν−c^ν)² while its own proof computes deg q =
  (k+1)ν+1: the printed pattern violates the identity its proof solves.
  Sub-erratum verified: 9.6(iii)(A)'s ratio 21/15 forces q = η(t−A)(t−B)
  = η·rad(p) (deg 15 = 1+7+7). PROOF-LEVEL as claimed.
- E8: on-page ✓ (§1). E9: Not 9.3's literal Y(F) (p. 49 re-read: "∃P:
  F = I_P(u) and H = I_P(π(H))") puts every cv vertex on a common ray
  with every chain vertex root-ward of its separation point, so the
  literal Σλ over a chain recounts each H; St 9.4's proof feeds ∪Y(F_i)
  ∪ {G} to Cor 7.1 as a plain set — the branch-at-F reading is forced.
  REAL definition/usage mismatch, correctly the standing H2 reading. ✓
- AF2 consistency: pin mode sets IIB_DERIVED = True (A2P fix 1) —
  checked in code; `iib` and gate outputs unchanged.

## 9. Overall verdict

Both results SURVIVE adversarial review; nothing is refuted, nothing
demoted. Recommend **PROMOTE BOTH**, with three cosmetic notes:

1. SHEET6-AF3 (cec5b3b): promote as-is. One nitpick: §4's "Prop 8.4
   forces M_{(0,y)} ≠ 1" silently assumes (0,y) ∈ T_a^searrow (not
   printed); it is a consistency remark with no verdict weight — suggest
   a hedge word. The pin, the 11-row table, the refutation arithmetic,
   the 4-class book, and both §5 negative results are exactly right.
2. SHEET6-L1 (62335cc): promote as-is, with (a) §1a's eta-law
   justification rewritten per front 4 (graded-ODE + resonance-emptiness,
   not bare equivariance — conclusion unchanged, every enumerated cell
   unaffected); (b) a code comment that phase-4 zch PRE-MERGE nodes are
   conservative over-generation (not V_a-legitimate).
3. Ledger: E7 proof-level upgrade CONFIRMED; E8, E9 CONFIRMED as filed.

NET STATE (post-review book). (a) td ≤ 5: residual 0, now doubly covered
(AF2 kill + entry-death of r7/r10; r1/r5 entry-dead). (b) Single-pole
td=6: 8 of 9 rows entry-dead; r8/M3 chain-closed; residual = the 4
r9/M2 classes on entry Q = (3,6,5,2,8), type (3,5), UNCONDITIONAL at the
entry layer: (1/3,7,3,5)@2 and (2/3,3s+2,3,2s+2)@2 at slack 1;
(1/4,5,4,4)@2 and (3/4,4s+3,4,3s+3)@2 at slack 0. SF1: 0. (c) Two-pole
td=6: residue A alone — unique merged child Q(G_m) = (6,12,3,2,5)@Σλ=0
via IIa(l=1), ν=3, at any merge depth, with the rigid template a_1/a_2 =
2+√3, b = (2/3)(a_1+a_2), suffix scale B = (3/2)A; 4 IV classes (2 robust
R3, 2 boundary R4). Any λ_root ≥ 1 strengthening kills the two slack-0
single-pole classes and the two boundary two-pole classes, leaving 2+2.
The whole td=6 question now rests on genuinely new mathematics: L1 §7's
h_1-branch budget at the resonant direction, Puiseux transport between
the pinned patterns, or AF3 §6's single-rooted-terminal arguments.

Artifacts: no engine changes needed; this review added only
/tmp/l1_frac_check.py (independent verifier, disposable). All four
engines reproduce their docs bit-for-bit; gate PASS.
