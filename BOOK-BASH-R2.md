# BOOK-BASH-R2.md — round 2: the 13 remaining classes (37 instances), book fully adjudicated

Status: SYNTHESIS of the round-2 per-class bash campaign, 2026-08-12.
Ground: BOOK-BASH.md (round 1: arsenal, kill-record style, proven kill
patterns), BOOK-ENUM.md + systems/book/*.json (cell data, cross-checked
per class, no mismatches), engines cases/{l1_ode_check, hiii_compose,
h3_check, sheet6_campaign, depth_closure_check, book_enum}.py
(read-only), thesis refs/sigray_full.pdf (Prop 8.1(iv) re-read on-page,
p.39–41), forced readings per SIGRAY-AUDIT.md. Arsenal applied in order
per class: **T1** pattern algebra (SHEET6-L1 method, Prop 8.1(iv)
δ·p·q′ − (1−u)·p′·q = ⊖·p on the cell's (p,q) shapes), **T2** suffix
chase (hiii_compose composed kill set + ψ-budget vs St 9.4), **T3**
coefficient lift (SHEET6-TEMPLATE E-mechanism), **T4** w-arithmetic —
with stop-at-first-kill. Every harness was gated on promoted round-1
records (residue-A check_A_l1(3) and/or ZCH(2,2,3) check_ZCH(2,3));
gate PASS in every run. All arithmetic exact (python fractions).

## 0. Verdict

**13 of 13 remaining classes bashed (37 of 37 instances) — the 22-class
book is now fully adjudicated at 75/75 instances. 12 classes KILLED
outright (35 instances DEAD: 13 review-confirmed with 2 votes, 7 with 1
vote banked, 15 engine-verified pending review); 1 class SURVIVES
(ZCH(2,3,2)M2@w6, 2 instances), bottoming out in a rigid one-scale
residue-A-type template.** Every round-2 kill is T1, known kill pattern
(a) — a divisibility-forced ⊖ = 0 degeneracy of Prop 8.1(iv) — and the
campaign closed both criteria in closed form:

- **Family Z:** the reduced ODE's triangular ladder forces the unique
  monic s with c̃ = 0 (⊖ = 0, contradicting the printed ⊖ ≠ 0) **iff
  (ν+1) | l** (exact-sweep verified over ν ≤ 7, l ≤ 12). All 7 remaining
  ZCH cells with (ν+1) | l die: (2,6) [3|6], (4,5) [5|5], (2,3) [3|3],
  (2,9) [3|9], (3,4) [4|4], (3,8) [4|8], (6,7) [7|7]. The residual
  forced shape s = t^m(t−a)^{l−m} is in every case independently
  multiply-inadmissible (root law, η law, MP6(c)).
- **Family I (ν = 1):** the merged-shape ODE degenerates onto the
  homogeneous branch **iff l/r ∈ ℤ (Wronskian / Laurent-residue
  C(−n,n−1) route, the r ≥ 3 log-obstruction analogue flagged in
  BOOK-ENUM §5.4) or r/l ∈ ℤ (reversed ladder, p = σ² forced)**. All 5
  book cells satisfy one of the two: (3,3), (4,4) [r=l], (3,6), (4,8)
  [l=2r], (4,2) [r=2l]. All die.

ZCH(2,3,2)M2@w6 is the unique remaining ZCH/I cell missing both
criteria ((ν+1) = 4 ∤ l = 2); T1/T1b/T2/T3 all close consistently on a
rigid template (c̃ = (9/40)a³ ≠ 0, roots (3±√3)a/4), joining the six
round-1 IIa survivors. All kills are vertex-local in (fam, r, ν, l) and
frame-free — no td, m, w, κ̄, or entry datum enters any solve — so each
single solve kills the class's entire panel set. **No new td becomes
fully excluded** (td = 7, 11, 13 remain the only ones): residue-A
IIa(2,3,1)M2@w2 still sits in every non-empty panel and survives, and
every composite td stays independently blocked by the TDU single-pole
residual. But the multi-pole book shrinks 62 → 27 live instances, and
every one of the 27 is now a bashed, rigid template — the unbashed
category is empty.

## 1. Verdict table

Round-2 classes (cell = (fam, r, ν, l) M @ w, κ̄_m, child (κ̄, D/i, ρ)):

| class | cell / child | panels | verdict | mechanism | confirmed? |
|---|---|---|---|---|---|
| ZCH(2,2,6)M3@w4 | κ̄5, (5,1,1/3) | 7: m=2 td9,12,14; m=3 td9,12,14; m=4 td12 | **DEAD** | T1 (family Z), ρ=1/5: ladder numerator (ν+1)j−l = 0 at j=2 (3\|6) ⟹ unique s = t²(t−a)⁴, c̃=0 ⟹ ⊖=0; quadruple-inadmissible (η law, root-law q-mult 5, MP6(c)). Frame-free ⟹ all 7 panels | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, incl. full independent re-implementation + on-page Prop 8.1(iv) check) |
| ZCH(2,4,5)M5@w4 | κ̄5, (5,1,1/5) | 7: m=2 td9,12,14; m=3 td9,12,14; m=4 td12 | **DEAD** | T1, ρ=1/5: k=0 numerator (ν+1)(k+1)−l = 5−5 = 0 ((ν+1)\|l ⟺ M=ν+1) ⟹ unique s = t(t−a)⁴, c̃=0 ⟹ ⊖=0; triple-inadmissible (root law, η law, MP6(c)) | 1 vote banked (KILL CONFIRMED, no escape); 1 more for full confirmation |
| ZCH(2,2,3)M3@w6 | κ̄9, (9,3,1) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, ρ=1/3: unique s = t(t−a)², c̃=0, q = p³ = p^{1/ρ} exactly the homogeneous branch; ⊖=0 + root law (q-mult 3) + η law (η-mult 3). Banks round-1 rider 3 as its own record | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, fresh-route re-derivations) |
| ZCH(2,2,9)M3@w6 | κ̄7, (7,1,1/3) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, ρ=1/7: numerator (2−k) = 0 at k=2 (3\|9) ⟹ unique s = t³(t−a)⁶, c̃=0 ⟹ ⊖=0; root-law q-mult 7, η-mult 4, MP6(c) | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, no escape found) |
| ZCH(2,3,2)M2@w6 | κ̄10, (10,4,1) | 2: m=2 td12; m=4 td12 | **SURVIVES** | T1/T1b/T2/T3 exhausted: full-rank ladder, c̃ = (9/40)a³ ≠ 0, admissible s with roots (3±√3)a/4; T1b (zch3_edges/Prop 9.3): ratio-partner realizable in both panels, td=6 non-joinability does NOT transfer; T2: 13 IV-survivor classes at λ=4..8, 0 open, 0 frontier; T3: all count laws close with equality (deg 39 = k_G+1, M_G = 2, a-free s1-transport) | n/a (survival; superset-sound) |
| ZCH(2,3,4)M4@w6 | κ̄8, (8,2,1/2) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, l = ν+1 ⟹ ρ = 1/(ν+1) = 1/4, B₀ = 0 ⟹ unique s = t(t−a)³, c̃=0 ⟹ ⊖=0; triple-inadmissible (0-root, triple root q-mult 4, MP6(c)) | **YES** — kill_confirmed, 2 votes (NOT REFUTED / CONFIRMED, no escape found) |
| ZCH(2,3,8)M4@w6 | κ̄7, (7,1,1/4) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, ρ=1/7: k=2 numerator 2·4−8 = 0 (4\|8) ⟹ unique s = t²(t−a)⁶, c̃=0 ⟹ ⊖=0; criterion sweep (ν,l) ∈ [1..7]×[1..12]: ct=0 ⟺ (ν+1)\|l | ENGINE-VERIFIED, REVIEW-PENDING (0 votes) |
| ZCH(2,6,7)M7@w6 | κ̄7, (7,1,1/7) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, l = ν+1 = 7 ⟹ ρ=1/7, k=1 numerator zero ⟹ unique s = t(t−a)⁶, c̃=0 ⟹ ⊖=0; quadruple-inadmissible (root-law q-mult 7, η-mult 7, MP6(c)) | ENGINE-VERIFIED, REVIEW-PENDING (0 votes) |
| I(3,1,3)M3@w2 | κ̄4, (4,2,2/3) | 4: m=3 td9,12,14; m=4 td12 | **DEAD** | T1, r = l (l/r = 1): constant-Wronskian rigidity W(s,p) = 2c̃; p·s″ = p″·s forces s = p for every cubic (kernel 0, residue obstruction −c′p″(aᵢ)/3p′(aᵢ)³ closes all branches) ⟹ W = 0 ⟹ ⊖=0; s = p triply inadmissible | ENGINE-VERIFIED, REVIEW-PENDING (0 votes) |
| I(3,1,6)M3@w2 | κ̄3, (3,1,1/3) | 4: m=3 td9,12,14; m=4 td12 | **DEAD** | T1, r \| l (l = 2r): (S/p²)′ = 3c̃/p³, Laurent residues N = 6u²+9uv+6v², pairwise resultants 800 ≠ 0 ⟹ ≥2 residues nonzero always ⟹ c̃=0; residual S = p², q = p³ triply inadmissible; both e0-subvariants closed (l ≤ 4 cap flag retired at l=6) | ENGINE-VERIFIED, REVIEW-PENDING (0 votes) |
| I(4,1,2)M2@w2 | κ̄6, (6,4,1) | 1: m=4 td12 | **DEAD** | T1, l \| r (r/l = 2, reversed divisibility): constant-pivot ladder (2,4,6,8) forces p = σ² for EVERY monic σ, c′ = 0 ⟹ ⊖=0; p non-squarefree contra r = 4 distinct arriving directions (MP6 D6d(a)); root-law mult 3; η-subvariant p = t²(t−b)² subsumed | ENGINE-VERIFIED, REVIEW-PENDING (0 votes) |
| I(4,1,4)M4@w2 | κ̄4, (4,2,1/2) | 1: m=4 td12 | **DEAD** | T1, r = l: Wronskian ladder, pivots (6,10,12,12) force s = p unconditionally ⟹ q = p², 2c = W(p,p) = 0 ⟹ ⊖=0; root-law q-mult 2 at all four roots; residue corroboration (p″ deg 2 < 4 distinct roots) | ENGINE-VERIFIED, REVIEW-PENDING (0 votes) |
| I(4,1,8)M4@w2 | κ̄3, (3,1,1/4) | 1: m=4 td12 | **DEAD** | T1, r \| l (l = 2r, n = 3): c ≠ 0 forces all residues of p⁻³ zero ⟹ H = 336p exactly ⟹ p = (t+a/4)⁴, triply inadmissible; c = 0 branch: kernel S = Cp², q = Cp³ ⟹ ⊖=0 + root-law q-mult 3. Both e0-subvariants covered | ENGINE-VERIFIED, REVIEW-PENDING (0 votes) |

## 2. Kill records (decisive arithmetic)

- **ZCH(2,2,6)M3@w4** (T1). Reduced family-Z ODE at ρ = 3/15 = 1/5:
  ladder s_{j−1} = a((ν+1)j−l)/((ν+1)(j−1−l))·s_j from s₆ = 1 gives
  s₅ = −4a … s₂ = a⁴, then the j=2 numerator 3·2−6 = 0 forces
  s₁ = s₀ = 0 ⟹ unique s = t²(t−a)⁴ (diagonal −36,…,−6 all nonzero,
  full rank) and c̃ = (aνl/D)s₀ = 0 for every gauge — ⊖ = 0 contra Prop
  8.1(iv); residual quadruple-inadmissible. Frame-free ⟹ all 7 panels.
  Machine: /tmp/zch226_verify.py (5 gauges, two independent routes) +
  engine check_ZCH(2,6) → s=[0,0,1,−4,6,−4,1], ct=0. Gates PASS.
  **kill_confirmed, 2 adversarial votes.**
- **ZCH(2,4,5)M5@w4** (T1). ρ = 5/25 = 1/5; k=4..1 give s₄ = −4a,
  s₃ = 6a², s₂ = −4a³, s₁ = a⁴; k=0: −25s₀ = a(5−5)s₁ = 0 ⟹ s₀ = 0,
  c̃ = (ρ−1)(−a)s₀ = 0 — the (ν+1) | l trigger IS the label M = ν+1 = 5.
  Unique s = t(t−a)⁴, triple-inadmissible. Machine: /tmp/zch245_verify.py
  (6 gauges, rank 5) + engine check_ZCH(4,5). Gates PASS. **1 vote
  banked (KILL CONFIRMED, no escape); second vote outstanding.**
- **ZCH(2,2,3)M3@w6 κ̄9** (T1). Same (ν,l) = (2,3) solve as the round-1
  @w4 kill (ρ = 1/3, s = t(t−a)², c̃ = 0), banked as its own record for
  the w=6/κ̄9 frame: q = η³(η²−a)³ = p³ = p^{1/ρ} identically — the
  homogeneous branch, with ⊖ = 0 + root-law + η-law violations; child
  cross-check ρ_child/(D/i) = 1/3 in both frames. Machine:
  /tmp/zch223_w6_verify.py (5 gauges, rank 3/3) + engine agreement.
  **kill_confirmed, 2 adversarial votes** (fresh-route re-derivations).
- **ZCH(2,2,9)M3@w6** (T1). ρ = 3/21 = 1/7; (7/2)E = t²s′ − ats′ − 9ts
  + 3as; recursion s_k = a(2−k)/(9−k)·s_{k+1} gives s₈…s₃ =
  (−6a, 15a², −20a³, 15a⁴, −6a⁵, a⁶), numerator zero at k=2 ⟹
  s₂ = s₁ = s₀ = 0 ⟹ unique s = t³(t−a)⁶, c̃ = (6a/7)s₀ = 0 ⟹ ⊖ = 0;
  q-mult 7 at the chain orbit, η-mult 4, MP6(c). Machine:
  /tmp/zch229_verify.py (5 gauges, 9×9 full rank) + engine
  check_ZCH(2,9). **kill_confirmed, 2 adversarial votes.**
- **ZCH(2,3,4)M4@w6** (T1). l = ν+1 ⟹ ρ = 1/4 (the degenerate
  subfamily (l+1)ν+1 = (ν+1)²); A_k = (3/4)(k−4), B_k = (3/4)k, B₀ = 0
  ⟹ unique s = t(t−a)³, c̃ = 0 ⟹ ⊖ = 0; triple-inadmissible. B₀ = 0 ⟺
  l = ν+1 is the trigger. Machine: /tmp/zch234_verify.py (5 gauges,
  rank 4/4; nondegenerate control (3,2) gives ct = 9/40 ≠ 0) + engine
  check_ZCH(3,4). **kill_confirmed, 2 adversarial votes.**
- **ZCH(2,3,8)M4@w6** (T1). ρ = 4/28 = 1/7; ladder s_{k−1} =
  a·s_k[k(ν+1)−l]/[(ν+1)(k−l−1)], k=2 numerator 2·4−8 = 0 ⟹ unique
  s = t²(t−a)⁶, c̃ = −a(ρ−1)s₀ = 0 ⟹ ⊖ = 0; root-law q-mult 7, η-mult
  3 at 0, MP6(c). Criterion sweep [1..7]×[1..12]: ct = 0 ⟺ (ν+1) | l.
  Machine: /tmp/zch238_verify.py (5 gauges) + engine check_ZCH(3,8).
  **ENGINE-VERIFIED, review-pending.**
- **ZCH(2,6,7)M7@w6** (T1). l = ν+1 = 7 ⟹ ρ = 7/49 = 1/7; pivots
  6(k−8)/7 ≠ 0 (full rank), k=1 numerator 6(k−1)/7 = 0 ⟹ s₀ = 0 ⟹
  unique s = t(t−a)⁶, c̃ = 0 ⟹ ⊖ = 0; quadruple-inadmissible (q-mult 7,
  η-mult 7, MP6(c)). Degeneracy criterion exact: s₀ = 0 forced ⟺
  ρ(ν+1) = 1 ⟺ l = ν+1. Machine: /tmp/zch267_verify.py (5 gauges) +
  engine check_ZCH(6,7). **ENGINE-VERIFIED, review-pending.**
- **I(3,1,3)M3@w2** (T1). ν=1 shape p monic cubic (3 simple orbits),
  q = p·s, deg s = 3, ρ = 1/2; Prop 8.1(iv) ⟹ W(s,p) = p·s′ − p′·s =
  2c̃ constant. Differentiate: p·s″ = p″·s; complete branch analysis —
  s₂ = p₂ ⟹ s = p ⟹ W = 0 ⟹ c̃ = 0; s₂ ≠ p₂ ⟹ shared monic quadratic
  g, W = ((p₂−s₂)/3)g² nonconstant (deg 4), no solution + root-law
  violation. Kernel 0 for EVERY cubic (348-cubic exact RREF sweep incl.
  degenerates); residues −c′p″(aᵢ)/3p′(aᵢ)³ cannot all vanish (p″
  linear). Unique solution s = p with ⊖ = 0 — contradiction. Machine:
  /tmp/i313_bash.py (gates PASS). **ENGINE-VERIFIED, review-pending.**
- **I(3,1,6)M3@w2** (T1). r | l (l/r = 2): p squarefree cubic, q = p·S,
  deg S = 6, ρ = 1/3 ⟹ (S/p²)′ = 3c̃/p³. Residues of p⁻³:
  N(u,v)/(u⁵v⁵), N = 6u²+9uv+6v²; gauge numerators N₁,N₂,N₃ with
  pairwise Sylvester resultants all = 800 ≠ 0 over ℤ ⟹ no complex
  configuration zeroes two ⟹ c̃ = 0. Residual: ker = ⟨p²⟩ (rank 6 on 25
  samples) ⟹ q = p³ = p^{1/ρ}, triply inadmissible; η-subvariant
  S(0) = 0 forces p(0) = 0, inadmissible. Machine: /tmp/bash_i316.py
  (16/16 PASS; r=2 sanity reproduces MP9/L1b). **ENGINE-VERIFIED,
  review-pending.**
- **I(4,1,2)M2@w2** (T1). l | r (r/l = 2): 4p·σ′ − 2p′·σ = c′ with σ
  monic deg 2; triangular ladder p₃ = 2s₁, p₂ = s₁²+2s₀, p₁ = 2s₁s₀,
  p₀ = s₀² ⟹ p = σ² exactly and c′ = 4s₀²s₁ − 4s₁s₀² = 0 identically —
  the polynomial homogeneous branch (family-I twin of the IIa (ν+1)|r
  kill). ⊖ = 0; p = σ² contra 4 distinct simple directions; root-law
  mult 3; η-subvariant p = t²(t−b)² subsumed at s₀ = 0. Machine:
  /tmp/bash_i412.py (19×19 exact grid, unique full-rank solution
  everywhere; both gates PASS). **ENGINE-VERIFIED, review-pending.**
- **I(4,1,4)M4@w2** (T1). r = l: p·s′ − p′·s = 2c; p·s″ = p″·s ladder
  with constant pivots (6,10,12,12) forces s = p for every monic
  quartic (symbolic over ℚ[p₀..p₃,e₀..e₃] + 825 exact solves, rank 5,
  no escape locus) ⟹ 2c = W(p,p) = 0 ⟹ ⊖ = 0; q = p² breaks the root
  law at all 4 roots. Residue corroboration: res p⁻² = −p″(aᵢ)/p′(aᵢ)³,
  ≥2 of 4 nonzero (deg p″ = 2). Machine: /tmp/i414_bash.py (exit 0,
  gates PASS). **ENGINE-VERIFIED, review-pending.**
- **I(4,1,8)M4@w2** (T1). r | l (l = 2r, n = 3): p·S′ − 2p′·S = c,
  (S/p²)′ = c/p³. c ≠ 0 branch: all residues Rᵢ = (3p″(aᵢ)² −
  p′(aᵢ)p‴(aᵢ))/2p′(aᵢ)⁵ must vanish ⟹ p | H, H := 3p″² − p′p‴ = 336p
  exactly ⟹ b = 3a²/8, c = a³/16, d = a⁴/256, i.e. p = (t+a/4)⁴ —
  quadruple root, triply inadmissible. c = 0 branch: ker = span{p²} ⟹
  q = Cp³ = Cp^{1/ρ} ⟹ ⊖ = 0 + root-law q-mult 3. Both e0-subvariants
  are q = p·S. Machine: /tmp/i418_bash.py (4 gates + 8 checks PASS).
  **ENGINE-VERIFIED, review-pending.**

## 3. The round-2 survivor — what it needs next

**ZCH(2,3,2)M2@w6 κ̄10, 2 panels (m=2 td12; m=4 td12).** The unique
ZCH/family-I escape of both divisibility criteria. Bottoms out in a
rigid one-scale residue-A-type template: s = t² − (3/2)at + (3/8)a²,
roots (3±√3)a/4 (simple, irrational ratio, distinct ν-orbits),
c̃ = (9/40)a³ ≠ 0, matching the SHEET6-L1 §4b closed form. T1b: case-II
edges realizable at every w=6 frame in both panels (the td=6 ZCH
non-joinability kill does not transfer). T2: sound composed residue of
13 IV-survivor classes at λ = 4,5,6,8 (0 open, 0 frontier, cheapest
λ = 4 vs cap ≥ 9). T3: E-mechanism count laws close with equality
(γ = 7/6, k_G = 38, deg 39 = k_G+1, M_G = 2, a-free s1-transport).
Needs, exactly like the IIa survivors: the L1 §7.2 global layer /
Puiseux substitution transport, or a per-panel TEMPLATE-genome run —
nothing in the printed statement list closes it.

## 4. Per-panel census after rounds 1+2

    panel      pre-bash | killed R1 | killed R2 | template-survivors
    m=2,td= 6      1    |     0     |     0     |   1 (residue-A)
    m=2,td= 8      1    |     0     |     0     |   1 (residue-A)
    m=2,td= 9      4    |     1     |     2     |   1 (residue-A)
    m=3,td= 9      8    |     3     |     4     |   1 (residue-A)
    m=2,td=10      2    |     0     |     0     |   2
    m=2,td=12     13    |     1     |     7     |   5
    m=3,td=12     10    |     2     |     4     |   4
    m=4,td=12     21    |     3     |    12     |   6
    m=2,td=14      7    |     1     |     2     |   4
    m=3,td=14      8    |     2     |     4     |   2
    TOTAL         75    |    13     |    35     |  27

Unbashed column: **0 everywhere** — the book is fully adjudicated.

## 5. Per-td exclusion status (combined ledger)

Single-pole ground truth unchanged (SHEET6-TDUNIFORM promoted: prime
theorem at prime td; composite residual 4/16/16/23/71/48 at
td = 6/8/9/10/12/14). Multi-pole ground is the book after both rounds:

| td | single-pole residual (TDU) | multi-pole book after R1+R2 | FULLY excluded? |
|---|---|---|---|
| 6 | 4 classes | 1 cell: residue-A only | NO |
| 7 | 0 (prime theorem) | empty | **YES** |
| 8 | 16 classes | 1 cell: residue-A only | NO |
| 9 | 16 classes | 2 cells: residue-A ×2 (was 8 — all 6 unbashed cells killed) | NO |
| 10 | 23 classes | 2 cells: residue-A + IIa(2,5,1)@w3 | NO |
| 11 | 0 (prime) | empty | **YES** |
| 12 | 71 classes | 15 cells (was 38): 14 IIa-template + ZCH(2,3,2)@w6 ×2 | NO |
| 13 | 0 (prime) | empty | **YES** |
| 14 | 48 classes | 6 cells (was 12): all template | NO |

## 6. FINAL COMBINED CENSUS (rounds 1+2)

The two-round campaign has now bashed all 22 classes / 75 cell
instances of the td ≤ 14 multi-pole book. **DEAD: 15 classes outright
plus one panel of a 16th — 48 of 75 instances** (round 1: IIa(3,2,1)M3@w2
×4, IIa(4,3,1)M4@w2 ×1, IIa(3,5,1)M3@w2 at m=3,td9 ×1, ZCH(2,2,3)M3@w4
×7; round 2: ZCH(2,2,6)M3@w4 ×7, ZCH(2,4,5)M5@w4 ×7, ZCH@w6
(2,2,3)κ̄9/(2,2,9)/(2,3,4)/(2,3,8)/(2,6,7) ×2 each, I(3,1,3) ×4,
I(3,1,6) ×4, I(4,1,2)/(4,1,4)/(4,1,8) ×1 each). Every kill in both
rounds was T1 or T2, and all 12 round-2 kills are the single T1 pattern
(a): divisibility-forced ⊖ = 0 homogeneous-branch degeneracy —
(ν+1) | l for family Z, l/r ∈ ℤ or r/l ∈ ℤ for family I — each
frame-free and multiply-overdetermined. Confirmation ledger for the 48:
19 instances review-confirmed with 2 adversarial votes each (R1: 6; R2:
ZCH(2,2,6) 7, ZCH(2,2,3)@w6 2, ZCH(2,2,9) 2, ZCH(2,3,4) 2), 7 with one
vote banked (ZCH(2,4,5)), 22 engine-verified pending review (R1
ZCH(2,2,3)@w4 7; R2: ZCH(2,3,8) 2, ZCH(2,6,7) 2, I-family 11).
**SURVIVING: 27 instances in 7 rigid one-scale coefficient templates**,
every one now bashed through the full applicable arsenal:

1. residue-A IIa(2,3,1)M2@w2 — 10 panels (every non-empty panel);
2. IIa(2,3,1)M2@w4 — 4 panels;
3. IIa(2,7,1)M2@w4 — 4 panels;
4. IIa(2,5,1)M2@w3 — 3 panels;
5. IIa(3,5,1)M3@w2 — 3 remaining panels (m=3/m=4 td12, m=3 td14);
6. IIa(4,7,1)M4@w2 — 1 panel (m=4 td12; 2 OPEN μ=3 tier-2 nodes);
7. ZCH(2,3,2)M2@w6 — 2 panels (m=2/m=4 td12).

Per-td: **fully excluded td = 7, 11, 13 — unchanged and structurally
unchangeable by this campaign**, since residue-A survives in every
non-empty panel and composite td are independently blocked by the TDU
single-pole residual. Multi-pole-side reductions: td = 6, 8, 9 are now
each reduced to residue-A alone (td=9 was 8 cells before round 2);
td = 10 to two IIa templates; td = 12 from 38 to 15 cells; td = 14 from
12 to 6. **The definitive list of what stands between the campaign and
td ≤ 14 multi-pole exclusion is exactly the 7 templates above (27
instances), plus the review/perimeter debt**: (i) closure of the
residue-A template (a1/a2 = 2±√3, b = (2/3)σ, suffix B = (3/2)A) via
the L1 §7.2 global layer or per-panel E-mechanism ladders — this single
object blocks every td; (ii) the flagged TEMPLATE-scale lever for
IIa(3,5,1) (W-residual deg 2 vs demanded ≤ 1 — would kill 3 instances
at once, UNRUN); (iii) resolution of IIa(4,7,1)'s 2 OPEN parametric
suffix nodes; (iv) Puiseux/transport tiers for the @w4/@w3 IIa
templates and the fresh ZCH(2,3,2) template — all beyond the printed
statement list; (v) banking the outstanding adversarial votes on 29
dead instances (1 more for ZCH(2,4,5); full review for R1 ZCH(2,2,3)@w4
— reproduced cell-for-cell as a mandatory gate in every round-2 harness
but still without votes of its own — and the 6 zero-vote round-2
records); (vi) the inherited superset-soundness perimeter
(P-realizability untracked, conservative join contexts, μ_e ≥ 2
quarantine, off-axis entries outside the M=1 lemma), relative to which
all exclusion claims are stated. Live book instances: 75 → 62 (round 1)
→ **27, all template, none unbashed.**

## 7. Artifacts

Round-2 session artifacts (outside repo, exact int/Fraction arithmetic,
all gate-checked): /tmp/zch226_verify.py, /tmp/zch245_verify.py,
/tmp/zch223_w6_verify.py (+ review scripts /tmp/zch223_w6_review.py,
/tmp/adv2_zch223_w6_review.py), /tmp/zch229_verify.py,
/tmp/zch232/{tier1_ode, tier1_edges, tier2_suffix, tier3_emech,
tier3b, final_consolidate}.py, /tmp/zch234_verify.py,
/tmp/zch238_verify.py, /tmp/zch267_verify.py, /tmp/i313_bash.py,
/tmp/bash_i316.py, /tmp/bash_i412.py, /tmp/i414_bash.py,
/tmp/i418_bash.py. Repo grounds (read-only):
/Users/dc/code/math/jc72108/BOOK-BASH.md, BOOK-ENUM.md, SHEET6-L1.md,
SHEET6-MULTIPOLE.md, SHEET6-DEPTH.md, SHEET6-TEMPLATE.md,
SHEET6-TDUNIFORM.md, SIGRAY-AUDIT.md, cases/{book_enum, l1_ode_check,
hiii_compose, h3_check, sheet6_campaign, depth_closure_check,
template_lift}.py, systems/book/book_m{2,3,4}_td{6..14}.json,
refs/sigray_full.pdf.