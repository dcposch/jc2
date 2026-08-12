Reading additional input from stdin...
OpenAI Codex v0.147.0
--------
workdir: /Users/dc/code/math/jc72108
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: ultra
reasoning summaries: none
session id: 019ff78d-a954-7d73-b988-762c511da444
--------
user
You are a senior mathematician evaluating an AI-driven research campaign on the plane Jacobian Conjecture (JC2). Read, in this order: README.md, BOOK-BASH-R2.md, SHEET6-MULTIPOLE.md (theorem MP), SHEET6-DEPTH.md, MATHIEU.md (theorem A), SHEET6-TEMPLATE.md sections 0-1, notes.md (last 150 lines). Then deliver, tersely: (1) STRESS TEST — the three weakest load-bearing points of the whole program (be specific: which claim, why fragile); (2) NEW AVENUES — five concrete proof or disproof ideas NOT already in the campaign record (check RECON.md and notes.md before proposing, to avoid duplicates); rank by expected decisiveness per unit effort; for each give the first concrete computation or lemma to try; (3) VERDICT — your honest probability assessment that JC2 is true, and where this program is most likely to break through or stall. Do not modify any files.
codex
I’ll audit the specified documents in exactly that order, then cross-check both `RECON.md` and the full campaign notes before proposing anything novel. I’ll keep the review read-only and separate structural weaknesses from merely unfinished steps.
exec
/bin/zsh -lc "wc -l README.md BOOK-BASH-R2.md SHEET6-MULTIPOLE.md SHEET6-DEPTH.md MATHIEU.md SHEET6-TEMPLATE.md notes.md RECON.md && sed -n '1,240p' README.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
      51 README.md
     305 BOOK-BASH-R2.md
     176 SHEET6-MULTIPOLE.md
     432 SHEET6-DEPTH.md
     484 MATHIEU.md
     403 SHEET6-TEMPLATE.md
     338 notes.md
     180 RECON.md
    2369 total
# jc72108

Started as: settle the (72,108) case — the last open degree pair below 125 for
the plane Jacobian Conjecture (GGV–Horruitiner, arXiv:2204.14178, Prop 4.3).
Grown into: a campaign on the remaining structural avenues (sheet-6 exclusion,
DC(2), residue theory, deg ≤ 150 frontier farm).

## Progress

### (72,108) — SETTLED (empty; no counterexample with these polygons)
- [x] Pipeline validated on solved GGV families (14/14 formulation×char combos)
- [x] Subcase (2): EMPTY over ℚ + 3 primes, all strata, audited
- [x] Subcase (1): settled via verified external artifacts (Helali, Suzuki) +
      our audit; own-leaf replication retired (novelty rule)
- [x] Cross-check vs Helali & Suzuki artifacts (three-way agreement)
- [x] Paper 1 drafted + compiled (Lean-checked example); awaiting review
- [ ] Certificates: cCa2/cCa6 char-0 lifts still running (ultramem)
- [ ] Pre-publication riders: reduce4 G4 cross-check

### Vertex-gap program
- [x] Theorem grid (2,2),(2,3),(2,4) + k≥3 impossibility (reviewed)
- [x] conj:R PROVED (Theorem A via Duistermaat-van der Kallen mechanism, adversarially
      reviewed): strip obstruction theory now UNIFORM in (k,d2), char 0
- [x] R functional = Grothendieck residue at toric boundary (3 interpretations
      verified; uniform extra formula; conj:R reduced to rigidity half)

### Sheet-6 (td = 6) exclusion — the active endgame
- [x] Campaign engine: pilot + Λ≤7 table + propagation bash (reviewed)
- [x] Sigray thesis: td≥6 proof shown incomplete as printed; errata E1–E10
- [x] ψ-budget (G2 closed), E5/N1 extraction, AF2 derived, entry-M pin proved
- [x] td ≤ 5: CLOSED (0 survivors). Single-pole td = 6: 4 r9/M2 classes
- [x] Two-pole (3,3): funneled to rigid template (a₁/a₂ = 2+√3); R6
      print-campaign closed (6/9 dead); 4 branches to coefficient level
- [ ] R1 decisive runs: minimal-branch mod-p screen RUNNING (ultramem);
      (1,2) core queued; chain cores building
- [x] Ops: msolve parenthesis hazard found + 401-file audit (all prior
      verdicts unaffected); emission rules hardened

### DC(2)
- [x] Degree-2 + degree-3 slices (reviewed; slice-scheme divergence at D=3;
      consistent with HOLDS at D ≤ 3); degree-4 sized, parked

### Frontier farm (deg ≤ 150)
- [x] §4 automation + FLINT port + sweep: 34 families, 62 systems emitted
      (7 families honestly out of reduce4 scope)
- [ ] Verdicts: 2 boxes grinding (EMPTYs banking; big char-0 cores need a
      higher-memory retry tier)

Docs: `CAMPAIGN.md` · `AUDIT.md` · `LEMMA.md` · `SURPLUS.md` · `RESIDUE.md` ·
`SHEET6-CAMPAIGN.md` (+ SHEET6-* satellites) · `DC2-PROGRAM.md` · `RECON.md` ·
`notes.md`

exec
/bin/zsh -lc "sed -n '1,360p' BOOK-BASH-R2.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# BOOK-BASH-R2.md — round 2: the 13 remaining classes (37 instances), book fully adjudicated

Status: SYNTHESIS of the round-2 per-class bash campaign + full adversarial
review pass, 2026-08-12. Ground: BOOK-BASH.md (round 1: arsenal,
kill-record style, proven kill patterns), BOOK-ENUM.md +
systems/book/*.json (cell data, cross-checked per class, no mismatches),
engines cases/{l1_ode_check, hiii_compose, h3_check, sheet6_campaign,
depth_closure_check, book_enum}.py (read-only), thesis
refs/sigray_full.pdf (Prop 8.1(iv) re-read on-page, p.39–41), forced
readings per SIGRAY-AUDIT.md. Arsenal applied in order per class: **T1**
pattern algebra (SHEET6-L1 method, Prop 8.1(iv)
δ·p·q′ − (1−u)·p′·q = ⊖·p on the cell's (p,q) shapes), **T2** suffix
chase (hiii_compose composed kill set + ψ-budget vs St 9.4), **T3**
coefficient lift (SHEET6-TEMPLATE E-mechanism), **T4** w-arithmetic —
with stop-at-first-kill. Every harness was gated on promoted round-1
records (residue-A check_A_l1(3) and/or ZCH(2,2,3) check_ZCH(2,3));
gate PASS in every run. All arithmetic exact (python fractions).

## 0. Verdict

**13 of 13 remaining classes bashed (37 of 37 instances) — the 22-class
book is now fully adjudicated at 75/75 instances. 12 classes KILLED
outright (35 instances DEAD — every kill record review-confirmed with 2
adversarial votes, NOT REFUTED / no escape found); 1 class SURVIVES
(ZCH(2,3,2)M2@w6, 2 instances, survival record review-audited),
bottoming out in a rigid one-scale residue-A-type template.** Every
round-2 kill is T1, known kill pattern (a) — a divisibility-forced
⊖ = 0 degeneracy of Prop 8.1(iv) — and the campaign closed both
criteria in closed form:

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
| ZCH(2,4,5)M5@w4 | κ̄5, (5,1,1/5) | 7: m=2 td9,12,14; m=3 td9,12,14; m=4 td12 | **DEAD** | T1, ρ=1/5: k=0 numerator (ν+1)(k+1)−l = 5−5 = 0 ((ν+1)\|l ⟺ M=ν+1) ⟹ unique s = t(t−a)⁴, c̃=0 ⟹ ⊖=0; triple-inadmissible (root law, η law, MP6(c)) | **YES** — kill_confirmed, 2 votes (KILL CONFIRMED ×2, incl. independent raw-ODE η-variable route; no escape found) |
| ZCH(2,2,3)M3@w6 | κ̄9, (9,3,1) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, ρ=1/3: unique s = t(t−a)², c̃=0, q = p³ = p^{1/ρ} exactly the homogeneous branch; ⊖=0 + root law (q-mult 3) + η law (η-mult 3). Banks round-1 rider 3 as its own record | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, fresh-route re-derivations: symbolic over ℚ(a) + η-variable) |
| ZCH(2,2,9)M3@w6 | κ̄7, (7,1,1/3) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, ρ=1/7: numerator (2−k) = 0 at k=2 (3\|9) ⟹ unique s = t³(t−a)⁶, c̃=0 ⟹ ⊖=0; root-law q-mult 7, η-mult 4, MP6(c) | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, no escape found, citations checked on-page) |
| ZCH(2,3,2)M2@w6 | κ̄10, (10,4,1) | 2: m=2 td12; m=4 td12 | **SURVIVES** | T1/T1b/T2/T3 exhausted: full-rank ladder, c̃ = (9/40)a³ ≠ 0, admissible s with roots (3±√3)a/4; T1b (zch3_edges/Prop 9.3): ratio-partner realizable in both panels, td=6 non-joinability does NOT transfer; T2: 13 IV-survivor classes at λ=4..8, 0 open, 0 frontier; T3: all count laws close with equality (deg 39 = k_G+1, M_G = 2, a-free s1-transport) | n/a (survival; superset-sound; survives_review banked) |
| ZCH(2,3,4)M4@w6 | κ̄8, (8,2,1/2) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, l = ν+1 ⟹ ρ = 1/(ν+1) = 1/4, B₀ = 0 ⟹ unique s = t(t−a)³, c̃=0 ⟹ ⊖=0; triple-inadmissible (0-root, triple root q-mult 4, MP6(c)) | **YES** — kill_confirmed, 2 votes (NOT REFUTED / CONFIRMED, incl. full independent re-implementation) |
| ZCH(2,3,8)M4@w6 | κ̄7, (7,1,1/4) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, ρ=1/7: k=2 numerator 2·4−8 = 0 (4\|8) ⟹ unique s = t²(t−a)⁶, c̃=0 ⟹ ⊖=0; criterion sweep (ν,l) ∈ [1..7]×[1..12]: ct=0 ⟺ (ν+1)\|l | **YES** — kill_confirmed, 2 votes (NOT REFUTED / KILL CONFIRMED, no escape found) |
| ZCH(2,6,7)M7@w6 | κ̄7, (7,1,1/7) | 2: m=2 td12; m=4 td12 | **DEAD** | T1, l = ν+1 = 7 ⟹ ρ=1/7, k=1 numerator zero ⟹ unique s = t(t−a)⁶, c̃=0 ⟹ ⊖=0; quadruple-inadmissible (root-law q-mult 7, η-mult 7, MP6(c)) | **YES** — kill_confirmed, 2 votes (VERIFIED, kill stands / NOT REFUTED, no escape found) |
| I(3,1,3)M3@w2 | κ̄4, (4,2,2/3) | 4: m=3 td9,12,14; m=4 td12 | **DEAD** | T1, r = l (l/r = 1): constant-Wronskian rigidity W(s,p) = 2c̃; p·s″ = p″·s forces s = p for every cubic (kernel 0, residue obstruction −c′p″(aᵢ)/3p′(aᵢ)³ closes all branches) ⟹ W = 0 ⟹ ⊖=0; s = p triply inadmissible | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, incl. fresh symbolic W(s,p) re-derivation over arbitrary cubics) |
| I(3,1,6)M3@w2 | κ̄3, (3,1,1/3) | 4: m=3 td9,12,14; m=4 td12 | **DEAD** | T1, r \| l (l = 2r): (S/p²)′ = 3c̃/p³, Laurent residues N = 6u²+9uv+6v², pairwise resultants 800 ≠ 0 ⟹ ≥2 residues nonzero always ⟹ c̃=0; residual S = p², q = p³ triply inadmissible; both e0-subvariants closed (l ≤ 4 cap flag retired at l=6) | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, incl. full 19-file panel-scope sweep of systems/book/*.json) |
| I(4,1,2)M2@w2 | κ̄6, (6,4,1) | 1: m=4 td12 | **DEAD** | T1, l \| r (r/l = 2, reversed divisibility): constant-pivot ladder (2,4,6,8) forces p = σ² for EVERY monic σ, c′ = 0 ⟹ ⊖=0; p non-squarefree contra r = 4 distinct arriving directions (MP6 D6d(a)); root-law mult 3; η-subvariant p = t²(t−b)² subsumed | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, incl. full independent symbolic re-derivation stronger than the grid check) |
| I(4,1,4)M4@w2 | κ̄4, (4,2,1/2) | 1: m=4 td12 | **DEAD** | T1, r = l: Wronskian ladder, pivots (6,10,12,12) force s = p unconditionally ⟹ q = p², 2c = W(p,p) = 0 ⟹ ⊖=0; root-law q-mult 2 at all four roots; residue corroboration (p″ deg 2 < 4 distinct roots) | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, fresh independent machine /tmp/i414_review.py + on-page Prop 8.1(iv) check) |
| I(4,1,8)M4@w2 | κ̄3, (3,1,1/4) | 1: m=4 td12 | **DEAD** | T1, r \| l (l = 2r, n = 3): c ≠ 0 forces all residues of p⁻³ zero ⟹ H = 336p exactly ⟹ p = (t+a/4)⁴, triply inadmissible; c = 0 branch: kernel S = Cp², q = Cp³ ⟹ ⊖=0 + root-law q-mult 3. Both e0-subvariants covered | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, incl. independent re-implementation of every load-bearing step + 18-JSON sole-panel scan) |

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
  (6 gauges, rank 5) + engine check_ZCH(4,5). Gates PASS.
  **kill_confirmed, 2 adversarial votes** (vote 1 via the raw printed
  ODE in the η variable, no reduction; vote 2 banked the formerly
  outstanding second review: KILL CONFIRMED, NO ESCAPE FOUND).
- **ZCH(2,2,3)M3@w6 κ̄9** (T1). Same (ν,l) = (2,3) solve as the round-1
  @w4 kill (ρ = 1/3, s = t(t−a)², c̃ = 0), banked as its own record for
  the w=6/κ̄9 frame: q = η³(η²−a)³ = p³ = p^{1/ρ} identically — the
  homogeneous branch, with ⊖ = 0 + root-law + η-law violations; child
  cross-check ρ_child/(D/i) = 1/3 in both frames. Machine:
  /tmp/zch223_w6_verify.py (5 gauges, rank 3/3) + engine agreement.
  **kill_confirmed, 2 adversarial votes** (fresh-route re-derivations:
  symbolic over ℚ(a), stronger than the numeric gauges, and a direct
  η-variable reduction).
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
  **kill_confirmed, 2 adversarial votes.**
- **ZCH(2,6,7)M7@w6** (T1). l = ν+1 = 7 ⟹ ρ = 7/49 = 1/7; pivots
  6(k−8)/7 ≠ 0 (full rank), k=1 numerator 6(k−1)/7 = 0 ⟹ s₀ = 0 ⟹
  unique s = t(t−a)⁶, c̃ = 0 ⟹ ⊖ = 0; quadruple-inadmissible (q-mult 7,
  η-mult 7, MP6(c)). Degeneracy criterion exact: s₀ = 0 forced ⟺
  ρ(ν+1) = 1 ⟺ l = ν+1. Machine: /tmp/zch267_verify.py (5 gauges) +
  engine check_ZCH(6,7). **kill_confirmed, 2 adversarial votes.**
- **I(3,1,3)M3@w2** (T1). ν=1 shape p monic cubic (3 simple orbits),
  q = p·s, deg s = 3, ρ = 1/2; Prop 8.1(iv) ⟹ W(s,p) = p·s′ − p′·s =
  2c̃ constant. Differentiate: p·s″ = p″·s; complete branch analysis —
  s₂ = p₂ ⟹ s = p ⟹ W = 0 ⟹ c̃ = 0; s₂ ≠ p₂ ⟹ shared monic quadratic
  g, W = ((p₂−s₂)/3)g² nonconstant (deg 4), no solution + root-law
  violation. Kernel 0 for EVERY cubic (348-cubic exact RREF sweep incl.
  degenerates); residues −c′p″(aᵢ)/3p′(aᵢ)³ cannot all vanish (p″
  linear). Unique solution s = p with ⊖ = 0 — contradiction. Machine:
  /tmp/i313_bash.py (gates PASS). **kill_confirmed, 2 adversarial
  votes** (incl. fresh symbolic re-derivation with p an arbitrary
  cubic, not reusing the artifact).
- **I(3,1,6)M3@w2** (T1). r | l (l/r = 2): p squarefree cubic, q = p·S,
  deg S = 6, ρ = 1/3 ⟹ (S/p²)′ = 3c̃/p³. Residues of p⁻³:
  N(u,v)/(u⁵v⁵), N = 6u²+9uv+6v²; gauge numerators N₁,N₂,N₃ with
  pairwise Sylvester resultants all = 800 ≠ 0 over ℤ ⟹ no complex
  configuration zeroes two ⟹ c̃ = 0. Residual: ker = ⟨p²⟩ (rank 6 on 25
  samples) ⟹ q = p³ = p^{1/ρ}, triply inadmissible; η-subvariant
  S(0) = 0 forces p(0) = 0, inadmissible. Machine: /tmp/bash_i316.py
  (16/16 PASS; r=2 sanity reproduces MP9/L1b). **kill_confirmed, 2
  adversarial votes** (incl. full 19-file panel-scope sweep: the cell
  exists in exactly the 4 claimed panels and nowhere else).
- **I(4,1,2)M2@w2** (T1). l | r (r/l = 2): 4p·σ′ − 2p′·σ = c′ with σ
  monic deg 2; triangular ladder p₃ = 2s₁, p₂ = s₁²+2s₀, p₁ = 2s₁s₀,
  p₀ = s₀² ⟹ p = σ² exactly and c′ = 4s₀²s₁ − 4s₁s₀² = 0 identically —
  the polynomial homogeneous branch (family-I twin of the IIa (ν+1)|r
  kill). ⊖ = 0; p = σ² contra 4 distinct simple directions; root-law
  mult 3; η-subvariant p = t²(t−b)² subsumed at s₀ = 0. Machine:
  /tmp/bash_i412.py (19×19 exact grid, unique full-rank solution
  everywhere; both gates PASS). **kill_confirmed, 2 adversarial votes**
  (incl. full independent symbolic re-derivation, strictly stronger
  than the grid check).
- **I(4,1,4)M4@w2** (T1). r = l: p·s′ − p′·s = 2c; p·s″ = p″·s ladder
  with constant pivots (6,10,12,12) forces s = p for every monic
  quartic (symbolic over ℚ[p₀..p₃,e₀..e₃] + 825 exact solves, rank 5,
  no escape locus) ⟹ 2c = W(p,p) = 0 ⟹ ⊖ = 0; q = p² breaks the root
  law at all 4 roots. Residue corroboration: res p⁻² = −p″(aᵢ)/p′(aᵢ)³,
  ≥2 of 4 nonzero (deg p″ = 2). Machine: /tmp/i414_bash.py (exit 0,
  gates PASS). **kill_confirmed, 2 adversarial votes** (incl. fresh
  independent machine /tmp/i414_review.py, fresh seed, 16/16 PASS, and
  the on-page Prop 8.1(iv) print check).
- **I(4,1,8)M4@w2** (T1). r | l (l = 2r, n = 3): p·S′ − 2p′·S = c,
  (S/p²)′ = c/p³. c ≠ 0 branch: all residues Rᵢ = (3p″(aᵢ)² −
  p′(aᵢ)p‴(aᵢ))/2p′(aᵢ)⁵ must vanish ⟹ p | H, H := 3p″² − p′p‴ = 336p
  exactly ⟹ b = 3a²/8, c = a³/16, d = a⁴/256, i.e. p = (t+a/4)⁴ —
  quadruple root, triply inadmissible. c = 0 branch: ker = span{p²} ⟹
  q = Cp³ = Cp^{1/ρ} ⟹ ⊖ = 0 + root-law q-mult 3. Both e0-subvariants
  are q = p·S. Machine: /tmp/i418_bash.py (4 gates + 8 checks PASS).
  **kill_confirmed, 2 adversarial votes** (incl. independent
  re-implementation of every load-bearing step + 18-JSON scan
  confirming the sole panel).

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
Survival is review-audited (survives_review banked; superset-sound).
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
| 12 | 71 classes | 15 cells (was 38): 13 IIa-template + ZCH(2,3,2)@w6 ×2 | NO |
| 13 | 0 (prime) | empty | **YES** |
| 14 | 48 classes | 6 cells (was 12): all IIa-template | NO |

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
**41 instances review-confirmed with 2 adversarial votes each** (R1: 6 —
IIa(3,2,1) ×4, IIa(4,3,1) ×1, IIa(3,5,1)@td9 ×1; R2: all 35), and **7
engine-verified pending formal per-record review** (R1 ZCH(2,2,3)M3@w4
×7 — its identical (ν,l) = (2,3) solve is now twice-refereed via the
round-2 @w6 record and was reproduced cell-for-cell as a mandatory gate
in every round-2 harness, but the @w4 record itself still carries no
votes of its own). **SURVIVING: 27 instances in 7 rigid one-scale
coefficient templates**, every one now bashed through the full
applicable arsenal:

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
instances), plus the residual review/perimeter debt**: (i) closure of
the residue-A template (a1/a2 = 2±√3, b = (2/3)σ, suffix B = (3/2)A)
via the L1 §7.2 global layer or per-panel E-mechanism ladders — this
single object blocks every td; (ii) the flagged TEMPLATE-scale lever
for IIa(3,5,1) (W-residual deg 2 vs demanded ≤ 1 — would kill 3
instances at once, UNRUN); (iii) resolution of IIa(4,7,1)'s 2 OPEN
parametric suffix nodes; (iv) Puiseux/transport tiers for the @w4/@w3
IIa templates and the fresh ZCH(2,3,2) template — all beyond the
printed statement list; (v) banking formal per-record votes on the 7
R1 ZCH(2,2,3)M3@w4 instances — after the round-2 review pass, the only
remaining review debt in the entire book; (vi) the inherited
superset-soundness perimeter (P-realizability untracked, conservative
join contexts, μ_e ≥ 2 quarantine, off-axis entries outside the M=1
lemma), relative to which all exclusion claims are stated. Live book
instances: 75 → 62 (round 1) → **27, all template, none unbashed.**

## 7. Artifacts

Round-2 session artifacts (outside repo, exact int/Fraction arithmetic,
all gate-checked): /tmp/zch226_verify.py, /tmp/zch245_verify.py,
/tmp/zch223_w6_verify.py, /tmp/zch229_verify.py,
/tmp/zch232/{tier1_ode, tier1_edges, tier2_suffix, tier3_emech,
tier3b, final_consolidate}.py, /tmp/zch234_verify.py,
/tmp/zch238_verify.py, /tmp/zch267_verify.py, /tmp/i313_bash.py,
/tmp/bash_i316.py, /tmp/bash_i412.py, /tmp/i414_bash.py,
/tmp/i418_bash.py; adversarial-review re-implementations incl.
/tmp/review_zch223_w6.py and /tmp/i414_review.py (fresh code, fresh
seeds, no repo imports). Repo grounds (read-only):
/Users/dc/code/math/jc72108/BOOK-BASH.md, BOOK-ENUM.md, SHEET6-L1.md,
SHEET6-MULTIPOLE.md, SHEET6-DEPTH.md, SHEET6-TEMPLATE.md,
SHEET6-TDUNIFORM.md, SIGRAY-AUDIT.md, cases/{book_enum, l1_ode_check,
hiii_compose, h3_check, sheet6_campaign, depth_closure_check,
template_lift}.py, systems/book/book_m{2,3,4}_td{6..14}.json,
refs/sigray_full.pdf.
exec
/bin/zsh -lc "sed -n '1,240p' SHEET6-MULTIPOLE.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# SHEET6-MULTIPOLE.md — the m-pole analogue of Prop 8.4: the maximal printed-tier kill, its exact frontier, and the honest obstruction

**Status: PROMOTED WITH ONE DEMOTION (2026-08-12, SHEET6-MP-REVIEW.md):
MP0-MP8 + Theorem O stand as printed; MP9 stands on corrected ground
(l-independent kappa<nu kill); the "finite book" rider is DEMOTED to
finite-per-parent-frame — chain-frame depth is the sole unbounded axis,
needs a closure lemma (empirically depth-invariant at td=6). Jump-book
parameterization spec: review doc final section.
UPDATE 2026-08-12: the closure lemma is PROVED — SHEET6-DEPTH.md
(chain-depth closure: w = (κ̄−ρ)/ν conserved by l=0 steps, finitely many
resonant steps, menu factors through w); the finite-book rider is
RESTORED in corrected form (SHEET6-DEPTH.md §8).**
Original sYNTHESIS (judge document).** Composite of three panel angles: A1 (piecewise regularity / merge cascade, T0–T7 + obstruction O; NOT REFUTED, 3/3 adversarial votes), A2 (Euler/budget ledger, Theorem M (1)–(5) + Proposition B; NOT REFUTED, 3/3 votes — all theorem clauses explicitly listed as surviving), A3 (merge pattern algebra, Theorem MPM P1–P5 + OB; adversarial record truncated at synthesis time — its clauses cross-derived by A1/A2 are grafted at full tier, its unique clauses quarantined in §7).
**Ground truth:** refs/sigray_full.pdf (printed page = pdf page); page citations below re-read on-page by the panel this session. Prior promoted sheets: SHEET6-2POLE.md, SHEET6-L1.md, SHEET6-LROOT.md, SHEET6-TDUNIFORM.md, SHEET6-A3L1-REVIEW.md.

---

## 0. Verdict in one paragraph

The requested lemma splits along an exact seam, and both halves are now theorems. **Kill half:** for m ≥ 2 poles the printed Prop 8.4 machinery is restored *verbatim* on the shared suffix at and below the global meet G\* of the m characteristic sequences (M_F ≠ 1 there whenever G\* ≠ (0,y)), and is *supplemented* above G\* by a merge calculus: entry M-values are pinned per pole, M = 1 cascades are forced into rigid single-orbit shapes, every merge with an M = 1 arrival has fully pinned anatomy (k = 0, gcd menu), non-resonant merges (l = 0) can never break M = 1, and the entire M = 1 region is budget-transparent (Σλ = 0). **Obstruction half:** the verbatim multi-pole analogue of Prop 8.4 ("M_F ≠ 1 on pre-merge segments") is *FALSE* — M = 1 is FORCED pre-merge whenever the poles enter with b_i = 1 — and the surviving escape hatch is exactly the set of **resonant jump vertices** (merges with l ≥ 1 extra q-orbits and M = gcd-value ≥ 2), which provably pass every printed statement (machine-verified witness at td = 6, m = 2). Theorem MP below is therefore the *maximal* printed-tier statement: it reduces the multi-pole problem, for every (m, td), to a finite book of jump-vertex cells.

---

## 1. Setting and notation

(f,g) a normalized counterexample of type (α,β), 2 ≤ α < β, gcd(α,β) = 1 (Not 2.4/St 2.1, pp. 8–9; the type is global, Lemma 2.1 p. 8). T_{a,pole} = {P_1,…,P_m}, m ≥ 2.

- **C_i** = characteristic sequence of P_i: F_0 = P_i, F_{j+1} = F_j°, terminating at (0,y) (Prop 8.4's construction pp. 44–45; Prop 9.2 p. 50; ° per Not 3.3 p. 12, branch-independent and deterministic).
- **U** := ∪_i C_i, the **chain tree**, partially ordered with root (0,y) at the bottom, poles at the top.
- **r(G)** := #{H ∈ Va ∩ Ta& \ {(0,y)} : H° = G} (in-degree). **Merge vertex**: r(G) ≥ 2. **G\*** := max(∩_i C_i), the global meet (= "G_last"; nonempty since (0,y) ∈ every C_i). **G_i** = first (highest) merge vertex of C_i; **pre-merge segment of C_i** = vertices of C_i strictly above G_i.
- At a merge G with arriving edges from H_e = G + c_e: **μ_e** := mult(p_G^{red}, c_e), **r** = number of arriving bundles, **ν** = ν_G, **l** = number of extra simple ν-orbit families of q_G off the roots of p_G, **k** = number of non-chain roots of p_G.
- **Regularity** = Not 9.2 (p. 48); M_F = gcd(deg p_F, deg p_{h_0,F},…) per Not 8.1 (p. 39); reduced pattern (p,q), i = deg p_F / M\*_F, identity **(iv)**: δpq′ − (1−u)p′q = ⊖p (Prop 8.1, pp. 39–41); λ_F, Y(F), ψ per Not 9.3/St 9.3/9.4 (p. 49); budget Σλ ≤ td − 1 − ψ (St 9.4 (25)–(26), p. 49); Euler identity (22) (Prop 7.5, p. 38).

---

## 2. THEOREM MP (m-pole piecewise kill + merge calculus; hypothesis perimeter §4)

Let T_{a,pole} = {P_1,…,P_m}, m ≥ 2, any td.

**MP0 (chain-completeness).** Ta& ∩ Va \ {(0,x),(0,y)} = U \ {(0,y)}; U is a finite tree under F ↦ F° rooted at (0,y), and its leaves are exactly P_1,…,P_m (no pole has a chain predecessor).

**MP1 (merge counting and localization).** Σ_{G ∈ U, r(G) ≥ 2} (r(G) − 1) = m − 1; hence ≤ m − 1 merge vertices, each with r(G) ≤ m. Not 9.2-regularity fails **exactly** at merge vertices. No merge vertex lies strictly below G\*, and r(G\*) ≥ 2. Every suffix vertex (≤ G\*, ≠ G\*) has a *unique* Ta& ∩ Va predecessor.

**MP2 (restored kill, general m).** If G\* ≠ (0,y), then **M_F ≠ 1 for every F ∈ U with F ≤ G\*** (trunk and G\* itself). The printed Prop 8.4 proof (pp. 44–45) runs verbatim; the singleton hypothesis is needed only above the last merge.

**MP3 (exact escape set).** The vertices escaping MP2 are exactly {F ∈ U : F > G\*}: ALL strict ancestors of G\* — pre-merge segments, inter-merge segments, and merge vertices above G\*. (Not merely "the first vertex above each merge": the M = 1 contradiction is manufactured only at (0,y), so no per-segment rerun of Prop 8.4 exists.)

**MP4 (entry pin; td- and m-uniform).** At every pole, (deg p_{P_i}, deg p_{g,P_i}) = b_i(α,β) and **M_{P_i} = b_i = deg p_{P_i}/α**. Moreover b_i = 1 (hence M_{P_i} = 1) is FORCED when Λ(P_i) = β (β-minimal pole) and when Λ(P_i) is prime. In particular at the minimal m-pole degree td = mβ, ALL entries have M = 1.

**MP5 (forced M = 1 propagation — the naive analogue is false, maximally).** If M_F = 1 at a pre-merge vertex of C_i (e.g. F = P_i when b_i = 1), then every C_i-vertex from F down to the last pre-merge vertex has reduced pattern a single SIMPLE ν-orbit (dp = ν, dq = nν + 1, n ≥ 1), M = 1, λ = 0, no ray of T_a separating there; the chain arrives at G_i with μ_i = 1. M = 1 likewise propagates down every merge-free segment (Prop 8.3(i)) and through every M = 1-emitting merge.

**MP6 (merge anatomy).** No merge vertex is a pole vertex. At a merge G with at least one arriving μ_e = 1 (automatic for any M = 1-ancestry arrival, since μ_e | M_{H_e} by St 8.4):
 (a) **k = 0**: every root of p_G carries an incoming chain; no non-chain roots, searrow or northeast; the roots are exactly the r arriving directions;
 (b) **equal-quotient law**: deg p_{H_e} = i·μ_e with one common i ≥ 2 for all e;
 (c) **q-shape** [P2]: q = η·rad(p)·Π_{s=1}^{l}(η^ν − b_s^ν) for ν ≥ 2 (η-factor absorbed at ν = 1), all q-roots simple;
 (d) **gcd menu**: dq ≡ 1 (mod ν), hence **gcd(M_G, ν_G) = 1** always; with no 0-chain, **M_G = gcd(Σ_e μ_e, (r+l)ν + 1)**, so M_G | Σ_e μ_e ≤ Σ_e M_{H_e} (subadditivity). All-μ=1 families: **IIa**: (dp,dq) = (rν, (r+l)ν+1), M_G = gcd(rν,(r+l)ν+1) **= gcd(r, lν+1)**; **ZCH** (one chain at the 0-direction): (dp,dq) = ((r−1)ν+1, (r−1+l)ν+1), M_G = gcd((r−1)ν+1, l); **I** (ν = 1): (dp,dq) = (r, r+l), M_G = gcd(r, l). Corollary: outside ZCH, **M_G | r ≤ m**;
 (e) **λ_G = 0**: no northeast direction exists and the l extras carry no tree vertex.

**MP7 (no-resonance kill and jump existence).** l = 0 at an all-M=1 merge forces M_G = 1 (IIa: gcd(r,1)) or is impossible outright (ZCH and ν = 1: q = p forces p′ = const ≠ 0 in (iv), i.e. deg p = 1 — contradiction). Hence an all-M=1 merge either emits M = 1 (cascade continues) or is a **resonant jump**: l ≥ 1 and 2 ≤ M_G ≤ r(G) ≤ m in the non-0-chain families. Consequently: if all entries have M = 1 (forced at td = mβ, or all Λ_i prime, by MP4), then either G\* ≠ (0,y) and at least one resonant jump vertex with the full MP6 anatomy exists at or above G\*, or G\* = (0,y) and the **root merge** itself has the all-μ=1 anatomy at ν = 1 (St 9.2(ii)) with k = 0, l ≥ 1, M = gcd(r,l), and the top-cancellation pin **k_f = (r+l)·l_f**, ψ = r+l−1 in St 9.4.

**MP8 (budget transparency — the obstruction's mechanism).** On the pure M=1 forest {F ∈ U : M ≡ 1 at F and at every U-vertex above F} and at every all-M=1 merge vertex (including jumps): Y(F) = ∅ and λ_F = 0. Itemizing the Euler equality (22) (Prop 7.5, p. 38) for m poles: pole clusters, chain paths, M=1 segments, and μ=1-arrival merges all contribute identically zero rows. Hence **no refinement or re-partition of any printed budget** (St 9.4/9.5 (25)–(26) p. 49, Cor 7.1 p. 39, identity (22)) can charge M=1 pre-merge ancestry even one unit, for any m and any td. The only printed per-pole cost is Λ-mass: td = ΣΛ_i ≥ mβ ≥ 3m (Props 5.7/5.8), i.e. m ≤ td/3.

**MP9 (m = 2, b = (1,1) sharpening; td-uniform).** Both chains are M=1/λ=0 single-simple-orbit to the meet, μ = (1,1).
 (Interior meet, G\* ≠ (0,y)): M_{G\*} = gcd(2, lν+1) must equal 2 (else MP2 kills), forcing l odd ≥ 1 and ν odd. ν = 1 is impossible: l even contradicts (iv) by the exact log-obstruction (all even l — upgrades SHEET6-L1 §4 beyond engine caps), l odd gives M = 1, killed by MP2. Survivors: exactly **IIa(l odd, ν ≥ 3 odd), M = 2** or **ZCH with gcd(ν+1, l) ≥ 2** — at total pre-merge + merge spend 0. [Cap flag: the ν = 1 variant with an η-factor in q is excluded only for l ≤ 4.]
 (Root meet, G\* = (0,y)) [+H1 for the last clause]: l = 0 impossible (q = p gives 0 = ⊖p ≠ 0 in (iv)); l even impossible (same log-obstruction, ν = 1 by St 9.2(ii)); residual: l odd, locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2 ≠ 0, exact), with k_f = (2+l)·l_f, ψ = l+1, and l ≤ td − 2 (Σλ = 0 in St 9.4 (25)); Prop 9.3(d) with child data (ν,κ̄,D) = (1,1,l_f) forces **κ̄ < ν at both parents** (the case-IV corner, 2POLE §4b). Empty at td = 6 by reach (2POLE §5b phase 3); OPEN at general td.

**OBSTRUCTION O (honest half; sharp).** The verbatim multi-pole analogue of Prop 8.4 is FALSE at printed tier: at td = 6, m = 2, both poles are row 1 of table (23) (p. 46) with M_P = gcd(2,3) = 1 *forced*, all pre-merge vertices have M = 1 *forced* (MP5), and the resonant jump (r,ν,l) = (2,3,1) with M = 2 solves the printed identity Prop 8.1(iv) *exactly* with rigid coefficients (a₁/a₂ = 2±√3; cases/l1_ode_check.py; SHEET6-L1 §5, SHEET6-2POLE §6a, machine-verified), at Σλ(pre-merge ∪ merge) = 0, passing every located printed constraint. The L1 §3 blind spot is r-uniform: the l extra q-orbits sit at non-roots of p, carry no tree vertex, no puncture, no cv vertex, no λ, no pole — nothing printed sees them except deg q. At pattern level the escape is m-uniform: for every m, choosing lν ≡ −1 (mod m), ν odd, gives M_{G\*} = m at spend 0 (arithmetic existence only; r-edge H1 ratio-consistency unverified for m ≥ 3). Hence the MP7 residual is irreducible from the printed statement list, and MP0–MP9 is the exact printed-tier frontier.

---

## 3. Derivation

All page numbers: refs/sigray_full.pdf, printed page = pdf page. The printed inventory used is listed once: St 2.1/Not 2.4 (pp. 8–9); Not 3.3 (p. 12); St 3.9 (p. 15); St 3.16 (p. 17); Prop 3.2/St 3.17/3.18 (p. 18); Prop 4.2 (p. 19); Prop 5.1/Not 5.1–5.2 (pp. 23–25); Prop 5.3 (p. 25); St 5.2 (p. 26); Props 5.5–5.8 (pp. 26–28); Thm 6.1 (p. 28); Not 6.1/St 6.1–6.2 (p. 29); Props 6.7/6.8 (pp. 33–34); Not 7.1/St 7.1–7.3 (p. 35); Prop 7.2 (p. 36); Prop 7.5 (22) (p. 38); Cor 7.1, Not 8.1, St 8.1, Prop 8.1 (pp. 39–41); St 8.2–8.5 (pp. 41–43); Cor 8.1, Props 8.2–8.4 (pp. 43–45); table (23) (p. 46); Not 9.1–9.2, St 9.1–9.4 (pp. 48–49); Prop 9.2 (p. 50).

### D1 (MP0)
(⊇) Each C_i ⊆ Ta& ∩ Va: the printed Prop 8.4 proof line (p. 45) "From Propositions 6.7 and 6.8, we obtain F_0,…,F_n ∈ Ta&" applies from F_0 = P_i — nothing in the construction uses |T_{a,pole}| = 1 (2POLE §1b); poles are in Ta& (d > 0 and deg p ≥ 2 by Prop 5.3(iv)–(v) + St 3.16), and Va-membership descends via Not 3.3(i).
(⊆) Any H ∈ Ta& ∩ Va \ {(0,x),(0,y)} has deg p_H ≥ 2 (St 3.16: p has more than one root). Prop 6.8 (p. 34, verbatim: "there exist P, u, v: F = I_P(u), v ≥ u, I_P(v) ∈ T_{a,pole}" — the pole lies above H on the SAME branch) gives I_P(v) = P_s. Not 3.3's ° enumerates every Va-vertex of I_P([0,v)) in decreasing order, branch-independently; H is one of them, so H ∈ C_s.
Leaves: a chain predecessor H of P_j would give deg p_H = mult(p_{P_j}, c) ≥ 2 (St 3.17(i) + St 3.16), contradicting squarefreeness of p_{P_j} (Prop 5.3(v)). So poles have in-degree 0; every non-pole U-vertex is some F°; leaves(U) = {P_1,…,P_m}. ∎

### D2 (MP1)
U is a finite tree: every vertex except (0,y) has the unique out-edge F → F° (Not 3.3 deterministic). Counting edges: Σ_G (r(G) − 1) = −1 over all of U with r = 0 exactly at the m leaves, so Σ_{r ≥ 2}(r − 1) = m − 1. By D1 the Not 9.2-predecessor set of G equals its U-predecessor set, so regularity ⇔ r(G) = 1. No merge strictly below G\*: below the meet all chains coincide (° deterministic; Not 3.3 betweenness excludes side entries from ≥ G\*); r(G\*) ≥ 2 by maximality of G\*. Unique-predecessor at suffix vertices (A2's complement): a second predecessor H′ of a suffix vertex S would, by St 3.16 + Prop 6.8, lie under some pole P_j; C_j visits H′ and continues to S (Prop 3.2 determinism), yet C_j also passes through G\* and reaches S through the trunk — a characteristic sequence is a simple descending path and cannot contain two predecessors of one vertex. Contradiction. ∎

### D3 (MP2, MP3)
Take F ≤ G\*, M_F = 1, G\* ≠ (0,y). Every step of the descent from F is regular (D2), so Prop 8.3 (p. 44, under the P1 reading of its hypothesis) applies inductively: M = 1 all the way down, with 8.3(ii) at interior steps and 8.3(iii) at (0,y): p_{(0,y)} = (η−c)^k, a single root ((0,y) is not a merge since G\* ≠ (0,y), and a second root direction would violate D2's unique-predecessor claim). The printed Bezout endgame (p. 45) then runs verbatim: St 8.1 combination at H = F_{n−1}, (k,l) = w(k_f,l_f) via Cor 6.1 + Prop 6.3; the k-computation's deg = mult steps are valid precisely because every p_{h_j,(0,y)} is evaluated at the single root (this is where 8.3(iii) is load-bearing); k = 1, l = l_f/k_f ∈ ℕ contradicting Thm 6.1 (l_f < k_f, p. 28). Nothing mentions |T_{a,pole}|. — Escape exactness: for F > G\*, the arrival step into the first merge at latest G\* is non-regular (D2), Prop 8.3 is inapplicable there, and since the contradiction lives only at (0,y), no vertex above G\* is killed by this route; conversely all F ≤ G\* are killed. ∎

### D4 (MP4)
Poles have m_F = 0 (Prop 5.1(i) + Not 5.1/5.2), so the h-family is {g} (Prop 4.2) and M_{P_i} = gcd(deg p_{P_i}, deg p_{g,P_i}) (Not 8.1). St 5.2(i): deg p/deg p_g = α/β at poles, so (deg p, deg p_g) = b_i(α,β) and M_{P_i} = b_i·gcd(α,β) = b_i = deg p_{P_i}/α. (Check: reproduces all 11 rows of table (23), p. 46, and St 9.6's printed M = 2 = gcd(4,6).) β-minimal: Λ(P) = a b αβ/ν (Prop 5.6 (19)) = β forces ν = abα; St 5.2(ii): ν | α ⇒ ab = 1 ⇒ b = 1; ν | β ⇒ abα | β with gcd(α,β) = 1 ⇒ α = 1, contra St 2.1. Prime Λ: case ν | α: Λ = ab(α/ν)β divisible by β ≥ 3, so Λ = β and a = b = α/ν = 1; case ν | β: Λ = abα(β/ν) divisible by α ≥ 2, so Λ = α < β ≤ Λ (Prop 5.7) — empty. Since the type (α,β) is global (Lemma 2.1), this is per-vertex, valid at every td — repairing the Λ = td-dependence of SHEET6-TDUNIFORM §2. ∎

### D5 (MP5)
Downward induction from an M = 1 pre-merge vertex H, K = H° still pre-merge: (a) St 8.4 (p. 42) at the pair (K, H = K + c): mult(p_K^{red}, c) | M_H = 1 — the chain orbit is simple. (b) St 8.2 (p. 41) at that μ = 1 arrival: deg q_K > deg p_K; then for every root c′ of p_K, deg q·mult(p,c′) ≥ deg q > deg p, so every root is searrow — **no northeast roots exist at K at all**. (c) A non-chain root c′ would give the tree vertex K ∗ εc′ (St 3.18; the 0-root always continues) with, by St 3.9(iii) + St 3.17(i) + Prop 8.1(i) + the St 6.2 computation (p. 29), K ∗ εc′ ∈ Ta& and deg p = i·mult(p^{red}, εc′) ≥ i ≥ 2; Prop 6.8 then manufactures a pole above it **on that branch** — necessarily one of the m poles of T_{a,pole} (this consumes no pole budget, which is why it scales to every m, replacing L1a's m=2-only third-pole counting); that pole's chain visits K through direction c′ (Not 3.3/Prop 3.2), making K a merge vertex — contradiction with K strictly pre-merge. So p_K = single simple ν-orbit, dp = ν. (d) Root law + eta law [P2] (exact order/residue counting on (iv): at a p-root of mult μ, mult(q) = 1 forced; off-p q-roots simple; η-residue b ≡ 1 mod ν): dq = nν + 1, M_K = gcd(ν, nν+1) = 1 — verbatim the thesis's own step in St 9.6's proof (p. 52). (e) λ_K = 0: no direction in Ta% exists (b); the q-extras at non-roots of p have no tree continuation (St 3.18). (f) No ray separates: all full-pattern roots lie in one ν-orbit with a unique continuing representative (St 3.18; Prop 5.6's proof, p. 27). At the merge arrival: St 8.4 at (G_i, H_i) gives μ_i = 1. ∎

### D6 (MP6)
Merge ≠ pole: an arriving direction has full multiplicity deg p_{H_e} ≥ 2, contradicting Prop 5.3(v) squarefreeness. Let some μ_j = 1. (a) k = 0: exactly the D5(c) manufacture, now read at G — every root of p_G supports, via Prop 6.8's same-branch pole, an incoming chain of one of the m poles; the roots of p_G are precisely the r arriving directions, in distinct ν-orbits (St 3.18: one continuation per orbit). (b) Equal-quotient: deg p_{H_e} = mult(p_G^{full}, c_e) = i·μ_e (St 3.17(i) + Prop 8.1(i): p^{full} = ⊖p^i); with μ_j = 1, i = deg p_{H_j} ≥ 2. (c) q-shape by root/eta laws [P2] as in D5(d). (d) Arithmetic: dq = (r+l)ν + 1 ≡ 1 (mod ν) forces gcd(M_G, ν) = 1 (Prop 8.1(v): M_G = gcd(dp, dq)); with dp = (Σμ_e)ν, any common divisor is coprime to ν hence divides Σμ_e: M_G = gcd(Σμ_e, (r+l)ν+1) | Σμ_e ≤ ΣM_{H_e} (St 8.4). All-μ=1 IIa: d | (r+l)ν+1 ⇒ gcd(d,ν) = 1 ⇒ (d | rν ⇔ d | r), and (r+l)ν+1 ≡ lν+1 (mod d): **gcd(rν,(r+l)ν+1) = gcd(r, lν+1)** exactly (A1's "divides" upgraded to A2/A3's equality; elementary both ways). ZCH: dp = (r−1)ν+1, difference lν, coprimality to ν gives M = gcd((r−1)ν+1, l). ν = 1: q = p·s, M = gcd(r, r+l) = gcd(r,l). (Machine-swept: r ≤ 9, ν ≤ 12, l ≤ 12, mixed μ-vectors; reproduces every recorded engine cell — (2,3,1) → 2; ZCH (2,2,3) → 3; ν=1 (2,l=2) → 2.) (e) λ_G = 0 as in D5(e). ∎

### D7 (MP7)
l = 0 kills: IIa: M = gcd(r,1) = 1. ZCH/ν=1: l = 0 forces q = p, and (iv) becomes (δ−1+u)pp′ = ⊖p, i.e. p′ = const ≠ 0, i.e. deg p = 1 — below ν+1 resp. 2 ≤ r: impossible. Cascade: Prop 8.3(i) propagates M = 1 down merge-free segments (regular steps, D2); at an M = 1-emitting merge the cascade continues (M_G = 1 known by direct gcd; steps below regular until the next merge). If the cascade reaches G\* with M = 1 and G\* ≠ (0,y), D3 gives the contradiction — so some merge at or above G\* breaks M = 1: a jump, with the D6 anatomy, and (all entries M = 1 ⇒ the FIRST break is an all-μ=1 merge) the resonance l ≥ 1 and 2 ≤ M ≤ r ≤ m outside ZCH. Entry forcing is D4. Root merge: (0,y) ∈ Ta& (d = l_f < k_f = deg p_{(0,y)}, Thm 6.1 read as the Ta&-inequality at π = 0), so D6 applies at (0,y) with ν = 1 (St 9.2(ii)); top-cancellation of (iv) (St 8.2's proof computation, forced since dq ≥ 2, u = 0, δ = l_f/i) gives l_f = i·r/(r+l) and k_f = i·r, hence **k_f = (r+l)·l_f** and ψ = ⌈k_f/l_f⌉ − 1 = r+l−1 (St 9.4). Prop 8.3(iii) fails (r ≥ 2 roots): no M = 1 kill at the root merge. ∎

### D8 (MP8)
Claim: every branch P ∈ Ra\R̄a through the pure M=1 forest or an all-M=1 merge has F\*_P ∈ T_{a,pole}. Ascend along P: at segment vertices the full pattern is a single simple orbit (D5), at all-M=1 merges all roots are chain roots (D6a), at poles the branch either separates above (where deg p = 1 by St 3.17(i) + Prop 5.3(v), and St 3.16 excludes Va-membership there and above) or continues along the defining branch (Prop 5.3(ix)). So P passes through a pole vertex Q₀, and since m_F is a vertex invariant, F\*_P = Q₀ ∈ T_{a,pole}. St 7.2 (p. 35) then bans cv vertices on P; Y(F) = ∅ (literally when M = 1 holds from the pole down: every ray through the segment reaches P_i, g(P) = ∞ by Prop 5.5, no cv vertex by Prop 7.2; under the E9/H2 branch-at-F reading for mid-segment onset); λ_F = 0 (St 9.3 (24)). Ledger itemization of the equality (22), extending SHEET6-LROOT §1 to m poles: (i) pole clusters carry zero cv mass (Prop 5.5 + Prop 7.2, per pole); (ii) chain paths carry none (T_{a,cv} ⊂ T_a^0 = {d = 0}, Not 7.1, while d > 0 down to d_{(0,y)} = l_f > 0); (iii) M=1 pre-merge sub-segments: identically zero rows (D5(f)); (iv) μ=1-arrival merges: zero rows (D6e) — the l q-extras are exhibited EMPTY ledger rows; (v) the x-side keeps its ≥ ψ cost (St 9.4's proof, p. 49). Since (22) is an Euler-characteristic *equality*, no re-partition or refinement of the printed counting frame can price these objects: "≥ 1 unit per M=1 occurrence" is structurally false at every m, td. The only remaining per-pole cost is td = ΣΛ_i ≥ mβ (Props 5.7/5.8): m ≤ td/3. ∎

### D9 (MP9)
m = 2, b = (1,1): D5 forces both chains M=1/λ=0 single-orbit, μ = (1,1) at the meet. Interior meet: r = 2 in D6d, M = gcd(2, lν+1); M = 1 is killed at G\* by D3, so M = 2, i.e. lν odd: l odd ≥ 1 (l = 0 gives gcd(2ν, 2ν+1) = 1), ν odd. ν = 1: (iv) reduces to 2ps′ − l p′s = c′ ≠ 0 (ρ = 2/(2+l), L1 §4's reduction re-derived); l even: divide by p^{(l+2)/2} — (s·p^{−l/2})′ = (c′/2)p^{−(l+2)/2}, whose partial-fraction residue at each root is C(−n, n−1)(a₁−a₂)^{1−2n} with n = (l+2)/2 and C(−n,n−1) = (−1)^{n−1}·C(2n−2, n−1) ≠ 0 for ALL n ≥ 2 (exact; machine-verified n = 2..6) — a log term, so no rational s exists unless c′ = 0, contra ⊖ ≠ 0. This holds at ALL even l, td-uniformly (upgrading L1b beyond its engine caps). l odd gives M = gcd(2, 2+l) = 1, killed. Survivors: IIa(l odd, ν ≥ 3 odd) / ZCH(gcd(ν+1,l) ≥ 2) — exactly the L1 §3 blind-spot family, spend 0. Root meet: ν = 1 (St 9.2(ii)); l = 0: root law gives q = p and (iv) reads 0 = ⊖p ≠ 0 — impossible; l even: the same log-obstruction (u = 0 changes nothing); l odd: locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2, machine-verified exact), no M = 1 kill (Prop 8.3(iii) fails: two predecessors); printed pins: k_f = (2+l)l_f (D7 at r = 2), ψ = l+1 admissible, Σλ = 0 ⇒ l ≤ td−2 (St 9.4 (25)); [+H1] Prop 9.3(d) with child (ν,κ̄,D) = (1,1,l_f) gives 1 = (κ̄_i + n_i)/ν_i, n_i ≥ 1, so κ̄_i ≤ ν_i − 1 at both parents. td = 6: empty by reach (2POLE §5b phase 3). ∎

---

## 4. Honest hypothesis perimeter

**Sanctioned hypotheses (all clauses):**
- **P1** — Prop 8.3's hypothesis read as Not 9.2-regularity (known printed typo; sanctioned SHEET6-2POLE §1b). Load-bearing in D3, D7.
- **P2** — root/eta laws as exact order/residue computations on the printed identity Prop 8.1(iv) (derivation in D5(d)/D6(c); promoted tier per SHEET6-A3L1-REVIEW). Load-bearing in D5–D7, D9.
- **P3** — y-side convention: characteristic sequences terminate at (0,y) as printed (Prop 9.2 p. 50; (0,x) ∈ Ta% per St 9.4's proof p. 49).
- **P4** — entry pin chain: Not 8.1 + Prop 5.1(i)/Not 5.1–5.2 + St 5.2(i) + St 2.1 (D4).

**Clause-local hypotheses:**
- **E9/H2** (branch-at-F reading of λ): needed in MP8 only for *mid-segment* M = 1 onset; when M = 1 holds from the pole down, Y(F) = ∅ holds in the literal Not 9.3 reading.
- **H1** (Prop 9.3(a)–(d) printed-step arithmetic): used only in MP9's root-residual κ̄ < ν clause.

**Engine caps (flagged, not closed):** the ν = 1 interior-merge variant with an η-factor in q (legal only at ν = 1) is excluded only for l ≤ 4 (cases/l1_ode_check.py families B/B-η).

**Open, stated, NOT claimed:** mixed merges with all μ_e ≥ 2 obey only MP6(b)/(d)-subadditivity (k = 0 needs some μ_e = 1; the l ≥ 1 forcing does not apply) — possible only for m ≥ 3 downstream of an earlier jump; the m ≥ 3 pattern-level escape (M = m via lν ≡ −1 mod m) is arithmetic existence only, r-edge H1 ratio-consistency unverified; the root-merge endgame at general td is open (closed at td = 6, m = 2); jump vertices are unkillable at printed tier (witness O — this is a theorem-grade negative, not a gap in the proof).

**Record caveats:** (i) A2's third adversarial vote flagged one *subsidiary* (non-load-bearing) sub-claim as failing and one unflagged record-contradiction; the vote explicitly lists all Theorem M clauses (1)–(4), (5I), the conditional content of (5R), and Prop B as surviving, and every A2 clause grafted here is cross-derived by A1 or so listed. (ii) A3's adversarial votes were truncated in the synthesis input; A3 clauses P1/P3/P4 are independently derived by A1/A2 and grafted at full tier; A3-unique kills are quarantined in §7.

---

## 5. The obstruction half, stated precisely

**Theorem O.** No printed-tier argument can prove M_F ≠ 1 on pre-merge segments (it is false: MP5 forces M = 1 there whenever b_i = 1, which is itself forced at td = mβ and at prime Λ_i), and no printed-tier argument can exclude resonant jump vertices: the cell (r,ν,l) = (2,3,1), M = 2 at td = 6, m = 2 solves Prop 8.1(iv) exactly with rigid coefficients (a₁/a₂ = 2±√3), passes Prop 8.1(iv)-(v), St 8.2/8.4, the root/eta laws, all located budget statements (Σλ = 2 ≤ 3 globally, 0 through the merge), and the entry pins — machine-verified (cases/l1_ode_check.py; SHEET6-2POLE §6a full hand-verified exhibit, every datum absolute). The blind spot is structural and r-uniform: the l extra q-orbits are invisible to every printed statement except deg q (SHEET6-L1 §3). Combined with MP8 (spend 0), the residual is irreducible: **MP0–MP9 is the maximal printed-tier kill**, and the multi-pole problem reduces, for each (m, td), to the finite book of resonant jump cells pinned by MP6/MP7 + the equal-quotient law + Prop 9.3's per-edge ratio equations (pp. 50–51), with entries pinned by MP4.

---

## 6. Refuted attempts (one line each)

1. **Verbatim m-pole Prop 8.4** ("M_F ≠ 1 on pre-merge segments"): FALSE — MP5 proves M = 1 is *forced* there whenever b_i = 1; witnessed forced at td = 6 (row 1 of table (23), M = gcd(2,3) = 1).
2. **Per-segment piecewise restoration** ("rerun the printed induction on each pre-merge segment; only the first vertex above each merge escapes"): wrong — the contradiction is manufactured only at (0,y), so ALL strict ancestors of G\* escape, including inter-merge segments (MP3).
3. **Budget kill** ("each M = 1 occurrence costs ≥ 1, so ≤ td−2 occurrences"): structurally false — the region contributes identically zero rows to the Euler *equality* (22) and Σλ = 0 there; no re-partition of any printed budget can charge it (MP8/Prop B).
4. **λ_root ≥ 1 transported to m poles** (the LROOT-style 8→4 route): dead — λ = 0 is forced at all-M=1 merges and at the root merge (MP8, generalizing SHEET6-LROOT §2 to all m).
5. **Non-resonant jump** (M ≥ 2 at a merge with l = 0): impossible — l = 0 forces M = 1 (IIa) or contradicts Prop 8.1(iv) outright (ZCH, ν = 1) (MP7).
6. **ν = 1 interior jump at m = 2**: dead at all l — even l by the exact log-obstruction (all l, beyond L1b's caps), odd l by M = 1 + MP2; only the η-factor subvariant remains cap-limited (l ≤ 4).
7. **Killing the jump vertex itself from printed statements**: impossible — the (2,3,1) M = 2 cell is a consistent exhibit solving every located printed constraint (Theorem O).
8. **Λ = td pin transport** (TDUNIFORM §2 verbatim at multi-pole): fails as stated (Λ(P_i) < td); rescued only by the per-pole β-minimal/prime-Λ argument via the *global* type (MP4/D4).

---

## 7. Supplementary kills at A3 tier (quarantined pending recorded adversarial confirmation)

From Theorem MPM (pattern-algebra angle; statement complete in the panel record, votes truncated at synthesis). These sharpen the jump book but are NOT counted in Theorem MP:
- **Prime-partition kill (P2):** Λ(P_i) prime forces a_i = b_i = 1, β = Λ(P_i), ν_i = α | Λ(P_i) − 1; hence no counterexample has two pole vertices with distinct prime Λ-parts (e.g. two-pole partitions 8 = 3+5, 10 = 3+7, 12 = 5+7 excluded outright), and a prime part p forces p | Λ_j for every other part unless ν_j = p, p | b_jα − 1, Λ_j = a_j b_j α.
- **RH-lemma kills (P5):** n_q − 1 ≤ D_min for searrow reduced patterns; saturated IIa cells with (lν+1) | r die (e.g. (3,2,1), (4,3,1), (5,4,1)); ν = 1 merges with gcd(r,l) ≥ 2 and (r | l or l | r) die (reproves L1b uniformly, extends to all r; no ν = 1 emission of M ≥ 2 for r ≤ 3); full-M ZCH cells (M = (r−1)ν+1) die; IIa l = 1 exists iff (ν+1) ∤ r, with a rigid one-scale closed form.
- **OB extension:** cells (3,5,1) M = 3 and (4,7,1) M = 4 solve Prop 8.1(iv) with admissible coefficients (machine-verified per A3) — candidate m = 3, 4 consistent exhibits.
**Action:** re-referee these three blocks (their derivation exists in the panel record through P2 case analysis; the machine check /tmp/mpm_check.py is session-local and must be rebuilt under cases/).

---

## 8. The sharpest remaining gap, and the concrete next step

**The gap.** Everything printed now funnels into a single residual object: the **resonant jump vertex** — an all-M=1 merge with l ≥ 1 extra simple q-orbits, M = gcd(r, lν+1) ≥ 2 (or its ZCH/mixed analogues), spend 0, whose l extras no printed statement can see (Theorem O). For m = 2 this is exactly IIa(l odd, ν ≥ 3 odd, M = 2) / ZCH(gcd(ν+1,l) ≥ 2) at an interior meet, plus the root-meet l-odd residual; for m ≥ 3 the cells lν ≡ −1 (mod m) exist at pattern level but their *reachability* (r-edge ratio consistency) is untested. The kill, if one exists, must come from the H1 layer that the printed statements stop short of: matching the rigid (iv)-coefficients of a jump cell against the per-edge Prop 9.3(a)–(d) ratio equations of ALL r incoming chains simultaneously — a computation never yet run for any cell (the l = 1 rigidity a₁/a₂ = 2±√3 shows the coefficients are fully pinned, so the match is a finite check per cell).

**Concrete next step (ordered, engine-able):**
1. **Build the r = 3 jump-cell reachability check**: extend cases/l1_ode_check.py + cases/twopole_check.py to r = 3 incoming edges; impose Prop 9.3(a)–(d) per-edge (H1 tier) plus the equal-quotient law and entry pin at the cell (r,ν,l) = (3,5,1), M = 3, in the minimal m = 3 configuration td = 3β. Outcome either way is decisive: a ratio-inconsistency kills the first m ≥ 3 escape cell and gives the template for the whole book; consistency produces the m = 3 exhibit and sharpens Theorem O to m ≥ 3.
2. **Close the m = 2 root-merge residual at td = 7, 8** (l odd, k_f = (2+l)l_f, both κ̄ < ν) by the reach method of 2POLE §5b phase 3 — the only MP9 clause still td-bounded.
3. **Run the coefficient-vs-ratio match for the td = 6 cell (2,3,1)**: the exhibit's pinned pattern coefficients against both parents' Prop 9.3 edge data — the single most valuable H1-tier computation, since this cell is the minimal consistent example anchoring the entire obstruction.
4. **Promote §7**: referee the A3 prime-partition and RH kills; if confirmed, they delete the partitions 8 = 3+5, 10 = 3+7, 12 = 5+7 and all saturated cells from the book before any engine run.

---

## 9. Cross-consistency notes (grafting record)

- A1.T2 = A2(4) (restored kill; A2's unique-predecessor argument adopted into D2/D3 as the cleaner single-root justification at (0,y)). A1.T4/T5 = A2(3) = A3.P4 (merge anatomy; independent derivations agree cell-by-cell). A1.T5's "M_G | gcd(r, lν+1)" upgraded to A2/A3's equality (elementary proof in D6d). A1.T6's root pin ψ = r+l−1 ⟷ A2(5R)'s ψ = l+1 at r = 2: consistent. A1.T7 = A2.Prop B (budget transparency; A2 adds the Euler-equality itemization, A1 adds the F\*_P ∈ T_{a,pole} branch argument — both used in D8). A1's G\* = A2's G_last (max ∩C_i). A2(1) prime-Λ pin subsumes A1's β-minimal pin; both in MP4.
- Escape-set adjudication: A1.T3's correction (ALL strict ancestors of G\* escape) supersedes any "first-vertex-above-merge" phrasing; A2(2)'s "pre-merge segment" forcing and A2.P3's inter-merge propagation condition are compatible refinements.
- The k = 0 manufacture (D5c/D6a) is the load-bearing novelty in both A1 and A2, derived independently with the same printed chain (St 6.2 computation + St 3.9(iii)/3.17(i)/8.1(i) + Prop 6.8 same-branch); its no-pole-budget character is what makes Theorem MP m-uniform.

## 10. Reproduction

- Printed ground truth: refs/sigray_full.pdf pp. 8–9, 12–19, 23–29, 32–36, 38–46, 48–52 (all re-read on-page by the panel).
- Machine checks: cases/l1_ode_check.py (jump-cell rigidity, families incl. B/B-η caps); cases/twopole_check.py (2POLE §5 phases); cases/lroot_ledger.py (ledger itemization template for D8); gcd sweeps r ≤ 9, ν ≤ 12, l ≤ 12 + mixed μ-vectors and the log-obstruction residues C(−n, n−1), n = 2..6 (panel sessions; A3's /tmp/mpm_check.py to be rebuilt under cases/ per §7).
- Prior sheets: SHEET6-2POLE.md §§1–6, SHEET6-L1.md §§0–7, SHEET6-LROOT.md §§1–5, SHEET6-TDUNIFORM.md §§1–8, SHEET6-A3L1-REVIEW.md.
codex
The first three documents already expose a key fault line: the campaign’s strongest statements are conditional on translating local reduced-pattern algebra back into globally reachable characteristic chains. I’m now checking whether the depth theorem genuinely closes that translation or only makes the candidate book finite.
exec
/bin/zsh -lc "sed -n '1,230p' SHEET6-DEPTH.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
Status: PROVED + PROMOTED (2026-08-12, SHEET6-DEPTH-REVIEW.md: all fronts confirmed; one fix adopted — the printed proof yields d0 <= 2*gen+2, not gen+2; td=6 unaffected; final BOOK(m,td) spec = review doc closing section).

# SHEET6-DEPTH.md — the Chain-Depth Closure Lemma: the M=1 jump-cell menu is depth-invariant

**Status: PROVED (2026-08-12), H1 tier (Prop 9.3 printed-step arithmetic) over
promoted MP0–MP8; machine-verified (cases/depth_closure_check.py, 13/13
exact checks). Consequence: the demoted "finite book per (m, td)" rider of
Theorem MP (SHEET6-MULTIPOLE.md §0/§5; demotion SHEET6-MP-REVIEW.md Front 5)
is RESTORED in corrected, sharper form (§8). Two engine-model corrections
found en route: the ZCH 0-edge is Prop 9.3 case (III), not (a)–(d) (§5c),
and the root-merge edge is case (IV) (i)–(m), which *derives* the n = ν−κ̄
pin (§5d).**

Ground truth: refs/sigray_full.pdf (printed page = pdf page), re-read
on-page this session: Def 3.1/3.2, St 3.1–3.2 (p. 10); Def 3.3–3.4,
Not 3.1–3.2, St 3.3 (p. 11); Not 3.3–3.8, St 3.4–3.6 (pp. 12–13); Not
3.9–3.11, St 3.7 (p. 13); Prop 3.1, Not 3.12, St 3.8 (p. 14); St 3.9
(p. 15); St 3.16, Prop 3.2, St 3.17 (pp. 17–18); Prop 5.3(iv)–(v) (p. 25);
St 5.2, Props 5.5–5.6 (pp. 26–27); Props 5.7–5.8, Def 5.1 (pp. 27–28);
Prop 8.1 (pp. 39–41); St 8.2/8.4 (pp. 41–42); Not 9.1, St 9.1–9.2 (p. 48);
Prop 9.2, Prop 9.3 (pp. 50–51); St 9.6 + proof (pp. 51–52). Promoted
priors: SHEET6-MULTIPOLE.md (MP0–MP9, Theorem O), SHEET6-MP-REVIEW.md
(esp. §5a/§5c), SHEET6-2POLE.md, SHEET6-L1.md. Engine cross-checked:
cases/twopole_check.py phase 4.

---

## 0. Verdict in one paragraph

The M=1 pre-merge chain step conserves a single rational invariant. Write
each chain frame in the i-normalized coordinates ρ := D_F/deg(p_F) (full
pattern degree) and set **w_F := (κ̄_F − ρ_F)/ν_F** with κ̄ := κ_F(1−π(F)).
Then (i) every M=1 segment vertex is a *Puiseux characteristic vertex* of
its own pole's series, with ν ≥ 2, and every chain edge is Prop 9.3 case
(II) (§2); (ii) the chain step multiplies w by n/Δ, Δ := (n−1)ν_child + 1,
where (ν_child, n) is the child's single-orbit pattern — so the infinite
"l = 0" direction (n = 1) that makes depth unbounded **fixes w**, while
every resonant step (n ≥ 2) requires Δ | num(w) and contracts w by a factor
≤ 2/3 (§3–4); (iii) the entire jump-cell layer factors through w: for every
μ = 1 edge into a merge, **κ̄_merge − D_merge/i = w** (the handshake), the
merged-child data is (κ̄, D/i, ρ) = w·(dq, dp, 1)/(dq−dp), the join forces
all arriving chains to share w, and per w the admissible cells are finite
with ν_cell *determined* by (κ̄_merge, l) (§5). Hence the set of w-values
over all depths is the finite computable closure W(w₀), realized by depth
d₀ = gen(W)+2, and the map (segment depth) → (reachable jump-cell menu) is
**constant beyond d₀**: DEPTH-INVARIANCE (Lemma, §6). At td = 6, m = 2:
W = {2}, d₀ = 2, and the menu is *exactly* the promoted residue cell
IIa (r,ν,l) = (2,3,1), M = 2, child (κ̄, D/i) = (5,3) — i.e. Q =
(6,12,3,2,5) — reproducing the 351/351 empirical depth-invariance and
reproving the root-meet kill in one line (root merges need w < 1). The
jump-vertex book is therefore **finite per (m, td)** (§8).

---

## 1. Setting and normalization

Notation as in SHEET6-MULTIPOLE.md §1. Fix a pole P_i ∈ T_{a,pole} with
entry datum (a_i, b_i, ν_i) of type (α,β) (MP4: Q(P_i) = (a_iα, b_iα, ν_i,
b_i, a_i(α+β)), St 5.2 + Not 8.1 + St 9.1 pp. 26/39/48). An **M=1 segment**
is a maximal run F_0 → F_1 → … → F_d of the characteristic sequence
(Prop 9.2, p. 50) with M ≡ 1, starting at the pole vertex (b_i = 1, forced
at β-minimal and prime Λ_i by MP4) or at an M=1-emitting merge child, and
ending at the last vertex before a merge vertex G (r(G) ≥ 2) or before
(0,y). By MP5, every F_j with j ≥ 1 has reduced pattern a single simple
ν-orbit: (dp, dq) = (ν_j, n_jν_j + 1), n_j ≥ 1, M = 1, λ = 0.

Frames are taken **i-normalized** ("shape space" of the engines, P-free):

- Q-datum (Not 9.1, p. 48): Q(F) = (D_F, deg(p_F), ν_F, M_F, κ̄_F),
  κ̄_F := κ_F(1−π(F)).
- ρ_F := D_F/deg(p_F) with deg(p_F) the FULL f-pattern degree (Not 3.10/
  3.13, pp. 13/16); by Prop 8.1(i) (p. 40) p_full = ⊖(ξ^δ p_red)^i, so
  deg(p_F) = i_F·deg(p_red) and ρ_F = (D_F/i_F)/deg(p_red).
- **w_F := (κ̄_F − ρ_F)/ν_F.**

ρ < κ̄ at every segment vertex (St 8.2, p. 41: deg q > deg p at μ = 1
arrivals, and dp/dq = i-normalized slope ratio, Prop 9.3(b)), so w > 0.

Equal-quotient transport (used throughout): for any edge F = G + c
(F above G; Prop 3.2/St 3.17(i), pp. 17–18), deg(p_F) = mult(p_G, c) =
i_G·mult(p_G^red, c) = i_G·μ_e, and μ_e | M_F = 1 by St 8.4 (p. 42) on M=1
ancestry, so **deg(p_parent) = i_child** on every segment edge and every
all-μ=1 merge edge. This is MP6(b) read at chain edges; it is what makes
the (b)-equation of Prop 9.3 close in the ρ-coordinate.

---

## 2. DS1 (characteristic rigidity): every segment vertex is a V_{1,a} characteristic vertex of its own pole, and every chain edge is Prop 9.3 case (II)

**Claim.** For 1 ≤ j ≤ d: (a) ν_j ≥ 2 and the orbit base c ≠ 0; (b)
F_j ∈ V_{1,a}; (c) κ̄_{F_j} ∈ ℤ; (d) π(F_j) is a characteristic exponent of
P_i's own Puiseux series, the segment vertices are *consecutive*
characteristic vertices I_{P_i}(α_s), and each edge F_{j-1} → F_j is case
(II) of Prop 9.3 (p. 50), so its (a)–(d) equations hold verbatim.

*Proof.* (a) F_j ∈ V_a ∩ Ta& \ {(0,x),(0,y)} (MP0), and St 3.16 (p. 17) is
an iff: p_{F_j} has more than one root. The single simple ν-orbit has root
set {ζc : ζ^ν = 1} — more than one root forces ν ≥ 2 and c ≠ 0. (This is
the thesis's own step: St 9.6's proof, p. 52, "by Statements 3.16 and 3.18
one has p(η) = ⊖(η^ν − c^ν) for some ν = ν_F".)

(b) Not 3.4 (p. 12): ν_F := 1 unless F ∈ V_{1,a}; so ν_j ≥ 2 ⟹ F_j ∈
V_{1,a}, i.e. F_j = I_{P′}(α′_{j′}) at a characteristic value of some
P′ ∈ R̄_a\R_a (Def 3.4, p. 11), with ν_j = e′_{j′−1}/e′_{j′} ≥ 2 strictly
(Def 3.1(ii), p. 10: e_i = gcd(e_{i−1}, β_i) < e_{i−1}).

(c) Not 3.5 (p. 12): κ_{F_j} = κ′/e′_{j′} and π(F_j) = β′_{j′}/κ′ with
e′_{j′} | β′_{j′} (Def 3.1(ii)), so κ_{F_j}π(F_j) = β′_{j′}/e′_{j′} ∈ ℤ and
κ̄_{F_j} ∈ ℤ.

(d) P_i's branch passes through F_j, so its series coefficient at the
exponent u := π(F_j) is a root of p_{F_j} (Prop 3.1(**), p. 14: pattern
roots = continuation coefficients of the fiber branches). By (a) the root
set contains no 0, so c_u(P_i) ≠ 0. Since F_j = I_{P′}(α′_{j′}), the series
P′ and P_i agree strictly below u (Def 3.3, p. 11: u ≤ O(P_i, P′)), so
they generate the same exponent lattice L below u; u ∉ L because β′_{j′}
is not divisible by e′_{j′−1} (Def 3.1(i)). A nonzero coefficient of P_i
at an exponent outside its running lattice is, by Def 3.1(i), exactly the
next characteristic exponent of P_i: u = α_s(P_i) for some s. Every V_a
vertex on I_{P_i}([0, π(P_i-vertex)]) is enumerated by the descent (Not
3.3, p. 12), every characteristic value of P_i is a V_a vertex (Def 3.4),
and every segment vertex is characteristic by the above — so consecutive
segment vertices sit at consecutive characteristic exponents of P_i. The
edge F_{j−1} → F_j then has parent at α_s(P_i), child at α_{s−1}(P_i):
with P = P_i this is literally case (II) of Prop 9.3 ("F ∈ V_{1,a} and
u = α_{j−1}"), and the case-(I)/(II) equations (a)–(d) apply. ∎

**Remarks.** (R1) The depth of an M=1 segment below its pole vertex is
therefore at most the number m_i of characteristic exponents of P_i, so
Π_j ν_j ≤ e_0 = κ_i and d ≤ log₂ κ_i. This is finite for every actual
(f,g) but κ_i is NOT bounded by (m, td) — td is the topological degree
(Def 5.1, p. 28), which does not control the Puiseux denominator at
infinity. This is the honest reason a depth CAP (option (a)) is
unavailable and depth-invariance is the right statement. (R2) The
phase-4 "zch chain children" of cases/twopole_check.py (ν_F = 1, p = η^i)
have a single distinct root, hence are NOT V_a vertices (St 3.16 iff) —
engine over-generation, harmless there (they produced no residue and, by
§3 R3 below, they conserve w anyway).

---

## 3. DS2 (the orbit map and its conserved quantity)

**Claim.** Let G → F be a segment edge (G = parent, F = G° single simple
(ν_F, n_Fν_F+1)-orbit, μ = 1). Then, with Δ_F := (n_F−1)ν_F + 1 = dq−dp:

    t     := (κ̄_G − ρ_G)/Δ_F        [edge scale]
    n_e   =  t·ν_F − ρ_G  ∈ ℕ*       [Prop 9.3(a)-(b) edge parameter]
    κ̄_F  =  (κ̄_G + n_e)/ν_G = t·dq_F/ν_G = w_G·dq_F/Δ_F
    ρ_F   =  t/ν_G,      κ̄_F = ρ_F·dq_F
    w_F   =  w_G · n_F/Δ_F.

In particular: **n_F = 1 ("l = 0" step, the unbounded direction) fixes
w_F = w_G for every admissible ν_F; n_F ≥ 2 ("resonant" step) contracts
w_F ≤ (2/3)·w_G** (since ν_F ≥ 2 gives Δ_F ≥ 2n_F − 1).

*Proof.* Case (II) applies (DS1(d)). Prop 9.3(b) (p. 50), i-normalized by
deg(p_G) = i_F (§1, μ_e = 1): dp_F/dq_F = (ρ_G + n_e)/(κ̄_G + n_e). Both
sides in lowest terms (gcd(ν_F, n_Fν_F+1) = 1), so ρ_G + n_e = tν_F and
κ̄_G + n_e = t·dq_F with t = (κ̄_G − ρ_G)/(dq_F − dp_F) = w_Gν_G/Δ_F.
Prop 9.3(d): κ̄_F = (κ̄_G + n_e)/ν_G = t·dq_F/ν_G. Prop 9.3(c) with
deg(p_F) = deg(p_G)·ν_F = i_Fν_F: ρ_F = (ρ_G + n_e)/(ν_Gν_F) = t/ν_G.
Then w_F = (κ̄_F − ρ_F)/ν_F = t(dq_F − 1)/(ν_Gν_F) = t·n_F/ν_G =
w_G·n_F/Δ_F. Contraction: n_F/Δ_F = n_F/((n_F−1)ν_F+1) ≤ n_F/(2n_F−1)
≤ 2/3 for n_F, ν_F ≥ 2. ∎

**Remarks.** (R3) Robustness: a hypothetical ν_F = 1 step has Δ = n_F, so
w_F = w_G for ALL n_F — the conservation does not even need DS1's
exclusion of such steps (they conserve w trivially; DS1 is what grounds
the case-(II) equations). (R4) The identity κ̄_F = ρ_F·dq_F means every
post-entry frame satisfies κ̄ = ρ·(own dq); equivalently ρ = w/n and
κ̄ = w(nν+1)/n: the frame is coded by (w, ν, n). (R5) The printed record
itself displays the conservation: St 9.6(v) (p. 51), the thesis's own
λ = 0 suffix family Q = ((6s+3)j, (4s+2)j, 2s+1, 2, 3s+3), has w ≡ 3/2
for every s (machine check 5).

---

## 4. DS3 (the resonance budget: finitely many w-values)

**Claim.** Write w_G = a/b in lowest terms. A resonant step (n_F ≥ 2)
requires **Δ_F | a**; consequently ν_F ≤ a − 1, n_F ≤ (a+1)/2, there are
at most as many resonant options as factorizations Δ − 1 = (n−1)ν with
Δ | a, and num(w_F) ≤ (2/3)·a. Hence along ANY segment, of ANY depth, the
number of resonant steps is < log_{3/2} num(w_0) + 1, and the set of
w-values reachable from w_0 (over all depths) lies in the finite,
explicitly computable closure

    W(w_0) := closure of {w_0} under w ↦ w·n/Δ,  Δ | num(w), Δ ≥ 3,
              Δ = (n−1)ν + 1, n ≥ 2, ν ≥ 2.

*Proof.* κ̄_F ∈ ℤ (DS1(c)) and κ̄_F = t·dq_F/ν_G = w_G·dq_F/Δ_F =
a·dq_F/(bΔ_F). Now gcd(Δ_F, dq_F) = gcd(Δ_F, dq_F − Δ_F) = gcd(Δ_F, ν_F)
= gcd((n_F−1)ν_F + 1, ν_F) = 1, so bΔ_F | a·dq_F forces Δ_F | a. Then
Δ_F ≥ ν_F + 1 and Δ_F ≥ 2n_F − 1 give the ranges, and num(w_F) divides
a·n_F/Δ_F ≤ (2/3)a. A strictly decreasing chain of positive integers
contracting by ≥ 1/3 per step has length < log_{3/2}(a_0) + 1. W(w_0) is
finite because each generation divides-and-contracts the numerator. ∎

**Entry values.** w_0 = (a_i(α+β) − a_i/b_i)/ν_i = a_i(b_i(α+β)−1)/(b_iν_i)
(MP4 entry pin); on the M=1 axis b_i = 1: w_0 = a_i(α+β−1)/ν_i. Λ_i =
a_ib_iαβ/ν_i ≤ td and mβ ≤ td bound a_i, α, β, ν_i, so num(w_0) ≤ td²/2
crudely; everything downstream is computable per (m, td). At td = 6:
w_0 = 1·(2+3−1)/2 = 2, and W(2) = {2} — no divisor Δ ≥ 3 of 2 exists, so
**no resonant step is admissible at all** (machine check 2).

---

## 5. DS4 (the jump-cell menu factors through w)

Let G be a merge with arriving all-μ=1 edges from last-segment vertices
H_e, and let (dp_c, dq_c) be the merged reduced pattern (MP6(d) menu:
IIa (rν, (r+l)ν+1); ZCH ((r−1)ν+1, (r−1+l)ν+1); I (r, r+l)),
Δ_c := dq_c − dp_c.

### 5a. The handshake

For every μ_e = 1 edge governed by the case-(I)/(II) equations:

    κ̄_G = (κ̄_e + n_e)/ν_e,   D_G/i := μ_e(ρ_e + n_e)/ν_e = (ρ_e + n_e)/ν_e
    ⟹  **κ̄_G − D_G/i = (κ̄_e − ρ_e)/ν_e = w_e.**

One line, cell-independent. Consequences: (i) the join condition (common
(κ̄_G, D/i) across edges, SHEET6-MP-REVIEW §5c layer J) forces **all
arriving chains to carry the same w**; (ii) solving the edge equation
against the cell exactly as in §3 gives

    κ̄_G = w·dq_c/Δ_c,   D_G/i = w·dp_c/Δ_c,   ρ_G = w/Δ_c,

so the **entire merged-child datum depends only on (w, cell)** — not on

exec
/bin/zsh -lc "sed -n '231,500p' SHEET6-DEPTH.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
the segment depth, not on (ν_e, n_e, κ̄_e) separately. (The per-edge
admissibility n_e ∈ ℕ*, n_e ≡ −κ̄_e (mod ν_e) does depend on the state
(w, ν_e, n_e); see §6 for why this does not spoil stabilization.)

### 5b. Cells are finite per w

For jump cells (l ≥ 1, MP7) one has dq_c ≤ (r+1)Δ_c in all three families
(elementary: e.g. IIa: (r+1)(lν+1) − ((r+l)ν+1) = r(lν+1−ν) ≥ 0), so
**w < κ̄_G ≤ (r+1)w, κ̄_G ∈ ℤ**. Fixing κ̄_G in this finite window and
setting Di := κ̄_G − w:

- IIa: ν(wr − Di·l) = Di ⟹ ν determined per l < wr/Di;
- ZCH: ν(l·Di − w(r−1)) = w ⟹ ν determined per l ≤ wr/Di;
- I: l = wr/Di (ν = 1).

Finitely many (family, ν, l, M = gcd) per (w, r ≤ m) — the SHEET6-MP-REVIEW
§5a per-frame finiteness, now *uniform in depth*. Cascade cells (l = 0,
M = 1 emission) are the infinite ν-family, but their child is again an
M=1 segment entry with **w_child = w·(r+l)/(lν+1)** (= r·w at l = 0),
ν-independent at l = 0; with MP1's Σ(r−1) = m−1 the composed closure
multiplies at most m−1 such factors — still a finite computable w-set.

### 5c. Correction: the ZCH 0-edge is case (III)

The 0-direction chain's own pole has coefficient 0 at π(G) (that is what
"chain at the 0-direction" means), so π(G) is NOT a characteristic
exponent of that pole's series, while G ∈ V_{1,a} whenever ν_G ≥ 2
(ν ≥ 2 forces V_1 membership, Not 3.4; π(G) is off-lattice, realized as a
characteristic value of the branch that does jump there). For the 0-edge
Prop 9.3 case (III) applies ("F ∈ V_{1,a} and u > α_{j−1}"), equations
(e)–(h) with ν := ν_F: i-normalized, κ̄_G = κ̄_e + n′, D_G/i = ρ_e + n′
with n′ = n/ν_G ∈ (1/ν_G)ℕ*, hence handshake

    **κ̄_G − D_G/i = κ̄_e − ρ_e = ν_e·w_e   (0-edge, case III).**

The join then demands w_other = ν_e·w_{0-chain} with ν_e ≥ 2: **ZCH cells
are reachable only when the arriving chains carry w's in an integer ratio
ν_e ≥ 2**. In particular, at td = 6 (single value w = 2) ZCH is
unreachable outright, and the corrected pre-suffix jump menu is exactly
{IIa (2,3,1), M = 2} — the promoted residue (machine check 7; the engine's
(a)–(d)-modelled ZCH child (M=3, κ̄=3) was suffix-killed in the promoted
record, so no promoted conclusion changes, but the book spec should carry
the corrected ZCH reach equation). The non-0 edges of a ZCH merge, and
all IIa edges, are case (II) (DS1(d) argument at the merge: nonzero
arrival coefficient at an off-lattice exponent = characteristic exponent
of the arriving pole's series); I-family merges (ν_G = 1) are case (I)
(V_{2,a}\V_{1,a}, lattice meet). All non-0 edges keep the §5a handshake.

### 5d. Root merges: w < 1, and the case-(IV) grounding of the n = ν−κ̄ pin

(0,y) ∉ V_{1,a} ∪ V_{2,a} (α_j > 0 and O(P,P′) > 0), so a root-merge edge
is Prop 9.3 **case (IV)**, equations (i)–(m) (p. 51): (i) ν_e = κ_e; (j)
(1−v)κ_e < ν_e, i.e. κ̄_e < ν_e; (k) d_{(0,y)} = (D_e + (ν_e − κ̄_e)·
deg p_e)/ν_e. Setting n* := ν_e − κ̄_e ≥ 1, (k) is the (c)-equation with
the edge parameter FORCED: n_e = n* — this derives, on printed ground, the
"n_e = ν_e − κ̄_e, both parents κ̄ < ν" pin that SHEET6-MP-REVIEW §2c
established for MP9's root clause (and (l)–(m) add d < deg p_G and the
M-divisibility as extra filters). The handshake at the root (κ̄_{(0,y)} =
1, St 9.2(iii); D_{(0,y)} = l_f, St 9.2(i); D/i = l_f/i₀):

    **w_e = 1 − l_f/i₀ ∈ (0,1): root merges require w < 1.**

At td = 6, W = {2}: root meets are dead in one line — reproving the §2c
raised-caps sweep result exactly (machine check 2: every reachable frame
has w = 2 ≥ 1).

---

## 6. The Chain-Depth Closure Lemma

**Lemma (chain-depth closure / depth-invariance).** Let (m, td) be given,
and let E be an M=1 segment entry (pole entry via MP4, or M=1-emitting
merge child), with invariant w_0 = w(E). Let Menu_{≤d}(E) be the set of
jump-cell data (family, ν, l, M, κ̄_G, D_G/i) reachable at the end of a
segment of depth ≤ d from E (per-edge Prop 9.3 reach, all-μ=1, MP6/MP7
anatomy). Then:

1. (finite w-alphabet) every frame reachable from E at any depth has
   w ∈ W(w_0), the finite closure of §4, and each segment performs fewer
   than log_{3/2} num(w_0) + 1 resonant steps; all other steps fix w;
2. (menu factorization) Menu_{≤d}(E) ⊆ Menu(W(w_0)) :=
   ∪_{w ∈ W(w_0)} Menu(w), which is finite by §5b, with the case-(III)
   ZCH constraint of §5c and the root constraint w < 1 of §5d;
3. (stabilization) Menu_{≤d}(E) = Menu_{≤d₀}(E) for all d ≥ d₀ where
   d₀ = gen(W(w_0)) + 2 ≤ log_{3/2} num(w_0) + 2: **the map
   depth ↦ reachable jump-cell menu is constant beyond d₀.**

*Proof.* 1 is DS1–DS3 (§2–§4). 2 is DS4 (§5): each edge's contribution to
the merged child is a function of (w_e, cell) alone; joins force shared
handshakes. 3: (⊇ for large d) an l = 0 step maps a state (w, ν, 1) to
(w, ν′, 1) and preserves the menu contribution — for integer w every
ν′ ≥ 2 is admissible (n_e = w(νν′ − 1) ∈ ℕ*, κ̄′ = w(ν′+1) ∈ ℤ), for
w = a/b the admissible ν′ form the congruence class ν′ ≡ −1 (mod b)
(nonempty, self-reproducing) whenever the state admits any continuation —
so every menu item realized at some depth ≤ d₀ is realized at every
larger depth along an l = 0 tail, or else lies on a w-branch with no
continuation, which contributes to no deeper menu either. (⊆) a menu item
at depth d > d₀ has a w-generation history of ≤ log_{3/2} num(w_0)
resonant steps; replaying exactly those steps (and one l = 0 step to
realize the same (ν, n)-admissibility class, available by the congruence
argument) realizes the same (w, cell) pair — with identical per-edge
integrality since menu admissibility from a state (w, ν, n) depends only
on that state and l = 0 tails reproduce the state family — at depth
≤ d₀. ∎

**At td = 6, m = 2** (entry (ρ, ν, κ̄) = (1, 2, 5)): W = {2}, gen = 0,
d₀ = 2; reachable frames are exactly {(2, ν, 2ν+2) : ν ≥ 2} (the
phase-4 record's 24 μ1-shapes; check 6); the menu is constant from depth 1
and equals the promoted record: jump cell IIa (2,3,1), M = 2, child
(κ̄, D/i, ρ) = (5, 3, 1/2) = Q(6,12,3,2,5) at i = 2 — explaining the
351/351 pair depth-invariance — plus the suffix-dead engine-model ZCH
(2,3) cell, which the corrected §5c model removes pre-suffix; ν = 1 cells
only l ∈ {1,2,4} (l = 1 has M = 1; l = 2,4 are MP9's even-l ODE-dead);
root meets: none (w = 2 ≥ 1).

---

## 7. Mechanical verification

cases/depth_closure_check.py — exact (int/Fraction), self-contained except
check 6, ~seconds; 13/13 PASS this session:

1. **Step laws** on every BFS edge (td=6 depth ≤ 12; all entries depth 8):
   w′ = w·n/Δ; Δ | num(w) at resonant steps; contraction ≤ 2/3.
2. **td=6 record**: W = {2}; no resonant step exists (Δ | 2 empty);
   cumulative jump menu constant depths 1–12; equals promoted cell + the
   suffix-dead ZCH; ν=1 cells l ∈ {1,2,4}; w ≥ 1 everywhere (no root).
3. **All m=2, b=1 entries with td ≤ 12** (10 entries, types (2,3)…(5,6)):
   BFS w-sets ⊆ W(w_0); menus stabilized at d₀ = gen+2 vs depth 8.
   Sample: w_0 = 4 gives W = {4, 2} (gen 1), w_0 = 6 gives W = {6, 4, 2}.
4. **Closed-form Menu(w)** (§5b ν-determination) ⊇ every swept frame menu.
5. **St 9.6(v) cross-check**: the printed λ=0 family has w ≡ 3/2 (s ≤ 20).
6. **Engine cross-check**: all 26 promoted twopole_check phase-4 shapes
   have w = 2 at every instance (including the ν=1 zch over-generation).
7. **Corrected ZCH case-(III) model**: 403 per-edge solves at td=6, none
   joinable (needs w′ = ν_G·w ∈ W): corrected menu = {IIa (2,3,1)} exactly.

Reproduction: `cd cases && python3 depth_closure_check.py` (exit 0 iff all
pass); `python3 twopole_check.py l1only` for the phase-4 baseline.

---

## 8. Consequence: the finite book, restored

**Theorem (finite jump-vertex book).** For every (m, td), the multi-pole
reduction of Theorem MP terminates in a FINITE book: BOOK(m, td) as in
SHEET6-MP-REVIEW §5c with layer C replaced by

    C′. Chain layer (CLOSED; H1): an M=1 segment is coded, up to
        menu-equivalence, by its invariant w; per entry w_0 =
        a(b(α+β)−1)/(bν) and the finite closure W(w_0) (§4); segments of
        arbitrary depth realize no jump-cell data beyond depth
        d₀ = gen(W)+2 (Lemma §6); M=1-emitting merges map w by
        ·(r+l)/(lν+1) (§5b), composed ≤ m−1 times (MP1).

and layer J indexed by (w, cell) instead of (frame, cell), with the added
filters: join ⟹ equal handshakes; ZCH ⟹ w-ratio ν_e ≥ 2 across edges
(§5c); root cells ⟹ w = 1 − l_f/i₀ < 1 (§5d). Layers E, T, R, S are
unchanged (printed). Every layer is finite: the demoted rider of
SHEET6-MULTIPOLE §0/§5 ("reduces, for each (m, td), to a finite book of
jump-vertex cells") holds with the book so corrected. ∎

Required engine fixes when the book is next run (no promoted conclusion
changes): (i) l1_merges/all_merges: ZCH edges must use the case-(III)
solve (n′ ∈ (1/ν)ℕ*, handshake ν_e·w_e) — the current (a)–(d) model
over-generates (its td=6 extras were suffix-dead); (ii) phase-4
zch_children (ν_F = 1 chain steps) can be deleted (DS1, St 3.16 iff);
(iii) phase-3 root filter can be strengthened to w < 1 (§5d), which also
subsumes the κ̄ < ν pin via case (IV)(j).

---

## 9. Honest perimeter

- **Tier.** DS1 is printed-tier over promoted MP5 (St 3.16 iff + Not
  3.4/3.5 + Def 3.1 + Prop 3.1 + St 3.17(i); the lattice argument in
  DS1(d) is elementary arithmetic of Defs 3.1–3.3). DS2–DS4 are H1
  (Prop 9.3 (a)–(h), (i)–(m) printed-step arithmetic), the tier already
  sanctioned for MP9's root clause and the review's §5a bounds. No new
  hypotheses beyond MP's P1/P2/P3/P4 + H1; E9/H2 not used.
- **Entry edge.** The first step out of a pole vertex with ν_pole = 1
  (Prop 5.5 case (i), pole vertex ∈ V_{2,a}) is grounded as in MP/the
  engines (H1 per-edge use from the entry frame); DS1 applies from F_1
  down regardless. Entry vertices with ν ≥ 2 are themselves V_1 (Prop 5.5
  case (ii)) and need no special treatment.
- **Scope.** The lemma closes the M=1 axis — exactly the F5 demotion. Out
  of scope, as in MP: mixed merges with all μ_e ≥ 2 (m ≥ 3, quarantined),
  the coefficient layer (Prop 8.1(iv) rigid solve vs ratio match, MP §8
  item 3), m ≥ 3 reachability of Theorem O's pattern-level escape, and
  M ≥ 2 suffix chains — though check 5 (St 9.6(v) conserves w = 3/2)
  strongly suggests the same closure mechanism governs the suffix; the
  suffix engine (hiii_compose) is anyway kill-complete per instance.
- **Menus.** "Stabilizes" is proved for the cumulative menu (what the
  book enumerates); per-depth menus can only shed transient-w items after
  d₀, never gain. Caps in the checker (ν ≤ 24/48, l ≤ 8/12, n_pat ≤ 8)
  affect only which INSTANCES are swept, not the menu conclusions, which
  are cap-free via §5b's determination equations; the resonance test
  Δ | num(w) is exact and cap-free.
- **Not claimed.** No bound on segment depth itself (impossible from
  (m, td): §2 R1); no claim that every W-value or menu cell is REALIZED
  by an absolute (f,g) — the book remains conservative (P-realizability
  untracked), exactly as in the promoted engines.

exec
/bin/zsh -lc "sed -n '1,250p' MATHIEU.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# MATHIEU.md — Mathieu–Zhao framing of R_{k,d2}, and the rigidity half of conj:R

Subject: the Mathieu subspace (Mathieu–Zhao) formulation of the residue
functional R_{k,d2} (RESIDUE.md), and an attack on the rigidity half of
paper1 conj:R through it.  Sources read: RESIDUE.md (full), SURPLUS.md,
SURPLUS-EXT.md §§0–1, LEMMA.md, paper1/main.tex §§ variants+functional.
Machine layer: cases/residue_check.py, new `mathieu` mode (§7; exit 0).

## 0. Headline

The Mathieu–Zhao lens does three things here.

1. BRIDGE (§3): with M_A := Im(L_A), L_A := A d/dy − kA′ (the 1-variable
   shadow of ad_{xA}, RESIDUE.md interp (c)), the rigidity half of conj:R
   at (k,d2) is EXACTLY the statement "1 ∉ M_A for every A with
   2 ≤ deg A ≤ d2".  If M_A is a Mathieu subspace, this follows at once,
   because a Mathieu subspace containing 1 is the whole algebra and M_A is
   provably proper.  Derived in full in §3.
2. APPLICABILITY (§4): the outer functional R is an honest Laurent-
   polynomial constant term (machine check M3), so Duistermaat–van der
   Kallen applies literally there — but vacuously.  The inner (rigidity)
   functional lives on a (δ+1)-punctured line, outside every proved
   instance of the MZ program; the Mathieu property of M_A is open (§6).
3. ATTACK (§5): the DvdK MECHANISM — the valuation-at-infinity /
   one-sided-support argument that proves the 1-variable case — applies
   directly to L_A and CLOSES the rigidity half: an elementary,
   coordinate-free proof (Theorem A) that A C′ − k A′ C = 1 with A, C
   polynomials forces deg A ≤ 1, for every k ≥ 1, in characteristic 0.
   Consequently (with RESIDUE.md §4b's uniform outer theorem) conj:R
   holds at ALL cells k, d2 ≥ 2 — including the previously open
   (3,4), (4,4), (5,4) and all d2 ≥ 5.  Status: PROVED + PROMOTED (2026-08-12, MATHIEU-REVIEW.md: all six fronts CONFIRMED; Theorem A real; conj:R closes at every cell k,d2>=2 char 0). Original status: new proof, this file;
   machine-corroborated at every step (§7); NEEDS adversarial review
   before the paper absorbs it (repo practice: LEMMA-REVIEW pattern).

## 1. The Mathieu–Zhao frame

### 1.1 Definitions (Zhao)

Let 𝒜 be a commutative algebra over a field F.  A subspace M ⊆ 𝒜 is a
MATHIEU SUBSPACE (Mathieu–Zhao space) if: for every a ∈ 𝒜 such that
a^m ∈ M for ALL m ≥ 1, and every b ∈ 𝒜, there is N = N(a,b) with
b·a^m ∈ M for all m ≥ N.  Every ideal is Mathieu (with N = 1); the point
of the notion is that M need not be closed under multiplication by 𝒜 —
only powers of "radical-like" elements eventually absorb factors.
Radical language: r(M) := {a : a^m ∈ M for all m ≫ 0} and
sr(M) := {a : ∀b, b·a^m ∈ M for all m ≫ 0}; M is Mathieu iff every a
with all powers in M lies in sr(M).

Trivial but load-bearing lemma (used in §3): if M is Mathieu and 1 ∈ M,
then M = 𝒜.  Proof: take a = 1; then 1^m = 1 ∈ M for all m, so for every
b there is N with b = b·1^m ∈ M.  ∎

### 1.2 The Duistermaat–van der Kallen theorem

THEOREM (DvdK, Indag. Math. 9 (1998)).  Let 𝒜 = C[x_1^{±1},…,x_n^{±1}]
and CT: 𝒜 → C the constant-term functional.  Then ker CT is a Mathieu
subspace of 𝒜: if CT(f^m) = 0 for all m ≥ 1, then for every g ∈ 𝒜,
CT(g f^m) = 0 for all large m.

This is the abelian (torus) case of Mathieu's 1995 conjecture for compact
connected Lie groups, and it is the ONE deep proved instance of the
program.  In one variable the proof yields the sharp support dichotomy:

  (DvdK-1D)  CT(f^m) = 0 for all m ≥ 1  ⟺  supp(f) ⊆ Z_{>0} or
             supp(f) ⊆ Z_{<0}  (f a Laurent polynomial, f = 0 allowed).

The mechanism of the 1-variable proof is a VALUATION argument at the two
punctures 0, ∞: if the support is two-sided, the leading behavior of f^m
at one puncture cannot cancel out of the constant term for every m.
That mechanism — leading-term one-sidedness at a distinguished place —
is what we transport in §5.  (Confidence: statement of the theorem HIGH;
the 1-D dichotomy as stated HIGH on truth, MEDIUM on being verbatim in
the paper.)

### 1.3 Ledger: theorem vs conjecture in the MZ literature

From memory (no web access); confidence labels per line.

PROVED:
- DvdK theorem, all n (above).  [HIGH]
- Zhao's framework papers exist and fix the definitions used here:
  "Generalizations of the image conjecture and the Mathieu conjecture"
  (J. Pure Appl. Algebra 214 (2010)) and "Mathieu subspaces of
  associative algebras" (J. Algebra 350 (2012)).  [HIGH]
- van den Essen–Wright–Zhao: the Image Conjecture for COMMUTING
  order-one operators with CONSTANT leading coefficients (the family
  containing the Gaussian-moment / ∂_i − x_i reformulations of JC),
  and: images of LOCALLY FINITE derivations of C[x,y] are Mathieu
  (J. Pure Appl. Algebra 215 (2011)).  [MEDIUM]
- Muzychuk–Pakovich: solution of the polynomial moment problem
  (vanishing of all moments forces composition structure) — the closest
  proved relative of "all residues of all powers vanish ⟹ structural
  degeneration" on multiply-punctured domains.  [MEDIUM-HIGH]

CONJECTURAL / NOT AVAILABLE:
- Mathieu's conjecture for nonabelian compact G: open.  [HIGH]
- Zhao's Image Conjecture in general: open.  [HIGH]
- Images of order-one operators with NON-CONSTANT leading coefficient
  (our L_A = A∂ − kA′): no proved Mathieu statement I can cite.  [HIGH
  that I cannot cite one; the statement itself is §6's SC1.]
- CT/residue functionals at ≥ 3 punctures (algebra C[y, 1/A], deg A ≥ 2):
  outside DvdK and outside every weighted-CT extension known to me; the
  weighted/twisted CT results in the MZ corpus stay on the 2-punctured
  torus with monomial or Gaussian weights.  [MEDIUM-HIGH]
- Laurent-SERIES analogues of DvdK (completed algebras): status unknown
  to me; not usable as a theorem.  [MEDIUM]

## 2. Our objects: algebras, functionals, candidate M

The campaign's functional (paper1 §functional, RESIDUE.md):
R_{k,d2} = Σ_{j=max(k+2,d2)}^{2d2} (−1)^j C(j,k+2) a2^{2d2−j} b_j,
with three verified interpretations: CT-at-infinity (b), iterated
Grothendieck residue of dP∧dQ/(x^{k+2}A^{k+2}) at the toric boundary
point (a), Koszul moment functional μ spanning the reachable cokernel of
ad_{xA} (c).  Three candidate (algebra, subspace) pairs present
themselves; choosing correctly is most of the work.

(i) OUTER pair — 𝒜 = C[w^{±1}], w = A(y) = 1 + a2·y the edge coordinate
on the binomial locus (a2 ≠ 0), M = ker CT.  Here R is literally a
Laurent-polynomial constant term:
    R_{k,d2} = CT_w( β′(w) · w^{−(k+1)} ),   β(w) := B((w−1)/a2),
equivalently a2^{2d2}·β_{k+2} = (−1)^k R (machine check M3, 12 cells —
this identity also re-derives the max(k+2,d2) lower-limit correction of
RESIDUE.md §1, since C(j,k+2) = 0 for j < k+2 and b_j is absent for
j < d2).  So on the binomial locus the torus normalization is exact and
NO twist blocks DvdK: it applies as stated.  But its conclusions are
eventual-vanishing statements, and on the elements we care about
(one-sided supports in w) those hold for trivial degree reasons; DvdK
gives no leverage on the outer half — which RESIDUE.md §4b anyway proved
uniformly.  The outer half is not where MZ content lives.

(ii) INNER localized pair — 𝒜 = W := C[y][1/A] (the coefficient ring
with the strip's edge polynomial inverted; A = P-column-1, deg A =: δ),
M = Im(d/dy|_W) = ∩_{A(r)=0} ker Res_r(· dy).  This is the right
invariant content: rigidity concerns the powers A^{−(k+1)}, and W is the
function ring of the (δ+1)-punctured projective line (roots of A and ∞).
For δ = 1 and A = y this is (a residue twist of) the DvdK 1-D situation;
for δ ≥ 2 it is outside every proved MZ instance (§1.3).

(iii) INNER polynomial pair (THE BRIDGE FRAME) — 𝒜 = C[y],
    L_A := A·d/dy − k·A′  (multiplication),   M_A := Im(L_A).
L_A is the 1-variable shadow of ad_{xA} on the inner column (RESIDUE.md
interp (c), weight k), and L_A(C) = A^{k+1}·(C/A^k)′.  Note that
ker(R) itself — the hyperplane in the b-coordinates — is NOT the right
M: R is the pairing of the FIXED cokernel functional μ against the
variable inhomogeneity G; the Mathieu structure lives on the μ/image
side, i.e. in M_A, not in one hyperplane of values.

Basic structure of M_A (proved in §3): μ_i ∘ L_A = 0 for the residue
functionals μ_i(f) := Res_{r_i}(f·A^{−(k+1)} dy) at the roots r_i of A —
the global, multi-point form of RESIDUE.md's μ; for squarefree A,
M_A = ∩_i ker μ_i, of codimension exactly δ in C[y].  So M_A is a
finite-codimension residue-kernel subspace — precisely the multi-point
generalization of DvdK's ker CT.

## 3. The bridge theorem

Throughout §§3–5, F is a field of characteristic 0 (see §5.4 for char p),
A ∈ F[y] with A(0) = 1 (units a1 = c1 = 1 scaled out as in SURPLUS-EXT
§0), δ := deg A, and k ≥ 1.

LEMMA B (block ⟺ ODE; the precise content of "rigidity half").  Fix
k ≥ 2, d2 ≥ 2 and a point a = (a2,…,a_{d2+1}), A = 1 + Σ_{i≥1} a_{i+1}y^i.
The d2 − 1 inner extras of the depth-2 block vanish at a if and only if
there exists C ∈ F[y] with support in {y,…,y^{kd2}} such that
    (ODE)   A·C′ − k·A′·C = 1 .
Proof.  Post-gap-kill, bracket Minkowski column k+1, read as a
polynomial in y, is A C′ − k A′ C with C = Q-column-k (SURPLUS-EXT §0,
cross-verified against the independent lattice-determinant enumeration
by surplus_ext.wide_W1).  The pair (A_i, c_j) contributes
(j − ki)·a_{(1,i)}c_j·y^{i+j−1}, so with deg A ≤ d2, supp C ⊆ {1..kd2}:
the y^0-coefficient is c_1 (the vertex equation, = 1 after unit
scaling); the y^{(k+1)d2−1}-coefficient is (kd2 − k·d2)a_{(1,d2)}c_{kd2}
= 0 identically (Prop A's stratum w = 0); and the block keys
(k+1, s), s = 2..(k+1)d2−1 are exactly the remaining coefficients
y^1..y^{(k+1)d2−2} of (ODE).  The triangular solve (col_series, pivots
n+1 ≠ 0 in char 0) uses the equations y^1..y^{kd2−1} to determine
c_2,…,c_{kd2} uniquely from c_1 = 1; the extras are the leftover
equations y^{kd2}..y^{(k+1)d2−2}.  If the extras vanish, the solved C
witnesses (ODE).  Conversely, a witness C of (ODE) with the stated
support is UNIQUE: two solutions differ by an element of
ker L_A = F·A^k (if A K′ = k A′ K then (K/A^k)′ = 0 in F(y), and the
constants of (F(y), d/dy) are F in char 0), and A^k(0) = 1 forces the
difference's constant term — hence the difference — to be 0 when both
have zero constant term.  So the solved series equals C and the extras
vanish.  ∎

BRIDGE THEOREM.  Fix k ≥ 1 and A with δ = deg A ≥ 2.  Then:
(a) (properness) No element of M_A = Im(L_A) has y-degree (k+1)δ − 1;
    in particular y^{(k+1)δ−1} ∉ M_A and M_A ⊊ C[y].
(b) (residue description) μ_i ∘ L_A = 0 for every root r_i of A, where
    μ_i(f) := Res_{r_i}(f·A^{−(k+1)}dy); if A is squarefree,
    M_A = ∩_{i=1}^{δ} ker μ_i, of codimension exactly δ.
(c) (bridge) If M_A is a Mathieu subspace of C[y], then 1 ∉ M_A.
(d) Hence: if M_A is Mathieu for every A with 2 ≤ deg A ≤ d2, then the
    rigidity half of conj:R holds at (k, d2): the inner extras force
    a_{(1,i)} = 0 for 2 ≤ i ≤ d2 ("A binomial").

Proof.
(a) LEADING-COEFFICIENT LEMMA (the engine of everything below): for
D ∈ F[y] nonzero with d := deg D,
    lc-formula:  coefficient of y^{δ+d−1} in L_A(D) = (d − kδ)·lc(A)·lc(D),
and L_A(D) has no coefficient above y^{δ+d−1}.  [Only the top×top pair
(i,j) = (δ,d) reaches i+j−1 = δ+d−1; its weight is (j − ki) = d − kδ.
Machine check M4b, symbolic, k, δ = 1..4, all d ≤ kδ+2.]  So:
if d ≠ kδ then deg L_A(D) = δ+d−1 exactly (char 0: d − kδ ≠ 0 in F);
if d = kδ the top cancels and deg L_A(D) ≤ (k+1)δ − 2.  Now take any
C with L_A(C) of degree (k+1)δ−1: writing C = α·y^{kδ} + (rest), the
y^{kδ}-part contributes degree ≤ (k+1)δ−2 and each other degree d
contributes exact degree δ+d−1 ≠ (k+1)δ−1 with no cross-cancellation at
distinct degrees — the top degree present among the parts survives.
Hence degree (k+1)δ−1 is never attained.  [Machine check M2a.]
(b) μ_i(L_A(C)) = Res_{r_i}((A C′ − kA′C)A^{−(k+1)}dy)
= Res_{r_i}((C/A^k)′ dy) = 0: the residue of an exact rational form
vanishes.  This is RESIDUE.md interp (c)'s "μ ∘ L = 0", globalized from
the binomial locus to every root of every A.  Codimension: L_A maps
F[y]_{≤n} to F[y]_{≤n+δ−1} with 1-dimensional kernel F·A^k (n ≥ kδ), so
dim L_A(F[y]_{≤n}) = n; and no C with deg C > n has L_A(C) in
F[y]_{≤n+δ−1} (by the lc-formula its degree is δ + deg C − 1 > n+δ−1
unless deg C = kδ ≤ n), so Im(L_A) ∩ F[y]_{≤n+δ−1} = L_A(F[y]_{≤n})
has codimension δ in F[y]_{≤n+δ−1}, stably in n.  For squarefree A the δ
functionals μ_i are linearly independent (f = (A/(y−r_i))^{k+1}·(y−r_i)^k
separates them) and annihilate Im(L_A) by the above, so they cut it out.
(c) By §1.1's lemma, a Mathieu M_A containing 1 would equal C[y],
contradicting (a).  So 1 ∉ M_A.
(d) 1 ∉ M_A for all 2 ≤ deg A ≤ d2 says (ODE) has no polynomial
solution when deg A ≥ 2 (the support cap is automatic: any solution has
deg C = kδ ≤ kd2 by the lc-formula, and can be normalized to zero
constant term by subtracting C(0)·A^k, which preserves deg ≤ kδ).  By
Lemma B the inner extras then vanish only where deg A ≤ 1.  Conversely
on the binomial locus C = ((1+a2y)^k − 1)/(ka2) (or C = y at a2 = 0)
solves (ODE) within the support, so the extras vanish there — the
variety of the inner extras is exactly {A binomial}.  ∎

Remark (shape of the bridge).  The mission's expected reduction was
"powers of a unit-type element have eventually-vanishing R".  The frame
that closes is sharper and simpler: the unit-type element is 1 itself,
whose powers are constant — so "eventually" collapses to "now", and the
Mathieu property is consumed exactly once, through "1 ∈ M ⟹ M = 𝒜".
In the localized frame (ii) the same statement reads: rigidity at all
weights simultaneously ⟺ NO power A^{−m} (m ≥ 2) of the unit 1/A of W
lies in Im(d/dy|_W) when δ ≥ 2 — a per-power nonvanishing, which is
strictly stronger than what Mathieu-ness of Im(d/dy|_W) asserts.  This
is the honest reason MZ theorems alone cannot finish: they control
eventual behavior, rigidity needs every power.  The proof in §5 supplies
the per-power statement directly.

## 4. Applicability of DvdK: exact diagnosis

Is our CT form literally a Laurent-polynomial constant term?

exec
/bin/zsh -lc "sed -n '251,560p' MATHIEU.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
- OUTER: YES, with no twist.  R = CT_w(β′(w)·w^{−(k+1)}) on the binomial
  locus (M3).  DvdK applies as a theorem; its conclusion is vacuous for
  our purposes (§2(i)).  No weighted/twisted extension is needed.
- INNER: NO.  Off the binomial locus the natural expansion places are
  the δ roots of A plus ∞; the algebra is W = C[y,1/A], the function
  ring of a (δ+1)-punctured P^1, and the functional is a TUPLE of
  residues (μ_1,…,μ_δ), not one CT.  The DvdK hypothesis that fails is
  the algebra itself: C[w^{±1}] is the 2-punctured case δ = 1.  The
  minimal degeneration is visible already there: for δ = 1 the powers
  A^{−m} (m ≥ 2) DO all lie in ker Res (one-sided Laurent support — no
  obstruction: the binomial locus), while for δ ≥ 2 Theorem A says no
  power does.  The rigidity dichotomy of conj:R IS the DvdK 1-D support
  dichotomy transported to the strip's toric boundary: "1/A behaves
  like a one-sided Laurent monomial ⟺ deg A ≤ 1 ⟺ the edge polynomial
  meets the boundary in at most one simple point".
- Zhao's known extensions (weighted CT, image-conjecture cases with
  constant leading coefficients, locally finite derivations in 2
  variables) all stay on ≤ 2 punctures or constant-coefficient
  operators; none covers L_A = A∂ − kA′ with deg A ≥ 2 (§1.3).  So the
  bridge hypothesis of §3(c) is genuinely conjectural (SC1, §6) — but,
  decisively, it is NOT needed: the DvdK mechanism itself closes the
  problem at the one place where our geometry is still one-sided for
  every A — the puncture at infinity.  That is §5.

## 5. The attack: the rigidity half, proved

### 5.1 Theorem A

THEOREM A (rigidity, all weights).  Let F have characteristic 0, let
w ≥ 1 be an integer, and let A, C ∈ F[y] satisfy
    A·C′ − w·A′·C = c   for some constant c ∈ F, c ≠ 0.
Then deg A ≤ 1.

Proof.  Both A and C are nonzero (else the left side is 0 ≠ c).  Write
δ := deg A, α := lc(A), and suppose δ ≥ 2.

Step 1 (leading-coefficient lemma).  For any nonzero D ∈ F[y] with
d := deg D, the coefficient of y^{δ+d−1} in A D′ − w A′ D is
(d − wδ)·α·lc(D), and no higher power of y occurs.  Indeed the pair
(A_i, D_j) contributes A_i D_j (j − wi) y^{i+j−1}, maximized at
(i,j) = (δ,d).  [Machine check M4b.]  In char 0, d ≠ wδ implies
(d − wδ) ≠ 0 in F, so then deg(A D′ − w A′ D) = δ + d − 1 exactly.

Step 2 (top degree of C).  If deg C ≠ wδ, Step 1 gives
deg(A C′ − w A′ C) = δ + deg C − 1 ≥ δ − 1 ≥ 1 > 0 = deg c,
a contradiction.  Hence deg C = wδ.

Step 3 (kernel element).  A·(A^w)′ − w·A′·A^w = wA^wA′ − wA′A^w = 0.
[Machine check M4a.]

Step 4 (subtract the kernel at top degree).  Let β := lc(C)/α^w ∈ F^×
and D := C − β·A^w.  By Step 3, A D′ − w A′ D = c still; by
construction deg D < wδ.  If D = 0 then c = 0, a contradiction.  If
D ≠ 0 then d := deg D < wδ, so by Step 1
deg(A D′ − w A′ D) = δ + d − 1 ≥ δ − 1 ≥ 1 > 0 = deg c,
again a contradiction.  Hence δ ≥ 2 is impossible.  ∎

For δ ≤ 1 the equation IS solvable (C = ((1+a2y)^w − 1)/(wa2), resp.
C = y at a2 = 0, for c = 1), so Theorem A is sharp; and it is exactly
the "valuation at infinity" DvdK mechanism: ord_∞ applied to
dt = dy/A^{w+1}, t = C/A^w, says t − t(∞) vanishes at ∞ to order
(w+1)δ − 1, which exceeds the map degree wδ as soon as δ ≥ 2 — the
support of the would-be solution is forced one-sided past its own
budget.  (The algebraic Steps 1–4 are that valuation argument made
elementary; no Riemann–Hurwitz needed.)

### 5.2 The rigidity half of conj:R

COROLLARY C (rigidity half, ALL cells).  For every k ≥ 2, d2 ≥ 2, over
any field of characteristic 0: the inner extras of the depth-2 block
vanish at a = (a2,…,a_{d2+1}) iff a3 = … = a_{d2+1} = 0.  Equivalently
V(inner extras) = {A binomial}: the inner column forces deg A ≤ 1.

Proof.  (⇐) On the binomial locus the explicit C above solves (ODE)
within the support {y,…,y^k} ⊆ {y,…,y^{kd2}}; by Lemma B the extras
vanish.  (⇒) If the extras vanish, Lemma B produces a polynomial C with
A C′ − k A′ C = 1; Theorem A (w = k ≥ 2 ≥ 1) forces deg A ≤ 1.  ∎

This settles, structurally and uniformly, the cells proved before by
per-cell work — (2,2) (inner extra −a3^k), (2,3)/(2,4) (squarefree +
A | N(A) divisibility), (3,3),(4,3),(5,3) (resultant certificates
with exponents (15,12),(26,34),(40,44)) — and the OPEN cells
(3,4),(4,4),(5,4) and all d2 ≥ 5, where the perfect-power component of
the divisibility route was the obstacle.  Note how the two halves of
the old argument collapse: perfect powers (1+uy)^δ die by evaluating
(ODE) at the multiple root (0 = 1) — no squarefreeness lemma needed —
and squarefree A of degree ≥ 2 die by Step 4 — no residue divisibility
A | N(A) needed.  The residue condition is bypassed, not solved:
Theorem A proves it could never hold (Corollary E).

COROLLARY D (conj:R, full statement).  For every k, d2 ≥ 2, char 0:
    V(extras) = {A binomial} ∩ ({a2 = 0} ∪ {R_{k,d2} = 0}).
Proof.  Corollary C reduces V(extras) to {A binomial} ∩ V(outer extras).
On the binomial locus, RESIDUE.md §4b (uniform outer theorem, chain
S1–S5; polynomial identities in (a2, b), so valid at a2 = 0 too) gives:
outer extras t ≥ 1 vanish identically and
extra_0 = ±(k+2)/C((k+1)d2, k+1)·a2^{(k−1)d2}·R_{k,d2}, which vanishes
iff a2 = 0 or R = 0 (note (k−1)d2 > 0).  ∎
Dependency note, honestly: §4b's S1–S5 is stated in RESIDUE.md as a
general derivation with each step a short general argument, machine-
verified at 11 cells; Corollary D inherits exactly that status plus
this file's review status.  Corollary C itself depends only on Lemma B
and Theorem A.

### 5.3 The residue dichotomy (the statement MZ was circling)

COROLLARY E.  Let A ∈ C[y] be squarefree with deg A ≥ 2.  Then for
EVERY m ≥ 2 there is a root r of A with Res_r(A^{−m} dy) ≠ 0.  (For
m = 1 all residues 1/A′(r) are nonzero; for deg A ≤ 1 all residues of
all powers m ≥ 2 vanish.)

Proof.  Suppose all residues of A^{−m}dy vanish.  Partial fractions
(simple roots): A^{−m} = Σ_i Σ_{l=2}^{m} c_{i,l}(y−r_i)^{−l} with no
l = 1 terms and no polynomial part; termwise integration gives
g ∈ C(y) with g′ = A^{−m} and pole order ≤ m−1 at each r_i and no other
poles.  Then C := A^{m−1}·g is pole-free, hence a polynomial, and
A C′ − (m−1) A′ C = A^m g′ = 1.  Theorem A (w = m−1 ≥ 1) forces
deg A ≤ 1, a contradiction.  ∎

Corollary E is the exact multi-place analogue of DvdK-1D: "all powers
of 1/A residue-free ⟺ the pole configuration is one-sided (a single
simple point)".  It also explains RESIDUE.md §5's observation that
perfect powers pass the residue test but fail the valuation: the
residue test alone (A | N(A) for k = 2) has the perfect-power
solutions, but the INTEGRATED statement — polynomiality of A^{m−1}g —
never survives past degree 1.

### 5.4 Characteristic

Theorem A as stated uses char 0 twice: (d − wδ) ≠ 0 in Step 1/2/4, and
"constants of (F(y), d/dy) = F" inside Lemma B's uniqueness (and the
triangular pivots n+1).  For the block instance all degrees are capped:
deg C ≤ kd2, |d − kδ| ≤ kd2, pivots n+1 ≤ (k+1)d2 − 1.  So Corollary C
holds over any field of characteristic p > (k+1)·d2 (conservative), in
the spirit of the campaign's per-cell prime exclusions ({2,3,5} at
(2,2), etc.).  In small characteristic Step 2 genuinely fails (deg C
can be wδ + p with vanishing leading weight), consistent with the
Mondello example living in char 2.

## 6. What remains for the MZ program proper: SC1

The bridge hypothesis of §3(c) is now not needed, but it is the
sharpest statement that MZ machinery would settle, and rigidity gives
it evidence.  Recording it precisely:

SUB-CONJECTURE SC1.  (a) Polynomial form: for every A ∈ C[y] squarefree
with deg A = δ ≥ 1 and every k ≥ 1, M_A = Im(A∂ − kA′) =
∩_{i=1}^δ ker(f ↦ Res_{r_i}(f A^{−(k+1)}dy)) is a Mathieu subspace of
C[y].  (b) Localized form: Im(d/dy) = ∩_i ker Res_{r_i}(· dy) is a
Mathieu subspace of C[y, 1/A].

Status: open; not covered by DvdK (wrong algebra for δ ≥ 2: δ+1
punctures) nor by any proved image-conjecture case (non-constant
leading coefficient).  Evidence from this file: (1) Corollary E
computes the full power-behavior of the natural test element a = 1/A in
frame (b): for δ ≥ 2 NO power lies in M (so a imposes no Mathieu
condition — consistency is free but meaningful: a genuinely fails the
membership test at every m, not just at one); for δ = 1 all powers
m ≥ 2 lie in M and the Mathieu conclusion holds explicitly —
Res_r(b·A^{−m}) = u^{−m}b^{(m−1)}(r)/(m−1)! = 0 as soon as
m > deg b + 1.  So SC1 passes every test reachable through powers of
1/A.  (2) DvdK-1D is (a twist of) the case δ = 1 of (b).  A proof of
SC1 for δ ≥ 2 would be the first Mathieu theorem on a curve with more
than two punctures, and this repo's block geometry is a ready-made
consumer; conversely a COUNTEREXAMPLE to SC1 would not damage conj:R
(Theorem A stands independently).

## 7. Mechanical verification (exact arithmetic)

cases/residue_check.py, new additive mode:
    python3 cases/residue_check.py mathieu     (exit 0 = all OK)
Default invocation is unchanged (T0–T5 suite re-run: ALL OK).  Checks,
all exact Fractions, run 2026-08-12, 0.3 s, MATHIEU OK:
- M1 rigidity dichotomy: for k = 1..5, d2 = 2..5, every deg A = δ ≤ d2,
  random/perfect-power/mixed numeric A: inner extras vanish ⟺ δ ≤ 1.
  (Sampled corroboration of Corollary C on and off the repo grid.)
- M2 bridge: (a) y^{(k+1)δ−1} ∉ Im(L_A) — properness witness of §3(a) —
  and (b) 1 ∈ Im(L_A) ⟺ δ ≤ 1, both by exact inconsistency/solvability
  of the full linear system (Gaussian elimination, generous degree cap),
  k = 1..4, δ = 1..4, including non-squarefree A.  The δ = 1 solvable
  control confirms the checker detects consistency when present.
- M3 CT form: a2^{2d2}·β_{k+2} = (−1)^k R_{k,d2} symbolically at 12
  cells (11 repo cells + (2,6)): R is an honest Laurent constant term;
  independently re-derives the max(k+2,d2) lower-limit correction.
- M4 Theorem A's two computational identities, SYMBOLICALLY (generic A
  and D, k, δ = 1..4, all d ≤ kδ+2): L_A(A^k) ≡ 0, and the
  leading-coefficient formula lc(L_A(D)) = (d − kδ)·lc(A)·lc(D) with
  exact cancellation at d = kδ and no overflow above δ+d−1.  With these
  two identities verified, the remaining content of Theorem A's proof
  is integer inequalities (δ + d − 1 ≥ 1, d − wδ ≠ 0).
- M5 per-cell tie at (2,2),(2,3),(3,3),(3,4),(4,4),(5,4),(2,5),(3,5),
  (2,6) — including every previously OPEN cell within reach: symbolic
  inner extras vanish identically on the binomial locus; are nonzero at
  all perfect-power points (1+uy)^δ, 2 ≤ δ ≤ d2 (the historically
  dangerous family) and at random off-binomial points; and the symbolic
  and numeric solve paths agree.

## 8. Consequences and next steps

For conj:R: the conjecture's rigidity half is a theorem (Corollary C),
and with RESIDUE.md §4b the full conj:R variety statement holds at every
cell k, d2 ≥ 2 (Corollary D).  Downstream (paper1 §functional's own
list): no depth-2 block point with all coordinates nonzero for any
k, d2 ≥ 2; pinning-type obstruction only at (2,2); no b-side obstruction
for d2 ≥ 3; no residue condition for k > 2d2 − 2.  The (3,3),(4,3),(5,3)
certificates upgrade from certified computation to structural theorem;
(3,4),(4,4),(5,4) and d2 ≥ 5 close.

For the strip program: every strip-shaped reduced subcase with k ≥ 2,
d2 ≥ 2 now carries the uniform support-rigidity + residue-hyperplane
constraint at depth 2 — the case analysis of SECTION4/coverage can cite
one theorem instead of a cell table.  Unchanged scope limits: strip
hypotheses (gap-kill, full block columns), d1 = 1, no y-axis support;
depth ≥ 3 untouched — though Theorem A is already the homogeneous
engine at every weight w = k+D−1, so the depth-D prediction of
RESIDUE.md §5 (one residue functional per deeper column) should now be
attackable by the same two lemmas.

Recommended next steps, in order: (1) adversarial review of Lemma B +
Theorem A (the proof is 15 lines; the risk concentrates in Lemma B's
block ⟺ ODE identification, which M5 tests at 9 cells); (2) absorb
into paper1 (§ variants shrinks: thm:23/thm:24 rigidity halves and
thm:k3 become corollaries; §functional's conjecture becomes a theorem
modulo §4b's write-up); (3) Lean formalization of Theorem A (kernel +
leading-coefficient argument; small, fits the repo's lean/ practice);
(4) depth ≥ 3 via the weight-w engine; (5) SC1 as a standalone MZ
contribution (first ≥ 3-puncture Mathieu statement), with Corollary E
as its power ledger.

## 9. Files

- MATHIEU.md (this file).
- cases/residue_check.py — `mathieu` mode appended (M1–M5); default
  T0–T5 suite unchanged and re-verified.

exec
/bin/zsh -lc "awk 'BEGIN{p=1} /"'^## 2'"\\./{p=0} p{print}' SHEET6-TEMPLATE.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# SHEET6-TEMPLATE.md — coefficient-level lift of the two-pole rigid template

Status: PROMOTED WITH CORRECTIONS (SHEET6-LT-REVIEW.md: fronts 3-5 confirmed; kill chances (i)/(iv) exponent-trivial so 3 genuine not 5; E11 REFUTED as erratum (follows from Prop 8.1(i)+3.17(i)+8.4, which also forces m_Fs=2 printed-tier); R1 spec SUPERSEDED by LT-REVIEW front 7 redesign: tower g^2 - s0*f^3 per Prop 4.2 (gauge a=0), R6 first, co-stage g, x-side lead, terminal J-closure). Original status: COMPLETE (2026-08-07, UNREVIEWED). Target: SHEET6-L1.md §7.2 — the lift from
Q-data + merge-local coefficients (SHEET6-2POLE.md §6a exhibit, L1c rigid
solution) to an explicit candidate Puiseux/Newton-tree data set for the
distinguished sheet-6 counterexample template, and the edge-by-edge
coefficient consistency sweep (St 3.9 transport). Ground truth:
refs/sigray_full.pdf read on-page. Engine: cases/template_lift.py (new,
additive; exact arithmetic over Q(sqrt 3) via Fraction pairs).

VERDICT: **FORMAL-CANDIDATE — the lift EXISTS and is STRICTLY RIGIDER than
L1 left it.** The coefficient-level sweep does not kill the template; it
(a) proves the naive h-tower reading (m_{F_s} = 1) IMPOSSIBLE by h1-branch
counting (16 <= 7 violation of St 3.11(i)+St 8.3(ii), sec 2c-E2), forcing
approximate-root tower depth m = 2 at the suffix vertex with
(k1,l1) = (3,4) UNIQUE (sec 2c-E3) — h1 = g^2 - s0(f-a)^3 "behaves like
f^{4/3}"; (b) RE-DERIVES the L1c rigid coefficients (a1a2 = sigma^2/6,
b = 2sigma/3) from pure branch counting, independently of the Prop 8.1(iv)
ODE (sec 2c-E4: the h2-collapse W(t) = t(t-b)^3 - (t-a1)^2(t-a2)^2 must
drop to degree 1); (c) passes three further nontrivial kill opportunities
by exact cancellation over Q(sqrt3): pole-lead cancellation m_i^2 =
s0*lam_i^3 automatic, h2-lead transport 27a_i(a_i-b)^3 =
sigma^3(a_i - (3/4)sigma) exact at both poles, every h-branch count
edge-EXACT (leak-free) for h in {f-a, g, h1, h2} on every template edge.
New pinned data: h2 = h1^3 - s1(f-a)^4 with resonant direction
b2 = (3/4)sigma at G_m; pole h1-pattern eta^2 - (4/3)w_i^2; w_i^4 pinned
by the merge data (sec 2c-E5). Bonus: in the minimal-tower branch the
FIRST-STEP merge is restored (m-growth lock, sec 2c-E2). Residual
problem set (sec 3): 6 items, all transport/global-tier, none
vertex-local. Engine: cases/template_lift.py — 11 check families,
46 checks, 0 FAIL, exact arithmetic.

## 0. Setting and conventions

Chain (root at the bottom; ° moves toward the root, + c away from it):

    P_1, P_2  (pole vertices, deepest)      pi = 37/42, kappa = 42
       \   /   two merge edges, mu=(1,1), n=(5,5)
        G_m   (merge vertex, V_{2,a})       pi = 16/21, kappa = 21
         |     suffix edge, mu=2 (IIa k=1), n=10
        F_s   (St 9.6(iii)(A) shape)        pi = 2/7,   kappa = 7
         |     terminal edge, case IV, R = 3, psi = 2
       (0,y)  =: R (root)                   pi = 0,     kappa = 1

Q(F) = (D_F, deg p_F, nu_F, M_F, kappa_F(1-pi(F))): P_i = (2,2,2,1,5),
G_m = (6,12,3,2,5), F_s = (42,126,7,3,5), R = (42,126,1,M_R,1).
Patterns p_{h,F} are the ACTUAL top polynomials of Not 3.10 (specific,
not up-to-constant); "reduced" refers to Prop 8.1's p_F = ⊖p^i,
p_{h_m,F} = p^k q, k = i(mu_F - 1), i = deg(p_F)/M*_F. h-tower
(Prop 4.2, T_a^+ everywhere on the chain since all D > 0): h_0 = g,
h_{j+1} = h_j^{k_j} - s_j(f-a)^{l_j}, (h_j^+)^{k_j} = s_j((f-a)^+)^{l_j}
at vertices where the tower is alive (j < m_F); m_F = the j at which
delta_j := kappa(d_F + d_{h_j,F} - alpha_j d_F - 1 + u) hits 0;
mu_F = alpha_{m_F} = sum_{j<m}(k_j-1)l_j/k_j. All arithmetic below is
exact over Q(sqrt3) (a_{1,2} = (sigma/2)(1 ± 1/sqrt3)).

## 1. The genome: full explicit tree data

### 1a. Exponent ladder and global frame

Global: type (alpha,beta) = (2,3); (k_f,l_f) = (126,42), (k_g,l_g) =
(189,63); deg(f-a) = 168, deg g = 252; td = 6 = Lambda(P_1)+Lambda(P_2)
= 3+3. Branch chart: (0,y)-side Puiseux series y = sum c_j x^{-j},
j in (1/42)N increasing, common root kappa = 42.

Ladder (kappa_F = product of nu's root-to-F; pi from kappa_F(1-pi) =
kappa-bar; d = D/kappa; ALL verified against St 3.17(ii) and the n-data):

| F   | pi(F) | kappa | nu | d_F  | D_F | d_g   | D_g | d_h1 | d_h2  | m_F |
|-----|-------|-------|----|------|-----|-------|-----|------|-------|-----|
| R   | 0     | 1     | 1  | 42   | 42  | 63    | 63  | 56   | 138   | >=3 |
| F_s | 2/7   | 7     | 7  | 6    | 42  | 9     | 63  | 8    | 138/7 | 2   |
| G_m | 16/21 | 21    | 3  | 2/7  | 6   | 3/7   | 9   | 8/21 | 8/7   | 1   |
| P_i | 37/42 | 42    | 2  | 1/21 | 2   | 1/14  | 3   | 1/7  | 3/7   | 0   |

d + d_g = 1 - pi holds exactly at P_i (5/42; Prop 4.1 equality = pole);
delta-table (Prop 4.2): delta_j(P_i) = (0): m=0. delta(G_m) = (10, 0):
m=1. delta(F_s) = (100, 30, 0): m=2. delta(R) = (104, 34, 4, ...): the
root tower continues to depth >= 3 with (k_2,l_2) = (7,23)
(d_h2/d = 138/42 = 23/7); root depth m_R is residual (sec 3, R4).

### 1b. Vertex data (patterns with explicit coefficients)

Scales: sigma (merge), A (suffix), w_1, w_2 (poles), c0 (root direction);
leads S_* (f-a), G_* (g), H_* (h1), K_* (h2); tower constants s0, s1.
a_{1,2} = (sigma/2)(1 ± 1/sqrt3) (a1+a2 = sigma, a1a2 = sigma^2/6,
a1/a2 = 2+sqrt3), b = (2/3)sigma, b2 = (3/4)sigma, B = (3/2)A.

R = (0,y): p = S_R (eta-c0)^126; p_g = G_R (eta-c0)^189, G_R^2 = s0 S_R^3
  (forced, sec 2c-E1); p_h1: mult(.,c0) = 168, level d_h1 = 56;
  p_h2: mult(.,c0) = 414, level 138.
F_s (M* = 21, i = 6, mu = 25/6, k_{h2} = 19):
  p    = S_F [(eta^7-A)^2(eta^7-B)]^6            (deg 126)
  p_g  = G_F [(eta^7-A)^2(eta^7-B)]^9            (deg 189), G_F^2 = s0 S_F^3
  p_h1 = H_F [(eta^7-A)^2(eta^7-B)]^8            (deg 168), H_F^3 = s1 S_F^4
  p_h2 = K_F [(eta^7-A)^2(eta^7-B)]^19 eta(eta^7-A)(eta^7-B)   (deg 414)
  reduced (p,q) = ((t-A)^2(t-B), eta(t-A)(t-B))|_{t=eta^7}, rho = 21/15;
  B = (3/2)A unique (Prop 8.1(iv), L1 family C re-verified).
G_m (M* = 6, i = 2, mu = 3/2, k_{h1} = 1):
  p    = S_M [(eta^3-a1)(eta^3-a2)]^2            (deg 12)
  p_g  = G_M [(eta^3-a1)(eta^3-a2)]^3            (deg 18), G_M^2 = s0 S_M^3
  p_h1 = H_M eta [(eta^3-a1)(eta^3-a2)]^2 (eta^3-b)          (deg 16)
  p_h2 = (sigma^3/27) H_M^3 [(eta^3-a1)(eta^3-a2)]^6 (eta^3-b2) (deg 39)
  reduced (p,q) = ((t-a1)(t-a2), eta(t-a1)(t-a2)(t-b))|_{t=eta^3}; the
  L1c solution, unique given sigma (re-verified).
P_i (M* = 2, i = 1, m = 0):
  p    = lam_i (eta^2 - w_i^2)
  p_g  = m_i eta (eta^2 - (3/2)w_i^2)   [2 p p_g' - 3 p' p_g = 3 lam m w^4]
  p_h1 = -(3/4) s0 lam_i^3 w_i^4 (eta^2 - (4/3)w_i^2)   (deg 2; sec 2c-E5)
  p_h2 = (p_h1)^3 = [-(3/4)s0 lam_i^3 w_i^4]^3 (eta^2-(4/3)w_i^2)^3 (deg 6)
  with m_i^2 = s0 lam_i^3 (forced AND automatic, sec 2c-E5).

### 1c. Edge data (n, mu, i, case labels, free dead-stretch coefficients)

| edge      | n  | steps at 1/kappa_G | mu | Prop 9.3 | free coeffs (grid) |
|-----------|----|--------------------|----|----------|--------------------|
| R->F_s    | -  | 2 at 1/7           | 6* | IV (terminal read up) | none (no integer in (0,2/7)) |
| F_s->G_m  | 10 | 10 at 1/21         | 2  | II(a) k=1, l=0 | 3 at 9/21,12/21,15/21 |
| G_m->P_i  | 5  | 5 at 1/42          | 1  | II(a) k=0, l=1 (merged IIa(3,1)) | 2 at 17/21,18/21 |

n == -kappa-bar mod nu checks: 10 == 1 mod 3, 5 == 1 mod 2; off-grid
intermediate coefficients vanish (a nonzero one would relocate the
characteristic exponent and change Q); on-grid ones are free template
parameters (7 total). *mu on R->F_s: mult(p_R, c0)/M*-bookkeeping at the
root; the terminal step is case IV with R = deg p_{F_s}/d_R = 3, psi = 2.

### 1d. Branch/puncture bookkeeping (y-side)

126 = k_f series: puncture P_1 (x-degree 42, all 42 conjugate series,
g-pole order 3), P_2 (same), B-side punctures totaling 42 series (6 per
eta-direction of the B-orbit at F_s; g finite there; carriers of the
lambda_{F_s} = 2 charge). Conjugacy audit: mu_42-action distributes P_i's
42 series as 7 x 3 x 2 over the (A-orbit x a_i-cube-orbit x ±w_i) tree
directions — deg p at each vertex = series through the prefix: 126/12/2
check exactly. h1-directions with NO f-branch: b-orbit at G_m (3
directions, 1 h1-series each, +1 at the eta = 0 direction: 12+3+1 = 16 =
deg p_{h1,G_m}); h2: b2-orbit (36+3 = 39). x-side: l_f = 42 series,
carries the psi = 2 charge (not modeled here; residual R5).


exec
/bin/zsh -lc 'tail -n 150 notes.md' in /Users/dc/code/math/jc72108
 succeeded in 0ms:
  the vertex-gap theorem in the (2,2) regime — awaiting DC's go-ahead per the
  standing no-paper-drafting instruction.
- ZHEGLOV-SCOPE.md: architecture mapped (GGV reduction -> head-chopping
  induction S4 -> string-equation transport S5 -> distinguished-coefficient
  contradiction S6). Top risk: S6 Steps 4-7 (rewritten in v4 AND v5) + the
  N-independence lemma. Machine audit lane ~45-75 agent-hours; expert lane
  3-5 weeks; paper under journal review (v5 thanks referees). Cheapest
  falsification (2-3h): random exact test of Lemma L:polynomials — launching.
- Zheglov T1 falsification test: Lemma L:polynomials PASSED 640/640 exact
  instances (4 regimes, 9 non-vacuous solvable cases matching deg H formula,
  48/48 solver controls). Kill-shot missed -> small confidence bump for S4;
  risk mass unchanged at S6 Steps 4-7 + N-independence. HOLDING at T1 (T2
  replay = 15-25 agent-hours, off critical path; escalate on anomaly or if
  DC(1) needed as citable). Artifacts: ZHEGLOV-LTEST.md, tests/ltest_*.py.
- SHEET6.md (P5): GO verdict — degree 6 ≈ 150-400 mechanizable exact-arith
  verifications (weeks-scale fan-out); wall (td 9 / bidegree (48,64)) is
  ABOVE 6. FOUND: Sigray 2008 thesis = independent degree-5 proof (RECON
  corrected). Caveats: both foundations unaudited; Żołądek gcd gap (GGV-
  documented). Pilot launched: machine-rederive Sigray Prop 9.1 + Stmt 9.6.
  USER ACTION WANTED: Żołądek PDF is CAPTCHA-walled — manual download needed.
- DC2-PROGRAM.md (P2): port-of-Zheglov blocked at step zero (centralizer
  rigidity collapses in A_2; prerequisite = 2D Schur-pair/Parshin theory,
  Zheglov's own open program; no Z^4 subrectangular reduction — vertex-gap
  slot). EXPERIMENT: DC(2) PROVED in Bernstein degree <= 2 (8s exact;
  deg-2 slice 0-dim of degree 90 = Lagrangian-cubic family over LGr(2,4) —
  geometry match; 5/5 operator-level certificates). Divergence at degree 3 =
  tier-1 next slice, queued. Full DC(2): unreachable at present.
- SHEET6-PILOT: Prop 9.1 exact PASS (11/11 rows, completeness certificates).
  Stmt 9.6 DISCREPANCY: thesis row (75,51) fails its own equation (p.52
  arithmetic slip, never-refereed source) — corrected statement drops the
  case, STRICTLY STRONGER; survivors {(21,15),(20,16)} verify. Degree-6 leaf
  table already emitted by the enumerator: 14 rows (< SHEET6's 20-30 est).
  Remaining for td=6: Props 9.3(e)-(m), lambda-budget, termination assembly.
- SURPLUS-EXT Phase C: surplus-4 variant THEOREM at (2,3) (dual proofs:
  resultant w/ constant lead + structural divisibility); torus-emptiness also
  proved at (2,4); rigidity certified (3,3),(4,3),(5,3). Pattern exact:
  leftovers = 2(w_P-1). DISCOVERY: log-residue functional R_{k,d2} =
  sum (-1)^j C(j,k+2) a2^(2d2-j) b_j survives per cell — PINS is its 1-term
  case; conjectured all k>=2,d2>=2; open (3,4),(4,4),(5,4),d2>=5. Erratum:
  scan's torus-solvable wide cells were numeric false positives (fixed in
  SURPLUS.md). Coverage: 0/34 current families in wide cells (theory
  completeness + beyond-150 relevance). P1 avenue now fully delivered:
  theorem grid (2,2),(2,3),(2,4) + k>=3 impossibility + coverage table.
- 2026-08-06 DECISION (DC): third replication of subcase (1) deprioritized —
  the deep cross-check (verified replays + closed gaps + 3-way transcription
  agreement) makes our own c1 Groebner runs evidentially marginal. Paper 2
  division: s2 ours end-to-end; s1 = external artifacts + our audit thereof.
  jc-b STOPPED. AWS Xeon Z-leaf + ultramem full-memory I-leaf continue as
  72h sunk-cost bonuses, then roll into sec4 Phase 2c / farm work.
- Xeon all-Z leaf FAILED at 940GB after 30h — every c1 leaf now exceeds 1TB.
  Xeon stopped (on-demand $, no viable leaf work); restarts for sec4 Phase 2c.
  Sole remaining bonus attempt: ultramem single-lane 1.7TB on I-leaves.
- 2026-08-07: leaf program CLOSED (DC directive: novelty only). 8TB moonshot
  declined (~15% x replication value). Capacity reorganized: farm dispatch on
  review+driver gates; R residue-interpretation agent launched; sheet-6 build
  next slot; DC(2) deg-3 slice after. Lifts continue (paper obligation).

## 2026-08-07 (loop): residue theorem lands; farm gate-complete; leaf retired
- **RESIDUE.md committed (e67c50a)**: R_{k,d2} IS a Grothendieck residue — iterated residue of dP∧dQ/(x^{k+2}A^{k+2}) at the toric boundary point {P=0}∩{x=0}. Three interpretations verified by exact arithmetic on 11 cells (48 checks): CT/contour form, Grothendieck form, Koszul moment functional spanning the reachable cokernel of ad_{xA}. Naive dP∧dQ/P^{k+2} refuted (exact form, residue ≡ 0). Uniform theorem all k,d2≥2: surviving outer extra = ±(k+2)/C((k+1)d2,k+1)·a2^{(k-1)d2}·R — explains every mystery unit (5,21,55,99,1001,364) as moments at top pivot; replaces per-cell certificates. conj:R now = its rigidity half only. Correction: sum starts j=max(k+2,d2).
- **Farm Phase 3 gate-complete**: driver agent hit the account credit ceiling (resets Aug 8 8pm PT) but deliverables were on disk; I ran gates locally — ALL FARM TESTS PASS incl GF6 (dry run reproduces S4 archives, 22 files byte-identical incl char 0, pivot product == AUDIT.md) and GF7 (dispatch covers 28 systems, balanced loads). deg≤150 sweep emission running locally under FLINT (13/~30 families done).
- **Ultramem I-leaf retired** (scp-script pattern beat the ssh-255 flake): lane4+msolve killed, cron removed. Rationale: replication, not novelty (user directive). cCa2/cCa6 Singular lifts untouched, still resident (~114 GB).
- **Blocked on credits until Aug 8 8pm PT**: sheet-6 case-bash build agent, DC(2) degree-3 slice agent. Local script work unaffected.

## 2026-08-07 (loop, later): deg<=150 sweep DONE; farm dispatch underway; credits restored
- Sweep final: 34 families, 62 .ms files (4.5 GB, largest 565 MB), 22 emitted-system cases + partials/cores. NOT COVERED (reduce4 STUCK, psi_j precondition / multi-root chain edge): 12_36mn23d144_r0-r2, 6_15mn27d147, 10_40mn32d150_r0-r1 — these stay open regardless of farm verdicts; candidates for a reduce4 extension later. PARTIAL/CORE emissions are valid (cascade steps are equivalences); they're just less reduced.
- Queues: --queues 2 -> box01 31 jobs/2.6GB, box02 31 jobs/2.2GB. Runner sorts smallest-first for early verdicts; NO guest poweroff (FARM_DONE marker + control-plane stop).
- Fleet: claude-x8i-3 restarted (new IP 54.175.21.169, 64c/991GB, msolve OK) <- box01 rsync in flight. jc-b restarted (32c/960GB, crontab wiped clean, msolve OK) <- box02 tgz in flight. ultramem-1 continues lifts only.
- Credits: user purchased more; probe confirmed live. Launched queued agents: sheet-6 case-bash build + DC(2) degree-3 slice (both in flight).
- Driver agent retired (its gates I re-ran locally: ALL FARM TESTS PASS, GF6 byte-identical vs S4 archives, GF7 dispatch cover).
- 2026-08-07: FARM LIVE — box01 (AWS Xeon 64c) + box02 (jc-b 32c), 62 jobs total, smallest-first; first EMPTY verdicts already in.
- SHEET6-CAMPAIGN.md: td=6 case-bash PHASE 1 COMPLETE. Built generic propagation
  engine (cases/sheet6_campaign.py; gate reproduces pilot exactly): ratio-eq
  Diophantine solver for all Prop 9.3 branches (I, IIa k>0/k=0, IIb, III) x mu|M,
  s-free reduction of parametric families w/ PIT certificates + s-shift, residue
  splitting, ceil-lambda budget BFS (Sigma lam <= td-2). Lambda<=7 table: 14 rows.
  VERDICTS (single-pole, conditional H1-H4+H3): td=6 rows 2,3 (both (2,3)-type)
  EXCLUDED; rows 6,8,9,11 reduce to ~14 case-III parametric s-tails (all s<=5
  instances die) + IV-terminals awaiting the root-kill H3. Two-pole 3+3 config
  OPEN (Prop 8.4 single-pole only). NEW THESIS ERRATA E2-E4: St 9.8/9.9/9.10
  "no solution"/"M_F=1" claims false (3nu=4m+1, 2nu=3m+1 families exist, lambda=0
  self-loops, M_F=2 via gcd(2nu,nu+1)). AUDIT FINDINGS: St 9.12's stated kills
  cannot close its own case-IV terminals (unstated root-kill = our H3, load-
  bearing G2); thesis silent on td<=5 rows 1,5,7,10 (rows 1,7 we closed
  mechanically; 5,10 have the same III-tails) => Sigray td>=6 proof INCOMPLETE
  as printed (JC td<=5 still safe via Orevkov/Domrina/Zoladek). Next: H3 audit
  (blocking, days), III-tail closure (~15 lemma-sized, 1-2h each, mechanizable),
  St 3.16/3.18 III-admissibility extraction (may kill all tails at once),
  two-pole analogue. Nothing farm-sized; all runs seconds-to-minutes exact.

## 2026-08-07 (loop, evening): P5+P2 build agents landed; reviews launched; farm grinding
- SHEET6 campaign (4835b13, UNREVIEWED): engine reproduces pilot; Lambda<=7 = 14 rows; td=6 rows 2,3 EXCLUDED; ~15 case-III s-tails + IV-terminals gated on H3 (root-kill). HEADLINE CLAIMS: 3 new thesis errata (E2-E4, lam=0 self-loop families the thesis says don't exist), G2 (St 9.12's kill set can't close its own IV-terminals — unstated H3 load-bearing), G3 (thesis silent on rows 1,5,7,10 => Sigray td>=6 INCOMPLETE AS PRINTED; td<=5 safe via Orevkov/Domrina/Zoladek). If review confirms: sheet-6 exclusion is genuinely open => our campaign = novel work, and RECON's "independent reproof" language needs qualification.
- DC2 degree-3 slice (1eb53b0, UNREVIEWED): 120 unknowns, 420 quantum/414 classical eqs; gate reproduces degree-2 exactly. HEADLINE: quantum corrections = 90 independent directions; at rational family points quantum corank 13 vs classical 14, rank exactly 1 on classical tangent => first measured DC/PC divergence (one scalar quantum obstruction kills one classical modulus). DC(2) consistent with HOLDS at D<=3. D=4 = 260 unknowns, big-box fibers.
- Adversarial reviews launched in parallel: SHEET6-REVIEW.md (vs sigray_full.pdf ground truth) + DC2-REVIEW.md (truncation-artifact attack prioritized).
- Farm: both boxes 4 verdicts each (all EMPTY so far), now grinding 4_12mn34d64_c2_core (35+ min in). 
- 2026-08-07 late: III-extraction landed (e5d42e7): E5 lambda-bound + N1 kill 10/13 td6 s-tails for ALL s; r6,r9 excluded mod H3+H5; G3 rows 5,10/M2 closed; 9 residual classes remain + IV-terminals (H3 agent still out). Combined H3+III adversarial review queued for when H3 lands.
- 2026-08-07 night: COMPOSITION LANDMARK (SHEET6-HIII-REVIEW.md): psi-budget CONFIRMED (G2 closed for real), E5/N1 CONFIRMED (+p.53 subscript-slip corroboration in thesis), composed engine gives td3:0 td4:0 td5:2 td6:13(AF3-superset)+1(SF1). Sanctioned td=6 table FULLY EXCLUDED mod {H1,H2,H4,AF2,AF3,H5a/b}+H3q — beyond what the thesis proves as printed. AF2-IIb pricing audit would kill both td5 residuals. Next: AF2-IIb audit + two-pole (3,3) config agents.
- 2026-08-07 latest: AF2-IIb DERIVED (no free reading); td<=5 sanctioned residual now 0, td6 down to 4 AF3-ext classes + two-pole (agent out). Errata count E1-E7. AF2 badge system retro-validated. Combined AF2+2POLE review queued when two-pole lands.
- 2026-08-07 night 2: TWO-POLE NOT EXCLUDED (284d847): exhibit survives with slack 1; 3 residue + 9 IV survivor classes; td=6 hinges on L1 (merged-pattern l>=1 inadmissibility). Launched combined AF2+2POLE adversarial review + dedicated L1 attack in parallel. THE FORK: L1 holds => td=6 theorem; L1 fails => counterexample template at the (3,3) merge.
- 2026-08-07 night 3: A2P review passed (8f3364f) — AF2 promoted as-is (E6 proven at proof level: thesis's own middle identity false + all p.53 usages compute the minus version); 2POLE promoted with fixes (derived-IIb default => book 2 residue + 6 IV; M_pole=gcd(P,P_g) pin kills residue B => TRUE survivor set = residue A + 2 boundary classes). In flight: L1 (fork-decider), AF3 sanction (last 4 single-pole classes).
- 2026-08-07 night 4: L1 PARTIAL (62335cc): merged pattern squeezed to 3 shapes via pin-propagation (mu=(1,1),k=0,lam=0); 2 of 3 proved empty; the third (IIa nu=3,l=1) is COEFFICIENT-CONSISTENT with explicit unique solution a1/a2=2+sqrt(3) — two-pole funnels to unique merged child (6,12,3,2,5)@lam0. Survivor book now: single-pole 4 r9/M2 (AF3, thesis-forced) + two-pole A + 4 IV classes on the rigid template. Closing needs global h1-branch accounting or Puiseux transport (beyond printed thesis). Combined AF3+L1 adversarial review launched. THE PICTURE: td=6 sheet-6 is one rigid coefficient template away from either a theorem or a counterexample search target.
- 2026-08-07 night 5 (905db83): A3L1 review — ALL FRONTS CONFIRMED, both promoted. CANONICAL BOOK: td<=5 CLOSED (0 survivors, independent of AF2); td=6 = 4 single-pole r9/M2 (thesis-forced entries) + two-pole residue A on the unique rigid template (merged child (6,12,3,2,5)@0, a1/a2=2+sqrt3). Endgame agents launched: (1) lam_root>=1 ledger attack (cuts 8->4), (2) coefficient-level template lift (genome -> edge consistency -> formal candidate or death edge; sizes farm computation if candidate). Errata E1-E9, five proof-level.
- 2026-08-07 night 6: LROOT decided (SHEET6-LROOT.md, UNREVIEWED): lam_root>=1 REFUTED — stronger, lam_root = 0 is FORCED at every case-IV terminal (IV's own hypothesis (0,y) ∉ V_2a = "single root direction" by Def 3.4, so NO branch leaves the chain at the root; the psi-charge lives in the OTHER tree component (St 3.3) so no double-charge was ever possible, but no y-side root unit exists either). Full Prop 7.5 (22) Euler-ledger itemized and BALANCED at 0 root-lambda for all 8 survivors (engine cases/lroot_ledger.py, exact, asserts; gates untouched PASS). Book STAYS 8. Positive yield: (i) every carrier forced to a single x-side cv vertex, kappa_G=1, x-side one unsplit Puiseux cluster below height R>=3 (2 vertices or kappa>=2 blow the budget) — new pin for the template lift; (ii) the 4 slack-0 classes are TOTALLY rigid: x-mass exactly psi=R-1, orbit cv masses exactly the (24)-prices, delta_a = 0 on EVERY fiber of the pencil; (iii) L1's merge blind spot re-derived from the budget side (resonant q-orbit direction carries no punctures => empty ledger row). New erratum E10 (St 3.15 (i)/(iii) labels swapped; thesis usage consistent with the swap). Surviving attack surfaces, precise: delta-strictness at mult>=2 direction collisions (would kill all four slack-0 at once — Prop 7.3 equality question, not printed), x-side-pin vs template realizability, h1-branch budget.
- 2026-08-07 night 7: TEMPLATE LIFT decided (SHEET6-TEMPLATE.md, UNREVIEWED): FORMAL-CANDIDATE — the coefficient-level lift of the two-pole rigid template EXISTS; no edge dies. Genome fully explicit (kappa=42 ladder pi=0,2/7,16/21,37/42; all f/g/h1/h2 patterns at R,F_s,G_m,P_i; 2 punctures x 42 series + 42 B-side = k_f 126). Sweep highlights: (i) h1-branch count (St 3.11(i)+8.3(ii)) KILLS the naive tower reading m_{F_s}=1 (16<=7) and forces approximate-root tower (k0,l0)=(2,3),(k1,l1)=(3,4) UNIQUE (h1 ~ f^{4/3}); supplies the missing proof of St 9.6's silent i=deg(p_G)/M_G (erratum candidate E11); (ii) h2-collapse W(t)=t(t-b)^3-(t-a1)^2(t-a2)^2 must drop to deg 1 — forcing EXACTLY b=2sig/3, a1a2=sig^2/6: the L1c rigid coefficients RE-DERIVED from branch counting, independent of the 8.1(iv) ODE; (iii) three more kill chances pass by exact identity: pole-lead cancellation m_i^2=s0*lam_i^3 automatic, H^3=s1*S^4 transport closes via c_m^7=A, h2-lead pole identity 27a(a-b)^3=sig^3(a-3sig/4) exact over Q(sqrt3); (iv) all 12 (edge,h) count/d-ladder cells EXACT (leak-free); (v) minimal-tower branch forces FIRST-STEP merge (m-growth lock; 2POLE 7.3 restored). New pinned data: b2=(3/4)sig h2-direction, p_h1,P=eta^2-(4/3)w^2, w_i^4 formulas, h1-corner (168,56). Engine cases/template_lift.py: 46 checks 0 FAIL. Residuals R1-R6: cancellation depths (R1, decidable by staged linear system ~10^2-10^3 unknowns, hours-days on farm — the cheap decisive experiment), h-Newton budgets/x-side (R2, merge with LROOT pin), cv realizability (R3), root tower depth>=3 with (k2,l2)=(7,23) + M_R (R4), Jacobian closure (R5), deeper-tower window 4/3<l1/k1<3 (R6, same mechanism recursively). td=6 now rests on R1-R6; naive 17.6k-var msolve Ansatz ruled out, template-constrained staging sized and buildable on lib/jc.py.
- 2026-08-07 night 6 (3f06c21): TEMPLATE = FORMAL-CANDIDATE, no edge dies; L1c coefficients re-derived independently via h2-collapse (convergence of ODE + branch-counting routes). lam_root REFUTED (c8f8bc8, ledger balances at 0 for all 8). Final night review launched (LROOT+TEMPLATE + R1 GO/NO-GO gate). If R1 gates GO: build the staged linear system over Q(sqrt3) — the cheap decisive experiment on the counterexample template.
- 2026-08-07 night 7 (c4624ff): LT review promoted LROOT+TEMPLATE (E11 demoted: printed-tier derivable; 3 genuine kill chances). R1 gated REDESIGN-then-GO; R1 agent launched with the 4 mandated fixes (tower g^2-s0*f^3 gauge a=0, R6-first, co-staged (f,g)+x-side lead, pre-registered J-closure interpretation). Pre-registered: R6 empty + R1 UNSOLVABLE = two-pole td6 template DIES (theorem-grade); R1 SOLVABLE = formal candidate deepens toward R2-R5. This is the decisive experiment.
- 2026-08-08 ~02:15: FOUR worker-agent stalls in a row (R1 x3, R6 x1; probe agents fine — infra issue with long worker streams tonight). Took R1/R6 inline: R1 redesign spec distilled+banked into SHEET6-R1.md; R6 layer-1 ledger done (73504ad): 8/8 integral, (2,3)+(2,5) reproduce the E2-killed i=2 geometry, 6 cases pend layer-2 pattern counts (Prop 8.1(ii)/4.2 m=2 forms). Morning plan: retry R6-layer-2 agent, then R1 build. Farm grinding (box01 6 verdicts). Sleeping long.
- 2026-08-08 (456c634): R6 CLOSED — all 8 deeper-tower window cases DEAD (six at merge transport, two at h2 pole-edge count). m_Gm=1 minimal genome forced; R1 now decisive for the whole residue-A configuration. Agents recovered (R6 layer-2 ran clean, 17 min). Launched in parallel: R6 adversarial review + R1 staged-system build (pre-registered interpretation). Farm: next poll due.
- 2026-08-09 early (5df68d2): R6 print campaign CLOSED — 6/9 window cases dead; survivors {minimal (3,4), (1,2), (2,3)-chain(6,17), (2,5)-chain(6,23)} SURVIVE-IN-PRINT (nothing printable kills them). R1 must enumerate 4 branches ((1,2) delta-spec written: one extra staged resonance level at G_m). When R1-build lands: extend to 4-branch enumeration, then ONE review over echo-rung + R1 before interpreting. Bonus pin a2/a1 = 2±sqrt3.
- 2026-08-09 (f29eafd): R1 CAP-2 CORE EMPTY — GB=[1], char 0, 5s on ultramem (118 vars, 64 eqs, underdetermined-yet-infeasible = deep clash signature). IF faithful (review a9bb… in flight, incl. minimal-infeasible-subsystem extraction + hand re-derivation): minimal-tower genome DEAD; remaining branches (1,2), (2,3)-chain, (2,5)-chain need own cores; all four dead => residue-A EXCLUDED => td=6 = 4 single-pole classes only.
- 2026-08-09 (d434895): R1 EMPTY RETRACTED — spurious doubly (msolve 0.10.1 silently mis-parses parenthesized input; system a-priori satisfiable; 57/57 shipped rows were silent truncations, zero discriminating rows). AUDIT: 401-file paren sweep — ONLY the r1 core affected; all (72,108)/farm/dc2 verdicts stand (our emitters expand fully). Emission rules hardened in AUDIT.md. Rebuild agent launched (4 mandates: paren-free, sentinel fix + discriminating rows, guards, verdict discipline; sibling-branch cores if cheap). Echo-rung work CONFIRMED by same review — R6 4-branch state stands.
- 2026-08-09: R1 full-degree cores DISPATCHED to ultramem (sequential: w-free p-screen -> full p-screen -> char-0 decisive -> (1,2) sibling). All guards passed pre-flight; runner has verdict authentication. This queue IS the decisive experiment for 2 of 4 residue-A branches.
- 2026-08-10: user restarting local machine. All 3 remote workloads nohup'd (ultramem R1 queue+lifts w/ cron; box01 farm; jc-b farm — jc-b was ssh-255 at last poll, re-check on resume). On session resume: re-arm /loop, poll all three.
- 2026-08-10 (post-reboot resume): jc-b was TERMINATED (preemption) — restarted, farm resumed cleanly (9 banked outputs kept, re-running the killed core.q). Box01: 6 EMPTY / 6 FAILED (big char-0 cores OOM-class; triage tier owed after queue drains). Ultramem R1 w-free p-screen ~1 day in, 1.07TB resident, alive. No LIFT-CERT yet. Loop re-armed.
- 2026-08-10 (08fbbda): TD-UNIFORM entry theorem landed (UNREVIEWED, review launched): pinned M = b; PRIME td => all single-pole rows b=1 => excluded at entry, uniformly (scan verified td<=40; td=37: 8/8 dead). Composite residual grows (212 survivors at td=16); td=9 slack-6 chain shows budgets saturate; bottleneck = multi-pole 8.4 analogue. If review holds: JC2 geometric-degree ladder at prime td rests entirely on multi-pole configs. R1-acceleration agent still out.
- 2026-08-10: TDU fully settled — PRIME THEOREM promoted (single-pole dead at entry for every prime td, perimeter H1/AF3-tier); composite table authoritative (212 survivors at td=16, lower bound); bottleneck = multi-pole 8.4 analogue. My td=9 'discrepancy' was a display-truncation miscount, caught by reconciler.
- 2026-08-10 (c8f2cb0): R1 REDUCED queue live on ultramem (49 rows/63 vars, verdict-equivalent, soundness-proven). Old 128-var run killed per acceleration agent's recommendation. Sweep calibration: GB deep at every char (12 primes all timeout locally) — this is a real computation even reduced. Chain folds still grinding locally toward the (2,3)/(2,5) cores.
- 2026-08-10 (353ed0d): CHAIN CORES LANDED. (2,5)-chain core NONEMPTY at p AND char 0 (487-elt GB, origin excluded) — the branch DEEPENS; deep-dive agent launched (dimension, degeneracy split, deferred-row evaluation: real template data vs artifact — this decides the counterexample frontier). (2,3)-chain core queued on ultramem behind reduced minimal queue. Byte-identity gate passed on the fold/CRT pipeline.
- 2026-08-10 evening: (2,5) locus REAL (dim 27, nondegenerate, explicit point) but deferred rows refute sampled points at rung 10 — rung-extension decides. SECOND msolve hazard (unreduced mod-p coefficients => silent corruption): 110 shipped files affected, verdict-contamination audit agent running (expected clean: c1 leaves never yielded accepted verdicts; (72,108) rests on char-0 + external artifacts).
- 2026-08-10 late: OPS SAGA RESOLVED — box01 root disk was 6.8GB (!), filled during box02-fold: EBS resized to 100GB (grown live, no downtime for the running job); truncated extracts purged; fold re-shipped; jc-b RETIRED after 3rd preemption (queue folded into box01 as lane 2, MEMGB=300/T=32, dual-lane). All 27 corrupt-class farm files replaced by round-trip-guarded reduced twins on box01; all previously banked box verdicts verified clean (W-class or char-0). (2,5) rung-extension decision runs still grinding locally.
- 2026-08-10 night: (2,5) rung-extension decision runs died locally (macOS mem-kill + 3000s timeout at 4 threads); shipped to ultramem as parallel runner (24 threads, 300GB cap, alongside the big reduced screen at 1.4TB+). Queue: ext_p105337 -> ext char-0. THE branch decider now runs on proper hardware.
- 2026-08-11 early: minimal-branch reduced wfree screen DIED at 1.5TB cap after 34h (no verdict); killed the auto-advanced (strictly bigger) full-p run; ultramem now dedicated to (2,5) ext decider (28h in). Minimal branch pivots to CHART DECOMPOSITION (agent launched: split reduced core into 4-16 guarded leaves w/ cover certificate, local calibration). The monolith era is over for this system class — decomposition always wins (campaign lesson, again).
- 2026-08-11: ULTRAMEM TERMINATION ROOT-CAUSED — not Spot preemption: the STALE jc_deadline poweroff cron (leaf-era) fired (deadline passed 25 min before death). Cron removed permanently. Cost: 28h of (2,5) ext compute. Recovery: ext decider MOVED to box01 (on-demand, 16 threads, 250GB cap, alongside farm lanes); (2,3) chain queue launched directly on ultramem (40 threads); lifts resumed. STANDING LESSON (2nd occurrence): guest lifecycle machinery must be inventoried and wiped on every box reuse — added to ops checklist.
- 2026-08-11 (e8839bb): minimal core decomposed (4 leaves, 1s each — monolith was foredoomed by relaxation artifact); UU chart NONEMPTY everywhere, core collapses to one conjugate-pair relation satisfied identically by template data. NO branch killed at core level yet — all discriminating content is in deferred bands. Minimal-branch ext build agent launched (mirrors (2,5) ext, in UU chart, with witness guard). Deciders running: (2,5) ext on box01, (2,3) chain on ultramem. (1,2) core to get the 4-leaf treatment after.
- 2026-08-11 ~05:00: minimal-ext DECIDED — branch survives entire in-window F_s band by explicit witness (all 323 eqs at 2 primes); next tier = depth-84 quotient (farm-scale, needs sizing). SURVIVOR PATTERN NOW UNIFORM: no two-pole branch dies at any accessible tier; discriminating content keeps receding deeper (depth-84 / R2-R5 / J-closure). Morning queue: depth-84 sizing, (1,2) 4-leaf, deciders.
- 2026-08-11 morning: Q0 PASSED — F_s ladder EXHAUSTED, minimal branch survives by explicit point (3913087). BUT the witness has s1F=0, and the tower tie H_F^3 = s1F*S_F^4 may force s1F != 0 — flagged as front 2 of the consolidated ladder review (sec 13-16, in flight). R2 build held pending that verdict. Deciders: (2,5) ext + (2,3) chain both ~23h in.
- 2026-08-11 (31f8309): LADDER REVIEW INVERTED THE VERDICT — survival was s1F=0 artifact; saturated Q0 = EMPTY both primes: minimal branch intended locus DIES at depth 84 (strong evidence, char-0 pending). Same artifact in (1,2). Saturated-rebuild agent launched (scale inventory + Rabinowitsch rows + E5/E6 tie emission + pattern-positive anchors; per-branch honest verdicts; char-0 upgrade attempt). If saturated kills hold at char 0 across minimal + (1,2), residue-A rests on (2,5)/(2,3) chains alone. The review protocol caught the ZZ-artifact pattern at a level where it had fooled four consecutive tier gates.
- 2026-08-11 (5a75ee3): G_m BRANCHES DEAD (verified+reproduced): minimal at depth-84 over Qbar (family object), (1,2) at terminal core char 0. Q2 full-locus screen + (1,2) E5-port review agent launched (the two riders). If Q2 empties and the port survives review: residue-A exclusion rests solely on the (2,3)/(2,5) chain deciders (grinding ~24h each). The kill side is winning.
- 2026-08-11: (2,5) ext p-screen DIED at 250GB/5h (monolith, pre-saturation object anyway); char-0 successor killed. (2,5) queued for saturated Q0-style gate after riders agent lands. Monolith count: 3 deaths, decomposed/witness gates: 100% decisive. The pattern is law now.
- 2026-08-11 midday: Q2 ladder closed (stratum-13 kill PROOF-TIER char 0; l12/l8/l4 shipped to box01 at 500GB/32t — GB cliff needs big iron; l1 build-gated). Saturated chain-gate agent launched for (2,3)/(2,5) — the last two open branches, built honest from birth. Residue-A endgame: minimal mostly dead (slots<13 strata pending), (1,2) owes ladder, chains at terminal gates.
- 2026-08-11 13:20: (2,3)sat screens live on ultramem (40t/1.4TB; stale unsaturated monolith killed). Fleet: box01 Q2-l12 + farm lanes; ultramem sat23 + lifts. Open ends: (2,5)sat NONEMPTY => next-tier build owed; (1,2) ladder owed; Q2 l1 build-gated.
- 2026-08-11 late: STUCK-FAMILY CLOSURE (33021f4): multi-root chain-edge cut implemented from GGV5's multiplicidad proposition — 4 of 7 stuck families now reduce fully (first verdict already: 12_36_r1_c3 EMPTY-BY-CASCADE, transfers to r2 twin); remaining 5 rho=2 families get guarded direct emission. The deg<=150 catalog now has NO family outside the pipeline. Emission driver detached (farm_stuck7.log, auto-finishes RED twins + queue + local msolve). Adversarial review owed on the cut transform before bound-150 claims.
- 2026-08-12: 5 monolith deaths diagnosed (vmem-cap silent kills) — requeued: q2l at 900GB (box01), sat23 at 1850GB (ultramem). Stuck-7 driver DONE (post-processing complete; one rc=124 timeout in tail). NEW AVENUE LAUNCHED: classical kill-test battery on the template (splice/Neumann, A-M semigroup, log-BMY, Jelonek) — four independent topology/combinatorics tests, any one can kill the two-pole configuration outright. Cut-transform review still out.
- 2026-08-12 (7242f2c): MATHIEU-ZHAO BREAKTHROUGH CLAIM — rigidity half of conj:R claimed PROVED (Theorem A, 15-line DvdK-mechanism ODE argument; M1-M5 machine checks pass incl perfect powers at all open cells). If review holds: conj:R closes at EVERY cell, strip theory uniform in (k,d2), paper1 conjecture becomes theorem. Max-depth adversarial review launched (fable) with small-degree counterexample sweeps + Lemma B bridge audit (agent's own flagged weak point). Workflows multipole-84 + sigray-audit grinding in parallel.
- 2026-08-12 (ad709ae): CLASSICAL BATTERY — the template SURVIVES topology: splice/Neumann PASS (all determinants/multiplicities positive), Jelonek PASS, A-M valuation PASS at poles with ZERO slack (ord f_y = -39 exact match), genus balance closes identically. One new kill (pi_G=4 branch dead). Sobering + significant: four independent classical tests, none contradicts the template — it is topologically a legitimate candidate. log-BMY still open pending B/x resolution tails (the one classical test left). All conclusions transfer to all surviving branch variants.
- 2026-08-12 (7179119): PAPER 1 v2 — the functional section is now THEOREMS (6.1 rigidity + 6.5 = former conj:R), 15pp, compiles clean. Ready for: (a) user's GGV follow-up note, (b) Zenodo artifact v2 (mathieu mode + MATHIEU docs added to bundle) when user wants. Still out: multipole-84 workflow, sigray-audit workflow, cut review, box01/ultramem screens.
- 2026-08-12 (0827409): THEOREM MP LANDS (multipole panel, 21 agents, 3.2M tokens): the td-ladder bottleneck is SETTLED at the structural level — verbatim m-pole 8.4 is FALSE, but the maximal kill + merge calculus reduces EVERY (m,td) multi-pole configuration to a finite book of resonant jump-vertex cells (2<=M<=r<=m, l>=1, full anatomy pinned). All 5 angles survived their refuters. Combined with prime-td + conj:R-now-theorem: the JC2 exclusion program is now finite-book at every level. NEXT: enumerate + bash the jump-vertex book (workflow-shaped); sigray-audit still running.
- 2026-08-12 (88186fd): SIGRAY FULL AUDIT (35 agents, 130 statements, 3.7M tokens): 10 NEW errata + 10 gaps found; every one triaged for campaign damage — NET RESULT: no promoted result damaged; multiple campaign readings PROVEN forced (H5a upgraded to printed-statement-forced via St 3.8; d_{f-a} reading mandatory via St 3.13/3.14). The thesis's section 2-6 foundations are now swept; the campaign's hypothesis perimeter is dramatically de-risked. Filing amendments owed (H3 quote, E-numbering of new errata) — doc-chore agent when slots free. MP integration review + cut review still out.
- 2026-08-12 (eb0abdf): MP promoted (MP0-MP8+O; MP9 corrected; finiteness rider demoted to per-frame). THE one open axis = chain-depth closure lemma — max-depth agent launched (stabilization orbit-map / Puiseux jump-count angles). If it lands: jump-vertex book FINITE per (m,td), and with prime-td + conj:R theorem + MP, the whole exclusion program becomes a finite enumeration at every level — the shape of a full JC2 proof modulo bashing the book.
- 2026-08-12 (depth): CHAIN-DEPTH CLOSURE LEMMA PROVED (SHEET6-DEPTH.md) — the M=1 chain step conserves w := (kap-rho)/nu on every l=0 step (the unbounded direction), resonant steps need Delta | num(w) and contract by <= 2/3, and the ENTIRE jump-cell menu factors through w (handshake kap_m - D/i = w; join forces equal w; nu determined per (kap_m,l)). Depth-invariance follows: menu constant beyond d0 = gen(W)+2. td=6: W={2}, menu == the promoted (2,3,1) cell exactly (explains 351/351). Bonuses: root merges need w<1 (one-line root kill); ZCH 0-edge is Prop 9.3 case (III) => needs w-ratio nu>=2 between chains (engine model corrected, no promoted conclusion touched); St 9.6(v) itself conserves w=3/2. 13/13 exact checks (cases/depth_closure_check.py). CONSEQUENCE: jump-vertex book FINITE per (m,td) — MP's demoted rider RESTORED (corrected book spec in SHEET6-DEPTH.md sec 8). The exclusion program is now a finite enumeration at every level, unconditionally at H1 tier.
- 2026-08-12 (2c81954): DEPTH CLOSURE LEMMA claimed (w-conservation; book finite per (m,td)) — max review launched (a case-branch drift or normalization mismatch would fake it; SIGRAY-AUDIT interaction checked). If it stands: launch the jump-book enumeration workflow with the reviewed spec — the program's final computational phase.
- 2026-08-12 (400b50b): DEPTH LEMMA PROMOTED — BOOK(m,td) enumeration is GO; enumerator agent launched (td 6-14, gate = td-6 record reproduction; mechanical kills inline; survivors banked for per-cell bash). The pipeline: prime-td theorem + Theorem MP + depth lemma + book bash = multi-pole exclusion per td; combined with conj:R theorem + degree farm = the full JC2 program, now finite at every level.
- 2026-08-12 (book): BOOK(m,td) ENUMERATED (cases/book_enum.py, BOOK-ENUM.md, systems/book/*.json): td=6..14, m=2..floor(td/3), reviewed spec E/T/C'/J'/R/S with the mechanical arsenal inline (MP7 l=0, gcd menu M>=2, kap-window integrality, corrected ZCH case-(III) w-ratio, root w<1, MP9 even-l, St 9.4 root budget). GATE PASS: td=6 m=2 == the promoted record cell-for-cell (unique residue-A IIa (2,3,1) M=2 child (5,3,1/2), R empty). RESULT: 421 cells, 346 killed, 75 survivors = only 22 distinct classes (31 IIa — ALL l=1, M=r, the Theorem-O escape pattern; 33 ZCH — only at w in {4,6} with an integer-ratio partner, first at td=9; 11 family-I — only r>=3, m>=3; 0 ROOT anywhere: every alphabet sits at w>=1, td-uniform root kill). Prime td 7/11/13 panels EMPTY (all entries off-axis b>=2 — the multi-pole shadow of the prime theorem). Largest class: residue-A in 10/18 panels; largest panel m=4 td=12 (21 cells). NEXT: per-cell bash — Prop 8.1(iv) rigid solve + coefficient-vs-ratio match (IIa l=1 family first), suffix engine from child data at budget td-2, r>=3 log-obstruction for family I, M>=2 chain engine for the 27 off-axis entry classes.
- 2026-08-12 (bd4baa2): BOOK BASH WORKFLOW launched (22 classes, full arsenal, adversarial votes per kill). If it drains the book: td 6-14 exclusion reduces to residue-A-type coefficient templates only — the program's endgame at every level. Prime td 7/11/13 already FULLY excluded.
- 2026-08-12 (5c6724b): BOOK BASH round 1 — 3 classes + 1 panel KILLED (frame-free T1 kills incl all 7 ZCH(2,2,3) panels); 6 survive to rigid one-scale templates; THE PICTURE SHARPENS: residue-A IIa(2,3,1) is in every nonempty panel and survives everywhere — the ladder's global bottleneck is ONE template family. Workflow resumed for the 13 unbashed ZCH/I classes (cache replay + live fill).
- 2026-08-12 (r2 interim): BOOK BASH ROUND 2 — 12 of 13 classes DEAD by first pass (only ZCH(2,3,2)M2@w6 survives); BUT the credit ceiling killed ~13 verify votes mid-run, so several 'confirmed' flags were VACUOUS (empty vote arrays). Credits restored; workflow resumed with cached bash results — live verifies + synthesis filling now. If kills hold: book = 7 surviving classes total, ALL of the rigid-template kind.
- 2026-08-12 (fbcd663): BOOK FULLY ADJUDICATED — 22 classes, 75 instances: 15 classes DEAD (closed-form kill criteria discovered: ZCH iff (nu+1)|l, family-I iff l/r or r/l in Z — these are little theorems in their own right), 7 SURVIVE, every survivor a rigid one-scale template. CREDIT CEILING hit again mid-verifies (resets Aug 15 8pm PT): 7 r2 kills carry engine-verification only, review votes OWED; cut-transform review agent presumed dead the same way. Agent work PAUSED until credits; local+fleet compute continues. Standing queue on credit restore: (1) r2 verify votes, (2) cut-transform review relaunch, (3) ZCH(2,2,3)@w4 r1 votes.
- 2026-08-12: cut transform PROMOTED (review passed; deg<=150 pipeline now fully load-bearing incl the stuck-7). Bound-150 blockers remaining: farm queue drain + big-core memory tier + two-machine replication decision + audit pass.
- 2026-08-12 (9fff9fc): BOOK FULLY CONFIRMED (all r2 kills 2-vote). TEMPLATE-FAMILY ATTACK workflow launched — 5 angles on the shared mechanism of the 7 survivors: GALOIS descent (new — the templates live in Q(sqrt d), conjugation swaps the poles; one non-symmetric pinned datum kills), the L1 sec-7.2 global h1-budget (the identified missing layer), panel budget squeeze (b>=2 entries may not reach mu=1 arrivals), classical battery on the 6 untested templates (zero-slack valuation test), and Weyl quantization (DC2 divergence as a weapon). This is the shot at closing td<=14 multi-pole outright.
- 2026-08-12 (33799c7): TEMPLATE ATTACK LANDS — book 27->23 (new law L6); three shield theorems prove Galois/budget/quantum have ZERO traction (templates conjugation-equivariant BY RIGIDITY — deep and slightly ominous); quantum divergence concentrates at the ONE resonant direction b. Everything now points at the same coordinates: L1 sec-7.2 coefficient tier at direction b.
- GROK 4.6 EVAL (xmodel/grok-eval-20260812.md): impressively deep repo read; P(JC2 true) ~0.72; 5 avenues incl. S_6 monodromy product test (covering-theoretic, Sigray-independent — GOOD and new), J-jet at G_m on the 7 dead-stretch coeffs (overlaps our R1 but sharper framing), Theorem-A-on-depth-3-column (cheap, connects our two lanes), mixed-merge completeness crack (checks our book's quarantine). Also flags the cheapest logged-but-unrun shot: IIa(3,5,1) W-residual deg-2-vs-<=1.

codex
The depth lemma does establish finiteness of the menu, but its stabilization proof and its scope are narrower than the README slogan “finite enumeration at every level” suggests: reachability remains conservative, mixed merges and coefficient/global realization remain outside it. I’m running an independent red-team pass in parallel while I finish the novelty ledger.
exec
/bin/zsh -lc "sed -n '1,240p' RECON.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# RECON — plane Jacobian Conjecture landscape, as of 2026-08-04

Scope: activity since ~2026-07-20 relevant to the (72,108)/degree-bound campaign.
Tags: COMPETES-WITH-US / USABLE-BY-US / CONTEXT.

## TL;DR
1. **We are not alone on (72,108) — but nobody has landed it properly.** Two public exclusion claims: Helali (07-21, Zenodo 21479814 + GitHub: 89 MB char-0 unit-ideal certificates, conditional on GGHV Prop 4.3, AI-built, unaudited, no arXiv) and Suzuki (07-22, Zenodo 21483636: dessins/Bézout/weighted-Macaulay exclusion of the (8,28) case, 5 MB verification pack), plus an artifact-less echo (Qiu, 08-01). No peer review, no expert endorsement, no GGV contact; openconjectures.org still shows the pre-125 status. A rigorously audited certificate (our lane) can still be the authoritative settlement — and their transcriptions are cross-check material for our Generator A audit.
2. **Plane case remains open with no credible resolution attempt:** Tao (07-21, no follow-up) confirms JC2 open; the only "proof" claim (collision-ideals + Lean, @chloeallegra228) is explicitly conditional on an unproven `PlanarNoHiddenInertia` axiom; several documented AI attacks on a 2D counterexample failed (one claims the failure is provable).
3. **New structural results we can use:** Shaska 2607.20210v2 (07-25) — in dim 2, graded-equivariant Keller maps are automorphisms for *every* weight sign pattern; Wilson 2607.23887 (07-26) — two-variable Gaussian Moments Conjecture *proved* by Newton-polygon **face isolation**; Speyer-thread Picard obstruction ("only d=3 threads the needle"); Suzuki's 5-class dessin classification of the (8,28) top edge.
4. **Dixmier:** Zheglov's DC1 (2410.06959v5, Jan 2026) unchanged and still unrefereed/unverified; Alpöge kills DC(n≥3); **DC(2) is open and is now the strongest surviving route to *proving* JC2** (Long/@octonion reports a near-miss DC(2) counterexample attempt via Poisson lifts — watch).
5. **Counterexample mechanisms multiply in dim ≥ 3, all silent on dim 2:** Gao's tangent-sweep (2608.00222, all dims > 2), the 98-map weighted-lift atlas (jacobianfun.org), degree-3 in C^19, Hessian(5)/Mathieu-SU(2)/GMC(n≥3) all fell — while every two-variable analog (GMC(2), graded-equivariant JC2) was *proved*. No bounties anywhere; UnsolvedMath = ULAM AI benchmark repo (no JC coordination); the Leiden Declaration (~3.4k signatories) sets publishing norms we should follow (AI disclosure, peer review before press).

## 1. X (via grok CLI)

### 1a. The seed event and principals
- 2026-07-20 — @__alpoge__ announcement thread — https://x.com/__alpoge__/status/2079028340955197566 — JC false: explicit cubic C^3→C^3 map, det J ≡ −2, three points ↦ (−1/4,0,0); credits Akhil Mathew for the question, Claude Fable for the construction; ~40M views; WolframAlpha verification subtweets. PDF write-up promised "eventually" (2026-07-20, .../2079301078068179224). [CONTEXT — this is our seed]
- 2026-07-21/22 — @__alpoge__ replies — engages Lowther's explicit coordinatization (.../2079546543254700471); Poisson/XYZ indexing + dim n vs 2n equivalences (.../2080070233742586215). **No Alpöge posts on the plane case, degree bounds, GGV, or Newton polygons.** [CONTEXT]
- Tao: no X account activity found; blog post 2026-07-21 (see §4), no follow-up since. Akhil Mathew: no original X posts; quoted in Fortune re "unsettling" pace + a "Leiden Declaration" on AI norms in math circulating (@v_shakthi 2026-08-02). Will Sawin: nothing substantive found. [CONTEXT]

### 1b. (72,108) / degree-bound program — DIRECT COMPETITION
- 2026-07-21 — @HelaliBillel — https://x.com/HelaliBillel/status/2079660726201856148 and .../2079660728907129102 — **Claims the (72,108)+(108,72) GGV-Horruitiner residual pairs are EXCLUDED** by exact characteristic-zero certificates (unit-ideal identities; "hard certificate ~89.1 MB over a degree-5 field") ⇒ claims max(deg P,deg Q) ≥ 125 for any planar counterexample. [COMPETES-WITH-US — same target, claims completion 4 days before our lane-2 runs]
- 2026-07-22 — @HelaliBillel — .../2079875807862734946, .../2079952758354878773 — moved on to next pair (75,125): F_2(3,5) geometry, Newton-polygon edges, order-by-order Jacobian expansion, reduction to 2128 vars / 3759 eqs (−1550 eliminated); (75,125) NOT yet excluded. Clarifies bound is the n=2 frontier, distinct from BCW cubic reduction. [COMPETES-WITH-US — is running the same program forward]
- 2026-08-01 — @QiuGuangwww — https://x.com/QiuGuangwww/status/2083602146508034380 (+ .../2083605448650068227) — claims an **independent second exclusion of (72,108)** (with ChatGPT+Grok): five degree-21 three-point covers, A_21 monodromy, exact Bézout certificates over F_101, "good reduction to char 0"; frames as conditional, complementary to Helali. [COMPETES-WITH-US — but mod-p + monodromy route, char-0 step unclear]
- 2026-07-25 — @openconjectures — .../2081132881833848977 — registry post: planar JC "known true up to degree 100" (i.e., pre-125 claims not yet absorbed), n=2 open, on "the Board". [CONTEXT — registry has NOT accepted the 125 bound]

### 1c. Plane-case attacks (AI-assisted and other)
- 2026-07-27/28 — @chloeallegra228 — .../2081612747465224648, .../2081877245577121991, .../2081941758661836921 — paper + Lean formalization of "collision ideals / off-diagonal sheets, JC as obstruction vanishing"; then **self-announced AI-assisted ideal-theoretic proof of JC(2)** — community reception unclear, no expert endorsement observed. [COMPETES-WITH-US if real; likely unvetted]
- 2026-07-23 — @ClaudeDotDo — .../2080176410723848606 — commitment hashes for a claimed "sterility theorem" for plane-JC line configurations (cross-model audits claimed, content hidden). [CONTEXT — unverifiable]
- 2026-07-26 — @CryptoJuudaime — .../2081425104727310590 — weekend Claude attempt at a 2D analog of Alpöge's mechanism; failed, claims the failure is *provable* (thread). [USABLE-BY-US — if the impossibility argument is real, it is a sheet/mechanism obstruction worth reading]
- 2026-07-21 — @sugarbets_ — .../2079582004522152400 — probing whether the n=3 mechanism descends to n=2 via a conductor/valuation obstruction. [USABLE-BY-US — valuation-flavored, same terrain as GGV (rho,sigma)]
- 2026-07-30/08-01 — @octonion (C. D. Long) — .../2082861558472814809, .../2083414091725406433, .../2082686467503993104 — planar JC "by far the most important case"; predicts AI+domain-expert proof "shortly", though his own nearby attempts stalled ("probably too difficult for current AI"). [CONTEXT]
- 2026-07-31/08-01 — @retr0techie — ~$1000 of API tokens on JC(2) with "Sol"; failed. [CONTEXT]

### 1d. Second-counterexample / mechanism activity (dim ≥ 3)
- 2026-07-20 — @alexisgallagher — .../2079251848515731535 — **98 maps C^3→C^3, one per generic fiber degree 3..100** at jacobianfun.org/counterexamples. [CONTEXT; cited by Gao 2608.00222]
- 2026-07-20 — @GuyZys — .../2079335737829580957 — "factory": parametric families, compositions, products; 16+ counterexamples, degrees from 4 up. @curioconsort SymPy factory similar. [CONTEXT]
- 2026-07-20 — @Hicksrad — .../2079226926825111848 — **degree-3 counterexample in C^19** via BCW reduction (deg ≤ 2 impossible by Wang). [CONTEXT]
- 2026-07-23 — @aryagm01 — .../2080176270675935378 — inequivalent C^3 example, det J ≡ −18, 4-to-1 generic fiber (not a coordinate change of the seed). [CONTEXT — second mechanism-instance in dim 3]
- 2026-07-20 — @davikrehalt — .../2079175065695035442 — clean geometric reformulation: P^1×Sym^2(P^1) → Sym^3(P^1) forget-a-root map, minus ramification and a well-chosen hyperplane. 2026-07-22 — @eigenstate (Rezchikov) — .../2080079977966403681 — 2D-picture derivation (three lines + two parabolas), rezchikov.me visualization. [USABLE-BY-US — sharpest statements of *why* dim 3 works; the failure mode of these constructions in dim 2 is the informative part]
- 2026-07-23 — @octonion — .../2080360259609084027 — **counterexample to the Poisson conjecture PC(2)** (with GPT-5.6), Lean-formalized ¬PC(2) ⟹ ¬JC(4); notes it removes one pathway to planar JC. [USABLE-BY-US — closes a proof route; check the Lean artifact]

### 1e. Dixmier status on X
- Consensus in window: Alpöge kills DC(n) for n ≥ 3 (DC_n ⟹ JC_n); **DC(1) claim (Zheglov, arXiv:2410.06959, ~78 pp, now v5) still unrefereed and not community-verified** (@SamuelGWalters 2026-07-22 ×2; @DavidTurturean 2026-07-22; @BrunsJulian1541 2026-07-22). DC(2) open; DC(2) ⟹ JC(2) so it is now the *strongest surviving route to a plane proof*, and a DC(2) counterexample would NOT disprove JC(2). [CONTEXT/USABLE]
- 2026-07-21/22 — @octonion — .../2079671934820687874, .../2079810183027458122 — near-miss DC(2) counterexample by lifting a rank-2 Poisson counterexample; "on the fence" whether DC(2) is true. [USABLE-BY-US — watch closely: a successful DC(2) lift would collapse the plane-proof route landscape]
- 2026-07-21/25 — @wmayner — .../2079452719824154931, .../2080901755278155784 — Fable-produced note: explicit Dixmier counterexamples for A_n, n≥3 (BCW direction), PDF at github.com/wmayner/dixmier-counterexample. [CONTEXT]

### 1f. "UnsolvedMath"
- **No X account/community named "UnsolvedMath" found.** Nearest live tracker: **@openconjectures** (openconjectures.org) — "public registry of open mathematical conjectures, ranked for renown and attackability. Posting when one falls." Tracks planar JC as open (renown 5/5, attackability 2/5), registry id ~jacobian-n2-1939; no bounties observed. [CONTEXT — see §3]

### 1g. Artifact verification of the competing claims (fetched 2026-08-04)
- **Helali:** Zenodo **10.5281/zenodo.21479814** v1.0.1, pub. 2026-07-21 — "Exact Computer-Assisted Exclusion of the (72,108) Frontier in the Two-Dimensional Jacobian Problem" + GitHub `bilLkarkariy/jc2-72-108-exact-certificates` (1 star, 5 commits). Claim structure: transcribes BOTH residual systems of GGHV Prop 4.3; Case 2 killed by a unit-ideal identity 1 = ΣT_iR_i; Case 1 splits into s=±c branches, an identity forces h=0, unit-ideal certificates kill the h=0 specialization; an involution transports the hard certificate between sign branches. Hard certificate 89,105,967 bytes; multiplier ansatz a 2010×1925 rational linear system, fixed 1925×1925 minor with det 10 mod 71; independent gmpy2 replay of 13,410 number-field products, ~70 s on a laptop, marker `JC2_72_108_EXACT_REPLAY_PASS`. **Explicitly conditional** on correctness + faithful transcription of GGHV's reduction; explicitly "not a proof of JC(2)". AI disclosure: OpenAI Codex. No arXiv (no endorsement), no expert audit visible. [COMPETES-WITH-US — inspectable, plausible, unaudited]
- **Suzuki (Eiki Suzuki, ORCID 0009-0002-0556-4967):** Zenodo **10.5281/zenodo.21483636** v1.1.4, pub. 2026-07-22 — "Exclusion of the (8,28) Newton-Polygon Case in the Plane Jacobian Conjecture" (EN+JA PDFs + 5.1 MB verification ZIP with negative controls). **This is exactly our A0=(8,28) family.** Method is structural, not brute-force: **5 dessin-d'enfants classes for the top-edge equation**, Bézout identity via exact elimination over a degree-5 number field, weighted Macaulay 261×261 minor with det ≡ 21 mod 23. Claims both alternatives excluded ⇒ bound 108 → 125. [COMPETES-WITH-US and USABLE-BY-US — small certificates, and the 5-class top-edge classification is directly relevant to our leading-tower combinatorics]
- **Qiu (@QiuGuangwww):** posts end "Paper and Code:" but **no recoverable link**; "five degree-21 three-point covers, A_21 monodromy" strongly echoes Suzuki's 5 dessin classes — possibly derivative. ~43 followers, zero engagement. [CONTEXT — discount until artifacts appear]
- **chloeallegra228:** GitHub `what-social-construct/collision-ideals` (Lean 4 + PDF "Collision Ideals and Off-Diagonal Sheets"). NOT an unconditional JC(2) proof: planar conclusion conditional on an unproven `PlanarNoHiddenInertia` hypothesis + literature interfaces (branch purity, finite-étale rigidity, Ax–Grothendieck for A^2). Author still seeking arXiv math.AG endorsement (2026-07-31). [CONTEXT — watch; the collision-ideal/sheet formalization could become USABLE if the axiom is honest]
- **Leiden Declaration** (leidendeclaration.ai; Zenodo 20302944; IMU letter 2026-06): Lorentz Center workshop product on AI-in-math norms — human responsibility, tool disclosure, peer review over press-release timelines; ~3,400 signatories, Tao/Scholze/Dijkgraaf featured; Gowers declined and blogged why (gowers.wordpress.com 2026-07-26). [CONTEXT — shapes how we should publish]

## 2. arXiv (math.AG / math.AC / math.RA, late July–Aug 2026)

Raw sweep (search "Jacobian conjecture", newest first) — details being verified:

- 2026-07-31 — arXiv:2608.00222v1 (math.AG), Shuhong Gao, "Counterexamples to the Jacobian conjecture in dimensions greater than two". New "tangent-sweep mechanism", explicit counterexample maps in ALL dims > 2 of varying geometric degree, verified in exact rational arithmetic. [tag TBD — mechanism may inform a dim-2 search]
- 2026-07-24 — arXiv:2607.22198v2 (math.AC), Meng & Yang, five-variable degree-14 counterexample to the Hessian conjecture; surveys low-dim status of JC/Hessian. [CONTEXT]
- 2026-07-23 — arXiv:2607.21572v2 (math.AG), Migus, generic degrees of real Keller maps with non-dense image; dim-2 statements conditional on planar JC. [CONTEXT]
- 2026-07-23 — arXiv:2607.20968v1 (math.AG), Huq-Kuruvilla, explicit char-2 counterexample to the separable JC (dim 3). [CONTEXT]
- 2026-07-22 — arXiv:2607.20597v1 (math.AC), Jelonek, "On mappings with Jacobian one" — component structure: automorphisms vs. components generically containing counterexamples. [details TBD]
- 2026-07-22 — arXiv:2607.20210v2 (math.AG), Shaska, "Graded Keller maps and the JC" — v2 posted; weight-sign patterns decide whether graded equivariant maps can be counterexamples (positive weights ⇒ none). [checking v2 diff]
- 2026-07-20 — arXiv:2607.18186v1 (math.PR), C. D. Long, "Small Counterexamples to the Gaussian Moments Conjecture" — explicit low-degree refutations "following routes derived from the recent Jacobian counterexample". [CONTEXT/USABLE]

Verified details on the key items:

- **Gao 2608.00222** (v1 2026-07-31): "tangent-sweep mechanism" — sweeping tangent lines of plane curves ("classical duality forces the map to hit most points several times"), generalized to direction fields on hypersurfaces. Explicit maps: 3D deg 4; 4D deg 5, 10; 5D deg 6, 12; arbitrarily large geometric degree per dimension. **Does not address dim 2 at all.** Credits Alpöge (07-19), Gallagher (07-20), Speyer (07-23). [USABLE-BY-US as negative-space: a second mechanism, still silent on the plane]
- **Shaska 2607.20210v2** (v1 07-22 14 KB → v2 07-25 44 KB, tripled): notes the Alpöge map is equivariant for wt(x,y,z)=(1,−1,−2); proves (i) all-positive-weight equivariant Keller maps are automorphisms (no counterexample can be graded that way), and (ii) **in dimension two the automorphism conclusion holds for EVERY weight sign pattern** — i.e., no graded/equivariant plane counterexample exists. Also Kummer-condition observations on stacky strata. No Newton-polygon/degree-bound content. [USABLE-BY-US — kills the graded-equivariant corner of the plane search space; consistent with and complementary to the GGV (rho,sigma) frame]
- **Jelonek 2607.20597** (07-22): generic elements of suitable components of Jacobian-1 maps are counterexamples for n ≥ 3, d ≥ 6 — post-refutation "failure is generic" structure theorem. [CONTEXT]
- **Meng–Yang 2607.22198v2** (07-24/27): Schur descent on the Alpöge map gives a 5-variable deg-14 Hessian-conjecture counterexample; ledger now "everything settled except HC(4) and JC(2)". [CONTEXT — sharpens that JC2 is the last survivor]
- **Huq-Kuruvilla 2607.20968** (07-23): explicit char-2 counterexample to separable JC in dim 3 (answers Silberman's question on Speyer's blog). [CONTEXT]
- **Mathieu/Gaussian-moments cluster:** Long 2607.18186 (07-20): explicit low-degree counterexamples to the Gaussian Moments Conjecture in dims 3,4 (routes derived from the JC counterexample); Long 2607.19012 (07-21): counterexamples to the xz-Conjecture and **the Mathieu Conjecture for SU(2)** — the Mathieu⇒JC proof route is now dead. **Wilson 2607.23887 (07-26): PROOF of the two-variable Gaussian Moments Conjecture by "face isolation" — Newton-polygon face analysis in two variables.** [USABLE-BY-US — same toolkit as ours (polygon faces/edges); the dim-2 positive result pattern continues; read for transferable face-isolation lemmas]
- Migus 2607.21572v2 (07-23): generic degrees of real Keller maps with non-dense image; dim-2 statements conditional on planar JC. [CONTEXT]
- No arXiv preprint yet from Alpöge himself (latest arXiv au:Alpoge item is Jan 2025); the counterexample's canonical writeups remain X + Tao/Speyer blogs + jacobianfun.org. [CONTEXT]

Dixmier sweep: Zheglov's claimed DC1 proof = arXiv:2410.06959, **v5 of 2026-01-19 (78 pp), UNCHANGED since — no post-counterexample update, no withdrawal, still unrefereed**. GGV themselves have prior Dixmier-counterexample-shape papers (2402.11135, 1205.6827). Logic worth keeping straight: JC2 ⟹ DC1 (so a DC1 *refutation* would kill plane JC — none exists); DC2 ⟹ JC2 (so DC2 is now the strongest surviving *proof* route; DC2 open). [CONTEXT]

## 3. UnsolvedMath
- **What it is:** unsolvedmath.com — "UnsolvedMath | Repository of Open Mathematics Problems", built by **ULAM AI (Przemek Chojecki, @prz_chojecki)**; companion Hugging Face dataset `ulamai/UnsolvedMath` (v1.2.0, generated **2026-07-31**, 5,426 problems, 17 domains, incl. 632 Erdős problems). Aggregates AMR lists, Erdős, Kirby, Kourovka, Hilbert, Smale etc., with per-record provenance and an L1–L5 difficulty scale + moderated forum. Positioning is *AI-benchmark repository*, not a coordination hub.
- **JC2 tracking:** no Jacobian-specific entry retrievable (site is JS-rendered; the HF dataset card does not surface one); dataset docs warn statuses "may be solved after dataset publication" with no live update mechanism documented. **No bounty, no working group.** [CONTEXT]
- **The de-facto live tracker is openconjectures.org** (@openconjectures): entry `jacobian-n2-1939` = **Open**, renown 5/5, attackability 2/5, "surviving case after the July 2026 refutation of JC(n), n≥3"; caveats that tracking may lag; **no degree-bound update to 125 recorded; no bounties; no coordination infrastructure.** Tao-blog commenters use it as the reference status page. [CONTEXT — if our certificate lands, this is where status flips first]

## 4. Other: GGV group pages, Tao blog, MathOverflow
- **Tao's blog:** only the 2026-07-21 "A digestion of the Jacobian conjecture counterexample" (terrytao.wordpress.com/2026/07/21/...). States plainly: "The conjecture remains open in two dimensions." **No follow-up post as of 2026-08-04**; only cosmetic post-publication edits; comments contain no plane-case program, no degree-bound discussion. [CONTEXT]
- **Speyer / Secret Blogging Seminar (2026-07-20)** (sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/): notes the seed map's homogeneity under deg(x,y,z)=(−1,1,2); discriminants factor as squares; sheets "escape to infinity together" over Δ=0. Comment thread is the sharpest public structure discussion: **Will Sawin** (07-20) gives the P^1×Sym^2(P^1)→Sym^3(P^1) formulation with X ≅ A^3 as iterated A^1-bundle; **"Skooi"** (07-21) proves the direct generalization π: P^1×P^(d−1)→P^d **fails for d ≥ 4 by a Picard/class-group obstruction (discriminant class Z/(d−2)) — "only d=3 threads the needle"**; Lior Silberman raises char-2 (answered by 2607.20968). [USABLE-BY-US — the obstruction calculus for why the mechanism needs d=3 is the best current hint at what a dim-2 mechanism must evade]
- **jacobianfun.org** (Alexis Gallagher + GPT-5.6 "sol"): explainer + atlas of 98 verified maps, fiber degrees 3–100, via a "weighted-lift" from seed polynomials p with p(0)=0, p(1)=−c, ∫₀¹p=0. Explicitly: "These three-variable constructions do not settle the separate two-variable case." No bounties/coordination. [CONTEXT]
- **GGV group (Guccione ×2 / Valqui, + Horruitiner):** **no public response to the counterexample and no new JC preprint** — latest arXiv item is math.GR (2606.05520, June 2026); latest JC-adjacent is Ramirez–Valqui **2506.05697** (June 2025), "The Groebner basis and solution set of a polynomial system related to the Jacobian conjecture" [USABLE-BY-US — closest published precedent for our Gröbner/msolve formulation; check their normalizations against Generator A]. Valqui's PUCP CRIS page (cris.pucp.edu.pe) shows nothing newer. Neither Helali nor Suzuki appears to have contacted them publicly. [CONTEXT]
- **MathOverflow: coverage gap** — mathoverflow.net and api.stackexchange.com both block our fetcher; domain-restricted search is likewise refused. Generic web search surfaced **no** post-07-20 MO thread on the plane case. Recommend a manual browser check of mathoverflow.net/search?q=jacobian+conjecture (newest). [GAP]
- **Lee–Li "Conjecture E"/Magnus program:** no new installment since "Magnus' formula revisited IV" (2408.01279, Aug 2024); no visible activity in the window. [CONTEXT]

## Implications for our campaign
1. **Priority risk is real but the authority slot is open.** Helali/Suzuki beat us to *claiming* (72,108)/(8,28) by days, but both are Zenodo-only, unaudited, and explicitly conditional on GGHV's reduction. Nobody has: (a) an arXiv-grade writeup, (b) an independent audit of the Prop 4.3 transcription, (c) GGV sign-off. Our differentiators should be exactly those three, plus certificate independence (msolve/Singular + FLINT checker vs. their SymPy/gmpy2 stack).
2. **Immediate technical to-dos:** (i) diff Helali's transcription (2010 eqs / 1925 unknowns, s=±c branch split, h=0 forcing) and Suzuki's formulation against our Generator A systems (open_8_28_c1: 187 vars/303 eqs; c2: 73/93) — agreement across three independent transcriptions would be a strong exhaustiveness argument; disagreement is a red flag we must resolve *before* trusting any verdict, ours included. (ii) Download both verification packs (Zenodo 21479814, 21483636) and replay them. (iii) Read Suzuki's 5-dessin top-edge classification — if correct it may shortcut our lane-2 msolve grind (structural kill vs. F4). (iv) Mine Wilson's face-isolation lemmas and Shaska's dim-2 equivariant theorem for reusable polygon-face arguments; both align with the GGV (rho,sigma) grading we already planned to exploit.
3. **If our lane-2 runs return nonempty** (candidate leading tower), the competitor claims imply we should expect a transcription discrepancy — their unit-ideal certificates and our solutions cannot both be right; the diff in (2i) becomes the decider.
4. **Write-up strategy:** follow Leiden norms (full AI disclosure, artifacts + independent checker, contact GGV before public claim — they are silent so far and are the natural validators; Ramirez–Valqui 2506.05697 shows Valqui already runs Gröbner pipelines and can referee this). Cite Helali/Suzuki as independent concurrent computations regardless of audit outcome.
5. **Program-level watch items:** DC(2) activity (a proof would subsume JC2; @octonion's lift attempts), any Alpöge PDF (promised, not yet posted), a Shaska v3 or responses, Gao-mechanism dim-2 descent attempts (@sugarbets_'s valuation obstruction probe), and the (75,125) frontier Helali has already opened — if the 125 bound stands, that pair is the next campaign target and we should pre-emit its systems.
6. **Coverage gaps in this recon:** MathOverflow (crawler-blocked — check manually), unsolvedmath.com's JC entry (JS-rendered), and the unverifiable Qiu "paper and code".

## Correction (2026-08-06, per SHEET6.md): "no independent reproof of
Żołądek degree-5" is WRONG — Sigray's independent 2008 ELTE thesis (decorated
Eggers-Wall trees, never journal-published) proves it; full text obtained
(refs/). Sheet-bound foundations are doubly-sourced, though BOTH unaudited
(Żołądek gcd-section gap documented by GGV).

## Delta — 2026-08-06 (window 2026-08-04 → 08-06; sources: grok CLI ×4, arXiv API, Zenodo API, GitHub API, web)

### Competitors: frozen across the board
1. **Helali silent on math.** Posts daily 08-04→08-06 but ONLY AI-product chatter; zero on (75,125)/Jacobian/Zenodo since 07-22. GitHub last push 07-21; Zenodo still v1.0.1. Last stance: "(75,125) not yet excluded" (07-22, .../2079875807862734946 — that thread also records a finer reduction, 578 free vars / 2,209 residual eqs, beyond the 2128/3759 noted in §1b; and .../2079848260445876630 acknowledges Suzuki as independent). [COMPETES — stalled 15 days]
2. **Suzuki static.** Zenodo 21483636 still v1.1.4 (modified 07-22); no new records under his name, no X activity in window. [COMPETES — static]
3. **Qiu vaporware confirmed.** "Paper and Code:" links never posted; his only post since 08-01 is a football reply (08-04, .../2084619096512160011). Discount fully. [CONTEXT]
4. **125 bound NOT absorbed.** openconjectures.org `jacobian-n2-1939` still Open, renown 5 / attack 2, no degree bound shown; @openconjectures' 08-01 kill-feed post (.../2083614487790354768) has no JC update — last explicit n=2 statement remains "true up to degree 100" (07-25). [CONTEXT — authority slot still open]
5. **NEW third (72,108) competitor, missed by the 08-04 snapshot:** Felipe Santibañez-Leal, Zenodo **21740213** — "A planar program for the two-variable JC: theorem ladder, staircase transport, and machine certificates at the (72,108) frontier" ("Paper B of 3"; cites GGHV 2204.14178 Prop 4.3; 33×33 core H(A,B,C), direction K_(2,8), 136,500 tensor-grid controls over 30 primes + CRT). **27 versions v0.09 (07-24) → v0.32 (08-01), then dormant — no in-window updates; does NOT claim exclusion.** Author is a mass-output AI-paper account (36 Zenodo records in ~10 days across unrelated fields: Huneke–Wiegand, Shub–Smale tau, ECG physics…). [COMPETES — third independent transcription = extra cross-check material for §Implications 2(i); credibility low]

### Dixmier / proof routes
6. **Zheglov: total silence.** arXiv 2410.06959 still v5 (2026-01-19); zero X discussion, no referee/verification news in window. [CONTEXT]
7. **@octonion: no new DC(2) content.** In-window only Poisson-fallout restatements (+ a SIC-POVM note 08-04). Last DC(2)/near-miss posts remain 07-22/23; one pre-window addition to §1e: 07-30 (.../2082888559946571943) — Mathieu fails via a Hopf-pair construction independent of JC(3). [CONTEXT]

### arXiv (math.AG/AC/RA, in/near window; 51 new entries swept, none JC(2)-direct; no Dixmier items; Gao still v1, Shaska solo still v2, no Alpöge PDF)
8. **Kistner–Shaska 2608.02863** (math.AG, 08-03; bot-tweeted 08-05): "Orbits and Fields of Definition for Graded Keller Maps" — sequel to §2's Shaska: populates hyperbolic-weight strata K(3,(1,−1,−1)) (cyclic cones, every composite generic degree ≥ 6; 33-sheeted member over Q) and K(3,(1,−p,−p)); geometric monodromy always full alternating/symmetric (solvable only at generic degree 3); genuine positive-dimensional moduli at degree 12. Dim 3 only — sharpens the dim-2/dim-3 dichotomy of §2. [USABLE — negative space + full-monodromy result to test Qiu-style A_N claims against]
9. **BACKFILL (07-29, missed by snapshot; visibility via @AlgebraicPapers 08-05): Mondello arXiv 2608.02634** — "A Dimension-Two Counterexample to the Separable Jacobian Conjecture in Characteristic Two". Explicit PLANE Keller pair over k=F̄₂: P = x+x²y+x⁴+x⁶y², Q = y+x⁵+x⁶y+x⁷y²+x⁸y³, det J = 1, three points share an image, [k(x,y):k(P,Q)] = 3 separable; derived from Huq-Kuruvilla's char-2 map (§2). [USABLE — **mandatory stress test: run OUR vertex-gap/strip-pair argument on this map's Newton polygon; it must fail only via an explicit char-0 step, else our mechanism has a hole**]
10. Periphery, in-window: Nisse 2608.03613/2608.03601 (08-04) — new Newton-polygon bounds for amoeba-contour cusps/nodes of plane curves (polygon-singularity toolkit, no JC content); Maxim–Messina 2608.04320 (08-05) — vanishing cohomology of fibers at bifurcation values incl. singularities at infinity (sheets-at-infinity terrain); Hajra 2608.04214 (08-04) — classification of affine surfaces finitely dominated by C*×C* (C² among targets). [CONTEXT]

### Our mechanism: still unclaimed
11. **No independent appearance of the vertex-gap mechanism.** X + arXiv searches for "vertex gap", "strip pairs", "parallel edges" (Jacobian context), "near-origin obstruction", polygon-obstruction phrasing: zero hits. Żołądek/Sigray sheet-degree bounds: zero public activity. [CLEAR — we remain alone on this]
12. **GGV still fully silent** (no reaction to counterexample or any exclusion claim through 08-06); **Lee–Li/Conjecture E: nothing**; **chloeallegra228: no JC follow-up in window** (Lean-process rants only; collision-ideals paper still NOT on arXiv — endorsement apparently still lacking). [CONTEXT]

### Ecosystem
13. **Alpöge JC PDF still missing** — but on 08-04 (.../2084776351878537387) he posted Fable write-ups for OTHER problems (Connes, permanent, quantum parallel repetition, CVP, Ehrhart): the write-up pipeline is active, JC not in it. **Tao's new post 08-06 is on the HRT counterexample** (Faulhuber–Petersen–van Velthoven–Voigtlaender) — the wave has moved to the next conjecture; still no JC(2) follow-up from him. Mainstream recaps 08-05/06 (ScienceDaily et al.) uniformly state 2D open. [CONTEXT]
14. Zenodo noise, in-window/backfill: Santana 21826515 (08-06) "JC and the Arrow of Time" (physics crank); Reed 21542914 (07-25, missed by snapshot) claims "Formal Resolution of the Two-Dimensional JC in Lean 4" via graded differential operators + Jung–van der Kulk — unvetted, zero community visibility, near-certainly wrong (JvdK-flavored circularity); Leal Ramirez 21538118 (07-24) — "nearly free divisor" homological analysis of the dim-3 map. [CONTEXT — noise tier, logged for completeness]
15. MathOverflow: still crawler-blocked; web search shows no new JC thread signal. [GAP persists]

### Delta implications
- Competitive pressure DROPPED in-window (Helali stalled, Qiu vaporware, Suzuki static, registry un-absorbed) while our differentiators (audit, arXiv-grade writeup, GGV contact) remain unclaimed — §Implications 1 stands, with more slack than feared.
- New to-do ahead of any publication: (a) stress-test the vertex-gap argument against Mondello's char-2 plane map (item 9); (b) add Santibañez-Leal v0.32 to the three-way transcription diff (item 5); (c) mine Kistner–Shaska's full-monodromy theorem when auditing any A_N-monodromy exclusion claim (item 8).

## Delta 2026-08-07: Sigray td>=6 demoted to incomplete-as-printed
SHEET6-CAMPAIGN.md + SHEET6-REVIEW.md (all fronts confirmed): the thesis's §9
propagation bash never treats leaf-table rows 1,5,7,10, its St 9.12 kill set
cannot close its own case-IV terminals without an unstated root-vertex kill
(our H3), and three printed "no solution"/"M_F=1" claims are false (E2-E4,
lambda=0 self-loop families). Consequence: Sigray is NOT an independent reproof
of td>=6 exclusion as printed; td<=5 remains safe via Orevkov/Domrina-Orevkov/
Zoladek. Our campaign engine (cases/sheet6_campaign.py) is now the most
complete written treatment of the td=6 bash; remaining gaps: H3 (blocking,
also needed by the thesis), ~15 case-III s-tails, two-pole (3,3) config.

## Delta 2026-08-10 (window 08-06 → 08-10; sources: grok CLI ×3, arXiv API, Zenodo API, GitHub API, web, local msolve repro)

### 1. Plane JC / JC(2) progress
- X: quiet — no proof/exclusion claims, no degree-bound posts; all known handles (Helali, Qiu, octonion, Alpöge, chloeallegra228, openconjectures) silent on Jacobian in-window; only "2D still open" recaps (@grok ×3, @claude_news 08-06, @0x_illuminati 08-09, etc.). [VERIFIED via grok; no substantive findings]
- Alpöge now posting on RH/zeta; JC PDF still missing. Tao's newest post = HRT counterexample (08-06), no JC(2) follow-up. openconjectures `jacobian-n2-1939` still Open, no degree bound absorbed. [VERIFIED]
- arXiv, new in window: **2608.05392** (subm. 08-05; Castañeda–Honorato–Valenzuela-Henríquez) — weak Markus–Yamabe FAILS for n≥14: a "chain realization" theorem turns any Keller map into a Hurwitz vector field whose singularities biject with a prescribed fiber; applied to the JC counterexample gives a deg-7 field on R^14 with 3 singularities (also deg-3 on R^18); dims 3–13 open; zero dim-2 content. [VERIFIED abstract; CONTEXT — fallout continues, plane untouched]
- Gao 2608.00222 still v1; Shaska 2607.20210 still v2; Mondello 2608.02634 still v1; no other JC/Keller/"Jacobian conjecture" arXiv items in window. [VERIFIED]

### 2. Sheet-number / topological degree / Sigray
- No findings. X: zero hits on topological/geometric degree of Jacobian pairs, "sheet six", Sigray/Orevkov/Domrina/Żołądek, Eggers–Wall trees (only false positives: Polish "żołądek", Dave Eggers). Web + arXiv likewise. Our td=6 campaign and the Sigray-incompleteness finding (Delta 08-07) remain unclaimed territory. [CLEAR]

### 3. Degree bounds / (72,108) competitors
- All known competitors frozen: Helali Zenodo v1.0.1 (GitHub push still 07-21, 1 star); Suzuki v1.1.4; Santibañez-Leal v0.32 (08-01); Qiu artifact-less and silent. No deg>125 verdicts, no (75,125) movement, no trace of anyone else sweeping ≤150. [VERIFIED via Zenodo/GitHub APIs + grok]
- **BACKFILL — FOURTH independent (72,108) artifact, missed by the 08-06 snapshot:** Ishihara Kotaro, Zenodo **21757679** (pub. 08-02, v1.3.0) — "A Reproducible Exact-Computational Artifact for the Planar Jacobian Degree Pair (72,108)": two Laurent/Newton systems, conditional on GGHV 2204.14178, exact certificates, "nine-variable source-to-chart provenance", one-command verification (14.4 MB zip + technical note PDF); explicitly makes NO priority claim and does not claim to prove JC2. [metadata VERIFIED, content UNVERIFIED; COMPETES/USABLE — the transcription diff of Implications 2(i) is now four-way]
- In-window Zenodo noise: Ross 21845742 (08-08) — two notes + code on the 3D counterexample (Tao-digestion keyed). [CONTEXT]

### 4. Dixmier / DC(2)
- Effectively no findings. Zheglov 2410.06959 still v5 (2026-01-19); no new Dixmier/Weyl-endomorphism arXiv items; X in-window only expository (@dif_engine 08-07 ×2, Japanese thread: Dixmier-implies-JC framing + authority priors). @octonion silent on DC/Poisson/Weyl since 08-04 (posting on Robbins algebra, RH strategy). Zero reaction anywhere to the DC/PC divergence (quantum-vs-Poisson rigidity) idea. [VERIFIED sweeps]

### 5. msolve parenthesized-input mis-parse — NOT known upstream
- Reproduced locally (homebrew msolve 0.10.1): input `x-(3+1)` → reduced GB `[x+1]`, exit 0, no warning (correct: `[x-4]`). [VERIFIED]
- GitHub sweep of algebraic-solving/msolve: NO existing issue/PR mentions parentheses. Nearest kin: **issue #354** (open 07-27, 0 comments) — silent mis-parse of division after a monomial (`x/2` → wrong answer or spurious `[-1]`, exit 0) — same failure class: undocumented syntax silently accepted; **#313** segfault on malformed input (`*x`), fix **PR #320** ("Reject malformed inputs in the term parser") open + unmerged since 03-23. [VERIFIED]
- **ACTION — we should file a new issue** (cite #354 as sibling, note #320's pending hardening); meanwhile keep our emitters paren-free and grep all existing .ms inputs for `(`.

### 6. AI-assisted math attacking JC / Dixmier
- No findings. No X or web trace of any other automated case-bash / Gröbner / degree-farm / Lean campaign on JC(2) or DC(2); no lab or group announcements; @openconjectures/unsolvedmath/ULAM silent; chloeallegra228 no JC follow-up (collision-ideals still not on arXiv). [CLEAR — ours remains the only visible systematic computational campaign]

### Delta implications
- Competitive pressure still FALLING: four (72,108) artifacts now exist, but all are static, conditional on GGHV, and unaudited; nobody visibly racing the ≤150 sweep or the sheet-6 lane. The authority slot (independent audit + arXiv writeup + GGV contact) is still open; GGV still silent (no new arXiv since 06/2026).
- New to-dos: (a) fold Ishihara v1.3.0 into the transcription diff — four-way agreement would be a strong exhaustiveness argument; (b) file the msolve parenthesis issue upstream; (c) skim 2608.05392's chain-realization theorem — the Keller-map→vector-field transfer is new machinery worth checking for a dim-2 converse.

exec
/bin/zsh -lc "sed -n '1,188p' notes.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# JC₂ campaign — high-level notes

(Working notes per DC's request: avenues, decisions, findings. Not a paper draft.)

## Where things stand (2026-07-28)
- (72,108) is the sole open Newton-polygon family below degree 125 (GGV 2022).
  We reduced both its subcases to small "cores" (30 and 73 vars) via:
  direct polygon transcription → torus normalization → gauge analysis
  (Q determined by P modulo explicit gauge) → bilinear b-elimination cascade.
- Pipeline validated on the solved (66,99) subcase: EMPTY [1] in 2.3s at p=65521
  (two machines, independent builds). Raw formulations of the same case need
  600-850 GB — explains why this sat unresolved since 2022.
- Line probe (validated on solved case): open subcase (2) has NO codim-1
  solution family at p ∈ {65521, 1048573, 2147483629}. Remaining outcomes:
  empty-with-deep-certificate, or small deep solution locus (= candidate
  counterexample towers).
- Verdict pending: msolve on the open cores (fleet: ultramem-1 + jc-b).
  Spot preemptions are the operational enemy; ~20h jobs lost twice.

## Avenue map (approved 2026-07-28)
1. **(72,108) resolution** — in flight. Either bound→125 (after char-0
   certificate + reduction audit) or first-ever live counterexample lead.
2. **Family farm** — approved. Automate GGV family enumeration → same pipeline
   per family → sweep all families to degree ~150-200 on a Spot fleet.
   Exclusion and search are the same computation. Prereq: validate Generator A
   on unreduced family data (§4 hand-reductions are the non-automated step).
3. **Algorithmic levers (my queue)**: left-kernel obstruction ideal (pure
   a-space, 18/24 vars); Cascade3 level-order fixes for (9,27)/(7,21) [G0
   completion]; plane probe (codim-2 test); engine diversity (Singular/M2/
   HC.jl) when quota allows.
4. **Proof-side threads (background)**: Conjecture E (Lee–Li remainder
   vanishing) — test low-degree instances computationally; Żołądek sheet-bound
   extension feasibility (chart case-analysis = agent-parallelizable);
   Zheglov DC₁ verification (would close the ¬DC₁ route).
5. **Not doing yet**: paper draft (per DC); Lean certificate formalization
   (post-verdict); GPU anything (no mature engine).

## Operational decisions log
- Spot-vs-on-demand: M3 quota = 96 vCPU global (ultramem-1:64 + jc-b:32 = at
  ceiling). On-demand M3 also capacity-blocked in us-central1-a. → QUOTA RAISE
  NEEDED for family farm (ask: M3 CPUs 96→512, or N2 equivalents).
- Preemption mitigations: redundant racing of the critical job on independent
  instances; @reboot resume; auto-restart guard; -v 2 progress files.
- All boxes self-poweroff when their queue drains (QUEUE_DONE marker).

## Open questions / risks
- Is the open-c2 core's grind "fat empty certificate" or "deep small variety"?
  (Line probe can't distinguish; msolve will.)
- Cascade3-over-ℚ soundness audit + G0 string identities still owed before any
  public claim (postverdict.md).
- Prop 4.3 (§4 reduction) is trusted from the unrefereed GGV chain; the direct
  raw-polygon runs (char-0 lane) provide partial independence.

## 2026-07-29 loop notes
- G0 sweep result: NO level direction (10 tried) completes Cascade3 on
  (9,27)/(7,21) — structural, not tuning. G0 stands at 3/5 solved families
  validated (both (9,24) forms + (8,28)-machinery); remaining 2 families
  emitted as partial-core fleet jobs instead (sound mid-cascade states).
- Open-case structure signal: complement chart (pivot-monomial = 0 branch) is
  HARD locally (>1h) where the regression analogue was instant — third
  qualitative difference between open and solved cases (after core hardness
  and fat memory).
- Plane probe (agent-built, gate-validated incl. planted-solution tests):
  open_8_28_c2 has NO codim-2 solution family at p=65521 (10 planes) and
  p=1048573 (2x5 planes); with the line probe, any solutions have codim >= 3
  in the 24-dim a-space. Empty-with-fat-certificate hypothesis strengthens.
- Farm prereq verdict: unreduced (48,64) family = 1314-var bilinear system;
  Cascade3 manages only 43/830 b-eliminations before swell (73 min). GGV's §4
  reductions are load-bearing. Farm routes: (a) automate §4 (edge-form
  factorization + corner-cutting automorphisms — the real prerequisite), or
  (b) raw unreduced systems directly on big-memory msolve — test queued on
  ultramem-1 (moh_48_64_raw, solved family = safe validation).
- 2026-07-30 (UTC) MILESTONE: open_8_28_c2 chartG (generic chart, 27 vars) =
  EMPTY [1] mod 65521 on jc-b, sub-second, verdict authenticated (proper F4
  header + full var order + basis length 1). Half of open subcase (2) decided
  at one prime. Remaining: complement = core + (a2=0 or a6=0) — split into
  two explicit sub-branch systems (cCa2, cCa6), racing locally + on jc-b's
  queue (unsplit). Then: other primes (queued), strict variant, subcase (1),
  char-0 for certificate grade.
- jc-b post-mortem: the "wedge" self-resolved via reset + one silently
  successful repoint attempt; giant-core jobs remain banned on 976GB boxes.
- Conjecture E (Lee-Li remainder vanishing): first computational verification
  of the 7 smallest instances ((a,b,m,n)=(2,3,2,4), delta=1): 6 HOLD with
  char-0 Groebner certificates + agreeing mod-p lane, 1 degenerate, 0 fail.
  Gate on commuting-pair fixture passed (automorphism pairs cannot realize
  these polygons by Abhyankar divisibility — commuting pairs are the right
  gate). lib/conjE.py, runs/conjE_results.txt. Evidence FOR the E=>...=>JC2
  program route. Next tier of instances is a scale-up when compute frees.
- 2026-07-30 AUDIT MILESTONE: the generic-chart emptiness of open subcase (2)
  is a SYMBOLIC theorem-fragment, not an F4 result: the cascade+chart
  substitution chain reduces original equation #3 (one explicit coefficient of
  [P,Q]-x^2) to the constant -1 on the chart locus. Independently audited at 6
  random exact-rational chart points (original equations + stored
  substitutions only; culprit = -1 at all points; 51/92 pivot equations
  vanish; no other constants). Valid over every field away from denominator
  primes. Regression contrast: the solved case's chartG has NO such collapse
  (needed real F4) — this shallowness is specific to (72,108) s2.
  TODO: extract which bracket position eq #3 is; write the substitution chain
  as a standalone lemma; attempt same for cCa2 (its char-0 [1] took real
  work; lift still running).
  Subcase (2) status: chartG EMPTY (symbolic+char-0+mod-p), cCa2 EMPTY
  (char-0+mod-p), cCa6 RUNNING (deg 12+, big box).
- 2026-07-31 MAJOR MILESTONE: open subcase (2) EMPTY at TWO primes across all
  three strata (chartG / cCa2 / cCa6 at p=65521 and p=1048573; cCa6 was the
  ~7h/48-thread nucleus each time). chartG+cCa2 also EMPTY over Q; chartG
  additionally by audited symbolic contradiction. Union of strata = full
  reduced variety of Prop 4.3 s2 => subcase (2) has NO solutions at either
  prime, pending: cCa6 char-0 (launching), strict variant (running),
  pipeline audit write-down. Subcase (1) = the remaining half of (72,108);
  chart decomposition being built now.
- 2026-08-01 MILESTONE: cCa6 EMPTY [1] over Q (17h43m, 761 GB peak, proper
  reduced-GB header). SUBCASE (2) OF (72,108) IS NOW EMPTY OVER Q IN FULL:
  chartG (symbolic + Q + 3 primes), cCa2 (Q + 3 primes), cCa6 (Q + 2 primes,
  3rd prime running on jc-b). GB=[1]/Q => empty over C. Conditional on:
  Generator-A transcription (regression-validated), Cascade3/two_chart/split
  soundness (numerically audited; formal write-down owed), msolve char-0
  correctness (+ multi-prime agreement), and GGV Prop 4.3.
  REMAINING for full (72,108) discard -> bound 125: subcase (1) (c1 core
  queued both boxes; chart decomposition blocked on two_chart swell guard),
  strict variant (1d1h in), audit paperwork + certificates.
- Strict-variant simplification: v6s (strict corner convention) died after
  ~1d2h, but is RETIRED as redundant: strict variety = nonorigin variety +
  extra origin-nonvanishing equations, i.e. a SUBSET — and the nonorigin
  subcase-(2) variety is proven empty over Q. Empty by inclusion; both polygon
  conventions settled for subcase (2) with zero further compute.
- AUDIT.md landed (410 lines): 8-claim soundness chain for "subcase (2) empty
  over char 0, conditional on GGV Prop 4.3", each claim with code citations +
  verification status; explicit trust boundary; remaining-obligations
  checklist (record pivot product from committed re-run; lemma write-downs;
  pin GGV arXiv versions; subcase (1) reserved for any bound-125 claim).
  Claim 2 torus algebra independently re-verified by hand.
- G0 deepened: solved case (9,24)-(3) EMPTY in 14/14 combinations swept by
  lane 1 (v6 core / chartG / chartC / strict x char-0 + three primes) —
  the pipeline reproduces known mathematics in every mode used for the
  open-case claims.
- 2026-08-02 LEMMA.md: the -1 collapse is a VERTEX-GAP OBSTRUCTION —
  vertex normalization a1*b3=1 vs gap-column death ((q0)_x=2) =>
  near-origin tower overdetermined by 1 => (unit)*a2^2*a6*b3 in I =>
  b3=0 contradiction. Chart-free: a2^2*a6 in I(core), DERIVING the
  cCa2/cCa6 split. Discriminator (q0)_x >= 2 sharply separates open vs
  solved family (verified symbolically both ways; eq3_chain.py committed).
  Valid char 0 + p outside {2,3,5,7,11,13}. Gaps: surplus condition not yet
  polygonal; c1's y-axis column breaks the mechanism (open there).
  FARM IMPLICATION: polygonal pre-filter candidate for family tables.
- SECTION4-AUTOMATION.md landed: §4 reductions ARE one algorithm, and it is
  COEFFICIENT-FREE (lattice arithmetic; RHS = x^(ceil(b/a)-2), matching all
  four props; subcase splits = root partitions + finite st-candidate lists).
  Agent-verified: reconstructed transforms reproduce all 7 emit.py polygon
  sets. Effort 2-3 weeks / 2-3 kLOC on lib/jc.py; regression gate = Props
  4.1-4.4 + the (8,32) discard. Farm now: quota + this implementation.
- LEMMA-REVIEW.md: 4/5 fronts CONFIRMED by independent recomputation
  (reproduction, geometry, chain soundness incl. fresh-point checks, prime
  hygiene {2,3,5,7,11,13} exact). Front 4 WEAKENED-and-improved: sharpness is
  side-symmetric (max((p0)_x,(q0)_x) >= 2); confound cell provably empty;
  swapped family also collapses; O(1) localization confirmed via toy family.
  Corrections appended to LEMMA.md. Mechanism STANDS.
- FACE-ISOLATION.md: Wilson GMC(2) port = partial-real (architecture matches
  slots JC2 already fills; disanalogy = infinite moment tower vs one bilinear
  identity). Transferable core = valuation-counting discipline; its TL1 is
  precisely our surplus-condition theorem (level filtration ~ p-adic
  valuation), verified on the c2 chain + a moment toy. Converges with the
  independent SURPLUS.md derivation in flight — cross-validate on landing.
- CROSSCHECK.md landed: THREE-WAY transcription agreement on Prop 4.3
  (Helali/Suzuki/ours; gauge-differences verified by hand). Both external
  artifacts cover BOTH subcases, both replays PASS (Helali 71s; Suzuki
  byte-identical 21.5s); our agent closed Helali's replay gap by proving his
  two untested identities. => bound-125 now rests on 2 external artifacts +
  our audited s2, with our c1 leaves as third replication (urgency reduced;
  a NONEMPTY leaf would contradict two artifacts = maximal alarm). Publication
  posture: cooperative (engage Helali, Suzuki, GGV; Leiden norms). c1-extract
  diff vs our core queued (crosscheck/c1_extracts/).
- SURPLUS.md v2: CONDITION (iii) PROVED from polygon data for the (k,d2)=(2,2)
  class (any strip lengths, char excl {2,3,5}) — includes (8,28). Props A/B
  (key/elimination counts) proved for ALL k,d2. Refinements: discriminator =
  leftover CONTENT not bare count (solved family counts 1 but leftover == 0);
  k>=3 breaks (iii) genuinely; wide strips: obstruction persists in non-
  surplus-1 form (4 leftovers, torus-empty numerically). Position rule:
  surplus key = w=1 stratum of Minkowski column k+2. Validation assertion-
  locked to the audited chain. Vertex-gap now fully polygon-theoretic in its
  regime. Next: adversarial review, TL1 cross-validation, then write-up.
- Ops: rev-order leaves deployed BOTH boxes (foreground file-based — the ssh
  failure law is now: complex inline commands flake, file-exec never has).
  Background gcloud-ssh loops retired permanently.
- SURPLUS-REVIEW.md: theorem CONFIRMED at variety level (scope map predicted
  4/4 fresh families; Props A/B independently re-derived; char {2,3,5} sharp;
  fix_ones-free). Errata applied: ideal-membership -> radical membership;
  content-discriminator marked observed-not-proved; TL1 scoped to (2,2) and
  superseded. VERDICT: SURPLUS+LEMMA ready for joint paper-grade write-up of

exec
/bin/zsh -lc "rg --files -g '*.md' | sort" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
AUDIT.md
BOOK-BASH-R2.md
BOOK-BASH.md
BOOK-ENUM.md
CAMPAIGN.md
CROSSCHECK.md
DC2-PROGRAM.md
DC2-REVIEW.md
FACE-ISOLATION.md
LEMMA-REVIEW.md
LEMMA.md
MATHIEU-REVIEW.md
MATHIEU.md
MONDELLO-CHECK.md
README.md
RECON.md
REDUCE4-CUT-REVIEW.md
REDUCE4-REVIEW.md
RESIDUE.md
SECTION4-AUTOMATION.md
SHEET6-2POLE.md
SHEET6-A2P-REVIEW.md
SHEET6-A3L1-REVIEW.md
SHEET6-AF2.md
SHEET6-AF3.md
SHEET6-CAMPAIGN.md
SHEET6-CLASSICAL.md
SHEET6-DEPTH-REVIEW.md
SHEET6-DEPTH.md
SHEET6-H3.md
SHEET6-HIII-REVIEW.md
SHEET6-III.md
SHEET6-L1.md
SHEET6-LROOT.md
SHEET6-LT-REVIEW.md
SHEET6-MP-REVIEW.md
SHEET6-MULTIPOLE.md
SHEET6-PILOT.md
SHEET6-R1-25LOCUS.md
SHEET6-R1-LADDER-REVIEW.md
SHEET6-R1-Q2E5.md
SHEET6-R1-REVIEW.md
SHEET6-R1.md
SHEET6-R6-REVIEW.md
SHEET6-R6.md
SHEET6-REVIEW.md
SHEET6-TDU-REVIEW.md
SHEET6-TDUNIFORM.md
SHEET6-TEMPLATE.md
SHEET6.md
SIGRAY-AUDIT.md
SURPLUS-EXT.md
SURPLUS-REVIEW.md
SURPLUS.md
TEMPLATE-ATTACK.md
ZHEGLOV-LTEST.md
ZHEGLOV-SCOPE.md
conjectureE-plan.md
dist/ZENODO-METADATA.md
lean/README.md
lib/FAMILIES.md
lib/FASTCOEF.md
notes.md
ops/msolve-issue-draft.md
phase0-email-draft.md
plan-72-108.md
postverdict.md
xmodel/grok-eval-20260812.md
xmodel/grok-thmA-review-20260812.md

exec
/bin/zsh -lc "wc -l TEMPLATE-ATTACK.md SHEET6-CLASSICAL.md xmodel/grok-eval-20260812.md SHEET6-DEPTH-REVIEW.md MATHIEU-REVIEW.md SHEET6-MP-REVIEW.md && sed -n '1,260p' TEMPLATE-ATTACK.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
     291 TEMPLATE-ATTACK.md
     338 SHEET6-CLASSICAL.md
      41 xmodel/grok-eval-20260812.md
     328 SHEET6-DEPTH-REVIEW.md
     255 MATHIEU-REVIEW.md
     320 SHEET6-MP-REVIEW.md
    1573 total
# TEMPLATE-ATTACK.md — the seven rigid templates under the five-angle composite attack (multi-pole book td = 6..14: 27 → 23)

Status: SYNTHESIS (judge-adjudicated), 2026-08-12. Ground: BOOK-BASH.md +
BOOK-BASH-R2.md §§0–3 (the fully adjudicated 22-class/75-instance book, 7
surviving template classes / 27 instances), SHEET6-TEMPLATE.md (genome),
SHEET6-L1.md (§5 rigid solve, §7.2 global layer), SHEET6-CLASSICAL.md,
SHEET6-MULTIPOLE.md (MP0–MP9), SHEET6-DEPTH.md (DS1–DS4), SHEET6-R1.md
(§16–17), SIGRAY-AUDIT.md, thesis refs/sigray_full.pdf. Five angles were
fired at the shared rigid-template mechanism and adversarially reviewed
(3 votes each): **four banked** (Galois/rationality OBSTRUCTION, panel-budget
OBSTRUCTION, classical battery KILL, Weyl-quantization OBSTRUCTION — the
last on a 2–1 split, riders in §6), **one refuted** (L1 §7.2 global
branch-budget sum; §4). All arithmetic exact (int/Fraction); every harness
gated on the promoted td=6 residue-A record (gate PASS in every run); no
repo files modified.

## 0. Verdict

**The live multi-pole book shrinks 27 → 23 instances. Four panel
instances are DEAD by a new, shared, review-confirmed (3 votes)
topological mechanism** — e-ladder primitivity (Def 3.1(ii):
gcd(k̄_V, ν_V) = 1 at every characteristic vertex) composed with the
MP6(b) equal-quotient synchronization (one common i = b_e·α·∏ν_seg
across the r merge edges):

1. **IIa(2,3,1)M2@w4, m=3 td12** — 2-adic i-sync disjointness (pole side
   v₂ = 1 vs cascade side v₂ ≥ 2).
2. **IIa(2,7,1)M2@w4, m=3 td12** — same 2-adic mechanism.
3. **IIa(3,5,1)M3@w2, m=3 td14** — parity disjointness (odd ∏ν at the
   n3-poles vs forced-even via the unique (ν,n) = (2,2) 3→2 contraction
   at the n2-pole; r = m = 3 forces all three at the jump).
4. **ZCH(2,3,2)M2@w6, m=2 td12** — mod-3 vs coprime-to-6 (0-chain needs
   3 | ∏ν by the case-III handshake ν_last·w_last = 6; the s-chain at
   w0 = 6 forces ∏ν coprime to 6; no common i exists).

The same laws prune **7 (2,3)-type a=2,ν=2 pole entries book-wide**
(k̄_P = a(α+β) = 10, gcd(10,2) = 2: pole vertex imprimitive) plus 2
residue-A entries by parity sync — residue-A loses 6 entries across 5
panels without losing a panel; the @w4 m=2 td12 panels survive on
narrowed entry sets.

**Equally load-bearing: three independent shield theorems now delimit
where the closing kill can live.** Galois descent, full-configuration
budget composition, branch/count arithmetic, and vertex-local
quantization are each PROVED to have zero traction against the rigid
templates — the discriminating content of the whole program is pinned to
the coefficient tier at the resonant direction (L1 §7.2: R1 staged
Puiseux transport + R2 x-side cancellation-depth window), and that
target now carries three new exact constraints (§1c). One structural
argument there closes td ≤ 14 multi-pole outright. No new td becomes
fully excluded (td = 7, 11, 13 remain the only ones): residue-A survives
in all 10 of its panels.

## 1. The composite result

### 1a. Kill layer (classical battery; review-confirmed 3/3)

New law **L6** (printed tier, on-page verified): at every characteristic
vertex the e-sequence must drop by exactly ν, forcing
**gcd(k̄_V, ν_V) = 1**, with k̄_P = κ_P(1−π_P) = a(α+β) at poles (Prop
4.1 equality) and k̄ = w(ν+1) at w-conserving segment vertices (DS2,
n = 1). Composed with **L5** (MP6(b)/St 3.17(i)/Prop 8.1(i): common
i = b_e·α·∏ν_seg across merge edges):

- at w = 2, 4 every segment ν is odd; at w = 6 coprime to 6; at w = 3
  the unique one-step 3→2 contraction vertex is (ν,n) = (2,2) — these
  cap-free divisibility invariants produce the four panel kills above
  (exhaustive attach searches confirm within engine caps; the 2-adic /
  mod-3 / parity kills themselves are cap-free given L6);
- the a2ν2-(2,3) pole entry dies outright everywhere (gcd(10,2) = 2).

Zero-slack control: the battery's T2a Jacobian-valuation test is proved
IDENTICALLY equivalent to Prop 4.1 (ord_u f_y = −(d_P + π_P) at a simple
pattern root), so it passes for all seven templates by construction —
the battery kills nothing by accident, and the four kills are genuinely
new content. Engine /tmp/classical6.py, 80 checks, 12 FAIL = the kills;
gate = residue-A td6 + m2td12 mixed entry reproduced cell-for-cell
(common i = 10, cross-pole Ξ = 20 both routes).

### 1b. Shield layer (three negative results, banked)

**(S1) Galois/rationality (74 exact checks, 0 FAIL).** All seven
templates are exactly conjugation-equivariant: τ: √d → −√d (resp. the
S3/S4 orbit action) maps the complete pinned data set onto itself with
pole chains swapped; every swap-invariant forced constant lies in
Q·σ^weight. Forced a priori: the defining laws are polynomial systems
over Q, their solution sets are Galois-stable, and rigidity forces
self-conjugacy up to pole swap. **Galois descent can never kill a rigid
template derived from rational laws.** Census: merge fields Q(√ν) for
the r = 2 cells (disc = σ²/ν); (3,5): irreducible cubic
50t³−50t²+15t−1, Galois S3, one real direction; (4,7): the recorded
quartic re-derived, Galois S4 three independent ways — maximally
generic orbits, no subfield available to any future descent.

**(S2) Panel-budget transparency (28/28 witnesses).** On the all-b=1
axis every object above the jump cell (pole rows, M=1 segments,
resonant contractions, all-μ=1 cascade merges) carries λ = 0 by the MP8
Euler-equality itemization — the R1/R2 suffix budgets td−2 / td−1−ψ
WERE the full-configuration budgets; the stated slacks are real.
Every feeding entry of all 27 instances is b = 1 (b ≥ 2 rows live only
in the off-axis multisets and feed no cell), and "b ≥ 2 forces a second
jump" is unprovable at printed tier (Prop 8.3 propagates only M = 1
downward). Explicit full-configuration witnesses exist for all 28 book
instances of the 7 classes: **composition arithmetic can never kill
these panels.**

**(S3) Quantum vertex transparency (Weyl gauge; 2–1 banked).** Chart
transport is quantum-exact (conjugation by exp(φ(x))); the first
invariant Moyal correction lands exactly 2κ̄_F below every bracket-window
top, and every rigid pinning equation (merge solve, suffix B = (3/2)A,
pole ODE ⊖ = 3λmw⁴, E1–E7 transports) is the top of its own window:
**the seven templates satisfy the quantum vertex equations with
identical coefficients**, and the 48 killed instances die identically in
A₁ (top-level T1 solves, correction-free). Direction of implication
honest: JC₂ ⇒ DC₁ only — this is delimitation, not a kill path.

### 1c. Active data extracted for the remaining layer

1. **Covariance selection rule (S1):** any correctly derived pinned
   datum of the §7.2 layer / R1 transport / per-panel E-ladders must be
   a single rational function evaluated along the direction orbit
   (S3/S4-equivariant for (3,5)/(4,7)), and any swap-invariant forced
   constant must be rational in the scale. Kill-certificate searches may
   be restricted WLOG to the τ-invariant rational subring; a
   non-covariant or irrational-invariant output is an automatic error
   certificate. (Retroactively explains the failed R1 13.1-bracket kill:
   an exact τ-conjugate pair, identically zero.)
2. **Quantum deg-0 datum (S3):** criticality census D_crit =
   D_F + D_g − 3κ̄ makes residue-A@w2 and @w4 (2,3)-entries the UNIQUE
   exactly-critical cells (D_crit = 0); ZCH@w6 is fully
   quantum-transparent (D_crit = −10). At the residue-A merge the
   parameter-free correction V(t) = Π³(f_top, g_top) is degree 9,
   divisible by the pattern p (V(aᵢ) = 0 — the pinned handoffs are not
   charged), and **nonzero exactly at the resonant direction:
   V(b = 2σ/3) = −878σ⁹/9261**. The entire first-order quantum
   divergence concentrates in the deg-0 stratum at b — the same single
   direction as the L1 §7.2 layer. Quantum-R1 = classical-R1 +
   (1/24)p·W: a zero-slack classical closure of §7.2 kills the quantum
   shadow outright, and conversely at (2,3)-critical panels.
3. **Two-jump quarantine narrowed (S2, conditional):** the attainable
   M=1 branch-arrival alphabet across all 10 surviving panels is exactly
   {2,3,4,6}, while five of seven templates emit strictly fractional
   child closures — **all two-jump (mixed-merge) trees die at m = 3**;
   at m = 4, td = 12 the only shape not w-killed is the double-residue-A
   pair-jump joining at w = 3/2, whose unique continuation cell
   IIa(2,5,1)M2 κ̄ = 4 is per-edge consistent (n_e = 7, D/i = 5/2).
   Conditional on extending case-II transport along the emitted M ≥ 2
   chain; μ_e = 2 arrivals stay quarantined.
4. **New coefficient pins for the unrun E-ladders (S2):** IIa l=0
   cascades are T1-rigid — pt = t^r + p₀, c̃ = ρp₀ ≠ 0, forcing
   c_e^{rν} equal across the arriving orbit (r = 2: c₁^ν = −c₂^ν);
   I(ν=1, l=1) forces b = σ/2, c̃ = −disc/6.

## 2. Updated survivor table (per class / per panel)

| class | cell / child | panels before | killed this round | surviving panels (23 total) | entry narrowing / notes |
|---|---|---|---|---|---|
| IIa(2,3,1)M2@w2 residue-A | κ̄5, (5,3,1/2) | 10 | 0 | m=2 td6,8,9,10,12,14; m=3 td9,12,14; m=4 td12 | 6 entries dead across 5 panels (a2ν2-imprimitive ×4: m2td9 e2, m2td12 e3/e4, m3td12 e2; parity-sync ×2); all shields apply; (2,3)-entries exactly quantum-critical |
| IIa(2,3,1)M2@w4 | κ̄10, (10,6,1) | 4 | **m=3 td12** | m=2 td12; m=4 td12; m=2 td14 | m2td12 entries e2/e3 dead (a2ν2); (2,3)-entries quantum-critical (D_crit = 0) |
| IIa(2,7,1)M2@w4 | κ̄11, (11,7,1/2) | 4 | **m=3 td12** | m=2 td12; m=4 td12; m=2 td14 | m2td12 entries e2/e3 dead (a2ν2); super-critical (D_crit = +2) |
| IIa(2,5,1)M2@w3 | κ̄8, (8,5,1/2) | 3 | 0 | m=2 td10,12,14 | passes the full classical battery (i-sync consistent, valid splice, parity); also the unique w = 3/2 two-jump continuation cell |
| IIa(3,5,1)M3@w2 | κ̄7, (7,5,1/3) | 3 | **m=3 td14** | m=3 td12; m=4 td12 | m3td12 entry 2 dead; W-deg-2 lever (§5) now kills 2 panels, not 3; S3 merge orbit, 1 real direction |
| IIa(4,7,1)M4@w2 | κ̄9, (9,7,1/4) | 1 | 0 | m=4 td12 | battery PASS (κ = 42, pairs (3,1)(7,5)(2,13), μ even); 2 OPEN tier-2 μ=3 III-E5 nodes still unresolved; S4 merge orbit |
| ZCH(2,3,2)M2@w6 | κ̄10, (10,4,1) | 2 | **m=2 td12** | m=4 td12 | survives via 3-pole cascade witness (r′=3, ν₁=3, i=18); fully quantum-transparent (D_crit = −10) |

## 3. Census and per-td ledger after this round

    panel      survivors before | killed here | survivors after
    m=2,td= 6         1         |     0       |   1 (residue-A)
    m=2,td= 8         1         |     0       |   1 (residue-A)
    m=2,td= 9         1         |     0       |   1 (residue-A)
    m=3,td= 9         1         |     0       |   1 (residue-A)
    m=2,td=10         2         |     0       |   2
    m=2,td=12         5         |     1       |   4 (residue-A, 231@w4, 271@w4, 251@w3)
    m=3,td=12         4         |     2       |   2 (residue-A, 351@w2)
    m=4,td=12         6         |     0       |   6 (all seven classes' m4 instances)
    m=2,td=14         4         |     0       |   4 (residue-A, 231@w4, 271@w4, 251@w3)
    m=3,td=14         2         |     1       |   1 (residue-A)
    TOTAL            27         |     4       |  23

Book totals: DEAD 48 → **52 of 75**. Per-td multi-pole residue: td6 = 1,
td8 = 1, td9 = 2, td10 = 2, td12 = 15 → **12**, td14 = 6 → **5**.
Fully excluded td: **7, 11, 13 unchanged** (residue-A survives in every
non-empty panel; composite td independently blocked by the TDU
single-pole residual).

## 4. Refuted attempts (one line each)

- **L1 §7.2 global h-branch budget sum** (this round): REFUTED 2–1 —
  the td=6 zero-slack closures (deg h1 = 224 = 168+56, deg h2 = 552 =
  414+138, total x-ray resonance, δ-law) verified by all three referees,
  but the headline corner-erratum was filed against the wrong document
  and the class-universal "no branch-count kill exists" overclaimed past
  the banked records; demoted to unbanked corroboration that the §7.2
  layer is coefficient-tier, not count-tier.
- **Galois descent kill:** structurally impossible — rigid solutions of
  rational laws are self-conjugate up to pole swap (a-priori theorem +
  74 checks); retained as checksum only.
- **Panel-budget squeeze / full-configuration pricing:** empty — MP8
  makes every pre-cell object a zero λ-row; suffix budgets were already
  full budgets (28/28 witnesses).
- **"b ≥ 2 entry forces a second jump":** unprovable at printed tier
  (Prop 8.3 is M=1-only downward) and vacuous on the book axis (all
  feeding entries b = 1).
- **Weyl vertex-tier quantum kill:** zero traction — every rigid solve
  is the top of its bracket window, corrections land 2κ̄ lower.
- **T2a Jacobian-valuation test vs ladder-consistent templates:** no
  kill power — identically Prop 4.1.
- **R1 13.1-bracket kill (prior session):** its bracket sum is an exact
  τ-conjugate pair with zero rational part, identically zero — failure
  now explained, not just observed.

## 5. Errata / adjudications required before the next build

1. **SHEET6-TEMPLATE.md 2c-E5, line 237 vs 239: exact factor 3** in the
   w_i⁴ denominator (81 vs 243), verified at two gauges; the R1 sat rows
   (SHEET6-R1-Q2E5.md §1.5, 729-normalization) sit on the 239 side, and
   §1.3's stray "81·7¹² not 243·7¹²" remark corroborates the conflict.
   Rational and pole-symmetric (Galois-irrelevant) but load-bearing for
   any R1 rerun with E5 quartic rows. ADJUDICATE FIRST.
2. **h2 corner spec discrepancy** ((7/2)(126,42) = (441,147) vs
   (23/7)(126,42) = (414,138)): the arithmetic conflict is real per all
   referees of the refuted angle, but its claimed location was
   misattributed — re-locate the (441,147) spec in the banked R2 window
   documents and adjudicate before staging the window (27 spurious rows
   / 9 spurious columns otherwise).

## 6. Honest riders

1. The Weyl shield (S3) is banked on a 2–1 split; the dissent flagged
   (i) loose wording in the "48 instances die in A₁" corollary against
   the kill book and (ii) one unproven step in the pattern-tier
   cleanness theorem. Its computational core (V(t), criticality census)
   was verified by all three referees, including a full independent
   reimplementation. Treat the deg-0 datum as solid, the theorem-tier
   prose as needing one tightening pass.
2. The classical-battery kills carry the stated caveats: multi-step
   w-contraction routes swept within engine caps (the deciding
   2-adic/mod-3/parity invariants are cap-free given L6); ZCH 0-root
   multiplicity taken at δ = 0 per the book's own dp-accounting;
   hierarchy panels with sub-jump merges marked ALIVE conservatively.
3. Claim 1c.3 (two-jump narrowing) is conditional on case-II/handshake
   transport along the emitted M ≥ 2 chain; μ_e = 2-arrival
   normalization remains quarantined — the perimeter is narrowed, not
   closed.
4. Survival remains superset-sound (P-realizability untracked); the
   per-direction E5/E6 context ladders for (2,5), (2,7), (3,5), (4,7)
   are still UNRUN — the covariance rule of 1c.1 is a falsifiable
   checksum on those future runs.

## 7. The sharpest remaining frontier — and the next step

**Frontier.** The shared mechanism is now triangulated from three
independent directions: the closing kill cannot be descent (S1), cannot
be composition/budget arithmetic (S2), cannot be vertex-local — classical
or quantum (S3, plus the whole T1–T4 record) — and (unbanked but
thrice-verified) is not a branch-count identity at infinity. What
remains is exactly the **L1 §7.2 global layer in its coefficient-tier
form: the R1 staged Puiseux transport and the R2 x-side
cancellation-depth window of h1 at the resonant direction b = 2σ/3**,

exec
/bin/zsh -lc "sed -n '261,340p' TEMPLATE-ATTACK.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
where (i) the R1 mod-p program has already killed one witness family at
depth 84 (SHEET6-R1 §17, strong-evidence tier), (ii) the quantum
divergence concentrates with explicit nonzero inhomogeneity
V(b) = −878σ⁹/9261, and (iii) the covariance rule cuts the search space
to the τ-invariant rational subring with a built-in error certificate.
A kill there at td=6 propagates by frame-homogeneity to all 10
residue-A panels and to the @w4 classes sharing the merge solve — and
with the (3,5,1) lever below, to effectively the whole book.

**Concrete next step (one sequenced session):**
1. Adjudicate erratum §5.1 (E5 factor 3) — blocking, pure arithmetic.
2. Re-locate and fix the h2 corner spec (§5.2).
3. Build the R2 h1 x-side window for the td=6 gate panel: the 70
   staged cancellation-depth columns at the undisputed h1 corner
   (56,168), exact arithmetic mod p at depth 84, restricted WLOG to the
   τ-invariant rational subring, targeting the resonant-direction
   column block; monitor with the covariance checksum (any
   non-covariant pinned output = error certificate). A rank deficit in
   the b-block is the kill.

**Secondary lever (cheap, parallel):** the IIa(3,5,1)M3@w2 TEMPLATE-
genome run — its W-residual sits at deg 2 vs the residue-A-pattern
demand deg ≤ 1; a per-panel absolute κ-ladder through the μ=3, ν_F=1
first suffix vertex demanding deg ≤ 1 kills both remaining (3,5,1)
panels at once (m=3 and m=4, td12), shrinking the book to 21 and
emptying the S3-orbit class.

Artifacts (session, outside repo): /tmp/galois_audit/{audit,covariance}.py,
/tmp/panel_squeeze.py, /tmp/classical6.py (+ /tmp/c6_full.log),
/tmp/qvertex2.py, /tmp/qvertex3.py, /tmp/qcensus.py,
/tmp/global_h1_sum.py (refuted-angle record, retained for salvage).
Repo grounds read-only throughout.
exec
/bin/zsh -lc "rg -n \"2\\*gen|gen\\+2|stabil|finite|Front|counter|weak|gap|replay|state\" SHEET6-DEPTH-REVIEW.md | head -n 100" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
6:DS4 (menu factorization), the Lemma (§6), the restored finite book (§8) —
22:- Front 1 (conservation law): **CONFIRMED** — re-derived from printed
26:- Front 2 (characteristic-vertex claim vs SIGRAY-AUDIT): **CONFIRMED under
30:- Front 3 (menu-through-w factorization): **CONFIRMED** — handshake and
32:  reach data are state-dependent existence certificates, not book data,
34:- Front 4 (d₀ = gen(W)+2): **STATEMENT VERIFIED THROUGH gen 4 WITHIN CAPS;
35:  PRINTED PROOF INCOMPLETE** — the §6(⊆) replay sketch supports only
36:  d₀ ≤ 2·gen+2; the sharper gen+2 is empirically tight at gen 3 and never
37:  violated (§4). One substantive fix owed; finiteness and td = 6 unaffected.
38:- Front 5 (mechanical): **CONFIRMED + EXTENDED, no violation found** (§5).
39:- Front 6 (final book spec): **DELIVERED** (§6).
41:Net: **the lemma STANDS** (claims 1, 2, 3, 5, 6 at their stated tiers;
43:repair, safe fallback 2·gen+2). The finite-book restoration (§8) stands.
47:## 1. Front 1 — the conservation law, re-derived branch by branch
99:does not depend on the proposition's unstated choice of P. DS1(d) is
134:## 2. Front 2 — survival under SIGRAY-AUDIT's forced readings
146:St 6.2 "in particular" clause anywhere in the doc. Front 2 is clean.
148:## 3. Front 3 — the factorization, hunted for leaks
162:  the frame state. Verdict: these are existence certificates for
165:  doc's §5a parenthesis flags the state-dependence explicitly, deferring
183:## 4. Front 4 — d₀ = gen(W)+2: the one real flaw
187:finite: confirmed (numerator strictly divides-and-contracts). Claim 1
188:(finite alphabet) and claim 2 (menu ⊆ Menu(W), finite) are PROVED at the
189:stated tier. Claim 3's (⊆) direction — every deep menu item realized by
190:depth d₀ = gen+2 — has an incomplete printed proof:
192:- The replay argument compresses a deep path to its resonant steps plus
196:  state is a dead end (fine); when n_F | w′ an interposed l = 0 step may
199:  written therefore proves realization by depth ≤ 2·gen+2, not gen+2.
206:  exceeded gen+2, and attains it** (maxFirst = 5 = gen+2 at w₀ = 405 and
207:  512, gen 3; maxFirst = 4 = gen+2 at w₀ = 128, gen 2). Step laws held on
211:Verdict: the CONSTANT gen+2 is true in every instance examined and tight;
213:restate d₀ ≤ 2·gen(W)+2 (which the doc's own argument proves, and which
214:changes nothing downstream — finiteness, menu content, W, and td = 6
220:## 5. Front 5 — mechanical verification and extension
226:  containment, stabilization at gen+2 vs depth 8, closed-form superset;
245:## 6. Front 6 — the FINAL book spec (deliverable)
248:enumeration workflow as-is. All layers finite per (m, td).
295:1. **§6 claim 3 (the one substantive fix)**: the (⊆) replay proof
296:   supports d₀ ≤ 2·gen(W)+2, not gen(W)+2 — restate with the safe
298:   lemma (resonant-from-resonant needs n_F | w′; n_F ∤ w′ states are
299:   dead ends — half the lemma is already in this review). Keep gen+2 as
316:   stabilization filter excludes I-family cells — this review verified
317:   they stabilize within the same d₀ (record it, e.g. as check 8).
326:    # gen-3/4 stress + full-menu (I-family) stabilization: inline sweeps

exec
/bin/zsh -lc "sed -n '148,324p' SHEET6-DEPTH-REVIEW.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
## 3. Front 3 — the factorization, hunted for leaks

- Handshake: from (c)+(d) i-normalized, κ̄_m − D_m/i = (κ̄_e − ρ_e)/ν_e =
  w_e in one line — re-derived; cell-independent as claimed. Join =
  common (κ̄_m, D_m/i) ⟹ common w (subtraction); conversely same (w,
  cell) ⟹ same child datum w·(dq_c, dp_c, 1)/Δ_c (two linear equations).
- §5b windows re-derived: dq_c ≤ (r+1)Δ_c holds in all three families for
  l ≥ 1 (IIa: r(lν+1−ν) ≥ 0; ZCH: rν(l−1)+ν−1 ≥ 0; I: r(l−1) ≥ 0), so
  κ̄_m ∈ (w, (r+1)w] ∩ ℤ; the three ν-determination identities re-derived
  (IIa: ν(wr − Di·l) = Di; ZCH: ν(l·Di − w(r−1)) = w; I: l = wr/Di).
  Finite per (w, r) as claimed. Cascade map w ↦ w(r+l)/(lν+1)
  (ν-independent = r·w at l = 0) re-derived; composed ≤ m−1 times by MP1.
- The hunt: MP-REVIEW §5a's per-edge bounds (n_e ≤ (rκ̄_e −(r+l)ρ_e −1)/l
  etc.) are NOT functions of w alone — they depend on (κ̄_e, ρ_e), i.e.
  the frame state. Verdict: these are existence certificates for
  reachability, not book data; every datum the book records — (family,
  ν_c, l, M, κ̄_m, D_m/i, child frame) — is (w, cell)-determined, and the
  doc's §5a parenthesis flags the state-dependence explicitly, deferring
  it to §6. l's range per (w, r, κ̄_m) is w-determined by the window +
  determination equations; l's realizability per frame is not, and need
  not be. M = gcd(dp_c, dq_c): cell-determined. r ≤ m: layer T. μ_e = 1:
  forced. i, l_f, coefficient solves: instance/coefficient layer, outside
  the pattern book by design. NO LEAK FOUND. Machine cross-check: closed
  form Menu(w) ⊇ every swept frame menu at every reached frame, all
  entries incl. adversarial (§5).
- ZCH correction (§5c): re-derived from (e)–(h); the corrected handshake
  ν_e·w_e and the join filter "w's in integer ratio ν_e ≥ 2" are exact
  consequences; the case-(III) classification of the 0-edge is proved,
  not assumed (0-coefficient at π(G_m) ⟹ off-support ⟹ non-
  characteristic; V₁ₐ membership from ν_m ≥ 2; u > α_{j−1} strict by
  descent-consecutiveness). Check 7's model matches (n = n′ν_m ∈ ℕ*).
- Root (§5d): (k) is (c) with n forced to ν_e − κ̄_e; (j) ⟺ n* ≥ 1;
  handshake 1 − D/i = w_e re-derived; w < 1 NECESSARY for root merges —
  confirmed, with one directionality nit in §8(iii) (see §7 item 3).

## 4. Front 4 — d₀ = gen(W)+2: the one real flaw

gen(W) = number of BFS generations of the arithmetic closure W(w₀) under
w ↦ w·n/Δ, Δ | num(w), Δ ≥ 3. The 2/3 constant: confirmed (§1a). W
finite: confirmed (numerator strictly divides-and-contracts). Claim 1
(finite alphabet) and claim 2 (menu ⊆ Menu(W), finite) are PROVED at the
stated tier. Claim 3's (⊆) direction — every deep menu item realized by
depth d₀ = gen+2 — has an incomplete printed proof:

- The replay argument compresses a deep path to its resonant steps plus
  "one l = 0 step". But resonant-step admissibility from a resonant child
  (w′, ν_F, n_F) — and even l = 0 admissibility from it — requires
  n_F | w′ (for integer w′: n_e = ...− w′/n_F ∈ ℤ). When n_F ∤ w′ the
  state is a dead end (fine); when n_F | w′ an interposed l = 0 step may
  still be needed before the next resonant step (positivity
  n_Fν_Fν′ > Δ′ can fail from the raw resonant child). The argument as
  written therefore proves realization by depth ≤ 2·gen+2, not gen+2.
- Adversarial machine hunt (this review): entries at w₀ = 8, 12, 16, 24,
  27, 30, 36, 60, 64, 105, 128, 147, 149, 173, 203, 210, 405, 512, 720
  (gen up to 4), fractional w₀ ∈ {3/2, 4/3, 7/4, 25/12, 19/9}, depth
  ≤ 10, caps ν ≤ 30, n_pat ≤ 10, first-appearance depth recorded for
  EVERY cell (jump cells, I-family, M = 1 cascade cells — the doc's
  checker only tracks `jumps()`): **maximum first-appearance depth never
  exceeded gen+2, and attains it** (maxFirst = 5 = gen+2 at w₀ = 405 and
  512, gen 3; maxFirst = 4 = gen+2 at w₀ = 128, gen 2). Step laws held on
  every edge (0 violations across ~10⁴ edges); reached w-sets ⊆ W(w₀)
  always.

Verdict: the CONSTANT gen+2 is true in every instance examined and tight;
its proof is not complete as printed. Required fix (§7 item 1): either
restate d₀ ≤ 2·gen(W)+2 (which the doc's own argument proves, and which
changes nothing downstream — finiteness, menu content, W, and td = 6
(gen 0, both give 2) are d₀-insensitive) — or supply the missing chaining
lemma. Caveat inherited from the doc's §9 (correctly flagged there): the
empirical d₀ verification is cap-limited; the menu CONTENT conclusions
are cap-free via §5b.

## 5. Front 5 — mechanical verification and extension

- depth_closure_check.py: 13/13 PASS re-run, exit 0. The checks verify
  what they claim: (1) per-edge law W/D/contraction on every BFS edge;
  (2) the td = 6 record incl. menu constancy 1–12 and the exact two-cell
  pre-suffix menu; (3+4) 10 real (m=2, b=1, td ≤ 12) entries, closure
  containment, stabilization at gen+2 vs depth 8, closed-form superset;
  (5) St 9.6(v) w ≡ 3/2 (re-derived by hand here as well: w =
  3(2s+1)²/(2(2s+1)²) = 3/2 identically); (6) all 26 promoted phase-4
  shapes have w = 2 at every instance; (7) the corrected case-(III) ZCH
  solve: 403 cells, none joinable at W = {2}.
- Entry-list note: check 3's entry generator imposes (α ≡ 0, β ≡ 1) or
  (β ≡ 0, α ≡ 1) mod ν — this is the pole q-shape pin dq ≡ 1 (mod ν) at
  b = 1, and it forces w₀ ∈ ℤ on the whole M=1 axis; fractional w enters
  only through m ≥ 3 cascade children. Consistent, worth a comment line.
- 351/351: twopole_check.py l1only re-run — 26 shapes, RESIDUE child
  (1/2, 3, 2, 5) at 351 parent pairs, ZCH suffix-DEAD ×276, ν=1 ODE-dead
  601 — and the w-formula PREDICTS the child: 2·(10, 6, 1)/4 =
  (κ̄, D/i, ρ) = (5, 3, 1/2). The "explains 351/351" claim is exact.
- Boundary adversarial (this review): w = 1 entry — no κ̄_m = 1 root
  cell anywhere (strictness of w < 1 confirmed); w = 2/3 and 3/4
  entries — root cells appear (9 and 6 resp.); w = −1/2 entry — no
  admissible children at all (inert); no frame with w ≥ 1 ever admitted
  a κ̄_m = 1 cell across all entries. §5d's picture is exact.

## 6. Front 6 — the FINAL book spec (deliverable)

Merge of SHEET6-MP-REVIEW §5c with this lemma's w-index; hand to the
enumeration workflow as-is. All layers finite per (m, td).

    BOOK(m, td), m ≥ 2, 3m ≤ mβ ≤ td:
    E. Entry layer (printed): type (α,β), 2 ≤ α < β, gcd = 1, mβ ≤ td;
       partition td = ΣΛ_i, Λ_i ≥ β; per pole (a_i, b_i, ν_i) with
       Λ_i = a_i b_i αβ/ν_i, ν_i | α or ν_i | β, plus the q-shape pin
       (b_iβ ≡ 1 mod ν_i when ν_i | α, symmetrically); Q(P_i) =
       (a_iα, b_iα, ν_i, b_i, a_i(α+β)); b_i = 1 forced at Λ_i = β or
       Λ_i prime. Each M=1 entry carries w₀ = a_i(b_i(α+β)−1)/(b_iν_i)
       (∈ ℤ at b_i = 1); num(w₀) ≤ td²/2.
    T. Tree layer (printed): rooted trees, m leaves, Σ(r−1) = m−1,
       r(G) ≤ m, no merge below G*.
    C′. Chain layer (CLOSED by the lemma; H1): an M=1 segment is coded
       by w alone. Alphabet: W = closure of the entry w₀'s under
       (i) resonant steps w ↦ w·n/Δ, Δ = (n−1)ν+1 ≥ 3, Δ | num(w),
       n ≥ 2, ν ≥ 2 (< log_{3/2}num(w₀)+1 per segment; all other steps
       fix w), and (ii) M=1-emitting merges w ↦ w·(r+l)/(lν+1), composed
       ≤ m−1 times. Segments of arbitrary depth realize no cell data
       beyond depth d₀ (≤ 2·gen(W)+2 proved; gen(W)+2 machine-verified
       through gen 4).
    J′. Jump layer, indexed by (w, cell), w ∈ W: cells (family, ν, l)
       with κ̄_m ∈ (w, (r+1)w] ∩ ℤ (integrality via St 9.1 + corrected
       St 3.8), Di := κ̄_m − w, ν DETERMINED per (κ̄_m, l): IIa
       ν(wr − Di·l) = Di; I l = wr/Di (ν = 1); M = gcd(dp_c, dq_c) ≥ 2,
       gcd(M, ν) = 1, M | r ≤ m outside ZCH; child datum (κ̄, D/i, ρ) =
       w·(dq_c, dp_c, 1)/Δ_c. Filters: all non-0 edges are case (II) with
       handshake κ̄_m − D_m/i = w (joins force equal w); ZCH 0-edge is
       case (III): solve with n′ ∈ (1/ν_m)ℕ*, handshake ν_e·w_e — ZCH
       reachable only if arriving w's stand in integer ratio ν_e ≥ 2.
       Coefficient layer per cell (out of pattern book): Prop 8.1(iv)
       rigid solve + the MP §8-item-3 coefficient-vs-ratio match.
    R. Root layer (printed + H1): case (IV), n* = ν_e − κ̄_e ≥ 1 forced
       ((j): κ̄_e < ν_e — keep as the engine filter; w_e = 1 − l_f/i₀ ∈
       (0,1) is the implied frame-free necessary form: root merges dead
       whenever W ∩ (0,1) = ∅), plus (l) d < deg p_G, (m) M-divisibility,
       l odd, l ≤ td−2, k_f = (r+l)l_f, ψ = r+l−1.
    S. Suffix layer (printed): MP2 restored kill below G*, single-pole
       engine, St 9.4 budget Σλ ≤ td−1−ψ. (Check 5's w ≡ 3/2 on St
       9.6(v) suggests the closure extends to M ≥ 2 suffixes — unproved,
       correctly out of scope.)

    Instance td = 6, m = 2: W = {2}, d₀ = 2; J′ = {IIa (2,3,1), M = 2,
    child (5, 3, 1/2)} exactly (corrected model removes ZCH pre-suffix);
    R empty (w = 2 ≥ 1); matches the promoted record cell-for-cell.

## 7. Required fixes (none demote the lemma)

1. **§6 claim 3 (the one substantive fix)**: the (⊆) replay proof
   supports d₀ ≤ 2·gen(W)+2, not gen(W)+2 — restate with the safe
   constant (nothing downstream changes), or add the missing chaining
   lemma (resonant-from-resonant needs n_F | w′; n_F ∤ w′ states are
   dead ends — half the lemma is already in this review). Keep gen+2 as
   the machine-verified sharp value (tight at gen 3).
2. **§5b κ̄_m ∈ ℤ at case-(I)/I-family merges**: DS1(c) covers only V₁ₐ
   vertices; cite St 9.1 (κ̄ = D_f + D_g on T_{a,pole}) + the
   audit-corrected St 3.8, or the equivalent lattice argument (at a
   strict V₂ₐ meet the contact exponent is in the common lattice, else
   some branch jumps and the vertex is V₁ₐ). One line.
3. **§8 engine fix (iii) directionality**: "root filter strengthened to
   w < 1 ... subsumes the κ̄ < ν pin" is backwards — (j) κ̄ < ν IMPLIES
   w < 1, not conversely (reachable hairline witness: (ρ, ν, κ̄) =
   (ν/(ν+1), ν, ν), w = ν/(ν+1) < 1, (j) fails). w < 1 is the correct
   frame-free necessary filter (and the right one-line td = 6 kill); the
   per-edge engine should keep (j)+(k)+(l)+(m). At td = 6 both kill
   everything — no promoted conclusion touched.
4. Cosmetic: §1 vs §3 edge-naming conventions (F = G + c vs G = F + c,
   both printed-faithful) deserve a one-line note; check 3's entry
   congruence (q-shape pin) deserves a code comment; the doc's `jumps()`
   stabilization filter excludes I-family cells — this review verified
   they stabilize within the same d₀ (record it, e.g. as check 8).

## 8. Reproduction

    cd cases && python3 depth_closure_check.py     # 13/13, exit 0
    python3 twopole_check.py l1only                # 26 shapes / 351 pairs
    python3 /tmp/depth_adv.py                      # this review: adversarial
                                                   # entries, boundary w,

exec
/bin/zsh -lc "sed -n '1,120p' xmodel/grok-eval-20260812.md && rg -ni \"avenue|next step|recommended|attack|monodromy|resultant|subresultant|discriminant|hurwitz|dessin|tropical|hensel|padic|p-adic|differential galois|creative telescop|ore|wronsk|trace|norm|resultant|resolution|blowup|fundamental group|braid|ramification|semigroup|conductor|intersection form|signature|lattice|motivic|d-module|holonomic|valuation|log-bmy|splice|neumann|jelonek|galois|witt|frobenius|bernoulli|mahler|syzygy|fitting|flatness|hilbert series|hilbert function|initial ideal|tropical basis|sos|positivstellensatz|real root|mason|abc|belyi\" --glob '*.md'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
I'll start by reading the campaign documents in the order you specified, then check RECON.md and notes.md so the stress test and new avenues aren't duplicates.Next I’ll pull TEMPLATE §§0–1, the end of notes.md, and RECON.md so the new-avenue list doesn’t repeat what’s already in the record.I’ve got the main theorems. Next I’ll scan the campaign record for already-proposed attacks so the five new avenues don’t repeat them.The program has reduced JC2’s sheet-6/multi-pole side to a handful of rigid templates and proved a real theorem on the strip side. The architecture that would turn those into a proof of JC2 is weaker than the writeups claim.

## 1. Stress test — three weakest load-bearing points

**A. Residue-A is treated as an object that “must die.”**  
Claim: IIa\((2,3,1)\,M=2@w=2\) (genome \(Q=(6,12,3,2,5)\), \(a_1/a_2=2\pm\sqrt{3}\), \(b=(2/3)\sigma\), \(B=(3/2)A\)) is the multi-pole bottleneck, and some unprinted global layer (L1 §7.2 / R1–R5) will kill it.  
Why fragile: it has now survived every *printed* constraint (Theorem O), the full coefficient lift (five independent identities close exactly, including the h2-collapse re-deriving L1c without the ODE), and the classical battery (splice/Seifert identity, Abhyankar–Moh at the poles with **zero slack** \(\operatorname{ord}_t f_y=-39\), Jelonek). Every Groebner “kill” of it has been an artifact (msolve parentheses, \(s_{1F}=0\), unreduced mod-\(p\), vmem-cap). Zero-slack topology plus receding discriminants is the signature of a real formal object, not a near-miss. If it algebraizes, JC2 is false and the exclusion program is hunting a theorem that does not exist.

**B. “Finite enumeration at every level.”**  
Claim (DEPTH §8 + notes): prime-td + Theorem MP + depth-closure + book-bash is a finite JC2 machine.  
Why fragile: TDU §7 already says the opposite on the single-pole side — composite residual \(4\to 212\) from \(\mathrm{td}=6\) to \(16\), *no* finite list. The book itself is a **superset**: \(P\)-realizability untracked, joins conservative, all-\(\mu_e\ge 2\) mixed merges quarantined (\(m\ge 3\), only possible downstream of a jump), off-axis \(b_i\ge 2\) outside the \(w\)-lemma. The reduction sits on P1 (Prop 8.3 read as Not 9.2 — a sanctioned typo) and H1 (Prop 9.3 case arithmetic), and the latter already drifted once (ZCH 0-edge is case (III), not (II)). One more case-label error reopens cells or silently drops them.

**C. The four single-pole r9/\(M=2\) classes are architecturally forgotten.**  
Claim in the current narrative: residue-A is “what stands between the campaign and \(\mathrm{td}\le 14\) multi-pole exclusion.”  
Why fragile: even a complete kill of all 27 multi-pole instances leaves \(\mathrm{td}=6\) open on the four thesis-forced single-pole classes (entry \(Q=(3,6,5,2,8)\), type \((3,5)\), \(M=b=2\)), and every composite \(\mathrm{td}\) independently blocked by TDU. Those four have not been hit with the T1 Wronskian ladder that just killed 15 multi-pole classes. “Multi-pole book drained” \(\neq\) “\(\mathrm{td}\) excluded.”

(Theorem A itself is not on this list. The 15-line leading-coefficient argument is solid; what is overstated is its *role* — it closes strip depth-2, not JC2.)

## 2. New avenues

Checked against RECON.md and notes.md (including the just-launched Galois / L1-§7.2 / panel-squeeze / classical-on-6 / Weyl battery, the TEMPLATE R1–R6 list, log-BMY, IIa\((3,5,1)\) \(W\)-residual, mixed-merge quarantine-as-scope, SC1, Mondello, face-isolation). These five are not in that record.

| rank | idea | why decisive / cheap | first concrete step |
|---|---|---|---|
| 1 | **T1 ladder on the 4 r9/\(M=2\) single-pole classes** | Same closed-form weapon that killed ZCH iff \((\nu+1)\mid l\) and family I iff \(l/r\) or \(r/l\in\mathbb{Z}\). Hours, exact. A hit is the first new single-pole kill since TDU and may uniformize composite \(\mathrm{td}\). | At the first non-pole \(V_a\) vertex of entry \(Q=(3,6,5,2,8)\), write Prop 8.1(iv) and run the triangular coefficient ladder (`l1_ode_check` style). Kill = \(\tilde{c}=0\) or a multiple root. |
| 2 | **Hurwitz factorization of \(\hat g:\overline{C}\to\mathbb{P}^1\) in \(S_6\)** | Classical battery used RH as a *number*. Existence of an actual degree-6 cover with the pinned local types is a different obstruction; failure kills residue-A independently of Sigray. | From Newton pairs \((7,2)(3,10)(2,5)\) at each pole, compute the local monodromy cycle type on the 6 sheets of \(\hat g\) (poles of order 3). Check whether two such classes, plus the \(x\)-side cluster (\(g\) finite there) and RH-constrained finite ramification, multiply to \(1\) in \(S_6\). |
| 3 | **\(J\)-jet at \(G_m\) on the 7 dead-stretch coefficients** | Not R1 (symmetric-function polynomiality) and not R5 (global \(J\)). The first non-constant term of \(J(f,g)\) in the \(G_m\)-chart is linear in the on-lattice free coeffs at \(17/21,18/21\) (merge) and \(9/21,12/21,15/21\) (suffix). Two Galois-conjugate poles \(\Rightarrow\) overdetermined. | Expand \(J\) to order \(1/\kappa_{G_m}\) past the pinned tops; set the first two jet coefficients to \(0\). Inconsistency or a pin that breaks \(w_i^4\) (TEMPLATE E5) is a kill. |
| 4 | **Theorem A on the depth-3 column of the two-pole support** | Connects the two successful lanes, which have been run in parallel. MATHIEU-REVIEW already has the depth-3 column \(2BE'-(k+1)B'E\). Residue-A is *not* a strip; if that column cannot vanish for the pinned leading forms, the genome is not a polynomial pair. | Take the Newton edges \((126,42)\), \((189,63)\) with root pattern \(p_R=S_R(\eta-c_0)^{126}\); extract the \(x^{k+2}\) bracket column; run the leading-coefficient lemma (MATHIEU §5.1 Step 1). |
| 5 | **Mixed-merge children of residue-A (not of off-axis entries)** | BOOK-ENUM’s “\(M\ge 2\) chain engine” is about \(b_i\ge 2\) *entries*. The live hole is a *second* merge with all \(\mu_e\ge 2\) downstream of the \(M=2\) jump, legal at \(m\ge 3\). Either the book is missing cells, or the quarantine closes. | From child \(Q=(6,12,3,2,5)\), enumerate MP6(b)/(d) mixed merges with \(\mu_e\ge 2\), \(r\le 4\), \(\mathrm{td}\le 14\). Any new \((p,q)\) not among the 27 survivors cracks completeness. |

## 3. Verdict

**P(JC2 true) \(\approx 0.72\).**

Dim-2 keeps proving the statements that are true (GMC(2), Shaska for every weight sign, no graded plane CE). Every known \(n\ge 3\) mechanism dies in the plane (Picard/\(d=3\) needle, no tangent-sweep, no graded escape). Eighty-five years without an example is evidence. Residue-A is the best formal candidate I have seen in this literature, but “passes the printed list” is exactly Theorem O, and an étale non-proper degree-6 endomorphism of \(\mathbb{A}^2\) is the thing JC2 says does not exist — consistency at vertices is cheap compared with algebraizing 126 series.

**Breakthrough** if it happens: another T1-style *criterion* (item 1, or a uniform kill of IIa\((r,rt-1,1)\), \(t\ge 2\)), or a covering-theoretic kill (item 2) that does not go through Sigray. The unrun IIa\((3,5,1)\) \(W\)-residual (\(\deg 2\) vs demanded \(\le 1\)) is the cheapest already-logged shot; I did not re-propose it.

**Stall** where the program is already stalling: R1/depth-84/deferred-band descent on residue-A (artifacts, 1.5 TB deaths, discriminants receding). Next: TDU’s growing composite single-pole residual, which no finite book-bash can finish. DC(2) is the strongest *proof* route and is blocked on 2-dimensional Schur/Parshin; it will not be this campaign’s win.

The honest fork is unchanged since L1: residue-A is either a counterexample or it dies by mathematics that is not in Sigray. Printed-tier is exhausted (Theorem O). Treat the next kill attempt that is *not* a larger Groebner core as the real experiment.
TEMPLATE-ATTACK.md:1:# TEMPLATE-ATTACK.md — the seven rigid templates under the five-angle composite attack (multi-pole book td = 6..14: 27 → 23)
TEMPLATE-ATTACK.md:10:(3 votes each): **four banked** (Galois/rationality OBSTRUCTION, panel-budget
TEMPLATE-ATTACK.md:42:**Equally load-bearing: three independent shield theorems now delimit
TEMPLATE-ATTACK.md:43:where the closing kill can live.** Galois descent, full-configuration
TEMPLATE-ATTACK.md:72:Zero-slack control: the battery's T2a Jacobian-valuation test is proved
TEMPLATE-ATTACK.md:82:**(S1) Galois/rationality (74 exact checks, 0 FAIL).** All seven
TEMPLATE-ATTACK.md:87:over Q, their solution sets are Galois-stable, and rigidity forces
TEMPLATE-ATTACK.md:88:self-conjugacy up to pole swap. **Galois descent can never kill a rigid
TEMPLATE-ATTACK.md:91:50t³−50t²+15t−1, Galois S3, one real direction; (4,7): the recorded
TEMPLATE-ATTACK.md:92:quartic re-derived, Galois S4 three independent ways — maximally
TEMPLATE-ATTACK.md:156:| class | cell / child | panels before | killed this round | surviving panels (23 total) | entry narrowing / notes |
TEMPLATE-ATTACK.md:161:| IIa(2,5,1)M2@w3 | κ̄8, (8,5,1/2) | 3 | 0 | m=2 td10,12,14 | passes the full classical battery (i-sync consistent, valid splice, parity); also the unique w = 3/2 two-jump continuation cell |
TEMPLATE-ATTACK.md:168:    panel      survivors before | killed here | survivors after
TEMPLATE-ATTACK.md:196:- **Galois descent kill:** structurally impossible — rigid solutions of
TEMPLATE-ATTACK.md:197:  rational laws are self-conjugate up to pole swap (a-priori theorem +
TEMPLATE-ATTACK.md:207:- **T2a Jacobian-valuation test vs ladder-consistent templates:** no
TEMPLATE-ATTACK.md:213:## 5. Errata / adjudications required before the next build
TEMPLATE-ATTACK.md:217:   (SHEET6-R1-Q2E5.md §1.5, 729-normalization) sit on the 239 side, and
TEMPLATE-ATTACK.md:219:   Rational and pole-symmetric (Galois-irrelevant) but load-bearing for
TEMPLATE-ATTACK.md:225:   documents and adjudicate before staging the window (27 spurious rows
TEMPLATE-ATTACK.md:233:   cleanness theorem. Its computational core (V(t), criticality census)
TEMPLATE-ATTACK.md:235:   reimplementation. Treat the deg-0 datum as solid, the theorem-tier
TEMPLATE-ATTACK.md:244:   normalization remains quarantined — the perimeter is narrowed, not
TEMPLATE-ATTACK.md:251:## 7. The sharpest remaining frontier — and the next step
TEMPLATE-ATTACK.md:270:**Concrete next step (one sequenced session):**
TEMPLATE-ATTACK.md:288:Artifacts (session, outside repo): /tmp/galois_audit/{audit,covariance}.py,
SHEET6-MULTIPOLE.md:4:MP0-MP8 + Theorem O stand as printed; MP9 stands on corrected ground
SHEET6-MULTIPOLE.md:12:RESTORED in corrected form (SHEET6-DEPTH.md §8).**
SHEET6-MULTIPOLE.md:13:Original sYNTHESIS (judge document).** Composite of three panel angles: A1 (piecewise regularity / merge cascade, T0–T7 + obstruction O; NOT REFUTED, 3/3 adversarial votes), A2 (Euler/budget ledger, Theorem M (1)–(5) + Proposition B; NOT REFUTED, 3/3 votes — all theorem clauses explicitly listed as surviving), A3 (merge pattern algebra, Theorem MPM P1–P5 + OB; adversarial record truncated at synthesis time — its clauses cross-derived by A1/A2 are grafted at full tier, its unique clauses quarantined in §7).
SHEET6-MULTIPOLE.md:20:The requested lemma splits along an exact seam, and both halves are now theorems. **Kill half:** for m ≥ 2 poles the printed Prop 8.4 machinery is restored *verbatim* on the shared suffix at and below the global meet G\* of the m characteristic sequences (M_F ≠ 1 there whenever G\* ≠ (0,y)), and is *supplemented* above G\* by a merge calculus: entry M-values are pinned per pole, M = 1 cascades are forced into rigid single-orbit shapes, every merge with an M = 1 arrival has fully pinned anatomy (k = 0, gcd menu), non-resonant merges (l = 0) can never break M = 1, and the entire M = 1 region is budget-transparent (Σλ = 0). **Obstruction half:** the verbatim multi-pole analogue of Prop 8.4 ("M_F ≠ 1 on pre-merge segments") is *FALSE* — M = 1 is FORCED pre-merge whenever the poles enter with b_i = 1 — and the surviving escape hatch is exactly the set of **resonant jump vertices** (merges with l ≥ 1 extra q-orbits and M = gcd-value ≥ 2), which provably pass every printed statement (machine-verified witness at td = 6, m = 2). Theorem MP below is therefore the *maximal* printed-tier statement: it reduces the multi-pole problem, for every (m, td), to a finite book of jump-vertex cells.
SHEET6-MULTIPOLE.md:26:(f,g) a normalized counterexample of type (α,β), 2 ≤ α < β, gcd(α,β) = 1 (Not 2.4/St 2.1, pp. 8–9; the type is global, Lemma 2.1 p. 8). T_{a,pole} = {P_1,…,P_m}, m ≥ 2.
SHEET6-MULTIPOLE.md:36:## 2. THEOREM MP (m-pole piecewise kill + merge calculus; hypothesis perimeter §4)
SHEET6-MULTIPOLE.md:44:**MP2 (restored kill, general m).** If G\* ≠ (0,y), then **M_F ≠ 1 for every F ∈ U with F ≤ G\*** (trunk and G\* itself). The printed Prop 8.4 proof (pp. 44–45) runs verbatim; the singleton hypothesis is needed only above the last merge.
SHEET6-MULTIPOLE.md:48:**MP4 (entry pin; td- and m-uniform).** At every pole, (deg p_{P_i}, deg p_{g,P_i}) = b_i(α,β) and **M_{P_i} = b_i = deg p_{P_i}/α**. Moreover b_i = 1 (hence M_{P_i} = 1) is FORCED when Λ(P_i) = β (β-minimal pole) and when Λ(P_i) is prime. In particular at the minimal m-pole degree td = mβ, ALL entries have M = 1.
SHEET6-MULTIPOLE.md:61:**MP8 (budget transparency — the obstruction's mechanism).** On the pure M=1 forest {F ∈ U : M ≡ 1 at F and at every U-vertex above F} and at every all-M=1 merge vertex (including jumps): Y(F) = ∅ and λ_F = 0. Itemizing the Euler equality (22) (Prop 7.5, p. 38) for m poles: pole clusters, chain paths, M=1 segments, and μ=1-arrival merges all contribute identically zero rows. Hence **no refinement or re-partition of any printed budget** (St 9.4/9.5 (25)–(26) p. 49, Cor 7.1 p. 39, identity (22)) can charge M=1 pre-merge ancestry even one unit, for any m and any td. The only printed per-pole cost is Λ-mass: td = ΣΛ_i ≥ mβ ≥ 3m (Props 5.7/5.8), i.e. m ≤ td/3.
SHEET6-MULTIPOLE.md:77:(⊆) Any H ∈ Ta& ∩ Va \ {(0,x),(0,y)} has deg p_H ≥ 2 (St 3.16: p has more than one root). Prop 6.8 (p. 34, verbatim: "there exist P, u, v: F = I_P(u), v ≥ u, I_P(v) ∈ T_{a,pole}" — the pole lies above H on the SAME branch) gives I_P(v) = P_s. Not 3.3's ° enumerates every Va-vertex of I_P([0,v)) in decreasing order, branch-independently; H is one of them, so H ∈ C_s.
SHEET6-MULTIPOLE.md:99:Claim: every branch P ∈ Ra\R̄a through the pure M=1 forest or an all-M=1 merge has F\*_P ∈ T_{a,pole}. Ascend along P: at segment vertices the full pattern is a single simple orbit (D5), at all-M=1 merges all roots are chain roots (D6a), at poles the branch either separates above (where deg p = 1 by St 3.17(i) + Prop 5.3(v), and St 3.16 excludes Va-membership there and above) or continues along the defining branch (Prop 5.3(ix)). So P passes through a pole vertex Q₀, and since m_F is a vertex invariant, F\*_P = Q₀ ∈ T_{a,pole}. St 7.2 (p. 35) then bans cv vertices on P; Y(F) = ∅ (literally when M = 1 holds from the pole down: every ray through the segment reaches P_i, g(P) = ∞ by Prop 5.5, no cv vertex by Prop 7.2; under the E9/H2 branch-at-F reading for mid-segment onset); λ_F = 0 (St 9.3 (24)). Ledger itemization of the equality (22), extending SHEET6-LROOT §1 to m poles: (i) pole clusters carry zero cv mass (Prop 5.5 + Prop 7.2, per pole); (ii) chain paths carry none (T_{a,cv} ⊂ T_a^0 = {d = 0}, Not 7.1, while d > 0 down to d_{(0,y)} = l_f > 0); (iii) M=1 pre-merge sub-segments: identically zero rows (D5(f)); (iv) μ=1-arrival merges: zero rows (D6e) — the l q-extras are exhibited EMPTY ledger rows; (v) the x-side keeps its ≥ ψ cost (St 9.4's proof, p. 49). Since (22) is an Euler-characteristic *equality*, no re-partition or refinement of the printed counting frame can price these objects: "≥ 1 unit per M=1 occurrence" is structurally false at every m, td. The only remaining per-pole cost is td = ΣΛ_i ≥ mβ (Props 5.7/5.8): m ≤ td/3. ∎
SHEET6-MULTIPOLE.md:120:**Open, stated, NOT claimed:** mixed merges with all μ_e ≥ 2 obey only MP6(b)/(d)-subadditivity (k = 0 needs some μ_e = 1; the l ≥ 1 forcing does not apply) — possible only for m ≥ 3 downstream of an earlier jump; the m ≥ 3 pattern-level escape (M = m via lν ≡ −1 mod m) is arithmetic existence only, r-edge H1 ratio-consistency unverified; the root-merge endgame at general td is open (closed at td = 6, m = 2); jump vertices are unkillable at printed tier (witness O — this is a theorem-grade negative, not a gap in the proof).
SHEET6-MULTIPOLE.md:122:**Record caveats:** (i) A2's third adversarial vote flagged one *subsidiary* (non-load-bearing) sub-claim as failing and one unflagged record-contradiction; the vote explicitly lists all Theorem M clauses (1)–(4), (5I), the conditional content of (5R), and Prop B as surviving, and every A2 clause grafted here is cross-derived by A1 or so listed. (ii) A3's adversarial votes were truncated in the synthesis input; A3 clauses P1/P3/P4 are independently derived by A1/A2 and grafted at full tier; A3-unique kills are quarantined in §7.
SHEET6-MULTIPOLE.md:128:**Theorem O.** No printed-tier argument can prove M_F ≠ 1 on pre-merge segments (it is false: MP5 forces M = 1 there whenever b_i = 1, which is itself forced at td = mβ and at prime Λ_i), and no printed-tier argument can exclude resonant jump vertices: the cell (r,ν,l) = (2,3,1), M = 2 at td = 6, m = 2 solves Prop 8.1(iv) exactly with rigid coefficients (a₁/a₂ = 2±√3), passes Prop 8.1(iv)-(v), St 8.2/8.4, the root/eta laws, all located budget statements (Σλ = 2 ≤ 3 globally, 0 through the merge), and the entry pins — machine-verified (cases/l1_ode_check.py; SHEET6-2POLE §6a full hand-verified exhibit, every datum absolute). The blind spot is structural and r-uniform: the l extra q-orbits are invisible to every printed statement except deg q (SHEET6-L1 §3). Combined with MP8 (spend 0), the residual is irreducible: **MP0–MP9 is the maximal printed-tier kill**, and the multi-pole problem reduces, for each (m, td), to the finite book of resonant jump cells pinned by MP6/MP7 + the equal-quotient law + Prop 9.3's per-edge ratio equations (pp. 50–51), with entries pinned by MP4.
SHEET6-MULTIPOLE.md:140:7. **Killing the jump vertex itself from printed statements**: impossible — the (2,3,1) M = 2 cell is a consistent exhibit solving every located printed constraint (Theorem O).
SHEET6-MULTIPOLE.md:147:From Theorem MPM (pattern-algebra angle; statement complete in the panel record, votes truncated at synthesis). These sharpen the jump book but are NOT counted in Theorem MP:
SHEET6-MULTIPOLE.md:155:## 8. The sharpest remaining gap, and the concrete next step
SHEET6-MULTIPOLE.md:157:**The gap.** Everything printed now funnels into a single residual object: the **resonant jump vertex** — an all-M=1 merge with l ≥ 1 extra simple q-orbits, M = gcd(r, lν+1) ≥ 2 (or its ZCH/mixed analogues), spend 0, whose l extras no printed statement can see (Theorem O). For m = 2 this is exactly IIa(l odd, ν ≥ 3 odd, M = 2) / ZCH(gcd(ν+1,l) ≥ 2) at an interior meet, plus the root-meet l-odd residual; for m ≥ 3 the cells lν ≡ −1 (mod m) exist at pattern level but their *reachability* (r-edge ratio consistency) is untested. The kill, if one exists, must come from the H1 layer that the printed statements stop short of: matching the rigid (iv)-coefficients of a jump cell against the per-edge Prop 9.3(a)–(d) ratio equations of ALL r incoming chains simultaneously — a computation never yet run for any cell (the l = 1 rigidity a₁/a₂ = 2±√3 shows the coefficients are fully pinned, so the match is a finite check per cell).
SHEET6-MULTIPOLE.md:159:**Concrete next step (ordered, engine-able):**
SHEET6-MULTIPOLE.md:160:1. **Build the r = 3 jump-cell reachability check**: extend cases/l1_ode_check.py + cases/twopole_check.py to r = 3 incoming edges; impose Prop 9.3(a)–(d) per-edge (H1 tier) plus the equal-quotient law and entry pin at the cell (r,ν,l) = (3,5,1), M = 3, in the minimal m = 3 configuration td = 3β. Outcome either way is decisive: a ratio-inconsistency kills the first m ≥ 3 escape cell and gives the template for the whole book; consistency produces the m = 3 exhibit and sharpens Theorem O to m ≥ 3.
SHEET6-MULTIPOLE.md:163:4. **Promote §7**: referee the A3 prime-partition and RH kills; if confirmed, they delete the partitions 8 = 3+5, 10 = 3+7, 12 = 5+7 and all saturated cells from the book before any engine run.
SHEET6-MULTIPOLE.md:169:- A1.T2 = A2(4) (restored kill; A2's unique-predecessor argument adopted into D2/D3 as the cleaner single-root justification at (0,y)). A1.T4/T5 = A2(3) = A3.P4 (merge anatomy; independent derivations agree cell-by-cell). A1.T5's "M_G | gcd(r, lν+1)" upgraded to A2/A3's equality (elementary proof in D6d). A1.T6's root pin ψ = r+l−1 ⟷ A2(5R)'s ψ = l+1 at r = 2: consistent. A1.T7 = A2.Prop B (budget transparency; A2 adds the Euler-equality itemization, A1 adds the F\*_P ∈ T_{a,pole} branch argument — both used in D8). A1's G\* = A2's G_last (max ∩C_i). A2(1) prime-Λ pin subsumes A1's β-minimal pin; both in MP4.
SHEET6-MULTIPOLE.md:171:- The k = 0 manufacture (D5c/D6a) is the load-bearing novelty in both A1 and A2, derived independently with the same printed chain (St 6.2 computation + St 3.9(iii)/3.17(i)/8.1(i) + Prop 6.8 same-branch); its no-pole-budget character is what makes Theorem MP m-uniform.
SHEET6-R1-LADDER-REVIEW.md:14:untouched: 44/44 sha256 vs /tmp/q0_regression_baseline.sha before AND
SHEET6-R1-LADDER-REVIEW.md:19:  by evaluation at both banked primes.
SHEET6-R1-LADDER-REVIEW.md:50:evaluation code), both primes p = 105337 / 105673, witness from
SHEET6-R1-LADDER-REVIEW.md:55:| r1_full_core.ms (ORIGINAL 105 eqs, char-0) | 105/105 vanish | 105/105 vanish |
SHEET6-R1-LADDER-REVIEW.md:56:| r1_full_core_p*.ms (p-variant) | 105/105 | 105/105 |
SHEET6-R1-LADDER-REVIEW.md:57:| r1_reduced_core.ms (56) | 56/56 | 56/56 |
SHEET6-R1-LADDER-REVIEW.md:59:| r1_12branch_core.ms (105, s1 = 0) | 105/105 | 105/105 |
SHEET6-R1-LADDER-REVIEW.md:84:own w-data therefore pins, through the E5 relation the §13.0 diagnosis
SHEET6-R1-LADDER-REVIEW.md:116:   therefore NOT discharged; both must run under saturation semantics.
SHEET6-R1-LADDER-REVIEW.md:118:   (1,2) witness (§15.2) sets s1 = 0 in its OWN core — the h2-tie
SHEET6-R1-LADDER-REVIEW.md:124:   emission should fix the name before a nonzero tie value matters.
SHEET6-R1-LADDER-REVIEW.md:161:  minimal reduced core 0/49 rows nonzero at (x = 0, W = HW = 0), (1,2)
SHEET6-R1-LADDER-REVIEW.md:162:  core 0/98 at (x = s1 = 0, W = HW = 0), both primes; (1,2) W-loaded
SHEET6-R1-LADDER-REVIEW.md:175:  proven by its origin point, verified above by direct evaluation at
SHEET6-R1-LADDER-REVIEW.md:178:  literally ±E — the "(1,2) shares the identical terminal core"
SHEET6-R1-LADDER-REVIEW.md:191:  fails before any anchor is even reached.
SHEET6-R1-LADDER-REVIEW.md:248:   restored as a variable, or equivalently the E6 tie linking the
SHEET6-R1-LADDER-REVIEW.md:262:   witness; its "survives core" verdict needs the s1-saturated re-run
SHEET6-R1-LADDER-REVIEW.md:263:   before the shared-terminal-core symmetry is leaned on.
SHEET6-R1-LADDER-REVIEW.md:265:   emission comment before nonzero values matter.
DC2-PROGRAM.md:48:- by §4's slice theorem (verified computationally below): all quadruples of Bernstein
DC2-PROGRAM.md:72:   lift of a rank-2 Poisson counterexample is exactly an attack on this gap; the lift
DC2-PROGRAM.md:82:Architecture per ZHEGLOV-SCOPE.md §1: (S2) normal forms A_1 ⊂ D_1 = K[[x]][∂] ⊂ D̂_1^sym,
DC2-PROGRAM.md:95:| Schur normal form SPS⁻¹ = ∂^p + explicit centralizer | converts [Q,P]=1 into finitely many normal-form coefficients | **BREAKS — first genuine obstruction, see below** |
DC2-PROGRAM.md:96:| Head-chopping induction, distance p+q−1 | well-founded descent | needs the normal-form coordinates; also no single well-founded order measure on bidegree pairs identified |
DC2-PROGRAM.md:101:Everything in Zheglov's proof after page 1 runs inside normal forms that exist because of
DC2-PROGRAM.md:105:[Q,P] = 1 a statement about finitely many coefficients: normalize P, then Q lives in the
DC2-PROGRAM.md:109:- **No normal form**: a single operator in two variables is not conjugate to a
DC2-PROGRAM.md:110:  constant-coefficient model; "normal forms of PDOs" in dim 2 is Zheglov's *own open
DC2-PROGRAM.md:113:  a full Weyl algebra. Normalizing P_1 leaves the remaining three generators in an
DC2-PROGRAM.md:119:theorem about ODOs on a formal disk, where Sato–Schur theory coordinatizes everything
DC2-PROGRAM.md:133:vertex normalization a_{p0}b_{q0} = ±1 at a unique-decomposition Minkowski vertex,
DC2-PROGRAM.md:138:Write elements of A_2 normally ordered: P = Σ a_p x^{p'}∂^{p''}, support in ℕ^4. The
DC2-PROGRAM.md:152:  elimination and well-foundedness survive; pivots are the same lattice determinants.
DC2-PROGRAM.md:163:  2-face. Making this precise (which 2-faces can occur, after normalizing by tame
DC2-PROGRAM.md:165:  and the natural first theorem of the program.
DC2-PROGRAM.md:174:The RHS of [Q_i, P_i] = 1 lives at the origin of ℤ^4. Vertex normalization: the origin
DC2-PROGRAM.md:181:- **Gap condition**: lattice points of a Q_i-polytope strictly between the origin block
DC2-PROGRAM.md:186:  polytope shape, the near-origin block has more forced-vanishing coefficients than
DC2-PROGRAM.md:195:The s = 1 stratum of every statement above is a theorem about PC_2-type quadruples; the
DC2-PROGRAM.md:290:- **T0 (done, this file)**: kernel + complete D ≤ 2 slice theorem, machine-verified;
DC2-PROGRAM.md:301:  a full theorem ("no graded counterexample") is plausibly provable — a publishable
DC2-PROGRAM.md:302:  stand-alone result mirroring the dim-2 graded-Keller theorem.
DC2-PROGRAM.md:308:- **T4 (years, research program)**: the Zheglov-route prerequisite — 2D normal
DC2-PROGRAM.md:316:after one normalization — that finiteness is what every known DC(1) argument (Dixmier's
DC2-PROGRAM.md:319:ℤ⁴ with a 2-parameter leading-form family, and the tame normalization group is small
DC2-PROGRAM.md:326:Months 1-2: T1 + T2 (D=3 quantum slice; graded theorem). Months 2-4: T3 quantum
DC2-PROGRAM.md:335:decisive intermediate artifact (graded theorem, D=3 divergence data, first shape
DC2-PROGRAM.md:351:constants commute with everything and are free; linear part normalized to identity —
DC2-PROGRAM.md:352:validity of that normalization re-checked at D=3 in §6.7). Unknowns: 4×(10+20) = **120**.
DC2-PROGRAM.md:496:  §6.0 normalization is consistent at D=3 (caveat: verified pointwise on the family,
DC2-PROGRAM.md:541:4. **Precise blockers to a full D ≤ 3 slice theorem** (what remains before "DC(2)
DC2-PROGRAM.md:542:   holds in degree ≤ 3" is a theorem rather than a sampled verdict):
DC2-PROGRAM.md:557:5. The unipotent normalization (linear part = identity) is validated at D=3 pointwise
DC2-PROGRAM.md:559:   solutions — at D ≥ 3 this is a theorem obligation, not a triviality (a
DC2-PROGRAM.md:573:fibers (linear-level or small-k) likely still local. Recommended D=4 scope: linear
CROSSCHECK.md:14:- Unknowns = all lattice points of hull(N(P)), hull(N(Q)); equations = all coeffs of
CROSSCHECK.md:16:  (0,0) coeff unconstrained; torus normalization FIX: P(8,16)=1, Q(12,24)=1.
CROSSCHECK.md:42:  nonzero" — same reading as our corners-attained saturation. Lattice counts: smaller
CROSSCHECK.md:45:- Suzuki notes all lattice points have nonneg coords, so L^(1) Laurent setting reduces to
CROSSCHECK.md:48:  Q=Dz^3+Ez^2+Fz+G (D: t^2..t^12) = same lattice supports; case 1 adds negative z-bands
CROSSCHECK.md:53:### Normalization: MODELING DIVERGENCES, all legitimate (gauge choices)
CROSSCHECK.md:56:  ambiguity — likely source of his degree-35 H(a_7): 5 dessin classes x 7 gauge).
CROSSCHECK.md:58:  normalization" Lemma: sets constant terms to 0 AND drops the (0,0) vertex-presence
CROSSCHECK.md:81:  Rabin-certified irreducible mod 67), matching Suzuki's "exactly 5 dessin classes"
CROSSCHECK.md:82:  count (passport (3^7),(2^10 1),(17,1^4)). SAME-FIELD CHECK DONE: discriminant square
CROSSCHECK.md:88:  (a_1=a_8=1 leaves 35th-root ambiguity), consistent with 5 dessin classes x 7.
CROSSCHECK.md:102:    hard identity h = Sum T_i E_i over L verified by independent gmpy2 evaluation
CROSSCHECK.md:132:  exhaustiveness of GGV Prop 4.3 itself, and the on-paper normalization argument
CROSSCHECK.md:144:- Structure: exhaustiveness of the 5-dessin split is machine-enumerated (Prufer trees
CROSSCHECK.md:167:  (b) The dessin/passport bridge (Riemann existence, Belyi passport derivation) is
CROSSCHECK.md:183:  corner sets, identical lattice supports (25+47 and 61+125 points), identical bracket
CROSSCHECK.md:185:  normalizations, each verified legitimate. This materially strengthens the
CROSSCHECK.md:188:  for diffing against our c1 core are staged in crosscheck/c1_extracts/ (branch
ZHEGLOV-SCOPE.md:9:- **S2 Preliminaries, theory of normal forms** (565–1300, ~735 ln): imports from [A.Z]=Zheglov's generalized Schur theory, [GZ1]=Guo–Zheglov normal forms, Dixmier, Wilson, Sato. Ring tower A_1 ⊂ D_1=K[[x]][∂] ⊂ D̂_1^sym; Schur operator S with SPS⁻¹=∂^p; centralizer C(∂^p) ≅ M_p(K[D^p]), "vector form". Mostly cited, not reproved.
ZHEGLOV-SCOPE.md:11:- **S4 Main preparatory theorems** (1451–2357, ~906 ln, biggest): **T:DC-pairs** (head-chopping process terminates, distance maximal = p+q−1) and **T:subrectangular_sequence** (all F_i(P,Q) subrectangular; edge polynomials f_{0,1}, f_{1,0} identified). Inductive engine: L:Q_p (tail shape), **L:induction_step** (1575), **L:polynomials** (1721, "key lemma", uses subrectangularity), **L:induction_step1** (1853).
ZHEGLOV-SCOPE.md:15:**Theorem chain:** ¬DC1 ⇒ subrectangular DC-pair [GGV, S3] ⇒ T:DC-pairs + T:subrectangular_sequence [S4] ⇒ family Φ_{N,1}-pairs with controlled sequences [L:Phi_N(P)] ⇒ string↔commutative correspondence [S5] transports to rank-1 spectral side ⇒ distinguished-coefficient computation contradicts N-independence [S6 Steps 4–7]. Normal forms (S2) are the ambient machinery for every step after S3.
ZHEGLOV-SCOPE.md:17:**External load-bearing inputs (not reproved here):** [GZ1] (arXiv 2303.10306, Guo–Zheglov normal forms — the whole calculus), [A.Z] (generalized Schur theory), [GGV] (subrectangular reduction of minimal counterexamples), Wilson's theorem, classical Schur–Sato. An error in [GZ1] would sink the paper wholesale.
ZHEGLOV-SCOPE.md:21:- v3 2024-10-23, 34 pp: "improved exposition, more details to the proof added".
ZHEGLOV-SCOPE.md:23:- v5 2026-01-19, 78 pp: "extended introduction, more comments and references added, **calculations at the last stage of the proof are simplified**, some typos fixed".
ZHEGLOV-SCOPE.md:30:**R4. String-equation correspondence for NON-coprime orders (S5, esp. T:one-to-one-correspondence & inverse, 2620–2790).** Extends A. Schwarz's coprime-order bijection; needed precisely because subrectangular DC-pairs have non-coprime orders. Feeds R:distinguished_coefficient (distinguished coefficient =0, via Newton–Puiseux + Wilson, rank-1). Formal-series existence/uniqueness/normalization arguments; the whole transport of the DC-pair to the Puiseux-series side rests here.
ZHEGLOV-SCOPE.md:38:- **R4 → (c), partial (a).** Correspondence theorems are conceptual; but cutting/glueing the tail is algorithmic on truncated series — can numerically instantiate: take explicit commuting rank-1 pairs (e.g. KdV/Burchnall–Chaundy pairs), glue tail, check [Q,P]=1 to finite order, and vice versa. Distinguished-coefficient=0 claim testable on explicit rank-1 examples.
ZHEGLOV-SCOPE.md:40:- **Global obstacle for (a):** all S4/S6 statements quantify over hypothetical DC-pairs (empty set if theorem true). Directly instantiable objects: automorphism pairs (φ(x),φ(∂)), string-equation solutions in D_1, commuting rank-1 pairs. Falsification target must be a lemma whose hypotheses these NON-vacuous objects satisfy: L:polynomials (any polynomials), S5 correspondence (any string solution), L:Q_p tail shape (any normalized P plus Q with [Q,P]=1 — automorphism pairs qualify!).
ZHEGLOV-SCOPE.md:46:- **Positive de-risking discovered:** the machinery papers are refereed — [GZ1] I (2406.14414, v4 Nov 2025) AND II (2511.05117) both "to appear in Izvestiya: Mathematics"; "Normal forms III" published in Proc. Steklov. [A.Z] published Steklov 2023; [GGV] J.Algebra 2014. So only DC5's own reasoning is unrefereed. v5 thanks **anonymous referees** ⇒ at least one journal round happened by Jan 2026; no acceptance 6+ months later.
ZHEGLOV-SCOPE.md:48:- MathOverflow + Reddit remain crawler-blocked [GAP, same as RECON]; manual browser check still recommended.
ZHEGLOV-SCOPE.md:56:- **T3. Machinery on non-vacuous objects**: automorphism pairs (φ(x),φ(∂)) in A_1 and Burchnall–Chaundy rank-1 commuting pairs; compute normal forms to finite order; test L:Q_p tail shape, termination + non-maximal distance (intro's claim), S5 cut/glue roundtrip, distinguished-coefficient=0 (R:distinguished_coefficient). ~10-20 agent-h. Tests R4 + S2 end-to-end where hypotheses are satisfiable.
ZHEGLOV-SCOPE.md:59:- **T6 (optional). Formalization**: not recommended — needs [GZ1] I+II first; est. 6-12 expert-months.
ZHEGLOV-SCOPE.md:61:**Decision note for campaign:** DC1 truth only closes the ¬DC1⇒¬JC2 refutation route; auditing Zheglov is *defensive* recon, not on our (72,108) critical path. Recommended spend: T1 now, T2 next; escalate to T3-T5 only if T1/T2 find anomalies or if we plan to cite DC1 as settled.
SHEET6-TDU-REVIEW.md:1:# SHEET6-TDU-REVIEW.md — Adversarial review of the TD-UNIFORM entry theorem (08fbbda)
SHEET6-TDU-REVIEW.md:5:— headline claim: single-pole exclusion at ENTRY for every PRIME td (Theorem
SHEET6-TDU-REVIEW.md:19:  ingredients re-read on-page; NOTHING before §9 (p. 45) mentions td or Λ;
SHEET6-TDU-REVIEW.md:41:**NET: Theorem TDU SURVIVES adversarial review** — single-pole
SHEET6-TDU-REVIEW.md:91:  arbitrary normalized counterexample; proof (monotone ρ, St 3.10/3.11/
SHEET6-TDU-REVIEW.md:94:- Prop 8.4 (p. 44): arbitrary normalized counterexample + T_a,pole = {G};
SHEET6-TDU-REVIEW.md:120:  prime THEOREM does not hinge on the α ≥ 2 convention; only the exact
SHEET6-TDU-REVIEW.md:148:  (`import sheet6_campaign as m; m.IIB_DERIVED = True` before importing
SHEET6-TDU-REVIEW.md:205:## 6. Front 6 — perimeter audit of Theorem TDU
SHEET6-TDU-REVIEW.md:215:  to the theorem's stated perimeter. Same trust tier — no downgrade.
README.md:5:Grown into: a campaign on the remaining structural avenues (sheet-6 exclusion,
README.md:21:- [x] Theorem grid (2,2),(2,3),(2,4) + k≥3 impossibility (reviewed)
README.md:22:- [x] conj:R PROVED (Theorem A via Duistermaat-van der Kallen mechanism, adversarially
README.md:35:      (1,2) core queued; chain cores building
README.md:46:- [ ] Verdicts: 2 boxes grinding (EMPTYs banking; big char-0 cores need a
FACE-ISOLATION.md:20:**Main theorem (support one-sidedness).** The monomial support of P (in Z,W) is
FACE-ISOLATION.md:39:3. **Prime isolation (Lemma 7, the core).** For λ/(c+d) ≥ 0 with denominator B:
FACE-ISOLATION.md:44:   mixed stratum has valuation ≥ R₀+1, by Kummer's theorem (a base-p carry in the
FACE-ISOLATION.md:45:   multinomial coefficient) or a divisibility split (k = p·l). So the p-adic
FACE-ISOLATION.md:46:   valuation SEPARATES the chosen face from all other strata: the vanishing of a
FACE-ISOLATION.md:49:4. **Frobenius reduction.** Mod p (residue field κ): CT(R̄^{qp}) = CT((R̄^q)^p) =
FACE-ISOLATION.md:59:   conv(S) finds an edge E where wt transitions sign; its inward normal isolates E
FACE-ISOLATION.md:70:P₄ (six monomials, arXiv:2607.18186) refutes GMC(n≥3). So the theorem is genuinely
FACE-ISOLATION.md:76:progression m=qp, carries a p-adic filtration whose graded-top piece is ONE face of
FACE-ISOLATION.md:88:| D4 | Multinomial strata k of E(P^m); mixing of faces inside one scalar; must be UNMIXED by p-adics (Lemma 7) | Bracket coefficient array is ALREADY graded by lattice position: the top ℓ-stratum involves only face(ℓ,P)×face(ℓ,Q). Isolation is free | **Key asymmetry**: Lemma 7's conclusion ports to the classical fact [ℓP,ℓQ]=0 (Abhyankar/GGV starting point). The port of "isolation" per se yields nothing new at leading order |
FACE-ISOLATION.md:90:| D6 | Face rigidity input: DvdK — CT(R^q)=0 ∀q ⇒ 0∉Newt(R) ⇒ one-sided | Edge rigidity inputs: [ℓP,ℓQ]=0 ⇒ ℓP,ℓQ powers of a common form h; carrying edge: Wronskian eq u·fg′−v·f′g=cT^s, solution set rigid/classifiable (= Suzuki's 5 dessin classes for the (8,28) top edge) | Analogy real at the "one-variable rigidity theorem" level, but the theorems are different animals: DvdK is an infinite-tower statement; the edge Wronskian is a single ODE |
FACE-ISOLATION.md:92:| D8 | Arithmetic lever: m=qp, good primes (G1–G4), Kummer carries, v_p separates pure face (=R₀) from mixed (≥R₀+1); Frobenius CT((R̄^q)^p)=(CT R̄^q)^p | **No classical counterpart in JC2 polygon analysis.** Nearest structures: (a) unit-pivot graded elimination killing sub-vertex strata (LEMMA.md's chain — an exact-arithmetic analog of "mixed strata have higher valuation"); (b) char-p Keller structure: [A^p,B]≡0, P̄^p central, Cartier operator, BKK/Tsuchimoto Frobenius bridge (JC⟺DC) | **The genuinely portable novelty lives here**; see TL1, TL2 |
FACE-ISOLATION.md:93:| D9 | Endgame: strict one-sidedness of supp(P) wrt wt ⇒ GMC(2) by degree bookkeeping (Lemma 3) | Endgame sought: polygon/support exclusions per (ρ,σ)-cell ⇒ degree bound (our campaign); or cone confinement ⇒ automorphism (Abhyankar–Moh shape) | Same proof architecture: support theorem first, analytic conclusion second |
FACE-ISOLATION.md:98:manufacture an infinite family (powers with p-adic descent, prime variation, or
FACE-ISOLATION.md:100:("CT of all powers vanish ⇒ support one-sided"); the edge Wronskian is first-order
FACE-ISOLATION.md:101:information. (iii) D8(b) is structurally attractive (Frobenius rescales the Newton
FACE-ISOLATION.md:107:**TL1 (Polygonal surplus criterion — level filtration as valuation).**
FACE-ISOLATION.md:108:Setting: reduced Keller-type pair over K, [P,Q]=x^k; N(P),N(Q) lattice strips of
FACE-ISOLATION.md:111:normalization (x^k at the Minkowski vertex p₀+q₀, unique unimodular decomposition,
FACE-ISOLATION.md:118:constants = lattice determinants det(corner, ·) ≠ 0) expresses the surplus as
FACE-ISOLATION.md:120:the chart M≠0. I.e. LEMMA.md condition (iii) is a THEOREM given (i)+(ii)+strip
FACE-ISOLATION.md:121:widths, by Wilson-style counting (pure stratum at valuation R₀ ↔ vertex path;
FACE-ISOLATION.md:128:**TL2 (Frobenius/Cartier non-adjacent face congruences — the p-lever).**
FACE-ISOLATION.md:130:p ∤ pivot constants). Mod p: [P̄,Q̄]=1 still; Frobenius makes P̄^p, Q̄^p central
FACE-ISOLATION.md:135:data at p·γ + O(1) — Frobenius scales the polygon by p — yielding congruence
FACE-ISOLATION.md:139:precise coefficient identity to extract is the (1/p)-normalized part of
FACE-ISOLATION.md:142:— evidence that Frobenius sees Keller structure; nothing face-local exists in
FACE-ISOLATION.md:148:Wronskian edge equation u·fg′−v·f′g = c·T^s. Depth-r strata of [P,Q]=x^k along d
FACE-ISOLATION.md:153:vanish then the pair (f,g) is a dessin-rigid pair: f,g are, up to common factor
FACE-ISOLATION.md:154:and reparametrization, powers of a single h with prescribed ramification" — would
FACE-ISOLATION.md:168:verified to the integer); v₇(pure) = 3 = R₀; v₇(mixed) = 4 ≥ R₀+1 — the p-adic
FACE-ISOLATION.md:170:normalization fails (v₃(pure-face) = 4 ≠ R₀ = 3), showing why G4 is needed for the
FACE-ISOLATION.md:172:face, which is the theorem's content in miniature.
FACE-ISOLATION.md:176:eliminations, all pivot constants nonzero lattice determinants
FACE-ISOLATION.md:180:(valuation R₀), the gap/sub-vertex strata are the "mixed terms" (killed = higher
FACE-ISOLATION.md:181:valuation), and the surplus back-substitution is the Frobenius/CT extraction. The
FACE-ISOLATION.md:189:to a one-variable object (D5), apply a one-variable rigidity theorem (D6), and
FACE-ISOLATION.md:191:ALREADY occupies all three slots (leading-form commutation, edge Wronskian/dessin
FACE-ISOLATION.md:195:1. **The counting discipline (TL1)** — Wilson's "pure stratum has valuation exactly
FACE-ISOLATION.md:198:   v_p and unit lattice-determinant pivots playing good-prime integrality. This is
FACE-ISOLATION.md:202:2. **The arithmetic lever (TL2)** — the m=qp / Frobenius trick has NO classical
FACE-ISOLATION.md:212:worlds' vocabularies. Recommended next step: prove TL1 (O(1)-sized block, explicit
FACE-ISOLATION.md:219:superseded by SURPLUS.md's scoped theorem + scope map.
SHEET6-CAMPAIGN.md:4:AF2 derivation (SHEET6-AF2.md) + two-pole attack (SHEET6-2POLE.md) + entry-M
SHEET6-CAMPAIGN.md:21:## 0a. Assembly-layer extraction (thesis pp. 37-60, needed before enumeration)
SHEET6-CAMPAIGN.md:61:  normalization forbids exactly this. Campaign runs with hypothesis **H3**: "case-IV
SHEET6-CAMPAIGN.md:183:| r8 | 3,6 ext | more III-tails (1 and 15) | superset |
SHEET6-CAMPAIGN.md:190:counts are before applying H3. No computation exceeded minutes; nothing farmed
SHEET6-CAMPAIGN.md:197:   ending at (0,y) via case IV contradicts normalization (candidate: case IV (l)
SHEET6-CAMPAIGN.md:216:   is the td=6 analogue of the Domrina-Orevkov multi-dicritical split.
SHEET6-CAMPAIGN.md:220:   superset runs (M | P) add only more III-tails, no new survivors. Justifying the
SHEET6-CAMPAIGN.md:249:  are independently covered by Orevkov/Domrina/Żołądek, so JC-td≤5 stands
MONDELLO-CHECK.md:23:- **Vertex normalization (i): HOLDS verbatim.** rhs monomial 1 at Minkowski vertex (1,1) = (1,0)+(0,1), unique decomposition, det = +1, corners saturated (vertex eq a·b = 1).
MONDELLO-CHECK.md:24:- **Gap condition (ii): FAILS.** In SURPLUS.md normalization this is the cell (k,d2) = (0,1): rhs = x⁰, {p₀,q₀} = {(1,0),(0,1)} so max((p₀)_x,(q₀)_x) = 1 < 2; no gap columns. Also d2 = 1 = the scope-map row with "no extra keys, no obstruction", and the top edges are NOT through the origin (Q straddles the direction line: offsets −1, 5).
MONDELLO-CHECK.md:25:- Verdict: **NEAR our setting (strip pair + exact condition (i)) but strictly OUTSIDE the proved (k,d2) = (2,2) obstruction cell** — so no tension with our char-0 theorems even before characteristic considerations.
MONDELLO-CHECK.md:30:**Over Q the machinery EMPTIES his data at the M2/gap-kill stage** (pre-block, LEMMA.md §2 step 1 / SURPLUS.md GAP-KILL analogue). Sparse run: 13 keys; after vertex normalization (pivot det((1,0),(0,1)) = +1, odd), the sub-vertex single-monomial keys force a(2,1) = 0 [pivot **+2**], a(4,0) = 0 [pivot **+4**], a(6,2) = 0 [pivot **+6**], then b(7,2) = 0 [pivot **+2**], b(6,1) = b(8,3) = 0 (odd pivots 1, 3): full collapse to the elementary automorphism P = a1x, Q = b0y + b1x⁵. Hull run agrees: strip corners a(2,1), a(6,2) killed by pivots +2, +6; Q-corner b(8,3) then dies; residual = triangular x-axis family (automorphisms). So **no char-≠2 Keller pair realizes these Newton polygons** — his example must live where those pivots die.
MONDELLO-CHECK.md:32:**The exact failing constants: the even lattice-determinant pivots det(p, q₀) = det((2,1),(0,1)) = 2, det((4,0),(0,1)) = 4, det((6,2),(0,1)) = 6** (and det((1,0),(7,2)) = 2 on the b(7,2) key). Mod 2, 10 of the 12 non-vertex bracket keys of his support are IDENTICALLY zero (every contributing det even; u-basis law [x^a u^b, x^c u^d] = (ad−bc)x^{a+c}u^{b+d−1} gives dets det((1,1),(4,2)) = −2, det((1,1),(5,3)) = −2, det((4,2),(5,3)) = 2, plus d((x²u)²) = 2(x²u)d(x²u) ≡ 0: the Frobenius-square strip is differentially invisible); the two surviving keys are cancellation identities his all-ones coefficients satisfy. The M2 stage never fires; the strips live.
MONDELLO-CHECK.md:34:Same prime in our own theorems: LEMMA.md §2 step 1's M2 key reads 2·a1·b2 = 0, and the SURPLUS.md (2,2) block chain divides by pivots {2,3,4,5,6} (first even: b4 = a2b3/(**2**a1) at key (3,2)) with char-exclusion set {2,3,5} declared sharp. Mondello's example is an existence proof that excluding char 2 there is NECESSARY, and it fails our machinery in exactly the predicted way: an explicit division by 2 in the pivot constants, nothing else (the −1/5 and R_{k,d2} binomials are not reached at his (k,d2) = (0,1) cell).
MONDELLO-CHECK.md:37:> **Remark.** The characteristic restrictions in our results are not an artifact of the method. Mondello's plane Keller pair P = x + x²y + x⁴ + x⁶y², Q = y + x⁵ + x⁶y + x⁷y² + x⁸y³ over F₂ (arXiv:2608.02634) has Jacobian determinant 1, sends the three distinct points (0,1), (1,0), (1,1) to a common image, and generates a degree 3 separable field extension, so even the separable Jacobian conjecture fails in characteristic two. Its Newton polygons form a strip pair along the direction (1,1) satisfying our vertex normalization, and in any characteristic other than two our near-origin eliminations, whose pivot constants at this polygon data are the lattice determinants 2, 4, and 6, force the strip corners to vanish and reduce any such pair to an elementary automorphism. In characteristic two every one of these determinants vanishes, the corresponding bracket equations become identically zero, and the strips survive; this is precisely the escape that Mondello's example exploits.
MONDELLO-CHECK.md:41:- **Not in-regime**: strip pair along d=(1,1) with vertex normalization (i) exact, but cell (k,d2) = (0,1) — outside the proved (2,2) obstruction cell (no gap columns, d2=1, top edges off origin). No contradiction with our char-0 theorems.
SHEET6.md:6:- **Żołądek 2008** (Topology 47(6) 431–469, DOI 10.1016/j.top.2008.04.001): bronze-OA but PDF endpoints (ScienceDirect, CORE) sit behind bot-checks; CAPTCHA completion is prohibited, so NOT obtained. No arXiv version; author page gone. Worked from zbMATH review Zbl 1174.14054 (Krasiński) + citing literature. Results: JC holds for (1) topdeg ≤ 5, (2) gcd(deg f,deg g) ≤ 16, (3) gcd = 2·prime.
SHEET6.md:7:  - **1-click human action for DC**: fetching the SD PDF in a normal browser session would upgrade the Żołądek half from reconstruction to verbatim.
SHEET6.md:8:- **Obtained (free, in `refs/`)**: Orevkov 1986 3-sheet paper (`jc86.pdf`, author-hosted English), Domrina–Orevkov 1998 4-sheet I (`do.pdf`), and — the decisive find — **Sigray's full 66-page 2008 ELTE PhD thesis "Jacobian trees and their applications"** (`sigray_full.pdf`, teo.elte.hu/minosites/ertekezes2008/sigray_i.pdf; booklet `sigray_i.pdf`), advisor A. Némethi.
SHEET6.md:10:- **1c. RECON correction**: "no independent reproof of ≤5 exists" is WRONG. Sigray's thesis Theorem 9.1 proves td(f,g) ≥ 6 for any counterexample, independently of Żołądek, same year, different machinery (decorated Eggers–Wall trees vs Newton–Puiseux charts). Never journal-published (zbMATH lists only his monodromy + kp′q−lpq′ papers) but cited as the bound by Makar-Limanov (arXiv:2106.06869) and Borisov (arXiv:1901.04073: "current best lower bound ... is 6"). Caveats on BOTH proofs: Żołądek's neighboring gcd sections have a **documented gap** (GGV arXiv:1401.1784: Lemma 4.10 "claims without proof that I₂ ⊂ (1/m)Γ(f₂)"; his claimed B>33 fails, B≥16 stands only via GGV's independent reproof) — his topdeg-5 sections have no reported gap but are unaudited; Sigray's thesis is unrefereed. Also flagged: arXiv:2407.13795 (Moskowicz, 2024, 8pp) claims NO Keller map has prime field-extension degree — unpublished, treat as unvetted; if ever verified it would exclude 7 and make 6, 8, 9 the whole frontier.
SHEET6.md:14:- **(A) Żołądek's Newton–Puiseux charts** (reconstructed from zbMATH + Nguyen Van Chau arXiv:0804.3172v2 + MIMUW seminar abstract): resolve (f,g) at infinity in BOTH source and target; near each divisor use multivalued charts (x^{−1/m}, ξ) — truncated fractional-power series x(Σc_k x^{−k/m} + ξx^{−n/m}) where ξ replaces the Puiseux tail ("left and right Newton-Puiseux charts", Chau). The Keller map becomes near-monomial in charts; jac≡1 forces rigid exponent+leading-coefficient relations. Topological degree = sheets over infinity = Σ local degrees over dicritical divisors, with Orevkov's identity Σ(ramification excess at infinity) = td − 1. Case analysis = finite enumeration of dicritical/chart configurations for td ≤ 5; each killed by exponent arithmetic or analytic contradiction.
SHEET6.md:15:- **(B) Sigray's decorated Eggers–Wall trees** (verbatim, thesis in hand): Abhyankar normal form (§2: Newton polygons in rectangles, fibers with 2 points at infinity); Eggers–Wall tree of Puiseux expansions of f-fiber branches at infinity (§3); extended Abhyankar fundamental theorem + partial order (§4); td and pole orders of g computed from tree data (§5, Props 5.5/5.8); tree structure symbols ↘↗ (§6); finite critical values budget (§7, Cor 7.1); Jacobian-forced number theory linking neighboring vertices (§8, Prop 8.1); §9: decoration Q(F) = (D_F, deg p_F, ν_F, M_F, κ_F(1−π(F))) must propagate along the "characteristic sequence" F₀→…→(0,y) to the root, under Diophantine constraints, with budget Σλ_{F_i} ≤ td−2 (St 9.4) — and no admissible propagation survives for td ≤ 5.
SHEET6.md:19:- **Orevkov/Domrina (3,4) were quasi-topological**: splice/Eisenbud–Neumann diagrams of the resolution boundary, homology, intersection form, canonical class K̃ = F*K + B of the branched cover; leaf kills by unimodularity/negative-definiteness/Abhyankar–Moh determinant arithmetic. Case tree at 4: ~19 configurations → 8 final diagrams (Domrina 2000), a few dozen leaves.
SHEET6.md:20:- **The 4→5 explosion is NOT case count — it is a provable method failure.** Egorov 2002 constructed a proper 5-sheeted "exotic covering" of C² (branching along two planes F₁*,F₂*; H²_c ≅ Z²; S₁² = −3, S₂² = −15, S₁·S₂ = −3; K(S₁)=K(S₂)=1) consistent with EVERY quasi-topological invariant Domrina–Orevkov use. So 5 required a new analytic layer: both 2008 proofs inject Abhyankar approximate-root/Puiseux-coefficient arithmetic (pole orders of g along f-branches; jac=1 exponent identities) that sees strictly more than the topology. That is the conceptual jump; the case tree itself only grew ~2×.
SHEET6.md:21:- **The real wall is at 9, not 6**: Sigray exhibits a decorated Eggers–Wall tree satisfying ALL his constraints at td = 9 with (deg f, deg g) = (48,64) — Moh's exceptional case — matching Orevkov's holomorphic "counterexamples to JC at infinity" (minimal td 9, bidegree (48,64); DO-I: the local-at-infinity method can at best reach ~8). Sigray verbatim: the problem at higher degree is not that computations are "more involved" but that a consistent tree EXISTS at 9. Corollary: td ∈ {6,7,8} is the entire remaining runway for at-infinity methods, with no known consistency obstruction below 9.
SHEET6.md:25:- **Configuration layer**: ramification budget Σλ ≤ td−2 = 4 and multi-pole-vertex splits (partitions of td−1 = 5 over dicritical vertices: 7 shapes) ⇒ **~7 top-level branches** vs effectively 3–4 at td 5.
SHEET6.md:30:- **Per-case task format** (one agent = one case): JSON {case_id; hypotheses: Q(G) parametric tuple, type row, Prop-9.3 branch (I/II/III/IV), mult(p,c) value; goal: complete list of admissible Q(F) or proof of emptiness; required output: solution families + machine-checkable trace}.
SHEET6.md:44:`sigray_full.pdf` (66pp thesis, THE working text) · `sigray_i.pdf` (booklet) · `jc86.pdf` (Orevkov 3-sheet) · `do.pdf` (DO 4-sheet I) · Egorov: mathnet.ru/eng/mzm364 · Domrina II: mathnet.ru/eng/im273 · zbMATH review via api.zbmath.org (an:1174.14054) · GGV gap report: arXiv:1401.1784 · Chau chart description: arXiv:0804.3172v2 · bound citations: arXiv:1901.04073, arXiv:2106.06869.
BOOK-ENUM.md:17:all of td = 7, 11, 13, the multi-pole shadow of the prime-td theorem:
BOOK-ENUM.md:94:    IIa, ALL at l = 1 — the Theorem-O escape lν ≡ −1 (mod r), M = r:
BOOK-ENUM.md:186:before any sweep output is written; the sweep aborts if it fails.
SHEET6-A3L1-REVIEW.md:26:  reproduces the Wronskian kernel exactly: s = p^{l/2}, ct = 0 forced)
SHEET6-A3L1-REVIEW.md:38:Verdict: **CONFIRMED**. Chain re-read on-page, attacked at both suggested
SHEET6-A3L1-REVIEW.md:45:  no degree-preservation issue exists (the attack dissolves: there is no
SHEET6-A3L1-REVIEW.md:169:  landed on the same cells. Worth a comment in the code, nothing more.
SHEET6-A3L1-REVIEW.md:180:  ⊖ ≠ 0. Odd l has M = 1 (restored 8.4) — nothing left over. The e0 = 1
postverdict.md:5:2. char-0 run of the core (open_8_28_c2_v6.q.ms, queued lane 2) -> if [1] over Q:
postverdict.md:7:3. Subcase (1): open_8_28_c1_v6 (73-var core, queued). BOTH subcases empty over Q
postverdict.md:14:1. Extract solutions: msolve -P 2 (rational parametrization / RUR) on the core.
postverdict.md:19:4. If solutions persist across primes: attempt Hensel lift / char-0 RUR
SHEET6-H3.md:9:(0,y) via Prop 9.3 case IV contradict the normalization of the Sigray engine
SHEET6-H3.md:14:satisfying every printed normalization constraint exists (§5b, r10/M4) —
SHEET6-H3.md:15:BUT a PROVED quantitative replacement (Theorem H3-psi, §4a) kills, from
SHEET6-H3.md:53:  "This, however contradicts Theorem 6.1 [l_f < k_f]." QED.
SHEET6-H3.md:66:## 2. Ground truth: Thm 6.1, its chart, and the normalization
SHEET6-H3.md:69:- Lemma 2.1 (pp. 8-9): normalized counterexample (f,g); f^+_{(1,1)} =
SHEET6-H3.md:75:  l_f <= k_f. Moreover, k_f = d_{(0,x)} and l_f = deg(p_{(0,x)}), so
SHEET6-H3.md:119:  cup V_{2,a} iff p_F has more than one root.
SHEET6-H3.md:127:Therefore   k_f / l_f  >=  deg(p_G) / d_F  =: R  >  1   by case IV (l).
SHEET6-H3.md:177:### 4a. Theorem (H3-psi). Let (f,g) be a normalized counterexample, and let
SHEET6-H3.md:294:  Normalization audit: l_f < k_f (Thm 6.1) ok; (k_g,l_g) = (5/4)(8j,4j) =
SHEET6-H3.md:320:- Superset entries (r8/M6, r9/M2, r9/M6): 30+8+45 = 83 more surviving
SHEET6-H3.md:337:thesis's td>=6 theorem REMAINS incomplete as printed for the G3 rows: row
SHEET6-H3.md:341:does not decide" (row 10 stays covered by Orevkov/Domrina/Zoladek
SHEET6-H3.md:346:IIa_0 low-lambda steps) immediately before the IV-capable node — the
SHEET6-H3.md:364:  root's St 9.2 signature — all case-I self-loop shapes (1/2,1,2,1) and
SHEET6-H3.md:393:    # prints the §5 table counts, per-hit dispositions, survivor traces
SHEET6-L1.md:54:    restored Prop 8.4 kills the merge: the whole book closes.]
SHEET6-L1.md:173:  theorem, independent of how B is priced or entered.
SHEET6-L1.md:244:(but M = 1: dead by restored 8.4); l = 2, nu odd: s = t^2 -
SHEET6-L1.md:383:   Domrina-Orevkov's splice methods also stopped.
CAMPAIGN.md:10:  bracket, convex-hull lattice enumeration, Generator A, msolve/Singular emitters
CAMPAIGN.md:11:- `tests/test_jc.py` — property tests + hand-checked lattice counts
CAMPAIGN.md:18:lattice points of hull(N(P)) and hull(N(Q)); equations = all coefficients of
CAMPAIGN.md:23:GB = [1] mod p  =>  strong evidence the reduced case is empty (theorem-grade
CAMPAIGN.md:29:- Pipeline validated: solved case (9,24)-(3) core = EMPTY [1] mod 65521 in 2.3s
CAMPAIGN.md:47:  torus-normalized reg_9_24_c3 (57/55 vars, the smallest solved case) both ran
CAMPAIGN.md:53:  vars in 0.3s but densifies (median eq 131 terms). Racing v3 (cascade core,
CAMPAIGN.md:64:  grading (GGV's valuation order) to avoid densification; then Generator B.
SHEET6-TDUNIFORM.md:3:Status: PROMOTED (SHEET6-TDU-REVIEW.md all fronts + sec 10 numeric reconciliation: PRIME THEOREM stands — single-pole excluded at entry for every prime td; authoritative composite survivor table td=4..16: 0/4/16/16/23/71/48/87/212, Sigma-lambda=0 counts -/0/0/2/2/2/4/6/4; C1 namespace fix verified, no further edits). Original status: COMPLETE (2026-08-10, this session; unreviewed). Mission: SHEET6 campaign
SHEET6-TDUNIFORM.md:7:general gcd/budget pattern, and state the theorem actually provable.
SHEET6-TDUNIFORM.md:19:- **Theorem TDU (§6): for every PRIME td, ALL single-pole configurations
SHEET6-TDUNIFORM.md:38:Setting: (f,g) a normalized counterexample of type (alpha,beta) (Not 2.4
SHEET6-TDUNIFORM.md:137:  Every prime td has live = 0 (the §2 theorem, mechanically re-verified);
SHEET6-TDUNIFORM.md:157:  under-explored III children at budget > 4).
SHEET6-TDUNIFORM.md:238:## 6. What is actually provable (theorem + perimeter)
SHEET6-TDUNIFORM.md:240:**Theorem TDU (td-uniform single-pole ENTRY exclusion).** Let (f,g) be a
SHEET6-TDUNIFORM.md:241:normalized counterexample with a single pole vertex (T_a,pole = {F}),
SHEET6-TDUNIFORM.md:259:**Theorem TDU-neg (non-generalization).** The promoted kill set (pin +
SHEET6-TDUNIFORM.md:322:  (SHEET6-CAMPAIGN §6 item 4, the Domrina-Orevkov-type split) is now THE
SHEET6-TDUNIFORM.md:385:- **Anatomy of 41 vs 16** (same BFS, traces kept, only the flag toggled):
REDUCE4-REVIEW.md:27:  q0=11 ((q_k): v_{4,-1}(A0)=11, gcd(3,11)=1); enR=(33,11)/11=(3,1) lattice ok;
REDUCE4-REVIEW.md:90:   lattice en(R)/st(R), killing unauthorized positive-axis corners.
REDUCE4-REVIEW.md:92:   paper practice (paper is no more explicit). DESIGN-JUSTIFIED.
REDUCE4-REVIEW.md:106:    confirmed in GGV1 tex; d0 bounds are pure lattice; PLLC via GGV5
REDUCE4-REVIEW.md:113:- Overall: every kill traceable to a cited result or to the design's
REDUCE4-REVIEW.md:126:  en(R) = (27,9)/7 not a lattice point (R1 lattice test fails)", status
REDUCE4-REVIEW.md:142:  with three riders: (a) run the design's G4 cross-check lane before any
SHEET6-CLASSICAL.md:10:  T1 SPLICE / LINK AT INFINITY:  PASS — edge dets positive, all pinned
SHEET6-CLASSICAL.md:14:  T2 ABHYANKAR-MOH / VALUATION:  PASS at poles (exact, ord_t f_y = -39
SHEET6-CLASSICAL.md:18:     (B/x resolution tails unpinned); its chi-shadow (delta ledger)
SHEET6-CLASSICAL.md:20:  T4 JELONEK:                    PASS — mu(F) = 6 exact by Bezout;
SHEET6-CLASSICAL.md:60:## 1. T1 — Splice diagram / link at infinity
SHEET6-CLASSICAL.md:66:Criteria used (stated in full before applying):
SHEET6-CLASSICAL.md:67:- (EN-1) [Eisenbud-Neumann, Ann. Math. Studies 110, Thm 11.2] A graph
SHEET6-CLASSICAL.md:71:- (EN-2) [EN, splice positivity for germs] The splice subtree of a LOCAL
SHEET6-CLASSICAL.md:75:- (N-3) [Neumann, Invent. math. 98 (1989)] The link at infinity of a
SHEET6-CLASSICAL.md:76:  reduced algebraic curve is determined by the splice diagram computed
SHEET6-CLASSICAL.md:80:- (RH) Riemann-Hurwitz for ghat: Cbar -> P^1 of degree 6 (poles only at
SHEET6-CLASSICAL.md:81:  P_1, P_2, order 3 each), with NO affine ramification: J(f,g) = 1 makes
SHEET6-CLASSICAL.md:86:### 1a. Splice data (engine sec 7)
SHEET6-CLASSICAL.md:123:r_X]/2, using the T2 valuation formulas e_p = n_p(282 - S_p)/42 (B) and
SHEET6-CLASSICAL.md:144:## 2. T2 — Abhyankar-Moh / semigroup arithmetic
SHEET6-CLASSICAL.md:146:VERDICT: **PASS at the poles with zero slack (exact valuation identity);
SHEET6-CLASSICAL.md:151:- (AM-1) [Abhyankar-Moh, J. reine angew. Math. 276 (1975) / semigroup
SHEET6-CLASSICAL.md:152:  paper 1977] For a curve with ONE place at infinity the semigroup
SHEET6-CLASSICAL.md:157:  one-place semigroup chain does NOT apply to it directly; per-place
SHEET6-CLASSICAL.md:160:- (AM-2) (classical, valuation form of J(f,g) = 1 along a fiber) On the
SHEET6-CLASSICAL.md:164:  contact tree, this is the two-term Abhyankar valuation bookkeeping.
SHEET6-CLASSICAL.md:229:  NOT apply to the plain compactification; the Orevkov-style application
SHEET6-CLASSICAL.md:232:  B-internal and x-internal resolution data — exactly the unpinned tail
SHEET6-CLASSICAL.md:246:resolution-graph Euler numbers cannot produce a contradiction at
SHEET6-CLASSICAL.md:261:## 4. T4 — Jelonek asymptotic variety
SHEET6-CLASSICAL.md:267:- (J-1) [Jelonek, Ann. Polon. Math. 58 (1993)] For a dominant polynomial
SHEET6-CLASSICAL.md:273:- (J-2) [Jelonek, degree bound; Testing sets for properness, 1999-2002]
SHEET6-CLASSICAL.md:297:enormous slack, no kill possible from it here.
SHEET6-CLASSICAL.md:301:(from the c_p(a) correspondence), the A-M semigroup chain on A(F) is a
SHEET6-CLASSICAL.md:325:   evaluated (data-free); (ii) T3's full log-BMY needs the B/x
SHEET6-CLASSICAL.md:326:   resolution tails (sec 3b); (iii) (J-2)'s exact constant quoted from
SHEET6-AF2.md:140:  F + 0 ∈ T_a↗, therefore λ_F ≥ 1", p. 54) because λ ≥ 1 suffices for its
SHEET6-AF2.md:154:Both classes ride ONE step (hiii_compose trace, reproduced §5): r10/M4
SURPLUS.md:9:origin), widths w_P,w_Q, bottom corners p0,q0. Orientation normalized so the gap
SURPLUS.md:11:irrelevant to counts). Hypothesis (i) verified: p0+q0=(k+1,1), unique lattice
SURPLUS.md:18:- n_keys: lattice count of block Minkowski points with >=1 live det!=0 pair,
SURPLUS.md:39:| swap_8_28_c2 | 2 | (1,2) | 2  | 3  | yes  | 9      | 8     | 1       | (4,7) PINS (same, normalized) | 1 | MATCH   |
SURPLUS.md:77:normalization (P,Q) -> (Q,-P) if needed so the gap side is Q:
SURPLUS.md:84:  {p0,q0} = {(1,0),(k,1)}; normalized: p0 = (1,0), q0 = (k,1);
SURPLUS.md:91:resp. Q is the full ladder of d2*c+1 resp. lattice points between bottom and
SURPLUS.md:106:only there. The block is therefore SELF-CONTAINED: its equations involve
SURPLUS.md:154:regime-dependent (Theorem below and scope map).
SURPLUS.md:162:THEOREM (condition (iii) from polygon data, regime (k,d2) = (2,2)). Let (P,Q)
SURPLUS.md:173:* = unit; all coefficients are lattice dets det(p,q)):
SURPLUS.md:201:(assertion-locked) for open, swap (after (P,Q)->(Q,-P) normalization), and
SURPLUS.md:206:core ideal - exactly LEMMA.md's ideal statement, now derived from corner
SURPLUS.md:212:OUTER column: stratum w = 1 (one lattice step below the top edge of
SURPLUS.md:271:  d2 >= 1 in scope. Main theorem — condition (iii) with surplus = 1,
SURPLUS.md:286:- §theorem: the chart-free "ideal membership" sentence is corrected to RADICAL
SURPLUS.md:295:  are torus-EMPTY, proved by exact resultant certificates (surplus_ext.py
SURPLUS.md:297:  verdicts at (2,3) (= toy_w3) and (2,4) are upgraded to exact theorems
SHEET6-R6.md:54:Shared kill (test A, BEFORE the banked "binding" suffix test can bind):
SHEET6-R6.md:234:  m>=3 pattern form at F_s must be computed before claiming the kill.
SHEET6-MP-REVIEW.md:1:# SHEET6-MP-REVIEW.md — Adversarial review of SHEET6-MULTIPOLE.md (0827409), the Theorem MP synthesis
SHEET6-MP-REVIEW.md:6:in the repo; this review therefore audits (a) the doc's own provenance map
SHEET6-MP-REVIEW.md:41:corrected. Theorem O stands. The finite-book rider is the one demotion.**
SHEET6-MP-REVIEW.md:60:- **Quarantine honored.** The three §7 blocks (prime-partition kill,
SHEET6-MP-REVIEW.md:66:  (8=3+5 etc.) stay in §7. (ii) Theorem O's m-uniform escape claims
SHEET6-MP-REVIEW.md:151:engine sweep)", and the phase-3 root menu should gain the l-family before
SHEET6-MP-REVIEW.md:153:Same tier as before (H1 + capped sweep) — no tier change, no new survivor.
SHEET6-MP-REVIEW.md:194:spot Theorem O claims.
SHEET6-MP-REVIEW.md:215:  pins. Theorem O's "solves every located printed constraint" stands.
SHEET6-MP-REVIEW.md:248:… to a finite book of jump-vertex cells" and Theorem O's "the finite book"
SHEET6-MP-REVIEW.md:249:are theorem-grade only in the per-frame sense; globally the book is
SHEET6-MP-REVIEW.md:284:    S. Suffix (printed): restored M ≠ 1 kill (MP2) + single-pole engine +
SHEET6-MP-REVIEW.md:302:   ground of §2c; add the l-family to the phase-3 root menu before any
SHEET6-MP-REVIEW.md:308:   to §8's next steps — it is arguably the cheapest high-value target: the
SHEET6-LROOT.md:157:normalization (Lemma 2.1(ii)) makes f and g exhaust together on the
SHEET6-LROOT.md:249:### 5c. The surviving attack surfaces (precise, none printed)
notes.md:3:(Working notes per DC's request: avenues, decisions, findings. Not a paper draft.)
notes.md:7:  We reduced both its subcases to small "cores" (30 and 73 vars) via:
notes.md:8:  direct polygon transcription → torus normalization → gauge analysis
notes.md:17:- Verdict pending: msolve on the open cores (fleet: ultramem-1 + jc-b).
notes.md:20:## Avenue map (approved 2026-07-28)
notes.md:21:1. **(72,108) resolution** — in flight. Either bound→125 (after char-0
notes.md:47:- Is the open-c2 core's grind "fat empty certificate" or "deep small variety"?
notes.md:49:- Cascade3-over-ℚ soundness audit + G0 string identities still owed before any
notes.md:58:  emitted as partial-core fleet jobs instead (sound mid-cascade states).
notes.md:61:  qualitative difference between open and solved cases (after core hardness
notes.md:68:  Cascade3 manages only 43/830 b-eliminations before swell (73 min). GGV's §4
notes.md:76:  at one prime. Remaining: complement = core + (a2=0 or a6=0) — split into
notes.md:81:  successful repoint attempt; giant-core jobs remain banned on 976GB boxes.
notes.md:90:  is a SYMBOLIC theorem-fragment, not an F4 result: the cascade+chart
notes.md:93:  random exact-rational chart points (original equations + stored
notes.md:118:  REMAINING for full (72,108) discard -> bound 125: subcase (1) (c1 core
notes.md:133:  lane 1 (v6 core / chartG / chartC / strict x char-0 + three primes) —
notes.md:137:  vertex normalization a1*b3=1 vs gap-column death ((q0)_x=2) =>
notes.md:139:  b3=0 contradiction. Chart-free: a2^2*a6 in I(core), DERIVING the
notes.md:146:  COEFFICIENT-FREE (lattice arithmetic; RHS = x^(ceil(b/a)-2), matching all
notes.md:159:  identity). Transferable core = valuation-counting discipline; its TL1 is
notes.md:160:  precisely our surplus-condition theorem (level filtration ~ p-adic
notes.md:161:  valuation), verified on the c2 chain + a moment toy. Converges with the
notes.md:170:  posture: cooperative (engage Helali, Suzuki, GGV; Leiden norms). c1-extract
notes.md:171:  diff vs our core queued (crosscheck/c1_extracts/).
notes.md:179:  locked to the audited chain. Vertex-gap now fully polygon-theoretic in its
notes.md:181:- Ops: rev-order leaves deployed BOTH boxes (foreground file-based — the ssh
notes.md:184:- SURPLUS-REVIEW.md: theorem CONFIRMED at variety level (scope map predicted
notes.md:189:  the vertex-gap theorem in the (2,2) regime — awaiting DC's go-ahead per the
notes.md:222:- SURPLUS-EXT Phase C: surplus-4 variant THEOREM at (2,3) (dual proofs:
notes.md:223:  resultant w/ constant lead + structural divisibility); torus-emptiness also
notes.md:230:  completeness + beyond-150 relevance). P1 avenue now fully delivered:
notes.md:231:  theorem grid (2,2),(2,3),(2,4) + k>=3 impossibility + coverage table.
notes.md:246:## 2026-08-07 (loop): residue theorem lands; farm gate-complete; leaf retired
notes.md:247:- **RESIDUE.md committed (e67c50a)**: R_{k,d2} IS a Grothendieck residue — iterated residue of dP∧dQ/(x^{k+2}A^{k+2}) at the toric boundary point {P=0}∩{x=0}. Three interpretations verified by exact arithmetic on 11 cells (48 checks): CT/contour form, Grothendieck form, Koszul moment functional spanning the reachable cokernel of ad_{xA}. Naive dP∧dQ/P^{k+2} refuted (exact form, residue ≡ 0). Uniform theorem all k,d2≥2: surviving outer extra = ±(k+2)/C((k+1)d2,k+1)·a2^{(k-1)d2}·R — explains every mystery unit (5,21,55,99,1001,364) as moments at top pivot; replaces per-cell certificates. conj:R now = its rigidity half only. Correction: sum starts j=max(k+2,d2).
notes.md:252:## 2026-08-07 (loop, later): deg<=150 sweep DONE; farm dispatch underway; credits restored
notes.md:253:- Sweep final: 34 families, 62 .ms files (4.5 GB, largest 565 MB), 22 emitted-system cases + partials/cores. NOT COVERED (reduce4 STUCK, psi_j precondition / multi-root chain edge): 12_36mn23d144_r0-r2, 6_15mn27d147, 10_40mn32d150_r0-r1 — these stay open regardless of farm verdicts; candidates for a reduce4 extension later. PARTIAL/CORE emissions are valid (cascade steps are equivalences); they're just less reduced.
notes.md:256:- Credits: user purchased more; probe confirmed live. Launched queued agents: sheet-6 case-bash build + DC(2) degree-3 slice (both in flight).
notes.md:273:  as printed (JC td<=5 still safe via Orevkov/Domrina/Zoladek). Next: H3 audit
notes.md:279:- SHEET6 campaign (4835b13, UNREVIEWED): engine reproduces pilot; Lambda<=7 = 14 rows; td=6 rows 2,3 EXCLUDED; ~15 case-III s-tails + IV-terminals gated on H3 (root-kill). HEADLINE CLAIMS: 3 new thesis errata (E2-E4, lam=0 self-loop families the thesis says don't exist), G2 (St 9.12's kill set can't close its own IV-terminals — unstated H3 load-bearing), G3 (thesis silent on rows 1,5,7,10 => Sigray td>=6 INCOMPLETE AS PRINTED; td<=5 safe via Orevkov/Domrina/Zoladek). If review confirms: sheet-6 exclusion is genuinely open => our campaign = novel work, and RECON's "independent reproof" language needs qualification.
notes.md:281:- Adversarial reviews launched in parallel: SHEET6-REVIEW.md (vs sigray_full.pdf ground truth) + DC2-REVIEW.md (truncation-artifact attack prioritized).
notes.md:282:- Farm: both boxes 4 verdicts each (all EMPTY so far), now grinding 4_12mn34d64_c2_core (35+ min in). 
notes.md:286:- 2026-08-07 night 2: TWO-POLE NOT EXCLUDED (284d847): exhibit survives with slack 1; 3 residue + 9 IV survivor classes; td=6 hinges on L1 (merged-pattern l>=1 inadmissibility). Launched combined AF2+2POLE adversarial review + dedicated L1 attack in parallel. THE FORK: L1 holds => td=6 theorem; L1 fails => counterexample template at the (3,3) merge.
notes.md:288:- 2026-08-07 night 4: L1 PARTIAL (62335cc): merged pattern squeezed to 3 shapes via pin-propagation (mu=(1,1),k=0,lam=0); 2 of 3 proved empty; the third (IIa nu=3,l=1) is COEFFICIENT-CONSISTENT with explicit unique solution a1/a2=2+sqrt(3) — two-pole funnels to unique merged child (6,12,3,2,5)@lam0. Survivor book now: single-pole 4 r9/M2 (AF3, thesis-forced) + two-pole A + 4 IV classes on the rigid template. Closing needs global h1-branch accounting or Puiseux transport (beyond printed thesis). Combined AF3+L1 adversarial review launched. THE PICTURE: td=6 sheet-6 is one rigid coefficient template away from either a theorem or a counterexample search target.
notes.md:289:- 2026-08-07 night 5 (905db83): A3L1 review — ALL FRONTS CONFIRMED, both promoted. CANONICAL BOOK: td<=5 CLOSED (0 survivors, independent of AF2); td=6 = 4 single-pole r9/M2 (thesis-forced entries) + two-pole residue A on the unique rigid template (merged child (6,12,3,2,5)@0, a1/a2=2+sqrt3). Endgame agents launched: (1) lam_root>=1 ledger attack (cuts 8->4), (2) coefficient-level template lift (genome -> edge consistency -> formal candidate or death edge; sizes farm computation if candidate). Errata E1-E9, five proof-level.
notes.md:290:- 2026-08-07 night 6: LROOT decided (SHEET6-LROOT.md, UNREVIEWED): lam_root>=1 REFUTED — stronger, lam_root = 0 is FORCED at every case-IV terminal (IV's own hypothesis (0,y) ∉ V_2a = "single root direction" by Def 3.4, so NO branch leaves the chain at the root; the psi-charge lives in the OTHER tree component (St 3.3) so no double-charge was ever possible, but no y-side root unit exists either). Full Prop 7.5 (22) Euler-ledger itemized and BALANCED at 0 root-lambda for all 8 survivors (engine cases/lroot_ledger.py, exact, asserts; gates untouched PASS). Book STAYS 8. Positive yield: (i) every carrier forced to a single x-side cv vertex, kappa_G=1, x-side one unsplit Puiseux cluster below height R>=3 (2 vertices or kappa>=2 blow the budget) — new pin for the template lift; (ii) the 4 slack-0 classes are TOTALLY rigid: x-mass exactly psi=R-1, orbit cv masses exactly the (24)-prices, delta_a = 0 on EVERY fiber of the pencil; (iii) L1's merge blind spot re-derived from the budget side (resonant q-orbit direction carries no punctures => empty ledger row). New erratum E10 (St 3.15 (i)/(iii) labels swapped; thesis usage consistent with the swap). Surviving attack surfaces, precise: delta-strictness at mult>=2 direction collisions (would kill all four slack-0 at once — Prop 7.3 equality question, not printed), x-side-pin vs template realizability, h1-branch budget.
notes.md:291:- 2026-08-07 night 7: TEMPLATE LIFT decided (SHEET6-TEMPLATE.md, UNREVIEWED): FORMAL-CANDIDATE — the coefficient-level lift of the two-pole rigid template EXISTS; no edge dies. Genome fully explicit (kappa=42 ladder pi=0,2/7,16/21,37/42; all f/g/h1/h2 patterns at R,F_s,G_m,P_i; 2 punctures x 42 series + 42 B-side = k_f 126). Sweep highlights: (i) h1-branch count (St 3.11(i)+8.3(ii)) KILLS the naive tower reading m_{F_s}=1 (16<=7) and forces approximate-root tower (k0,l0)=(2,3),(k1,l1)=(3,4) UNIQUE (h1 ~ f^{4/3}); supplies the missing proof of St 9.6's silent i=deg(p_G)/M_G (erratum candidate E11); (ii) h2-collapse W(t)=t(t-b)^3-(t-a1)^2(t-a2)^2 must drop to deg 1 — forcing EXACTLY b=2sig/3, a1a2=sig^2/6: the L1c rigid coefficients RE-DERIVED from branch counting, independent of the 8.1(iv) ODE; (iii) three more kill chances pass by exact identity: pole-lead cancellation m_i^2=s0*lam_i^3 automatic, H^3=s1*S^4 transport closes via c_m^7=A, h2-lead pole identity 27a(a-b)^3=sig^3(a-3sig/4) exact over Q(sqrt3); (iv) all 12 (edge,h) count/d-ladder cells EXACT (leak-free); (v) minimal-tower branch forces FIRST-STEP merge (m-growth lock; 2POLE 7.3 restored). New pinned data: b2=(3/4)sig h2-direction, p_h1,P=eta^2-(4/3)w^2, w_i^4 formulas, h1-corner (168,56). Engine cases/template_lift.py: 46 checks 0 FAIL. Residuals R1-R6: cancellation depths (R1, decidable by staged linear system ~10^2-10^3 unknowns, hours-days on farm — the cheap decisive experiment), h-Newton budgets/x-side (R2, merge with LROOT pin), cv realizability (R3), root tower depth>=3 with (k2,l2)=(7,23) + M_R (R4), Jacobian closure (R5), deeper-tower window 4/3<l1/k1<3 (R6, same mechanism recursively). td=6 now rests on R1-R6; naive 17.6k-var msolve Ansatz ruled out, template-constrained staging sized and buildable on lib/jc.py.
notes.md:293:- 2026-08-07 night 7 (c4624ff): LT review promoted LROOT+TEMPLATE (E11 demoted: printed-tier derivable; 3 genuine kill chances). R1 gated REDESIGN-then-GO; R1 agent launched with the 4 mandated fixes (tower g^2-s0*f^3 gauge a=0, R6-first, co-staged (f,g)+x-side lead, pre-registered J-closure interpretation). Pre-registered: R6 empty + R1 UNSOLVABLE = two-pole td6 template DIES (theorem-grade); R1 SOLVABLE = formal candidate deepens toward R2-R5. This is the decisive experiment.
notes.md:296:- 2026-08-09 early (5df68d2): R6 print campaign CLOSED — 6/9 window cases dead; survivors {minimal (3,4), (1,2), (2,3)-chain(6,17), (2,5)-chain(6,23)} SURVIVE-IN-PRINT (nothing printable kills them). R1 must enumerate 4 branches ((1,2) delta-spec written: one extra staged resonance level at G_m). When R1-build lands: extend to 4-branch enumeration, then ONE review over echo-rung + R1 before interpreting. Bonus pin a2/a1 = 2±sqrt3.
notes.md:297:- 2026-08-09 (f29eafd): R1 CAP-2 CORE EMPTY — GB=[1], char 0, 5s on ultramem (118 vars, 64 eqs, underdetermined-yet-infeasible = deep clash signature). IF faithful (review a9bb… in flight, incl. minimal-infeasible-subsystem extraction + hand re-derivation): minimal-tower genome DEAD; remaining branches (1,2), (2,3)-chain, (2,5)-chain need own cores; all four dead => residue-A EXCLUDED => td=6 = 4 single-pole classes only.
notes.md:298:- 2026-08-09 (d434895): R1 EMPTY RETRACTED — spurious doubly (msolve 0.10.1 silently mis-parses parenthesized input; system a-priori satisfiable; 57/57 shipped rows were silent truncations, zero discriminating rows). AUDIT: 401-file paren sweep — ONLY the r1 core affected; all (72,108)/farm/dc2 verdicts stand (our emitters expand fully). Emission rules hardened in AUDIT.md. Rebuild agent launched (4 mandates: paren-free, sentinel fix + discriminating rows, guards, verdict discipline; sibling-branch cores if cheap). Echo-rung work CONFIRMED by same review — R6 4-branch state stands.
notes.md:299:- 2026-08-09: R1 full-degree cores DISPATCHED to ultramem (sequential: w-free p-screen -> full p-screen -> char-0 decisive -> (1,2) sibling). All guards passed pre-flight; runner has verdict authentication. This queue IS the decisive experiment for 2 of 4 residue-A branches.
notes.md:301:- 2026-08-10 (post-reboot resume): jc-b was TERMINATED (preemption) — restarted, farm resumed cleanly (9 banked outputs kept, re-running the killed core.q). Box01: 6 EMPTY / 6 FAILED (big char-0 cores OOM-class; triage tier owed after queue drains). Ultramem R1 w-free p-screen ~1 day in, 1.07TB resident, alive. No LIFT-CERT yet. Loop re-armed.
notes.md:302:- 2026-08-10 (08fbbda): TD-UNIFORM entry theorem landed (UNREVIEWED, review launched): pinned M = b; PRIME td => all single-pole rows b=1 => excluded at entry, uniformly (scan verified td<=40; td=37: 8/8 dead). Composite residual grows (212 survivors at td=16); td=9 slack-6 chain shows budgets saturate; bottleneck = multi-pole 8.4 analogue. If review holds: JC2 geometric-degree ladder at prime td rests entirely on multi-pole configs. R1-acceleration agent still out.
notes.md:303:- 2026-08-10: TDU fully settled — PRIME THEOREM promoted (single-pole dead at entry for every prime td, perimeter H1/AF3-tier); composite table authoritative (212 survivors at td=16, lower bound); bottleneck = multi-pole 8.4 analogue. My td=9 'discrepancy' was a display-truncation miscount, caught by reconciler.
notes.md:304:- 2026-08-10 (c8f2cb0): R1 REDUCED queue live on ultramem (49 rows/63 vars, verdict-equivalent, soundness-proven). Old 128-var run killed per acceleration agent's recommendation. Sweep calibration: GB deep at every char (12 primes all timeout locally) — this is a real computation even reduced. Chain folds still grinding locally toward the (2,3)/(2,5) cores.
notes.md:305:- 2026-08-10 (353ed0d): CHAIN CORES LANDED. (2,5)-chain core NONEMPTY at p AND char 0 (487-elt GB, origin excluded) — the branch DEEPENS; deep-dive agent launched (dimension, degeneracy split, deferred-row evaluation: real template data vs artifact — this decides the counterexample frontier). (2,3)-chain core queued on ultramem behind reduced minimal queue. Byte-identity gate passed on the fold/CRT pipeline.
notes.md:309:- 2026-08-11 early: minimal-branch reduced wfree screen DIED at 1.5TB cap after 34h (no verdict); killed the auto-advanced (strictly bigger) full-p run; ultramem now dedicated to (2,5) ext decider (28h in). Minimal branch pivots to CHART DECOMPOSITION (agent launched: split reduced core into 4-16 guarded leaves w/ cover certificate, local calibration). The monolith era is over for this system class — decomposition always wins (campaign lesson, again).
notes.md:310:- 2026-08-11: ULTRAMEM TERMINATION ROOT-CAUSED — not Spot preemption: the STALE jc_deadline poweroff cron (leaf-era) fired (deadline passed 25 min before death). Cron removed permanently. Cost: 28h of (2,5) ext compute. Recovery: ext decider MOVED to box01 (on-demand, 16 threads, 250GB cap, alongside farm lanes); (2,3) chain queue launched directly on ultramem (40 threads); lifts resumed. STANDING LESSON (2nd occurrence): guest lifecycle machinery must be inventoried and wiped on every box reuse — added to ops checklist.
notes.md:311:- 2026-08-11 (e8839bb): minimal core decomposed (4 leaves, 1s each — monolith was foredoomed by relaxation artifact); UU chart NONEMPTY everywhere, core collapses to one conjugate-pair relation satisfied identically by template data. NO branch killed at core level yet — all discriminating content is in deferred bands. Minimal-branch ext build agent launched (mirrors (2,5) ext, in UU chart, with witness guard). Deciders running: (2,5) ext on box01, (2,3) chain on ultramem. (1,2) core to get the 4-leaf treatment after.
notes.md:315:- 2026-08-11 (5a75ee3): G_m BRANCHES DEAD (verified+reproduced): minimal at depth-84 over Qbar (family object), (1,2) at terminal core char 0. Q2 full-locus screen + (1,2) E5-port review agent launched (the two riders). If Q2 empties and the port survives review: residue-A exclusion rests solely on the (2,3)/(2,5) chain deciders (grinding ~24h each). The kill side is winning.
notes.md:319:- 2026-08-11 late: STUCK-FAMILY CLOSURE (33021f4): multi-root chain-edge cut implemented from GGV5's multiplicidad proposition — 4 of 7 stuck families now reduce fully (first verdict already: 12_36_r1_c3 EMPTY-BY-CASCADE, transfers to r2 twin); remaining 5 rho=2 families get guarded direct emission. The deg<=150 catalog now has NO family outside the pipeline. Emission driver detached (farm_stuck7.log, auto-finishes RED twins + queue + local msolve). Adversarial review owed on the cut transform before bound-150 claims.
notes.md:320:- 2026-08-12: 5 monolith deaths diagnosed (vmem-cap silent kills) — requeued: q2l at 900GB (box01), sat23 at 1850GB (ultramem). Stuck-7 driver DONE (post-processing complete; one rc=124 timeout in tail). NEW AVENUE LAUNCHED: classical kill-test battery on the template (splice/Neumann, A-M semigroup, log-BMY, Jelonek) — four independent topology/combinatorics tests, any one can kill the two-pole configuration outright. Cut-transform review still out.
notes.md:321:- 2026-08-12 (7242f2c): MATHIEU-ZHAO BREAKTHROUGH CLAIM — rigidity half of conj:R claimed PROVED (Theorem A, 15-line DvdK-mechanism ODE argument; M1-M5 machine checks pass incl perfect powers at all open cells). If review holds: conj:R closes at EVERY cell, strip theory uniform in (k,d2), paper1 conjecture becomes theorem. Max-depth adversarial review launched (fable) with small-degree counterexample sweeps + Lemma B bridge audit (agent's own flagged weak point). Workflows multipole-84 + sigray-audit grinding in parallel.
notes.md:322:- 2026-08-12 (ad709ae): CLASSICAL BATTERY — the template SURVIVES topology: splice/Neumann PASS (all determinants/multiplicities positive), Jelonek PASS, A-M valuation PASS at poles with ZERO slack (ord f_y = -39 exact match), genus balance closes identically. One new kill (pi_G=4 branch dead). Sobering + significant: four independent classical tests, none contradicts the template — it is topologically a legitimate candidate. log-BMY still open pending B/x resolution tails (the one classical test left). All conclusions transfer to all surviving branch variants.
notes.md:323:- 2026-08-12 (7179119): PAPER 1 v2 — the functional section is now THEOREMS (6.1 rigidity + 6.5 = former conj:R), 15pp, compiles clean. Ready for: (a) user's GGV follow-up note, (b) Zenodo artifact v2 (mathieu mode + MATHIEU docs added to bundle) when user wants. Still out: multipole-84 workflow, sigray-audit workflow, cut review, box01/ultramem screens.
notes.md:324:- 2026-08-12 (0827409): THEOREM MP LANDS (multipole panel, 21 agents, 3.2M tokens): the td-ladder bottleneck is SETTLED at the structural level — verbatim m-pole 8.4 is FALSE, but the maximal kill + merge calculus reduces EVERY (m,td) multi-pole configuration to a finite book of resonant jump-vertex cells (2<=M<=r<=m, l>=1, full anatomy pinned). All 5 angles survived their refuters. Combined with prime-td + conj:R-now-theorem: the JC2 exclusion program is now finite-book at every level. NEXT: enumerate + bash the jump-vertex book (workflow-shaped); sigray-audit still running.
notes.md:325:- 2026-08-12 (88186fd): SIGRAY FULL AUDIT (35 agents, 130 statements, 3.7M tokens): 10 NEW errata + 10 gaps found; every one triaged for campaign damage — NET RESULT: no promoted result damaged; multiple campaign readings PROVEN forced (H5a upgraded to printed-statement-forced via St 3.8; d_{f-a} reading mandatory via St 3.13/3.14). The thesis's section 2-6 foundations are now swept; the campaign's hypothesis perimeter is dramatically de-risked. Filing amendments owed (H3 quote, E-numbering of new errata) — doc-chore agent when slots free. MP integration review + cut review still out.
notes.md:326:- 2026-08-12 (eb0abdf): MP promoted (MP0-MP8+O; MP9 corrected; finiteness rider demoted to per-frame). THE one open axis = chain-depth closure lemma — max-depth agent launched (stabilization orbit-map / Puiseux jump-count angles). If it lands: jump-vertex book FINITE per (m,td), and with prime-td + conj:R theorem + MP, the whole exclusion program becomes a finite enumeration at every level — the shape of a full JC2 proof modulo bashing the book.
notes.md:327:- 2026-08-12 (depth): CHAIN-DEPTH CLOSURE LEMMA PROVED (SHEET6-DEPTH.md) — the M=1 chain step conserves w := (kap-rho)/nu on every l=0 step (the unbounded direction), resonant steps need Delta | num(w) and contract by <= 2/3, and the ENTIRE jump-cell menu factors through w (handshake kap_m - D/i = w; join forces equal w; nu determined per (kap_m,l)). Depth-invariance follows: menu constant beyond d0 = gen(W)+2. td=6: W={2}, menu == the promoted (2,3,1) cell exactly (explains 351/351). Bonuses: root merges need w<1 (one-line root kill); ZCH 0-edge is Prop 9.3 case (III) => needs w-ratio nu>=2 between chains (engine model corrected, no promoted conclusion touched); St 9.6(v) itself conserves w=3/2. 13/13 exact checks (cases/depth_closure_check.py). CONSEQUENCE: jump-vertex book FINITE per (m,td) — MP's demoted rider RESTORED (corrected book spec in SHEET6-DEPTH.md sec 8). The exclusion program is now a finite enumeration at every level, unconditionally at H1 tier.
notes.md:328:- 2026-08-12 (2c81954): DEPTH CLOSURE LEMMA claimed (w-conservation; book finite per (m,td)) — max review launched (a case-branch drift or normalization mismatch would fake it; SIGRAY-AUDIT interaction checked). If it stands: launch the jump-book enumeration workflow with the reviewed spec — the program's final computational phase.
notes.md:329:- 2026-08-12 (400b50b): DEPTH LEMMA PROMOTED — BOOK(m,td) enumeration is GO; enumerator agent launched (td 6-14, gate = td-6 record reproduction; mechanical kills inline; survivors banked for per-cell bash). The pipeline: prime-td theorem + Theorem MP + depth lemma + book bash = multi-pole exclusion per td; combined with conj:R theorem + degree farm = the full JC2 program, now finite at every level.
notes.md:330:- 2026-08-12 (book): BOOK(m,td) ENUMERATED (cases/book_enum.py, BOOK-ENUM.md, systems/book/*.json): td=6..14, m=2..floor(td/3), reviewed spec E/T/C'/J'/R/S with the mechanical arsenal inline (MP7 l=0, gcd menu M>=2, kap-window integrality, corrected ZCH case-(III) w-ratio, root w<1, MP9 even-l, St 9.4 root budget). GATE PASS: td=6 m=2 == the promoted record cell-for-cell (unique residue-A IIa (2,3,1) M=2 child (5,3,1/2), R empty). RESULT: 421 cells, 346 killed, 75 survivors = only 22 distinct classes (31 IIa — ALL l=1, M=r, the Theorem-O escape pattern; 33 ZCH — only at w in {4,6} with an integer-ratio partner, first at td=9; 11 family-I — only r>=3, m>=3; 0 ROOT anywhere: every alphabet sits at w>=1, td-uniform root kill). Prime td 7/11/13 panels EMPTY (all entries off-axis b>=2 — the multi-pole shadow of the prime theorem). Largest class: residue-A in 10/18 panels; largest panel m=4 td=12 (21 cells). NEXT: per-cell bash — Prop 8.1(iv) rigid solve + coefficient-vs-ratio match (IIa l=1 family first), suffix engine from child data at budget td-2, r>=3 log-obstruction for family I, M>=2 chain engine for the 27 off-axis entry classes.
notes.md:333:- 2026-08-12 (r2 interim): BOOK BASH ROUND 2 — 12 of 13 classes DEAD by first pass (only ZCH(2,3,2)M2@w6 survives); BUT the credit ceiling killed ~13 verify votes mid-run, so several 'confirmed' flags were VACUOUS (empty vote arrays). Credits restored; workflow resumed with cached bash results — live verifies + synthesis filling now. If kills hold: book = 7 surviving classes total, ALL of the rigid-template kind.
notes.md:334:- 2026-08-12 (fbcd663): BOOK FULLY ADJUDICATED — 22 classes, 75 instances: 15 classes DEAD (closed-form kill criteria discovered: ZCH iff (nu+1)|l, family-I iff l/r or r/l in Z — these are little theorems in their own right), 7 SURVIVE, every survivor a rigid one-scale template. CREDIT CEILING hit again mid-verifies (resets Aug 15 8pm PT): 7 r2 kills carry engine-verification only, review votes OWED; cut-transform review agent presumed dead the same way. Agent work PAUSED until credits; local+fleet compute continues. Standing queue on credit restore: (1) r2 verify votes, (2) cut-transform review relaunch, (3) ZCH(2,2,3)@w4 r1 votes.
notes.md:335:- 2026-08-12: cut transform PROMOTED (review passed; deg<=150 pipeline now fully load-bearing incl the stuck-7). Bound-150 blockers remaining: farm queue drain + big-core memory tier + two-machine replication decision + audit pass.
notes.md:336:- 2026-08-12 (9fff9fc): BOOK FULLY CONFIRMED (all r2 kills 2-vote). TEMPLATE-FAMILY ATTACK workflow launched — 5 angles on the shared mechanism of the 7 survivors: GALOIS descent (new — the templates live in Q(sqrt d), conjugation swaps the poles; one non-symmetric pinned datum kills), the L1 sec-7.2 global h1-budget (the identified missing layer), panel budget squeeze (b>=2 entries may not reach mu=1 arrivals), classical battery on the 6 untested templates (zero-slack valuation test), and Weyl quantization (DC2 divergence as a weapon). This is the shot at closing td<=14 multi-pole outright.
notes.md:337:- 2026-08-12 (33799c7): TEMPLATE ATTACK LANDS — book 27->23 (new law L6); three shield theorems prove Galois/budget/quantum have ZERO traction (templates conjugation-equivariant BY RIGIDITY — deep and slightly ominous); quantum divergence concentrates at the ONE resonant direction b. Everything now points at the same coordinates: L1 sec-7.2 coefficient tier at direction b.
notes.md:338:- GROK 4.6 EVAL (xmodel/grok-eval-20260812.md): impressively deep repo read; P(JC2 true) ~0.72; 5 avenues incl. S_6 monodromy product test (covering-theoretic, Sigray-independent — GOOD and new), J-jet at G_m on the 7 dead-stretch coeffs (overlaps our R1 but sharper framing), Theorem-A-on-depth-3-column (cheap, connects our two lanes), mixed-merge completeness crack (checks our book's quarantine). Also flags the cheapest logged-but-unrun shot: IIa(3,5,1) W-residual deg-2-vs-<=1.
SHEET6-DEPTH-REVIEW.md:6:DS4 (menu factorization), the Lemma (§6), the restored finite book (§8) —
SHEET6-DEPTH-REVIEW.md:25:  (§1 below); i-normalization consistent with MP/engines (§1c).
SHEET6-DEPTH-REVIEW.md:52:parent), F = G° the child; case (II) equations, i-normalized with
SHEET6-DEPTH-REVIEW.md:80:| case | equations | w-law (i-normalized, μ = 1) | where it occurs in the lemma |
SHEET6-DEPTH-REVIEW.md:90:whose lattice argument I re-derived independently: exponent lattices below
SHEET6-DEPTH-REVIEW.md:96:vertices). Moreover the argument is P-robust: whichever P Prop 9.3
SHEET6-DEPTH-REVIEW.md:113:### 1c. Normalization audit vs MP5/MP6 and the engines
SHEET6-DEPTH-REVIEW.md:127:  normalization slip — it is not: St 9.6's proof itself computes
SHEET6-DEPTH-REVIEW.md:139:| Not 3.5 (κ_F) | GAP = H5a; jump/max reading FORCED (via St 3.8) | DS1(c) evaluates κ_F at F = I_{P′}(α′_{j′}) as κ′/e′_{j′} — the JUMP value | YES — at a V₁ₐ vertex the max-over-branches equals the jump value: branches realizing u characteristically share e′_{j′}/κ′ = gcd-lattice of (e′_{j′−1}/κ′, u) (rational, branch-free); non-jumping branches give the coarser (smaller) κ/e_{j−1}. Re-derived here. Prop 9.3's proof-internal κ_F = κ_G/ν_G is the same-branch jump-value relation — H5a-consistent |
SHEET6-DEPTH-REVIEW.md:150:- Handshake: from (c)+(d) i-normalized, κ̄_m − D_m/i = (κ̄_e − ρ_e)/ν_e =
SHEET6-DEPTH-REVIEW.md:197:  still be needed before the next resonant step (positivity
SHEET6-DEPTH-REVIEW.md:199:  written therefore proves realization by depth ≤ 2·gen+2, not gen+2.
SHEET6-DEPTH-REVIEW.md:284:    S. Suffix layer (printed): MP2 restored kill below G*, single-pole
SHEET6-DEPTH-REVIEW.md:303:   audit-corrected St 3.8, or the equivalent lattice argument (at a
SHEET6-DEPTH-REVIEW.md:304:   strict V₂ₐ meet the contact exponent is in the common lattice, else
SHEET6-TEMPLATE.md:28:FIRST-STEP merge is restored (m-growth lock, sec 2c-E2). Residual
SHEET6-TEMPLATE.md:160:F_s: B = (3/2)A unique (computed here in the honest i-normalization
SHEET6-TEMPLATE.md:186:⊖ p21^{6 l1/k1}, and the thesis's own silent normalization in St 9.6
SHEET6-TEMPLATE.md:191:SIDE THEOREM (merge depth locked to tower depth). In the minimal-tower
SHEET6-TEMPLATE.md:196:RESTORED at the lift level for this branch; deeper merges live only in
SHEET6-TEMPLATE.md:295:  138). A contradiction here would be an L2-successor theorem; the
SHEET6-TEMPLATE.md:307:  deg p_{h3,R}) in {1,3}; if the two-pole-restored Prop 8.4 layer can be
SHEET6-TEMPLATE.md:343:until a terminal nonlinear core of expected size <= 20 vars, msolve-easy)
SHEET6-TEMPLATE.md:358:2. The thesis's silent i = deg(p_G)/M_G normalization in St 9.6 (p. 52)
SHEET6-R1-REVIEW.md:1:# SHEET6-R1-REVIEW.md — Adversarial review of the R1 cap-2 core kill (f29eafd)
SHEET6-R1-REVIEW.md:4:Scope: the SHEET6-R1.md sec 6 claim "`systems/r1/r1_gmband_core.ms`
SHEET6-R1-REVIEW.md:6:coefficient level, conditional on core-emission faithfulness". Ground
SHEET6-R1-REVIEW.md:46:dropped by sentinel cancellation, and the banked core contains NONE of
SHEET6-R1-REVIEW.md:51:the full-degree core (SHEET6-R1 sec 5 step 1), which has never been
SHEET6-R1-REVIEW.md:70:  normalization re-verified by hand. Quadratic form = both signs kept.
SHEET6-R1-REVIEW.md:81:  FREE (E5 quartic relation deferred to terminal core)"). The doc's
SHEET6-R1-REVIEW.md:85:  template constraint that is OMITTED, the core is weakened, never
SHEET6-R1-REVIEW.md:107:mandate satisfied. Normalizations line up exactly (through-factor count
SHEET6-R1-REVIEW.md:118:family is the (1/21)-lattice condition at the kappa = 21 vertex
SHEET6-R1-REVIEW.md:133:set. The emit_gm_core lossy filter (`any(k[-1] == HIVAR)`) therefore
SHEET6-R1-REVIEW.md:135:flags conservative" (gate 3) strips sentinels from BOTH sides before
SHEET6-R1-REVIEW.md:203:   /tmp/r1rev/core_correct.ms, byte-provenance from the same state).
SHEET6-R1-REVIEW.md:210:A hand-verifiable contradiction chain over Q(sqrt3) therefore does NOT
SHEET6-R1-REVIEW.md:211:exist for this core — the opposite: a hand-verifiable SOLUTION exists.
SHEET6-R1-REVIEW.md:247:terminal core, never yet built or solved. The book of 4 + residue-A
SHEET6-R1-REVIEW.md:252:Required fixes before ANY future core verdict is bankable:
SHEET6-R1-REVIEW.md:263:   g^2, f^3 and the jets BEFORE any subtraction/combination; re-run
SHEET6-R1-REVIEW.md:266:3. **[1]-plausibility guard**: before accepting an empty-variety
SHEET6-R1-REVIEW.md:278:   encoded core.
SHEET6-R1-REVIEW.md:291:- Reproduce [1] + artifact: `msolve -g 2 -f systems/r1/r1_gmband_core.ms`
SHEET6-R1-REVIEW.md:295:  /tmp/r1_state.pkl.cap2: /tmp/r1rev/reemit.py -> /tmp/r1rev/core_correct.ms.
SHEET6-PILOT.md:44:  ⇒ under Λ ≤ 6: β ≤ 6, plus 1 < α < β, gcd(α,β) = 1 (type of normalized counterexample).
SHEET6-PILOT.md:46:  Pre-registered hand-check BEFORE coding: (B) fails its own equation: 75·(5+13) = 1350 ≠ 51·(1+26) = 1377.
SHEET6-2POLE.md:3:Status: PROMOTED (2026-08-07, SHEET6-A2P-REVIEW.md: mathematical core
SHEET6-2POLE.md:11:machinery read-only). Literature: refs/do.pdf (Domrina-Orevkov I),
SHEET6-2POLE.md:31:"Proposition 8.4. Let (f,g) be a normalized counterexample of the Jacobian
SHEET6-2POLE.md:75:- (iii) M=1 kill PARTIALLY RESTORED: for F on {G_m} cup (suffix), the
SHEET6-2POLE.md:106:1. SHARED TYPE: one (α,β) = (2,3) for the single normalized pair (f,g)
SHEET6-2POLE.md:118:   two-equation consistency is the resultant-type relation tying the
SHEET6-2POLE.md:119:   poles; it replaces "splice/linking data" in the Eggers-Wall frame.
SHEET6-2POLE.md:131:   normalization are the complete list. (Prop 7.5's Euler-characteristic
SHEET6-2POLE.md:152:## 3. Literature analogue: Domrina-Orevkov's multi-dicritical split
SHEET6-2POLE.md:156:COMPONENTS of the resolution at infinity (components of L~ on which F is
SHEET6-2POLE.md:170:whole case analysis over splice-diagram combinatorics (~19 configurations
SHEET6-2POLE.md:176:2. Their method has a PROVABLE ceiling (Orevkov's exotic-covering
SHEET6-2POLE.md:182:   (3+3 > 5), and DO's td=4 multi-dicritical treatment is splice-diagram
SHEET6-2POLE.md:220:  restored kill fires (interior merge) — KILLED.
SHEET6-2POLE.md:246:### 5a. The obstruction attack FAILS: minimum spend is 0, not > 4
SHEET6-2POLE.md:269:suffix = composed single-pole engine with restored M=1 kill, N1, E5-III,
SHEET6-2POLE.md:271:caps); kill histogram: 95.6% M=1-at-merge (restored Prop 8.4; percentage
SHEET6-2POLE.md:286:levels even before budget filtering.)
SHEET6-2POLE.md:342:  impossible (l = 0 gives M(G_m) = gcd(2ν, 2ν+1) = 1, killed by restored
SHEET6-2POLE.md:357:## 7. Consequences for the td=6 theorem statement
SHEET6-2POLE.md:365:   theorem can be claimed until L1/L2 (or a counterexample) resolves it.
SHEET6-2POLE.md:380:4. Domrina-Orevkov parallel (§3): as at td=4, the multi-dicritical/
SHEET6-2POLE.md:394:  mirrored from the thesis's own patterns; flagged, unproven).
SHEET6-2POLE.md:410:    # (kill histogram: 50097 restored-8.4 / 1373 suffix-dead / 336 N1);
SHEET6-HIII-REVIEW.md:17:- Front 4 (N1 gcd theorem, H5a): **CONFIRMED**
SHEET6-HIII-REVIEW.md:23:## 1. Front 1 — psi-budget derivation (Result 1's core kill)
SHEET6-HIII-REVIEW.md:67:  H4/AF3. The psi-budget THEOREM itself is unconditional on those.
SHEET6-HIII-REVIEW.md:148:Verdict: **CONFIRMED as a theorem under H5a**; H5a itself is the only reading
SHEET6-HIII-REVIEW.md:165:  integer kap-bar); (b) Not 3.8's F*c and the next step's Prop 9.3
SHEET6-HIII-REVIEW.md:168:  logged as an interpretation, not a theorem. (Same ambiguity family
SHEET6-HIII-REVIEW.md:226:remains externally covered (Orevkov/Domrina/Zoladek, RECON), so this is an
SHEET6-HIII-REVIEW.md:263:- No circularity found. Result 1's psi-budget theorem uses printed
SHEET6-HIII-REVIEW.md:271:  chain graph that Result 2 proves is not a theorem of the thesis's
SHEET6-HIII-REVIEW.md:296:- SHEET6-H3 (048f2d9): Fronts 1-2 CONFIRMED. The psi-budget theorem is
SHEET6-HIII-REVIEW.md:305:  N1 a clean theorem under H5a, which is coherence-forced). Its 9-class
conjectureE-plan.md:97:Iterated downward over `ℓ`, this yields `P_1(x_ℓ)=0` for all `ℓ ∈ [u_F,v_F]`, i.e. one more
conjectureE-plan.md:100:**Relation to the generalized Magnus expansion** (Theorem `prop:Magnus_formula_equivalence`,
conjectureE-plan.md:157:paper III ([GHLL3], see the authors' site) before trusting any surprising verdict.
conjectureE-plan.md:206:   theorem guarantees `B_max` is supported with the induced `c_β`; the pipeline must confirm
conjectureE-plan.md:228:show that the following conjecture implies the Jacobian conjecture" (§4, before `Jac_conj5`) —
conjectureE-plan.md:246:Caveats before announcing a kill: (i) the TeX source contains commented-out sharper case-split
conjectureE-plan.md:248:formulation; (ii) confirm the witness respects the exact normalizations (`c̃`-constancy, the
AUDIT.md:13:  → torus normalization fix_ones     (lib/jc.py, emit.py emit_normalized)
AUDIT.md:16:      V(core) = V(chartG) ∪ V(core + prod(pivots))
AUDIT.md:25:algebraic closure K̄ (claim 1); it can be torus-normalized within K̄ (claim 2);
AUDIT.md:26:the normalized solution survives to the Cascade3 core (claim 3) and hence lies
AUDIT.md:50:- *Support = hull ∩ Z².* Unknowns are one coefficient per lattice point of
AUDIT.md:52:  `lattice_points`, lib/jc.py:113-139, with `ccw_order` asserting strict
AUDIT.md:54:  hull is allowed, exactly as in the Prop 4.3 shape constraint. Lattice counts
AUDIT.md:56:  hand-verified via Pick's theorem in tests/test_jc.py:14-27.
AUDIT.md:72:  nonorigin variety therefore settles both readings by inclusion** — this
AUDIT.md:82:reg_9_24_c3 core EMPTY [1] mod 65521 in 2.3 s (README.md; runs/
AUDIT.md:91:## Claim 2 — Torus normalization is lossless for emptiness
AUDIT.md:112:  So every solution is torus-equivalent to a normalized one; conversely a
AUDIT.md:113:  normalized solution is a solution. Hence emptiness transfers both ways
AUDIT.md:117:**Why the hypothesis is machine-checked.** `emit_normalized` computes
AUDIT.md:124:det ≠ 0: proved-in-code. Pipeline behavior on normalized systems:
AUDIT.md:135:W = ∅ iff the final core system is empty.
AUDIT.md:165:  b-variables keeps every monomial b-degree ≤ 1 forever — substitutes are
AUDIT.md:169:  over on the core). The MAXTERMS_EQ guard only *aborts* (status
AUDIT.md:174:  audited numerically: sample random exact points of the core, reconstruct
AUDIT.md:192:**Statement.** For the finished core C,
AUDIT.md:194:**V(core) = π(V(chartG)) ∪ V(chartC)**, where chartC = core equations +
AUDIT.md:196:core empty ⟺ both leaves empty.
AUDIT.md:208:  literally a core point. So both leaves map into V(core).
AUDIT.md:209:- (⊆) At a core point, either every chosen pivot coeff is ≠ 0 — set
AUDIT.md:216:  monomials in original core variables (`info` records length 1 for each),
AUDIT.md:217:  so prod is a genuine core-variable monomial. The general-position code
AUDIT.md:233:**V(chartC) = V(core + a2) ∪ V(core + a6)** — the emitted kill-branches
AUDIT.md:238:a6 = 0. Substituting a2 := 0 (resp. a6 := 0) into the core is an isomorphism
AUDIT.md:239:onto V(core) ∩ {a2 = 0} (a2, a6 are interior P-coefficients, not corner
AUDIT.md:244:the core.
AUDIT.md:308:a theorem-fragment independent of F4 — valid over every field in which the
AUDIT.md:324:stored substitution logs: equation #3 evaluates to exactly −1 at all 6
AUDIT.md:370:     against the paper other than eyes + the lattice-count tests.
AUDIT.md:371:4. **Not** in the trust boundary: torus normalization (claim 2, self-
AUDIT.md:378:## Remaining obligations before any public claim
AUDIT.md:386:- [ ] **Certificates for cCa2 and cCa6**: rerun cCa2 lift with more
AUDIT.md:392:      before lifts land.
AUDIT.md:408:      before any "(72,108) family discarded / bound = 125" statement.
AUDIT.md:417:Hence V(complement) = V(core + a2*a6 = 0) = V(core, a2=0) ∪ V(core, a6=0),
AUDIT.md:431:contained parentheses — systems/r1/r1_gmband_core.ms (the new R1 engine's
AUDIT.md:438:cannot be [1] — guard against impossible verdicts) before its verdicts
AUDIT.md:447:system (r1_25chain_core: spurious GB=[1] at three primes; the same
AUDIT.md:476:  - 27 systems/farm/* p65521 partial/core files (max up to 9.3e30),
AUDIT.md:519:   3/5 via other lanes). ordtest_*: runs errored (runs/ordtest_*.err),
AUDIT.md:532:   7_42*_c3_core.p65521 at 5.1MB, 8_28mn32d108_c1_core.p65521 at
AUDIT.md:546:bignum evaluation of every row at 2 random points mod p, original vs
AUDIT.md:569:reduced into [0,p) before it ships.** Checklist per new emitter/file:
AUDIT.md:579:2^63-clamp finding before filing upstream.
AUDIT.md:581:On every box restart/reuse: crontab -l FIRST; remove any deadline/poweroff/lifecycle entries before launching work (two incidents: jc-b poweroff loop, ultramem jc_deadline kill).
SHEET6-R6-REVIEW.md:164:  (p. 41) asserts "p has more than one root" verbatim at non-pole chain
SHEET6-R6-REVIEW.md:280:Required edits to SHEET6-R6.md before any re-bank: fix d_h1@P = 1/7 and
SHEET6-III.md:14:vertex has gcd(κ̄, ν) = 1; a theorem of Def 3.1 + Not 3.4/3.5) and the
SHEET6-III.md:20:the St 9.4 budget, 1 more instance-set by N1); entries **r6 and r9 become
SHEET6-III.md:44:  if and only if p_F has more than one root. Set F ∈ V_a and let ν := ν_F. Then
SHEET6-III.md:68:  exists. By the regularity condition, H ∈ T_a%. Therefore λ_F ≥ 1." (9.8-9.10
SHEET6-III.md:80:  shared support. Hence the lattice generated by the shared exponents is
SHEET6-III.md:110:  non-cancelling coefficient), and the Galois structure gives q = η q̃(η^ν):
SHEET6-III.md:166:resultant |a_ν b_κ − a_κ b_ν|); (K3) no (k, ν_F) with κ̄_F ∈ N, M_F =
SHEET6-III.md:230:  theorem under it) is consistent with all thesis-printed Q-data. Interpretive
SHEET6-III.md:240:  is not a theorem of the thesis's own definitions. E5 was never exercised
SHEET6-III.md:248:- **Theorem-solid vs interpreted**: N1's gcd computation, the common-grid
SHEET6-III.md:272:residue sets are sample-asserted out to 3× the resultant period; every
plan-72-108.md:15:Scale: N(P) contains 61 lattice points, N(Q) 125 → ~186 coefficient unknowns before
plan-72-108.md:16:normalization; bracket support gives ~350–450 bilinear equations. GGV's canonical system
plan-72-108.md:47:### Phase 1 — core library (week 1–2)
plan-72-108.md:56:  normalize the 2–3 dim torus (x,y,D scalings). Small code, hard to get wrong.
plan-72-108.md:58:  d_k ∈ K[y] with valuation degree bounds; impose (D^2)_{-k} = 0, (D^3 + corrections)_{-j} = 0
plan-72-108.md:61:- Regression gate G0 (must pass before touching the open case):
plan-72-108.md:76:  vanishing range (more P_{-k} = 0, Q_{-j} = 0 via Generator B's tower) and re-probe. Dimension
plan-72-108.md:79:  core (target: ≤ ~120 scalar unknowns after substitution + torus + forced-monomial shapes),
plan-72-108.md:84:  elimination order; deeper valuation forcing à la their monomial-root arguments).
plan-72-108.md:86:### Phase 4 — theorem-grade result (week 4+)
plan-72-108.md:93:  on the torus-normalized bilinear formulation; two independent implementations of the
plan-72-108.md:95:- Writeup: theorem (bound 108 → 125) or the live-lead analysis + artifact repo
plan-72-108.md:101:Phase 4 in S1 world: <$200 total. Escalation envelope if S1 fails: $2k–15k (S2) before
SHEET6-A2P-REVIEW.md:43:Verdict: **CONFIRMED**. Read before anything else, as instructed; the
SHEET6-A2P-REVIEW.md:106:  T_a^nearrow, therefore lambda_F >= 1" — verbatim, as quoted); the k
SHEET6-A2P-REVIEW.md:144:  baseline engine trace shows exactly this route (ENTRY (1,4,4,9) --mu=4
SHEET6-A2P-REVIEW.md:178:  where its branch leaves the chain) restores disjointness and is what
SHEET6-A2P-REVIEW.md:208:  correctly; it is effectively one more erratum of the E5/E6 family.
SHEET6-A2P-REVIEW.md:261:  III-kinds; phase 2: 52389 solved, kills 50097 (restored-8.4) + 1373
SHEET6-A2P-REVIEW.md:272:  every child has M = gcd(2nu, 2nu+1) = 1: restored-8.4, the 96%-bucket;
SHEET6-A2P-REVIEW.md:274:  more, 4 > 3 = psi-budget: suffix-DEAD (consistent with A' existing
SHEET6-A2P-REVIEW.md:302:  merges 52389 -> 47970 (kills 46337 restored-8.4 / 745 DEAD / 336 N1),
SHEET6-A2P-REVIEW.md:348:- SHEET6-2POLE (284d847): **CONFIRMED on its mathematical core**
SURPLUS-EXT.md:1:# SURPLUS-EXT: Extending the vertex-gap theorem beyond (k,d2)=(2,2)
SURPLUS-EXT.md:9:  {p0,q0} = {(1,0),(k,1)}; normalized so gap side is Q: p0=(1,0), q0=(k,1).
SURPLUS-EXT.md:23:- Cell labels used in §3: THEOREM-COVERED = (k,d2)=(2,2) gap regime (proved
SURPLUS-EXT.md:24:  theorem, SURPLUS.md); MECHANISM-ABSENT = k<=0 / k=1 (no gap) / d2=1 (no
SURPLUS-EXT.md:29:  system is exactly solved by the surplus-4 variant theorem (§1): torus-
SURPLUS-EXT.md:40:cross-checked against an independent lattice-det enumeration of every block
SURPLUS-EXT.md:73:### 1.2 Torus-emptiness: theorem or sub-regime
SURPLUS-EXT.md:75:THEOREM (surplus-4 variant, inner part; (k,d2) = (2,3), depth-2 block, any
SURPLUS-EXT.md:81:exact theorem.
SURPLUS-EXT.md:83:Proof 1 (resultant; machine-verified, wide phaseC2, exit 0).
SURPLUS-EXT.md:86:a common root iff the resultant vanishes: any common zero has a3 = 0. Then
SURPLUS-EXT.md:114:COMPLETE VARIETY (surplus-4 variant theorem, full form; machine layer
SURPLUS-EXT.md:147:THEOREM (w_P = 4, cell (2,4); char 0, excluded primes within {2,3,5,7}).
SURPLUS-EXT.md:174:CERTIFIED at (k,3) for k = 3, 4, 5 by a uniform two-resultant certificate:
SURPLUS-EXT.md:189:these systems; the resultant certificates replace them.
SURPLUS-EXT.md:217:  reduces to exactly -a3^k (i.e. -a3^k b_q0 a1^{1-k} with units restored).
SURPLUS-EXT.md:220:  top Q-coefficient is -(1/15) a2 a6 — byte-matching the (2,2) theorem's
SURPLUS-EXT.md:258:Step 4 (k = 2 contrast = the theorem's obstruction, re-derived). For k = 2
SURPLUS-EXT.md:274:THEOREM (no near-origin obstruction, k >= 3, d2 = 2, depth-2 block; char 0
SURPLUS-EXT.md:284:    to all k (the TRIVIAL verdict on the outer extra is now a theorem:
SURPLUS-EXT.md:308:(denominators s <= 2k+3, k, m-k-1, a2-chart), as in the (2,2) theorem.
SURPLUS-EXT.md:359:open_8_28_c2: strip, k=2, d=(1,2), wP=2, wQ=3, gap -> THEOREM-COVERED.
SURPLUS-EXT.md:362:- THEOREM-COVERED: 1 row, (8,28)+(11/4,7)+(3,2) — PARTIAL: its strip
SURPLUS-EXT.md:363:  subcase c2 is the proved (2,2) theorem; its sibling subcase c1 is
SURPLUS-EXT.md:391:COUNTS (34 rows): THEOREM-COVERED 1 (partial: 1 of 2 subcases);
SURPLUS-EXT.md:395:Headline: the proved (2,2) theorem covers exactly the open_8_28_c2 corner
SURPLUS-EXT.md:412:  (k,d2) column-ODE solve), wide_W0/W1 (anchor + independent lattice-det
SURPLUS-EXT.md:413:  cross-check), phaseC2 (W2 resultant -3200 a3^7, W3 slices), phaseC2b
SURPLUS-EXT.md:416:  Resultants via exact Sylvester determinants (presultant/pdet).
SURPLUS-EXT.md:422:(2,2) theorem's only confirmed client is open_8_28_c2; no wide-strip
SURPLUS-EXT.md:424:Phase B (§2): k >= 3, d2 = 2 verdict is a THEOREM (log-residue dichotomy:
SURPLUS-EXT.md:427:theorem at (2,3): V(4 leftovers) = {a3=a4=0} n ({a2=0} u {R=0}),
SURPLUS-EXT.md:429:proofs: resultant certificate; squarefree+divisibility). Same at (2,4)
ZHEGLOV-LTEST.md:8:> Suppose g̃ ∈ ℂ[x] is a polynomial with more than one root. Suppose deg_x(g̃)=l̃,
ZHEGLOV-LTEST.md:24:- "more than one root": g̃ built as c·∏(x−r_i)^{m_i} with ≥2 *distinct* rationals
ZHEGLOV-LTEST.md:68:covariance of the ODE (2 distinct roots normalize to {0,1}).
ZHEGLOV-LTEST.md:86:arose (all 640 draws consistent). Reading-sensitivity: "more than one root"
SHEET6-LT-REVIEW.md:19:  Prop 4.2(iii); side theorem printed-tier sound via Cor 6.1)
SHEET6-LT-REVIEW.md:21:  hand, unique; same normalization as L1c — no gauge mismatch)
SHEET6-LT-REVIEW.md:25:- Front 6 (E10, E11): **E10 CONFIRMED** (core; two filing errors fixed
SHEET6-LT-REVIEW.md:30:  f−a tower normalization / gauge; UNSOLVABLE-scope caveat vs R6; x-side +
SHEET6-LT-REVIEW.md:100:  chains. Riemann-Hurwitz-type global excess for g is not in the frame
SHEET6-LT-REVIEW.md:145:  THEOREM (first-step merge in the minimal branch) is the same mechanism
SHEET6-LT-REVIEW.md:167:is in the SAME normalization — no gauge artifact.
SHEET6-LT-REVIEW.md:186:  independent and agree exactly. No normalization mismatch exists to
SHEET6-LT-REVIEW.md:232:### E10 (St 3.15 label swap): **CONFIRMED in core, filing needs two fixes**
SHEET6-LT-REVIEW.md:255:  printed-label casualties are 5.5 (iff), 7.2, 7.3. Core erratum stands;
SHEET6-LT-REVIEW.md:328:layer itself. RECOMMENDED ORDER: run the R6 recursion (the E3-E6
SHEET6-LT-REVIEW.md:329:mechanism one tower level up — paper-only, same shape) BEFORE R1; if R6
SHEET6-LT-REVIEW.md:333:### 7d. Underdetermined ingredients (spec must pin before coding)
SHEET6-LT-REVIEW.md:346:3. SOLVABLE endpoint: define the terminal nonlinear core. Without a
SHEET6-LT-REVIEW.md:349:   deg f" — a real theorem (an L2'-tier structure result) but NOT a
SHEET6-LT-REVIEW.md:350:   candidate pair. With the J-check included in the ≤ 20-var core, a
SHEET6-LT-REVIEW.md:353:   currently unsubstantiated — derive it when pinning the core.
SHEET6-LT-REVIEW.md:357:GO criteria after redesign: (i) tower normalization fixed per 7b (gauge
SHEET6-LT-REVIEW.md:358:a = 0 recommended); (ii) conclusion template written down in advance:
SHEET6-LT-REVIEW.md:361:depth + terminal core outcome; (iii) discrete-choice enumeration in the
SHEET6-LT-REVIEW.md:382:   the side theorem is printed-tier sound. Required edits: strike E11
SHEET6-LT-REVIEW.md:386:   (f−a) tower normalization in §2c-E1/R1 or pin gauge a = 0 (front 7 —
SHEET6-LT-REVIEW.md:389:   pins). Recommended sequencing: (a) close or open the R6 window on
SHEET6-R1-Q2E5.md:19:  "(1,2) branch DIES at its terminal core" verdict is **RETRACTED**;
SHEET6-R1-Q2E5.md:21:  branch SURVIVES its terminal core, mirroring the minimal branch.
SHEET6-R1-Q2E5.md:23:  the two before it (ZZ leaf, Q0 s1F): a constraint transported to the
SHEET6-R1-Q2E5.md:27:- Q2 design (§19): sizing gate honored mechanically; row-subset
SHEET6-R1-Q2E5.md:81:coefficient (SUB-top; free g/f tail data at core tier) equals
SHEET6-R1-Q2E5.md:84:is not a core-level pattern row, and no print statement makes it one.
SHEET6-R1-Q2E5.md:102:  misattributed: rows 87-91 are the (1,2) core's h2-stage (B12-h2-quot)
SHEET6-R1-Q2E5.md:103:  G_m quotient rows — evidence about the h2-stage normalization, i.e.
SHEET6-R1-Q2E5.md:121:- phase_minsat rows (minimal E5, HM restored, x 2^18): coefficients
SHEET6-R1-Q2E5.md:129:to Z) + H12·tH12 - 1 + s1·t12 - 1 (s1 occurs in NO row: its core
SHEET6-R1-Q2E5.md:138:RESTATED (1,2) VERDICT (honest): the §18.2 core-level kill is
SHEET6-R1-Q2E5.md:140:branch SURVIVES its terminal core exactly as the minimal branch does
SHEET6-R1-Q2E5.md:143:retracted rows. The (1,2) branch's honest status: ALIVE at core;
SHEET6-R1-Q2E5.md:158:- SIZING GATE (15.6) audited mechanically BEFORE any build: the
SHEET6-R1-Q2E5.md:176:  SHEET6-R1.md §19.0 BEFORE the runs.
SHEET6-R1-Q2E5.md:187:  regression anchors before any run is trusted (front-5 discipline).
SHEET6-R1-Q2E5.md:202:be checked against its .out size before being read as a verdict).
BOOK-BASH.md:13:on the promoted td=6 record before use (gate PASS in every run).
BOOK-BASH.md:23:11, 13 remain the only fully-excluded degrees (TDU prime theorem on the
BOOK-BASH.md:29:therefore a single object: the residue-A template (a1/a2 = 2±√3,
BOOK-BASH.md:46:| IIa(4,7,1)M4@w2 | κ̄9, (9,7,1/4) | 1: m=4 td12 | **SURVIVES** | T1–T4 exhausted; T1 rigid quartic 128t⁴−448t³+560t²−280t+35; T2: 15 IV classes + 2 OPEN μ=3 III-E5 parametric nodes; T3 W deg 8→3 (five exact cancellations); first coefficient-consistent m=4 Theorem-O escape | n/a (note: only bashed class with OPEN suffix kinds) |
BOOK-BASH.md:89:closable from the printed statement list (Theorem-O escape lν ≡ −1 mod r,
BOOK-BASH.md:125:   nodes at λ ≥ 5) — resolve before any claim of suffix completeness.
BOOK-BASH.md:127:Unbashed classes — next steps per BOOK-ENUM §5: ZCH cells need the
BOOK-BASH.md:151:the PRIME THEOREM excludes single-pole at entry for every prime td,
BOOK-BASH.md:161:| 7 | 0 (prime theorem) | empty (prime-panel shadow; off-axis only) | **YES** |
BOOK-BASH.md:218:7. **Do-not-rebash honored.** td=6/m=2 residue-A was used only as the
LEMMA.md:42:i.e. eq #3 is the **vertex normalization**: x² must be attained at the bottom
LEMMA.md:55:1. **Immediate M2 zeroing (before any elimination).** The sub-vertex keys
LEMMA.md:63:   unit corner coefficient times a nonzero lattice determinant: the far
LEMMA.md:95:**unit·a2²·a6·b3 ∈ I(core)**; since the vertex equation makes b3 a unit,
LEMMA.md:96:a2²·a6 ∈ I(core) — the core variety lies in {a2=0} ∪ {a6=0}, which is
LEMMA.md:99:{−8,−6,−4,−2,2,3,…,16,18,20,22} (lattice determinants det(corner, q)); the
LEMMA.md:105:## 3. Valuation interpretation
LEMMA.md:107:The level function ℓ = 2i+j orders lattice points along the strips; the
LEMMA.md:115:  **corner normalization**: for [P,Q] = x², the valuation of x² selects the
LEMMA.md:130:  corner normalization**. So yes: eq #3's collapse is a recognizable
LEMMA.md:138:with [P,Q] = x^k, N(P) and N(Q) lattice strips of widths ≤ w_P, w_Q along a
LEMMA.md:142:  (i) *(vertex normalization)* x^k sits at the Minkowski vertex p₀+q₀ with
LEMMA.md:152:      P-columns 1 … 2) has one more vanishing bracket coefficient than
LEMMA.md:184:to 0 against the vertex normalization), while reg_9_24_c3 has (q₀)_x = 1
LEMMA.md:191:  near-origin columns; equivalently a2²a6 ∈ I(core). This upgrades AUDIT
LEMMA.md:217:- Erratum §2: the M2 zeroings interleave as 2 before / 1 after the
ops/msolve-issue-draft.md:24:happy to provide more cases.
REDUCE4-CUT-REVIEW.md:20:  "multiplicity exactly γ" as a theorem — and for these families the last
REDUCE4-CUT-REVIEW.md:28:  chains ≤ deg 150 are swept), not a per-family theorem. The
REDUCE4-CUT-REVIEW.md:75:  normalization: fixing 2 corner coefficients + the rhs coefficient to 1
REDUCE4-CUT-REVIEW.md:104:  core_eqs (1964) as the banked record.
REDUCE4-CUT-REVIEW.md:106:  (2,0) is IDENTICALLY zero on these supports — the only y=0 lattice
REDUCE4-CUT-REVIEW.md:189:  no-progress-guard log truncation is worth a one-line fix before the
REDUCE4-CUT-REVIEW.md:199:  \section*, notation shares the theorem counter, algorithm floats do
REDUCE4-CUT-REVIEW.md:203:  (4) is existence-only — "exactly γ" is indeed NOT a theorem there; the
REDUCE4-CUT-REVIEW.md:210:  Definition 2.11 `admisible`). Rider (a) is therefore HALF-APPLIED.
REDUCE4-CUT-REVIEW.md:225:  0.0 s, core_eqs 1964 = banked. Kill re-verified two ways: structurally
REDUCE4-CUT-REVIEW.md:226:  (only y=0 lattice point of either polygon is (0,0) ⇒ coeff((2,0)) of
REDUCE4-CUT-REVIEW.md:255:   6_15 and 8_28mn34 emit all-ψ-normal cases; 12_33mn23d135 reduces with
BOOK-BASH-R2.md:39:  homogeneous branch **iff l/r ∈ ℤ (Wronskian / Laurent-residue
BOOK-BASH-R2.md:72:| I(3,1,3)M3@w2 | κ̄4, (4,2,2/3) | 4: m=3 td9,12,14; m=4 td12 | **DEAD** | T1, r = l (l/r = 1): constant-Wronskian rigidity W(s,p) = 2c̃; p·s″ = p″·s forces s = p for every cubic (kernel 0, residue obstruction −c′p″(aᵢ)/3p′(aᵢ)³ closes all branches) ⟹ W = 0 ⟹ ⊖=0; s = p triply inadmissible | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, incl. fresh symbolic W(s,p) re-derivation over arbitrary cubics) |
BOOK-BASH-R2.md:73:| I(3,1,6)M3@w2 | κ̄3, (3,1,1/3) | 4: m=3 td9,12,14; m=4 td12 | **DEAD** | T1, r \| l (l = 2r): (S/p²)′ = 3c̃/p³, Laurent residues N = 6u²+9uv+6v², pairwise resultants 800 ≠ 0 ⟹ ≥2 residues nonzero always ⟹ c̃=0; residual S = p², q = p³ triply inadmissible; both e0-subvariants closed (l ≤ 4 cap flag retired at l=6) | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, incl. full 19-file panel-scope sweep of systems/book/*.json) |
BOOK-BASH-R2.md:75:| I(4,1,4)M4@w2 | κ̄4, (4,2,1/2) | 1: m=4 td12 | **DEAD** | T1, r = l: Wronskian ladder, pivots (6,10,12,12) force s = p unconditionally ⟹ q = p², 2c = W(p,p) = 0 ⟹ ⊖=0; root-law q-mult 2 at all four roots; residue corroboration (p″ deg 2 < 4 distinct roots) | **YES** — kill_confirmed, 2 votes (NOT REFUTED ×2, fresh independent machine /tmp/i414_review.py + on-page Prop 8.1(iv) check) |
BOOK-BASH-R2.md:145:  pairwise Sylvester resultants all = 800 ≠ 0 over ℤ ⟹ no complex
BOOK-BASH-R2.md:219:theorem at prime td; composite residual 4/16/16/23/71/48 at
BOOK-BASH-R2.md:225:| 7 | 0 (prime theorem) | empty | **YES** |
BOOK-BASH-R2.md:269:each reduced to residue-A alone (td=9 was 8 cells before round 2);
BOOK-BASH-R2.md:278:instances at once, UNRUN); (iii) resolution of IIa(4,7,1)'s 2 OPEN
MATHIEU-REVIEW.md:4:Scope: Theorem A (rigidity, all weights), Lemma B (block ⟺ ODE), the
MATHIEU-REVIEW.md:12:(two scope sharpenings). Overall: **THEOREM A IS A REAL PROOF.** The
MATHIEU-REVIEW.md:18:## 1. Theorem A itself
MATHIEU-REVIEW.md:21:Independent re-derivation (from scratch, before re-reading §5.1; my
MATHIEU-REVIEW.md:38:A(0) = 0 or lc(A) pathological — the theorem nowhere uses A(0) = 1 (the
MATHIEU-REVIEW.md:39:normalization lives in Lemma B, not here); w-coefficient edge — w ≥ 1
MATHIEU-REVIEW.md:45:(c) the c ≠ 0 normalization: RIGHT, and it cannot degenerate on a
MATHIEU-REVIEW.md:46:subvariety. In the unnormalized block gauge the ODE right side is
MATHIEU-REVIEW.md:61:strengthens the theorem as requested.
MATHIEU-REVIEW.md:91:  conventions (w0/W1 lattice cross-check re-run, exit 0) and against
MATHIEU-REVIEW.md:92:  LEMMA.md's (2,2) instance (−a3²b3/a1 ↔ normalized −a3²).
MATHIEU-REVIEW.md:99:- Gauge/normalization matching: units a_{p0} = b_{q0} = 1 as in
MATHIEU-REVIEW.md:103:  (Theorem A's weight w vs the stratum weight w = d2·i − j) — cosmetic,
MATHIEU-REVIEW.md:121:the r_i — cosmetic). Circularity check: Theorem A's proof consumes ONLY
MATHIEU-REVIEW.md:125:per-power Remark after the Bridge Theorem is also correct: Corollary E
MATHIEU-REVIEW.md:160:therefore stands; its honest dependency note is now discharged by this
MATHIEU-REVIEW.md:164:## 5. Machine checks M1–M5: theorem vs instances
MATHIEU-REVIEW.md:179:gold-standard step (recommended, not required): the planned Lean
MATHIEU-REVIEW.md:182:third algebraic path (no sympy on this machine; the repo's resultant
MATHIEU-REVIEW.md:188:UPGRADES (if/now that Theorem A stands):
MATHIEU-REVIEW.md:189:- paper1: conj:R (§functional) becomes a theorem for all k, d2 ≥ 2
MATHIEU-REVIEW.md:192:  corollaries of Lemma B + Theorem A + the §4b closed form; the
MATHIEU-REVIEW.md:202:  theorem-covered cell at depth 2; the scope map's cell table collapses
MATHIEU-REVIEW.md:206:  citation instead of a cell table; SURPLUS-EXT's per-cell resultant
MATHIEU-REVIEW.md:208:- Depth ≥ 3 (attackable, NOT closed): Theorem A is weight-uniform
MATHIEU-REVIEW.md:220:unneeded). Theorem A closes the depth-2 rigidity question — it does not
MATHIEU-REVIEW.md:228:2. Symbol collision: Theorem A's weight w vs LEMMA/SURPLUS's stratum
MATHIEU-REVIEW.md:230:3. Bridge Theorem (b): the μ_i live over the splitting field of A;
MATHIEU-REVIEW.md:233:confidence labels; nothing in Corollaries C/D depends on it — Theorem A
MATHIEU-REVIEW.md:237:Theorem A is a correct, complete, 15-line proof; Lemma B's block ⟺ ODE
MATHIEU-REVIEW.md:243:verified. The rigidity half of conj:R is a theorem. Recommend: absorb
MATHIEU-REVIEW.md:244:into paper1 (with nits 1–2), keep the resultant certificates as
MATHIEU-REVIEW.md:252:  Theorem A sweep w ≤ 6, δ ≤ 5, adversarial A, kernel = span{A^w};
RESIDUE.md:9:cascade, scope map), LEMMA.md §3 (tower/valuation reading), paper1/main.tex
RESIDUE.md:45:  (2,2): -(4/20) a2^2 b4        = -(1/5) a2^2 a6      [= repo theorem]
RESIDUE.md:90:CANDIDATE (b1, 1-variable residue; the core formula). With G := 2BC'-kB'C
RESIDUE.md:95:CANDIDATE (b2, residue theorem / CT at infinity): the only poles of
RESIDUE.md:103:and Res_{y0} = -Res_infty (residue theorem on P^1; the CT-at-infinity
RESIDUE.md:111:## 4. Interpretation (c): Koszul / syzygy obstruction
RESIDUE.md:123:provable, so this step is a general theorem, not per-cell). Findings:
RESIDUE.md:127:EXACTLY mu(G) = 0, one residue condition. This is the precise syzygy
RESIDUE.md:133:## 4b. DERIVED (paper calc, to machine-verify): uniform outer theorem
RESIDUE.md:155:THEOREM for all k >= 2, d2 >= 2 at depth 2, machine-verified at 11
RESIDUE.md:175:dy/A^{k+1} at roots of A vanish AND the valuation normalization holds;
RESIDUE.md:177:sum-of-residues) but fail the valuation — explaining exactly why the
RESIDUE.md:179:divisibility). Not closed here; honest status: open as before.
RESIDUE.md:181:(k,d2), k,d2 >= 2, depth 2 — no more per-cell certificates; empty-sum
RESIDUE.md:182:rule k+2 > 2d2 <=> no obstruction (k>=3,d2=2 theorem is its shadow).
RESIDUE.md:196:    at-infinity form via the residue theorem — the alternating-binomial
RESIDUE.md:203:    the block window (syzygy/Koszul reading), which is what makes the
RESIDUE.md:206:per-cell "outer identity" into a uniform closed-form theorem
SHEET6-R1-25LOCUS.md:1:# SHEET6-R1-25LOCUS — solution locus of the (2,5)-chain R1 core
SHEET6-R1-25LOCUS.md:3:Input: runs/r1/r1_25chain_core.out (reduced GB, char 0, 487 elements,
SHEET6-R1-25LOCUS.md:5:55 s). System: systems/r1/r1_25chain_core.ms — 44 eqs = 7 radical + 37
SHEET6-R1-25LOCUS.md:67:- Run A (/tmp/r1_25_ndA.ms): the 44 core eqs + Rabinowitsch rows
SHEET6-R1-25LOCUS.md:98:CORRUPTS the system: r1_25chain_core at p = 105337, 105673, 999999937
SHEET6-R1-25LOCUS.md:100:pre-reduced into [0,p) returns a 487-element GB whose normalized
SHEET6-R1-25LOCUS.md:107:Corollary: char-0 nonemptiness of the (2,5) core is corroborated at an
SHEET6-R1-25LOCUS.md:121:systems/r1/r1_25chain_core.ms mod 105337** (independent parser):
SHEET6-R1-25LOCUS.md:136:## 5. Deferred-row evaluation at the point
SHEET6-R1-25LOCUS.md:140:variables beyond the core's 29** (slot 10: +8, slot 12: +34, slot 14:
SHEET6-R1-25LOCUS.md:141:+44, slot 16: +54, slot 18: +80, slot 20: +90), plus ~39 more f-side
SHEET6-R1-25LOCUS.md:143:are therefore NOT functions on the core locus: at a core point they
SHEET6-R1-25LOCUS.md:148:specialize every xWG.pkl entry (core 29 + radicals pinned; interior
SHEET6-R1-25LOCUS.md:160:point — the pipeline reproduces the banked core rows exactly.
SHEET6-R1-25LOCUS.md:175:the core locus: they are genuinely discriminating. (Both fiber tests
SHEET6-R1-25LOCUS.md:184:1. **The (2,5)-chain core locus is REAL, not a degenerate artifact.**
SHEET6-R1-25LOCUS.md:193:   the 25-row core (all 37 emitted rows) is satisfiable
SHEET6-R1-25LOCUS.md:195:   the core level.
SHEET6-R1-25LOCUS.md:198:   hangs exactly there.** At two independent nondegenerate core
SHEET6-R1-25LOCUS.md:201:   So V(core) is NOT the surviving locus: the true target is the
SHEET6-R1-25LOCUS.md:202:   proper closed subvariety V* = proj(V(core + 12 deferred families)),
SHEET6-R1-25LOCUS.md:203:   which excludes the generic core point. V* may still be nonempty
SHEET6-R1-25LOCUS.md:212:   msolve on core + r<=10 rows returns [1] (char 0 or 2 good primes,
dist/ZENODO-METADATA.md:13:- **Keywords:** Jacobian conjecture; Newton polygon; strip pairs; vertex-gap obstruction; computer-assisted proof; Lean; mathlib; exact rational arithmetic; resultant certificates
dist/ZENODO-METADATA.md:19:The bundle contains every certificate the paper's unconditional theorems rest
dist/ZENODO-METADATA.md:23:resultant certificates at (3,3), (4,3), (5,3) (exponents (15,12), (26,34),
dist/ZENODO-METADATA.md:25:impossibility theorem; (3) a full-pipeline replay of the (8,28) worked
DC2-REVIEW.md:4:`cases/dc2_deg3.py`. Verdicts: CONFIRMED (survives attack) / REFUTED /
DC2-REVIEW.md:7:Poisson bracket, own Jacobian/syzygy linear algebra, own seeds/points);
DC2-REVIEW.md:34:"quantum has 6 more equations" is inherent, and the doc's rank
DC2-REVIEW.md:122:## Front 2 — Syzygy counts (414 cl / rank 410, exactly 4 Jacobi syzygies;
DC2-REVIEW.md:132:  touching the w-λ columns, so every syzygy is supported on the deg-1
DC2-REVIEW.md:136:- WHY they are Jacobi: reviewer built the predicted syzygy from scratch —
DC2-REVIEW.md:179:- Read the code: `stage_gate` **re-derives**, it does not compare stored
DC2-REVIEW.md:187:  PASS, 0.2 s (the "~11 s" folklore figure is stale — gate alone is 0.2 s).
DC2-REVIEW.md:265:unipotent normalization pointwise-only at D=3 (§6.7.5 — genuinely
SECTION4-AUTOMATION.md:15:- **GGV1** = arXiv:1401.1784 (Dec-2015 arXiv version; §7 = "More conditions on B",
SECTION4-AUTOMATION.md:22:  `casos imposibles`: ℘(n′,n′−1) ∉ PLLC), last-possible-corner machinery.
SECTION4-AUTOMATION.md:60:5. TAIL RESOLUTION (only if a residual vertex with unknown following edge
SECTION4-AUTOMATION.md:74:The bracket exponent is thus pure lattice data, known before any branching.
SECTION4-AUTOMATION.md:76:**Why 4.4 has no tail-resolution stage:** its single cut collapses the edge
SECTION4-AUTOMATION.md:116:lists of lattice polygons in ℤ² (Laurent allowed: x-exponents may be negative;
SECTION4-AUTOMATION.md:118:stores one 1/m-polygon S with SuppP = m·S, SuppQ = n·S (they individuate only at
SECTION4-AUTOMATION.md:119:the tail-resolution step). Consts = symbolic scalars (λ, α_i, …) each carrying
SECTION4-AUTOMATION.md:131:  edge of direction (ρ,σ) only when ρ = 1 after normalization, i.e. (1,−K)
SECTION4-AUTOMATION.md:150:provisional corner (i_st − K·d, 0), refined later by tail resolution.
SECTION4-AUTOMATION.md:155:   [P,Q] ∈ K^× still (i.e. before T-final); v-ratios m/n at (1,1),(0,1) (resp.
SECTION4-AUTOMATION.md:161:   en(R) = (1/(qm))·en of that edge must be a LATTICE point, and R's support
SECTION4-AUTOMATION.md:182:R7 **PLLC checks (GGV2 `cota`, `casos imposibles`; GGV2 Prop 3.29 / Rem 3.31
SECTION4-AUTOMATION.md:191:R9 **Tail resolution (GGV1 Prop 8.2 + GGV22's opposite-vertex filter).**
SECTION4-AUTOMATION.md:193:   (i) Enumerate opposite-vertex candidates (a″,b″) on the lattice strip below
SECTION4-AUTOMATION.md:211:algorithm explores the whole tree; a leaf = emitted case or contradiction):
SECTION4-AUTOMATION.md:236:  the lattice-point count of the current 1/m-polygon (edge slots consumed:
SECTION4-AUTOMATION.md:259:G3 **Step invariants** (checked after every op): polygon convexity & lattice
SECTION4-AUTOMATION.md:260:   integrality of mandated corners; en(R) lattice test in R1; v_{ρ,σ}-consistency
SECTION4-AUTOMATION.md:275:The good news (established by the traces): for §4-class families the loop never
SECTION4-AUTOMATION.md:304:| Lattice/state core (Laurent polygons, v/st/en/dir, T-ops) | 1–2 d | partly in `lib/jc.py` |
SECTION4-AUTOMATION.md:330:produces byte-identical output (34-row before/after diff, 0 regressions),
SECTION4-AUTOMATION.md:346:therefore support-exact REGARDLESS of how zdeg−γ splits among the other
SECTION4-AUTOMATION.md:390:ψ_j as before or is covered by one of the two direct emissions; identical
SECTION4-AUTOMATION.md:414:Audit trail: 34-row before/after diff — the 22 previously-non-stuck rows
SECTION4-AUTOMATION.md:430:| family | (m,n) | deg | cases | ψ-normal (rhs x^k) | pre-ψ (rhs x^0) |
SECTION4-AUTOMATION.md:480:runs/stuck7_verdicts/ (verdicts need authentication before banking:
LEMMA-REVIEW.md:4:(claim survives attack) / REFUTED / WEAKENED. All reviewer code was written
LEMMA-REVIEW.md:5:from scratch where independence is claimed (own hull/lattice/det-formula
LEMMA-REVIEW.md:29:  There are 3 zeroings total: b1, b2 strictly *before* any elimination
LEMMA-REVIEW.md:35:Independent recomputation (own monotone-chain hull, own half-plane lattice
LEMMA-REVIEW.md:41:- (3,1) has **exactly one** decomposition over the full lattice-point sets
LEMMA-REVIEW.md:74:  coefficient times a nonzero lattice determinant" holds.
LEMMA-REVIEW.md:88:  cascade-stage zeros vanish; replayed form == direct evaluation for all 92
LEMMA-REVIEW.md:176:data before any general statement — do the surplus derivation first; the
MATHIEU.md:4:functional R_{k,d2} (RESIDUE.md), and an attack on the rigidity half of
MATHIEU.md:24:3. ATTACK (§5): the DvdK MECHANISM — the valuation-at-infinity /
MATHIEU.md:27:   coordinate-free proof (Theorem A) that A C′ − k A′ C = 1 with A, C
MATHIEU.md:29:   Consequently (with RESIDUE.md §4b's uniform outer theorem) conj:R
MATHIEU.md:31:   (3,4), (4,4), (5,4) and all d2 ≥ 5.  Status: PROVED + PROMOTED (2026-08-12, MATHIEU-REVIEW.md: all six fronts CONFIRMED; Theorem A real; conj:R closes at every cell k,d2>=2 char 0). Original status: new proof, this file;
MATHIEU.md:33:   before the paper absorbs it (repo practice: LEMMA-REVIEW pattern).
MATHIEU.md:53:### 1.2 The Duistermaat–van der Kallen theorem
MATHIEU.md:55:THEOREM (DvdK, Indag. Math. 9 (1998)).  Let 𝒜 = C[x_1^{±1},…,x_n^{±1}]
MATHIEU.md:67:The mechanism of the 1-variable proof is a VALUATION argument at the two
MATHIEU.md:71:is what we transport in §5.  (Confidence: statement of the theorem HIGH;
MATHIEU.md:75:### 1.3 Ledger: theorem vs conjecture in the MZ literature
MATHIEU.md:80:- DvdK theorem, all n (above).  [HIGH]
MATHIEU.md:106:  to me; not usable as a theorem.  [MEDIUM]
MATHIEU.md:125:j < d2).  So on the binomial locus the torus normalization is exact and
MATHIEU.md:156:## 3. The bridge theorem
MATHIEU.md:169:cross-verified against the independent lattice-determinant enumeration
MATHIEU.md:188:BRIDGE THEOREM.  Fix k ≥ 1 and A with δ = deg A ≥ 2.  Then:
MATHIEU.md:228:deg C = kδ ≤ kd2 by the lc-formula, and can be normalized to zero
MATHIEU.md:244:is the honest reason MZ theorems alone cannot finish: they control
MATHIEU.md:252:  locus (M3).  DvdK applies as a theorem; its conclusion is vacuous for
MATHIEU.md:261:  obstruction: the binomial locus), while for δ ≥ 2 Theorem A says no
MATHIEU.md:275:## 5. The attack: the rigidity half, proved
MATHIEU.md:277:### 5.1 Theorem A
MATHIEU.md:279:THEOREM A (rigidity, all weights).  Let F have characteristic 0, let
MATHIEU.md:309:C = y at a2 = 0, for c = 1), so Theorem A is sharp; and it is exactly
MATHIEU.md:310:the "valuation at infinity" DvdK mechanism: ord_∞ applied to
MATHIEU.md:314:budget.  (The algebraic Steps 1–4 are that valuation argument made
MATHIEU.md:315:elementary; no Riemann–Hurwitz needed.)
MATHIEU.md:327:A C′ − k A′ C = 1; Theorem A (w = k ≥ 2 ≥ 1) forces deg A ≤ 1.  ∎
MATHIEU.md:329:This settles, structurally and uniformly, the cells proved before by
MATHIEU.md:331:A | N(A) divisibility), (3,3),(4,3),(5,3) (resultant certificates
MATHIEU.md:339:Theorem A proves it could never hold (Corollary E).
MATHIEU.md:344:On the binomial locus, RESIDUE.md §4b (uniform outer theorem, chain
MATHIEU.md:353:and Theorem A.
MATHIEU.md:367:A C′ − (m−1) A′ C = A^m g′ = 1.  Theorem A (w = m−1 ≥ 1) forces
MATHIEU.md:373:perfect powers pass the residue test but fail the valuation: the
MATHIEU.md:380:Theorem A as stated uses char 0 twice: (d − wδ) ≠ 0 in Step 1/2/4, and
MATHIEU.md:413:SC1 for δ ≥ 2 would be the first Mathieu theorem on a curve with more
MATHIEU.md:416:(Theorem A stands independently).
MATHIEU.md:435:- M4 Theorem A's two computational identities, SYMBOLICALLY (generic A
MATHIEU.md:439:  two identities verified, the remaining content of Theorem A's proof
MATHIEU.md:448:## 8. Consequences and next steps
MATHIEU.md:450:For conj:R: the conjecture's rigidity half is a theorem (Corollary C),
MATHIEU.md:456:certificates upgrade from certified computation to structural theorem;
MATHIEU.md:462:one theorem instead of a cell table.  Unchanged scope limits: strip
MATHIEU.md:464:depth ≥ 3 untouched — though Theorem A is already the homogeneous
MATHIEU.md:467:attackable by the same two lemmas.
MATHIEU.md:469:Recommended next steps, in order: (1) adversarial review of Lemma B +
MATHIEU.md:470:Theorem A (the proof is 15 lines; the risk concentrates in Lemma B's
MATHIEU.md:473:thm:k3 become corollaries; §functional's conjecture becomes a theorem
MATHIEU.md:474:modulo §4b's write-up); (3) Lean formalization of Theorem A (kernel +
SHEET6-REVIEW.md:73:  "Therefore l in N. This, however contradicts Theorem 6.1 [l_f < k_f]") —
SHEET6-REVIEW.md:122:  campaign's own qualification (td<=5 safe via Orevkov/Domrina/Zoladek
SHEET6-REVIEW.md:192:  the stored THESIS_TABLE — stored values appear only as the comparison
SHEET6-REVIEW.md:217:§9 kills only row 4 of the five Lambda<=5 rows — the thesis's td>=6 theorem
RECON.md:7:1. **We are not alone on (72,108) — but nobody has landed it properly.** Two public exclusion claims: Helali (07-21, Zenodo 21479814 + GitHub: 89 MB char-0 unit-ideal certificates, conditional on GGHV Prop 4.3, AI-built, unaudited, no arXiv) and Suzuki (07-22, Zenodo 21483636: dessins/Bézout/weighted-Macaulay exclusion of the (8,28) case, 5 MB verification pack), plus an artifact-less echo (Qiu, 08-01). No peer review, no expert endorsement, no GGV contact; openconjectures.org still shows the pre-125 status. A rigorously audited certificate (our lane) can still be the authoritative settlement — and their transcriptions are cross-check material for our Generator A audit.
RECON.md:8:2. **Plane case remains open with no credible resolution attempt:** Tao (07-21, no follow-up) confirms JC2 open; the only "proof" claim (collision-ideals + Lean, @chloeallegra228) is explicitly conditional on an unproven `PlanarNoHiddenInertia` axiom; several documented AI attacks on a 2D counterexample failed (one claims the failure is provable).
RECON.md:9:3. **New structural results we can use:** Shaska 2607.20210v2 (07-25) — in dim 2, graded-equivariant Keller maps are automorphisms for *every* weight sign pattern; Wilson 2607.23887 (07-26) — two-variable Gaussian Moments Conjecture *proved* by Newton-polygon **face isolation**; Speyer-thread Picard obstruction ("only d=3 threads the needle"); Suzuki's 5-class dessin classification of the (8,28) top edge.
RECON.md:11:5. **Counterexample mechanisms multiply in dim ≥ 3, all silent on dim 2:** Gao's tangent-sweep (2608.00222, all dims > 2), the 98-map weighted-lift atlas (jacobianfun.org), degree-3 in C^19, Hessian(5)/Mathieu-SU(2)/GMC(n≥3) all fell — while every two-variable analog (GMC(2), graded-equivariant JC2) was *proved*. No bounties anywhere; UnsolvedMath = ULAM AI benchmark repo (no JC coordination); the Leiden Declaration (~3.4k signatories) sets publishing norms we should follow (AI disclosure, peer review before press).
RECON.md:18:- Tao: no X account activity found; blog post 2026-07-21 (see §4), no follow-up since. Akhil Mathew: no original X posts; quoted in Fortune re "unsettling" pace + a "Leiden Declaration" on AI norms in math circulating (@v_shakthi 2026-08-02). Will Sawin: nothing substantive found. [CONTEXT]
RECON.md:21:- 2026-07-21 — @HelaliBillel — https://x.com/HelaliBillel/status/2079660726201856148 and .../2079660728907129102 — **Claims the (72,108)+(108,72) GGV-Horruitiner residual pairs are EXCLUDED** by exact characteristic-zero certificates (unit-ideal identities; "hard certificate ~89.1 MB over a degree-5 field") ⇒ claims max(deg P,deg Q) ≥ 125 for any planar counterexample. [COMPETES-WITH-US — same target, claims completion 4 days before our lane-2 runs]
RECON.md:23:- 2026-08-01 — @QiuGuangwww — https://x.com/QiuGuangwww/status/2083602146508034380 (+ .../2083605448650068227) — claims an **independent second exclusion of (72,108)** (with ChatGPT+Grok): five degree-21 three-point covers, A_21 monodromy, exact Bézout certificates over F_101, "good reduction to char 0"; frames as conditional, complementary to Helali. [COMPETES-WITH-US — but mod-p + monodromy route, char-0 step unclear]
RECON.md:26:### 1c. Plane-case attacks (AI-assisted and other)
RECON.md:27:- 2026-07-27/28 — @chloeallegra228 — .../2081612747465224648, .../2081877245577121991, .../2081941758661836921 — paper + Lean formalization of "collision ideals / off-diagonal sheets, JC as obstruction vanishing"; then **self-announced AI-assisted ideal-theoretic proof of JC(2)** — community reception unclear, no expert endorsement observed. [COMPETES-WITH-US if real; likely unvetted]
RECON.md:28:- 2026-07-23 — @ClaudeDotDo — .../2080176410723848606 — commitment hashes for a claimed "sterility theorem" for plane-JC line configurations (cross-model audits claimed, content hidden). [CONTEXT — unverifiable]
RECON.md:30:- 2026-07-21 — @sugarbets_ — .../2079582004522152400 — probing whether the n=3 mechanism descends to n=2 via a conductor/valuation obstruction. [USABLE-BY-US — valuation-flavored, same terrain as GGV (rho,sigma)]
RECON.md:39:- 2026-07-20 — @davikrehalt — .../2079175065695035442 — clean geometric reformulation: P^1×Sym^2(P^1) → Sym^3(P^1) forget-a-root map, minus ramification and a well-chosen hyperplane. 2026-07-22 — @eigenstate (Rezchikov) — .../2080079977966403681 — 2D-picture derivation (three lines + two parabolas), rezchikov.me visualization. [USABLE-BY-US — sharpest statements of *why* dim 3 works; the failure mode of these constructions in dim 2 is the informative part]
RECON.md:48:- **No X account/community named "UnsolvedMath" found.** Nearest live tracker: **@openconjectures** (openconjectures.org) — "public registry of open mathematical conjectures, ranked for renown and attackability. Posting when one falls." Tracks planar JC as open (renown 5/5, attackability 2/5), registry id ~jacobian-n2-1939; no bounties observed. [CONTEXT — see §3]
RECON.md:52:- **Suzuki (Eiki Suzuki, ORCID 0009-0002-0556-4967):** Zenodo **10.5281/zenodo.21483636** v1.1.4, pub. 2026-07-22 — "Exclusion of the (8,28) Newton-Polygon Case in the Plane Jacobian Conjecture" (EN+JA PDFs + 5.1 MB verification ZIP with negative controls). **This is exactly our A0=(8,28) family.** Method is structural, not brute-force: **5 dessin-d'enfants classes for the top-edge equation**, Bézout identity via exact elimination over a degree-5 number field, weighted Macaulay 261×261 minor with det ≡ 21 mod 23. Claims both alternatives excluded ⇒ bound 108 → 125. [COMPETES-WITH-US and USABLE-BY-US — small certificates, and the 5-class top-edge classification is directly relevant to our leading-tower combinatorics]
RECON.md:53:- **Qiu (@QiuGuangwww):** posts end "Paper and Code:" but **no recoverable link**; "five degree-21 three-point covers, A_21 monodromy" strongly echoes Suzuki's 5 dessin classes — possibly derivative. ~43 followers, zero engagement. [CONTEXT — discount until artifacts appear]
RECON.md:55:- **Leiden Declaration** (leidendeclaration.ai; Zenodo 20302944; IMU letter 2026-06): Lorentz Center workshop product on AI-in-math norms — human responsibility, tool disclosure, peer review over press-release timelines; ~3,400 signatories, Tao/Scholze/Dijkgraaf featured; Gowers declined and blogged why (gowers.wordpress.com 2026-07-26). [CONTEXT — shapes how we should publish]
RECON.md:65:- 2026-07-22 — arXiv:2607.20597v1 (math.AC), Jelonek, "On mappings with Jacobian one" — component structure: automorphisms vs. components generically containing counterexamples. [details TBD]
RECON.md:73:- **Jelonek 2607.20597** (07-22): generic elements of suitable components of Jacobian-1 maps are counterexamples for n ≥ 3, d ≥ 6 — post-refutation "failure is generic" structure theorem. [CONTEXT]
RECON.md:85:- **The de-facto live tracker is openconjectures.org** (@openconjectures): entry `jacobian-n2-1939` = **Open**, renown 5/5, attackability 2/5, "surviving case after the July 2026 refutation of JC(n), n≥3"; caveats that tracking may lag; **no degree-bound update to 125 recorded; no bounties; no coordination infrastructure.** Tao-blog commenters use it as the reference status page. [CONTEXT — if our certificate lands, this is where status flips first]
RECON.md:89:- **Speyer / Secret Blogging Seminar (2026-07-20)** (sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/): notes the seed map's homogeneity under deg(x,y,z)=(−1,1,2); discriminants factor as squares; sheets "escape to infinity together" over Δ=0. Comment thread is the sharpest public structure discussion: **Will Sawin** (07-20) gives the P^1×Sym^2(P^1)→Sym^3(P^1) formulation with X ≅ A^3 as iterated A^1-bundle; **"Skooi"** (07-21) proves the direct generalization π: P^1×P^(d−1)→P^d **fails for d ≥ 4 by a Picard/class-group obstruction (discriminant class Z/(d−2)) — "only d=3 threads the needle"**; Lior Silberman raises char-2 (answered by 2607.20968). [USABLE-BY-US — the obstruction calculus for why the mechanism needs d=3 is the best current hint at what a dim-2 mechanism must evade]
RECON.md:91:- **GGV group (Guccione ×2 / Valqui, + Horruitiner):** **no public response to the counterexample and no new JC preprint** — latest arXiv item is math.GR (2606.05520, June 2026); latest JC-adjacent is Ramirez–Valqui **2506.05697** (June 2025), "The Groebner basis and solution set of a polynomial system related to the Jacobian conjecture" [USABLE-BY-US — closest published precedent for our Gröbner/msolve formulation; check their normalizations against Generator A]. Valqui's PUCP CRIS page (cris.pucp.edu.pe) shows nothing newer. Neither Helali nor Suzuki appears to have contacted them publicly. [CONTEXT]
RECON.md:97:2. **Immediate technical to-dos:** (i) diff Helali's transcription (2010 eqs / 1925 unknowns, s=±c branch split, h=0 forcing) and Suzuki's formulation against our Generator A systems (open_8_28_c1: 187 vars/303 eqs; c2: 73/93) — agreement across three independent transcriptions would be a strong exhaustiveness argument; disagreement is a red flag we must resolve *before* trusting any verdict, ours included. (ii) Download both verification packs (Zenodo 21479814, 21483636) and replay them. (iii) Read Suzuki's 5-dessin top-edge classification — if correct it may shortcut our lane-2 msolve grind (structural kill vs. F4). (iv) Mine Wilson's face-isolation lemmas and Shaska's dim-2 equivariant theorem for reusable polygon-face arguments; both align with the GGV (rho,sigma) grading we already planned to exploit.
RECON.md:99:4. **Write-up strategy:** follow Leiden norms (full AI disclosure, artifacts + independent checker, contact GGV before public claim — they are silent so far and are the natural validators; Ramirez–Valqui 2506.05697 shows Valqui already runs Gröbner pipelines and can referee this). Cite Helali/Suzuki as independent concurrent computations regardless of audit outcome.
RECON.md:100:5. **Program-level watch items:** DC(2) activity (a proof would subsume JC2; @octonion's lift attempts), any Alpöge PDF (promised, not yet posted), a Shaska v3 or responses, Gao-mechanism dim-2 descent attempts (@sugarbets_'s valuation obstruction probe), and the (75,125) frontier Helali has already opened — if the 125 bound stands, that pair is the next campaign target and we should pre-emit its systems.
RECON.md:115:4. **125 bound NOT absorbed.** openconjectures.org `jacobian-n2-1939` still Open, renown 5 / attack 2, no degree bound shown; @openconjectures' 08-01 kill-feed post (.../2083614487790354768) has no JC update — last explicit n=2 statement remains "true up to degree 100" (07-25). [CONTEXT — authority slot still open]
RECON.md:116:5. **NEW third (72,108) competitor, missed by the 08-04 snapshot:** Felipe Santibañez-Leal, Zenodo **21740213** — "A planar program for the two-variable JC: theorem ladder, staircase transport, and machine certificates at the (72,108) frontier" ("Paper B of 3"; cites GGHV 2204.14178 Prop 4.3; 33×33 core H(A,B,C), direction K_(2,8), 136,500 tensor-grid controls over 30 primes + CRT). **27 versions v0.09 (07-24) → v0.32 (08-01), then dormant — no in-window updates; does NOT claim exclusion.** Author is a mass-output AI-paper account (36 Zenodo records in ~10 days across unrelated fields: Huneke–Wiegand, Shub–Smale tau, ECG physics…). [COMPETES — third independent transcription = extra cross-check material for §Implications 2(i); credibility low]
RECON.md:123:8. **Kistner–Shaska 2608.02863** (math.AG, 08-03; bot-tweeted 08-05): "Orbits and Fields of Definition for Graded Keller Maps" — sequel to §2's Shaska: populates hyperbolic-weight strata K(3,(1,−1,−1)) (cyclic cones, every composite generic degree ≥ 6; 33-sheeted member over Q) and K(3,(1,−p,−p)); geometric monodromy always full alternating/symmetric (solvable only at generic degree 3); genuine positive-dimensional moduli at degree 12. Dim 3 only — sharpens the dim-2/dim-3 dichotomy of §2. [USABLE — negative space + full-monodromy result to test Qiu-style A_N claims against]
RECON.md:133:14. Zenodo noise, in-window/backfill: Santana 21826515 (08-06) "JC and the Arrow of Time" (physics crank); Reed 21542914 (07-25, missed by snapshot) claims "Formal Resolution of the Two-Dimensional JC in Lean 4" via graded differential operators + Jung–van der Kulk — unvetted, zero community visibility, near-certainly wrong (JvdK-flavored circularity); Leal Ramirez 21538118 (07-24) — "nearly free divisor" homological analysis of the dim-3 map. [CONTEXT — noise tier, logged for completeness]
RECON.md:137:- Competitive pressure DROPPED in-window (Helali stalled, Qiu vaporware, Suzuki static, registry un-absorbed) while our differentiators (audit, arXiv-grade writeup, GGV contact) remain unclaimed — §Implications 1 stands, with more slack than feared.
RECON.md:138:- New to-do ahead of any publication: (a) stress-test the vertex-gap argument against Mondello's char-2 plane map (item 9); (b) add Santibañez-Leal v0.32 to the three-way transcription diff (item 5); (c) mine Kistner–Shaska's full-monodromy theorem when auditing any A_N-monodromy exclusion claim (item 8).
RECON.md:146:of td>=6 exclusion as printed; td<=5 remains safe via Orevkov/Domrina-Orevkov/
RECON.md:156:- arXiv, new in window: **2608.05392** (subm. 08-05; Castañeda–Honorato–Valenzuela-Henríquez) — weak Markus–Yamabe FAILS for n≥14: a "chain realization" theorem turns any Keller map into a Hurwitz vector field whose singularities biject with a prescribed fiber; applied to the JC counterexample gives a deg-7 field on R^14 with 3 singularities (also deg-3 on R^18); dims 3–13 open; zero dim-2 content. [VERIFIED abstract; CONTEXT — fallout continues, plane untouched]
RECON.md:160:- No findings. X: zero hits on topological/geometric degree of Jacobian pairs, "sheet six", Sigray/Orevkov/Domrina/Żołądek, Eggers–Wall trees (only false positives: Polish "żołądek", Dave Eggers). Web + arXiv likewise. Our td=6 campaign and the Sigray-incompleteness finding (Delta 08-07) remain unclaimed territory. [CLEAR]
RECON.md:163:- All known competitors frozen: Helali Zenodo v1.0.1 (GitHub push still 07-21, 1 star); Suzuki v1.1.4; Santibañez-Leal v0.32 (08-01); Qiu artifact-less and silent. No deg>125 verdicts, no (75,125) movement, no trace of anyone else sweeping ≤150. [VERIFIED via Zenodo/GitHub APIs + grok]
RECON.md:175:### 6. AI-assisted math attacking JC / Dixmier
RECON.md:176:- No findings. No X or web trace of any other automated case-bash / Gröbner / degree-farm / Lean campaign on JC(2) or DC(2); no lab or group announcements; @openconjectures/unsolvedmath/ULAM silent; chloeallegra228 no JC follow-up (collision-ideals still not on arXiv). [CLEAR — ours remains the only visible systematic computational campaign]
RECON.md:180:- New to-dos: (a) fold Ishihara v1.3.0 into the transcription diff — four-way agreement would be a strong exhaustiveness argument; (b) file the msolve parenthesis issue upstream; (c) skim 2608.05392's chain-realization theorem — the Keller-map→vector-field transfer is new machinery worth checking for a dim-2 converse.
lib/FAMILIES.md:7:dependence; exact `int`/`Fraction` lattice arithmetic only.
lib/FAMILIES.md:46:  finalization (R10); pure lattice data, fixed before any branching.
lib/FAMILIES.md:60:   Theorem 2.19 shows a type II.b) corner of a *standard* pair cannot have
xmodel/grok-eval-20260812.md:1:I'll start by reading the campaign documents in the order you specified, then check RECON.md and notes.md so the stress test and new avenues aren't duplicates.Next I’ll pull TEMPLATE §§0–1, the end of notes.md, and RECON.md so the new-avenue list doesn’t repeat what’s already in the record.I’ve got the main theorems. Next I’ll scan the campaign record for already-proposed attacks so the five new avenues don’t repeat them.The program has reduced JC2’s sheet-6/multi-pole side to a handful of rigid templates and proved a real theorem on the strip side. The architecture that would turn those into a proof of JC2 is weaker than the writeups claim.
xmodel/grok-eval-20260812.md:7:Why fragile: it has now survived every *printed* constraint (Theorem O), the full coefficient lift (five independent identities close exactly, including the h2-collapse re-deriving L1c without the ODE), and the classical battery (splice/Seifert identity, Abhyankar–Moh at the poles with **zero slack** \(\operatorname{ord}_t f_y=-39\), Jelonek). Every Groebner “kill” of it has been an artifact (msolve parentheses, \(s_{1F}=0\), unreduced mod-\(p\), vmem-cap). Zero-slack topology plus receding discriminants is the signature of a real formal object, not a near-miss. If it algebraizes, JC2 is false and the exclusion program is hunting a theorem that does not exist.
xmodel/grok-eval-20260812.md:10:Claim (DEPTH §8 + notes): prime-td + Theorem MP + depth-closure + book-bash is a finite JC2 machine.  
xmodel/grok-eval-20260812.md:11:Why fragile: TDU §7 already says the opposite on the single-pole side — composite residual \(4\to 212\) from \(\mathrm{td}=6\) to \(16\), *no* finite list. The book itself is a **superset**: \(P\)-realizability untracked, joins conservative, all-\(\mu_e\ge 2\) mixed merges quarantined (\(m\ge 3\), only possible downstream of a jump), off-axis \(b_i\ge 2\) outside the \(w\)-lemma. The reduction sits on P1 (Prop 8.3 read as Not 9.2 — a sanctioned typo) and H1 (Prop 9.3 case arithmetic), and the latter already drifted once (ZCH 0-edge is case (III), not (II)). One more case-label error reopens cells or silently drops them.
xmodel/grok-eval-20260812.md:15:Why fragile: even a complete kill of all 27 multi-pole instances leaves \(\mathrm{td}=6\) open on the four thesis-forced single-pole classes (entry \(Q=(3,6,5,2,8)\), type \((3,5)\), \(M=b=2\)), and every composite \(\mathrm{td}\) independently blocked by TDU. Those four have not been hit with the T1 Wronskian ladder that just killed 15 multi-pole classes. “Multi-pole book drained” \(\neq\) “\(\mathrm{td}\) excluded.”
xmodel/grok-eval-20260812.md:17:(Theorem A itself is not on this list. The 15-line leading-coefficient argument is solid; what is overstated is its *role* — it closes strip depth-2, not JC2.)
xmodel/grok-eval-20260812.md:19:## 2. New avenues
xmodel/grok-eval-20260812.md:21:Checked against RECON.md and notes.md (including the just-launched Galois / L1-§7.2 / panel-squeeze / classical-on-6 / Weyl battery, the TEMPLATE R1–R6 list, log-BMY, IIa\((3,5,1)\) \(W\)-residual, mixed-merge quarantine-as-scope, SC1, Mondello, face-isolation). These five are not in that record.
xmodel/grok-eval-20260812.md:26:| 2 | **Hurwitz factorization of \(\hat g:\overline{C}\to\mathbb{P}^1\) in \(S_6\)** | Classical battery used RH as a *number*. Existence of an actual degree-6 cover with the pinned local types is a different obstruction; failure kills residue-A independently of Sigray. | From Newton pairs \((7,2)(3,10)(2,5)\) at each pole, compute the local monodromy cycle type on the 6 sheets of \(\hat g\) (poles of order 3). Check whether two such classes, plus the \(x\)-side cluster (\(g\) finite there) and RH-constrained finite ramification, multiply to \(1\) in \(S_6\). |
xmodel/grok-eval-20260812.md:27:| 3 | **\(J\)-jet at \(G_m\) on the 7 dead-stretch coefficients** | Not R1 (symmetric-function polynomiality) and not R5 (global \(J\)). The first non-constant term of \(J(f,g)\) in the \(G_m\)-chart is linear in the on-lattice free coeffs at \(17/21,18/21\) (merge) and \(9/21,12/21,15/21\) (suffix). Two Galois-conjugate poles \(\Rightarrow\) overdetermined. | Expand \(J\) to order \(1/\kappa_{G_m}\) past the pinned tops; set the first two jet coefficients to \(0\). Inconsistency or a pin that breaks \(w_i^4\) (TEMPLATE E5) is a kill. |
xmodel/grok-eval-20260812.md:28:| 4 | **Theorem A on the depth-3 column of the two-pole support** | Connects the two successful lanes, which have been run in parallel. MATHIEU-REVIEW already has the depth-3 column \(2BE'-(k+1)B'E\). Residue-A is *not* a strip; if that column cannot vanish for the pinned leading forms, the genome is not a polynomial pair. | Take the Newton edges \((126,42)\), \((189,63)\) with root pattern \(p_R=S_R(\eta-c_0)^{126}\); extract the \(x^{k+2}\) bracket column; run the leading-coefficient lemma (MATHIEU §5.1 Step 1). |
xmodel/grok-eval-20260812.md:35:Dim-2 keeps proving the statements that are true (GMC(2), Shaska for every weight sign, no graded plane CE). Every known \(n\ge 3\) mechanism dies in the plane (Picard/\(d=3\) needle, no tangent-sweep, no graded escape). Eighty-five years without an example is evidence. Residue-A is the best formal candidate I have seen in this literature, but “passes the printed list” is exactly Theorem O, and an étale non-proper degree-6 endomorphism of \(\mathbb{A}^2\) is the thing JC2 says does not exist — consistency at vertices is cheap compared with algebraizing 126 series.
xmodel/grok-eval-20260812.md:37:**Breakthrough** if it happens: another T1-style *criterion* (item 1, or a uniform kill of IIa\((r,rt-1,1)\), \(t\ge 2\)), or a covering-theoretic kill (item 2) that does not go through Sigray. The unrun IIa\((3,5,1)\) \(W\)-residual (\(\deg 2\) vs demanded \(\le 1\)) is the cheapest already-logged shot; I did not re-propose it.
xmodel/grok-eval-20260812.md:39:**Stall** where the program is already stalling: R1/depth-84/deferred-band descent on residue-A (artifacts, 1.5 TB deaths, discriminants receding). Next: TDU’s growing composite single-pole residual, which no finite book-bash can finish. DC(2) is the strongest *proof* route and is blocked on 2-dimensional Schur/Parshin; it will not be this campaign’s win.
xmodel/grok-eval-20260812.md:41:The honest fork is unchanged since L1: residue-A is either a counterexample or it dies by mathematics that is not in Sigray. Printed-tier is exhausted (Theorem O). Treat the next kill attempt that is *not* a larger Groebner core as the real experiment.
SHEET6-AF3.md:29:Claim (AF3′): for every F ∈ T_a,pole of a normalized counterexample,
SHEET6-AF3.md:116:(row 9; ρ = 1/2). A hypothetical carrier is a normalized counterexample of
SHEET6-AF3.md:177:entry r9 Q=(3,6,5,2,8) of a type-(3,5) normalized counterexample — now
SIGRAY-AUDIT.md:12:| Not 2.3 | 9 | VERIFIED | Normalized counterexample well-defined; the "from now on" reduction is sound via Lem 2.1. |
SIGRAY-AUDIT.md:18:| St 3.2 | 11 | VERIFIED_WITH_NIT | Proof MISSING in thesis and claim nontrivial (false for general series sets); re-derived via Galois-orbit ultrametricity + greedy anchor induction; 400-trial exact confirmation. Typos ("There exits", "THE Puiseux series"). |
SIGRAY-AUDIT.md:37:| St 3.8 | 14 | ERRATUM | NEW. D_{h,F} ∈ Z FALSE under Not 3.5's P-presentation: explicit contact-vertex witness gives D = −1/2 ∉ Z (and ill-defined value 1 vs 2 even when integral). This UPGRADES H5a from coherence-forced convention to printed-statement-forced: only the jump/max κ_F reading makes St 3.8 true; corrected version proved in two lines (lattice argument). Not previously filed against St 3.8. |
SIGRAY-AUDIT.md:39:| Prop 3.1 | 14–15 | VERIFIED_WITH_NIT | Counting identities (*)/(**) re-derived (unramified cover + Hensel + squarefree ⇒ distinct) and machine-checked at κ = 2, 4. Print errors: "c_j x^{-j}" must be c_j x^{-j/κ} (E5/E8-grade typo); proof cites form (4) where (3) is meant; proof terse. |
SIGRAY-AUDIT.md:59:| Prop 4.5 | 22–23 | VERIFIED_WITH_NIT | Proof reconstructed; rests on Lem 2.1(i)'s rectangle/corner property of the fixed normalized f — load-bearing but unstated. Print: missing ⁺ superscript in hypothesis; relies on St 3.12 whose print is garbled (see St 3.12 erratum). |
SIGRAY-AUDIT.md:84:Of the 72 items audited (thesis pp. 7–30, Not 2.1 → Prop 6.2): **21 VERIFIED, 33 VERIFIED_WITH_NIT, 9 ERRATUM, 2 KNOWN_ERRATUM, 7 GAP**. Cross-check against the campaign catalogue (SHEET6-CAMPAIGN.md §7 = E1–E4 + G1–G3; E5 in SHEET6-III.md; E6–E7 in SHEET6-AF2.md; E8–E9 in SHEET6-AF3.md; E10–E11 in SHEET6-LT-REVIEW.md §6): E1–E7, E9, E11 and G1–G3 all concern §9/assembly (pp. 42–60) and do not touch this batch; the only catalogued items in scope are **E8** (Prop 5.1's cosmetic "Proposition 8" cite-slip — reconfirmed as filed) and **E10** (St 3.15 label swap — independently reconfirmed with exact witnesses; its casualty Prop 5.2 matches LT-REVIEW's FILING FIX 1 exactly). Accordingly, the two KNOWN_ERRATUM verdicts (St 3.15, Prop 5.2) are the catalogue's E10 items, while **all 9 ERRATUM verdicts are NEW**: St 3.7 (missing κπ(F) ∈ N hypothesis in (5)), St 3.8 (D ∈ Z falsified by Not 3.5's P-presentation — this upgrades the campaign's standing H5a convention to printed-statement-forced), St 3.11 (missing prime in (ii) + false equality-propagation clause), St 3.12 (duplicated identity, no (0,x) clause), St 3.13 (false for a ≠ 0; Not 3.13's p_{f−a} slip; recommended E12-candidate), St 3.18 (ε dropped from the unique-continuation conclusion), Prop 5.3 (ratio inverted in (ii)/(viii)), Prop 5.5 (proof-level g-subscript drops + "Statement 18" dangler), and Prop 6.2 (hypothesis F/G swap, same family as E10). Of the 7 GAP verdicts, one is the campaign's known-but-unnumbered **H5a** (Not 3.5 ambiguity, SHEET6-III.md §5 / SHEET6-HIII-REVIEW.md Front 4); the other six are NEW: St 3.14 (cross-fiber Ω alignment/conjugation twist in (ii)), Prop 4.2 (l_j ≠ 0 inference fails at constant-leading-part vertices; the "(7) automatic" Remark is circular), Prop 5.1 (b = 0 argument breaks at g(P) ∈ C* punctures — beyond the catalogued cosmetic E8), Prop 5.4 (q-half of the η^ν-structure never proved; verified repair supplied), Prop 5.8 (no proof printed; the "for ANY a" strength needs an unwritten a-uniformity argument), and St 6.2 (the "in particular" clause needs an H ∈ T_a⁺ hypothesis). A recurring uncatalogued slip family — Not 3.13's p_F/d_F must read p_{f−a,F}/d_{f−a,F} — drives the St 3.13 erratum and riders on Not 3.14, St 3.14, St 3.15 (hypothesis), and St 3.16; the campaign already computes with the corrected reading throughout. Three filing fixes are owed independently of new numbering: SHEET6-H3.md §2a (St 3.12) and SHEET6-A2P-REVIEW.md (St 3.18) present silently corrected text as "verbatim" quotes, and SHEET6-A3L1-REVIEW.md quotes Prop 5.3(ii)'s inverted ratio unflagged.
SIGRAY-AUDIT.md:91:- **Prop 5.8 (20) [GAP]** — the enumeration bedrock: td = ΣΛ over pole vertices is the entry point of the whole td = 6 case table (SHEET6-CAMPAIGN.md §0a/§1/§5, G1's adopted reading is "under (20) as printed"), TDUNIFORM (R3) and the prime theorem, L1, 2POLE. Critically, SHEET6-LROOT.md (PROMOTED) uses "(20) already allocates ALL td units of pole mass to T_{a,pole}" for pole purity and claims δ_a = 0 "for EVERY fiber" — exactly the any-a strength whose proof is missing. Highest-priority repair item (route: St 3.14 transport + ν_F-invariance under M_{a,b}).
SIGRAY-AUDIT.md:92:- **Not 3.5 / H5a [GAP] + St 3.8 [ERRATUM]** — the κ_F convention feeds Not 3.11, Not 5.3's Q-data, Prop 9.3, and the E5-corrected λ-bound engine; SHEET6-III.md's promoted tails closure (10 of 13) is explicitly conditional on H5a/H5b. The St 3.8 finding is favorable: it forces the H5a reading from the printed text, converting a standing hypothesis into a theorem-level constraint — ledger should record the upgrade. D-integrality (St 3.8, corrected) also underpins Prop 5.7 and every integer Q-datum in the §9 tables.
SIGRAY-AUDIT.md:93:- **Prop 5.4 [GAP]** — its (i)/(ii) η^ν-patterns are the source of St 5.2(ii)'s ν-menu, used verbatim by TDUNIFORM (R2) (PROMOTED prime theorem) and AF3's parity pin (PROMOTED, A3L1-REVIEW confirmed). The q-half those results consume is exactly the unproven half; the verified repair in this audit (using α ≥ 2) should be banked as the supporting derivation.
SIGRAY-AUDIT.md:97:- **St 3.18 [ERRATUM]** — root ↔ direction correspondence with unique-ε continuation is core to direction pricing: III (S1/S2 c = 0 forcing), L1 (one-continuation-per-orbit exclusions), AF2 (R1), TDUNIFORM (unpriced q-orbits), A2P-REVIEW. All uses are of the corrected "F*(εc)" form; A2P-REVIEW's "verbatim" label must be fixed when filing.
SIGRAY-AUDIT.md:102:- **St 3.13 + Not 3.13/3.14 slip family [ERRATUM]** — LROOT (PROMOTED) places cv vertices at "the unique (St 3.13) d = 0 point" under the corrected d_{f−a} reading it already uses; file as E12 so the reading is on the ledger rather than folklore.
SIGRAY-AUDIT.md:105:**Tier 3 — used, failure mode outside campaign usage (verify-on-use guards recommended):**
lib/FASTCOEF.md:27:(default 20000). Changing it changes which cores are reachable; parity runs
lib/FASTCOEF.md:55:  sequence, zeroed vars, log, core equations, two_chart leaves, and
lib/FASTCOEF.md:56:  byte-identical .ms emissions (SystemA raw, core at p=65521 and char 0,
lib/FASTCOEF.md:65:invariants as before); in tie cases cores could differ from pre-change
lib/FASTCOEF.md:67:open_8_28_c2: identical cores (no tie was actually decided differently).
lib/FASTCOEF.md:82:## Benchmarks (12-core M-series Mac, 32 GB, 2026-08-05, final code)
lib/FASTCOEF.md:91:| reg_9_24_c3                   | 0.3s           | 0.2s               | 1.5x    | reduced; identical 23-var core |
lib/FASTCOEF.md:92:| open_8_28_c2                  | 1.7s           | 1.3s               | 1.3x    | reduced; identical 30-var core |
lib/FASTCOEF.md:93:| open_8_28_c1                  | 143.7s         | 107.1s             | 1.3x    | reduced; identical 73-var core (114 elims, median eq 1166 terms) |
lib/FASTCOEF.md:104:does not run to a reduced core, because the MAXTERMS_EQ=20000 swell cap is
xmodel/grok-thmA-review-20260812.md:1:I'll read MATHIEU.md, the prior review, RESIDUE.md, and LEMMA.md, then re-derive Theorem A independently and try to break it.Reading the four source documents in full before any independent derivation.Theorem A’s four-step algebra looks intact; next I’ll re-derive Lemma B against the actual block conventions and hunt degree/support mismatches.Reading the paper’s `thm:ode` and SURPLUS Props A/B, then running an independent exact-arithmetic search for counterexamples.I’ll independently re-derive the identities and run an exact-arithmetic counterexample search, including the characteristic-2 control the proof itself flags.Writing an independent exact-arithmetic checker (no repo imports) and re-deriving the leading-coefficient identity by hand.**VERDICT: CONFIRMED**
xmodel/grok-thmA-review-20260812.md:3:Theorem A (MATHIEU.md §5.1) is a complete elementary proof. Lemma B’s block↔ODE identification matches SURPLUS-EXT §0 / SURPLUS Prop A–B / LEMMA.md lattice conventions. No missed degree configuration, no char-0 hole. Char 0 is sharp: explicit counterexamples exist in \(\mathbb{F}_2\).
xmodel/grok-thmA-review-20260812.md:13:4. **Degree-configuration audit (the attack).** Configurations checked independently and killed:
xmodel/grok-thmA-review-20260812.md:20:5. **Char-0 edge / sharpness.** The implication “\(d\neq w\delta\Rightarrow d-w\delta\neq 0\) in \(F\)” is the unique char-0 input. It is necessary. Independent brute force over \(\mathbb{F}_2\) found genuine counterexamples to the *statement* of Theorem A, e.g.
xmodel/grok-thmA-review-20260812.md:30:   LEMMA.md: key \((i,j)=[x^i y^j]\), Minkowski point \((i+1,j+1)\), \(\mathrm{coeff}=\sum\det(p,q)a_p b_q\). Inner column = Minkowski \(x=k+1\) = bracket \(x^k\). SURPLUS-EXT “key \((X,s)=[y^{s-1}]\)” matches: vertex \((k+1,1)\leftrightarrow y^0\); \(w=0\) top \((k+1,(k+1)d_2)\leftrightarrow y^{(k+1)d_2-1}\), weight \(kd_2-kd_2=0\); extras \(w\in[1,d_2-1]\) are \(y^{kd_2}\ldots y^{(k+1)d_2-2}\), count \(d_2-1\). Q-col-\(k\) support: \(w_Q=kd_2-1\) forces \(j\in\{1,\ldots,kd_2\}\). LEMMA.md’s \((2,2)\) rigidity key is Minkowski \((3,5)=[y^4]\), the unique extra at \((k,d_2)=(2,2)\). Pair formula \(=\) lattice det, checked by expanding both sides at \((k,d_2)\in\{2,3,5\}\times\{2,3,4\}\).
xmodel/grok-thmA-review-20260812.md:36:9. **Valuation reading (remark after Thm A).** With \(t=C/A^w\), Step 2 forces \(v_\infty(t)=0\). Then \(v_\infty(t')=(w+1)\delta\), so \(t-t(\infty)\) must vanish at \(\infty\) to order \((w+1)\delta-1\). Budget from \(\deg D<w\delta\) is at most \(w\delta\). Inequality \((w+1)\delta-1>w\delta\iff\delta\ge 2\). Faithful transcription of Steps 1–4; not an extra hypothesis.
xmodel/grok-thmA-review-20260812.md:38:**Nits (non-load-bearing).** Symbol collision Theorem-A weight \(w\) vs SURPLUS stratum \(w=d_2 i-j\). Lemma B’s “\(y^0\) coefficient is \(c_1\)” is after the stated unit scaling; unnormalized it is \(a_1 c_1\). Bridge (d) parenthetical “any solution has \(\deg C=k\delta\)” holds only for \(\delta\ge 2\).
SURPLUS-REVIEW.md:22:- k=1 caveat: the "gap side = x-max" normalization is UNDEFINED at k=1 (both
SURPLUS-REVIEW.md:48:  structurally 100% in the normalized orientation, all 20 grid cells.
SURPLUS-REVIEW.md:51:  normalization is UNDEFINED at k=1 (both corners have x=1). In the reg
SURPLUS-REVIEW.md:56:  under the normalization so they are not false, but the doc's table and note 1
SURPLUS-REVIEW.md:62:- Main-theorem cross-check by linear algebra (no cascade): at generic a,
SURPLUS-REVIEW.md:74:## 3. Main theorem proof, (k,d2)=(2,2): step-by-step audit
SURPLUS-REVIEW.md:102:     "a2^2 a6 in I(core)" if I(core) is read as the generated ideal (fine if
SURPLUS-REVIEW.md:103:     I(core) means the ideal of the core variety). LEMMA.md sec 2.2's "key (2,4)
SURPLUS-REVIEW.md:106:   - The theorem's own conclusion ("the chart inverting {a2,a6} is empty",
SURPLUS-REVIEW.md:119:   (i)); no dependence on LEMMA.md's far-corner fix_ones normalization, in
SURPLUS-REVIEW.md:191:discrepancies inside their stated scope; the (2,2) main theorem's equations,
SURPLUS-REVIEW.md:198:Defects found (all repairable, none fatal to the (2,2) theorem):
SURPLUS-REVIEW.md:204:2. k=1 scope gap: the gap-side normalization is undefined at k=1; Prop B and
SURPLUS-REVIEW.md:224:theorem, (2,2) regime): YES — ready for paper-grade drafting after the small
SURPLUS-REVIEW.md:231:evidence (d2>=3) — keep those out of the theorem statement, keep the
lean/README.md:3:Machine-checks the certificate-level core of `../LEMMA.md` / paper1 Section 5:
lean/README.md:11:  `../cases/eq3_chain.py`). Two theorems:
lean/README.md:41:the counting/census theorem (51 zero / 40 polynomial / 1 constant); the
SHEET6-DEPTH.md:8:Theorem MP (SHEET6-MULTIPOLE.md §0/§5; demotion SHEET6-MP-REVIEW.md Front 5)
SHEET6-DEPTH.md:9:is RESTORED in corrected, sharper form (§8). Two engine-model corrections
SHEET6-DEPTH.md:22:priors: SHEET6-MULTIPOLE.md (MP0–MP9, Theorem O), SHEET6-MP-REVIEW.md
SHEET6-DEPTH.md:31:each chain frame in the i-normalized coordinates ρ := D_F/deg(p_F) (full
SHEET6-DEPTH.md:51:jump-vertex book is therefore **finite per (m, td)** (§8).
SHEET6-DEPTH.md:55:## 1. Setting and normalization
SHEET6-DEPTH.md:63:ending at the last vertex before a merge vertex G (r(G) ≥ 2) or before
SHEET6-DEPTH.md:67:Frames are taken **i-normalized** ("shape space" of the engines, P-free):
SHEET6-DEPTH.md:77:arrivals, and dp/dq = i-normalized slope ratio, Prop 9.3(b)), so w > 0.
SHEET6-DEPTH.md:97:an iff: p_{F_j} has more than one root. The single simple ν-orbit has root
SHEET6-DEPTH.md:98:set {ζc : ζ^ν = 1} — more than one root forces ν ≥ 2 and c ≠ 0. (This is
SHEET6-DEPTH.md:116:they generate the same exponent lattice L below u; u ∉ L because β′_{j′}
SHEET6-DEPTH.md:118:at an exponent outside its running lattice is, by Def 3.1(i), exactly the
SHEET6-DEPTH.md:129:therefore at most the number m_i of characteristic exponents of P_i, so
SHEET6-DEPTH.md:157:*Proof.* Case (II) applies (DS1(d)). Prop 9.3(b) (p. 50), i-normalized by
SHEET6-DEPTH.md:258:(ν ≥ 2 forces V_1 membership, Not 3.4; π(G) is off-lattice, realized as a
SHEET6-DEPTH.md:261:(e)–(h) with ν := ν_F: i-normalized, κ̄_G = κ̄_e + n′, D_G/i = ρ_e + n′
SHEET6-DEPTH.md:275:arrival coefficient at an off-lattice exponent = characteristic exponent
SHEET6-DEPTH.md:277:(V_{2,a}\V_{1,a}, lattice meet). All non-0 edges keep the §5a handshake.
SHEET6-DEPTH.md:373:## 8. Consequence: the finite book, restored
SHEET6-DEPTH.md:375:**Theorem (finite jump-vertex book).** For every (m, td), the multi-pole
SHEET6-DEPTH.md:376:reduction of Theorem MP terminates in a FINITE book: BOOK(m, td) as in
SHEET6-DEPTH.md:406:  3.4/3.5 + Def 3.1 + Prop 3.1 + St 3.17(i); the lattice argument in
SHEET6-DEPTH.md:419:  item 3), m ≥ 3 reachability of Theorem O's pattern-level escape, and
SHEET6-R1.md:3:Status: FULL-DEGREE TERMINAL CORE BUILT, GUARDED, AND RUN LOCALLY
SHEET6-R1.md:5:minimal-branch G_m core (C1-Gm proven vacuous; 10 constant rows carry
SHEET6-R1.md:7:systems/r1/r1_full_core.ms with mod-p / w-free variants and the
SHEET6-R1.md:8:(1,2)-sibling core; msolve local: no [1] on any faithful encoding
SHEET6-R1.md:11:the banked core. Engine: cases/r1_experiment.py + cases/r1_fullcore.py.
SHEET6-R1.md:18:- Tower normalization (7b): stage the PRINT-TRUE tower h1 = g^2 - s0 f^3,
SHEET6-R1.md:44:- (d) Pre-register terminal J-closure BEFORE solving. PENDING details.
SHEET6-R1.md:46:## 1. Pre-Registered Interpretation (fixed BEFORE any solve)
SHEET6-R1.md:48:- R6 window empty AND R1 staged system UNSOLVABLE => template DIES (two-pole td=6 excluded, theorem-grade).
SHEET6-R1.md:54:consistency to depth deg f = 168 (an L2'-tier structure theorem, NOT a
SHEET6-R1.md:55:candidate pair). The terminal nonlinear core (expected <= 20 vars; size
SHEET6-R1.md:57:J(f,g) in C^*; only SOLVABLE-with-core-passing = near-counterexample
SHEET6-R1.md:73:### 3.0 Engine formulation (cases/r1_experiment.py; fixed before solving)
SHEET6-R1.md:79:sigma = 6 (x/y-scale pair normalizes (A, sigma) jointly; det 420 != 0)
SHEET6-R1.md:96:force per-embedding evaluation (not expected).
SHEET6-R1.md:100:fractional parts; F_s-jet: slots not in (1/7)-lattice; G_m analog).
SHEET6-R1.md:108:still-free unknowns nonlinearly => deferred to terminal core. Ledger:
SHEET6-R1.md:117:start clean; `--depth=N`, default 54). Each phase < 10 min foreground.
SHEET6-R1.md:149:Structural finding (engine-derived, banked before the run finishes): in
SHEET6-R1.md:165:still-free unknowns defer to the core; 1414 rows, stages m = 18..52):
SHEET6-R1.md:184:H_M) — exactly the "terminal nonlinear core" of the pre-registration,
SHEET6-R1.md:190:Terminal core (banked explicit form + sizing, spec item 5 "else"
SHEET6-R1.md:191:branch): systems/r1/r1_gmband_core.ms + .vars.txt — the G_m-band
SHEET6-R1.md:200:can eliminate ~half the variables before a farm run. Independent
SHEET6-R1.md:221:  defer to the terminal core (1136 of 1414 rows). A solvable linear
SHEET6-R1.md:229:  decisive content at this depth IS the banked terminal core (109
SHEET6-R1.md:232:  core, not on any further linear stage; (iv) the J(f,g) closure is
SHEET6-R1.md:234:  merge) and remains an unfulfilled core member, so no candidate-tier
SHEET6-R1.md:239:## 5. Next Step
SHEET6-R1.md:241:1. Full-degree core build: per-(orbit,k) sub-checkpointing at
SHEET6-R1.md:245:   (mod-p first) on the reduced core. UNSOLVABLE core (with R6 closed)
SHEET6-R1.md:251:3. Merge the LROOT x-side pin to express J(f,g) in the core (R5), the
SHEET6-R1.md:253:4. B-side partition audit (42 vs 2x21 etc. for f; 42+21 for g) before
SHEET6-R1.md:256:## 6. Core verdict (parent session, 2026-08-09)
SHEET6-R1.md:258:`systems/r1/r1_gmband_core.ms` (cap-2 G_m-band core: 118 vars incl. 9
SHEET6-R1.md:260:**EMPTY — GB = [1]** in ~5 s (runs/r1_gmband_core.out, 759 B, verdict
SHEET6-R1.md:261:line present; not a silent death). Since the core is a constraint SUBSET
SHEET6-R1.md:264:CONDITIONAL on core-emission faithfulness (under adversarial review; a
SHEET6-R1.md:265:spurious over-constraint would fake this). Note the signature: 64
SHEET6-R1.md:270:core): (1,2) [delta-spec written], (2,3)-chain (6,17), (2,5)-chain
SHEET6-R1.md:286:soundness fix, [1]-plausibility guards, then the FULL-DEGREE core build
SHEET6-R1.md:289:## 8. Rebuilt terminal core — build log (2026-08-09, per SHEET6-R1-REVIEW mandates)
SHEET6-R1.md:291:Mission: full-degree discriminating G_m core for the minimal branch,
SHEET6-R1.md:295:### 8.0 Plan (banked before work)
SHEET6-R1.md:300:   (HIVAR,) keys); (b) block-refactored G_m jets: f^3 and g^2 built as
SHEET6-R1.md:302:   jmul(f^2,f) blowup; slot truncation is order-independent since slots
SHEET6-R1.md:316:5. Emit systems/r1/r1_full_core.ms (char 0, radical gens as vars) +
SHEET6-R1.md:325:satisfies the core, msolve UNSOLVABLE is impossible for the intended
SHEET6-R1.md:338:  A2^3-3+r3, Phi42 as literal string. emit_core / emit_gm_core rewired.
SHEET6-R1.md:344:Sizing (combinatorial, before build): weight<=20 multiset counts:
SHEET6-R1.md:350:exact fold if timing allows. Driver: cases/r1_fullcore.py (next).
SHEET6-R1.md:352:### 8.2 Full-degree build driver (cases/r1_fullcore.py)
SHEET6-R1.md:388:   — exactly the slot-20 lattice 2n == 20 (mod 6). Full consistency.
SHEET6-R1.md:390:   1..19 on the lattice) + WG-quot 5 (n = 1,4,7,10,13; n = 16 cancels
SHEET6-R1.md:391:   identically as it must) + WG-quot-deg 6 (n = 19..34 lattice).
SHEET6-R1.md:398:   a-priori possible for this core. Screen emitted:
SHEET6-R1.md:399:   systems/r1/r1_full_core_modp.ms (98 eqs, 119 vars, 6.5 MB, char p).
SHEET6-R1.md:406:  (runs/r1_full_core_modp.ms.screen.out). INTERPRETATION UNDER GUARD
SHEET6-R1.md:412:  the quotient rows". The char-0 core (radicals as VARIABLES) is the
SHEET6-R1.md:418:  n = 1,4,7,10,13 (lattice n < 16) and n = 19,22,25,28,31 (beyond
SHEET6-R1.md:430:  mod-p folds before emission (structural equality of supports +
SHEET6-R1.md:437:  terminal core (98 rows), which is the banked sec-3 terminal family;
SHEET6-R1.md:443:  quotient vs qpat after s1-subtraction. Lattice consistency checked:
SHEET6-R1.md:454:keys SYMBOLIC and only the K3 Fraction pairs reduced mod p (rnorm
SHEET6-R1.md:460:EXACT char-0 W_G. Note: C1-Gm vacuity means the core needs W_G only.
SHEET6-R1.md:468:  test, keys all equal). uf30 is a free direction of the G_m core (it
SHEET6-R1.md:481:- Stale cap-2 artifacts renamed r1_gmband_core.{ms,vars.txt}.RETRACTED
SHEET6-R1.md:483:  consumable namespace; superseded by r1_full_core*).
SHEET6-R1.md:486:  each on 12 cores; post-fold chain armed (CRT -> emit+guards ->
SHEET6-R1.md:494:a pipeline error under guard 3b). The screen's [1] therefore hinges on
SHEET6-R1.md:520:raw-key reduction in rmul_p (rnorm chain + Phi42 z-reduction cached
SHEET6-R1.md:562:Vandermonde (stored (V^-1)^T V c instead of c). Caught by the
SHEET6-R1.md:564:Repair applied in place per prime: c = V^-1 V^T stored (phase_fixz,
SHEET6-R1.md:568:coefficients up to 5.6e34/32 (true magnitudes are enormous — sums over
SHEET6-R1.md:583:### 8.17 EXACT CORE BUILT + ALL GUARDS PASS (06:07)
SHEET6-R1.md:588:- EMITTED systems/r1/r1_full_core.ms — the pre-registered full-degree
SHEET6-R1.md:589:  minimal-branch G_m terminal core: 7 expanded radical eqs + 98 rows
SHEET6-R1.md:591:  gens, 18.1 MB, integer coefficients, content-normalized, NO parens.
SHEET6-R1.md:592:  Also r1_full_core_p{105337,105673}.ms (same system, coefficients mod
SHEET6-R1.md:593:  p, radicals still variables) and r1_full_core_wfree_p*.ms (z, r3,
SHEET6-R1.md:601:  dropped). Row labels: r1_full_core.rows.txt.
SHEET6-R1.md:613:### 8.19 (1,2) sibling core EMITTED
SHEET6-R1.md:617:p=105337): 68,254 entries / 93 keys. (1,2)-branch core emitted per the
SHEET6-R1.md:618:SHEET6-R6 4.3 delta-spec: systems/r1/r1_12branch_core.ms — 105 eqs
SHEET6-R1.md:624:the (1,2) core is also NOT origin-satisfiable => genuinely
SHEET6-R1.md:625:discriminating). Row labels: r1_12branch_core.rows.txt.
SHEET6-R1.md:631:| r1_full_core_modp.ms (screen) | 119 | p | specialized | RANDOM point | [1] in ~1 s (E5-load diagnostic, NOT a verdict — w-point not on quartic locus) |
SHEET6-R1.md:633:| r1_full_core_wfree_p105337.ms | 123 | p | z,r3,A1,A2,EB specialized | FREE | TIMEOUT 1200 s (no [1]) |
SHEET6-R1.md:634:| r1_full_core_wfree_p105673.ms | 123 | p | specialized | FREE | TIMEOUT 1200 s (no [1]) |
SHEET6-R1.md:636:| r1_full_core_p105337.ms | 128 | p | VARIABLES | free | TIMEOUT 1200 s (no [1]) |
SHEET6-R1.md:637:| r1_full_core.ms (PRE-REGISTERED) | 128 | 0 | VARIABLES | free | TIMEOUT 1200 s (no [1], no basis) |
SHEET6-R1.md:639:| r1_full_core_p105673.ms | 128 | p | VARIABLES | free | TIMEOUT 1200 s (no [1]) |
SHEET6-R1.md:641:(All outputs in runs/r1_full_core*.out.)
SHEET6-R1.md:646:  **NOT TRIGGERED.** The correct full-degree minimal-branch core
SHEET6-R1.md:658:  the banked, guard-certified core.** What IS established (new, exact,
SHEET6-R1.md:659:  guarded): (i) the true full-degree minimal-branch G_m terminal core
SHEET6-R1.md:662:  and verified on two independent evaluation paths); (ii) the core is
SHEET6-R1.md:668:  mod-p INCONSISTENT with the core ([1] in 1 s) while w-free encodings
SHEET6-R1.md:671:  direction of this core). The kill-or-candidate decision is exactly
SHEET6-R1.md:672:  the farm-scale GB of r1_full_core.ms (and its mod-p reductions
SHEET6-R1.md:675:Deliverables: systems/r1/r1_full_core.ms (+.rows.txt, char-0
SHEET6-R1.md:676:pre-registered core), r1_full_core_p{105337,105673}.ms (mod-p
SHEET6-R1.md:677:reductions, radicals as variables), r1_full_core_wfree_p*.ms (w-free
SHEET6-R1.md:678:branch screens), r1_full_core_modp.ms (all-specialized diagnostic),
SHEET6-R1.md:679:r1_12branch_core.ms (+.rows.txt, (1,2)-sibling core per the 4.3
SHEET6-R1.md:680:delta-spec, guard-passed), r1_gmband_core.ms.RETRACTED (quarantined);
SHEET6-R1.md:681:engine fixes in cases/r1_experiment.py; builder cases/r1_fullcore.py;
SHEET6-R1.md:682:run logs runs/r1_full_core*.out; state /tmp/r1full (16 CRT primes,
SHEET6-R1.md:685:## 9. Chain-branch terminal cores ((2,3)->(6,17), (2,5)->(6,23)) — build log (2026-08-10)
SHEET6-R1.md:687:### 9.0 Plan + in-window structure (banked before build)
SHEET6-R1.md:691:re-emission of the minimal core is the regression gate): --blocks (DONE
SHEET6-R1.md:696:8.3; re-emitted r1_full_core_modp.ms BYTE-IDENTICAL to the banked copy),
SHEET6-R1.md:733:  local (2,5) core = level 1 + r=0 legality + r=2 tie: every row a true
SHEET6-R1.md:734:  consequence of the chain genome (necessary-condition core).
SHEET6-R1.md:736:the Rabinowitsch row t1*s1 - 1 = 0 => cL != 0 => the core does NOT
SHEET6-R1.md:748:resp. 139/6. Fresh vars per chain core: s1 (tie scale), t1 (its
SHEET6-R1.md:751:emit_expanded, AUDIT rule); guards A-D on both cores; w-free mod-p
SHEET6-R1.md:756:cases/r1_fullcore.py additions (nothing above the chain section
SHEET6-R1.md:762:mod-p evaluation vs the factored form at both round-trip primes:
SHEET6-R1.md:769:exactly; chain_rows / emit_chain_core / emit_chain_wfree / phase_chain
SHEET6-R1.md:773:Key-lattice census (scalar fold pWG, verified): W_G keys live ONLY at
SHEET6-R1.md:776:(n = 1..31) — the 8.4 qcheck facts reproduced. All chain lattices
SHEET6-R1.md:779:synthetic lattice-correct miniature W_G (throwaway outdir): row
SHEET6-R1.md:784:origin census = exactly 1 constant row (t1*s1 - 1) per core. Post
SHEET6-R1.md:788:=> 2 constant rows for the (2,3) core.
SHEET6-R1.md:829:emitted artifact systems/r1/r1_full_core.ms, not the pickles; all
SHEET6-R1.md:833:(written BEFORE any sweep run)
SHEET6-R1.md:835:A char-0 point of the core specializes to a point mod almost all p
SHEET6-R1.md:837:coordinates). Therefore, for independent random primes p_1..p_k:
SHEET6-R1.md:852:### 10.1 Linearity analysis of the emitted core (phase analyze/incidence)
SHEET6-R1.md:856:  "mostly linear rows" premise is FALSE for this core; the correct
SHEET6-R1.md:865:- Soundness scheme (fixed before running): eliminate (v, A) only when
SHEET6-R1.md:883:- systems/r1/r1_reduced_core.ms (char 0, 56 eqs, 63 vars, 0.9 MB)
SHEET6-R1.md:884:- r1_reduced_core_p{105337,105673}.ms (mod p, radicals as variables)
SHEET6-R1.md:885:- r1_reduced_core_wfree_p{105337,105673}.ms (z,r3,A1,A2,EB specialized,
SHEET6-R1.md:887:- r1_reduced_core.rows.txt (provenance: per-pivot bank + row map)
SHEET6-R1.md:890:40/49 vanish at x=0; 9 quotient-family rows do NOT => reduced core NOT
SHEET6-R1.md:900:### 10.3 Run ledger, reduced core (msolve 0.10.1, -g 2, timeout 1200 s)
SHEET6-R1.md:905:| r1_reduced_core.ms (char 0, radicals as vars) | 63 | 0 | TIMEOUT 1200 s |
SHEET6-R1.md:906:| r1_reduced_core_p105337.ms | 63 | p | TIMEOUT 1200 s |
SHEET6-R1.md:907:| r1_reduced_core_p105673.ms | 63 | p | TIMEOUT 1200 s |
SHEET6-R1.md:908:| r1_reduced_core_wfree_p105337.ms | 58 | p | TIMEOUT 1200 s |
SHEET6-R1.md:909:| r1_reduced_core_wfree_p105673.ms | 58 | p | TIMEOUT 1200 s |
SHEET6-R1.md:947:| r1_reduced_core_p40427 | 40427 | radicals as vars | TIMEOUT 3900 s |
SHEET6-R1.md:948:| r1_reduced_core_p56453 | 56453 | radicals as vars | TIMEOUT 3900 s |
SHEET6-R1.md:949:| r1_reduced_core_p76631 | 76631 | radicals as vars | TIMEOUT 3900 s |
SHEET6-R1.md:950:| r1_reduced_core_wfree_p105337 | 105337 | wfree branch | TIMEOUT 3900 s |
SHEET6-R1.md:966:1. RETARGET, do not keep as-is: r1_reduced_core.ms is verdict-
SHEET6-R1.md:967:   equivalent to r1_full_core.ms (certified bijection x A^46) at 63 vs
SHEET6-R1.md:971:   core (same pre-registered object, same sec-1 table).
SHEET6-R1.md:972:2. CALIBRATE BEFORE BURNING WALL CLOCK: bank ONE mod-p verdict first
SHEET6-R1.md:973:   (farm, reduced core, a few primes, multi-hour budgets). EMPTY at
SHEET6-R1.md:979:   REDUCED core) says this GB is deep at any characteristic; if 2.
SHEET6-R1.md:982:   pivots barred here -- or slot-band staging), not more budget.
SHEET6-R1.md:990:## 11. Chain-core first verdicts (parent session, 2026-08-10)
SHEET6-R1.md:993:reproduces r1_full_core.ms exactly); both chain cores accepted (guards
SHEET6-R1.md:996:**(2,5)-chain core: NONEMPTY at p=105337 AND at char 0** (local msolve,
SHEET6-R1.md:997:minutes; runs/r1/r1_25chain_core.out = reduced GB, 487 elements, char 0,
SHEET6-R1.md:1000:the branch's formal candidate DEEPENS. Scope: the core carries 25/37
SHEET6-R1.md:1005:(2,3)-chain core (110 eqs, 9.7 MB): queued on ultramem behind the
SHEET6-R1.md:1008:## 12. (2,5) EXTENDED core: deferred rungs r <= 10 (2026-08-10)
SHEET6-R1.md:1010:### 12.0 Plan + pre-registration (banked before build)
SHEET6-R1.md:1012:Decision target (SHEET6-R1-25LOCUS SS6.3, pre-registered): core (all 44
SHEET6-R1.md:1013:eqs of r1_25chain_core.ms) + the SYMBOLIC deferred tie rows for rungs
SHEET6-R1.md:1021:Construction (engine-exact, additive to cases/r1_fullcore.py):
SHEET6-R1.md:1043:Guards (all must pass BEFORE any verdict): A paren sweep; B
SHEET6-R1.md:1055:Regression gate: re-emission of the unextended core stays
SHEET6-R1.md:1056:byte-identical to the banked r1_25chain_core.ms.
SHEET6-R1.md:1064:Engine additions (cases/r1_fullcore.py, ADDITIVE — nothing above the
SHEET6-R1.md:1072:byte-identical core regression gate).
SHEET6-R1.md:1096:Extended system r1_25chain_ext: **132 rows** = 44 core eqs (7 radical
SHEET6-R1.md:1098:r1_25chain_core.ms modulo the continuation comma) + 95 deferred rows
SHEET6-R1.md:1099:(r=4: 23, r=6: 24, r=8: 24, r=10: 24); vars = 9 radicals + 29 core-x
SHEET6-R1.md:1110:| regression gate (core re-emission) | PASS — BYTE-IDENTICAL to banked r1_25chain_core.ms (guards A-D re-passed on the core en route) |
SHEET6-R1.md:1130:| ext_p105337 solo | 3000 s | **TIMEOUT** (RSS to ~16 GB, 100% CPU throughout; no partial output — msolve writes only at completion). The extended GB is FAR heavier than the core's 487-elt/55 s: the 95 deferred rows carry real load |
SHEET6-R1.md:1132:## 13. Chart decomposition of the reduced core (2026-08-11)
SHEET6-R1.md:1135:artifact systems/r1/r1_reduced_core.ms; prior emissions untouched).
SHEET6-R1.md:1139:### 13.0 Structural finding (banked BEFORE any leaf run) + design
SHEET6-R1.md:1143:row touches both W-sides; NO row has an x-free W-free term. Therefore
SHEET6-R1.md:1145:term of EVERY row: it lies on V(reduced core) EXACTLY, in char 0 and
SHEET6-R1.md:1148:contains this point; 34 h + 1.5 TB were spent toward a foredoomed,
SHEET6-R1.md:1149:undiagnostic NONEMPTY. Diagnosis: the emitted core is a RELAXATION --
SHEET6-R1.md:1153:were subsumed as embeddings, so no quartic row exists in the core).
SHEET6-R1.md:1157:to the pivot-blocking variables W1, W2): split V(reduced core) by the
SHEET6-R1.md:1172:PRE-REGISTERED INTERPRETATION (fixed BEFORE any leaf solve): the four
SHEET6-R1.md:1173:leaves partition V(core) by a boolean tautology, so (all leaves EMPTY)
SHEET6-R1.md:1174:<=> core EMPTY, and any leaf point maps to a core point. ZZ is
SHEET6-R1.md:1183:The composite relaxed-core verdict (NONEMPTY via ZZ) is reported
SHEET6-R1.md:1212:ENTIRE minimal-branch G_m terminal core, restricted to the intended
SHEET6-R1.md:1221:+s/3 and -s/3 -- the sum is IDENTICALLY ZERO. The G_m core's only
SHEET6-R1.md:1247:COVER CERTIFICATE. Claim: V(reduced core) = U_pat pi(V(leaf_pat)),
SHEET6-R1.md:1261:point maps to a core point by forgetting uWi and restoring W_i = 0
SHEET6-R1.md:1263:EMPTY on all leaves <=> core EMPTY, and any leaf witness lifts.
SHEET6-R1.md:1267:Runs: msolve 0.10.1, -g 2 -t 4, timeout 900 s, local (12-core/32 GB);
SHEET6-R1.md:1280:1. Relaxed-core p-screen at BOTH banked primes: NONEMPTY =
SHEET6-R1.md:1282:   UU-stratum (15-elt GB). ZU/UZ EMPTY: every core point mod p has
SHEET6-R1.md:1284:   core is NOT killed at p. No EMPTY trigger; no inflation.
SHEET6-R1.md:1287:   with guard E + sec-10.2 guard E, V(full core) NONEMPTY over Qbar).
SHEET6-R1.md:1288:   The pre-registered decisive object (char-0 core emptiness, sec
SHEET6-R1.md:1290:   DEEPENS; R1's terminal G_m core imposes, on the intended chart,
SHEET6-R1.md:1296:   above at ~1 s/leaf. RETIRE the reduced-core monolith from the
SHEET6-R1.md:1302:rational point of the FULL terminal core with W1, W2 != 0 was
SHEET6-R1.md:1304:INDEPENDENT parser (r1_fullcore.parse_eval):
SHEET6-R1.md:1310:  r1_reduced_core.ms AND ALL 105 eqs of r1_full_core.ms evaluate to 0.
SHEET6-R1.md:1323:(systems/, runs/ are gitignored-regenerable; leaves re-emittable via
SHEET6-R1.md:1324:build + emit from r1_reduced_core.ms). Prior emissions byte-untouched.
SHEET6-R1.md:1344:## 14. Minimal-branch EXTENDED system: UU-chart core + F_s-band rungs r <= 4 (2026-08-11)
SHEET6-R1.md:1346:### 14.0 Design + rung choice + pre-registration (banked BEFORE build)
SHEET6-R1.md:1349:12), mandated by sec 13: the core alone is non-discriminating (UU chart
SHEET6-R1.md:1353:SYSTEM = core + chart + deferred F_s rungs:
SHEET6-R1.md:1354:- CORE PART: r1_full_core.ms VERBATIM (105 eqs; regression gate:
SHEET6-R1.md:1355:  byte-identity). The UNREDUCED core is required for soundness: the
SHEET6-R1.md:1358:  the reduced core (or the UU leaf) with raw F_s rows would leave
SHEET6-R1.md:1360:  full core carries the same variety with zero substitution machinery.
SHEET6-R1.md:1364:  w_i units. Adjoining the inverses to the FULL core is sound: the
SHEET6-R1.md:1385:New variables (beyond the core's 119): uW1, uW2 + the F_s-window vars
SHEET6-R1.md:1389:PRE-REGISTERED INTERPRETATION (sec 1 discipline, fixed before any
SHEET6-R1.md:1399:GUARDS (all must pass before any verdict): A paren sweep; B two-prime
SHEET6-R1.md:1403:banked full-core witnesses MUST satisfy all 105 core + 2 chart rows of
SHEET6-R1.md:1416:banked r1_full_core_p*.ms used the older signed-digit reduction; the
SHEET6-R1.md:1422:engine files byte-untouched; runtime-only monkey-patch of R1.rnorm).
SHEET6-R1.md:1424:Fold-shape measurements (orbit B, slot cap 13, banked before the full
SHEET6-R1.md:1426:- rnorm memo (rnorm(key,c) is EXACTLY linear in c; key-part cached;
SHEET6-R1.md:1427:  300-sample A/B against the unpatched rnorm asserted at patch time):
SHEET6-R1.md:1437:  the zeta^{7js} phases by selector BEFORE any eta-product): 31.4 s,
SHEET6-R1.md:1465:EMITTED (systems/r1/): r1_minimal_ext.ms (323 eqs = 105 core VERBATIM
SHEET6-R1.md:1471:vars, 18 MB each: banked wfree core rows verbatim + uW rows + F_s
SHEET6-R1.md:1477:| regression gate | PASS -- first 105 eqs BYTE-IDENTICAL to r1_full_core.ms |
SHEET6-R1.md:1479:| B round-trip | PASS both primes -- char0 vs p-variant exact (323 rows); F_s rows exact vs internal VExpr eval (216/216, and all nonzero at random points); wfree core rows via 2-point cross-ratio (banked wfree emission is unscaled; char-0 is content-normalized -- per-row scalar allowance, sec-12 E(i) style) |
SHEET6-R1.md:1482:| E witness (13.4, both primes) | core+chart: ALL 107 rows vanish -- emission validated end-to-end through both banked back-maps. F_s rows: 0/216 nonzero -> VACUOUS AT THE WITNESS (see 14.3) |
SHEET6-R1.md:1488:satisfy ALL 323 equations of the emitted extended system -- core (105),
SHEET6-R1.md:1490:is therefore decided by explicit point BEFORE msolve: NONEMPTY at both
SHEET6-R1.md:1503:foredoomed-run lesson applied BEFORE spending the compute): rung 5
SHEET6-R1.md:1513:is NON-DISCRIMINATING against the minimal-branch core's surviving
SHEET6-R1.md:1514:locus at the banked primes -- the free-x directions the core leaves
SHEET6-R1.md:1538:The GB confirmation therefore ships to box01 (sizes above; NOTE:
SHEET6-R1.md:1557:   over the F_s-window vars exactly as the core did.
SHEET6-R1.md:1573:new file; runtime-only rnorm memo patch, A/B-tested at import; no
SHEET6-R1.md:1581:### 15.0 Part-A plan + pre-registration (banked BEFORE any build/solve)
SHEET6-R1.md:1583:Mission: apply the sec-13 chart decomposition to the (1,2) sibling core
SHEET6-R1.md:1584:systems/r1/r1_12branch_core.ms (8.19: 105 eqs = 7 radical + 98 rows
SHEET6-R1.md:1587:(imports r1_decompose/r1_reduce functions; minimal-core leaves stay
SHEET6-R1.md:1588:byte-identical -- sha256 regression gate on systems/r1/leaves/ before
SHEET6-R1.md:1592:Design deltas vs sec 13 (mechanical): (i) input = the RAW (1,2) core
SHEET6-R1.md:1596:(ii) cover-cert part (iii) is REPLACED: the (1,2) core has 10
SHEET6-R1.md:1603:PRE-REGISTERED INTERPRETATION (fixed BEFORE any leaf solve; sec-1
SHEET6-R1.md:1605:SHEET6-R6 4.3): the 4 leaves partition V(core) by the (W1,W2)
SHEET6-R1.md:1607:- ALL FOUR leaves EMPTY (GB=[1]) at both banked primes => (1,2) core
SHEET6-R1.md:1610:  its terminal core.
SHEET6-R1.md:1615:- UU NONEMPTY => (1,2) survives its terminal core on the intended
SHEET6-R1.md:1659:satisfies the (1,2) core's entire UU residual identically, and the
SHEET6-R1.md:1667:EMITTED (systems/r1/leaves/, minimal-core leaf_* files BYTE-UNTOUCHED
SHEET6-R1.md:1685:2); (iii') REPLACED per 15.0: origin census on the RAW core at both
SHEET6-R1.md:1691:leaves <=> core EMPTY; any leaf witness lifts.
SHEET6-R1.md:1698:emitted (1,2)-core eqs under the INDEPENDENT parser.  The (1,2)
SHEET6-R1.md:1699:p-screen NONEMPTY verdict is therefore explicit-point-certified
SHEET6-R1.md:1700:BEFORE msolve; calibration runs are confirmation only.  (Same W1
SHEET6-R1.md:1734:   and in char 0 => the (1,2) branch SURVIVES its terminal core on
SHEET6-R1.md:1739:3. ZU/UZ EMPTY (char-0-proven on ZU): every core point has W1, W2
SHEET6-R1.md:1831:  witness-specialized quotient evaluation.  Specialize each orbit
SHEET6-R1.md:1840:  first (all 40 unknowns = 0 vs the constants) is pure evaluation.
SHEET6-R1.md:1845:  13.4 machinery) and fresh primes (13.6 walk); same Q0 evaluation
SHEET6-R1.md:1848:  Soundness: EMPTY(core + chart + quotient) => EMPTY(full tier)
SHEET6-R1.md:1852:  parametrization (13.1: core == E x A^38 on the chart; invertible
SHEET6-R1.md:1869:    sibling ladders ((1,2) -- now at the SAME E-core, sec 15.1-15.2
SHEET6-R1.md:1888:char-0-decided: every char-0 core point has W1, W2 both zero or both
SHEET6-R1.md:1897:lines); state /tmp/r1dec12 (core.pkl parse cache + leaves.pkl).
SHEET6-R1.md:1898:Minimal-core leaf emissions BYTE-IDENTICAL (sha256 gate, 16/16 OK).
SHEET6-R1.md:1905:### 16.0 Plan + pre-registration (banked BEFORE build; 15.6 semantics
SHEET6-R1.md:1909:registry/build_generators at depth 84, r1_fullcore mod-p machinery
SHEET6-R1.md:1910:pjmul/ring_modp, r1_minimal_ext witness_point + rnorm memo).
SHEET6-R1.md:1912:BEFORE any work (/tmp/q0_regression_baseline.sha); must be unchanged
SHEET6-R1.md:1917:(banked 135 emitted vars via r1_full_core.rows.txt map + sec-14 ext
SHEET6-R1.md:1932:ANCHORS (8.4-style, ALL must pass before any row is trusted; failures
SHEET6-R1.md:1955:banked primes.  Zero-extension pre-check (pure evaluation, banked
SHEET6-R1.md:1974:| A4 free closure measured | PASS -- band rows s = 6..54 carry ZERO constant part at the witness (15.5 argument reproduced by direct evaluation) |
SHEET6-R1.md:2003:satisfies the entire Q0 block by pure evaluation, BEFORE msolve.
SHEET6-R1.md:2032:(pre-registered trigger: all witnesses die).  Therefore:
SHEET6-R1.md:2062:staged as window rows co-graded with the banked y-side core, x-side
SHEET6-R1.md:2068:(4) a 15.6-style kill/survive pre-registration banked BEFORE the
SHEET6-R1.md:2112:checked before AND after).  msolve 0.10.1, -g 2 -t 4, timeboxed
SHEET6-R1.md:2136:| H_M (G_m h1-lead) | 1b: lead of forced-degree pattern p_h1,Gm (deg 16); E5 pins it against w_i^4 | RESTORED as variable HM + E5 rows; nonzero automatic from uW + E5 (and from E6 tie + s1F-saturation) |
SHEET6-R1.md:2148:restored (4(a_i-b)HM + 729 S_M^3 (a1-a2)^4 a_i^2 alpha_i W_i^4 = 0;
SHEET6-R1.md:2177:| r1_minsat.ms = leaf_UU + E5(HM) + HM*tH-1, char 0 | GB != [1] NONEMPTY -- core-level saturation does NOT kill the minimal branch (the 13.1 consistency identity is real) |
SHEET6-R1.md:2188:of the UU core (the pre-registered Q0/Q1 object).  Q2 -- the
SHEET6-R1.md:2194:### 18.2 (1,2) branch: core-level saturated verdict (mandates 3b, 2, 5)
SHEET6-R1.md:2211:exactly the content factor the (1,2) core's own row 87 carries
SHEET6-R1.md:2213:sum (9+-5r3)/a_i == 4 != 0: relation E (the (1,2) core's entire UU
SHEET6-R1.md:2224:reading, **the (1,2) branch DIES AT ITS TERMINAL CORE, char-0
SHEET6-R1.md:2247:  tie-conformance before a survival is claimed.
SHEET6-R1.md:2278:| branch | core level (saturated) | depth-84 / ext tier | status |
SHEET6-R1.md:2281:| (1,2) | **DEAD, char 0 + 2p (18.2)** | not needed | DEAD at core (E5-12 port contingency noted) |
SHEET6-R1.md:2282:| (2,3) | chain core queued (sec 11) | -- | untouched this session; same saturation advisory as (2,5) applies to any future ext build |
SHEET6-R1.md:2283:| (2,5) | core NONEMPTY (sec 11) | ext decider running on box01 | advisory 18.3: EMPTY valid as-is; NONEMPTY needs saturated re-run |
SHEET6-R1.md:2292:### 19.0 Pre-registration (banked BEFORE the Q2 runs; 15.6 semantics
SHEET6-R1.md:2298:E) and the free core directions OPEN above a stratum cutoff: free
SHEET6-R1.md:2299:core vars at slot < LCUT are 0, at slot >= LCUT symbolic; LCUT = 1 is
SHEET6-R1.md:2305:(HM restored, W symbolic) + E6 cube tie + s1F*tSAT-1.  Etale radicals
SHEET6-R1.md:2334:before any run is read.
SHEET6-R1.md:2371:### 19.3 RETRACTION of the 18.2 (1,2) core kill (SHEET6-R1-Q2E5.md
SHEET6-R1.md:2387:depth-tier row family for the (1,2) ladder, not a core row).  The
SHEET6-R1.md:2399:RESTATED (1,2) VERDICT: the branch SURVIVES its terminal core under
SHEET6-R1.md:2401:occurs in NO core row -- its saturation is vacuous there, banked
SHEET6-R1.md:2459:msolve headroom; the l8 local attempt cost 14.5 GB before timeout).
SHEET6-R1.md:2490:ledger lines append to runs/r1_q2_runs.log as they finish.  The local GB-resolution cliff sits EXACTLY between stratum
SHEET6-R1.md:2518:| branch | core level (saturated) | depth-84 tier | status |
SHEET6-R1.md:2521:| (1,2) | **ALIVE at core** (19.3 retraction; r1_12sat_corr NONEMPTY char 0 + 2p) | not built (its own per-branch ladder; the k1=1 s1-tie is a series-tier row at pole level 4/42) | 18.2 kill RETRACTED; obligations = 15.3 list |
SHEET6-R1.md:2522:| (2,3) | chain core queued (sec 11) | -- | untouched; 18.3-style saturation advisory binds |
SHEET6-R1.md:2523:| (2,5) | core NONEMPTY (sec 11) | ext decider on box01 | advisory 18.3 unchanged |
SHEET6-R1.md:2534:retrofitted), so their core verdicts land at the same evidence tier
SHEET6-R1.md:2571:### 20.0 Pre-registration + scale inventory (banked BEFORE build)
SHEET6-R1.md:2573:BASE objects (sec 9/11, guard-certified, UNSATURATED): r1_23chain_core
SHEET6-R1.md:2576:and r1_25chain_core (44 eqs = 7 radical + 11 quot + 2 quot-deg +
SHEET6-R1.md:2607:K3), gating emission.  NET: saturated gate = base core VERBATIM +
SHEET6-R1.md:2611:- r1_Xsat.ms (char 0) = base core rows byte-VERBATIM + uW1*W1-1 +
SHEET6-R1.md:2628:ANCHORS (pattern-positive, mandate 4, all PASS required before any
SHEET6-R1.md:2632:k3poly_pow_pattern); value + alignment (deg/monic/lattice n mod 3) +
SHEET6-R1.md:2641:(n -> n+3, lattice-preserving), global sign flip, single-coefficient
SHEET6-R1.md:2643:row's n.  Emission->VExpr closure: FC.guards on the BANKED core files
SHEET6-R1.md:2650:  terminal core mod p (strong evidence); char-0 [1] on r1_Xsat.ms =>
SHEET6-R1.md:2664:ADDITIVE file cases/r1_chain_sat.py (r1_fullcore.py untouched).
SHEET6-R1.md:2686:+ slot).  Both BANKED core .ms files re-certified against the
SHEET6-R1.md:2690:the (2,5) core rows carry NO W-monomials (uW saturation VACUOUS at
SHEET6-R1.md:2691:its core tier -- the W-load enters at ext rungs r >= 4: 70/134 ext
SHEET6-R1.md:2692:rows W-loaded), while the (2,3) core has 66 W-loaded rows (uW
SHEET6-R1.md:2693:BINDING at core).  The uW rows stay in both gates (standing rule);
SHEET6-R1.md:2726:| r1_23sat_p105337 (MAIN, saturated; FIRST-EVER run of the (2,3) core) | TIMEOUT 1200 s / 15.0 GB rss | (see below) |

exec
/bin/zsh -lc "rg -ni \"liouville|x[[:space:]]*d[yY]|f[[:space:]]*d[gG]|closed 1-form|closed one-form|symplectic potential|primitive of|period pairing|residue.*x.*dy|residue.*f.*dg\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 succeeded in 0ms:
./notes.md:289:- 2026-08-07 night 5 (905db83): A3L1 review — ALL FRONTS CONFIRMED, both promoted. CANONICAL BOOK: td<=5 CLOSED (0 survivors, independent of AF2); td=6 = 4 single-pole r9/M2 (thesis-forced entries) + two-pole residue A on the unique rigid template (merged child (6,12,3,2,5)@0, a1/a2=2+sqrt3). Endgame agents launched: (1) lam_root>=1 ledger attack (cuts 8->4), (2) coefficient-level template lift (genome -> edge consistency -> formal candidate or death edge; sizes farm computation if candidate). Errata E1-E9, five proof-level.
./notes.md:330:- 2026-08-12 (book): BOOK(m,td) ENUMERATED (cases/book_enum.py, BOOK-ENUM.md, systems/book/*.json): td=6..14, m=2..floor(td/3), reviewed spec E/T/C'/J'/R/S with the mechanical arsenal inline (MP7 l=0, gcd menu M>=2, kap-window integrality, corrected ZCH case-(III) w-ratio, root w<1, MP9 even-l, St 9.4 root budget). GATE PASS: td=6 m=2 == the promoted record cell-for-cell (unique residue-A IIa (2,3,1) M=2 child (5,3,1/2), R empty). RESULT: 421 cells, 346 killed, 75 survivors = only 22 distinct classes (31 IIa — ALL l=1, M=r, the Theorem-O escape pattern; 33 ZCH — only at w in {4,6} with an integer-ratio partner, first at td=9; 11 family-I — only r>=3, m>=3; 0 ROOT anywhere: every alphabet sits at w>=1, td-uniform root kill). Prime td 7/11/13 panels EMPTY (all entries off-axis b>=2 — the multi-pole shadow of the prime theorem). Largest class: residue-A in 10/18 panels; largest panel m=4 td=12 (21 cells). NEXT: per-cell bash — Prop 8.1(iv) rigid solve + coefficient-vs-ratio match (IIa l=1 family first), suffix engine from child data at budget td-2, r>=3 log-obstruction for family I, M>=2 chain engine for the 27 off-axis entry classes.
./notes.md:331:- 2026-08-12 (bd4baa2): BOOK BASH WORKFLOW launched (22 classes, full arsenal, adversarial votes per kill). If it drains the book: td 6-14 exclusion reduces to residue-A-type coefficient templates only — the program's endgame at every level. Prime td 7/11/13 already FULLY excluded.
./xmodel/grok-eval-20260812.md:28:| 4 | **Theorem A on the depth-3 column of the two-pole support** | Connects the two successful lanes, which have been run in parallel. MATHIEU-REVIEW already has the depth-3 column \(2BE'-(k+1)B'E\). Residue-A is *not* a strip; if that column cannot vanish for the pinned leading forms, the genome is not a polynomial pair. | Take the Newton edges \((126,42)\), \((189,63)\) with root pattern \(p_R=S_R(\eta-c_0)^{126}\); extract the \(x^{k+2}\) bracket column; run the leading-coefficient lemma (MATHIEU §5.1 Step 1). |

exec
/bin/zsh -lc "rg -ni \"Formanek|primitive element|trace form|field trace|norm.*x|different ideal|Dedekind different|discriminant ideal|minimal polynomial of x|C\\(f,g\\)\\(x\\)|birational.*x\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 succeeded in 0ms:
./SHEET6-AF3.md:29:Claim (AF3′): for every F ∈ T_a,pole of a normalized counterexample,
./SHEET6-AF3.md:116:(row 9; ρ = 1/2). A hypothetical carrier is a normalized counterexample of
./SHEET6-AF3.md:177:entry r9 Q=(3,6,5,2,8) of a type-(3,5) normalized counterexample — now
./SHEET6-MULTIPOLE.md:26:(f,g) a normalized counterexample of type (α,β), 2 ≤ α < β, gcd(α,β) = 1 (Not 2.4/St 2.1, pp. 8–9; the type is global, Lemma 2.1 p. 8). T_{a,pole} = {P_1,…,P_m}, m ≥ 2.
./SURPLUS-REVIEW.md:51:  normalization is UNDEFINED at k=1 (both corners have x=1). In the reg
./SIGRAY-AUDIT.md:12:| Not 2.3 | 9 | VERIFIED | Normalized counterexample well-defined; the "from now on" reduction is sound via Lem 2.1. |
./DC2-PROGRAM.md:82:Architecture per ZHEGLOV-SCOPE.md §1: (S2) normal forms A_1 ⊂ D_1 = K[[x]][∂] ⊂ D̂_1^sym,
./DC2-PROGRAM.md:95:| Schur normal form SPS⁻¹ = ∂^p + explicit centralizer | converts [Q,P]=1 into finitely many normal-form coefficients | **BREAKS — first genuine obstruction, see below** |
./DC2-PROGRAM.md:101:Everything in Zheglov's proof after page 1 runs inside normal forms that exist because of
./DC2-PROGRAM.md:133:vertex normalization a_{p0}b_{q0} = ±1 at a unique-decomposition Minkowski vertex,
./DC2-PROGRAM.md:138:Write elements of A_2 normally ordered: P = Σ a_p x^{p'}∂^{p''}, support in ℕ^4. The
./DC2-PROGRAM.md:316:after one normalization — that finiteness is what every known DC(1) argument (Dixmier's
./CROSSCHECK.md:16:  (0,0) coeff unconstrained; torus normalization FIX: P(8,16)=1, Q(12,24)=1.
./CROSSCHECK.md:58:  normalization" Lemma: sets constant terms to 0 AND drops the (0,0) vertex-presence
./SHEET6-TDU-REVIEW.md:91:  arbitrary normalized counterexample; proof (monotone ρ, St 3.10/3.11/
./SHEET6-TDU-REVIEW.md:94:- Prop 8.4 (p. 44): arbitrary normalized counterexample + T_a,pole = {G};
./FACE-ISOLATION.md:111:normalization (x^k at the Minkowski vertex p₀+q₀, unique unimodular decomposition,
./ZHEGLOV-SCOPE.md:9:- **S2 Preliminaries, theory of normal forms** (565–1300, ~735 ln): imports from [A.Z]=Zheglov's generalized Schur theory, [GZ1]=Guo–Zheglov normal forms, Dixmier, Wilson, Sato. Ring tower A_1 ⊂ D_1=K[[x]][∂] ⊂ D̂_1^sym; Schur operator S with SPS⁻¹=∂^p; centralizer C(∂^p) ≅ M_p(K[D^p]), "vector form". Mostly cited, not reproved.
./ZHEGLOV-SCOPE.md:17:**External load-bearing inputs (not reproved here):** [GZ1] (arXiv 2303.10306, Guo–Zheglov normal forms — the whole calculus), [A.Z] (generalized Schur theory), [GGV] (subrectangular reduction of minimal counterexamples), Wilson's theorem, classical Schur–Sato. An error in [GZ1] would sink the paper wholesale.
./ZHEGLOV-SCOPE.md:30:**R4. String-equation correspondence for NON-coprime orders (S5, esp. T:one-to-one-correspondence & inverse, 2620–2790).** Extends A. Schwarz's coprime-order bijection; needed precisely because subrectangular DC-pairs have non-coprime orders. Feeds R:distinguished_coefficient (distinguished coefficient =0, via Newton–Puiseux + Wilson, rank-1). Formal-series existence/uniqueness/normalization arguments; the whole transport of the DC-pair to the Puiseux-series side rests here.
./ZHEGLOV-SCOPE.md:56:- **T3. Machinery on non-vacuous objects**: automorphism pairs (φ(x),φ(∂)) in A_1 and Burchnall–Chaundy rank-1 commuting pairs; compute normal forms to finite order; test L:Q_p tail shape, termination + non-maximal distance (intro's claim), S5 cut/glue roundtrip, distinguished-coefficient=0 (R:distinguished_coefficient). ~10-20 agent-h. Tests R4 + S2 end-to-end where hypotheses are satisfiable.
./SHEET6.md:15:- **(B) Sigray's decorated Eggers–Wall trees** (verbatim, thesis in hand): Abhyankar normal form (§2: Newton polygons in rectangles, fibers with 2 points at infinity); Eggers–Wall tree of Puiseux expansions of f-fiber branches at infinity (§3); extended Abhyankar fundamental theorem + partial order (§4); td and pole orders of g computed from tree data (§5, Props 5.5/5.8); tree structure symbols ↘↗ (§6); finite critical values budget (§7, Cor 7.1); Jacobian-forced number theory linking neighboring vertices (§8, Prop 8.1); §9: decoration Q(F) = (D_F, deg p_F, ν_F, M_F, κ_F(1−π(F))) must propagate along the "characteristic sequence" F₀→…→(0,y) to the root, under Diophantine constraints, with budget Σλ_{F_i} ≤ td−2 (St 9.4) — and no admissible propagation survives for td ≤ 5.
./SHEET6-LT-REVIEW.md:30:  f−a tower normalization / gauge; UNSOLVABLE-scope caveat vs R6; x-side +
./SHEET6-LT-REVIEW.md:186:  independent and agree exactly. No normalization mismatch exists to
./SHEET6-LT-REVIEW.md:357:GO criteria after redesign: (i) tower normalization fixed per 7b (gauge
./SHEET6-CAMPAIGN.md:61:  normalization forbids exactly this. Campaign runs with hypothesis **H3**: "case-IV
./notes.md:137:  vertex normalization a1*b3=1 vs gap-column death ((q0)_x=2) =>
./notes.md:170:  posture: cooperative (engage Helali, Suzuki, GGV; Leiden norms). c1-extract
./MATHIEU.md:125:j < d2).  So on the binomial locus the torus normalization is exact and
./plan-72-108.md:56:  normalize the 2–3 dim torus (x,y,D scalings). Small code, hard to get wrong.
./LEMMA.md:42:i.e. eq #3 is the **vertex normalization**: x² must be attained at the bottom
./LEMMA.md:115:  **corner normalization**: for [P,Q] = x², the valuation of x² selects the
./LEMMA.md:142:  (i) *(vertex normalization)* x^k sits at the Minkowski vertex p₀+q₀ with
./LEMMA.md:184:to 0 against the vertex normalization), while reg_9_24_c3 has (q₀)_x = 1
./REDUCE4-CUT-REVIEW.md:75:  normalization: fixing 2 corner coefficients + the rhs coefficient to 1
./SHEET6-TDUNIFORM.md:38:Setting: (f,g) a normalized counterexample of type (alpha,beta) (Not 2.4
./SHEET6-TDUNIFORM.md:241:normalized counterexample with a single pole vertex (T_a,pole = {F}),
./RECON.md:18:- Tao: no X account activity found; blog post 2026-07-21 (see §4), no follow-up since. Akhil Mathew: no original X posts; quoted in Fortune re "unsettling" pace + a "Leiden Declaration" on AI norms in math circulating (@v_shakthi 2026-08-02). Will Sawin: nothing substantive found. [CONTEXT]
./RECON.md:55:- **Leiden Declaration** (leidendeclaration.ai; Zenodo 20302944; IMU letter 2026-06): Lorentz Center workshop product on AI-in-math norms — human responsibility, tool disclosure, peer review over press-release timelines; ~3,400 signatories, Tao/Scholze/Dijkgraaf featured; Gowers declined and blogged why (gowers.wordpress.com 2026-07-26). [CONTEXT — shapes how we should publish]
./RECON.md:91:- **GGV group (Guccione ×2 / Valqui, + Horruitiner):** **no public response to the counterexample and no new JC preprint** — latest arXiv item is math.GR (2606.05520, June 2026); latest JC-adjacent is Ramirez–Valqui **2506.05697** (June 2025), "The Groebner basis and solution set of a polynomial system related to the Jacobian conjecture" [USABLE-BY-US — closest published precedent for our Gröbner/msolve formulation; check their normalizations against Generator A]. Valqui's PUCP CRIS page (cris.pucp.edu.pe) shows nothing newer. Neither Helali nor Suzuki appears to have contacted them publicly. [CONTEXT]
./SECTION4-AUTOMATION.md:430:| family | (m,n) | deg | cases | ψ-normal (rhs x^k) | pre-ψ (rhs x^0) |
./SHEET6-R1.md:1426:- rnorm memo (rnorm(key,c) is EXACTLY linear in c; key-part cached;
./SHEET6-R1-REVIEW.md:107:mandate satisfied. Normalizations line up exactly (through-factor count
./MONDELLO-CHECK.md:23:- **Vertex normalization (i): HOLDS verbatim.** rhs monomial 1 at Minkowski vertex (1,1) = (1,0)+(0,1), unique decomposition, det = +1, corners saturated (vertex eq a·b = 1).
./MONDELLO-CHECK.md:24:- **Gap condition (ii): FAILS.** In SURPLUS.md normalization this is the cell (k,d2) = (0,1): rhs = x⁰, {p₀,q₀} = {(1,0),(0,1)} so max((p₀)_x,(q₀)_x) = 1 < 2; no gap columns. Also d2 = 1 = the scope-map row with "no extra keys, no obstruction", and the top edges are NOT through the origin (Q straddles the direction line: offsets −1, 5).
./MONDELLO-CHECK.md:30:**Over Q the machinery EMPTIES his data at the M2/gap-kill stage** (pre-block, LEMMA.md §2 step 1 / SURPLUS.md GAP-KILL analogue). Sparse run: 13 keys; after vertex normalization (pivot det((1,0),(0,1)) = +1, odd), the sub-vertex single-monomial keys force a(2,1) = 0 [pivot **+2**], a(4,0) = 0 [pivot **+4**], a(6,2) = 0 [pivot **+6**], then b(7,2) = 0 [pivot **+2**], b(6,1) = b(8,3) = 0 (odd pivots 1, 3): full collapse to the elementary automorphism P = a1x, Q = b0y + b1x⁵. Hull run agrees: strip corners a(2,1), a(6,2) killed by pivots +2, +6; Q-corner b(8,3) then dies; residual = triangular x-axis family (automorphisms). So **no char-≠2 Keller pair realizes these Newton polygons** — his example must live where those pivots die.
./MONDELLO-CHECK.md:37:> **Remark.** The characteristic restrictions in our results are not an artifact of the method. Mondello's plane Keller pair P = x + x²y + x⁴ + x⁶y², Q = y + x⁵ + x⁶y + x⁷y² + x⁸y³ over F₂ (arXiv:2608.02634) has Jacobian determinant 1, sends the three distinct points (0,1), (1,0), (1,1) to a common image, and generates a degree 3 separable field extension, so even the separable Jacobian conjecture fails in characteristic two. Its Newton polygons form a strip pair along the direction (1,1) satisfying our vertex normalization, and in any characteristic other than two our near-origin eliminations, whose pivot constants at this polygon data are the lattice determinants 2, 4, and 6, force the strip corners to vanish and reduce any such pair to an elementary automorphism. In characteristic two every one of these determinants vanishes, the corresponding bracket equations become identically zero, and the strips survive; this is precisely the escape that Mondello's example exploits.
./MONDELLO-CHECK.md:41:- **Not in-regime**: strip pair along d=(1,1) with vertex normalization (i) exact, but cell (k,d2) = (0,1) — outside the proved (2,2) obstruction cell (no gap columns, d2=1, top edges off origin). No contradiction with our char-0 theorems.
./SHEET6-PILOT.md:44:  ⇒ under Λ ≤ 6: β ≤ 6, plus 1 < α < β, gcd(α,β) = 1 (type of normalized counterexample).
./SHEET6-2POLE.md:31:"Proposition 8.4. Let (f,g) be a normalized counterexample of the Jacobian
./AUDIT.md:13:  → torus normalization fix_ones     (lib/jc.py, emit.py emit_normalized)
./SHEET6-H3.md:14:satisfying every printed normalization constraint exists (§5b, r10/M4) —
./SHEET6-H3.md:69:- Lemma 2.1 (pp. 8-9): normalized counterexample (f,g); f^+_{(1,1)} =
./SHEET6-H3.md:177:### 4a. Theorem (H3-psi). Let (f,g) be a normalized counterexample, and let
./SHEET6-LROOT.md:157:normalization (Lemma 2.1(ii)) makes f and g exhaust together on the

exec
/bin/zsh -lc "rg -ni \"Donaldson|unimodular|intersection (matrix|form)|plumbing|negative definite|lattice embedding|signature theorem|Rohlin|Neumann|splice\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 succeeded in 0ms:
./TEMPLATE-ATTACK.md:161:| IIa(2,5,1)M2@w3 | κ̄8, (8,5,1/2) | 3 | 0 | m=2 td10,12,14 | passes the full classical battery (i-sync consistent, valid splice, parity); also the unique w = 3/2 two-jump continuation cell |
./DC2-PROGRAM.md:168:  unit pivots at saturated corners with unimodular slot-dets. New vs. abelian: blocks
./FACE-ISOLATION.md:111:normalization (x^k at the Minkowski vertex p₀+q₀, unique unimodular decomposition,
./SHEET6.md:19:- **Orevkov/Domrina (3,4) were quasi-topological**: splice/Eisenbud–Neumann diagrams of the resolution boundary, homology, intersection form, canonical class K̃ = F*K + B of the branched cover; leaf kills by unimodularity/negative-definiteness/Abhyankar–Moh determinant arithmetic. Case tree at 4: ~19 configurations → 8 final diagrams (Domrina 2000), a few dozen leaves.
./SHEET6-CLASSICAL.md:10:  T1 SPLICE / LINK AT INFINITY:  PASS — edge dets positive, all pinned
./SHEET6-CLASSICAL.md:60:## 1. T1 — Splice diagram / link at infinity
./SHEET6-CLASSICAL.md:67:- (EN-1) [Eisenbud-Neumann, Ann. Math. Studies 110, Thm 11.2] A graph
./SHEET6-CLASSICAL.md:71:- (EN-2) [EN, splice positivity for germs] The splice subtree of a LOCAL
./SHEET6-CLASSICAL.md:75:- (N-3) [Neumann, Invent. math. 98 (1989)] The link at infinity of a
./SHEET6-CLASSICAL.md:76:  reduced algebraic curve is determined by the splice diagram computed
./SHEET6-CLASSICAL.md:86:### 1a. Splice data (engine sec 7)
./notes.md:320:- 2026-08-12: 5 monolith deaths diagnosed (vmem-cap silent kills) — requeued: q2l at 900GB (box01), sat23 at 1850GB (ultramem). Stuck-7 driver DONE (post-processing complete; one rc=124 timeout in tail). NEW AVENUE LAUNCHED: classical kill-test battery on the template (splice/Neumann, A-M semigroup, log-BMY, Jelonek) — four independent topology/combinatorics tests, any one can kill the two-pole configuration outright. Cut-transform review still out.
./notes.md:322:- 2026-08-12 (ad709ae): CLASSICAL BATTERY — the template SURVIVES topology: splice/Neumann PASS (all determinants/multiplicities positive), Jelonek PASS, A-M valuation PASS at poles with ZERO slack (ord f_y = -39 exact match), genus balance closes identically. One new kill (pi_G=4 branch dead). Sobering + significant: four independent classical tests, none contradicts the template — it is topologically a legitimate candidate. log-BMY still open pending B/x resolution tails (the one classical test left). All conclusions transfer to all surviving branch variants.
./SHEET6-2POLE.md:119:   poles; it replaces "splice/linking data" in the Eggers-Wall frame.
./SHEET6-2POLE.md:170:whole case analysis over splice-diagram combinatorics (~19 configurations
./SHEET6-2POLE.md:171:-> 8 final diagrams, killed by unimodularity/negative-definiteness/
./SHEET6-2POLE.md:182:   (3+3 > 5), and DO's td=4 multi-dicritical treatment is splice-diagram
./SHEET6-L1.md:383:   Domrina-Orevkov's splice methods also stopped.
./SURPLUS-REVIEW.md:121:10. Unimodularity: used exactly twice (units from the vertex equation; the
./xmodel/grok-eval-20260812.md:7:Why fragile: it has now survived every *printed* constraint (Theorem O), the full coefficient lift (five independent identities close exactly, including the h2-collapse re-deriving L1c without the ODE), and the classical battery (splice/Seifert identity, Abhyankar–Moh at the poles with **zero slack** \(\operatorname{ord}_t f_y=-39\), Jelonek). Every Groebner “kill” of it has been an artifact (msolve parentheses, \(s_{1F}=0\), unreduced mod-\(p\), vmem-cap). Zero-slack topology plus receding discriminants is the signature of a real formal object, not a near-miss. If it algebraizes, JC2 is false and the exclusion program is hunting a theorem that does not exist.

exec
/bin/zsh -lc "rg -ni \"Alexander polynomial|A.?Campo|monodromy zeta|fibered (link|multilink)|Milnor fiber|spectrum at infinity|spectral number|Steenbrink|vanishing cycle\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 exited 1 in 0ms:
codex
Two sharper issues have emerged from the cross-check: the enumerated “book” appears to omit all off-axis \(M_{\text{entry}}\ge2\) configurations, and two inputs used to derive the book are marked as gaps in the campaign’s own Sigray audit. I’m verifying the exact scope before elevating either to the final top three.
exec
/bin/zsh -lc "rg -n -C 4 \"OFF-AXIS|off-axis|b_i.?≥.?2|b.?≥.?2|prime|fully excluded|entry multiset|27\" BOOK-ENUM.md BOOK-BASH-R2.md SHEET6-DEPTH.md SHEET6-MULTIPOLE.md && rg -n -C 5 \"Prop 5\\.8|5\\.8|St 6\\.2|6\\.2|in particular|GAP|d_H|d.*<.?0\" SIGRAY-AUDIT.md SHEET6-MULTIPOLE.md SHEET6-MP-REVIEW.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
SHEET6-DEPTH.md-15-on-page this session: Def 3.1/3.2, St 3.1–3.2 (p. 10); Def 3.3–3.4,
SHEET6-DEPTH.md-16-Not 3.1–3.2, St 3.3 (p. 11); Not 3.3–3.8, St 3.4–3.6 (pp. 12–13); Not
SHEET6-DEPTH.md-17-3.9–3.11, St 3.7 (p. 13); Prop 3.1, Not 3.12, St 3.8 (p. 14); St 3.9
SHEET6-DEPTH.md-18-(p. 15); St 3.16, Prop 3.2, St 3.17 (pp. 17–18); Prop 5.3(iv)–(v) (p. 25);
SHEET6-DEPTH.md:19:St 5.2, Props 5.5–5.6 (pp. 26–27); Props 5.7–5.8, Def 5.1 (pp. 27–28);
SHEET6-DEPTH.md-20-Prop 8.1 (pp. 39–41); St 8.2/8.4 (pp. 41–42); Not 9.1, St 9.1–9.2 (p. 48);
SHEET6-DEPTH.md-21-Prop 9.2, Prop 9.3 (pp. 50–51); St 9.6 + proof (pp. 51–52). Promoted
SHEET6-DEPTH.md-22-priors: SHEET6-MULTIPOLE.md (MP0–MP9, Theorem O), SHEET6-MP-REVIEW.md
SHEET6-DEPTH.md-23-(esp. §5a/§5c), SHEET6-2POLE.md, SHEET6-L1.md. Engine cross-checked:
--
SHEET6-DEPTH.md-58-entry datum (a_i, b_i, ν_i) of type (α,β) (MP4: Q(P_i) = (a_iα, b_iα, ν_i,
SHEET6-DEPTH.md-59-b_i, a_i(α+β)), St 5.2 + Not 8.1 + St 9.1 pp. 26/39/48). An **M=1 segment**
SHEET6-DEPTH.md-60-is a maximal run F_0 → F_1 → … → F_d of the characteristic sequence
SHEET6-DEPTH.md-61-(Prop 9.2, p. 50) with M ≡ 1, starting at the pole vertex (b_i = 1, forced
SHEET6-DEPTH.md:62:at β-minimal and prime Λ_i by MP4) or at an M=1-emitting merge child, and
SHEET6-DEPTH.md-63-ending at the last vertex before a merge vertex G (r(G) ≥ 2) or before
SHEET6-DEPTH.md-64-(0,y). By MP5, every F_j with j ≥ 1 has reduced pattern a single simple
SHEET6-DEPTH.md-65-ν-orbit: (dp, dq) = (ν_j, n_jν_j + 1), n_j ≥ 1, M = 1, λ = 0.
SHEET6-DEPTH.md-66-
--
SHEET6-MULTIPOLE.md-44-**MP2 (restored kill, general m).** If G\* ≠ (0,y), then **M_F ≠ 1 for every F ∈ U with F ≤ G\*** (trunk and G\* itself). The printed Prop 8.4 proof (pp. 44–45) runs verbatim; the singleton hypothesis is needed only above the last merge.
SHEET6-MULTIPOLE.md-45-
SHEET6-MULTIPOLE.md-46-**MP3 (exact escape set).** The vertices escaping MP2 are exactly {F ∈ U : F > G\*}: ALL strict ancestors of G\* — pre-merge segments, inter-merge segments, and merge vertices above G\*. (Not merely "the first vertex above each merge": the M = 1 contradiction is manufactured only at (0,y), so no per-segment rerun of Prop 8.4 exists.)
SHEET6-MULTIPOLE.md-47-
SHEET6-MULTIPOLE.md:48:**MP4 (entry pin; td- and m-uniform).** At every pole, (deg p_{P_i}, deg p_{g,P_i}) = b_i(α,β) and **M_{P_i} = b_i = deg p_{P_i}/α**. Moreover b_i = 1 (hence M_{P_i} = 1) is FORCED when Λ(P_i) = β (β-minimal pole) and when Λ(P_i) is prime. In particular at the minimal m-pole degree td = mβ, ALL entries have M = 1.
SHEET6-MULTIPOLE.md-49-
SHEET6-MULTIPOLE.md-50-**MP5 (forced M = 1 propagation — the naive analogue is false, maximally).** If M_F = 1 at a pre-merge vertex of C_i (e.g. F = P_i when b_i = 1), then every C_i-vertex from F down to the last pre-merge vertex has reduced pattern a single SIMPLE ν-orbit (dp = ν, dq = nν + 1, n ≥ 1), M = 1, λ = 0, no ray of T_a separating there; the chain arrives at G_i with μ_i = 1. M = 1 likewise propagates down every merge-free segment (Prop 8.3(i)) and through every M = 1-emitting merge.
SHEET6-MULTIPOLE.md-51-
SHEET6-MULTIPOLE.md-52-**MP6 (merge anatomy).** No merge vertex is a pole vertex. At a merge G with at least one arriving μ_e = 1 (automatic for any M = 1-ancestry arrival, since μ_e | M_{H_e} by St 8.4):
--
SHEET6-MULTIPOLE.md-55- (c) **q-shape** [P2]: q = η·rad(p)·Π_{s=1}^{l}(η^ν − b_s^ν) for ν ≥ 2 (η-factor absorbed at ν = 1), all q-roots simple;
SHEET6-MULTIPOLE.md-56- (d) **gcd menu**: dq ≡ 1 (mod ν), hence **gcd(M_G, ν_G) = 1** always; with no 0-chain, **M_G = gcd(Σ_e μ_e, (r+l)ν + 1)**, so M_G | Σ_e μ_e ≤ Σ_e M_{H_e} (subadditivity). All-μ=1 families: **IIa**: (dp,dq) = (rν, (r+l)ν+1), M_G = gcd(rν,(r+l)ν+1) **= gcd(r, lν+1)**; **ZCH** (one chain at the 0-direction): (dp,dq) = ((r−1)ν+1, (r−1+l)ν+1), M_G = gcd((r−1)ν+1, l); **I** (ν = 1): (dp,dq) = (r, r+l), M_G = gcd(r, l). Corollary: outside ZCH, **M_G | r ≤ m**;
SHEET6-MULTIPOLE.md-57- (e) **λ_G = 0**: no northeast direction exists and the l extras carry no tree vertex.
SHEET6-MULTIPOLE.md-58-
SHEET6-MULTIPOLE.md:59:**MP7 (no-resonance kill and jump existence).** l = 0 at an all-M=1 merge forces M_G = 1 (IIa: gcd(r,1)) or is impossible outright (ZCH and ν = 1: q = p forces p′ = const ≠ 0 in (iv), i.e. deg p = 1 — contradiction). Hence an all-M=1 merge either emits M = 1 (cascade continues) or is a **resonant jump**: l ≥ 1 and 2 ≤ M_G ≤ r(G) ≤ m in the non-0-chain families. Consequently: if all entries have M = 1 (forced at td = mβ, or all Λ_i prime, by MP4), then either G\* ≠ (0,y) and at least one resonant jump vertex with the full MP6 anatomy exists at or above G\*, or G\* = (0,y) and the **root merge** itself has the all-μ=1 anatomy at ν = 1 (St 9.2(ii)) with k = 0, l ≥ 1, M = gcd(r,l), and the top-cancellation pin **k_f = (r+l)·l_f**, ψ = r+l−1 in St 9.4.
SHEET6-MULTIPOLE.md-60-
SHEET6-MULTIPOLE.md-61-**MP8 (budget transparency — the obstruction's mechanism).** On the pure M=1 forest {F ∈ U : M ≡ 1 at F and at every U-vertex above F} and at every all-M=1 merge vertex (including jumps): Y(F) = ∅ and λ_F = 0. Itemizing the Euler equality (22) (Prop 7.5, p. 38) for m poles: pole clusters, chain paths, M=1 segments, and μ=1-arrival merges all contribute identically zero rows. Hence **no refinement or re-partition of any printed budget** (St 9.4/9.5 (25)–(26) p. 49, Cor 7.1 p. 39, identity (22)) can charge M=1 pre-merge ancestry even one unit, for any m and any td. The only printed per-pole cost is Λ-mass: td = ΣΛ_i ≥ mβ ≥ 3m (Props 5.7/5.8), i.e. m ≤ td/3.
SHEET6-MULTIPOLE.md-62-
SHEET6-MULTIPOLE.md-63-**MP9 (m = 2, b = (1,1) sharpening; td-uniform).** Both chains are M=1/λ=0 single-simple-orbit to the meet, μ = (1,1).
--
SHEET6-MULTIPOLE.md-86-### D4 (MP4)
SHEET6-MULTIPOLE.md-87-Poles have m_F = 0 (Prop 5.1(i) + Not 5.1/5.2), so the h-family is {g} (Prop 4.2) and M_{P_i} = gcd(deg p_{P_i}, deg p_{g,P_i}) (Not 8.1). St 5.2(i): deg p/deg p_g = α/β at poles, so (deg p, deg p_g) = b_i(α,β) and M_{P_i} = b_i·gcd(α,β) = b_i = deg p_{P_i}/α. (Check: reproduces all 11 rows of table (23), p. 46, and St 9.6's printed M = 2 = gcd(4,6).) β-minimal: Λ(P) = a b αβ/ν (Prop 5.6 (19)) = β forces ν = abα; St 5.2(ii): ν | α ⇒ ab = 1 ⇒ b = 1; ν | β ⇒ abα | β with gcd(α,β) = 1 ⇒ α = 1, contra St 2.1. Prime Λ: case ν | α: Λ = ab(α/ν)β divisible by β ≥ 3, so Λ = β and a = b = α/ν = 1; case ν | β: Λ = abα(β/ν) divisible by α ≥ 2, so Λ = α < β ≤ Λ (Prop 5.7) — empty. Since the type (α,β) is global (Lemma 2.1), this is per-vertex, valid at every td — repairing the Λ = td-dependence of SHEET6-TDUNIFORM §2. ∎
SHEET6-MULTIPOLE.md-88-
SHEET6-MULTIPOLE.md-89-### D5 (MP5)
SHEET6-MULTIPOLE.md:90:Downward induction from an M = 1 pre-merge vertex H, K = H° still pre-merge: (a) St 8.4 (p. 42) at the pair (K, H = K + c): mult(p_K^{red}, c) | M_H = 1 — the chain orbit is simple. (b) St 8.2 (p. 41) at that μ = 1 arrival: deg q_K > deg p_K; then for every root c′ of p_K, deg q·mult(p,c′) ≥ deg q > deg p, so every root is searrow — **no northeast roots exist at K at all**. (c) A non-chain root c′ would give the tree vertex K ∗ εc′ (St 3.18; the 0-root always continues) with, by St 3.9(iii) + St 3.17(i) + Prop 8.1(i) + the St 6.2 computation (p. 29), K ∗ εc′ ∈ Ta& and deg p = i·mult(p^{red}, εc′) ≥ i ≥ 2; Prop 6.8 then manufactures a pole above it **on that branch** — necessarily one of the m poles of T_{a,pole} (this consumes no pole budget, which is why it scales to every m, replacing L1a's m=2-only third-pole counting); that pole's chain visits K through direction c′ (Not 3.3/Prop 3.2), making K a merge vertex — contradiction with K strictly pre-merge. So p_K = single simple ν-orbit, dp = ν. (d) Root law + eta law [P2] (exact order/residue counting on (iv): at a p-root of mult μ, mult(q) = 1 forced; off-p q-roots simple; η-residue b ≡ 1 mod ν): dq = nν + 1, M_K = gcd(ν, nν+1) = 1 — verbatim the thesis's own step in St 9.6's proof (p. 52). (e) λ_K = 0: no direction in Ta% exists (b); the q-extras at non-roots of p have no tree continuation (St 3.18). (f) No ray separates: all full-pattern roots lie in one ν-orbit with a unique continuing representative (St 3.18; Prop 5.6's proof, p. 27). At the merge arrival: St 8.4 at (G_i, H_i) gives μ_i = 1. ∎
SHEET6-MULTIPOLE.md-91-
SHEET6-MULTIPOLE.md-92-### D6 (MP6)
SHEET6-MULTIPOLE.md:93:Merge ≠ pole: an arriving direction has full multiplicity deg p_{H_e} ≥ 2, contradicting Prop 5.3(v) squarefreeness. Let some μ_j = 1. (a) k = 0: exactly the D5(c) manufacture, now read at G — every root of p_G supports, via Prop 6.8's same-branch pole, an incoming chain of one of the m poles; the roots of p_G are precisely the r arriving directions, in distinct ν-orbits (St 3.18: one continuation per orbit). (b) Equal-quotient: deg p_{H_e} = mult(p_G^{full}, c_e) = i·μ_e (St 3.17(i) + Prop 8.1(i): p^{full} = ⊖p^i); with μ_j = 1, i = deg p_{H_j} ≥ 2. (c) q-shape by root/eta laws [P2] as in D5(d). (d) Arithmetic: dq = (r+l)ν + 1 ≡ 1 (mod ν) forces gcd(M_G, ν) = 1 (Prop 8.1(v): M_G = gcd(dp, dq)); with dp = (Σμ_e)ν, any common divisor is coprime to ν hence divides Σμ_e: M_G = gcd(Σμ_e, (r+l)ν+1) | Σμ_e ≤ ΣM_{H_e} (St 8.4). All-μ=1 IIa: d | (r+l)ν+1 ⇒ gcd(d,ν) = 1 ⇒ (d | rν ⇔ d | r), and (r+l)ν+1 ≡ lν+1 (mod d): **gcd(rν,(r+l)ν+1) = gcd(r, lν+1)** exactly (A1's "divides" upgraded to A2/A3's equality; elementary both ways). ZCH: dp = (r−1)ν+1, difference lν, coprimality to ν gives M = gcd((r−1)ν+1, l). ν = 1: q = p·s, M = gcd(r, r+l) = gcd(r,l). (Machine-swept: r ≤ 9, ν ≤ 12, l ≤ 12, mixed μ-vectors; reproduces every recorded engine cell — (2,3,1) → 2; ZCH (2,2,3) → 3; ν=1 (2,l=2) → 2.) (e) λ_G = 0 as in D5(e). ∎
SHEET6-MULTIPOLE.md-94-
SHEET6-MULTIPOLE.md-95-### D7 (MP7)
SHEET6-MULTIPOLE.md-96-l = 0 kills: IIa: M = gcd(r,1) = 1. ZCH/ν=1: l = 0 forces q = p, and (iv) becomes (δ−1+u)pp′ = ⊖p, i.e. p′ = const ≠ 0, i.e. deg p = 1 — below ν+1 resp. 2 ≤ r: impossible. Cascade: Prop 8.3(i) propagates M = 1 down merge-free segments (regular steps, D2); at an M = 1-emitting merge the cascade continues (M_G = 1 known by direct gcd; steps below regular until the next merge). If the cascade reaches G\* with M = 1 and G\* ≠ (0,y), D3 gives the contradiction — so some merge at or above G\* breaks M = 1: a jump, with the D6 anatomy, and (all entries M = 1 ⇒ the FIRST break is an all-μ=1 merge) the resonance l ≥ 1 and 2 ≤ M ≤ r ≤ m outside ZCH. Entry forcing is D4. Root merge: (0,y) ∈ Ta& (d = l_f < k_f = deg p_{(0,y)}, Thm 6.1 read as the Ta&-inequality at π = 0), so D6 applies at (0,y) with ν = 1 (St 9.2(ii)); top-cancellation of (iv) (St 8.2's proof computation, forced since dq ≥ 2, u = 0, δ = l_f/i) gives l_f = i·r/(r+l) and k_f = i·r, hence **k_f = (r+l)·l_f** and ψ = ⌈k_f/l_f⌉ − 1 = r+l−1 (St 9.4). Prop 8.3(iii) fails (r ≥ 2 roots): no M = 1 kill at the root merge. ∎
SHEET6-MULTIPOLE.md-97-
--
SHEET6-MULTIPOLE.md-124----
SHEET6-MULTIPOLE.md-125-
SHEET6-MULTIPOLE.md-126-## 5. The obstruction half, stated precisely
SHEET6-MULTIPOLE.md-127-
SHEET6-MULTIPOLE.md:128:**Theorem O.** No printed-tier argument can prove M_F ≠ 1 on pre-merge segments (it is false: MP5 forces M = 1 there whenever b_i = 1, which is itself forced at td = mβ and at prime Λ_i), and no printed-tier argument can exclude resonant jump vertices: the cell (r,ν,l) = (2,3,1), M = 2 at td = 6, m = 2 solves Prop 8.1(iv) exactly with rigid coefficients (a₁/a₂ = 2±√3), passes Prop 8.1(iv)-(v), St 8.2/8.4, the root/eta laws, all located budget statements (Σλ = 2 ≤ 3 globally, 0 through the merge), and the entry pins — machine-verified (cases/l1_ode_check.py; SHEET6-2POLE §6a full hand-verified exhibit, every datum absolute). The blind spot is structural and r-uniform: the l extra q-orbits are invisible to every printed statement except deg q (SHEET6-L1 §3). Combined with MP8 (spend 0), the residual is irreducible: **MP0–MP9 is the maximal printed-tier kill**, and the multi-pole problem reduces, for each (m, td), to the finite book of resonant jump cells pinned by MP6/MP7 + the equal-quotient law + Prop 9.3's per-edge ratio equations (pp. 50–51), with entries pinned by MP4.
SHEET6-MULTIPOLE.md-129-
SHEET6-MULTIPOLE.md-130----
SHEET6-MULTIPOLE.md-131-
SHEET6-MULTIPOLE.md-132-## 6. Refuted attempts (one line each)
--
SHEET6-MULTIPOLE.md-137-4. **λ_root ≥ 1 transported to m poles** (the LROOT-style 8→4 route): dead — λ = 0 is forced at all-M=1 merges and at the root merge (MP8, generalizing SHEET6-LROOT §2 to all m).
SHEET6-MULTIPOLE.md-138-5. **Non-resonant jump** (M ≥ 2 at a merge with l = 0): impossible — l = 0 forces M = 1 (IIa) or contradicts Prop 8.1(iv) outright (ZCH, ν = 1) (MP7).
SHEET6-MULTIPOLE.md-139-6. **ν = 1 interior jump at m = 2**: dead at all l — even l by the exact log-obstruction (all l, beyond L1b's caps), odd l by M = 1 + MP2; only the η-factor subvariant remains cap-limited (l ≤ 4).
SHEET6-MULTIPOLE.md-140-7. **Killing the jump vertex itself from printed statements**: impossible — the (2,3,1) M = 2 cell is a consistent exhibit solving every located printed constraint (Theorem O).
SHEET6-MULTIPOLE.md:141:8. **Λ = td pin transport** (TDUNIFORM §2 verbatim at multi-pole): fails as stated (Λ(P_i) < td); rescued only by the per-pole β-minimal/prime-Λ argument via the *global* type (MP4/D4).
SHEET6-MULTIPOLE.md-142-
SHEET6-MULTIPOLE.md-143----
SHEET6-MULTIPOLE.md-144-
SHEET6-MULTIPOLE.md-145-## 7. Supplementary kills at A3 tier (quarantined pending recorded adversarial confirmation)
SHEET6-MULTIPOLE.md-146-
SHEET6-MULTIPOLE.md-147-From Theorem MPM (pattern-algebra angle; statement complete in the panel record, votes truncated at synthesis). These sharpen the jump book but are NOT counted in Theorem MP:
SHEET6-MULTIPOLE.md:148:- **Prime-partition kill (P2):** Λ(P_i) prime forces a_i = b_i = 1, β = Λ(P_i), ν_i = α | Λ(P_i) − 1; hence no counterexample has two pole vertices with distinct prime Λ-parts (e.g. two-pole partitions 8 = 3+5, 10 = 3+7, 12 = 5+7 excluded outright), and a prime part p forces p | Λ_j for every other part unless ν_j = p, p | b_jα − 1, Λ_j = a_j b_j α.
SHEET6-MULTIPOLE.md-149-- **RH-lemma kills (P5):** n_q − 1 ≤ D_min for searrow reduced patterns; saturated IIa cells with (lν+1) | r die (e.g. (3,2,1), (4,3,1), (5,4,1)); ν = 1 merges with gcd(r,l) ≥ 2 and (r | l or l | r) die (reproves L1b uniformly, extends to all r; no ν = 1 emission of M ≥ 2 for r ≤ 3); full-M ZCH cells (M = (r−1)ν+1) die; IIa l = 1 exists iff (ν+1) ∤ r, with a rigid one-scale closed form.
SHEET6-MULTIPOLE.md-150-- **OB extension:** cells (3,5,1) M = 3 and (4,7,1) M = 4 solve Prop 8.1(iv) with admissible coefficients (machine-verified per A3) — candidate m = 3, 4 consistent exhibits.
SHEET6-MULTIPOLE.md-151-**Action:** re-referee these three blocks (their derivation exists in the panel record through P2 case analysis; the machine check /tmp/mpm_check.py is session-local and must be rebuilt under cases/).
SHEET6-MULTIPOLE.md-152-
--
SHEET6-MULTIPOLE.md-159-**Concrete next step (ordered, engine-able):**
SHEET6-MULTIPOLE.md-160-1. **Build the r = 3 jump-cell reachability check**: extend cases/l1_ode_check.py + cases/twopole_check.py to r = 3 incoming edges; impose Prop 9.3(a)–(d) per-edge (H1 tier) plus the equal-quotient law and entry pin at the cell (r,ν,l) = (3,5,1), M = 3, in the minimal m = 3 configuration td = 3β. Outcome either way is decisive: a ratio-inconsistency kills the first m ≥ 3 escape cell and gives the template for the whole book; consistency produces the m = 3 exhibit and sharpens Theorem O to m ≥ 3.
SHEET6-MULTIPOLE.md-161-2. **Close the m = 2 root-merge residual at td = 7, 8** (l odd, k_f = (2+l)l_f, both κ̄ < ν) by the reach method of 2POLE §5b phase 3 — the only MP9 clause still td-bounded.
SHEET6-MULTIPOLE.md-162-3. **Run the coefficient-vs-ratio match for the td = 6 cell (2,3,1)**: the exhibit's pinned pattern coefficients against both parents' Prop 9.3 edge data — the single most valuable H1-tier computation, since this cell is the minimal consistent example anchoring the entire obstruction.
SHEET6-MULTIPOLE.md:163:4. **Promote §7**: referee the A3 prime-partition and RH kills; if confirmed, they delete the partitions 8 = 3+5, 10 = 3+7, 12 = 5+7 and all saturated cells from the book before any engine run.
SHEET6-MULTIPOLE.md-164-
SHEET6-MULTIPOLE.md-165----
SHEET6-MULTIPOLE.md-166-
SHEET6-MULTIPOLE.md-167-## 9. Cross-consistency notes (grafting record)
SHEET6-MULTIPOLE.md-168-
SHEET6-MULTIPOLE.md:169:- A1.T2 = A2(4) (restored kill; A2's unique-predecessor argument adopted into D2/D3 as the cleaner single-root justification at (0,y)). A1.T4/T5 = A2(3) = A3.P4 (merge anatomy; independent derivations agree cell-by-cell). A1.T5's "M_G | gcd(r, lν+1)" upgraded to A2/A3's equality (elementary proof in D6d). A1.T6's root pin ψ = r+l−1 ⟷ A2(5R)'s ψ = l+1 at r = 2: consistent. A1.T7 = A2.Prop B (budget transparency; A2 adds the Euler-equality itemization, A1 adds the F\*_P ∈ T_{a,pole} branch argument — both used in D8). A1's G\* = A2's G_last (max ∩C_i). A2(1) prime-Λ pin subsumes A1's β-minimal pin; both in MP4.
SHEET6-MULTIPOLE.md-170-- Escape-set adjudication: A1.T3's correction (ALL strict ancestors of G\* escape) supersedes any "first-vertex-above-merge" phrasing; A2(2)'s "pre-merge segment" forcing and A2.P3's inter-merge propagation condition are compatible refinements.
SHEET6-MULTIPOLE.md-171-- The k = 0 manufacture (D5c/D6a) is the load-bearing novelty in both A1 and A2, derived independently with the same printed chain (St 6.2 computation + St 3.9(iii)/3.17(i)/8.1(i) + Prop 6.8 same-branch); its no-pole-budget character is what makes Theorem MP m-uniform.
SHEET6-MULTIPOLE.md-172-
SHEET6-MULTIPOLE.md-173-## 10. Reproduction
--
BOOK-BASH-R2.md-47-rigid template (c̃ = (9/40)a³ ≠ 0, roots (3±√3)a/4), joining the six
BOOK-BASH-R2.md-48-round-1 IIa survivors. All kills are vertex-local in (fam, r, ν, l) and
BOOK-BASH-R2.md-49-frame-free — no td, m, w, κ̄, or entry datum enters any solve — so each
BOOK-BASH-R2.md-50-single solve kills the class's entire panel set. **No new td becomes
BOOK-BASH-R2.md:51:fully excluded** (td = 7, 11, 13 remain the only ones): residue-A
BOOK-BASH-R2.md-52-IIa(2,3,1)M2@w2 still sits in every non-empty panel and survives, and
BOOK-BASH-R2.md-53-every composite td stays independently blocked by the TDU single-pole
BOOK-BASH-R2.md:54:residual. But the multi-pole book shrinks 62 → 27 live instances, and
BOOK-BASH-R2.md:55:every one of the 27 is now a bashed, rigid template — the unbashed
BOOK-BASH-R2.md-56-category is empty.
BOOK-BASH-R2.md-57-
BOOK-BASH-R2.md-58-## 1. Verdict table
BOOK-BASH-R2.md-59-
--
BOOK-BASH-R2.md-208-    m=3,td=12     10    |     2     |     4     |   4
BOOK-BASH-R2.md-209-    m=4,td=12     21    |     3     |    12     |   6
BOOK-BASH-R2.md-210-    m=2,td=14      7    |     1     |     2     |   4
BOOK-BASH-R2.md-211-    m=3,td=14      8    |     2     |     4     |   2
BOOK-BASH-R2.md:212:    TOTAL         75    |    13     |    35     |  27
BOOK-BASH-R2.md-213-
BOOK-BASH-R2.md-214-Unbashed column: **0 everywhere** — the book is fully adjudicated.
BOOK-BASH-R2.md-215-
BOOK-BASH-R2.md-216-## 5. Per-td exclusion status (combined ledger)
BOOK-BASH-R2.md-217-
BOOK-BASH-R2.md:218:Single-pole ground truth unchanged (SHEET6-TDUNIFORM promoted: prime
BOOK-BASH-R2.md:219:theorem at prime td; composite residual 4/16/16/23/71/48 at
BOOK-BASH-R2.md-220-td = 6/8/9/10/12/14). Multi-pole ground is the book after both rounds:
BOOK-BASH-R2.md-221-
BOOK-BASH-R2.md-222-| td | single-pole residual (TDU) | multi-pole book after R1+R2 | FULLY excluded? |
BOOK-BASH-R2.md-223-|---|---|---|---|
BOOK-BASH-R2.md-224-| 6 | 4 classes | 1 cell: residue-A only | NO |
BOOK-BASH-R2.md:225:| 7 | 0 (prime theorem) | empty | **YES** |
BOOK-BASH-R2.md-226-| 8 | 16 classes | 1 cell: residue-A only | NO |
BOOK-BASH-R2.md-227-| 9 | 16 classes | 2 cells: residue-A ×2 (was 8 — all 6 unbashed cells killed) | NO |
BOOK-BASH-R2.md-228-| 10 | 23 classes | 2 cells: residue-A + IIa(2,5,1)@w3 | NO |
BOOK-BASH-R2.md:229:| 11 | 0 (prime) | empty | **YES** |
BOOK-BASH-R2.md-230-| 12 | 71 classes | 15 cells (was 38): 13 IIa-template + ZCH(2,3,2)@w6 ×2 | NO |
BOOK-BASH-R2.md:231:| 13 | 0 (prime) | empty | **YES** |
BOOK-BASH-R2.md-232-| 14 | 48 classes | 6 cells (was 12): all IIa-template | NO |
BOOK-BASH-R2.md-233-
BOOK-BASH-R2.md-234-## 6. FINAL COMBINED CENSUS (rounds 1+2)
BOOK-BASH-R2.md-235-
--
BOOK-BASH-R2.md-249-engine-verified pending formal per-record review** (R1 ZCH(2,2,3)M3@w4
BOOK-BASH-R2.md-250-×7 — its identical (ν,l) = (2,3) solve is now twice-refereed via the
BOOK-BASH-R2.md-251-round-2 @w6 record and was reproduced cell-for-cell as a mandatory gate
BOOK-BASH-R2.md-252-in every round-2 harness, but the @w4 record itself still carries no
BOOK-BASH-R2.md:253:votes of its own). **SURVIVING: 27 instances in 7 rigid one-scale
BOOK-BASH-R2.md-254-coefficient templates**, every one now bashed through the full
BOOK-BASH-R2.md-255-applicable arsenal:
BOOK-BASH-R2.md-256-
BOOK-BASH-R2.md-257-1. residue-A IIa(2,3,1)M2@w2 — 10 panels (every non-empty panel);
--
BOOK-BASH-R2.md-261-5. IIa(3,5,1)M3@w2 — 3 remaining panels (m=3/m=4 td12, m=3 td14);
BOOK-BASH-R2.md-262-6. IIa(4,7,1)M4@w2 — 1 panel (m=4 td12; 2 OPEN μ=3 tier-2 nodes);
BOOK-BASH-R2.md-263-7. ZCH(2,3,2)M2@w6 — 2 panels (m=2/m=4 td12).
BOOK-BASH-R2.md-264-
BOOK-BASH-R2.md:265:Per-td: **fully excluded td = 7, 11, 13 — unchanged and structurally
BOOK-BASH-R2.md-266-unchangeable by this campaign**, since residue-A survives in every
BOOK-BASH-R2.md-267-non-empty panel and composite td are independently blocked by the TDU
BOOK-BASH-R2.md-268-single-pole residual. Multi-pole-side reductions: td = 6, 8, 9 are now
BOOK-BASH-R2.md-269-each reduced to residue-A alone (td=9 was 8 cells before round 2);
BOOK-BASH-R2.md-270-td = 10 to two IIa templates; td = 12 from 38 to 15 cells; td = 14 from
BOOK-BASH-R2.md-271-12 to 6. **The definitive list of what stands between the campaign and
BOOK-BASH-R2.md:272:td ≤ 14 multi-pole exclusion is exactly the 7 templates above (27
BOOK-BASH-R2.md-273-instances), plus the residual review/perimeter debt**: (i) closure of
BOOK-BASH-R2.md-274-the residue-A template (a1/a2 = 2±√3, b = (2/3)σ, suffix B = (3/2)A)
BOOK-BASH-R2.md-275-via the L1 §7.2 global layer or per-panel E-mechanism ladders — this
BOOK-BASH-R2.md-276-single object blocks every td; (ii) the flagged TEMPLATE-scale lever
--
BOOK-BASH-R2.md-281-printed statement list; (v) banking formal per-record votes on the 7
BOOK-BASH-R2.md-282-R1 ZCH(2,2,3)M3@w4 instances — after the round-2 review pass, the only
BOOK-BASH-R2.md-283-remaining review debt in the entire book; (vi) the inherited
BOOK-BASH-R2.md-284-superset-soundness perimeter (P-realizability untracked, conservative
BOOK-BASH-R2.md:285:join contexts, μ_e ≥ 2 quarantine, off-axis entries outside the M=1
BOOK-BASH-R2.md-286-lemma), relative to which all exclusion claims are stated. Live book
BOOK-BASH-R2.md:287:instances: 75 → 62 (round 1) → **27, all template, none unbashed.**
BOOK-BASH-R2.md-288-
BOOK-BASH-R2.md-289-## 7. Artifacts
BOOK-BASH-R2.md-290-
BOOK-BASH-R2.md-291-Round-2 session artifacts (outside repo, exact int/Fraction arithmetic,
--
BOOK-ENUM.md-13-The reviewed final book is FINITE and SMALL at every (m, td) with
BOOK-ENUM.md-14-td = 6..14, m = 2..⌊td/3⌋: **421 cells enumerated, 346 killed by the
BOOK-ENUM.md-15-inline mechanical arsenal, 75 survivors** across 18 panels (9 panels are
BOOK-ENUM.md-16-EMPTY — every entry off the all-M=1 axis or no entry at all; this includes
BOOK-ENUM.md:17:all of td = 7, 11, 13, the multi-pole shadow of the prime-td theorem:
BOOK-ENUM.md:18:partitions of a prime td always force a prime or β-minimal Λ_i companion
BOOK-ENUM.md:19:whose type admits only b ≥ 2 partners). No ROOT cell survives anywhere:
BOOK-ENUM.md-20-every reachable w-alphabet lies in w ≥ 1 (entry w0 = a(b(α+β)−1)/(bν) > 1
BOOK-ENUM.md-21-and cascades expand while resonant steps never cross 1 in the swept range),
BOOK-ENUM.md-22-so the case-(IV) w < 1 window is empty — the td=6 root-kill argument is
BOOK-ENUM.md-23-td-uniform over the whole sweep. Survivors: 31 IIa, 33 ZCH, 11 family-I
--
BOOK-ENUM.md-31-## 1. Spec-to-code map (cases/book_enum.py)
BOOK-ENUM.md-32-
BOOK-ENUM.md-33-| Layer | Spec (review §6) | Code | Inline kills |
BOOK-ENUM.md-34-|---|---|---|---|
BOOK-ENUM.md:35:| E entries | type (α,β), gcd 1, mβ ≤ td; td = ΣΛ_i, Λ_i ≥ β; per pole (a,b,ν) with q-shape pin; MP4 pin M_i = b_i | `entries`/`pole_options` REUSING `sheet6_campaign.tdu_rows(Λ_i)` filtered to the global type (pin okA/okB inline) | any b_i ≥ 2 ⟹ OFF-AXIS class (counted, banked, not cell-expanded; MP7 hypothesis fails) |
BOOK-ENUM.md-36-| T trees | Σ(r−1) = m−1, r(G) ≤ m, no merge below G* | `set_partitions`/`block_partitions`, recursive branch hierarchies (budget exact by construction) | — |
BOOK-ENUM.md-37-| C′ chains | w0 = a(b(α+β)−1)/(bν); resonant steps Δ \| num(w); cascade w ↦ w(r+l)/(lν+1); d0 ≤ 2·gen+2 | `w0_of`; `w_closure` (verbatim from promoted depth_closure_check.py); `merge_cascade_ws`; d0 recorded per entry-w0 in JSON | M=1 emission only (MP7); I r=2 even-l cascade excluded (log-obstruction); ZCH cascade gated by reach law |
BOOK-ENUM.md-38-| J′ jump cells | κ̄_m ∈ (w, (r+1)w] ∩ ℤ; ν determined per (κ̄_m, l); IIa/ZCH/I gcd menu; joins force equal w; ZCH w-ratio ν_e ≥ 2 | `window_cells`, `child_datum`, `enum_context`, `zch_reachable` | mp7_l0_M1, mp7_l0_impossible, M1_mp2, mp9_nu1_even_l (I r=2), zch_w_ratio; M ≥ 2, gcd(M,ν)=1, M \| r (non-ZCH) asserted |
BOOK-ENUM.md-39-| R root cells | case (IV): w_e = 1 − l_f/i0 < 1 necessary; l odd; St 9.4 ψ = r+l−1 | `enum_root` | root_w_window (W ∩ (0,1) = ∅), root_even_l, root_st94 (l > td−r) |
--
BOOK-ENUM.md-60-## 3. Per-(m, td) census (td = 6..14, m = 2..⌊td/3⌋)
BOOK-ENUM.md-61-
BOOK-ENUM.md-62-    (m,td)  entries b1 off | cells killed surv | kill histogram (l0M1/l0imp/M1/mp9/zchr/rootw)
BOOK-ENUM.md-63-    m=2 td= 6    1   1   0 |   13    12     1 | 1/2/2/2/1/4
BOOK-ENUM.md:64:    m=2 td= 7    1   0   1 |    0     0     0 | (all entries off-axis)
BOOK-ENUM.md-65-    m=2 td= 8    2   1   1 |   15    14     1 | 1/2/2/2/1/6
BOOK-ENUM.md-66-    m=2 td= 9    2   2   0 |   22    18     4 | 1/2/5/2/1/7
BOOK-ENUM.md-67-    m=3 td= 9    1   1   0 |   40    32     8 | 2/4/8/2/2/14
BOOK-ENUM.md:68:    m=2 td=10    5   3   2 |   29    27     2 | 2/4/6/4/3/8
BOOK-ENUM.md:69:    m=3 td=10    1   0   1 |    0     0     0 | (off-axis)
BOOK-ENUM.md:70:    m=2 td=11    2   0   2 |    0     0     0 | (off-axis; prime td)
BOOK-ENUM.md:71:    m=3 td=11    1   0   1 |    0     0     0 | (off-axis; prime td)
BOOK-ENUM.md-72-    m=2 td=12   11   7   4 |   55    42    13 | 3/6/13/7/3/10
BOOK-ENUM.md-73-    m=3 td=12    4   3   1 |   58    48    10 | 3/6/10/5/4/20
BOOK-ENUM.md-74-    m=4 td=12    1   1   0 |   88    67    21 | 4/8/15/5/5/30
BOOK-ENUM.md:75:    m=2 td=13    4   0   4 |    0     0     0 | (off-axis; prime td)
BOOK-ENUM.md:76:    m=3 td=13    2   0   2 |    0     0     0 | (off-axis; prime td)
BOOK-ENUM.md:77:    m=4 td=13    1   0   1 |    0     0     0 | (off-axis; prime td)
BOOK-ENUM.md-78-    m=2 td=14    7   4   3 |   48    41     7 | 3/6/10/7/3/12
BOOK-ENUM.md-79-    m=3 td=14    4   1   3 |   53    45     8 | 2/4/9/2/4/24
BOOK-ENUM.md:80:    m=4 td=14    1   0   1 |    0     0     0 | (off-axis)
BOOK-ENUM.md-81-    TOTAL                  |  421   346    75 |
BOOK-ENUM.md-82-
BOOK-ENUM.md-83-root_even_l / root_st94 never fire (root_w_window kills every root
BOOK-ENUM.md-84-candidate first — no alphabet reaches w < 1). Full per-panel data incl.
BOOK-ENUM.md:85:off-axis entry tags, per-w0 closures W/gen/d0, and complete survivor
BOOK-ENUM.md-86-records: systems/book/book_m{m}_td{td}.json.
BOOK-ENUM.md-87-
BOOK-ENUM.md-88-## 4. Survivor census: 75 instances, 22 distinct cell classes
BOOK-ENUM.md-89-
--
BOOK-ENUM.md-138-   log-obstruction is unproved (MP9 is r=2); a Laurent-residue computation
BOOK-ENUM.md-139-   for C(−n, n−1) at r ≥ 3 could kill (4,1,2)/(4,1,4)/(4,1,8) and
BOOK-ENUM.md-140-   (3,1,3)/(3,1,6) outright. Cap flag inherited: the ν=1 η-factor
BOOK-ENUM.md-141-   subvariant is excluded only for l ≤ 4.
BOOK-ENUM.md:142:5. **Off-axis entry classes** (any b_i ≥ 2; 27 entry multisets across the
BOOK-ENUM.md-143-   sweep, tags banked per panel): outside the closed M=1 lemma — need the
BOOK-ENUM.md-144-   M ≥ 2 chain engine (quarantined mixed merges; MP perimeter). These are
BOOK-ENUM.md:145:   CONFIGURATIONS, not book cells; the prime-td panels are 100% off-axis.
BOOK-ENUM.md-146-
BOOK-ENUM.md-147-## 6. Engine choices and honest perimeter
BOOK-ENUM.md-148-
BOOK-ENUM.md-149-- **Conservative throughout** (the book's promoted stance: superset, never
--
BOOK-ENUM.md-169-  cap); root_even_l/root_st94 are implemented but never fire in the sweep.
BOOK-ENUM.md-170-- **d0 ≤ 2·gen(W)+2** (the promoted DEPTH-REVIEW constant) is recorded per
BOOK-ENUM.md-171-  entry w0 in the JSON (`entry_w0` → W, gen, d0); menu content is
BOOK-ENUM.md-172-  depth-free via §5b, so d0 is metadata, not a cap.
BOOK-ENUM.md:173:- **Off-axis** = any pole with b_i ≥ 2 (entry M = b_i ≥ 2 by MP4): the
BOOK-ENUM.md-174-  chain-depth closure lemma covers only the all-M=1 axis; these multisets
BOOK-ENUM.md-175-  are counted and their tags banked, never cell-expanded. Mixed merges
BOOK-ENUM.md-176-  with μ_e ≥ 2 remain quarantined (MP perimeter).
BOOK-ENUM.md-177-
SHEET6-MP-REVIEW.md-184-self-contradictory as printed (take H = F) — P1's regularity reading (Not
SHEET6-MP-REVIEW.md-185-9.2, p. 48, verbatim) is necessary and correctly flagged, not silently
SHEET6-MP-REVIEW.md-186-assumed; Prop 8.4's proof (pp. 44–45) matches D3 step-for-step (the
SHEET6-MP-REVIEW.md-187-deg = mult line at (0,y) is where 8.3(iii) is load-bearing, as claimed);
SHEET6-MP-REVIEW.md-188-table (23) row 1 (p. 46); Prop 5.6 (19), Prop 5.7's two-case proof, Prop
SHEET6-MP-REVIEW.md:189:5.8 (20) (pp. 27–28) — D4's Λ = abαβ/ν arithmetic and both forcing cases
SHEET6-MP-REVIEW.md-190-re-derived and CONFIRMED; St 5.2 (p. 26); Thm 6.1 (p. 28); Prop 9.2
SHEET6-MP-REVIEW.md-191-(p. 50); Prop 9.3(a)–(m) (pp. 50–51); St 9.6's proof zoo (p. 52) — the
SHEET6-MP-REVIEW.md-192-mult = 1 step D5(d) cites is verbatim ("deg(q) = nν+1 … M_F = 1"), and the
SHEET6-MP-REVIEW.md-193-l = 0 arguments all pass through k ≠ 0 northeast roots, exactly the blind
SHEET6-MP-REVIEW.md-194-spot Theorem O claims.
--
SHEET6-MP-REVIEW.md-254-
SHEET6-MP-REVIEW.md-255-### 5c. The jump-book parameterization, as handed to the enumeration engine
SHEET6-MP-REVIEW.md-256-
SHEET6-MP-REVIEW.md-257-    BOOK(m, td), m ≥ 2, 3m ≤ mβ ≤ td:
SHEET6-MP-REVIEW.md-258-    E. Entry layer (printed; finite): type (α,β), 2 ≤ α < β, gcd = 1,
SHEET6-MP-REVIEW.md:259:       mβ ≤ td; partition td = Σ_{i=1..m} Λ_i, Λ_i ≥ β (Props 5.7/5.8);
SHEET6-MP-REVIEW.md-260-       per pole (a_i, b_i, ν_i): Λ_i = a_i b_i αβ/ν_i, ν_i | α or ν_i | β
SHEET6-MP-REVIEW.md-261-       (St 5.2(ii) + (19)); entry datum Q(P_i) = (D = a_iα, deg p = b_iα,
SHEET6-MP-REVIEW.md-262-       ν_i, M = b_i, κ̄ = a_i(α+β)), λ = 0. b_i = 1 forced if Λ_i = β or
SHEET6-MP-REVIEW.md-263-       Λ_i prime (MP4).
SHEET6-MP-REVIEW.md-264-    T. Tree layer (printed; finite): rooted trees, m leaves, merge
--
SIGRAY-AUDIT.md-1-# SIGRAY-AUDIT.md — Section 2–6 statement audit (thesis pp. 7–30)
SIGRAY-AUDIT.md-2-
SIGRAY-AUDIT.md:3:Source: `/Users/dc/code/math/jc72108/refs/sigray_full.pdf` (printed page = pdf page). Batch: 72 items, Not 2.1 through Prop 6.2. Verdicts cross-checked against the campaign's erratum catalogue E1–E11 + G1–G3 (`SHEET6-CAMPAIGN.md` §7, `SHEET6-LT-REVIEW.md` §6, `SHEET6-AF2.md`, `SHEET6-AF3.md`, `SHEET6-III.md` §5) and against usage in the promoted SHEET6 docs.
SIGRAY-AUDIT.md-4-
SIGRAY-AUDIT.md-5-## 1. Verdict ledger (sorted by thesis page)
SIGRAY-AUDIT.md-6-
SIGRAY-AUDIT.md-7-| id | page | verdict | note |
SIGRAY-AUDIT.md-8-|---|---|---|---|
--
SIGRAY-AUDIT.md-21-| Not 3.2 | 11 | VERIFIED_WITH_NIT | (0,y), (0,x) well-defined single classes; usual "independent of P" remark omitted; nonemptiness of S*_y, S*_x implicit. |
SIGRAY-AUDIT.md-22-| St 3.3 | 11 | VERIFIED_WITH_NIT | Two components re-derived (cross-form O = −1 separates; rays connect each side). Nit: printed S*_{a,x}, S*_{a,y} never defined (stray subscript). |
SIGRAY-AUDIT.md-23-| Def 3.4 | 11 | VERIFIED_WITH_NIT | V_a well-defined and finite; "u = α_{j,P} for some j" must be read j ≥ 1 (forced downstream) — matches campaign's H1-tier reading dependence (LT-REVIEW LR1(a)), deliberately unfiled. |
SIGRAY-AUDIT.md-24-| Not 3.3 | 12 | VERIFIED_WITH_NIT | Edge structure re-derived (u* unique, F°-independence, edges biject with non-root vertices). Nits: forward reference to T_a; edge interval printed backwards (I_P([u,u*]) for I_P([u*,u])). |
SIGRAY-AUDIT.md-25-| Not 3.4 | 12 | VERIFIED | ν_F P-independence PROVED here (not claimed in print; 20000-trial exact sweep) — settles SHEET6-HIII-REVIEW's parenthetical worry negatively: H5a does NOT infect ν_F. |
SIGRAY-AUDIT.md:26:| Not 3.5 | 12 | GAP | κ_F NOT well-defined as printed: explicit two-branch witness gives κ_F = 4 vs 2 at the same vertex. = campaign's standing item H5a (SHEET6-III.md §5, HIII-REVIEW Front 4), documented but NOT E/G-numbered. Forced repair: jump-realization/max (Eggers-Wall) value. |
SIGRAY-AUDIT.md-27-| Not 3.6 | 12 | VERIFIED_WITH_NIT | T_a well-formed; printed "T_{a,y} := T_{a,y} ∩ T_a" is circular — RHS must be the starred components of St 3.3. Cosmetic. |
SIGRAY-AUDIT.md-28-| St 3.4 | 12 | VERIFIED | No proof printed; π(F) ∈ Q re-derived for all three vertex classes (V_{1,a}, V_{2,a}, roots). H5a does not affect it. |
SIGRAY-AUDIT.md-29-| Not 3.7 | 12 | VERIFIED | Suitable κ exist = common multiples of the finitely many pole multiplicities; requires the Not 3.2 reading of forms (3)/(4). |
SIGRAY-AUDIT.md-30-| Not 3.8 | 12 | VERIFIED | Both embedded "independent of P" claims re-derived (thesis: "easy to check"); F*c half needs only n ∈ N (n = 0 allowed). |
SIGRAY-AUDIT.md-31-| St 3.5 | 13 | VERIFIED_WITH_NIT | Re-derived ((F*c)′ = F); hypothesis omits "suitable" for κ; harmless. |
--
SIGRAY-AUDIT.md-42-| St 3.11 | 16 | ERRATUM | NEW (the campaign's own paraphrases silently correct it). Printed (ii)'s first term lacks the prime (should be d_{h,F'}): as printed the first inequality is vacuous and the equality-propagation clause is FALSE (explicit counterexample, verified). Corrected version fully re-derived. (i) and the upper bound of (ii) true as printed. |
SIGRAY-AUDIT.md-43-| Not 3.13 | 16 | VERIFIED_WITH_NIT | Load-bearing slip: p_F, d_F must be read p_{f−a,F}, d_{f−a,F} (literal h = f empties T_a⁻ and falsifies St 3.13). Campaign already adopts this reading (SHEET6-H3.md). |
SIGRAY-AUDIT.md-44-| St 3.12 | 16 | ERRATUM | NEW. Print (600 dpi confirmed) shows the SAME identity twice — no (0,x)/(1,0) clause; even one instance false under the printed chart naming. Corrected: h⁺_{(0,y)} = h⁺_{(1,0)}, h⁺_{(0,x)} = h⁺_{(0,1)}. Consequence inequalities TRUE. SHEET6-H3.md §2a's "verbatim" quote silently corrects the print — filing amendment needed. |
SIGRAY-AUDIT.md-45-| St 3.13 | 16 | ERRATUM | NEW (E12-candidate). FALSE as printed for a ≠ 0: d_{f,I(u)} freezes at 0 past the crossing (exact counterexample f = xy, a = 1) — uniqueness fails. TRUE with d_{f−a}: unique zero re-derived. Root cause = Not 3.13 slip; same one-token repair fixes Not 3.14, St 3.14, St 3.15's hypothesis. Campaign silently uses corrected reading (SHEET6-LROOT.md). |
SIGRAY-AUDIT.md-46-| Not 3.14 | 16 | VERIFIED_WITH_NIT | Trichotomy trivially a partition; inherits the Not 3.13 slip — printed reading gives T_a⁻ = ∅ and an infinite T⁰ tail, breaking Not 7.1/Prop 7.5 downstream; corrected reading is the one actually used. |
SIGRAY-AUDIT.md:47:| St 3.14 | 16–17 | GAP | (a) Printed reading false for a ≠ 0 (d_{f−a} repair mandatory). (b) Under the repair, all steps re-derived except (ii): "η_F = η_G" assumes the per-fiber Ω picks aligned continuations; can fail up to a root-of-unity conjugation twist for κ > 1. Repair: weaken (ii) up to twist (preserves d, deg, root multiplicities — all the campaign uses) or strengthen St 3.2. NEW. |
SIGRAY-AUDIT.md-48-| St 3.15 | 17 | KNOWN_ERRATUM | = E10 (labels (i)/(iii) swapped), independently reconfirmed with exact witnesses; multiplicity clause verified modulo the swap; d_{h,H} typo. ADDITION to the filing: the hypothesis's p_F must also read p_{f−a,F} (Not 3.13 slip), else vacuous/false for deep F on fibers a ≠ 0. |
SIGRAY-AUDIT.md-49-| St 3.16 | 17 | VERIFIED_WITH_NIT | No proof printed; both halves (vertex iff >1 root; η^ν root pattern) re-derived + exact confirmation. Same Not 3.13 p_{f−a} reading dependence (uncatalogued). |
SIGRAY-AUDIT.md-50-| Prop 3.2 | 18 | VERIFIED | No proof printed; existence/uniqueness/κ-independence of F = G + c re-derived, incl. unstated P-independence of c. |
SIGRAY-AUDIT.md-51-| St 3.17 | 18 | VERIFIED_WITH_NIT | (i)/(ii) re-derived (vertex-free segment argument + St 3.9 iteration) + exact confirmation. Nits: "π_G" undefined notation; p_{f−a} reading dependence. |
SIGRAY-AUDIT.md-52-| St 3.18 | 18 | ERRATUM | NEW. Conclusion prints "…unique ν_F-th root of unity, ε such that F * c exists" — ε never occurs in the conclusion; literally false whenever ν_F ≥ 2. Corrected "F * (εc) exists" re-derived TRUE (uniqueness leans on St 3.2's coherent Ω). SHEET6-A2P-REVIEW quotes the corrected form as "verbatim" — uncatalogued; campaign usage is of the corrected form throughout. |
SIGRAY-AUDIT.md-53-| Prop 4.1 | 18 | VERIFIED_WITH_NIT | Chain-rule identity and (8) dichotomy re-derived (numeric check passed). Nits: undefined "T_{κ,a}"; p_k-for-p_l display slip; hypothesis (7) not load-bearing for 4.1 itself. |
SIGRAY-AUDIT.md:54:| Prop 4.2 | 19 | GAP | NEW. All printed formulas re-derive exactly ((9), (10), δ-descent, uniqueness), but "since h_j is non-constant, l_j ≠ 0" conflates h_j with its leading part: if h⁺_{j,F} ∈ C* (finite nonzero asymptotic value — live for a non-proper Keller pair) the tower is stuck (l_j = 0 ∉ N*). The Remark "(7) automatic when d_F > 0" is circular. Repairs identified (constant-shift steps, or prove the (7)-analogue). Nil impact on all concrete campaign towers (nonconstant tops). Off-by-one N*^{m−1} tuple tags; stray ",b". |
SIGRAY-AUDIT.md-55-| Prop 4.3 | 20–21 | VERIFIED_WITH_NIT | NO proof printed; full analogue proof reconstructed and CLOSES ((7) excludes 4.2's stuck corner at j = 0; strict negativity closes j ≥ 1) — explains why (7) is hypothesized here and 4.2's missing analogue is exactly its gap. (iv)'s (f⁺_F)^μ vs (f−a)⁺_F reconciled: T_a⁻ ≠ ∅ forces a = 0. |
SIGRAY-AUDIT.md-56-| Not 4.1 | 21 | VERIFIED_WITH_NIT | Well-defined via 4.2's uniqueness; ⪯ is a PREORDER, not partial order (antisymmetry fails) — downstream uses need only the preorder. Stray parenthesis typo. |
SIGRAY-AUDIT.md-57-| Not 4.2 | 21 | VERIFIED_WITH_NIT | Well-posed via 4.3; dropped b-subscripts in the strict clause; duplicated "b ∈ C"; inherited off-by-one dimension tags; "preorder" not "partial order". |
SIGRAY-AUDIT.md-58-| Prop 4.4 | 21–22 | VERIFIED_WITH_NIT | Proof re-derived link-by-link (T_a⁺ chain, T_a⁻ λ-interpolation) — sound. Nits: F′ never defined in the statement (= tree parent); "any F, F′ ∈ T_a⁻" overstates what is proved (neighbour version + chaining suffices for all downstream uses); minor citation/notation slips. |
SIGRAY-AUDIT.md-59-| Prop 4.5 | 22–23 | VERIFIED_WITH_NIT | Proof reconstructed; rests on Lem 2.1(i)'s rectangle/corner property of the fixed normalized f — load-bearing but unstated. Print: missing ⁺ superscript in hypothesis; relies on St 3.12 whose print is garbled (see St 3.12 erratum). |
SIGRAY-AUDIT.md-60-| Prop 4.6 | 23 | VERIFIED_WITH_NIT | No proof printed; (11)–(17) fully re-derived + machine-verified (295-trial exact sweep); the (12) "<" vs (15) ">" sign asymmetry confirmed correct. Nits: "Set F = T_a⁺ ∪ T_a⁻" misprints ∈; T_a⁻ case rests on 4.3(iv) not "(10)". |
SIGRAY-AUDIT.md:61:| Prop 5.1 | 23–24 | GAP | NEW (beyond catalogued cosmetic E8 cite-slip, reconfirmed). Monotone-ρ argument sound at punctures with g(P) ∈ {0, ∞}, but at g(P) ∈ C* the printed b = 0 reading breaks: (7) fails, m undefined, ρ_0 never vanishes — no threshold u exists. Corrected with forced b = g(P) (thesis's own §7 corroborates); campaign's pole-vertex uses (b = 0) unaffected. |
SIGRAY-AUDIT.md-62-| Prop 5.2 | 24 | KNOWN_ERRATUM | = E10 casualty exactly as filed (LT-REVIEW §6 FILING FIX 1): statement TRUE, printed proof's last inference only reads correctly under the erroneous St 3.15 labels. Repair re-derived here inside the printed apparatus. |
SIGRAY-AUDIT.md-63-| Not 5.1 | 24 | VERIFIED_WITH_NIT | Threshold uniqueness re-derived unconditionally; existence inherits Prop 5.1's b = 0 gap (F*_P undefined at g(P) ∈ C* punctures under the printed reading); unconditional for g-poles — the only campaign use. |
SIGRAY-AUDIT.md-64-| St 5.1 | 24 | VERIFIED_WITH_NIT | Proof re-derived both directions; k/l vs l/k letter-shuffle in the displayed ratio (harmless); only T_a⁺ vertices invoked, so the 5.1 gap never bites. |
SIGRAY-AUDIT.md-65-| Not 5.2 | 25 | VERIFIED | T_{a,pole} well-defined; threshold uniqueness re-derived; cut with T_a⁺ meaningful. |
SIGRAY-AUDIT.md-66-| Prop 5.3 | 25–26 | ERRATUM | NEW statement-level: (ii) and (viii) ratios INVERTED — printed d_{g,F} = (k_f/k_g)d_F, correct (k_g/k_f)d_F = (β/α)d_F; proof has a second distinct slip (k_f/l_f). Forced by 4.6(11), St 5.2(i), Prop 5.7, table (23). All NINE properties re-derived TRUE after correction. Campaign (TDUNIFORM R1) silently uses corrected direction; A3L1-REVIEW:61 quotes the print unflagged. Secondary: (vii) never actually derived in print; (vi) missing ",c". |
SIGRAY-AUDIT.md:67:| Prop 5.4 | 26 | GAP | NEW. Statement TRUE (verified by exact null-space computation on three patterns) but the printed proof never proves the q-half (η^ν-class structure of p_{g,F}; "0 is a root of q" in case (i) nowhere argued). Complete repair supplied and verified; load-bears on α ≥ 2 (St 2.1) — for α = 1 genuine counterexample solutions exist. |
SIGRAY-AUDIT.md-68-| Not 5.3 | 26 | VERIFIED | Q-datum well-defined on T_{a,pole}: κ_F supplied by 5.3(iv), integrality by St 3.8, positivity by T_a⁺ + 5.3(ii) (unaffected by the 5.3 ratio erratum). |
SIGRAY-AUDIT.md-69-| St 5.2 | 26 | VERIFIED_WITH_NIT | (i)/(ii) re-derived + 2988-tuple exact sweep, no violation. Consistent ONLY with corrected 5.3(ii)/(viii) — independent corroboration of that new erratum. |
SIGRAY-AUDIT.md-70-| Prop 5.5 | 26 | ERRATUM | NEW proof-level: all three case conclusions drop g-subscripts (case (ii, c ≠ 0) as printed literally contradicts (18)); dangling "Statement 18" citation (same class as E8). Boxed statement (18) re-derived TRUE; the iff direction needs E10-corrected St 3.15 (known co-dependence, already listed in LT-REVIEW). Corrected proof closes in full. |
SIGRAY-AUDIT.md-71-| Prop 5.6 | 27 | VERIFIED_WITH_NIT | (19) re-derived exactly in all three root-pattern cases (orbit arithmetic exhaustively swept). One-line printed proof silently needs 5.3(v)/(ix) (simplicity; one puncture per continuation). |
SIGRAY-AUDIT.md-72-| Prop 5.7 | 27 | VERIFIED | Λ ≥ β re-derived with the missing a,b-scaling supplied; ν_F < deg p_F needs 5.3(iv); sweep confirms bound tight (table (23) rows r5, r10). |
SIGRAY-AUDIT.md-73-| Def 5.1 | 28 | VERIFIED | Generic preimage count well-posed; Keller condition forces dominance and multiplicity 1, so td ∈ N*. |
SIGRAY-AUDIT.md:74:| Prop 5.8 | 28 | GAP | NEW. NO proof printed for (20) (text goes straight to §6). Re-derivation succeeds for all but finitely many a; the printed strength "for ANY a ∈ C" needs an unwritten a-uniformity argument (repair route: St 3.14 transport + ν_F-invariance under M_{a,b}, the latter unproven). Campaign applies (20) at fixed dicritical fibers (LROOT "δ_a = 0 for EVERY fiber"); TDUNIFORM/TDU-REVIEW treat 5.8 as trust-perimeter without noting the missing proof. |
SIGRAY-AUDIT.md-75-| Prop 6.1 | 28 | VERIFIED_WITH_NIT | Indirect proof re-derived ((16) ⟺ (17) under the hypothesis, contradicting 4.6's exclusivity; 2000-trial check). Literal broken "Notation ??" reference; T_a⁻ half tacitly needs Prop 4.3. |
SIGRAY-AUDIT.md-76-| Thm 6.1 | 28 | VERIFIED_WITH_NIT | l_f < k_f re-derived (Lem 2.1(iii) + Prop 6.1 at the root). Nits: systematic chart-naming inconsistency (operative convention vs literal Not 3.2 chain — conclusion invariant); flags the St 3.12 duplicated-identity print typo. |
SIGRAY-AUDIT.md-77-| Not 6.1 | 29 | VERIFIED | T↗/T↘ well-posed, disjoint, exhaust T_a⁺ by Prop 6.1; transcription exact. |
SIGRAY-AUDIT.md-78-| St 6.1 | 29 | VERIFIED | One-line proof sound; Prop 6.1's dichotomy independently re-checked in both branches. |
SIGRAY-AUDIT.md:79:| St 6.2 | 29 | GAP | NEW. The iff re-derived exactly. The "in particular" clause (unproven in print) does NOT follow as stated: H ∈ T_a⁺ — required for H ∈ T↘ — is not implied (explicit abstract counterconfiguration with d_H < 0). Corrected statement: add H ∈ V_a ∩ T_a⁺ or weaken to the inequality. Potentially load-bearing for St 9.6–9.9's regularity contrapositive. Distinct from E5. |
SIGRAY-AUDIT.md:80:| Prop 6.2 | 29–30 | ERRATUM | NEW. Hypothesis F/G swap: printed side conditions (i) G ∈ T_a⁻ / (ii) F ∈ T_a⁺ are the exact mirror of what Prop 4.4 needs; mixed-sign case admitted and the proof breaks in three places (exact witness). Corrected (i′) F ∈ T_a⁻ / (ii′) G ∈ T_a⁺: entire proof re-derived + 300k/82k-trial exact sweeps, 0 failures. Same family as E10. Thesis's only citation (Prop 6.3, G ∈ T↘ branch) satisfies (ii′) — downstream unaffected. Two benign /κ display drops also noted. |
SIGRAY-AUDIT.md-81-
SIGRAY-AUDIT.md-82-## 2. Summary
SIGRAY-AUDIT.md-83-
SIGRAY-AUDIT.md:84:Of the 72 items audited (thesis pp. 7–30, Not 2.1 → Prop 6.2): **21 VERIFIED, 33 VERIFIED_WITH_NIT, 9 ERRATUM, 2 KNOWN_ERRATUM, 7 GAP**. Cross-check against the campaign catalogue (SHEET6-CAMPAIGN.md §7 = E1–E4 + G1–G3; E5 in SHEET6-III.md; E6–E7 in SHEET6-AF2.md; E8–E9 in SHEET6-AF3.md; E10–E11 in SHEET6-LT-REVIEW.md §6): E1–E7, E9, E11 and G1–G3 all concern §9/assembly (pp. 42–60) and do not touch this batch; the only catalogued items in scope are **E8** (Prop 5.1's cosmetic "Proposition 8" cite-slip — reconfirmed as filed) and **E10** (St 3.15 label swap — independently reconfirmed with exact witnesses; its casualty Prop 5.2 matches LT-REVIEW's FILING FIX 1 exactly). Accordingly, the two KNOWN_ERRATUM verdicts (St 3.15, Prop 5.2) are the catalogue's E10 items, while **all 9 ERRATUM verdicts are NEW**: St 3.7 (missing κπ(F) ∈ N hypothesis in (5)), St 3.8 (D ∈ Z falsified by Not 3.5's P-presentation — this upgrades the campaign's standing H5a convention to printed-statement-forced), St 3.11 (missing prime in (ii) + false equality-propagation clause), St 3.12 (duplicated identity, no (0,x) clause), St 3.13 (false for a ≠ 0; Not 3.13's p_{f−a} slip; recommended E12-candidate), St 3.18 (ε dropped from the unique-continuation conclusion), Prop 5.3 (ratio inverted in (ii)/(viii)), Prop 5.5 (proof-level g-subscript drops + "Statement 18" dangler), and Prop 6.2 (hypothesis F/G swap, same family as E10). Of the 7 GAP verdicts, one is the campaign's known-but-unnumbered **H5a** (Not 3.5 ambiguity, SHEET6-III.md §5 / SHEET6-HIII-REVIEW.md Front 4); the other six are NEW: St 3.14 (cross-fiber Ω alignment/conjugation twist in (ii)), Prop 4.2 (l_j ≠ 0 inference fails at constant-leading-part vertices; the "(7) automatic" Remark is circular), Prop 5.1 (b = 0 argument breaks at g(P) ∈ C* punctures — beyond the catalogued cosmetic E8), Prop 5.4 (q-half of the η^ν-structure never proved; verified repair supplied), Prop 5.8 (no proof printed; the "for ANY a" strength needs an unwritten a-uniformity argument), and St 6.2 (the "in particular" clause needs an H ∈ T_a⁺ hypothesis). A recurring uncatalogued slip family — Not 3.13's p_F/d_F must read p_{f−a,F}/d_{f−a,F} — drives the St 3.13 erratum and riders on Not 3.14, St 3.14, St 3.15 (hypothesis), and St 3.16; the campaign already computes with the corrected reading throughout. Three filing fixes are owed independently of new numbering: SHEET6-H3.md §2a (St 3.12) and SHEET6-A2P-REVIEW.md (St 3.18) present silently corrected text as "verbatim" quotes, and SHEET6-A3L1-REVIEW.md quotes Prop 5.3(ii)'s inverted ratio unflagged.
SIGRAY-AUDIT.md-85-
SIGRAY-AUDIT.md-86-## 3. Load-bearing risk
SIGRAY-AUDIT.md-87-
SIGRAY-AUDIT.md:88:Every ERRATUM/GAP/KNOWN_ERRATUM item is inside the campaign's trust perimeter (SHEET6-TEMPLATE.md §6 lists "Prop 3.1, St 3.7–3.18, Prop 4.1–4.6, Prop 5.1–5.8" wholesale). Grep-verified usage by promoted results, ordered by residual risk:
SIGRAY-AUDIT.md-89-
SIGRAY-AUDIT.md-90-**Tier 1 — unproven strength actually consumed by promoted results:**
SIGRAY-AUDIT.md:91:- **Prop 5.8 (20) [GAP]** — the enumeration bedrock: td = ΣΛ over pole vertices is the entry point of the whole td = 6 case table (SHEET6-CAMPAIGN.md §0a/§1/§5, G1's adopted reading is "under (20) as printed"), TDUNIFORM (R3) and the prime theorem, L1, 2POLE. Critically, SHEET6-LROOT.md (PROMOTED) uses "(20) already allocates ALL td units of pole mass to T_{a,pole}" for pole purity and claims δ_a = 0 "for EVERY fiber" — exactly the any-a strength whose proof is missing. Highest-priority repair item (route: St 3.14 transport + ν_F-invariance under M_{a,b}).
SIGRAY-AUDIT.md:92:- **Not 3.5 / H5a [GAP] + St 3.8 [ERRATUM]** — the κ_F convention feeds Not 3.11, Not 5.3's Q-data, Prop 9.3, and the E5-corrected λ-bound engine; SHEET6-III.md's promoted tails closure (10 of 13) is explicitly conditional on H5a/H5b. The St 3.8 finding is favorable: it forces the H5a reading from the printed text, converting a standing hypothesis into a theorem-level constraint — ledger should record the upgrade. D-integrality (St 3.8, corrected) also underpins Prop 5.7 and every integer Q-datum in the §9 tables.
SIGRAY-AUDIT.md:93:- **Prop 5.4 [GAP]** — its (i)/(ii) η^ν-patterns are the source of St 5.2(ii)'s ν-menu, used verbatim by TDUNIFORM (R2) (PROMOTED prime theorem) and AF3's parity pin (PROMOTED, A3L1-REVIEW confirmed). The q-half those results consume is exactly the unproven half; the verified repair in this audit (using α ≥ 2) should be banked as the supporting derivation.
SIGRAY-AUDIT.md:94:- **St 6.2 [GAP]** — the climb/regularity workhorse: AF2's (R2) climb, III's regularity step, A2P-REVIEW's (R2) iff, and the campaign's St 9.6–9.9 propagation analogues use the "in particular" clause contrapositively with regularity. A2P-REVIEW already tracks the standing hypothesis (F, G ∈ V_a ∩ T_a⁺) — the missing H ∈ T_a⁺ hypothesis should be added wherever the clause is invoked; a deep child with d_H ≤ 0 and large multiplicity would evade regularity as printed.
SIGRAY-AUDIT.md-95-
SIGRAY-AUDIT.md-96-**Tier 2 — load-bearing, but campaign already computes with the corrected form (filing fixes only):**
SIGRAY-AUDIT.md-97-- **St 3.18 [ERRATUM]** — root ↔ direction correspondence with unique-ε continuation is core to direction pricing: III (S1/S2 c = 0 forcing), L1 (one-continuation-per-orbit exclusions), AF2 (R1), TDUNIFORM (unpriced q-orbits), A2P-REVIEW. All uses are of the corrected "F*(εc)" form; A2P-REVIEW's "verbatim" label must be fixed when filing.
SIGRAY-AUDIT.md-98-- **St 3.15 = E10 [KNOWN_ERRATUM]** — value dichotomy used by LROOT's pole purity ("St 3.15 with corrected labels, E10"), Prop 5.5/5.6's (18)/(19), A3L1/A2P. Already catalogued; add the p_{f−a} hypothesis rider found here.
SIGRAY-AUDIT.md-99-- **Prop 5.3 [ERRATUM]** — (v)/(vi)/(ix) drive LROOT pole purity, AF3's pattern layer, 2POLE, L1; the inverted (ii)/(viii) ratio is silently corrected in TDUNIFORM (R1). File the erratum + flag A3L1-REVIEW:61.
--
SIGRAY-AUDIT.md-101-- **St 3.12 [ERRATUM]** — used by Thm 6.1, Prop 4.5, LROOT root data, and H3's mult/deg transport (the promoted H3 root-kill). Consequence inequalities true; H3.md §2a's "verbatim" quote must be amended.
SIGRAY-AUDIT.md-102-- **St 3.13 + Not 3.13/3.14 slip family [ERRATUM]** — LROOT (PROMOTED) places cv vertices at "the unique (St 3.13) d = 0 point" under the corrected d_{f−a} reading it already uses; file as E12 so the reading is on the ledger rather than folklore.
SIGRAY-AUDIT.md-103-- **St 3.11 [ERRATUM]** — heavily used (R6 echo kills, TEMPLATE's 16 ≤ 7 kill, LT-REVIEW:132, R1-Q2E5), but exclusively clause (i) and the upper bound of (ii), both true as printed; the erratum (missing prime + equality clause) is outside every campaign use.
SIGRAY-AUDIT.md-104-
SIGRAY-AUDIT.md-105-**Tier 3 — used, failure mode outside campaign usage (verify-on-use guards recommended):**
SIGRAY-AUDIT.md:106:- **Prop 4.2 [GAP]** — towers are everywhere (R1's g² − s₀f³ tower per LT-REVIEW front 7 redesign, TEMPLATE, R6's (1,l)-tails, L1, TDUNIFORM); the stuck corner (h⁺_j ∈ C*) is unreachable in every concrete campaign tower (pole vertices, m = 0, nonconstant tops), but any future use of 4.2 at vertices where g has a finite nonzero asymptotic value must first exclude the degenerate shape.
SIGRAY-AUDIT.md:107:- **Prop 5.1 / Not 5.1 [GAP]** — T_{a,pole} existence machinery used by AF3, A3L1, TDUNIFORM entry, CAMPAIGN; all uses are at g-poles where b = 0 is valid; the g(P) ∈ C* gap is dormant. E8 stays as filed.
SIGRAY-AUDIT.md:108:- **St 3.14 [GAP]** — used by LT-REVIEW (Prop 7.3's pattern-preservation mechanism) and as the natural Prop 5.8 repair route; the conjugation-twist gap preserves d, deg, and root multiplicities — everything those uses need — but the twist must be carried explicitly if (ii) is ever used for exact leading coefficients across fibers.
SIGRAY-AUDIT.md-109-- **Prop 5.2 [KNOWN_ERRATUM]** — LROOT cites its no-pole conclusion inside the E10 discussion with corrected labels; statement true, repair re-derived; no action beyond the existing FILING FIX 1.
SIGRAY-AUDIT.md:110:- **Prop 6.2 [ERRATUM]** — L1 (PROMOTED) uses "(14) = the root law" only via Prop 6.3, whose branch satisfies the corrected (ii′); condition (i) is never invoked anywhere in thesis or campaign. File the swap; no downstream damage.
SIGRAY-AUDIT.md-111-- **St 3.7 [ERRATUM]** — appears only in TEMPLATE's trust-perimeter listing; every actual use imposes κπ(F) ∈ N, which is precisely the missing hypothesis. Benign; file for completeness.
--
SHEET6-MULTIPOLE.md-56- (d) **gcd menu**: dq ≡ 1 (mod ν), hence **gcd(M_G, ν_G) = 1** always; with no 0-chain, **M_G = gcd(Σ_e μ_e, (r+l)ν + 1)**, so M_G | Σ_e μ_e ≤ Σ_e M_{H_e} (subadditivity). All-μ=1 families: **IIa**: (dp,dq) = (rν, (r+l)ν+1), M_G = gcd(rν,(r+l)ν+1) **= gcd(r, lν+1)**; **ZCH** (one chain at the 0-direction): (dp,dq) = ((r−1)ν+1, (r−1+l)ν+1), M_G = gcd((r−1)ν+1, l); **I** (ν = 1): (dp,dq) = (r, r+l), M_G = gcd(r, l). Corollary: outside ZCH, **M_G | r ≤ m**;
SHEET6-MULTIPOLE.md-57- (e) **λ_G = 0**: no northeast direction exists and the l extras carry no tree vertex.
SHEET6-MULTIPOLE.md-58-
SHEET6-MULTIPOLE.md-59-**MP7 (no-resonance kill and jump existence).** l = 0 at an all-M=1 merge forces M_G = 1 (IIa: gcd(r,1)) or is impossible outright (ZCH and ν = 1: q = p forces p′ = const ≠ 0 in (iv), i.e. deg p = 1 — contradiction). Hence an all-M=1 merge either emits M = 1 (cascade continues) or is a **resonant jump**: l ≥ 1 and 2 ≤ M_G ≤ r(G) ≤ m in the non-0-chain families. Consequently: if all entries have M = 1 (forced at td = mβ, or all Λ_i prime, by MP4), then either G\* ≠ (0,y) and at least one resonant jump vertex with the full MP6 anatomy exists at or above G\*, or G\* = (0,y) and the **root merge** itself has the all-μ=1 anatomy at ν = 1 (St 9.2(ii)) with k = 0, l ≥ 1, M = gcd(r,l), and the top-cancellation pin **k_f = (r+l)·l_f**, ψ = r+l−1 in St 9.4.
SHEET6-MULTIPOLE.md-60-
SHEET6-MULTIPOLE.md:61:**MP8 (budget transparency — the obstruction's mechanism).** On the pure M=1 forest {F ∈ U : M ≡ 1 at F and at every U-vertex above F} and at every all-M=1 merge vertex (including jumps): Y(F) = ∅ and λ_F = 0. Itemizing the Euler equality (22) (Prop 7.5, p. 38) for m poles: pole clusters, chain paths, M=1 segments, and μ=1-arrival merges all contribute identically zero rows. Hence **no refinement or re-partition of any printed budget** (St 9.4/9.5 (25)–(26) p. 49, Cor 7.1 p. 39, identity (22)) can charge M=1 pre-merge ancestry even one unit, for any m and any td. The only printed per-pole cost is Λ-mass: td = ΣΛ_i ≥ mβ ≥ 3m (Props 5.7/5.8), i.e. m ≤ td/3.
SHEET6-MULTIPOLE.md-62-
SHEET6-MULTIPOLE.md-63-**MP9 (m = 2, b = (1,1) sharpening; td-uniform).** Both chains are M=1/λ=0 single-simple-orbit to the meet, μ = (1,1).
SHEET6-MULTIPOLE.md-64- (Interior meet, G\* ≠ (0,y)): M_{G\*} = gcd(2, lν+1) must equal 2 (else MP2 kills), forcing l odd ≥ 1 and ν odd. ν = 1 is impossible: l even contradicts (iv) by the exact log-obstruction (all even l — upgrades SHEET6-L1 §4 beyond engine caps), l odd gives M = 1, killed by MP2. Survivors: exactly **IIa(l odd, ν ≥ 3 odd), M = 2** or **ZCH with gcd(ν+1, l) ≥ 2** — at total pre-merge + merge spend 0. [Cap flag: the ν = 1 variant with an η-factor in q is excluded only for l ≤ 4.]
SHEET6-MULTIPOLE.md-65- (Root meet, G\* = (0,y)) [+H1 for the last clause]: l = 0 impossible (q = p gives 0 = ⊖p ≠ 0 in (iv)); l even impossible (same log-obstruction, ν = 1 by St 9.2(ii)); residual: l odd, locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2 ≠ 0, exact), with k_f = (2+l)·l_f, ψ = l+1, and l ≤ td − 2 (Σλ = 0 in St 9.4 (25)); Prop 9.3(d) with child data (ν,κ̄,D) = (1,1,l_f) forces **κ̄ < ν at both parents** (the case-IV corner, 2POLE §4b). Empty at td = 6 by reach (2POLE §5b phase 3); OPEN at general td.
SHEET6-MULTIPOLE.md-66-
--
SHEET6-MULTIPOLE.md-68-
SHEET6-MULTIPOLE.md-69----
SHEET6-MULTIPOLE.md-70-
SHEET6-MULTIPOLE.md-71-## 3. Derivation
SHEET6-MULTIPOLE.md-72-
SHEET6-MULTIPOLE.md:73:All page numbers: refs/sigray_full.pdf, printed page = pdf page. The printed inventory used is listed once: St 2.1/Not 2.4 (pp. 8–9); Not 3.3 (p. 12); St 3.9 (p. 15); St 3.16 (p. 17); Prop 3.2/St 3.17/3.18 (p. 18); Prop 4.2 (p. 19); Prop 5.1/Not 5.1–5.2 (pp. 23–25); Prop 5.3 (p. 25); St 5.2 (p. 26); Props 5.5–5.8 (pp. 26–28); Thm 6.1 (p. 28); Not 6.1/St 6.1–6.2 (p. 29); Props 6.7/6.8 (pp. 33–34); Not 7.1/St 7.1–7.3 (p. 35); Prop 7.2 (p. 36); Prop 7.5 (22) (p. 38); Cor 7.1, Not 8.1, St 8.1, Prop 8.1 (pp. 39–41); St 8.2–8.5 (pp. 41–43); Cor 8.1, Props 8.2–8.4 (pp. 43–45); table (23) (p. 46); Not 9.1–9.2, St 9.1–9.4 (pp. 48–49); Prop 9.2 (p. 50).
SHEET6-MULTIPOLE.md-74-
SHEET6-MULTIPOLE.md-75-### D1 (MP0)
SHEET6-MULTIPOLE.md-76-(⊇) Each C_i ⊆ Ta& ∩ Va: the printed Prop 8.4 proof line (p. 45) "From Propositions 6.7 and 6.8, we obtain F_0,…,F_n ∈ Ta&" applies from F_0 = P_i — nothing in the construction uses |T_{a,pole}| = 1 (2POLE §1b); poles are in Ta& (d > 0 and deg p ≥ 2 by Prop 5.3(iv)–(v) + St 3.16), and Va-membership descends via Not 3.3(i).
SHEET6-MULTIPOLE.md-77-(⊆) Any H ∈ Ta& ∩ Va \ {(0,x),(0,y)} has deg p_H ≥ 2 (St 3.16: p has more than one root). Prop 6.8 (p. 34, verbatim: "there exist P, u, v: F = I_P(u), v ≥ u, I_P(v) ∈ T_{a,pole}" — the pole lies above H on the SAME branch) gives I_P(v) = P_s. Not 3.3's ° enumerates every Va-vertex of I_P([0,v)) in decreasing order, branch-independently; H is one of them, so H ∈ C_s.
SHEET6-MULTIPOLE.md-78-Leaves: a chain predecessor H of P_j would give deg p_H = mult(p_{P_j}, c) ≥ 2 (St 3.17(i) + St 3.16), contradicting squarefreeness of p_{P_j} (Prop 5.3(v)). So poles have in-degree 0; every non-pole U-vertex is some F°; leaves(U) = {P_1,…,P_m}. ∎
--
SHEET6-MULTIPOLE.md-85-
SHEET6-MULTIPOLE.md-86-### D4 (MP4)
SHEET6-MULTIPOLE.md-87-Poles have m_F = 0 (Prop 5.1(i) + Not 5.1/5.2), so the h-family is {g} (Prop 4.2) and M_{P_i} = gcd(deg p_{P_i}, deg p_{g,P_i}) (Not 8.1). St 5.2(i): deg p/deg p_g = α/β at poles, so (deg p, deg p_g) = b_i(α,β) and M_{P_i} = b_i·gcd(α,β) = b_i = deg p_{P_i}/α. (Check: reproduces all 11 rows of table (23), p. 46, and St 9.6's printed M = 2 = gcd(4,6).) β-minimal: Λ(P) = a b αβ/ν (Prop 5.6 (19)) = β forces ν = abα; St 5.2(ii): ν | α ⇒ ab = 1 ⇒ b = 1; ν | β ⇒ abα | β with gcd(α,β) = 1 ⇒ α = 1, contra St 2.1. Prime Λ: case ν | α: Λ = ab(α/ν)β divisible by β ≥ 3, so Λ = β and a = b = α/ν = 1; case ν | β: Λ = abα(β/ν) divisible by α ≥ 2, so Λ = α < β ≤ Λ (Prop 5.7) — empty. Since the type (α,β) is global (Lemma 2.1), this is per-vertex, valid at every td — repairing the Λ = td-dependence of SHEET6-TDUNIFORM §2. ∎
SHEET6-MULTIPOLE.md-88-
SHEET6-MULTIPOLE.md-89-### D5 (MP5)
SHEET6-MULTIPOLE.md:90:Downward induction from an M = 1 pre-merge vertex H, K = H° still pre-merge: (a) St 8.4 (p. 42) at the pair (K, H = K + c): mult(p_K^{red}, c) | M_H = 1 — the chain orbit is simple. (b) St 8.2 (p. 41) at that μ = 1 arrival: deg q_K > deg p_K; then for every root c′ of p_K, deg q·mult(p,c′) ≥ deg q > deg p, so every root is searrow — **no northeast roots exist at K at all**. (c) A non-chain root c′ would give the tree vertex K ∗ εc′ (St 3.18; the 0-root always continues) with, by St 3.9(iii) + St 3.17(i) + Prop 8.1(i) + the St 6.2 computation (p. 29), K ∗ εc′ ∈ Ta& and deg p = i·mult(p^{red}, εc′) ≥ i ≥ 2; Prop 6.8 then manufactures a pole above it **on that branch** — necessarily one of the m poles of T_{a,pole} (this consumes no pole budget, which is why it scales to every m, replacing L1a's m=2-only third-pole counting); that pole's chain visits K through direction c′ (Not 3.3/Prop 3.2), making K a merge vertex — contradiction with K strictly pre-merge. So p_K = single simple ν-orbit, dp = ν. (d) Root law + eta law [P2] (exact order/residue counting on (iv): at a p-root of mult μ, mult(q) = 1 forced; off-p q-roots simple; η-residue b ≡ 1 mod ν): dq = nν + 1, M_K = gcd(ν, nν+1) = 1 — verbatim the thesis's own step in St 9.6's proof (p. 52). (e) λ_K = 0: no direction in Ta% exists (b); the q-extras at non-roots of p have no tree continuation (St 3.18). (f) No ray separates: all full-pattern roots lie in one ν-orbit with a unique continuing representative (St 3.18; Prop 5.6's proof, p. 27). At the merge arrival: St 8.4 at (G_i, H_i) gives μ_i = 1. ∎
SHEET6-MULTIPOLE.md-91-
SHEET6-MULTIPOLE.md-92-### D6 (MP6)
SHEET6-MULTIPOLE.md-93-Merge ≠ pole: an arriving direction has full multiplicity deg p_{H_e} ≥ 2, contradicting Prop 5.3(v) squarefreeness. Let some μ_j = 1. (a) k = 0: exactly the D5(c) manufacture, now read at G — every root of p_G supports, via Prop 6.8's same-branch pole, an incoming chain of one of the m poles; the roots of p_G are precisely the r arriving directions, in distinct ν-orbits (St 3.18: one continuation per orbit). (b) Equal-quotient: deg p_{H_e} = mult(p_G^{full}, c_e) = i·μ_e (St 3.17(i) + Prop 8.1(i): p^{full} = ⊖p^i); with μ_j = 1, i = deg p_{H_j} ≥ 2. (c) q-shape by root/eta laws [P2] as in D5(d). (d) Arithmetic: dq = (r+l)ν + 1 ≡ 1 (mod ν) forces gcd(M_G, ν) = 1 (Prop 8.1(v): M_G = gcd(dp, dq)); with dp = (Σμ_e)ν, any common divisor is coprime to ν hence divides Σμ_e: M_G = gcd(Σμ_e, (r+l)ν+1) | Σμ_e ≤ ΣM_{H_e} (St 8.4). All-μ=1 IIa: d | (r+l)ν+1 ⇒ gcd(d,ν) = 1 ⇒ (d | rν ⇔ d | r), and (r+l)ν+1 ≡ lν+1 (mod d): **gcd(rν,(r+l)ν+1) = gcd(r, lν+1)** exactly (A1's "divides" upgraded to A2/A3's equality; elementary both ways). ZCH: dp = (r−1)ν+1, difference lν, coprimality to ν gives M = gcd((r−1)ν+1, l). ν = 1: q = p·s, M = gcd(r, r+l) = gcd(r,l). (Machine-swept: r ≤ 9, ν ≤ 12, l ≤ 12, mixed μ-vectors; reproduces every recorded engine cell — (2,3,1) → 2; ZCH (2,2,3) → 3; ν=1 (2,l=2) → 2.) (e) λ_G = 0 as in D5(e). ∎
SHEET6-MULTIPOLE.md-94-
SHEET6-MULTIPOLE.md-95-### D7 (MP7)
SHEET6-MULTIPOLE.md-96-l = 0 kills: IIa: M = gcd(r,1) = 1. ZCH/ν=1: l = 0 forces q = p, and (iv) becomes (δ−1+u)pp′ = ⊖p, i.e. p′ = const ≠ 0, i.e. deg p = 1 — below ν+1 resp. 2 ≤ r: impossible. Cascade: Prop 8.3(i) propagates M = 1 down merge-free segments (regular steps, D2); at an M = 1-emitting merge the cascade continues (M_G = 1 known by direct gcd; steps below regular until the next merge). If the cascade reaches G\* with M = 1 and G\* ≠ (0,y), D3 gives the contradiction — so some merge at or above G\* breaks M = 1: a jump, with the D6 anatomy, and (all entries M = 1 ⇒ the FIRST break is an all-μ=1 merge) the resonance l ≥ 1 and 2 ≤ M ≤ r ≤ m outside ZCH. Entry forcing is D4. Root merge: (0,y) ∈ Ta& (d = l_f < k_f = deg p_{(0,y)}, Thm 6.1 read as the Ta&-inequality at π = 0), so D6 applies at (0,y) with ν = 1 (St 9.2(ii)); top-cancellation of (iv) (St 8.2's proof computation, forced since dq ≥ 2, u = 0, δ = l_f/i) gives l_f = i·r/(r+l) and k_f = i·r, hence **k_f = (r+l)·l_f** and ψ = ⌈k_f/l_f⌉ − 1 = r+l−1 (St 9.4). Prop 8.3(iii) fails (r ≥ 2 roots): no M = 1 kill at the root merge. ∎
SHEET6-MULTIPOLE.md-97-
SHEET6-MULTIPOLE.md-98-### D8 (MP8)
SHEET6-MULTIPOLE.md:99:Claim: every branch P ∈ Ra\R̄a through the pure M=1 forest or an all-M=1 merge has F\*_P ∈ T_{a,pole}. Ascend along P: at segment vertices the full pattern is a single simple orbit (D5), at all-M=1 merges all roots are chain roots (D6a), at poles the branch either separates above (where deg p = 1 by St 3.17(i) + Prop 5.3(v), and St 3.16 excludes Va-membership there and above) or continues along the defining branch (Prop 5.3(ix)). So P passes through a pole vertex Q₀, and since m_F is a vertex invariant, F\*_P = Q₀ ∈ T_{a,pole}. St 7.2 (p. 35) then bans cv vertices on P; Y(F) = ∅ (literally when M = 1 holds from the pole down: every ray through the segment reaches P_i, g(P) = ∞ by Prop 5.5, no cv vertex by Prop 7.2; under the E9/H2 branch-at-F reading for mid-segment onset); λ_F = 0 (St 9.3 (24)). Ledger itemization of the equality (22), extending SHEET6-LROOT §1 to m poles: (i) pole clusters carry zero cv mass (Prop 5.5 + Prop 7.2, per pole); (ii) chain paths carry none (T_{a,cv} ⊂ T_a^0 = {d = 0}, Not 7.1, while d > 0 down to d_{(0,y)} = l_f > 0); (iii) M=1 pre-merge sub-segments: identically zero rows (D5(f)); (iv) μ=1-arrival merges: zero rows (D6e) — the l q-extras are exhibited EMPTY ledger rows; (v) the x-side keeps its ≥ ψ cost (St 9.4's proof, p. 49). Since (22) is an Euler-characteristic *equality*, no re-partition or refinement of the printed counting frame can price these objects: "≥ 1 unit per M=1 occurrence" is structurally false at every m, td. The only remaining per-pole cost is td = ΣΛ_i ≥ mβ (Props 5.7/5.8): m ≤ td/3. ∎
SHEET6-MULTIPOLE.md-100-
SHEET6-MULTIPOLE.md-101-### D9 (MP9)
SHEET6-MULTIPOLE.md-102-m = 2, b = (1,1): D5 forces both chains M=1/λ=0 single-orbit, μ = (1,1) at the meet. Interior meet: r = 2 in D6d, M = gcd(2, lν+1); M = 1 is killed at G\* by D3, so M = 2, i.e. lν odd: l odd ≥ 1 (l = 0 gives gcd(2ν, 2ν+1) = 1), ν odd. ν = 1: (iv) reduces to 2ps′ − l p′s = c′ ≠ 0 (ρ = 2/(2+l), L1 §4's reduction re-derived); l even: divide by p^{(l+2)/2} — (s·p^{−l/2})′ = (c′/2)p^{−(l+2)/2}, whose partial-fraction residue at each root is C(−n, n−1)(a₁−a₂)^{1−2n} with n = (l+2)/2 and C(−n,n−1) = (−1)^{n−1}·C(2n−2, n−1) ≠ 0 for ALL n ≥ 2 (exact; machine-verified n = 2..6) — a log term, so no rational s exists unless c′ = 0, contra ⊖ ≠ 0. This holds at ALL even l, td-uniformly (upgrading L1b beyond its engine caps). l odd gives M = gcd(2, 2+l) = 1, killed. Survivors: IIa(l odd, ν ≥ 3 odd) / ZCH(gcd(ν+1,l) ≥ 2) — exactly the L1 §3 blind-spot family, spend 0. Root meet: ν = 1 (St 9.2(ii)); l = 0: root law gives q = p and (iv) reads 0 = ⊖p ≠ 0 — impossible; l even: the same log-obstruction (u = 0 changes nothing); l odd: locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2, machine-verified exact), no M = 1 kill (Prop 8.3(iii) fails: two predecessors); printed pins: k_f = (2+l)l_f (D7 at r = 2), ψ = l+1 admissible, Σλ = 0 ⇒ l ≤ td−2 (St 9.4 (25)); [+H1] Prop 9.3(d) with child (ν,κ̄,D) = (1,1,l_f) gives 1 = (κ̄_i + n_i)/ν_i, n_i ≥ 1, so κ̄_i ≤ ν_i − 1 at both parents. td = 6: empty by reach (2POLE §5b phase 3). ∎
SHEET6-MULTIPOLE.md-103-
SHEET6-MULTIPOLE.md-104----
--
SHEET6-MULTIPOLE.md-166-
SHEET6-MULTIPOLE.md-167-## 9. Cross-consistency notes (grafting record)
SHEET6-MULTIPOLE.md-168-
SHEET6-MULTIPOLE.md-169-- A1.T2 = A2(4) (restored kill; A2's unique-predecessor argument adopted into D2/D3 as the cleaner single-root justification at (0,y)). A1.T4/T5 = A2(3) = A3.P4 (merge anatomy; independent derivations agree cell-by-cell). A1.T5's "M_G | gcd(r, lν+1)" upgraded to A2/A3's equality (elementary proof in D6d). A1.T6's root pin ψ = r+l−1 ⟷ A2(5R)'s ψ = l+1 at r = 2: consistent. A1.T7 = A2.Prop B (budget transparency; A2 adds the Euler-equality itemization, A1 adds the F\*_P ∈ T_{a,pole} branch argument — both used in D8). A1's G\* = A2's G_last (max ∩C_i). A2(1) prime-Λ pin subsumes A1's β-minimal pin; both in MP4.
SHEET6-MULTIPOLE.md-170-- Escape-set adjudication: A1.T3's correction (ALL strict ancestors of G\* escape) supersedes any "first-vertex-above-merge" phrasing; A2(2)'s "pre-merge segment" forcing and A2.P3's inter-merge propagation condition are compatible refinements.
SHEET6-MULTIPOLE.md:171:- The k = 0 manufacture (D5c/D6a) is the load-bearing novelty in both A1 and A2, derived independently with the same printed chain (St 6.2 computation + St 3.9(iii)/3.17(i)/8.1(i) + Prop 6.8 same-branch); its no-pole-budget character is what makes Theorem MP m-uniform.
SHEET6-MULTIPOLE.md-172-
SHEET6-MULTIPOLE.md-173-## 10. Reproduction
SHEET6-MULTIPOLE.md-174-
SHEET6-MULTIPOLE.md-175-- Printed ground truth: refs/sigray_full.pdf pp. 8–9, 12–19, 23–29, 32–36, 38–46, 48–52 (all re-read on-page by the panel).
SHEET6-MULTIPOLE.md-176-- Machine checks: cases/l1_ode_check.py (jump-cell rigidity, families incl. B/B-η caps); cases/twopole_check.py (2POLE §5 phases); cases/lroot_ledger.py (ledger itemization template for D8); gcd sweeps r ≤ 9, ν ≤ 12, l ≤ 12 + mixed μ-vectors and the log-obstruction residues C(−n, n−1), n = 2..6 (panel sessions; A3's /tmp/mpm_check.py to be rebuilt under cases/ per §7).

exec
/bin/zsh -lc "sed -n '1,220p' BOOK-ENUM.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# BOOK-ENUM.md — the BOOK(m, td) enumeration, run with the mechanical kill arsenal inline

Status: COMPLETE (2026-08-12, this session). Engine: cases/book_enum.py
(exact int/Fraction; 0.04 s for the full sweep). GATE PASS: td=6, m=2
reproduces the promoted record cell-for-cell. Banked: systems/book/
book_m{m}_td{td}.json (18 panels) + summary.json. Spec authority:
SHEET6-DEPTH-REVIEW.md §6 (final BOOK spec), SHEET6-MULTIPOLE.md
MP4/MP6/MP7/MP8, SHEET6-DEPTH.md DS1–DS4 + the promoted d0 ≤ 2·gen+2 fix,
SHEET6-TDUNIFORM.md tdu_rows (promoted, reused verbatim).

## 0. Verdict

The reviewed final book is FINITE and SMALL at every (m, td) with
td = 6..14, m = 2..⌊td/3⌋: **421 cells enumerated, 346 killed by the
inline mechanical arsenal, 75 survivors** across 18 panels (9 panels are
EMPTY — every entry off the all-M=1 axis or no entry at all; this includes
all of td = 7, 11, 13, the multi-pole shadow of the prime-td theorem:
partitions of a prime td always force a prime or β-minimal Λ_i companion
whose type admits only b ≥ 2 partners). No ROOT cell survives anywhere:
every reachable w-alphabet lies in w ≥ 1 (entry w0 = a(b(α+β)−1)/(bν) > 1
and cascades expand while resonant steps never cross 1 in the swept range),
so the case-(IV) w < 1 window is empty — the td=6 root-kill argument is
td-uniform over the whole sweep. Survivors: 31 IIa, 33 ZCH, 11 family-I
(all at r = 3), concentrated at w ∈ {2, 3, 4, 6}. The single largest
surviving class is the promoted **residue-A cell IIa (r,ν,l) = (2,3,1),
M = 2, child (κ̄, D/i, ρ) = (5, 3, 1/2) at w = 2** — present in 10 of the
18 panels (every non-empty m=2 panel and, via pair-branches, m = 3, 4).
ZCH cells appear only where the alphabet holds two w's at integer ratio
≥ 2 (the corrected case-(III) reach law): first at td = 9.

## 1. Spec-to-code map (cases/book_enum.py)

| Layer | Spec (review §6) | Code | Inline kills |
|---|---|---|---|
| E entries | type (α,β), gcd 1, mβ ≤ td; td = ΣΛ_i, Λ_i ≥ β; per pole (a,b,ν) with q-shape pin; MP4 pin M_i = b_i | `entries`/`pole_options` REUSING `sheet6_campaign.tdu_rows(Λ_i)` filtered to the global type (pin okA/okB inline) | any b_i ≥ 2 ⟹ OFF-AXIS class (counted, banked, not cell-expanded; MP7 hypothesis fails) |
| T trees | Σ(r−1) = m−1, r(G) ≤ m, no merge below G* | `set_partitions`/`block_partitions`, recursive branch hierarchies (budget exact by construction) | — |
| C′ chains | w0 = a(b(α+β)−1)/(bν); resonant steps Δ \| num(w); cascade w ↦ w(r+l)/(lν+1); d0 ≤ 2·gen+2 | `w0_of`; `w_closure` (verbatim from promoted depth_closure_check.py); `merge_cascade_ws`; d0 recorded per entry-w0 in JSON | M=1 emission only (MP7); I r=2 even-l cascade excluded (log-obstruction); ZCH cascade gated by reach law |
| J′ jump cells | κ̄_m ∈ (w, (r+1)w] ∩ ℤ; ν determined per (κ̄_m, l); IIa/ZCH/I gcd menu; joins force equal w; ZCH w-ratio ν_e ≥ 2 | `window_cells`, `child_datum`, `enum_context`, `zch_reachable` | mp7_l0_M1, mp7_l0_impossible, M1_mp2, mp9_nu1_even_l (I r=2), zch_w_ratio; M ≥ 2, gcd(M,ν)=1, M \| r (non-ZCH) asserted |
| R root cells | case (IV): w_e = 1 − l_f/i0 < 1 necessary; l odd; St 9.4 ψ = r+l−1 | `enum_root` | root_w_window (W ∩ (0,1) = ∅), root_even_l, root_st94 (l > td−r) |
| S suffix | MP2 + single-pole engine + St 9.4 | NOT run here (per-cell bash next); MP8 encoded: `lambda_spent = 0`, `suffix_budget = td−2` (root: td−1−ψ) per survivor | — |

## 2. The gate (mandatory; PASS)

    GATE td=6 m=2: survivors=1 [('IIa', 2, 3, 1, 2, 5)]
      histogram: {M1_mp2: 2, mp9_nu1_even_l: 2, mp7_l0_impossible: 2,
                  SURVIVE: 1, mp7_l0_M1: 1, root_w_window: 4, zch_w_ratio: 1}
    GATE PASS: unique IIa (2,3,1) M=2 kap=5 child (5,3,1/2) at w=2
               (residue-A), R empty

Cell-for-cell against the promoted record (DEPTH §6 instance line): the
single entry (2,3), Λ = (3,3), both poles (a,b,ν) = (1,1,2), w0 = 2,
W = {2}, gen 0, d0 = 2; the IIa (2,3,1) survivor is Q = (6,12,3,2,5) at
i = 2 — the residue-A configuration (a1/a2 = 2±√3, cases/l1_ode_check.py);
the engine-model ZCH (2,3) cell is now killed pre-suffix by the corrected
case-(III) w-ratio law (`zch_w_ratio`, was suffix-killed in the promoted
record — same verdict, earlier mechanism); ν=1 cells l ∈ {2,4} die by the
even-l log-obstruction, l=1 by M=1+MP2; all 4 root candidates die by the
w < 1 window (w = 2 ≥ 1). Nothing else exists.

## 3. Per-(m, td) census (td = 6..14, m = 2..⌊td/3⌋)

    (m,td)  entries b1 off | cells killed surv | kill histogram (l0M1/l0imp/M1/mp9/zchr/rootw)
    m=2 td= 6    1   1   0 |   13    12     1 | 1/2/2/2/1/4
    m=2 td= 7    1   0   1 |    0     0     0 | (all entries off-axis)
    m=2 td= 8    2   1   1 |   15    14     1 | 1/2/2/2/1/6
    m=2 td= 9    2   2   0 |   22    18     4 | 1/2/5/2/1/7
    m=3 td= 9    1   1   0 |   40    32     8 | 2/4/8/2/2/14
    m=2 td=10    5   3   2 |   29    27     2 | 2/4/6/4/3/8
    m=3 td=10    1   0   1 |    0     0     0 | (off-axis)
    m=2 td=11    2   0   2 |    0     0     0 | (off-axis; prime td)
    m=3 td=11    1   0   1 |    0     0     0 | (off-axis; prime td)
    m=2 td=12   11   7   4 |   55    42    13 | 3/6/13/7/3/10
    m=3 td=12    4   3   1 |   58    48    10 | 3/6/10/5/4/20
    m=4 td=12    1   1   0 |   88    67    21 | 4/8/15/5/5/30
    m=2 td=13    4   0   4 |    0     0     0 | (off-axis; prime td)
    m=3 td=13    2   0   2 |    0     0     0 | (off-axis; prime td)
    m=4 td=13    1   0   1 |    0     0     0 | (off-axis; prime td)
    m=2 td=14    7   4   3 |   48    41     7 | 3/6/10/7/3/12
    m=3 td=14    4   1   3 |   53    45     8 | 2/4/9/2/4/24
    m=4 td=14    1   0   1 |    0     0     0 | (off-axis)
    TOTAL                  |  421   346    75 |

root_even_l / root_st94 never fire (root_w_window kills every root
candidate first — no alphabet reaches w < 1). Full per-panel data incl.
off-axis entry tags, per-w0 closures W/gen/d0, and complete survivor
records: systems/book/book_m{m}_td{td}.json.

## 4. Survivor census: 75 instances, 22 distinct cell classes

By family: 31 IIa, 33 ZCH, 11 I (r ≥ 3 only), 0 ROOT. By w: 31 at w=2,
3 at w=3, 29 at w=4, 12 at w=6. Distinct classes (fam, r, ν, l, M) @ w
→ κ̄_m [panels]:

    IIa, ALL at l = 1 — the Theorem-O escape lν ≡ −1 (mod r), M = r:
      (2,3,1)M2 @w2 κ̄5  [10 panels: every non-empty one — residue-A]
      (2,3,1)M2 @w4 κ̄10, (2,7,1)M2 @w4 κ̄11        [td=12,14 panels]
      (2,5,1)M2 @w3 κ̄8                             [m=2 td=10,12,14]
      (3,2,1)M3 @w2 κ̄6, (3,5,1)M3 @w2 κ̄7          [m=3,4 panels]
      (4,3,1)M4 @w2 κ̄8, (4,7,1)M4 @w2 κ̄9          [m=4 td=12]
    ZCH (all r = 2; need the integer-ratio partner w_z = w/ν_e ∈ W):
      @w4 (ratio 2 over w=2): (2,2,3)M3 κ̄6, (2,2,6)M3 κ̄5, (2,4,5)M5 κ̄5
      @w6 (ratio 3 or 3/2-free: partner w=2): (2,2,3)M3 κ̄9, (2,2,9)M3 κ̄7,
        (2,3,2)M2 κ̄10, (2,3,4)M4 κ̄8, (2,3,8)M4 κ̄7, (2,6,7)M7 κ̄7
    I (ν = 1 interior, r ≥ 3; M = gcd(r,l) ≥ 2; η-variant cap flag):
      @w2: (3,1,3)M3 κ̄4, (3,1,6)M3 κ̄3, (4,1,2)M2 κ̄6, (4,1,4)M4 κ̄4,
           (4,1,8)M4 κ̄3

Empirical structure worth recording: (i) every IIa survivor has l = 1 and
M = r — exactly the MP §O pattern-level escape, now with the full w-window
arithmetic behind it; (ii) ZCH survivors exist only at w ∈ {4, 6}, i.e.
only where a cascade or a larger entry (w0 = 4, 6) coexists with the w = 2
axis at integer ratio — first instance td = 9; (iii) family-I interior
cells enter only at m ≥ 3 (r ≥ 3), as MP9 forces; (iv) the m=4 td=12
panel (the single (2,3)^4 entry at Λ = (3,3,3,3)) is the largest panel:
21 survivors, all three families.

## 5. What the survivors need next (the per-cell bash)

Each surviving cell carries `lambda_spent = 0` (MP8: the entire pre-merge
+ merge region is budget-transparent) and `suffix_budget = td − 2`; the
remaining kill surface is exactly the S layer plus the coefficient layer:

1. **Prop 8.1(iv) rigid solve** per cell (à la cases/l1_ode_check.py
   families A/Z): the merge-local ODE identity with the l extra q-orbits;
   then the MP §8-item-3 coefficient-vs-ratio match (never yet run for any
   cell but residue-A). The IIa l=1 family is the natural first target —
   it is one ODE family in (r, ν).
2. **Suffix engine run** from the child datum Q = (D, deg p, ν_cell, M,
   κ̄_m) at i ≥ 2 (child_kap/child_D_over_i/child_rho in the JSON) under
   the promoted single-pole kill set (hiii_compose E5/N1/AF2/H3q, as in
   tdu_bash) with budget Σλ ≤ td − 2 — the td=6 precedent killed the ZCH
   cell's analogue at this layer.
3. **ZCH cells**: verify the ratio-partner is realizable as an actual
   0-direction chain (the book only checks the arithmetic w-ratio law);
   the case-(III) per-edge solve with n′ ∈ (1/ν_m)ℕ* is in
   depth_closure_check.zch3_edges, ready to lift.
4. **Family-I cells** (r ≥ 3): the r ≥ 3 analogue of the even-l
   log-obstruction is unproved (MP9 is r=2); a Laurent-residue computation
   for C(−n, n−1) at r ≥ 3 could kill (4,1,2)/(4,1,4)/(4,1,8) and
   (3,1,3)/(3,1,6) outright. Cap flag inherited: the ν=1 η-factor
   subvariant is excluded only for l ≤ 4.
5. **Off-axis entry classes** (any b_i ≥ 2; 27 entry multisets across the
   sweep, tags banked per panel): outside the closed M=1 lemma — need the
   M ≥ 2 chain engine (quarantined mixed merges; MP perimeter). These are
   CONFIGURATIONS, not book cells; the prime-td panels are 100% off-axis.

## 6. Engine choices and honest perimeter

- **Conservative throughout** (the book's promoted stance: superset, never
  subset): (i) the J′ menu is the frame-free §5b determination — per-edge
  n_e ≥ 1 admissibility from a concrete frame is NOT imposed; (ii) a cell
  survives if ANY join context supports it; (iii) fractional-w ν′-congruence
  realizability of l=0 tails is not tracked; (iv) P-realizability (an
  absolute (f,g)) is untracked, exactly as in the promoted engines.
- **Cascade child formulas**: the review's C′(ii) prints the IIa map
  w ↦ w(r+l)/(lν+1); the exact DS4 analogues for ZCH (w(r−1+l)/(lν),
  ratio-gated) and I (w(r+l−1)/l, r=2 even-l excluded by the
  log-obstruction) are included — conservative (can only enlarge W; at
  m = 2 no cascade fits the merge budget, so the gate is insensitive).
- **Cascade budget is tree-exact**, tighter than the review's "composed
  ≤ m−1 times" cap: hierarchies on m leaves give Σ(r−1) = m−1 with the
  final cell = G* consuming r−1 ≥ 1, hence ≤ m−2 cascade compositions,
  0 at m = 2 (this is what MP2 forces anyway).
- **MP9 even-l log-obstruction** applied at r = 2, ν = 1 in both jump and
  cascade position (it is a local ODE identity at the merge); NOT applied
  at r ≥ 3 (unproved there — those cells survive into §4).
- **Root candidates** at contexts whose alphabet misses (0,1) are banked
  with w = '-' and killed by `root_w_window` (the l-range 1..td−2 printed
  cap); root_even_l/root_st94 are implemented but never fire in the sweep.
- **d0 ≤ 2·gen(W)+2** (the promoted DEPTH-REVIEW constant) is recorded per
  entry w0 in the JSON (`entry_w0` → W, gen, d0); menu content is
  depth-free via §5b, so d0 is metadata, not a cap.
- **Off-axis** = any pole with b_i ≥ 2 (entry M = b_i ≥ 2 by MP4): the
  chain-depth closure lemma covers only the all-M=1 axis; these multisets
  are counted and their tags banked, never cell-expanded. Mixed merges
  with μ_e ≥ 2 remain quarantined (MP perimeter).

## 7. Reproduction

    cd cases && python3 book_enum.py     # gate + full sweep, ~0.05 s, exit 0
                                         # writes systems/book/*.json
    python3 depth_closure_check.py       # 13/13 promoted priors
    python3 -c "import sheet6_campaign as sc; print(sc.tdu_gate())"  # tdu_rows ground

Gate = run_cell(2,6) checked field-for-field against the promoted record
before any sweep output is written; the sweep aborts if it fails.


exec
/bin/zsh -lc "sed -n '1,125p' SIGRAY-AUDIT.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# SIGRAY-AUDIT.md — Section 2–6 statement audit (thesis pp. 7–30)

Source: `/Users/dc/code/math/jc72108/refs/sigray_full.pdf` (printed page = pdf page). Batch: 72 items, Not 2.1 through Prop 6.2. Verdicts cross-checked against the campaign's erratum catalogue E1–E11 + G1–G3 (`SHEET6-CAMPAIGN.md` §7, `SHEET6-LT-REVIEW.md` §6, `SHEET6-AF2.md`, `SHEET6-AF3.md`, `SHEET6-III.md` §5) and against usage in the promoted SHEET6 docs.

## 1. Verdict ledger (sorted by thesis page)

| id | page | verdict | note |
|---|---|---|---|
| Not 2.1 | 7 | VERIFIED | Definition well-formed: ~ is an equivalence preserving the Jacobian condition; lex-min exists; swap automorphism gives deg f ≤ deg g (used in Lem 2.1(iii)). |
| Not 2.2 | 7 | VERIFIED | Q⁺ := Q ∩ [0,∞); inclusion of 0 deliberate and consistently used (Lem 2.1's α ≠ 0 step would otherwise be vacuous). |
| Lem 2.1 | 8 | VERIFIED_WITH_NIT | Statement + proof re-derived with exact arithmetic; two [A]-citations re-proved from scratch. Nits: [A, 18.13]/[A, 19.2] are load-bearing external inputs not in repo refs; the symmetric j>l_f rectangle case is not literally covered by the printed parenthetical. |
| Not 2.3 | 9 | VERIFIED | Normalized counterexample well-defined; the "from now on" reduction is sound via Lem 2.1. |
| Not 2.4 | 9 | VERIFIED | Type (α,β) well-posed (k_f,k_g ∈ N* from Lem 2.1(i)); (iii) forces α < β. |
| St 2.1 | 9 | VERIFIED_WITH_NIT | Claim (α ≠ 1, β ≠ 1) TRUE, but printed citation "(iv)" insufficient for β ≠ 1 — needs (iii)+(iv); one-word citation repair. |
| St 3.1 | 10 | VERIFIED | No proof printed; the exactly-one-of-(i)/(ii) dichotomy and Puiseux form re-derived from scratch. |
| Def 3.1 | 10 | VERIFIED | Characteristic sequence well-defined: gcd(κ, supp) = 1 forces termination e_m = 1; β_i strictly increasing. |
| Def 3.2 | 10 | VERIFIED_WITH_NIT | Contact order O well-defined; must read 0 ∈ Q⁺ (constant terms); O(P,P) left undefined (needed by Def 3.3); stray ∞ upper-limit typo. |
| St 3.2 | 11 | VERIFIED_WITH_NIT | Proof MISSING in thesis and claim nontrivial (false for general series sets); re-derived via Galois-orbit ultrametricity + greedy anchor induction; 400-trial exact confirmation. Typos ("There exits", "THE Puiseux series"). |
| Def 3.3 | 11 | VERIFIED_WITH_NIT | ~ IS an equivalence, but reflexivity needs unstated O(P,P) = ∞ and transitivity (ultrametric inequality) is nowhere established in the thesis. |
| Not 3.1 | 11 | VERIFIED | I_P injective, π well-defined, π∘I_P = id — all re-derived. |
| Not 3.2 | 11 | VERIFIED_WITH_NIT | (0,y), (0,x) well-defined single classes; usual "independent of P" remark omitted; nonemptiness of S*_y, S*_x implicit. |
| St 3.3 | 11 | VERIFIED_WITH_NIT | Two components re-derived (cross-form O = −1 separates; rays connect each side). Nit: printed S*_{a,x}, S*_{a,y} never defined (stray subscript). |
| Def 3.4 | 11 | VERIFIED_WITH_NIT | V_a well-defined and finite; "u = α_{j,P} for some j" must be read j ≥ 1 (forced downstream) — matches campaign's H1-tier reading dependence (LT-REVIEW LR1(a)), deliberately unfiled. |
| Not 3.3 | 12 | VERIFIED_WITH_NIT | Edge structure re-derived (u* unique, F°-independence, edges biject with non-root vertices). Nits: forward reference to T_a; edge interval printed backwards (I_P([u,u*]) for I_P([u*,u])). |
| Not 3.4 | 12 | VERIFIED | ν_F P-independence PROVED here (not claimed in print; 20000-trial exact sweep) — settles SHEET6-HIII-REVIEW's parenthetical worry negatively: H5a does NOT infect ν_F. |
| Not 3.5 | 12 | GAP | κ_F NOT well-defined as printed: explicit two-branch witness gives κ_F = 4 vs 2 at the same vertex. = campaign's standing item H5a (SHEET6-III.md §5, HIII-REVIEW Front 4), documented but NOT E/G-numbered. Forced repair: jump-realization/max (Eggers-Wall) value. |
| Not 3.6 | 12 | VERIFIED_WITH_NIT | T_a well-formed; printed "T_{a,y} := T_{a,y} ∩ T_a" is circular — RHS must be the starred components of St 3.3. Cosmetic. |
| St 3.4 | 12 | VERIFIED | No proof printed; π(F) ∈ Q re-derived for all three vertex classes (V_{1,a}, V_{2,a}, roots). H5a does not affect it. |
| Not 3.7 | 12 | VERIFIED | Suitable κ exist = common multiples of the finitely many pole multiplicities; requires the Not 3.2 reading of forms (3)/(4). |
| Not 3.8 | 12 | VERIFIED | Both embedded "independent of P" claims re-derived (thesis: "easy to check"); F*c half needs only n ∈ N (n = 0 allowed). |
| St 3.5 | 13 | VERIFIED_WITH_NIT | Re-derived ((F*c)′ = F); hypothesis omits "suitable" for κ; harmless. |
| St 3.6 | 13 | VERIFIED | Re-derived with explicit witness coefficient; edge cases (n = 1, zero coefficient) check out. |
| Not 3.9 | 13 | VERIFIED_WITH_NIT | Well-posed; strict truncation j < π(F) is exactly what gives P-independence. Nits: "Ω(F)" slip for Ω(P); asymmetric unused κ-hypothesis in the x-case. |
| St 3.7 | 13 | ERRATUM | NEW. Eq (5) FALSE as printed: hypothesis κπ(F) ∈ N missing (its twin (6) carries it); exact-arithmetic counterexamples at κπ(F) ∉ Z. Corrected statement adds the hypothesis. Benign downstream: Not 3.10 hedges, all later uses impose κπ(F) ∈ N. |
| Not 3.10 | 13 | VERIFIED_WITH_NIT | Decomposition unique; d_{h,F}, p_{h,F}, h⁺_F invariant under change of suitable κ; the "Assume ... form (5)" hedge insulates it from the St 3.7 erratum. |
| Not 3.11 | 13–14 | VERIFIED_WITH_NIT | Under the canonical maximal-presentation reading, κ_F at v is (Q,j)-independent — re-derived. Nits: type slip (v names a set), existence of v tacit, formal reliance on P-dependent Not 3.5. Related but distinct from E5/H5a. |
| St 3.8 | 14 | ERRATUM | NEW. D_{h,F} ∈ Z FALSE under Not 3.5's P-presentation: explicit contact-vertex witness gives D = −1/2 ∉ Z (and ill-defined value 1 vs 2 even when integral). This UPGRADES H5a from coherence-forced convention to printed-statement-forced: only the jump/max κ_F reading makes St 3.8 true; corrected version proved in two lines (lattice argument). Not previously filed against St 3.8. |
| Not 3.12 | 14 | VERIFIED | mult(p,z) well-posed via unique factorization; degenerate p ≡ 0 never fed to it. |
| Prop 3.1 | 14–15 | VERIFIED_WITH_NIT | Counting identities (*)/(**) re-derived (unramified cover + Hensel + squarefree ⇒ distinct) and machine-checked at κ = 2, 4. Print errors: "c_j x^{-j}" must be c_j x^{-j/κ} (E5/E8-grade typo); proof cites form (4) where (3) is meant; proof terse. |
| St 3.9 | 15 | VERIFIED_WITH_NIT | (i)–(iii) re-derived and machine-checked on two ladders; the one-line printed argument is sound. Display typos (upper limit l for n, x^{-κ}η for x^{-1/κ}η, missing /) all self-repairing; forward reference to Not 3.13. |
| St 3.10 | 16 | VERIFIED | No proof printed; ω, ω* monotone/continuity/slope laws re-derived via contact orders; exact spot-check passed. |
| St 3.11 | 16 | ERRATUM | NEW (the campaign's own paraphrases silently correct it). Printed (ii)'s first term lacks the prime (should be d_{h,F'}): as printed the first inequality is vacuous and the equality-propagation clause is FALSE (explicit counterexample, verified). Corrected version fully re-derived. (i) and the upper bound of (ii) true as printed. |
| Not 3.13 | 16 | VERIFIED_WITH_NIT | Load-bearing slip: p_F, d_F must be read p_{f−a,F}, d_{f−a,F} (literal h = f empties T_a⁻ and falsifies St 3.13). Campaign already adopts this reading (SHEET6-H3.md). |
| St 3.12 | 16 | ERRATUM | NEW. Print (600 dpi confirmed) shows the SAME identity twice — no (0,x)/(1,0) clause; even one instance false under the printed chart naming. Corrected: h⁺_{(0,y)} = h⁺_{(1,0)}, h⁺_{(0,x)} = h⁺_{(0,1)}. Consequence inequalities TRUE. SHEET6-H3.md §2a's "verbatim" quote silently corrects the print — filing amendment needed. |
| St 3.13 | 16 | ERRATUM | NEW (E12-candidate). FALSE as printed for a ≠ 0: d_{f,I(u)} freezes at 0 past the crossing (exact counterexample f = xy, a = 1) — uniqueness fails. TRUE with d_{f−a}: unique zero re-derived. Root cause = Not 3.13 slip; same one-token repair fixes Not 3.14, St 3.14, St 3.15's hypothesis. Campaign silently uses corrected reading (SHEET6-LROOT.md). |
| Not 3.14 | 16 | VERIFIED_WITH_NIT | Trichotomy trivially a partition; inherits the Not 3.13 slip — printed reading gives T_a⁻ = ∅ and an infinite T⁰ tail, breaking Not 7.1/Prop 7.5 downstream; corrected reading is the one actually used. |
| St 3.14 | 16–17 | GAP | (a) Printed reading false for a ≠ 0 (d_{f−a} repair mandatory). (b) Under the repair, all steps re-derived except (ii): "η_F = η_G" assumes the per-fiber Ω picks aligned continuations; can fail up to a root-of-unity conjugation twist for κ > 1. Repair: weaken (ii) up to twist (preserves d, deg, root multiplicities — all the campaign uses) or strengthen St 3.2. NEW. |
| St 3.15 | 17 | KNOWN_ERRATUM | = E10 (labels (i)/(iii) swapped), independently reconfirmed with exact witnesses; multiplicity clause verified modulo the swap; d_{h,H} typo. ADDITION to the filing: the hypothesis's p_F must also read p_{f−a,F} (Not 3.13 slip), else vacuous/false for deep F on fibers a ≠ 0. |
| St 3.16 | 17 | VERIFIED_WITH_NIT | No proof printed; both halves (vertex iff >1 root; η^ν root pattern) re-derived + exact confirmation. Same Not 3.13 p_{f−a} reading dependence (uncatalogued). |
| Prop 3.2 | 18 | VERIFIED | No proof printed; existence/uniqueness/κ-independence of F = G + c re-derived, incl. unstated P-independence of c. |
| St 3.17 | 18 | VERIFIED_WITH_NIT | (i)/(ii) re-derived (vertex-free segment argument + St 3.9 iteration) + exact confirmation. Nits: "π_G" undefined notation; p_{f−a} reading dependence. |
| St 3.18 | 18 | ERRATUM | NEW. Conclusion prints "…unique ν_F-th root of unity, ε such that F * c exists" — ε never occurs in the conclusion; literally false whenever ν_F ≥ 2. Corrected "F * (εc) exists" re-derived TRUE (uniqueness leans on St 3.2's coherent Ω). SHEET6-A2P-REVIEW quotes the corrected form as "verbatim" — uncatalogued; campaign usage is of the corrected form throughout. |
| Prop 4.1 | 18 | VERIFIED_WITH_NIT | Chain-rule identity and (8) dichotomy re-derived (numeric check passed). Nits: undefined "T_{κ,a}"; p_k-for-p_l display slip; hypothesis (7) not load-bearing for 4.1 itself. |
| Prop 4.2 | 19 | GAP | NEW. All printed formulas re-derive exactly ((9), (10), δ-descent, uniqueness), but "since h_j is non-constant, l_j ≠ 0" conflates h_j with its leading part: if h⁺_{j,F} ∈ C* (finite nonzero asymptotic value — live for a non-proper Keller pair) the tower is stuck (l_j = 0 ∉ N*). The Remark "(7) automatic when d_F > 0" is circular. Repairs identified (constant-shift steps, or prove the (7)-analogue). Nil impact on all concrete campaign towers (nonconstant tops). Off-by-one N*^{m−1} tuple tags; stray ",b". |
| Prop 4.3 | 20–21 | VERIFIED_WITH_NIT | NO proof printed; full analogue proof reconstructed and CLOSES ((7) excludes 4.2's stuck corner at j = 0; strict negativity closes j ≥ 1) — explains why (7) is hypothesized here and 4.2's missing analogue is exactly its gap. (iv)'s (f⁺_F)^μ vs (f−a)⁺_F reconciled: T_a⁻ ≠ ∅ forces a = 0. |
| Not 4.1 | 21 | VERIFIED_WITH_NIT | Well-defined via 4.2's uniqueness; ⪯ is a PREORDER, not partial order (antisymmetry fails) — downstream uses need only the preorder. Stray parenthesis typo. |
| Not 4.2 | 21 | VERIFIED_WITH_NIT | Well-posed via 4.3; dropped b-subscripts in the strict clause; duplicated "b ∈ C"; inherited off-by-one dimension tags; "preorder" not "partial order". |
| Prop 4.4 | 21–22 | VERIFIED_WITH_NIT | Proof re-derived link-by-link (T_a⁺ chain, T_a⁻ λ-interpolation) — sound. Nits: F′ never defined in the statement (= tree parent); "any F, F′ ∈ T_a⁻" overstates what is proved (neighbour version + chaining suffices for all downstream uses); minor citation/notation slips. |
| Prop 4.5 | 22–23 | VERIFIED_WITH_NIT | Proof reconstructed; rests on Lem 2.1(i)'s rectangle/corner property of the fixed normalized f — load-bearing but unstated. Print: missing ⁺ superscript in hypothesis; relies on St 3.12 whose print is garbled (see St 3.12 erratum). |
| Prop 4.6 | 23 | VERIFIED_WITH_NIT | No proof printed; (11)–(17) fully re-derived + machine-verified (295-trial exact sweep); the (12) "<" vs (15) ">" sign asymmetry confirmed correct. Nits: "Set F = T_a⁺ ∪ T_a⁻" misprints ∈; T_a⁻ case rests on 4.3(iv) not "(10)". |
| Prop 5.1 | 23–24 | GAP | NEW (beyond catalogued cosmetic E8 cite-slip, reconfirmed). Monotone-ρ argument sound at punctures with g(P) ∈ {0, ∞}, but at g(P) ∈ C* the printed b = 0 reading breaks: (7) fails, m undefined, ρ_0 never vanishes — no threshold u exists. Corrected with forced b = g(P) (thesis's own §7 corroborates); campaign's pole-vertex uses (b = 0) unaffected. |
| Prop 5.2 | 24 | KNOWN_ERRATUM | = E10 casualty exactly as filed (LT-REVIEW §6 FILING FIX 1): statement TRUE, printed proof's last inference only reads correctly under the erroneous St 3.15 labels. Repair re-derived here inside the printed apparatus. |
| Not 5.1 | 24 | VERIFIED_WITH_NIT | Threshold uniqueness re-derived unconditionally; existence inherits Prop 5.1's b = 0 gap (F*_P undefined at g(P) ∈ C* punctures under the printed reading); unconditional for g-poles — the only campaign use. |
| St 5.1 | 24 | VERIFIED_WITH_NIT | Proof re-derived both directions; k/l vs l/k letter-shuffle in the displayed ratio (harmless); only T_a⁺ vertices invoked, so the 5.1 gap never bites. |
| Not 5.2 | 25 | VERIFIED | T_{a,pole} well-defined; threshold uniqueness re-derived; cut with T_a⁺ meaningful. |
| Prop 5.3 | 25–26 | ERRATUM | NEW statement-level: (ii) and (viii) ratios INVERTED — printed d_{g,F} = (k_f/k_g)d_F, correct (k_g/k_f)d_F = (β/α)d_F; proof has a second distinct slip (k_f/l_f). Forced by 4.6(11), St 5.2(i), Prop 5.7, table (23). All NINE properties re-derived TRUE after correction. Campaign (TDUNIFORM R1) silently uses corrected direction; A3L1-REVIEW:61 quotes the print unflagged. Secondary: (vii) never actually derived in print; (vi) missing ",c". |
| Prop 5.4 | 26 | GAP | NEW. Statement TRUE (verified by exact null-space computation on three patterns) but the printed proof never proves the q-half (η^ν-class structure of p_{g,F}; "0 is a root of q" in case (i) nowhere argued). Complete repair supplied and verified; load-bears on α ≥ 2 (St 2.1) — for α = 1 genuine counterexample solutions exist. |
| Not 5.3 | 26 | VERIFIED | Q-datum well-defined on T_{a,pole}: κ_F supplied by 5.3(iv), integrality by St 3.8, positivity by T_a⁺ + 5.3(ii) (unaffected by the 5.3 ratio erratum). |
| St 5.2 | 26 | VERIFIED_WITH_NIT | (i)/(ii) re-derived + 2988-tuple exact sweep, no violation. Consistent ONLY with corrected 5.3(ii)/(viii) — independent corroboration of that new erratum. |
| Prop 5.5 | 26 | ERRATUM | NEW proof-level: all three case conclusions drop g-subscripts (case (ii, c ≠ 0) as printed literally contradicts (18)); dangling "Statement 18" citation (same class as E8). Boxed statement (18) re-derived TRUE; the iff direction needs E10-corrected St 3.15 (known co-dependence, already listed in LT-REVIEW). Corrected proof closes in full. |
| Prop 5.6 | 27 | VERIFIED_WITH_NIT | (19) re-derived exactly in all three root-pattern cases (orbit arithmetic exhaustively swept). One-line printed proof silently needs 5.3(v)/(ix) (simplicity; one puncture per continuation). |
| Prop 5.7 | 27 | VERIFIED | Λ ≥ β re-derived with the missing a,b-scaling supplied; ν_F < deg p_F needs 5.3(iv); sweep confirms bound tight (table (23) rows r5, r10). |
| Def 5.1 | 28 | VERIFIED | Generic preimage count well-posed; Keller condition forces dominance and multiplicity 1, so td ∈ N*. |
| Prop 5.8 | 28 | GAP | NEW. NO proof printed for (20) (text goes straight to §6). Re-derivation succeeds for all but finitely many a; the printed strength "for ANY a ∈ C" needs an unwritten a-uniformity argument (repair route: St 3.14 transport + ν_F-invariance under M_{a,b}, the latter unproven). Campaign applies (20) at fixed dicritical fibers (LROOT "δ_a = 0 for EVERY fiber"); TDUNIFORM/TDU-REVIEW treat 5.8 as trust-perimeter without noting the missing proof. |
| Prop 6.1 | 28 | VERIFIED_WITH_NIT | Indirect proof re-derived ((16) ⟺ (17) under the hypothesis, contradicting 4.6's exclusivity; 2000-trial check). Literal broken "Notation ??" reference; T_a⁻ half tacitly needs Prop 4.3. |
| Thm 6.1 | 28 | VERIFIED_WITH_NIT | l_f < k_f re-derived (Lem 2.1(iii) + Prop 6.1 at the root). Nits: systematic chart-naming inconsistency (operative convention vs literal Not 3.2 chain — conclusion invariant); flags the St 3.12 duplicated-identity print typo. |
| Not 6.1 | 29 | VERIFIED | T↗/T↘ well-posed, disjoint, exhaust T_a⁺ by Prop 6.1; transcription exact. |
| St 6.1 | 29 | VERIFIED | One-line proof sound; Prop 6.1's dichotomy independently re-checked in both branches. |
| St 6.2 | 29 | GAP | NEW. The iff re-derived exactly. The "in particular" clause (unproven in print) does NOT follow as stated: H ∈ T_a⁺ — required for H ∈ T↘ — is not implied (explicit abstract counterconfiguration with d_H < 0). Corrected statement: add H ∈ V_a ∩ T_a⁺ or weaken to the inequality. Potentially load-bearing for St 9.6–9.9's regularity contrapositive. Distinct from E5. |
| Prop 6.2 | 29–30 | ERRATUM | NEW. Hypothesis F/G swap: printed side conditions (i) G ∈ T_a⁻ / (ii) F ∈ T_a⁺ are the exact mirror of what Prop 4.4 needs; mixed-sign case admitted and the proof breaks in three places (exact witness). Corrected (i′) F ∈ T_a⁻ / (ii′) G ∈ T_a⁺: entire proof re-derived + 300k/82k-trial exact sweeps, 0 failures. Same family as E10. Thesis's only citation (Prop 6.3, G ∈ T↘ branch) satisfies (ii′) — downstream unaffected. Two benign /κ display drops also noted. |

## 2. Summary

Of the 72 items audited (thesis pp. 7–30, Not 2.1 → Prop 6.2): **21 VERIFIED, 33 VERIFIED_WITH_NIT, 9 ERRATUM, 2 KNOWN_ERRATUM, 7 GAP**. Cross-check against the campaign catalogue (SHEET6-CAMPAIGN.md §7 = E1–E4 + G1–G3; E5 in SHEET6-III.md; E6–E7 in SHEET6-AF2.md; E8–E9 in SHEET6-AF3.md; E10–E11 in SHEET6-LT-REVIEW.md §6): E1–E7, E9, E11 and G1–G3 all concern §9/assembly (pp. 42–60) and do not touch this batch; the only catalogued items in scope are **E8** (Prop 5.1's cosmetic "Proposition 8" cite-slip — reconfirmed as filed) and **E10** (St 3.15 label swap — independently reconfirmed with exact witnesses; its casualty Prop 5.2 matches LT-REVIEW's FILING FIX 1 exactly). Accordingly, the two KNOWN_ERRATUM verdicts (St 3.15, Prop 5.2) are the catalogue's E10 items, while **all 9 ERRATUM verdicts are NEW**: St 3.7 (missing κπ(F) ∈ N hypothesis in (5)), St 3.8 (D ∈ Z falsified by Not 3.5's P-presentation — this upgrades the campaign's standing H5a convention to printed-statement-forced), St 3.11 (missing prime in (ii) + false equality-propagation clause), St 3.12 (duplicated identity, no (0,x) clause), St 3.13 (false for a ≠ 0; Not 3.13's p_{f−a} slip; recommended E12-candidate), St 3.18 (ε dropped from the unique-continuation conclusion), Prop 5.3 (ratio inverted in (ii)/(viii)), Prop 5.5 (proof-level g-subscript drops + "Statement 18" dangler), and Prop 6.2 (hypothesis F/G swap, same family as E10). Of the 7 GAP verdicts, one is the campaign's known-but-unnumbered **H5a** (Not 3.5 ambiguity, SHEET6-III.md §5 / SHEET6-HIII-REVIEW.md Front 4); the other six are NEW: St 3.14 (cross-fiber Ω alignment/conjugation twist in (ii)), Prop 4.2 (l_j ≠ 0 inference fails at constant-leading-part vertices; the "(7) automatic" Remark is circular), Prop 5.1 (b = 0 argument breaks at g(P) ∈ C* punctures — beyond the catalogued cosmetic E8), Prop 5.4 (q-half of the η^ν-structure never proved; verified repair supplied), Prop 5.8 (no proof printed; the "for ANY a" strength needs an unwritten a-uniformity argument), and St 6.2 (the "in particular" clause needs an H ∈ T_a⁺ hypothesis). A recurring uncatalogued slip family — Not 3.13's p_F/d_F must read p_{f−a,F}/d_{f−a,F} — drives the St 3.13 erratum and riders on Not 3.14, St 3.14, St 3.15 (hypothesis), and St 3.16; the campaign already computes with the corrected reading throughout. Three filing fixes are owed independently of new numbering: SHEET6-H3.md §2a (St 3.12) and SHEET6-A2P-REVIEW.md (St 3.18) present silently corrected text as "verbatim" quotes, and SHEET6-A3L1-REVIEW.md quotes Prop 5.3(ii)'s inverted ratio unflagged.

## 3. Load-bearing risk

Every ERRATUM/GAP/KNOWN_ERRATUM item is inside the campaign's trust perimeter (SHEET6-TEMPLATE.md §6 lists "Prop 3.1, St 3.7–3.18, Prop 4.1–4.6, Prop 5.1–5.8" wholesale). Grep-verified usage by promoted results, ordered by residual risk:

**Tier 1 — unproven strength actually consumed by promoted results:**
- **Prop 5.8 (20) [GAP]** — the enumeration bedrock: td = ΣΛ over pole vertices is the entry point of the whole td = 6 case table (SHEET6-CAMPAIGN.md §0a/§1/§5, G1's adopted reading is "under (20) as printed"), TDUNIFORM (R3) and the prime theorem, L1, 2POLE. Critically, SHEET6-LROOT.md (PROMOTED) uses "(20) already allocates ALL td units of pole mass to T_{a,pole}" for pole purity and claims δ_a = 0 "for EVERY fiber" — exactly the any-a strength whose proof is missing. Highest-priority repair item (route: St 3.14 transport + ν_F-invariance under M_{a,b}).
- **Not 3.5 / H5a [GAP] + St 3.8 [ERRATUM]** — the κ_F convention feeds Not 3.11, Not 5.3's Q-data, Prop 9.3, and the E5-corrected λ-bound engine; SHEET6-III.md's promoted tails closure (10 of 13) is explicitly conditional on H5a/H5b. The St 3.8 finding is favorable: it forces the H5a reading from the printed text, converting a standing hypothesis into a theorem-level constraint — ledger should record the upgrade. D-integrality (St 3.8, corrected) also underpins Prop 5.7 and every integer Q-datum in the §9 tables.
- **Prop 5.4 [GAP]** — its (i)/(ii) η^ν-patterns are the source of St 5.2(ii)'s ν-menu, used verbatim by TDUNIFORM (R2) (PROMOTED prime theorem) and AF3's parity pin (PROMOTED, A3L1-REVIEW confirmed). The q-half those results consume is exactly the unproven half; the verified repair in this audit (using α ≥ 2) should be banked as the supporting derivation.
- **St 6.2 [GAP]** — the climb/regularity workhorse: AF2's (R2) climb, III's regularity step, A2P-REVIEW's (R2) iff, and the campaign's St 9.6–9.9 propagation analogues use the "in particular" clause contrapositively with regularity. A2P-REVIEW already tracks the standing hypothesis (F, G ∈ V_a ∩ T_a⁺) — the missing H ∈ T_a⁺ hypothesis should be added wherever the clause is invoked; a deep child with d_H ≤ 0 and large multiplicity would evade regularity as printed.

**Tier 2 — load-bearing, but campaign already computes with the corrected form (filing fixes only):**
- **St 3.18 [ERRATUM]** — root ↔ direction correspondence with unique-ε continuation is core to direction pricing: III (S1/S2 c = 0 forcing), L1 (one-continuation-per-orbit exclusions), AF2 (R1), TDUNIFORM (unpriced q-orbits), A2P-REVIEW. All uses are of the corrected "F*(εc)" form; A2P-REVIEW's "verbatim" label must be fixed when filing.
- **St 3.15 = E10 [KNOWN_ERRATUM]** — value dichotomy used by LROOT's pole purity ("St 3.15 with corrected labels, E10"), Prop 5.5/5.6's (18)/(19), A3L1/A2P. Already catalogued; add the p_{f−a} hypothesis rider found here.
- **Prop 5.3 [ERRATUM]** — (v)/(vi)/(ix) drive LROOT pole purity, AF3's pattern layer, 2POLE, L1; the inverted (ii)/(viii) ratio is silently corrected in TDUNIFORM (R1). File the erratum + flag A3L1-REVIEW:61.
- **Prop 5.5 (18) [ERRATUM]** — Λ values feed the entire Λ ≤ 7 leaf table (CAMPAIGN §1), 2POLE, LROOT. Statement re-derived true; proof-level subscript drops benign; iff already listed as E10 casualty in LT-REVIEW.
- **St 3.12 [ERRATUM]** — used by Thm 6.1, Prop 4.5, LROOT root data, and H3's mult/deg transport (the promoted H3 root-kill). Consequence inequalities true; H3.md §2a's "verbatim" quote must be amended.
- **St 3.13 + Not 3.13/3.14 slip family [ERRATUM]** — LROOT (PROMOTED) places cv vertices at "the unique (St 3.13) d = 0 point" under the corrected d_{f−a} reading it already uses; file as E12 so the reading is on the ledger rather than folklore.
- **St 3.11 [ERRATUM]** — heavily used (R6 echo kills, TEMPLATE's 16 ≤ 7 kill, LT-REVIEW:132, R1-Q2E5), but exclusively clause (i) and the upper bound of (ii), both true as printed; the erratum (missing prime + equality clause) is outside every campaign use.

**Tier 3 — used, failure mode outside campaign usage (verify-on-use guards recommended):**
- **Prop 4.2 [GAP]** — towers are everywhere (R1's g² − s₀f³ tower per LT-REVIEW front 7 redesign, TEMPLATE, R6's (1,l)-tails, L1, TDUNIFORM); the stuck corner (h⁺_j ∈ C*) is unreachable in every concrete campaign tower (pole vertices, m = 0, nonconstant tops), but any future use of 4.2 at vertices where g has a finite nonzero asymptotic value must first exclude the degenerate shape.
- **Prop 5.1 / Not 5.1 [GAP]** — T_{a,pole} existence machinery used by AF3, A3L1, TDUNIFORM entry, CAMPAIGN; all uses are at g-poles where b = 0 is valid; the g(P) ∈ C* gap is dormant. E8 stays as filed.
- **St 3.14 [GAP]** — used by LT-REVIEW (Prop 7.3's pattern-preservation mechanism) and as the natural Prop 5.8 repair route; the conjugation-twist gap preserves d, deg, and root multiplicities — everything those uses need — but the twist must be carried explicitly if (ii) is ever used for exact leading coefficients across fibers.
- **Prop 5.2 [KNOWN_ERRATUM]** — LROOT cites its no-pole conclusion inside the E10 discussion with corrected labels; statement true, repair re-derived; no action beyond the existing FILING FIX 1.
- **Prop 6.2 [ERRATUM]** — L1 (PROMOTED) uses "(14) = the root law" only via Prop 6.3, whose branch satisfies the corrected (ii′); condition (i) is never invoked anywhere in thesis or campaign. File the swap; no downstream damage.
- **St 3.7 [ERRATUM]** — appears only in TEMPLATE's trust-perimeter listing; every actual use imposes κπ(F) ∈ N, which is precisely the missing hypothesis. Benign; file for completeness.
exec
/bin/zsh -lc "rg -ni \"flat family|flatness|conservation of number|relative (curve|divisor)|intersection number|compactif|normalization.*fiber|degree of.*g|pushforward.*divisor|pole divisor|specialization.*divisor|Hilbert polynomial\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 succeeded in 0ms:
./SHEET6.md:13:Both: compactify, resolve indeterminacy at infinity, then add Abhyankar-type ARITHMETIC of Puiseux data to the topology.
./SHEET6-CLASSICAL.md:229:  NOT apply to the plain compactification; the Orevkov-style application
./MATHIEU.md:294:Step 2 (top degree of C).  If deg C ≠ wδ, Step 1 gives
./SECTION4-AUTOMATION.md:29:  used once in Prop 4.3), Thm 7.3 (intersection numbers — NOT needed for
./SHEET6-A3L1-REVIEW.md:149:  pattern degree of the last pre-merge vertex, ≥ 2 even for immediate
./RECON.md:160:- No findings. X: zero hits on topological/geometric degree of Jacobian pairs, "sheet six", Sigray/Orevkov/Domrina/Żołądek, Eggers–Wall trees (only false positives: Polish "żołądek", Dave Eggers). Web + arXiv likewise. Our td=6 campaign and the Sigray-incompleteness finding (Delta 08-07) remain unclaimed territory. [CLEAR]

exec
/bin/zsh -lc "rg -ni \"Abel.?Jacobi|Picard group|divisor class|principal divisor|Jacobian of (the )?(fiber|curve)|Riemann.?Roch|Mittag.?Leffler|component group|chip.?firing|tropical Jacobian|Baker.?Norine\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 exited 1 in 0ms:
exec
/bin/zsh -lc "rg -ni \"Weierstrass|multi.?point semigroup|value semigroup|Delgado|Poincar[eé] series|gap sequence|gonality|Clifford\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 exited 1 in 0ms:
exec
/bin/zsh -lc "rg -ni \"Bernstein|Kushnirenko|BKK|mixed volume|tropical intersection|stable intersection|secondary polytope|principal A.?determinant|sparse resultant|amoeba\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 succeeded in 0ms:
./DC2-PROGRAM.md:16:[∂_i, x_j] = δ_ij, [x_i, x_j] = [∂_i, ∂_j] = 0. Simple, Noetherian, GKdim 4; Bernstein
./DC2-PROGRAM.md:46:- Bernstein-top forms of a deg-≤2 quadruple span an abelian subalgebra of
./DC2-PROGRAM.md:48:- by §4's slice theorem (verified computationally below): all quadruples of Bernstein
./DC2-PROGRAM.md:198:worthwhile exclusions must use the correction terms (they first act at Bernstein degree
./DC2-PROGRAM.md:206:### 4.1 The slice: Bernstein degree ≤ 2 quadruples (Generator-A analogue)
./DC2-PROGRAM.md:208:**every CCR quadruple with all four generators of Bernstein degree ≤ 2 is an
./DC2-PROGRAM.md:254:  argued. Quantum corrections first act at Bernstein degree 3. PASS.
./DC2-PROGRAM.md:278:**Slice verdict: DC(2) HOLDS in Bernstein degree ≤ 2.** Every deg ≤ 2 CCR quadruple =
./DC2-PROGRAM.md:539:   candidate; DC(2) consistent with HOLDS at Bernstein degree ≤ 3 on everything
./FACE-ISOLATION.md:92:| D8 | Arithmetic lever: m=qp, good primes (G1–G4), Kummer carries, v_p separates pure face (=R₀) from mixed (≥R₀+1); Frobenius CT((R̄^q)^p)=(CT R̄^q)^p | **No classical counterpart in JC2 polygon analysis.** Nearest structures: (a) unit-pivot graded elimination killing sub-vertex strata (LEMMA.md's chain — an exact-arithmetic analog of "mixed strata have higher valuation"); (b) char-p Keller structure: [A^p,B]≡0, P̄^p central, Cartier operator, BKK/Tsuchimoto Frobenius bridge (JC⟺DC) | **The genuinely portable novelty lives here**; see TL1, TL2 |
./notes.md:212:  slot). EXPERIMENT: DC(2) PROVED in Bernstein degree <= 2 (8s exact;
./RECON.md:125:10. Periphery, in-window: Nisse 2608.03613/2608.03601 (08-04) — new Newton-polygon bounds for amoeba-contour cusps/nodes of plane curves (polygon-singularity toolkit, no JC content); Maxim–Messina 2608.04320 (08-05) — vanishing cohomology of fibers at bifurcation values incl. singularities at infinity (sheets-at-infinity terrain); Hajra 2608.04214 (08-04) — classification of affine surfaces finitely dominated by C*×C* (C² among targets). [CONTEXT]

exec
/bin/zsh -lc "rg -ni \"polar curve|polar quotient|L[eê]-Teissier|Merle|Jacobian Newton polygon|discriminant curve|Teissier|Gauss map|dual curve|Pl[uü]cker\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 exited 1 in 0ms:
exec
/bin/zsh -lc "rg -ni \"Camacho|Baum.?Bott|foliation|Godbillon|holonomy index|CS index|line at infinity.*index|Poincar[eé].?Hopf\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 exited 1 in 0ms:
exec
/bin/zsh -lc "rg -ni \"exact.*form|polynomial.*de Rham|x.?dy|f.?dg|generating function|symplectic primitive|Liouville|Camacho|Baum.?Bott|A.?Campo|Alexander polynomial|multi.?point.*semigroup|Weierstrass|Abel.?Jacobi|tropical.*principal|chip.?firing|relative intersection|conservation of number|pole divisor.*flat|stable curve|Mittag.?Leffler\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 succeeded in 0ms:
./SHEET6-MULTIPOLE.md:67:**OBSTRUCTION O (honest half; sharp).** The verbatim multi-pole analogue of Prop 8.4 is FALSE at printed tier: at td = 6, m = 2, both poles are row 1 of table (23) (p. 46) with M_P = gcd(2,3) = 1 *forced*, all pre-merge vertices have M = 1 *forced* (MP5), and the resonant jump (r,ν,l) = (2,3,1) with M = 2 solves the printed identity Prop 8.1(iv) *exactly* with rigid coefficients (a₁/a₂ = 2±√3; cases/l1_ode_check.py; SHEET6-L1 §5, SHEET6-2POLE §6a, machine-verified), at Σλ(pre-merge ∪ merge) = 0, passing every located printed constraint. The L1 §3 blind spot is r-uniform: the l extra q-orbits sit at non-roots of p, carry no tree vertex, no puncture, no cv vertex, no λ, no pole — nothing printed sees them except deg q. At pattern level the escape is m-uniform: for every m, choosing lν ≡ −1 (mod m), ν odd, gives M_{G\*} = m at spend 0 (arithmetic existence only; r-edge H1 ratio-consistency unverified for m ≥ 3). Hence the MP7 residual is irreducible from the printed statement list, and MP0–MP9 is the exact printed-tier frontier.
./SHEET6-MULTIPOLE.md:102:m = 2, b = (1,1): D5 forces both chains M=1/λ=0 single-orbit, μ = (1,1) at the meet. Interior meet: r = 2 in D6d, M = gcd(2, lν+1); M = 1 is killed at G\* by D3, so M = 2, i.e. lν odd: l odd ≥ 1 (l = 0 gives gcd(2ν, 2ν+1) = 1), ν odd. ν = 1: (iv) reduces to 2ps′ − l p′s = c′ ≠ 0 (ρ = 2/(2+l), L1 §4's reduction re-derived); l even: divide by p^{(l+2)/2} — (s·p^{−l/2})′ = (c′/2)p^{−(l+2)/2}, whose partial-fraction residue at each root is C(−n, n−1)(a₁−a₂)^{1−2n} with n = (l+2)/2 and C(−n,n−1) = (−1)^{n−1}·C(2n−2, n−1) ≠ 0 for ALL n ≥ 2 (exact; machine-verified n = 2..6) — a log term, so no rational s exists unless c′ = 0, contra ⊖ ≠ 0. This holds at ALL even l, td-uniformly (upgrading L1b beyond its engine caps). l odd gives M = gcd(2, 2+l) = 1, killed. Survivors: IIa(l odd, ν ≥ 3 odd) / ZCH(gcd(ν+1,l) ≥ 2) — exactly the L1 §3 blind-spot family, spend 0. Root meet: ν = 1 (St 9.2(ii)); l = 0: root law gives q = p and (iv) reads 0 = ⊖p ≠ 0 — impossible; l even: the same log-obstruction (u = 0 changes nothing); l odd: locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2, machine-verified exact), no M = 1 kill (Prop 8.3(iii) fails: two predecessors); printed pins: k_f = (2+l)l_f (D7 at r = 2), ψ = l+1 admissible, Σλ = 0 ⇒ l ≤ td−2 (St 9.4 (25)); [+H1] Prop 9.3(d) with child (ν,κ̄,D) = (1,1,l_f) gives 1 = (κ̄_i + n_i)/ν_i, n_i ≥ 1, so κ̄_i ≤ ν_i − 1 at both parents. td = 6: empty by reach (2POLE §5b phase 3). ∎
./SHEET6-MULTIPOLE.md:128:**Theorem O.** No printed-tier argument can prove M_F ≠ 1 on pre-merge segments (it is false: MP5 forces M = 1 there whenever b_i = 1, which is itself forced at td = mβ and at prime Λ_i), and no printed-tier argument can exclude resonant jump vertices: the cell (r,ν,l) = (2,3,1), M = 2 at td = 6, m = 2 solves Prop 8.1(iv) exactly with rigid coefficients (a₁/a₂ = 2±√3), passes Prop 8.1(iv)-(v), St 8.2/8.4, the root/eta laws, all located budget statements (Σλ = 2 ≤ 3 globally, 0 through the merge), and the entry pins — machine-verified (cases/l1_ode_check.py; SHEET6-2POLE §6a full hand-verified exhibit, every datum absolute). The blind spot is structural and r-uniform: the l extra q-orbits are invisible to every printed statement except deg q (SHEET6-L1 §3). Combined with MP8 (spend 0), the residual is irreducible: **MP0–MP9 is the maximal printed-tier kill**, and the multi-pole problem reduces, for each (m, td), to the finite book of resonant jump cells pinned by MP6/MP7 + the equal-quotient law + Prop 9.3's per-edge ratio equations (pp. 50–51), with entries pinned by MP4.
./SHEET6-III.md:274:budget kill is an exact linear-form positivity check over all s ≥ 0. Exact
./SHEET6-HIII-REVIEW.md:133:  exactly this formula family — strong independent support for reading
./SURPLUS-EXT.md:52:y^9, y^10 in A E' - 3 A' E + 2 B C' - 2 B' C. Exact reduced forms:
./SHEET6.md:31:- **Verification standard**: exact arithmetic only (PARI/SymPy; no floats, no Gröbner needed at this layer). Every "no solution" needs a certificate: explicit congruence obstruction (with modulus), or monotone bound + finite sweep below it. Two independent implementations per case (repo's dual-build culture); spot-formalize the Diophantine kills in Lean post-verdict. Symbolic residue computations are NOT needed for the Sigray engine (they belong to Żołądek's chart engine, which we'd hold in reserve as cross-check).
./MATHIEU.md:214:= Res_{r_i}((C/A^k)′ dy) = 0: the residue of an exact rational form
./MONDELLO-CHECK.md:17:- Separability: [P,Q]=1≠0 ⇒ dP∧dQ=dx∧dy≠0 ⇒ separating transcendence basis ⇒ separable (also 3 odd = prime to 2).
./FACE-ISOLATION.md:131:for the Poisson structure ([A^p,B]≡0), and dP̄∧dQ̄=dx∧dy gives, via the Cartier
./FACE-ISOLATION.md:132:operator C on 1-forms (C(f^{p−1}df)=df, C kills exact forms), the identity
./SIGRAY-AUDIT.md:15:| St 3.1 | 10 | VERIFIED | No proof printed; the exactly-one-of-(i)/(ii) dichotomy and Puiseux form re-derived from scratch. |
./SIGRAY-AUDIT.md:84:Of the 72 items audited (thesis pp. 7–30, Not 2.1 → Prop 6.2): **21 VERIFIED, 33 VERIFIED_WITH_NIT, 9 ERRATUM, 2 KNOWN_ERRATUM, 7 GAP**. Cross-check against the campaign catalogue (SHEET6-CAMPAIGN.md §7 = E1–E4 + G1–G3; E5 in SHEET6-III.md; E6–E7 in SHEET6-AF2.md; E8–E9 in SHEET6-AF3.md; E10–E11 in SHEET6-LT-REVIEW.md §6): E1–E7, E9, E11 and G1–G3 all concern §9/assembly (pp. 42–60) and do not touch this batch; the only catalogued items in scope are **E8** (Prop 5.1's cosmetic "Proposition 8" cite-slip — reconfirmed as filed) and **E10** (St 3.15 label swap — independently reconfirmed with exact witnesses; its casualty Prop 5.2 matches LT-REVIEW's FILING FIX 1 exactly). Accordingly, the two KNOWN_ERRATUM verdicts (St 3.15, Prop 5.2) are the catalogue's E10 items, while **all 9 ERRATUM verdicts are NEW**: St 3.7 (missing κπ(F) ∈ N hypothesis in (5)), St 3.8 (D ∈ Z falsified by Not 3.5's P-presentation — this upgrades the campaign's standing H5a convention to printed-statement-forced), St 3.11 (missing prime in (ii) + false equality-propagation clause), St 3.12 (duplicated identity, no (0,x) clause), St 3.13 (false for a ≠ 0; Not 3.13's p_{f−a} slip; recommended E12-candidate), St 3.18 (ε dropped from the unique-continuation conclusion), Prop 5.3 (ratio inverted in (ii)/(viii)), Prop 5.5 (proof-level g-subscript drops + "Statement 18" dangler), and Prop 6.2 (hypothesis F/G swap, same family as E10). Of the 7 GAP verdicts, one is the campaign's known-but-unnumbered **H5a** (Not 3.5 ambiguity, SHEET6-III.md §5 / SHEET6-HIII-REVIEW.md Front 4); the other six are NEW: St 3.14 (cross-fiber Ω alignment/conjugation twist in (ii)), Prop 4.2 (l_j ≠ 0 inference fails at constant-leading-part vertices; the "(7) automatic" Remark is circular), Prop 5.1 (b = 0 argument breaks at g(P) ∈ C* punctures — beyond the catalogued cosmetic E8), Prop 5.4 (q-half of the η^ν-structure never proved; verified repair supplied), Prop 5.8 (no proof printed; the "for ANY a" strength needs an unwritten a-uniformity argument), and St 6.2 (the "in particular" clause needs an H ∈ T_a⁺ hypothesis). A recurring uncatalogued slip family — Not 3.13's p_F/d_F must read p_{f−a,F}/d_{f−a,F} — drives the St 3.13 erratum and riders on Not 3.14, St 3.14, St 3.15 (hypothesis), and St 3.16; the campaign already computes with the corrected reading throughout. Three filing fixes are owed independently of new numbering: SHEET6-H3.md §2a (St 3.12) and SHEET6-A2P-REVIEW.md (St 3.18) present silently corrected text as "verbatim" quotes, and SHEET6-A3L1-REVIEW.md quotes Prop 5.3(ii)'s inverted ratio unflagged.
./RESIDUE.md:71:exact forms / wrong x-order). Refutation control (a2-variant): the naive
./RESIDUE.md:82:independent of Q col k+1 (any E: exact form) and of deeper columns of
./RESIDUE.md:154:expansion) or the verified exactness lemma; so this is a UNIFORM
./notes.md:247:- **RESIDUE.md committed (e67c50a)**: R_{k,d2} IS a Grothendieck residue — iterated residue of dP∧dQ/(x^{k+2}A^{k+2}) at the toric boundary point {P=0}∩{x=0}. Three interpretations verified by exact arithmetic on 11 cells (48 checks): CT/contour form, Grothendieck form, Koszul moment functional spanning the reachable cokernel of ad_{xA}. Naive dP∧dQ/P^{k+2} refuted (exact form, residue ≡ 0). Uniform theorem all k,d2≥2: surviving outer extra = ±(k+2)/C((k+1)d2,k+1)·a2^{(k-1)d2}·R — explains every mystery unit (5,21,55,99,1001,364) as moments at top pivot; replaces per-cell certificates. conj:R now = its rigidity half only. Correction: sum starts j=max(k+2,d2).
./notes.md:291:- 2026-08-07 night 7: TEMPLATE LIFT decided (SHEET6-TEMPLATE.md, UNREVIEWED): FORMAL-CANDIDATE — the coefficient-level lift of the two-pole rigid template EXISTS; no edge dies. Genome fully explicit (kappa=42 ladder pi=0,2/7,16/21,37/42; all f/g/h1/h2 patterns at R,F_s,G_m,P_i; 2 punctures x 42 series + 42 B-side = k_f 126). Sweep highlights: (i) h1-branch count (St 3.11(i)+8.3(ii)) KILLS the naive tower reading m_{F_s}=1 (16<=7) and forces approximate-root tower (k0,l0)=(2,3),(k1,l1)=(3,4) UNIQUE (h1 ~ f^{4/3}); supplies the missing proof of St 9.6's silent i=deg(p_G)/M_G (erratum candidate E11); (ii) h2-collapse W(t)=t(t-b)^3-(t-a1)^2(t-a2)^2 must drop to deg 1 — forcing EXACTLY b=2sig/3, a1a2=sig^2/6: the L1c rigid coefficients RE-DERIVED from branch counting, independent of the 8.1(iv) ODE; (iii) three more kill chances pass by exact identity: pole-lead cancellation m_i^2=s0*lam_i^3 automatic, H^3=s1*S^4 transport closes via c_m^7=A, h2-lead pole identity 27a(a-b)^3=sig^3(a-3sig/4) exact over Q(sqrt3); (iv) all 12 (edge,h) count/d-ladder cells EXACT (leak-free); (v) minimal-tower branch forces FIRST-STEP merge (m-growth lock; 2POLE 7.3 restored). New pinned data: b2=(3/4)sig h2-direction, p_h1,P=eta^2-(4/3)w^2, w_i^4 formulas, h1-corner (168,56). Engine cases/template_lift.py: 46 checks 0 FAIL. Residuals R1-R6: cancellation depths (R1, decidable by staged linear system ~10^2-10^3 unknowns, hours-days on farm — the cheap decisive experiment), h-Newton budgets/x-side (R2, merge with LROOT pin), cv realizability (R3), root tower depth>=3 with (k2,l2)=(7,23) + M_R (R4), Jacobian closure (R5), deeper-tower window 4/3<l1/k1<3 (R6, same mechanism recursively). td=6 now rests on R1-R6; naive 17.6k-var msolve Ansatz ruled out, template-constrained staging sized and buildable on lib/jc.py.
./SHEET6-R6-REVIEW.md:75:**CONFIRMED.** Printed twice, in the exact form banked:
./SHEET6-MP-REVIEW.md:95:  exactly. MP4's b-formula reproduces all 11 rows of (23) (b = 1 except
./xmodel/grok-eval-20260812.md:7:Why fragile: it has now survived every *printed* constraint (Theorem O), the full coefficient lift (five independent identities close exactly, including the h2-collapse re-deriving L1c without the ODE), and the classical battery (splice/Seifert identity, Abhyankar–Moh at the poles with **zero slack** \(\operatorname{ord}_t f_y=-39\), Jelonek). Every Groebner “kill” of it has been an artifact (msolve parentheses, \(s_{1F}=0\), unreduced mod-\(p\), vmem-cap). Zero-slack topology plus receding discriminants is the signature of a real formal object, not a near-miss. If it algebraizes, JC2 is false and the exclusion program is hunting a theorem that does not exist.
./xmodel/grok-eval-20260812.md:25:| 1 | **T1 ladder on the 4 r9/\(M=2\) single-pole classes** | Same closed-form weapon that killed ZCH iff \((\nu+1)\mid l\) and family I iff \(l/r\) or \(r/l\in\mathbb{Z}\). Hours, exact. A hit is the first new single-pole kill since TDU and may uniformize composite \(\mathrm{td}\). | At the first non-pole \(V_a\) vertex of entry \(Q=(3,6,5,2,8)\), write Prop 8.1(iv) and run the triangular coefficient ladder (`l1_ode_check` style). Kill = \(\tilde{c}=0\) or a multiple root. |
./RECON.md:61:- 2026-07-31 — arXiv:2608.00222v1 (math.AG), Shuhong Gao, "Counterexamples to the Jacobian conjecture in dimensions greater than two". New "tangent-sweep mechanism", explicit counterexample maps in ALL dims > 2 of varying geometric degree, verified in exact rational arithmetic. [tag TBD — mechanism may inform a dim-2 search]
./SHEET6-R1.md:77:scales) => s0 = 1, tower h1 = g^2 - s0 f^3 EXACT (T_a^+ print-true form);

exec
/bin/zsh -lc "sed -n '1,280p' SHEET6-CLASSICAL.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# SHEET6-CLASSICAL.md — four classical kill-tests on the two-pole template

Status: COMPLETE (2026-08-12, UNREVIEWED). Mission: run four independent
CLASSICAL kill-tests (topology/combinatorics, no Groebner) on the sheet-6
two-pole counterexample template (ground truth SHEET6-TEMPLATE.md sec 1;
class 2P-R3a of SHEET6-LROOT.md sec 4). Engine: cases/classical_tests.py
(new, additive; exact Fraction arithmetic; 22 checks, 0 FAIL).

VERDICT SUMMARY:
  T1 SPLICE / LINK AT INFINITY:  PASS — edge dets positive, all pinned
     node multiplicities l_v > 0 (168/294/2022/4664), and the
     Seifert/Euler (genus) balance closes as an EXACT IDENTITY with all
     unpinned tail data cancelling (sec 1c). Full kill power, zero slack.
  T2 ABHYANKAR-MOH / VALUATION:  PASS at poles (exact, ord_t f_y = -39
     forced == computed); KILLS the x-side slack-1 branch pi_G = 4;
     new sharp windows on B-/x-tails (secs 2b, 2c).
  T3 BMY / LOG-SURFACE:          NEEDS-DATA for full (K+D)^2 <= 3e_orb
     (B/x resolution tails unpinned); its chi-shadow (delta ledger)
     PASSES identically; integral witnesses exist (sec 3a).
  T4 JELONEK:                    PASS — mu(F) = 6 exact by Bezout;
     A(F) nonempty curve, >= 2 component families, total asymptotic
     excess Sum(e_p - 1) = 2g + 6 >= 6; degree ceiling passes.
  Coverage: all four verdicts use only the shared (f,g) genome and
  transfer verbatim to the surviving variants (1,2), (2,3)-chain,
  (2,5)-chain.

## 0. Shared input data (from SHEET6-TEMPLATE.md sec 1, LROOT sec 3-4)

Generic fiber C = {f = a}, deg 168, irreducible (f primitive: J(f,g)=1
kills f = h(p)). Newton corner (deg_y, deg_x) = (126, 42); g: (189, 63),
deg g = 252. Places at infinity of C:

Y-side point at infinity (x = infty, y -> c0), 126 local series
y = c0 + sum c_j x^{-j}, j in (1/42)N:
  - P_1: 1 place, 42 conjugate series, Newton pairs (7,2)(3,10)(2,5)
    [char exponents 12/42 < 32/42 < 37/42 in u = 1/x], g-pole order 3.
  - P_2: same shape (a2-side).
  - B-side: 42 series, 6 per direction of the 7-element B-orbit at F_s
    (split from A-side at exponent 12/42); g FINITE there; place
    partition below F_s NOT pinned (each place degree divisible by 7);
    LROOT ledger: one orbit cluster, price D/i - kbar = 42/6 - 5 = 2 =
    Sigma-lambda.
  - Contact table (exponent of first difference, in units of 1/42):
    same-(A-dir, cube-dir) +/- pair: 37; same A-dir, diff cube-dir: 32;
    diff A-dir (incl. all A-vs-B and B-vs-B diff dir): 12;
    same B-dir pairs: > 12, unpinned.
X-side point at infinity ([0:1:0], y = infty, x -> c0'), l_f = 42 series
  x = c0' + c1' y^{-1} + c2' y^{-2} + (split at height >= 3): single
  cluster, one cv vertex, kappa_G = 1, pi_G in [3,4] (LROOT LR2);
  pairwise contact >= 3 in y^{-1}; g finite; carries psi = 2.
Pole bookkeeping: td = 6 = Lambda(P_1) + Lambda(P_2) = 3 + 3; g has NO
  other poles at infinity on C, so ghat: Cbar -> P^1 has degree 6.

Variant transfer: the surviving branches (1,2), (2,3)-chain, (2,5)-chain
(SHEET6-R6.md) differ only in the h-TOWER exponents (k_j,l_j); the
Puiseux/Eggers-Wall data of f and g (the genome above) is SHARED. All
four tests below use only (f,g)-genome data, so every verdict transfers
verbatim to all surviving variants unless explicitly noted.

## 1. T1 — Splice diagram / link at infinity

VERDICT: **PASS — and the Seifert/Euler compatibility closes as an exact
identity with all unpinned data cancelling** (sec 1c). One chart subtlety
matters and is recorded (1c-i).

Criteria used (stated in full before applying):
- (EN-1) [Eisenbud-Neumann, Ann. Math. Studies 110, Thm 11.2] A graph
  multilink is fibered iff the multiplicity l_v = sum over link components
  L_i of m_i lk(L_i, S_v) is nonzero at EVERY node v (S_v = virtual
  component at v). Necessary condition applied here with all m_i = 1.
- (EN-2) [EN, splice positivity for germs] The splice subtree of a LOCAL
  germ of an algebraic branch has all edge determinants positive; for a
  Puiseux chain with Newton pairs (p_i, q_i) the consecutive edge
  determinant equals q_{i+1}, so positivity == q_{i+1} > 0.
- (N-3) [Neumann, Invent. math. 98 (1989)] The link at infinity of a
  reduced algebraic curve is determined by the splice diagram computed
  from the Puiseux data at infinity; for a REGULAR (generic) fiber the
  multilink at infinity is fibered (regular links at infinity), so (EN-1)
  positivity at every node is necessary for the template.
- (RH) Riemann-Hurwitz for ghat: Cbar -> P^1 of degree 6 (poles only at
  P_1, P_2, order 3 each), with NO affine ramification: J(f,g) = 1 makes
  dg|_{fiber} nowhere zero on the affine part (dg/dt = -(dx/dt)/f_y along
  the fiber). Hence g(Cbar) = -3 + (1/2) Sum_{finite punctures}(e_p - 1),
  e_p = ord_t(g - c_p) at puncture p.

### 1a. Splice data (engine sec 7)

P_i-branch Newton pairs, affine chart (u = 1/x): (7,2)(3,10)(2,5),
reproducing char exponents 12/42 < 32/42 < 37/42; cabling weights
(a_1,a_2,a_3) = (2, 52, 317). Local chart at [1:0:0] (all 126 y-series
enter P^2 at ONE point, tangent to L_infty; coordinates (1/x, y/x); every
contact shifts by +1): local pairs (7,9)(3,10)(2,5), cabling
(9, 199, 1199). Edge determinants along both P-chains: q_2, q_3 = 10, 5
> 0: PASS. B-arm and x-arm edge determinants are of the same q-form and
are positive for ANY admissible tail (grid increments are positive), so
edge positivity cannot kill the surviving variants either.

### 1b. Node multiplicities l_v (engine sec 8)

l_v = lk(C, curvetta_v) computed by Bezout: lk = deg C * deg gamma_v
minus intersections at infinity in correct local charts. Curvettas:
truncation curves (e.g. at F_s: x^2(y-c0)^7 = eta^7, deg 9).

    node:  root(L_infty)  F_s   G_m   P_i
    l_v:   168            294   2022  4664

All strictly positive: no EN-fiberedness obstruction at any pinned node.
B-internal and x-internal nodes are not pinned; their l_v are finite
sums of positive contact terms minus the same Bezout correction and were
not evaluated (NEEDS-DATA for those nodes only).

### 1c. Seifert/Euler compatibility = the genus balance (engine sec 5)

The link-at-infinity fiber surface Euler characteristic must agree with
the algebraic fiber; in Euler form this is: genus from the degree-genus
formula (tree side) == genus from (RH) (fibration side). With
  SigS = total B-side same-direction contact sum (units 1/42),
  SigU = total x-side contact sum, r_B, r_X = numbers of B-/x-places:
tree side: g = 13861 - delta_Y - delta_X, delta_Y = (T_Y - 126 + 2 +
r_B)/2 with T_Y = 4890 + 126*125 + SigS/42 (the 126*125 is the local
chart +1 shift), delta_X = (SigU + 42*41 - 42 + r_X)/2;
fibration side: g = -3 + [(11844 - SigS)/42 + (5250 - SigU) - r_B -
r_X]/2, using the T2 valuation formulas e_p = n_p(282 - S_p)/42 (B) and
e'_p = n'_p(125 - U_p) (x-side).

**The two sides agree IDENTICALLY: every unpinned symbol cancels and the
constants match exactly** (engine: all five coefficients zero). Closed
form, new pin for ALL surviving branches:

    g(Cbar) = 2763 - (SigS/42 + SigU + r_B + r_X)/2.

This test had full kill power: the constants absorb the pinned contact
table (597/624/504/432 in 1/42 units), both Newton corners, Lambda = 3,
and deg ghat = 6; any one of them off by any amount breaks the identity.
It closes with zero slack.

(1c-i) Chart caveat, recorded for review: contacts must be taken in the
local coordinates (1/x, y/x) at [1:0:0] (resp. (1/y, x/y) at [0:1:0]),
NOT in the affine series chart; the +1 shift contributes
(126*125 + 42*41)/2 = 8736 to the delta ledger, exactly the amount by
which the naive-chart computation fails. A naive-chart reading would
report a spurious kill.

## 2. T2 — Abhyankar-Moh / semigroup arithmetic

VERDICT: **PASS at the poles with zero slack (exact valuation identity);
one auxiliary branch KILLED (x-side slack-1, pi_G = 4); sharp new pins
on the B-side and x-side tails.**

Criteria used:
- (AM-1) [Abhyankar-Moh, J. reine angew. Math. 276 (1975) / semigroup
  paper 1977] For a curve with ONE place at infinity the semigroup
  condition (delta-sequence, n_i delta_i > delta_{i+1}) holds; corollary
  relevant to Jacobian pairs: if J(f,g) in C* and the pair were a
  counterexample, deg f does not divide deg g and vice versa.
  Honest scope: the template fiber has >= 4 places at infinity, so the
  one-place semigroup chain does NOT apply to it directly; per-place
  germ data alone carries no A-M obstruction (any Puiseux germ arises on
  some algebraic curve). What survives at multi-place level is (AM-2).
- (AM-2) (classical, valuation form of J(f,g) = 1 along a fiber) On the
  smooth fiber f = a, dg/dt = -(dx/dt)/f_y and dg/dt = (dy/dt)/f_x for
  any local parameter t. At each place at infinity this pins
  ord_t(f_y) resp. ord_t(f_x) against ord_t(g) — pure arithmetic in the
  contact tree, this is the two-term Abhyankar valuation bookkeeping.
- (AM-3) [Moh, J. reine angew. Math. 340 (1983)] No counterexample with
  max(deg f, deg g) <= 100. (Consistency only.)

### 2a. Pole places: exact pass (engine sec 3)

At P_1 (u-degree 42): sum of contacts of one P_1-series against the
other 125 y-series = (597 + 624 + 504)/42 = 1725/42. With
lc_y(f-a) = gamma x^42(1+..): ord_t f_y = 42(-42 + 1725/42) = -39.
(AM-2) requires ord_t f_y = ord_t(dx/dt) - ord_t(dg/dt) = -43 - (-4)
= -39 given Lambda(P_1) = 3. **Exact match, zero slack** — this couples
the entire pinned contact table to the pole order of g. Independent
crosscheck: g along a P_1-branch by the product formula over g's 189
series (contacts 171@12, 15@32, 3@37, lc_g = gamma_g x^63):
ord_u g = -63 + 2643/42 = -1/14, i.e. Lambda = 3 recovered from g's own
tree. Same at P_2 by the sqrt3-conjugation symmetry. Parity audit:
mu(P_i) = 2278 even, delta(P_i) = 1139 (a branch must have even Milnor
number): PASS.

### 2b. B-side pin (engine sec 4)

For a B-series with same-direction contact sum S_i (5 pairs, units
1/42): ord_u(g - c_p) = (282 - S_i)/42, so a B-place of degree n_p has

    e_p = n_p (282 - S_p)/42,  integer, 1 <= e_p, and <= 6 by the
    degree budget of ghat (per asymptotic value).

Consequences: S_p = 282 - 42 e_p/n_p in [246, 281]; the B-side
same-direction contacts are FORCED to average approx (49..56)/42 per
pair — deeper than the pole depth 37/42. The template's unmodeled
B-tail is not free: its split depths are pinned to a narrow window.

### 2c. x-side pin and a kill (engine sec 4)

For an x-series with contact sum U_i (41 pairs, units 1, all >= 3):
ord_v(g - c'_p) = 125 - U_i, so e'_p = n'_p(125 - U_p) >= 1 forces

    123 <= U_p < 125,  hence  pi_G <= U_p/41 < 125/41 = 3 + 2/41.

**LROOT LR2's slack-1 alternative pi_G = 4 is DEAD** (it would force
U >= 164, i.e. a g-POLE of order >= 39 at every x-place, contradicting
td = 6 = 3 + 3 exhausted at P_1, P_2). The x-side cv vertex is pinned to
pi_G in [3, 3 + 2/41): essentially the slack-0 position. Also
e'_p <= 2 n'_p automatically (contacts >= 3), a new ceiling on the
x-side dicritical multiplicities.

### 2d. Degree-pair conditions (engine sec 10)

168 does not divide 252 (AM-1 corollary): PASS. gcd = 84, type (2,3);
min degree 168 > 100 (AM-3): consistent, outside Moh's verified range.
All of sec 2 uses only the shared genome: transfers to all surviving
variants.

## 3. T3 — BMY / log-surface ledger

VERDICT: **NEEDS-DATA for the full (K+D)^2 <= 3 e_orb comparison; the
Euler-characteristic shadow of the test (delta/genus ledger) is fully
computable and PASSES identically; integrality/feasibility of the
ledger PASSES with explicit witnesses.**

Criteria:
- (BMY-1) [Miyaoka, Math. Ann. 268 (1984); Kobayashi, Math. Ann. 289
  (1990), orbifold form] For a log-canonical pair (X, D), D reduced NC,
  with kappa(K_X + D) >= 0: (K_X + D)^2 <= 3 e_orb(X \ D).
  Honest scope: X \ D = C^2 has kappa = -infty, so the inequality does
  NOT apply to the plain compactification; the Orevkov-style application
  needs the auxiliary log surface built from the resolved pencil of f
  (vertical boundary + sections), and building THAT graph requires the
  B-internal and x-internal resolution data — exactly the unpinned tail
  of the template. No honest verdict is possible on the pinned skeleton
  alone; what IS computable is the Euler-number arithmetic that any such
  surface must satisfy, namely the delta/genus ledger.
- (BMY-2) degree-genus + delta additivity over the two singular points
  at infinity (Serre; delta = (T - n + r)/2 per point, validated on
  (t^2,t^3), (t^3,t^5), (t^4, t^2+t^3) in-engine).

### 3a. What was computed (engine secs 2, 5, 9)

Pinned local data at [1:0:0]: delta(P_i) = 1139, (P_1 . P_2) = 2388,
(P_i . B) = 2268 each, local Newton pairs (7,9)(3,10)(2,5) per P-branch:
the input for the (future) full dual graph. Ledger identity: sec 1c
(shared with T1): the delta/genus balance closes identically; the
resolution-graph Euler numbers cannot produce a contradiction at
chi-level no matter how the B/x-tails resolve. Feasibility with all
integrality/budget constraints: nonempty; witnesses include
(r_B, e_B, r_X, e'_X, g) = (1,1,6,2,0) [rational fiber, genus 0] and
(1,3,6,2,1), (2,1,6,2,0), etc.

### 3b. Missing data for a decisive T3

(i) B-side place partition (r_B in {1..6}, degrees in 7Z) and split
depths (S_p already windowed by T2b); (ii) x-side partition r_X and
split heights (windowed by T2c); (iii) then a finite continued-fraction
computation gives the full dual graph, K^2, e, and (BMY-1) on the
fibered log surface. Given (i)+(ii) this is a mechanical extension of
cases/classical_tests.py.

## 4. T4 — Jelonek asymptotic variety

VERDICT: **PASS (consistent), with exact geometric degree mu(F) = 6 and
a quantified non-properness excess >= 6.**

Criteria:
- (J-1) [Jelonek, Ann. Polon. Math. 58 (1993)] For a dominant polynomial
  F = (f,g): C^2 -> C^2 the non-properness set A(F) is empty or a curve;
  every irreducible component is the image of a polynomial map C -> C^2
  (hence a rational curve with ONE place at infinity). A Keller
  counterexample is non-proper (a proper Keller map is invertible), so
  A(F) is a nonempty curve.
- (J-2) [Jelonek, degree bound; Testing sets for properness, 1999-2002]
  deg A(F) <= (deg f * deg g - mu(F)) / min(deg f, deg g), mu(F) =
  geometric degree. (Bound form quoted from memory; only used as a
  sanity ceiling, nothing below depends on its exact shape.)

### 4a. Computations (engine secs 6, 9)

mu(F) = 6 EXACT by Bezout with infinity corrections: 168*252 = 42336;

2026-08-12T20:06:28.570316Z ERROR codex_core::tools::router: error=timeout_ms must be at least 10000
exec
/bin/zsh -lc "rg -ni \"Castelnuovo|Severi inequality|gonality|bidegree.*curve|P\\"'^1.?x.?P'"\\"'^1|P1.?x.?P1|two maps" --glob '"'*.md' ." in /Users/dc/code/math/jc72108
 exited 1 in 0ms:
exec
/bin/zsh -lc "rg -ni \"Tschirnhausen|Maroni|Casnati|pushforward.*O|Birkhoff.?Grothendieck|trace.*x|norm.*x|resolvent\" --glob '*.md' ." in /Users/dc/code/math/jc72108
 succeeded in 0ms:
./SHEET6-MULTIPOLE.md:26:(f,g) a normalized counterexample of type (α,β), 2 ≤ α < β, gcd(α,β) = 1 (Not 2.4/St 2.1, pp. 8–9; the type is global, Lemma 2.1 p. 8). T_{a,pole} = {P_1,…,P_m}, m ≥ 2.
./DC2-PROGRAM.md:82:Architecture per ZHEGLOV-SCOPE.md §1: (S2) normal forms A_1 ⊂ D_1 = K[[x]][∂] ⊂ D̂_1^sym,
./DC2-PROGRAM.md:95:| Schur normal form SPS⁻¹ = ∂^p + explicit centralizer | converts [Q,P]=1 into finitely many normal-form coefficients | **BREAKS — first genuine obstruction, see below** |
./DC2-PROGRAM.md:101:Everything in Zheglov's proof after page 1 runs inside normal forms that exist because of
./DC2-PROGRAM.md:133:vertex normalization a_{p0}b_{q0} = ±1 at a unique-decomposition Minkowski vertex,
./DC2-PROGRAM.md:138:Write elements of A_2 normally ordered: P = Σ a_p x^{p'}∂^{p''}, support in ℕ^4. The
./DC2-PROGRAM.md:316:after one normalization — that finiteness is what every known DC(1) argument (Dixmier's
./CROSSCHECK.md:16:  (0,0) coeff unconstrained; torus normalization FIX: P(8,16)=1, Q(12,24)=1.
./CROSSCHECK.md:58:  normalization" Lemma: sets constant terms to 0 AND drops the (0,0) vertex-presence
./SHEET6-TDU-REVIEW.md:91:  arbitrary normalized counterexample; proof (monotone ρ, St 3.10/3.11/
./SHEET6-TDU-REVIEW.md:94:- Prop 8.4 (p. 44): arbitrary normalized counterexample + T_a,pole = {G};
./FACE-ISOLATION.md:111:normalization (x^k at the Minkowski vertex p₀+q₀, unique unimodular decomposition,
./SHEET6.md:15:- **(B) Sigray's decorated Eggers–Wall trees** (verbatim, thesis in hand): Abhyankar normal form (§2: Newton polygons in rectangles, fibers with 2 points at infinity); Eggers–Wall tree of Puiseux expansions of f-fiber branches at infinity (§3); extended Abhyankar fundamental theorem + partial order (§4); td and pole orders of g computed from tree data (§5, Props 5.5/5.8); tree structure symbols ↘↗ (§6); finite critical values budget (§7, Cor 7.1); Jacobian-forced number theory linking neighboring vertices (§8, Prop 8.1); §9: decoration Q(F) = (D_F, deg p_F, ν_F, M_F, κ_F(1−π(F))) must propagate along the "characteristic sequence" F₀→…→(0,y) to the root, under Diophantine constraints, with budget Σλ_{F_i} ≤ td−2 (St 9.4) — and no admissible propagation survives for td ≤ 5.
./notes.md:137:  vertex normalization a1*b3=1 vs gap-column death ((q0)_x=2) =>
./notes.md:170:  posture: cooperative (engage Helali, Suzuki, GGV; Leiden norms). c1-extract
./MATHIEU.md:125:j < d2).  So on the binomial locus the torus normalization is exact and
./SHEET6-LT-REVIEW.md:30:  f−a tower normalization / gauge; UNSOLVABLE-scope caveat vs R6; x-side +
./SHEET6-LT-REVIEW.md:186:  independent and agree exactly. No normalization mismatch exists to
./SHEET6-LT-REVIEW.md:357:GO criteria after redesign: (i) tower normalization fixed per 7b (gauge
./SURPLUS-REVIEW.md:51:  normalization is UNDEFINED at k=1 (both corners have x=1). In the reg
./SHEET6-AF3.md:29:Claim (AF3′): for every F ∈ T_a,pole of a normalized counterexample,
./SHEET6-AF3.md:116:(row 9; ρ = 1/2). A hypothetical carrier is a normalized counterexample of
./SHEET6-AF3.md:177:entry r9 Q=(3,6,5,2,8) of a type-(3,5) normalized counterexample — now
./SECTION4-AUTOMATION.md:430:| family | (m,n) | deg | cases | ψ-normal (rhs x^k) | pre-ψ (rhs x^0) |
./plan-72-108.md:56:  normalize the 2–3 dim torus (x,y,D scalings). Small code, hard to get wrong.
./SIGRAY-AUDIT.md:12:| Not 2.3 | 9 | VERIFIED | Normalized counterexample well-defined; the "from now on" reduction is sound via Lem 2.1. |
./SHEET6-CAMPAIGN.md:61:  normalization forbids exactly this. Campaign runs with hypothesis **H3**: "case-IV
./MONDELLO-CHECK.md:23:- **Vertex normalization (i): HOLDS verbatim.** rhs monomial 1 at Minkowski vertex (1,1) = (1,0)+(0,1), unique decomposition, det = +1, corners saturated (vertex eq a·b = 1).
./MONDELLO-CHECK.md:24:- **Gap condition (ii): FAILS.** In SURPLUS.md normalization this is the cell (k,d2) = (0,1): rhs = x⁰, {p₀,q₀} = {(1,0),(0,1)} so max((p₀)_x,(q₀)_x) = 1 < 2; no gap columns. Also d2 = 1 = the scope-map row with "no extra keys, no obstruction", and the top edges are NOT through the origin (Q straddles the direction line: offsets −1, 5).
./MONDELLO-CHECK.md:30:**Over Q the machinery EMPTIES his data at the M2/gap-kill stage** (pre-block, LEMMA.md §2 step 1 / SURPLUS.md GAP-KILL analogue). Sparse run: 13 keys; after vertex normalization (pivot det((1,0),(0,1)) = +1, odd), the sub-vertex single-monomial keys force a(2,1) = 0 [pivot **+2**], a(4,0) = 0 [pivot **+4**], a(6,2) = 0 [pivot **+6**], then b(7,2) = 0 [pivot **+2**], b(6,1) = b(8,3) = 0 (odd pivots 1, 3): full collapse to the elementary automorphism P = a1x, Q = b0y + b1x⁵. Hull run agrees: strip corners a(2,1), a(6,2) killed by pivots +2, +6; Q-corner b(8,3) then dies; residual = triangular x-axis family (automorphisms). So **no char-≠2 Keller pair realizes these Newton polygons** — his example must live where those pivots die.
./MONDELLO-CHECK.md:37:> **Remark.** The characteristic restrictions in our results are not an artifact of the method. Mondello's plane Keller pair P = x + x²y + x⁴ + x⁶y², Q = y + x⁵ + x⁶y + x⁷y² + x⁸y³ over F₂ (arXiv:2608.02634) has Jacobian determinant 1, sends the three distinct points (0,1), (1,0), (1,1) to a common image, and generates a degree 3 separable field extension, so even the separable Jacobian conjecture fails in characteristic two. Its Newton polygons form a strip pair along the direction (1,1) satisfying our vertex normalization, and in any characteristic other than two our near-origin eliminations, whose pivot constants at this polygon data are the lattice determinants 2, 4, and 6, force the strip corners to vanish and reduce any such pair to an elementary automorphism. In characteristic two every one of these determinants vanishes, the corresponding bracket equations become identically zero, and the strips survive; this is precisely the escape that Mondello's example exploits.
./MONDELLO-CHECK.md:41:- **Not in-regime**: strip pair along d=(1,1) with vertex normalization (i) exact, but cell (k,d2) = (0,1) — outside the proved (2,2) obstruction cell (no gap columns, d2=1, top edges off origin). No contradiction with our char-0 theorems.
./SHEET6-R1-REVIEW.md:107:mandate satisfied. Normalizations line up exactly (through-factor count
./AUDIT.md:13:  → torus normalization fix_ones     (lib/jc.py, emit.py emit_normalized)
./SHEET6-2POLE.md:31:"Proposition 8.4. Let (f,g) be a normalized counterexample of the Jacobian
./SHEET6-H3.md:14:satisfying every printed normalization constraint exists (§5b, r10/M4) —
./SHEET6-H3.md:69:- Lemma 2.1 (pp. 8-9): normalized counterexample (f,g); f^+_{(1,1)} =
./SHEET6-H3.md:177:### 4a. Theorem (H3-psi). Let (f,g) be a normalized counterexample, and let
./conjectureE-plan.md:22:`𝕋` = Tschirnhausen polynomials `α(z) = z^k + e_{k−2}z^{k−2} + ... + e_0` (monic, no `z^{k−1}`).
./conjectureE-plan.md:136:- `α° = z² + e₀` (Tschirnhausen of degree `δa = 2`), unknown `e₀`.
./conjectureE-plan.md:249:`1·x^{m/aδ}y^{n/aδ}` term in `E°`, Tschirnhausen `α°`); (iii) char-0 certificate, not just mod-p.
./REDUCE4-CUT-REVIEW.md:75:  normalization: fixing 2 corner coefficients + the rhs coefficient to 1
./LEMMA.md:42:i.e. eq #3 is the **vertex normalization**: x² must be attained at the bottom
./LEMMA.md:115:  **corner normalization**: for [P,Q] = x², the valuation of x² selects the
./LEMMA.md:142:  (i) *(vertex normalization)* x^k sits at the Minkowski vertex p₀+q₀ with
./LEMMA.md:184:to 0 against the vertex normalization), while reg_9_24_c3 has (q₀)_x = 1
./RECON.md:18:- Tao: no X account activity found; blog post 2026-07-21 (see §4), no follow-up since. Akhil Mathew: no original X posts; quoted in Fortune re "unsettling" pace + a "Leiden Declaration" on AI norms in math circulating (@v_shakthi 2026-08-02). Will Sawin: nothing substantive found. [CONTEXT]
./RECON.md:55:- **Leiden Declaration** (leidendeclaration.ai; Zenodo 20302944; IMU letter 2026-06): Lorentz Center workshop product on AI-in-math norms — human responsibility, tool disclosure, peer review over press-release timelines; ~3,400 signatories, Tao/Scholze/Dijkgraaf featured; Gowers declined and blogged why (gowers.wordpress.com 2026-07-26). [CONTEXT — shapes how we should publish]
./RECON.md:91:- **GGV group (Guccione ×2 / Valqui, + Horruitiner):** **no public response to the counterexample and no new JC preprint** — latest arXiv item is math.GR (2606.05520, June 2026); latest JC-adjacent is Ramirez–Valqui **2506.05697** (June 2025), "The Groebner basis and solution set of a polynomial system related to the Jacobian conjecture" [USABLE-BY-US — closest published precedent for our Gröbner/msolve formulation; check their normalizations against Generator A]. Valqui's PUCP CRIS page (cris.pucp.edu.pe) shows nothing newer. Neither Helali nor Suzuki appears to have contacted them publicly. [CONTEXT]
./RECON.md:176:- No findings. No X or web trace of any other automated case-bash / Gröbner / degree-farm / Lean campaign on JC(2) or DC(2); no lab or group announcements; @openconjectures/unsolvedmath/ULAM silent; chloeallegra228 no JC follow-up (collision-ideals still not on arXiv). [CLEAR — ours remains the only visible systematic computational campaign]
./SHEET6-PILOT.md:44:  ⇒ under Λ ≤ 6: β ≤ 6, plus 1 < α < β, gcd(α,β) = 1 (type of normalized counterexample).
./SHEET6-A2P-REVIEW.md:144:  baseline engine trace shows exactly this route (ENTRY (1,4,4,9) --mu=4
./SHEET6-R1.md:1426:- rnorm memo (rnorm(key,c) is EXACTLY linear in c; key-part cached;
./ZHEGLOV-SCOPE.md:9:- **S2 Preliminaries, theory of normal forms** (565–1300, ~735 ln): imports from [A.Z]=Zheglov's generalized Schur theory, [GZ1]=Guo–Zheglov normal forms, Dixmier, Wilson, Sato. Ring tower A_1 ⊂ D_1=K[[x]][∂] ⊂ D̂_1^sym; Schur operator S with SPS⁻¹=∂^p; centralizer C(∂^p) ≅ M_p(K[D^p]), "vector form". Mostly cited, not reproved.
./ZHEGLOV-SCOPE.md:17:**External load-bearing inputs (not reproved here):** [GZ1] (arXiv 2303.10306, Guo–Zheglov normal forms — the whole calculus), [A.Z] (generalized Schur theory), [GGV] (subrectangular reduction of minimal counterexamples), Wilson's theorem, classical Schur–Sato. An error in [GZ1] would sink the paper wholesale.
./ZHEGLOV-SCOPE.md:30:**R4. String-equation correspondence for NON-coprime orders (S5, esp. T:one-to-one-correspondence & inverse, 2620–2790).** Extends A. Schwarz's coprime-order bijection; needed precisely because subrectangular DC-pairs have non-coprime orders. Feeds R:distinguished_coefficient (distinguished coefficient =0, via Newton–Puiseux + Wilson, rank-1). Formal-series existence/uniqueness/normalization arguments; the whole transport of the DC-pair to the Puiseux-series side rests here.
./ZHEGLOV-SCOPE.md:56:- **T3. Machinery on non-vacuous objects**: automorphism pairs (φ(x),φ(∂)) in A_1 and Burchnall–Chaundy rank-1 commuting pairs; compute normal forms to finite order; test L:Q_p tail shape, termination + non-maximal distance (intro's claim), S5 cut/glue roundtrip, distinguished-coefficient=0 (R:distinguished_coefficient). ~10-20 agent-h. Tests R4 + S2 end-to-end where hypotheses are satisfiable.
./SHEET6-LROOT.md:157:normalization (Lemma 2.1(ii)) makes f and g exhaust together on the
./SHEET6-TDUNIFORM.md:38:Setting: (f,g) a normalized counterexample of type (alpha,beta) (Not 2.4
./SHEET6-TDUNIFORM.md:241:normalized counterexample with a single pole vertex (T_a,pole = {F}),

exec
/bin/zsh -lc "nl -ba BOOK-ENUM.md | sed -n '1,65p;150,215p' && nl -ba BOOK-BASH-R2.md | sed -n '45,58p;210,245p' && nl -ba SIGRAY-AUDIT.md | sed -n '65,80p;84,100p' && nl -ba SHEET6-MULTIPOLE.md | sed -n '46,64p;86,102p;116,130p' && nl -ba SHEET6-DEPTH.md | sed -n '398,432p' && nl -ba notes.md | sed -n '324,346p'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
     1	# BOOK-ENUM.md — the BOOK(m, td) enumeration, run with the mechanical kill arsenal inline
     2	
     3	Status: COMPLETE (2026-08-12, this session). Engine: cases/book_enum.py
     4	(exact int/Fraction; 0.04 s for the full sweep). GATE PASS: td=6, m=2
     5	reproduces the promoted record cell-for-cell. Banked: systems/book/
     6	book_m{m}_td{td}.json (18 panels) + summary.json. Spec authority:
     7	SHEET6-DEPTH-REVIEW.md §6 (final BOOK spec), SHEET6-MULTIPOLE.md
     8	MP4/MP6/MP7/MP8, SHEET6-DEPTH.md DS1–DS4 + the promoted d0 ≤ 2·gen+2 fix,
     9	SHEET6-TDUNIFORM.md tdu_rows (promoted, reused verbatim).
    10	
    11	## 0. Verdict
    12	
    13	The reviewed final book is FINITE and SMALL at every (m, td) with
    14	td = 6..14, m = 2..⌊td/3⌋: **421 cells enumerated, 346 killed by the
    15	inline mechanical arsenal, 75 survivors** across 18 panels (9 panels are
    16	EMPTY — every entry off the all-M=1 axis or no entry at all; this includes
    17	all of td = 7, 11, 13, the multi-pole shadow of the prime-td theorem:
    18	partitions of a prime td always force a prime or β-minimal Λ_i companion
    19	whose type admits only b ≥ 2 partners). No ROOT cell survives anywhere:
    20	every reachable w-alphabet lies in w ≥ 1 (entry w0 = a(b(α+β)−1)/(bν) > 1
    21	and cascades expand while resonant steps never cross 1 in the swept range),
    22	so the case-(IV) w < 1 window is empty — the td=6 root-kill argument is
    23	td-uniform over the whole sweep. Survivors: 31 IIa, 33 ZCH, 11 family-I
    24	(all at r = 3), concentrated at w ∈ {2, 3, 4, 6}. The single largest
    25	surviving class is the promoted **residue-A cell IIa (r,ν,l) = (2,3,1),
    26	M = 2, child (κ̄, D/i, ρ) = (5, 3, 1/2) at w = 2** — present in 10 of the
    27	18 panels (every non-empty m=2 panel and, via pair-branches, m = 3, 4).
    28	ZCH cells appear only where the alphabet holds two w's at integer ratio
    29	≥ 2 (the corrected case-(III) reach law): first at td = 9.
    30	
    31	## 1. Spec-to-code map (cases/book_enum.py)
    32	
    33	| Layer | Spec (review §6) | Code | Inline kills |
    34	|---|---|---|---|
    35	| E entries | type (α,β), gcd 1, mβ ≤ td; td = ΣΛ_i, Λ_i ≥ β; per pole (a,b,ν) with q-shape pin; MP4 pin M_i = b_i | `entries`/`pole_options` REUSING `sheet6_campaign.tdu_rows(Λ_i)` filtered to the global type (pin okA/okB inline) | any b_i ≥ 2 ⟹ OFF-AXIS class (counted, banked, not cell-expanded; MP7 hypothesis fails) |
    36	| T trees | Σ(r−1) = m−1, r(G) ≤ m, no merge below G* | `set_partitions`/`block_partitions`, recursive branch hierarchies (budget exact by construction) | — |
    37	| C′ chains | w0 = a(b(α+β)−1)/(bν); resonant steps Δ \| num(w); cascade w ↦ w(r+l)/(lν+1); d0 ≤ 2·gen+2 | `w0_of`; `w_closure` (verbatim from promoted depth_closure_check.py); `merge_cascade_ws`; d0 recorded per entry-w0 in JSON | M=1 emission only (MP7); I r=2 even-l cascade excluded (log-obstruction); ZCH cascade gated by reach law |
    38	| J′ jump cells | κ̄_m ∈ (w, (r+1)w] ∩ ℤ; ν determined per (κ̄_m, l); IIa/ZCH/I gcd menu; joins force equal w; ZCH w-ratio ν_e ≥ 2 | `window_cells`, `child_datum`, `enum_context`, `zch_reachable` | mp7_l0_M1, mp7_l0_impossible, M1_mp2, mp9_nu1_even_l (I r=2), zch_w_ratio; M ≥ 2, gcd(M,ν)=1, M \| r (non-ZCH) asserted |
    39	| R root cells | case (IV): w_e = 1 − l_f/i0 < 1 necessary; l odd; St 9.4 ψ = r+l−1 | `enum_root` | root_w_window (W ∩ (0,1) = ∅), root_even_l, root_st94 (l > td−r) |
    40	| S suffix | MP2 + single-pole engine + St 9.4 | NOT run here (per-cell bash next); MP8 encoded: `lambda_spent = 0`, `suffix_budget = td−2` (root: td−1−ψ) per survivor | — |
    41	
    42	## 2. The gate (mandatory; PASS)
    43	
    44	    GATE td=6 m=2: survivors=1 [('IIa', 2, 3, 1, 2, 5)]
    45	      histogram: {M1_mp2: 2, mp9_nu1_even_l: 2, mp7_l0_impossible: 2,
    46	                  SURVIVE: 1, mp7_l0_M1: 1, root_w_window: 4, zch_w_ratio: 1}
    47	    GATE PASS: unique IIa (2,3,1) M=2 kap=5 child (5,3,1/2) at w=2
    48	               (residue-A), R empty
    49	
    50	Cell-for-cell against the promoted record (DEPTH §6 instance line): the
    51	single entry (2,3), Λ = (3,3), both poles (a,b,ν) = (1,1,2), w0 = 2,
    52	W = {2}, gen 0, d0 = 2; the IIa (2,3,1) survivor is Q = (6,12,3,2,5) at
    53	i = 2 — the residue-A configuration (a1/a2 = 2±√3, cases/l1_ode_check.py);
    54	the engine-model ZCH (2,3) cell is now killed pre-suffix by the corrected
    55	case-(III) w-ratio law (`zch_w_ratio`, was suffix-killed in the promoted
    56	record — same verdict, earlier mechanism); ν=1 cells l ∈ {2,4} die by the
    57	even-l log-obstruction, l=1 by M=1+MP2; all 4 root candidates die by the
    58	w < 1 window (w = 2 ≥ 1). Nothing else exists.
    59	
    60	## 3. Per-(m, td) census (td = 6..14, m = 2..⌊td/3⌋)
    61	
    62	    (m,td)  entries b1 off | cells killed surv | kill histogram (l0M1/l0imp/M1/mp9/zchr/rootw)
    63	    m=2 td= 6    1   1   0 |   13    12     1 | 1/2/2/2/1/4
    64	    m=2 td= 7    1   0   1 |    0     0     0 | (all entries off-axis)
    65	    m=2 td= 8    2   1   1 |   15    14     1 | 1/2/2/2/1/6
   150	  subset): (i) the J′ menu is the frame-free §5b determination — per-edge
   151	  n_e ≥ 1 admissibility from a concrete frame is NOT imposed; (ii) a cell
   152	  survives if ANY join context supports it; (iii) fractional-w ν′-congruence
   153	  realizability of l=0 tails is not tracked; (iv) P-realizability (an
   154	  absolute (f,g)) is untracked, exactly as in the promoted engines.
   155	- **Cascade child formulas**: the review's C′(ii) prints the IIa map
   156	  w ↦ w(r+l)/(lν+1); the exact DS4 analogues for ZCH (w(r−1+l)/(lν),
   157	  ratio-gated) and I (w(r+l−1)/l, r=2 even-l excluded by the
   158	  log-obstruction) are included — conservative (can only enlarge W; at
   159	  m = 2 no cascade fits the merge budget, so the gate is insensitive).
   160	- **Cascade budget is tree-exact**, tighter than the review's "composed
   161	  ≤ m−1 times" cap: hierarchies on m leaves give Σ(r−1) = m−1 with the
   162	  final cell = G* consuming r−1 ≥ 1, hence ≤ m−2 cascade compositions,
   163	  0 at m = 2 (this is what MP2 forces anyway).
   164	- **MP9 even-l log-obstruction** applied at r = 2, ν = 1 in both jump and
   165	  cascade position (it is a local ODE identity at the merge); NOT applied
   166	  at r ≥ 3 (unproved there — those cells survive into §4).
   167	- **Root candidates** at contexts whose alphabet misses (0,1) are banked
   168	  with w = '-' and killed by `root_w_window` (the l-range 1..td−2 printed
   169	  cap); root_even_l/root_st94 are implemented but never fire in the sweep.
   170	- **d0 ≤ 2·gen(W)+2** (the promoted DEPTH-REVIEW constant) is recorded per
   171	  entry w0 in the JSON (`entry_w0` → W, gen, d0); menu content is
   172	  depth-free via §5b, so d0 is metadata, not a cap.
   173	- **Off-axis** = any pole with b_i ≥ 2 (entry M = b_i ≥ 2 by MP4): the
   174	  chain-depth closure lemma covers only the all-M=1 axis; these multisets
   175	  are counted and their tags banked, never cell-expanded. Mixed merges
   176	  with μ_e ≥ 2 remain quarantined (MP perimeter).
   177	
   178	## 7. Reproduction
   179	
   180	    cd cases && python3 book_enum.py     # gate + full sweep, ~0.05 s, exit 0
   181	                                         # writes systems/book/*.json
   182	    python3 depth_closure_check.py       # 13/13 promoted priors
   183	    python3 -c "import sheet6_campaign as sc; print(sc.tdu_gate())"  # tdu_rows ground
   184	
   185	Gate = run_cell(2,6) checked field-for-field against the promoted record
   186	before any sweep output is written; the sweep aborts if it fails.
   187	
    45	ZCH(2,3,2)M2@w6 is the unique remaining ZCH/I cell missing both
    46	criteria ((ν+1) = 4 ∤ l = 2); T1/T1b/T2/T3 all close consistently on a
    47	rigid template (c̃ = (9/40)a³ ≠ 0, roots (3±√3)a/4), joining the six
    48	round-1 IIa survivors. All kills are vertex-local in (fam, r, ν, l) and
    49	frame-free — no td, m, w, κ̄, or entry datum enters any solve — so each
    50	single solve kills the class's entire panel set. **No new td becomes
    51	fully excluded** (td = 7, 11, 13 remain the only ones): residue-A
    52	IIa(2,3,1)M2@w2 still sits in every non-empty panel and survives, and
    53	every composite td stays independently blocked by the TDU single-pole
    54	residual. But the multi-pole book shrinks 62 → 27 live instances, and
    55	every one of the 27 is now a bashed, rigid template — the unbashed
    56	category is empty.
    57	
    58	## 1. Verdict table
   210	    m=2,td=14      7    |     1     |     2     |   4
   211	    m=3,td=14      8    |     2     |     4     |   2
   212	    TOTAL         75    |    13     |    35     |  27
   213	
   214	Unbashed column: **0 everywhere** — the book is fully adjudicated.
   215	
   216	## 5. Per-td exclusion status (combined ledger)
   217	
   218	Single-pole ground truth unchanged (SHEET6-TDUNIFORM promoted: prime
   219	theorem at prime td; composite residual 4/16/16/23/71/48 at
   220	td = 6/8/9/10/12/14). Multi-pole ground is the book after both rounds:
   221	
   222	| td | single-pole residual (TDU) | multi-pole book after R1+R2 | FULLY excluded? |
   223	|---|---|---|---|
   224	| 6 | 4 classes | 1 cell: residue-A only | NO |
   225	| 7 | 0 (prime theorem) | empty | **YES** |
   226	| 8 | 16 classes | 1 cell: residue-A only | NO |
   227	| 9 | 16 classes | 2 cells: residue-A ×2 (was 8 — all 6 unbashed cells killed) | NO |
   228	| 10 | 23 classes | 2 cells: residue-A + IIa(2,5,1)@w3 | NO |
   229	| 11 | 0 (prime) | empty | **YES** |
   230	| 12 | 71 classes | 15 cells (was 38): 13 IIa-template + ZCH(2,3,2)@w6 ×2 | NO |
   231	| 13 | 0 (prime) | empty | **YES** |
   232	| 14 | 48 classes | 6 cells (was 12): all IIa-template | NO |
   233	
   234	## 6. FINAL COMBINED CENSUS (rounds 1+2)
   235	
   236	The two-round campaign has now bashed all 22 classes / 75 cell
   237	instances of the td ≤ 14 multi-pole book. **DEAD: 15 classes outright
   238	plus one panel of a 16th — 48 of 75 instances** (round 1: IIa(3,2,1)M3@w2
   239	×4, IIa(4,3,1)M4@w2 ×1, IIa(3,5,1)M3@w2 at m=3,td9 ×1, ZCH(2,2,3)M3@w4
   240	×7; round 2: ZCH(2,2,6)M3@w4 ×7, ZCH(2,4,5)M5@w4 ×7, ZCH@w6
   241	(2,2,3)κ̄9/(2,2,9)/(2,3,4)/(2,3,8)/(2,6,7) ×2 each, I(3,1,3) ×4,
   242	I(3,1,6) ×4, I(4,1,2)/(4,1,4)/(4,1,8) ×1 each). Every kill in both
   243	rounds was T1 or T2, and all 12 round-2 kills are the single T1 pattern
   244	(a): divisibility-forced ⊖ = 0 homogeneous-branch degeneracy —
   245	(ν+1) | l for family Z, l/r ∈ ℤ or r/l ∈ ℤ for family I — each
    65	| Not 5.2 | 25 | VERIFIED | T_{a,pole} well-defined; threshold uniqueness re-derived; cut with T_a⁺ meaningful. |
    66	| Prop 5.3 | 25–26 | ERRATUM | NEW statement-level: (ii) and (viii) ratios INVERTED — printed d_{g,F} = (k_f/k_g)d_F, correct (k_g/k_f)d_F = (β/α)d_F; proof has a second distinct slip (k_f/l_f). Forced by 4.6(11), St 5.2(i), Prop 5.7, table (23). All NINE properties re-derived TRUE after correction. Campaign (TDUNIFORM R1) silently uses corrected direction; A3L1-REVIEW:61 quotes the print unflagged. Secondary: (vii) never actually derived in print; (vi) missing ",c". |
    67	| Prop 5.4 | 26 | GAP | NEW. Statement TRUE (verified by exact null-space computation on three patterns) but the printed proof never proves the q-half (η^ν-class structure of p_{g,F}; "0 is a root of q" in case (i) nowhere argued). Complete repair supplied and verified; load-bears on α ≥ 2 (St 2.1) — for α = 1 genuine counterexample solutions exist. |
    68	| Not 5.3 | 26 | VERIFIED | Q-datum well-defined on T_{a,pole}: κ_F supplied by 5.3(iv), integrality by St 3.8, positivity by T_a⁺ + 5.3(ii) (unaffected by the 5.3 ratio erratum). |
    69	| St 5.2 | 26 | VERIFIED_WITH_NIT | (i)/(ii) re-derived + 2988-tuple exact sweep, no violation. Consistent ONLY with corrected 5.3(ii)/(viii) — independent corroboration of that new erratum. |
    70	| Prop 5.5 | 26 | ERRATUM | NEW proof-level: all three case conclusions drop g-subscripts (case (ii, c ≠ 0) as printed literally contradicts (18)); dangling "Statement 18" citation (same class as E8). Boxed statement (18) re-derived TRUE; the iff direction needs E10-corrected St 3.15 (known co-dependence, already listed in LT-REVIEW). Corrected proof closes in full. |
    71	| Prop 5.6 | 27 | VERIFIED_WITH_NIT | (19) re-derived exactly in all three root-pattern cases (orbit arithmetic exhaustively swept). One-line printed proof silently needs 5.3(v)/(ix) (simplicity; one puncture per continuation). |
    72	| Prop 5.7 | 27 | VERIFIED | Λ ≥ β re-derived with the missing a,b-scaling supplied; ν_F < deg p_F needs 5.3(iv); sweep confirms bound tight (table (23) rows r5, r10). |
    73	| Def 5.1 | 28 | VERIFIED | Generic preimage count well-posed; Keller condition forces dominance and multiplicity 1, so td ∈ N*. |
    74	| Prop 5.8 | 28 | GAP | NEW. NO proof printed for (20) (text goes straight to §6). Re-derivation succeeds for all but finitely many a; the printed strength "for ANY a ∈ C" needs an unwritten a-uniformity argument (repair route: St 3.14 transport + ν_F-invariance under M_{a,b}, the latter unproven). Campaign applies (20) at fixed dicritical fibers (LROOT "δ_a = 0 for EVERY fiber"); TDUNIFORM/TDU-REVIEW treat 5.8 as trust-perimeter without noting the missing proof. |
    75	| Prop 6.1 | 28 | VERIFIED_WITH_NIT | Indirect proof re-derived ((16) ⟺ (17) under the hypothesis, contradicting 4.6's exclusivity; 2000-trial check). Literal broken "Notation ??" reference; T_a⁻ half tacitly needs Prop 4.3. |
    76	| Thm 6.1 | 28 | VERIFIED_WITH_NIT | l_f < k_f re-derived (Lem 2.1(iii) + Prop 6.1 at the root). Nits: systematic chart-naming inconsistency (operative convention vs literal Not 3.2 chain — conclusion invariant); flags the St 3.12 duplicated-identity print typo. |
    77	| Not 6.1 | 29 | VERIFIED | T↗/T↘ well-posed, disjoint, exhaust T_a⁺ by Prop 6.1; transcription exact. |
    78	| St 6.1 | 29 | VERIFIED | One-line proof sound; Prop 6.1's dichotomy independently re-checked in both branches. |
    79	| St 6.2 | 29 | GAP | NEW. The iff re-derived exactly. The "in particular" clause (unproven in print) does NOT follow as stated: H ∈ T_a⁺ — required for H ∈ T↘ — is not implied (explicit abstract counterconfiguration with d_H < 0). Corrected statement: add H ∈ V_a ∩ T_a⁺ or weaken to the inequality. Potentially load-bearing for St 9.6–9.9's regularity contrapositive. Distinct from E5. |
    80	| Prop 6.2 | 29–30 | ERRATUM | NEW. Hypothesis F/G swap: printed side conditions (i) G ∈ T_a⁻ / (ii) F ∈ T_a⁺ are the exact mirror of what Prop 4.4 needs; mixed-sign case admitted and the proof breaks in three places (exact witness). Corrected (i′) F ∈ T_a⁻ / (ii′) G ∈ T_a⁺: entire proof re-derived + 300k/82k-trial exact sweeps, 0 failures. Same family as E10. Thesis's only citation (Prop 6.3, G ∈ T↘ branch) satisfies (ii′) — downstream unaffected. Two benign /κ display drops also noted. |
    84	Of the 72 items audited (thesis pp. 7–30, Not 2.1 → Prop 6.2): **21 VERIFIED, 33 VERIFIED_WITH_NIT, 9 ERRATUM, 2 KNOWN_ERRATUM, 7 GAP**. Cross-check against the campaign catalogue (SHEET6-CAMPAIGN.md §7 = E1–E4 + G1–G3; E5 in SHEET6-III.md; E6–E7 in SHEET6-AF2.md; E8–E9 in SHEET6-AF3.md; E10–E11 in SHEET6-LT-REVIEW.md §6): E1–E7, E9, E11 and G1–G3 all concern §9/assembly (pp. 42–60) and do not touch this batch; the only catalogued items in scope are **E8** (Prop 5.1's cosmetic "Proposition 8" cite-slip — reconfirmed as filed) and **E10** (St 3.15 label swap — independently reconfirmed with exact witnesses; its casualty Prop 5.2 matches LT-REVIEW's FILING FIX 1 exactly). Accordingly, the two KNOWN_ERRATUM verdicts (St 3.15, Prop 5.2) are the catalogue's E10 items, while **all 9 ERRATUM verdicts are NEW**: St 3.7 (missing κπ(F) ∈ N hypothesis in (5)), St 3.8 (D ∈ Z falsified by Not 3.5's P-presentation — this upgrades the campaign's standing H5a convention to printed-statement-forced), St 3.11 (missing prime in (ii) + false equality-propagation clause), St 3.12 (duplicated identity, no (0,x) clause), St 3.13 (false for a ≠ 0; Not 3.13's p_{f−a} slip; recommended E12-candidate), St 3.18 (ε dropped from the unique-continuation conclusion), Prop 5.3 (ratio inverted in (ii)/(viii)), Prop 5.5 (proof-level g-subscript drops + "Statement 18" dangler), and Prop 6.2 (hypothesis F/G swap, same family as E10). Of the 7 GAP verdicts, one is the campaign's known-but-unnumbered **H5a** (Not 3.5 ambiguity, SHEET6-III.md §5 / SHEET6-HIII-REVIEW.md Front 4); the other six are NEW: St 3.14 (cross-fiber Ω alignment/conjugation twist in (ii)), Prop 4.2 (l_j ≠ 0 inference fails at constant-leading-part vertices; the "(7) automatic" Remark is circular), Prop 5.1 (b = 0 argument breaks at g(P) ∈ C* punctures — beyond the catalogued cosmetic E8), Prop 5.4 (q-half of the η^ν-structure never proved; verified repair supplied), Prop 5.8 (no proof printed; the "for ANY a" strength needs an unwritten a-uniformity argument), and St 6.2 (the "in particular" clause needs an H ∈ T_a⁺ hypothesis). A recurring uncatalogued slip family — Not 3.13's p_F/d_F must read p_{f−a,F}/d_{f−a,F} — drives the St 3.13 erratum and riders on Not 3.14, St 3.14, St 3.15 (hypothesis), and St 3.16; the campaign already computes with the corrected reading throughout. Three filing fixes are owed independently of new numbering: SHEET6-H3.md §2a (St 3.12) and SHEET6-A2P-REVIEW.md (St 3.18) present silently corrected text as "verbatim" quotes, and SHEET6-A3L1-REVIEW.md quotes Prop 5.3(ii)'s inverted ratio unflagged.
    85	
    86	## 3. Load-bearing risk
    87	
    88	Every ERRATUM/GAP/KNOWN_ERRATUM item is inside the campaign's trust perimeter (SHEET6-TEMPLATE.md §6 lists "Prop 3.1, St 3.7–3.18, Prop 4.1–4.6, Prop 5.1–5.8" wholesale). Grep-verified usage by promoted results, ordered by residual risk:
    89	
    90	**Tier 1 — unproven strength actually consumed by promoted results:**
    91	- **Prop 5.8 (20) [GAP]** — the enumeration bedrock: td = ΣΛ over pole vertices is the entry point of the whole td = 6 case table (SHEET6-CAMPAIGN.md §0a/§1/§5, G1's adopted reading is "under (20) as printed"), TDUNIFORM (R3) and the prime theorem, L1, 2POLE. Critically, SHEET6-LROOT.md (PROMOTED) uses "(20) already allocates ALL td units of pole mass to T_{a,pole}" for pole purity and claims δ_a = 0 "for EVERY fiber" — exactly the any-a strength whose proof is missing. Highest-priority repair item (route: St 3.14 transport + ν_F-invariance under M_{a,b}).
    92	- **Not 3.5 / H5a [GAP] + St 3.8 [ERRATUM]** — the κ_F convention feeds Not 3.11, Not 5.3's Q-data, Prop 9.3, and the E5-corrected λ-bound engine; SHEET6-III.md's promoted tails closure (10 of 13) is explicitly conditional on H5a/H5b. The St 3.8 finding is favorable: it forces the H5a reading from the printed text, converting a standing hypothesis into a theorem-level constraint — ledger should record the upgrade. D-integrality (St 3.8, corrected) also underpins Prop 5.7 and every integer Q-datum in the §9 tables.
    93	- **Prop 5.4 [GAP]** — its (i)/(ii) η^ν-patterns are the source of St 5.2(ii)'s ν-menu, used verbatim by TDUNIFORM (R2) (PROMOTED prime theorem) and AF3's parity pin (PROMOTED, A3L1-REVIEW confirmed). The q-half those results consume is exactly the unproven half; the verified repair in this audit (using α ≥ 2) should be banked as the supporting derivation.
    94	- **St 6.2 [GAP]** — the climb/regularity workhorse: AF2's (R2) climb, III's regularity step, A2P-REVIEW's (R2) iff, and the campaign's St 9.6–9.9 propagation analogues use the "in particular" clause contrapositively with regularity. A2P-REVIEW already tracks the standing hypothesis (F, G ∈ V_a ∩ T_a⁺) — the missing H ∈ T_a⁺ hypothesis should be added wherever the clause is invoked; a deep child with d_H ≤ 0 and large multiplicity would evade regularity as printed.
    95	
    96	**Tier 2 — load-bearing, but campaign already computes with the corrected form (filing fixes only):**
    97	- **St 3.18 [ERRATUM]** — root ↔ direction correspondence with unique-ε continuation is core to direction pricing: III (S1/S2 c = 0 forcing), L1 (one-continuation-per-orbit exclusions), AF2 (R1), TDUNIFORM (unpriced q-orbits), A2P-REVIEW. All uses are of the corrected "F*(εc)" form; A2P-REVIEW's "verbatim" label must be fixed when filing.
    98	- **St 3.15 = E10 [KNOWN_ERRATUM]** — value dichotomy used by LROOT's pole purity ("St 3.15 with corrected labels, E10"), Prop 5.5/5.6's (18)/(19), A3L1/A2P. Already catalogued; add the p_{f−a} hypothesis rider found here.
    99	- **Prop 5.3 [ERRATUM]** — (v)/(vi)/(ix) drive LROOT pole purity, AF3's pattern layer, 2POLE, L1; the inverted (ii)/(viii) ratio is silently corrected in TDUNIFORM (R1). File the erratum + flag A3L1-REVIEW:61.
   100	- **Prop 5.5 (18) [ERRATUM]** — Λ values feed the entire Λ ≤ 7 leaf table (CAMPAIGN §1), 2POLE, LROOT. Statement re-derived true; proof-level subscript drops benign; iff already listed as E10 casualty in LT-REVIEW.
    46	**MP3 (exact escape set).** The vertices escaping MP2 are exactly {F ∈ U : F > G\*}: ALL strict ancestors of G\* — pre-merge segments, inter-merge segments, and merge vertices above G\*. (Not merely "the first vertex above each merge": the M = 1 contradiction is manufactured only at (0,y), so no per-segment rerun of Prop 8.4 exists.)
    47	
    48	**MP4 (entry pin; td- and m-uniform).** At every pole, (deg p_{P_i}, deg p_{g,P_i}) = b_i(α,β) and **M_{P_i} = b_i = deg p_{P_i}/α**. Moreover b_i = 1 (hence M_{P_i} = 1) is FORCED when Λ(P_i) = β (β-minimal pole) and when Λ(P_i) is prime. In particular at the minimal m-pole degree td = mβ, ALL entries have M = 1.
    49	
    50	**MP5 (forced M = 1 propagation — the naive analogue is false, maximally).** If M_F = 1 at a pre-merge vertex of C_i (e.g. F = P_i when b_i = 1), then every C_i-vertex from F down to the last pre-merge vertex has reduced pattern a single SIMPLE ν-orbit (dp = ν, dq = nν + 1, n ≥ 1), M = 1, λ = 0, no ray of T_a separating there; the chain arrives at G_i with μ_i = 1. M = 1 likewise propagates down every merge-free segment (Prop 8.3(i)) and through every M = 1-emitting merge.
    51	
    52	**MP6 (merge anatomy).** No merge vertex is a pole vertex. At a merge G with at least one arriving μ_e = 1 (automatic for any M = 1-ancestry arrival, since μ_e | M_{H_e} by St 8.4):
    53	 (a) **k = 0**: every root of p_G carries an incoming chain; no non-chain roots, searrow or northeast; the roots are exactly the r arriving directions;
    54	 (b) **equal-quotient law**: deg p_{H_e} = i·μ_e with one common i ≥ 2 for all e;
    55	 (c) **q-shape** [P2]: q = η·rad(p)·Π_{s=1}^{l}(η^ν − b_s^ν) for ν ≥ 2 (η-factor absorbed at ν = 1), all q-roots simple;
    56	 (d) **gcd menu**: dq ≡ 1 (mod ν), hence **gcd(M_G, ν_G) = 1** always; with no 0-chain, **M_G = gcd(Σ_e μ_e, (r+l)ν + 1)**, so M_G | Σ_e μ_e ≤ Σ_e M_{H_e} (subadditivity). All-μ=1 families: **IIa**: (dp,dq) = (rν, (r+l)ν+1), M_G = gcd(rν,(r+l)ν+1) **= gcd(r, lν+1)**; **ZCH** (one chain at the 0-direction): (dp,dq) = ((r−1)ν+1, (r−1+l)ν+1), M_G = gcd((r−1)ν+1, l); **I** (ν = 1): (dp,dq) = (r, r+l), M_G = gcd(r, l). Corollary: outside ZCH, **M_G | r ≤ m**;
    57	 (e) **λ_G = 0**: no northeast direction exists and the l extras carry no tree vertex.
    58	
    59	**MP7 (no-resonance kill and jump existence).** l = 0 at an all-M=1 merge forces M_G = 1 (IIa: gcd(r,1)) or is impossible outright (ZCH and ν = 1: q = p forces p′ = const ≠ 0 in (iv), i.e. deg p = 1 — contradiction). Hence an all-M=1 merge either emits M = 1 (cascade continues) or is a **resonant jump**: l ≥ 1 and 2 ≤ M_G ≤ r(G) ≤ m in the non-0-chain families. Consequently: if all entries have M = 1 (forced at td = mβ, or all Λ_i prime, by MP4), then either G\* ≠ (0,y) and at least one resonant jump vertex with the full MP6 anatomy exists at or above G\*, or G\* = (0,y) and the **root merge** itself has the all-μ=1 anatomy at ν = 1 (St 9.2(ii)) with k = 0, l ≥ 1, M = gcd(r,l), and the top-cancellation pin **k_f = (r+l)·l_f**, ψ = r+l−1 in St 9.4.
    60	
    61	**MP8 (budget transparency — the obstruction's mechanism).** On the pure M=1 forest {F ∈ U : M ≡ 1 at F and at every U-vertex above F} and at every all-M=1 merge vertex (including jumps): Y(F) = ∅ and λ_F = 0. Itemizing the Euler equality (22) (Prop 7.5, p. 38) for m poles: pole clusters, chain paths, M=1 segments, and μ=1-arrival merges all contribute identically zero rows. Hence **no refinement or re-partition of any printed budget** (St 9.4/9.5 (25)–(26) p. 49, Cor 7.1 p. 39, identity (22)) can charge M=1 pre-merge ancestry even one unit, for any m and any td. The only printed per-pole cost is Λ-mass: td = ΣΛ_i ≥ mβ ≥ 3m (Props 5.7/5.8), i.e. m ≤ td/3.
    62	
    63	**MP9 (m = 2, b = (1,1) sharpening; td-uniform).** Both chains are M=1/λ=0 single-simple-orbit to the meet, μ = (1,1).
    64	 (Interior meet, G\* ≠ (0,y)): M_{G\*} = gcd(2, lν+1) must equal 2 (else MP2 kills), forcing l odd ≥ 1 and ν odd. ν = 1 is impossible: l even contradicts (iv) by the exact log-obstruction (all even l — upgrades SHEET6-L1 §4 beyond engine caps), l odd gives M = 1, killed by MP2. Survivors: exactly **IIa(l odd, ν ≥ 3 odd), M = 2** or **ZCH with gcd(ν+1, l) ≥ 2** — at total pre-merge + merge spend 0. [Cap flag: the ν = 1 variant with an η-factor in q is excluded only for l ≤ 4.]
    86	### D4 (MP4)
    87	Poles have m_F = 0 (Prop 5.1(i) + Not 5.1/5.2), so the h-family is {g} (Prop 4.2) and M_{P_i} = gcd(deg p_{P_i}, deg p_{g,P_i}) (Not 8.1). St 5.2(i): deg p/deg p_g = α/β at poles, so (deg p, deg p_g) = b_i(α,β) and M_{P_i} = b_i·gcd(α,β) = b_i = deg p_{P_i}/α. (Check: reproduces all 11 rows of table (23), p. 46, and St 9.6's printed M = 2 = gcd(4,6).) β-minimal: Λ(P) = a b αβ/ν (Prop 5.6 (19)) = β forces ν = abα; St 5.2(ii): ν | α ⇒ ab = 1 ⇒ b = 1; ν | β ⇒ abα | β with gcd(α,β) = 1 ⇒ α = 1, contra St 2.1. Prime Λ: case ν | α: Λ = ab(α/ν)β divisible by β ≥ 3, so Λ = β and a = b = α/ν = 1; case ν | β: Λ = abα(β/ν) divisible by α ≥ 2, so Λ = α < β ≤ Λ (Prop 5.7) — empty. Since the type (α,β) is global (Lemma 2.1), this is per-vertex, valid at every td — repairing the Λ = td-dependence of SHEET6-TDUNIFORM §2. ∎
    88	
    89	### D5 (MP5)
    90	Downward induction from an M = 1 pre-merge vertex H, K = H° still pre-merge: (a) St 8.4 (p. 42) at the pair (K, H = K + c): mult(p_K^{red}, c) | M_H = 1 — the chain orbit is simple. (b) St 8.2 (p. 41) at that μ = 1 arrival: deg q_K > deg p_K; then for every root c′ of p_K, deg q·mult(p,c′) ≥ deg q > deg p, so every root is searrow — **no northeast roots exist at K at all**. (c) A non-chain root c′ would give the tree vertex K ∗ εc′ (St 3.18; the 0-root always continues) with, by St 3.9(iii) + St 3.17(i) + Prop 8.1(i) + the St 6.2 computation (p. 29), K ∗ εc′ ∈ Ta& and deg p = i·mult(p^{red}, εc′) ≥ i ≥ 2; Prop 6.8 then manufactures a pole above it **on that branch** — necessarily one of the m poles of T_{a,pole} (this consumes no pole budget, which is why it scales to every m, replacing L1a's m=2-only third-pole counting); that pole's chain visits K through direction c′ (Not 3.3/Prop 3.2), making K a merge vertex — contradiction with K strictly pre-merge. So p_K = single simple ν-orbit, dp = ν. (d) Root law + eta law [P2] (exact order/residue counting on (iv): at a p-root of mult μ, mult(q) = 1 forced; off-p q-roots simple; η-residue b ≡ 1 mod ν): dq = nν + 1, M_K = gcd(ν, nν+1) = 1 — verbatim the thesis's own step in St 9.6's proof (p. 52). (e) λ_K = 0: no direction in Ta% exists (b); the q-extras at non-roots of p have no tree continuation (St 3.18). (f) No ray separates: all full-pattern roots lie in one ν-orbit with a unique continuing representative (St 3.18; Prop 5.6's proof, p. 27). At the merge arrival: St 8.4 at (G_i, H_i) gives μ_i = 1. ∎
    91	
    92	### D6 (MP6)
    93	Merge ≠ pole: an arriving direction has full multiplicity deg p_{H_e} ≥ 2, contradicting Prop 5.3(v) squarefreeness. Let some μ_j = 1. (a) k = 0: exactly the D5(c) manufacture, now read at G — every root of p_G supports, via Prop 6.8's same-branch pole, an incoming chain of one of the m poles; the roots of p_G are precisely the r arriving directions, in distinct ν-orbits (St 3.18: one continuation per orbit). (b) Equal-quotient: deg p_{H_e} = mult(p_G^{full}, c_e) = i·μ_e (St 3.17(i) + Prop 8.1(i): p^{full} = ⊖p^i); with μ_j = 1, i = deg p_{H_j} ≥ 2. (c) q-shape by root/eta laws [P2] as in D5(d). (d) Arithmetic: dq = (r+l)ν + 1 ≡ 1 (mod ν) forces gcd(M_G, ν) = 1 (Prop 8.1(v): M_G = gcd(dp, dq)); with dp = (Σμ_e)ν, any common divisor is coprime to ν hence divides Σμ_e: M_G = gcd(Σμ_e, (r+l)ν+1) | Σμ_e ≤ ΣM_{H_e} (St 8.4). All-μ=1 IIa: d | (r+l)ν+1 ⇒ gcd(d,ν) = 1 ⇒ (d | rν ⇔ d | r), and (r+l)ν+1 ≡ lν+1 (mod d): **gcd(rν,(r+l)ν+1) = gcd(r, lν+1)** exactly (A1's "divides" upgraded to A2/A3's equality; elementary both ways). ZCH: dp = (r−1)ν+1, difference lν, coprimality to ν gives M = gcd((r−1)ν+1, l). ν = 1: q = p·s, M = gcd(r, r+l) = gcd(r,l). (Machine-swept: r ≤ 9, ν ≤ 12, l ≤ 12, mixed μ-vectors; reproduces every recorded engine cell — (2,3,1) → 2; ZCH (2,2,3) → 3; ν=1 (2,l=2) → 2.) (e) λ_G = 0 as in D5(e). ∎
    94	
    95	### D7 (MP7)
    96	l = 0 kills: IIa: M = gcd(r,1) = 1. ZCH/ν=1: l = 0 forces q = p, and (iv) becomes (δ−1+u)pp′ = ⊖p, i.e. p′ = const ≠ 0, i.e. deg p = 1 — below ν+1 resp. 2 ≤ r: impossible. Cascade: Prop 8.3(i) propagates M = 1 down merge-free segments (regular steps, D2); at an M = 1-emitting merge the cascade continues (M_G = 1 known by direct gcd; steps below regular until the next merge). If the cascade reaches G\* with M = 1 and G\* ≠ (0,y), D3 gives the contradiction — so some merge at or above G\* breaks M = 1: a jump, with the D6 anatomy, and (all entries M = 1 ⇒ the FIRST break is an all-μ=1 merge) the resonance l ≥ 1 and 2 ≤ M ≤ r ≤ m outside ZCH. Entry forcing is D4. Root merge: (0,y) ∈ Ta& (d = l_f < k_f = deg p_{(0,y)}, Thm 6.1 read as the Ta&-inequality at π = 0), so D6 applies at (0,y) with ν = 1 (St 9.2(ii)); top-cancellation of (iv) (St 8.2's proof computation, forced since dq ≥ 2, u = 0, δ = l_f/i) gives l_f = i·r/(r+l) and k_f = i·r, hence **k_f = (r+l)·l_f** and ψ = ⌈k_f/l_f⌉ − 1 = r+l−1 (St 9.4). Prop 8.3(iii) fails (r ≥ 2 roots): no M = 1 kill at the root merge. ∎
    97	
    98	### D8 (MP8)
    99	Claim: every branch P ∈ Ra\R̄a through the pure M=1 forest or an all-M=1 merge has F\*_P ∈ T_{a,pole}. Ascend along P: at segment vertices the full pattern is a single simple orbit (D5), at all-M=1 merges all roots are chain roots (D6a), at poles the branch either separates above (where deg p = 1 by St 3.17(i) + Prop 5.3(v), and St 3.16 excludes Va-membership there and above) or continues along the defining branch (Prop 5.3(ix)). So P passes through a pole vertex Q₀, and since m_F is a vertex invariant, F\*_P = Q₀ ∈ T_{a,pole}. St 7.2 (p. 35) then bans cv vertices on P; Y(F) = ∅ (literally when M = 1 holds from the pole down: every ray through the segment reaches P_i, g(P) = ∞ by Prop 5.5, no cv vertex by Prop 7.2; under the E9/H2 branch-at-F reading for mid-segment onset); λ_F = 0 (St 9.3 (24)). Ledger itemization of the equality (22), extending SHEET6-LROOT §1 to m poles: (i) pole clusters carry zero cv mass (Prop 5.5 + Prop 7.2, per pole); (ii) chain paths carry none (T_{a,cv} ⊂ T_a^0 = {d = 0}, Not 7.1, while d > 0 down to d_{(0,y)} = l_f > 0); (iii) M=1 pre-merge sub-segments: identically zero rows (D5(f)); (iv) μ=1-arrival merges: zero rows (D6e) — the l q-extras are exhibited EMPTY ledger rows; (v) the x-side keeps its ≥ ψ cost (St 9.4's proof, p. 49). Since (22) is an Euler-characteristic *equality*, no re-partition or refinement of the printed counting frame can price these objects: "≥ 1 unit per M=1 occurrence" is structurally false at every m, td. The only remaining per-pole cost is td = ΣΛ_i ≥ mβ (Props 5.7/5.8): m ≤ td/3. ∎
   100	
   101	### D9 (MP9)
   102	m = 2, b = (1,1): D5 forces both chains M=1/λ=0 single-orbit, μ = (1,1) at the meet. Interior meet: r = 2 in D6d, M = gcd(2, lν+1); M = 1 is killed at G\* by D3, so M = 2, i.e. lν odd: l odd ≥ 1 (l = 0 gives gcd(2ν, 2ν+1) = 1), ν odd. ν = 1: (iv) reduces to 2ps′ − l p′s = c′ ≠ 0 (ρ = 2/(2+l), L1 §4's reduction re-derived); l even: divide by p^{(l+2)/2} — (s·p^{−l/2})′ = (c′/2)p^{−(l+2)/2}, whose partial-fraction residue at each root is C(−n, n−1)(a₁−a₂)^{1−2n} with n = (l+2)/2 and C(−n,n−1) = (−1)^{n−1}·C(2n−2, n−1) ≠ 0 for ALL n ≥ 2 (exact; machine-verified n = 2..6) — a log term, so no rational s exists unless c′ = 0, contra ⊖ ≠ 0. This holds at ALL even l, td-uniformly (upgrading L1b beyond its engine caps). l odd gives M = gcd(2, 2+l) = 1, killed. Survivors: IIa(l odd, ν ≥ 3 odd) / ZCH(gcd(ν+1,l) ≥ 2) — exactly the L1 §3 blind-spot family, spend 0. Root meet: ν = 1 (St 9.2(ii)); l = 0: root law gives q = p and (iv) reads 0 = ⊖p ≠ 0 — impossible; l even: the same log-obstruction (u = 0 changes nothing); l odd: locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2, machine-verified exact), no M = 1 kill (Prop 8.3(iii) fails: two predecessors); printed pins: k_f = (2+l)l_f (D7 at r = 2), ψ = l+1 admissible, Σλ = 0 ⇒ l ≤ td−2 (St 9.4 (25)); [+H1] Prop 9.3(d) with child (ν,κ̄,D) = (1,1,l_f) gives 1 = (κ̄_i + n_i)/ν_i, n_i ≥ 1, so κ̄_i ≤ ν_i − 1 at both parents. td = 6: empty by reach (2POLE §5b phase 3). ∎
   116	- **H1** (Prop 9.3(a)–(d) printed-step arithmetic): used only in MP9's root-residual κ̄ < ν clause.
   117	
   118	**Engine caps (flagged, not closed):** the ν = 1 interior-merge variant with an η-factor in q (legal only at ν = 1) is excluded only for l ≤ 4 (cases/l1_ode_check.py families B/B-η).
   119	
   120	**Open, stated, NOT claimed:** mixed merges with all μ_e ≥ 2 obey only MP6(b)/(d)-subadditivity (k = 0 needs some μ_e = 1; the l ≥ 1 forcing does not apply) — possible only for m ≥ 3 downstream of an earlier jump; the m ≥ 3 pattern-level escape (M = m via lν ≡ −1 mod m) is arithmetic existence only, r-edge H1 ratio-consistency unverified; the root-merge endgame at general td is open (closed at td = 6, m = 2); jump vertices are unkillable at printed tier (witness O — this is a theorem-grade negative, not a gap in the proof).
   121	
   122	**Record caveats:** (i) A2's third adversarial vote flagged one *subsidiary* (non-load-bearing) sub-claim as failing and one unflagged record-contradiction; the vote explicitly lists all Theorem M clauses (1)–(4), (5I), the conditional content of (5R), and Prop B as surviving, and every A2 clause grafted here is cross-derived by A1 or so listed. (ii) A3's adversarial votes were truncated in the synthesis input; A3 clauses P1/P3/P4 are independently derived by A1/A2 and grafted at full tier; A3-unique kills are quarantined in §7.
   123	
   124	---
   125	
   126	## 5. The obstruction half, stated precisely
   127	
   128	**Theorem O.** No printed-tier argument can prove M_F ≠ 1 on pre-merge segments (it is false: MP5 forces M = 1 there whenever b_i = 1, which is itself forced at td = mβ and at prime Λ_i), and no printed-tier argument can exclude resonant jump vertices: the cell (r,ν,l) = (2,3,1), M = 2 at td = 6, m = 2 solves Prop 8.1(iv) exactly with rigid coefficients (a₁/a₂ = 2±√3), passes Prop 8.1(iv)-(v), St 8.2/8.4, the root/eta laws, all located budget statements (Σλ = 2 ≤ 3 globally, 0 through the merge), and the entry pins — machine-verified (cases/l1_ode_check.py; SHEET6-2POLE §6a full hand-verified exhibit, every datum absolute). The blind spot is structural and r-uniform: the l extra q-orbits are invisible to every printed statement except deg q (SHEET6-L1 §3). Combined with MP8 (spend 0), the residual is irreducible: **MP0–MP9 is the maximal printed-tier kill**, and the multi-pole problem reduces, for each (m, td), to the finite book of resonant jump cells pinned by MP6/MP7 + the equal-quotient law + Prop 9.3's per-edge ratio equations (pp. 50–51), with entries pinned by MP4.
   129	
   130	---
   398	(iii) phase-3 root filter can be strengthened to w < 1 (§5d), which also
   399	subsumes the κ̄ < ν pin via case (IV)(j).
   400	
   401	---
   402	
   403	## 9. Honest perimeter
   404	
   405	- **Tier.** DS1 is printed-tier over promoted MP5 (St 3.16 iff + Not
   406	  3.4/3.5 + Def 3.1 + Prop 3.1 + St 3.17(i); the lattice argument in
   407	  DS1(d) is elementary arithmetic of Defs 3.1–3.3). DS2–DS4 are H1
   408	  (Prop 9.3 (a)–(h), (i)–(m) printed-step arithmetic), the tier already
   409	  sanctioned for MP9's root clause and the review's §5a bounds. No new
   410	  hypotheses beyond MP's P1/P2/P3/P4 + H1; E9/H2 not used.
   411	- **Entry edge.** The first step out of a pole vertex with ν_pole = 1
   412	  (Prop 5.5 case (i), pole vertex ∈ V_{2,a}) is grounded as in MP/the
   413	  engines (H1 per-edge use from the entry frame); DS1 applies from F_1
   414	  down regardless. Entry vertices with ν ≥ 2 are themselves V_1 (Prop 5.5
   415	  case (ii)) and need no special treatment.
   416	- **Scope.** The lemma closes the M=1 axis — exactly the F5 demotion. Out
   417	  of scope, as in MP: mixed merges with all μ_e ≥ 2 (m ≥ 3, quarantined),
   418	  the coefficient layer (Prop 8.1(iv) rigid solve vs ratio match, MP §8
   419	  item 3), m ≥ 3 reachability of Theorem O's pattern-level escape, and
   420	  M ≥ 2 suffix chains — though check 5 (St 9.6(v) conserves w = 3/2)
   421	  strongly suggests the same closure mechanism governs the suffix; the
   422	  suffix engine (hiii_compose) is anyway kill-complete per instance.
   423	- **Menus.** "Stabilizes" is proved for the cumulative menu (what the
   424	  book enumerates); per-depth menus can only shed transient-w items after
   425	  d₀, never gain. Caps in the checker (ν ≤ 24/48, l ≤ 8/12, n_pat ≤ 8)
   426	  affect only which INSTANCES are swept, not the menu conclusions, which
   427	  are cap-free via §5b's determination equations; the resonance test
   428	  Δ | num(w) is exact and cap-free.
   429	- **Not claimed.** No bound on segment depth itself (impossible from
   430	  (m, td): §2 R1); no claim that every W-value or menu cell is REALIZED
   431	  by an absolute (f,g) — the book remains conservative (P-realizability
   432	  untracked), exactly as in the promoted engines.
   324	- 2026-08-12 (0827409): THEOREM MP LANDS (multipole panel, 21 agents, 3.2M tokens): the td-ladder bottleneck is SETTLED at the structural level — verbatim m-pole 8.4 is FALSE, but the maximal kill + merge calculus reduces EVERY (m,td) multi-pole configuration to a finite book of resonant jump-vertex cells (2<=M<=r<=m, l>=1, full anatomy pinned). All 5 angles survived their refuters. Combined with prime-td + conj:R-now-theorem: the JC2 exclusion program is now finite-book at every level. NEXT: enumerate + bash the jump-vertex book (workflow-shaped); sigray-audit still running.
   325	- 2026-08-12 (88186fd): SIGRAY FULL AUDIT (35 agents, 130 statements, 3.7M tokens): 10 NEW errata + 10 gaps found; every one triaged for campaign damage — NET RESULT: no promoted result damaged; multiple campaign readings PROVEN forced (H5a upgraded to printed-statement-forced via St 3.8; d_{f-a} reading mandatory via St 3.13/3.14). The thesis's section 2-6 foundations are now swept; the campaign's hypothesis perimeter is dramatically de-risked. Filing amendments owed (H3 quote, E-numbering of new errata) — doc-chore agent when slots free. MP integration review + cut review still out.
   326	- 2026-08-12 (eb0abdf): MP promoted (MP0-MP8+O; MP9 corrected; finiteness rider demoted to per-frame). THE one open axis = chain-depth closure lemma — max-depth agent launched (stabilization orbit-map / Puiseux jump-count angles). If it lands: jump-vertex book FINITE per (m,td), and with prime-td + conj:R theorem + MP, the whole exclusion program becomes a finite enumeration at every level — the shape of a full JC2 proof modulo bashing the book.
   327	- 2026-08-12 (depth): CHAIN-DEPTH CLOSURE LEMMA PROVED (SHEET6-DEPTH.md) — the M=1 chain step conserves w := (kap-rho)/nu on every l=0 step (the unbounded direction), resonant steps need Delta | num(w) and contract by <= 2/3, and the ENTIRE jump-cell menu factors through w (handshake kap_m - D/i = w; join forces equal w; nu determined per (kap_m,l)). Depth-invariance follows: menu constant beyond d0 = gen(W)+2. td=6: W={2}, menu == the promoted (2,3,1) cell exactly (explains 351/351). Bonuses: root merges need w<1 (one-line root kill); ZCH 0-edge is Prop 9.3 case (III) => needs w-ratio nu>=2 between chains (engine model corrected, no promoted conclusion touched); St 9.6(v) itself conserves w=3/2. 13/13 exact checks (cases/depth_closure_check.py). CONSEQUENCE: jump-vertex book FINITE per (m,td) — MP's demoted rider RESTORED (corrected book spec in SHEET6-DEPTH.md sec 8). The exclusion program is now a finite enumeration at every level, unconditionally at H1 tier.
   328	- 2026-08-12 (2c81954): DEPTH CLOSURE LEMMA claimed (w-conservation; book finite per (m,td)) — max review launched (a case-branch drift or normalization mismatch would fake it; SIGRAY-AUDIT interaction checked). If it stands: launch the jump-book enumeration workflow with the reviewed spec — the program's final computational phase.
   329	- 2026-08-12 (400b50b): DEPTH LEMMA PROMOTED — BOOK(m,td) enumeration is GO; enumerator agent launched (td 6-14, gate = td-6 record reproduction; mechanical kills inline; survivors banked for per-cell bash). The pipeline: prime-td theorem + Theorem MP + depth lemma + book bash = multi-pole exclusion per td; combined with conj:R theorem + degree farm = the full JC2 program, now finite at every level.
   330	- 2026-08-12 (book): BOOK(m,td) ENUMERATED (cases/book_enum.py, BOOK-ENUM.md, systems/book/*.json): td=6..14, m=2..floor(td/3), reviewed spec E/T/C'/J'/R/S with the mechanical arsenal inline (MP7 l=0, gcd menu M>=2, kap-window integrality, corrected ZCH case-(III) w-ratio, root w<1, MP9 even-l, St 9.4 root budget). GATE PASS: td=6 m=2 == the promoted record cell-for-cell (unique residue-A IIa (2,3,1) M=2 child (5,3,1/2), R empty). RESULT: 421 cells, 346 killed, 75 survivors = only 22 distinct classes (31 IIa — ALL l=1, M=r, the Theorem-O escape pattern; 33 ZCH — only at w in {4,6} with an integer-ratio partner, first at td=9; 11 family-I — only r>=3, m>=3; 0 ROOT anywhere: every alphabet sits at w>=1, td-uniform root kill). Prime td 7/11/13 panels EMPTY (all entries off-axis b>=2 — the multi-pole shadow of the prime theorem). Largest class: residue-A in 10/18 panels; largest panel m=4 td=12 (21 cells). NEXT: per-cell bash — Prop 8.1(iv) rigid solve + coefficient-vs-ratio match (IIa l=1 family first), suffix engine from child data at budget td-2, r>=3 log-obstruction for family I, M>=2 chain engine for the 27 off-axis entry classes.
   331	- 2026-08-12 (bd4baa2): BOOK BASH WORKFLOW launched (22 classes, full arsenal, adversarial votes per kill). If it drains the book: td 6-14 exclusion reduces to residue-A-type coefficient templates only — the program's endgame at every level. Prime td 7/11/13 already FULLY excluded.
   332	- 2026-08-12 (5c6724b): BOOK BASH round 1 — 3 classes + 1 panel KILLED (frame-free T1 kills incl all 7 ZCH(2,2,3) panels); 6 survive to rigid one-scale templates; THE PICTURE SHARPENS: residue-A IIa(2,3,1) is in every nonempty panel and survives everywhere — the ladder's global bottleneck is ONE template family. Workflow resumed for the 13 unbashed ZCH/I classes (cache replay + live fill).
   333	- 2026-08-12 (r2 interim): BOOK BASH ROUND 2 — 12 of 13 classes DEAD by first pass (only ZCH(2,3,2)M2@w6 survives); BUT the credit ceiling killed ~13 verify votes mid-run, so several 'confirmed' flags were VACUOUS (empty vote arrays). Credits restored; workflow resumed with cached bash results — live verifies + synthesis filling now. If kills hold: book = 7 surviving classes total, ALL of the rigid-template kind.
   334	- 2026-08-12 (fbcd663): BOOK FULLY ADJUDICATED — 22 classes, 75 instances: 15 classes DEAD (closed-form kill criteria discovered: ZCH iff (nu+1)|l, family-I iff l/r or r/l in Z — these are little theorems in their own right), 7 SURVIVE, every survivor a rigid one-scale template. CREDIT CEILING hit again mid-verifies (resets Aug 15 8pm PT): 7 r2 kills carry engine-verification only, review votes OWED; cut-transform review agent presumed dead the same way. Agent work PAUSED until credits; local+fleet compute continues. Standing queue on credit restore: (1) r2 verify votes, (2) cut-transform review relaunch, (3) ZCH(2,2,3)@w4 r1 votes.
   335	- 2026-08-12: cut transform PROMOTED (review passed; deg<=150 pipeline now fully load-bearing incl the stuck-7). Bound-150 blockers remaining: farm queue drain + big-core memory tier + two-machine replication decision + audit pass.
   336	- 2026-08-12 (9fff9fc): BOOK FULLY CONFIRMED (all r2 kills 2-vote). TEMPLATE-FAMILY ATTACK workflow launched — 5 angles on the shared mechanism of the 7 survivors: GALOIS descent (new — the templates live in Q(sqrt d), conjugation swaps the poles; one non-symmetric pinned datum kills), the L1 sec-7.2 global h1-budget (the identified missing layer), panel budget squeeze (b>=2 entries may not reach mu=1 arrivals), classical battery on the 6 untested templates (zero-slack valuation test), and Weyl quantization (DC2 divergence as a weapon). This is the shot at closing td<=14 multi-pole outright.
   337	- 2026-08-12 (33799c7): TEMPLATE ATTACK LANDS — book 27->23 (new law L6); three shield theorems prove Galois/budget/quantum have ZERO traction (templates conjugation-equivariant BY RIGIDITY — deep and slightly ominous); quantum divergence concentrates at the ONE resonant direction b. Everything now points at the same coordinates: L1 sec-7.2 coefficient tier at direction b.
   338	- GROK 4.6 EVAL (xmodel/grok-eval-20260812.md): impressively deep repo read; P(JC2 true) ~0.72; 5 avenues incl. S_6 monodromy product test (covering-theoretic, Sigray-independent — GOOD and new), J-jet at G_m on the 7 dead-stretch coeffs (overlaps our R1 but sharper framing), Theorem-A-on-depth-3-column (cheap, connects our two lanes), mixed-merge completeness crack (checks our book's quarantine). Also flags the cheapest logged-but-unrun shot: IIa(3,5,1) W-residual deg-2-vs-<=1.

collab: Wait
2026-08-12T20:09:10.657029Z ERROR codex_core::tools::router: error=timeout_ms must be at least 10000
exec
/bin/zsh -lc "rg -n -C 8 \"k = 0|pole manufacture|manufacture|St 6\\.2|T_a.?\\+|d_H\" SHEET6-MP-REVIEW.md SHEET6-A3L1-REVIEW.md SHEET6-2POLE.md SHEET6-L1.md SHEET6-III.md SHEET6-AF2.md | head -n 300" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
SHEET6-MP-REVIEW.md-46-promoted sheets:
SHEET6-MP-REVIEW.md-47-
SHEET6-MP-REVIEW.md-48-| clause | source per §9 | independent in-doc derivation | promoted-record anchor |
SHEET6-MP-REVIEW.md-49-|---|---|---|---|
SHEET6-MP-REVIEW.md-50-| MP0 | A1/A2 (cross) | D1: Prop 6.8 + St 3.16/3.17(i) + Prop 5.3(v) | 2POLE §1b/§1c |
SHEET6-MP-REVIEW.md-51-| MP1 | A2 (unique-predecessor adopted) | D2: edge count Σ(r−1) = −1 + m leaves (verified: gives m−1) | 2POLE §1c(ii) at m=2 |
SHEET6-MP-REVIEW.md-52-| MP2/MP3 | A1.T2 = A2(4); A1.T3 correction | D3: P1 + 8.3(iii) single-root + p.45 Bezout | 2POLE §1c(iii) |
SHEET6-MP-REVIEW.md-53-| MP4 | A2(1) ⊇ A1's β-minimal | D4: (19) + St 5.2 + St 2.1 arithmetic (re-done here, §3b) | L1a(a)/A3L1 fronts 1–2 |
SHEET6-MP-REVIEW.md:54:| MP5 | A1/A2 (k=0 manufacture in both, §9) | D5: St 8.4/8.2 + Prop 6.8 same-branch | L1a(b) |
SHEET6-MP-REVIEW.md-55-| MP6 | A1.T4/T5 = A2(3) = A3.P4 | D6: St 3.17(i)/8.1(i)/(v) + gcd arithmetic | L1a(c) 3-shape menu |
SHEET6-MP-REVIEW.md-56-| MP7 | A1/A2 | D7: gcd + (iv) degeneration + St 9.2(ii) | L1 §0/§4 |
SHEET6-MP-REVIEW.md-57-| MP8 | A1.T7 = A2.Prop B | D8: (22) itemization + F*_P argument | LROOT §1–2 |
SHEET6-MP-REVIEW.md-58-| MP9 | A1/A2 + D9's new residue closed form | D9 | L1 §4–§6, 2POLE §4b/§5b |
SHEET6-MP-REVIEW.md-59-
SHEET6-MP-REVIEW.md-60-- **Quarantine honored.** The three §7 blocks (prime-partition kill,
SHEET6-MP-REVIEW.md-61-  RH-lemma kills, OB extension (3,5,1)/(4,7,1)) were grepped against
SHEET6-MP-REVIEW.md-62-  MP0–MP9, §0, §5, §6, §8. No leak. The two near-misses are clean:
--
SHEET6-MP-REVIEW.md-152-any reuse at general td (where the doc correctly marks the residual OPEN).
SHEET6-MP-REVIEW.md-153-Same tier as before (H1 + capped sweep) — no tier change, no new survivor.
SHEET6-MP-REVIEW.md-154-
SHEET6-MP-REVIEW.md-155-## 3. Front 3 — page fidelity (all six re-read on-page this session)
SHEET6-MP-REVIEW.md-156-
SHEET6-MP-REVIEW.md-157-1. **Prop 6.8 (p. 34)**: verbatim "Set F ∈ Ta&. Assume deg(p_F) ≠ 1. Then
SHEET6-MP-REVIEW.md-158-   there exist P ∈ R̄_a\R_a, u,v ∈ Q⁺ with (i) F = I_P(u); (ii) v ≥ u;
SHEET6-MP-REVIEW.md-159-   (iii) I_P(v) ∈ T_{a,pole}." Same P, parameter above u — the same-branch
SHEET6-MP-REVIEW.md:160:   pole manufacture MP0/D5(c)/D6(a) uses. CONFIRMED (note the hypothesis
SHEET6-MP-REVIEW.md-161-   deg p_F ≠ 1: every MP application supplies deg p ≥ 2 via St 3.16/3.17(i)).
SHEET6-MP-REVIEW.md-162-2. **Not 8.1 (p. 39)**: M_F := gcd(deg p_F, deg p_{h_0,F},…,deg p_{h_m,F}),
SHEET6-MP-REVIEW.md-163-   h_i per Prop 4.2 (h_0 = g). CONFIRMED (with m_F = 0 at poles this is
SHEET6-MP-REVIEW.md-164-   exactly D4's pin).
SHEET6-MP-REVIEW.md-165-3. **Prop 8.1 (pp. 39–41)**: F ∈ Ta&, u = π(F), i := deg(p_F)/M*_F ∈ N*;
SHEET6-MP-REVIEW.md-166-   (i) (ξ^δp)^i = ⊖f_F⁺ (so p_full = p^i — D6(b)'s ground); (iv)
SHEET6-MP-REVIEW.md-167-   δpq′ − (1−u)p′q = ⊖p; (v) M_F = gcd(deg p, deg q); proof line
SHEET6-MP-REVIEW.md-168-   deg(p) = M*_F. CONFIRMED, exactly as used in D5–D9.
--
SHEET6-MP-REVIEW.md-216-
SHEET6-MP-REVIEW.md-217-## 5. Front 5 — the reduction claim (the review's main deliverable)
SHEET6-MP-REVIEW.md-218-
SHEET6-MP-REVIEW.md-219-### 5a. What is actually proven
SHEET6-MP-REVIEW.md-220-
SHEET6-MP-REVIEW.md-221-Finitely many at printed tier, per (m, td): types and entries (D4:
SHEET6-MP-REVIEW.md-222-partitions td = ΣΛ_i, Λ_i ≥ β; finitely many (a_i,b_i,ν_i) per Λ_i via
SHEET6-MP-REVIEW.md-223-(19) + St 5.2(ii)); tree shapes (MP1: ≤ m−1 merges, Σ(r−1) = m−1, r ≤ m);
SHEET6-MP-REVIEW.md:224:merge-local anatomy (MP6: μ⃗ = 1 at all-M=1 merges, k = 0, family ∈
SHEET6-MP-REVIEW.md-225-{IIa, ZCH, I}, M from the gcd menu, M | r ≤ m outside ZCH, gcd(M,ν) = 1);
SHEET6-MP-REVIEW.md-226-root cells (ν = 1, l ≤ td−2 via ψ = r+l−1 and (25) — finite per td). At H1
SHEET6-MP-REVIEW.md-227-tier, the per-edge Prop 9.3 equations make (l, n_e, ν) **finite per parent
SHEET6-MP-REVIEW.md-228-frame**: for the all-μ=1 IIa jump, cross-multiplying (b) gives
SHEET6-MP-REVIEW.md-229-ν·(rκ̄_e − (r+l)ρ_e − l·n_e) = ρ_e + n_e, so n_e ≤ (rκ̄_e − (r+l)ρ_e −1)/l,
SHEET6-MP-REVIEW.md-230-l ≤ (r(κ̄_e − ρ_e) − 1)/(ρ_e + 1), and each admissible (l, n_e) DETERMINES
SHEET6-MP-REVIEW.md-231-ν. This is real and enumeration-ready.
SHEET6-MP-REVIEW.md-232-
--
SHEET6-MP-REVIEW.md-266-    C. Chain layer (H1; the unbounded direction): per edge, step frames
SHEET6-MP-REVIEW.md-267-       (ρ, ν, κ̄, M) evolve by Prop 9.3(a)–(d) with n ≥ 1,
SHEET6-MP-REVIEW.md-268-       n ≡ −κ̄ (mod ν); M = 1 segments are forced single-simple-orbit,
SHEET6-MP-REVIEW.md-269-       λ = 0 (MP5); depth cap OR closure lemma REQUIRED here.
SHEET6-MP-REVIEW.md-270-    J. Jump cells (printed anatomy + H1 reach; finite per frame):
SHEET6-MP-REVIEW.md-271-       family ∈ {IIa: (dp,dq) = (rν,(r+l)ν+1), M = gcd(r, lν+1);
SHEET6-MP-REVIEW.md-272-       ZCH: ((r−1)ν+1,(r−1+l)ν+1), M = gcd((r−1)ν+1, l);
SHEET6-MP-REVIEW.md-273-       I: (r, r+l), M = gcd(r,l)}; constraints: μ_e | M_{H_e} (= 1 on
SHEET6-MP-REVIEW.md:274:       all-M=1 ancestry), k = 0, common i ≥ 2 with deg p_{H_e} = iμ_e,
SHEET6-MP-REVIEW.md-275-       l ≥ 1, M ≥ 2, gcd(M,ν) = 1, M | r ≤ m outside ZCH; per-edge reach:
SHEET6-MP-REVIEW.md-276-       dp/dq = μ_e(ρ_e+n_e)/(κ̄_e+n_e), n_e ≥ 1, n_e ≡ −κ̄_e (mod ν_e),
SHEET6-MP-REVIEW.md-277-       common child (κ̄, D, i) — bounds n_e, l and determines ν per frame
SHEET6-MP-REVIEW.md-278-       (§5a). Coefficient layer: Prop 8.1(iv) rigid solve (à la
SHEET6-MP-REVIEW.md-279-       l1_ode_check families A/Z), then the §8-item-3 coefficient-vs-ratio
SHEET6-MP-REVIEW.md-280-       match (never yet run).
SHEET6-MP-REVIEW.md-281-    R. Root cells (printed + H1; finite per td): ν = 1, all-μ=1, l odd,
SHEET6-MP-REVIEW.md-282-       l ≤ td−2, k_f = (r+l)l_f, ψ = r+l−1, both parents κ̄ < ν (Prop
--
SHEET6-L1.md-10-on-page (printed page = pdf page). Engines: cases/twopole_check.py (new
SHEET6-L1.md-11-additive PHASE 4 `l1_stage`; phases 1-3 untouched, baseline reproduced)
SHEET6-L1.md-12-and cases/l1_ode_check.py (new: exact coefficient solver for Prop 8.1(iv)
SHEET6-L1.md-13-at the merge and suffix patterns).
SHEET6-L1.md-14-
SHEET6-L1.md-15-VERDICT: **PARTIAL — proved for every family except one, where it is
SHEET6-L1.md-16-FALSE at every level the printed thesis can see.**
SHEET6-L1.md-17-(i) L1a (§2, printed-tier): M = 1 propagates from the poles down BOTH
SHEET6-L1.md:18:pre-merge chains, forcing mu = (1,1), k = 0, lambda = 0 at any merge.
SHEET6-L1.md-19-This upgrades the A2P §2d entry-label kill of residue B to a structural
SHEET6-L1.md-20-merge-impossibility (mu = (2,2) cannot occur), re-kills A' independently
SHEET6-L1.md-21-of the AF2 pricing tier, and forces the full merged-pattern anatomy into
SHEET6-L1.md-22-three families (§0): IIa(l) [both chains at nonzero orbits], ZCH(l) [one
SHEET6-L1.md-23-chain at the 0-direction], I(l) [nu = 1] — the last two MISSING from
SHEET6-L1.md-24-every prior enumeration.
SHEET6-L1.md-25-(ii) L1 HOLDS on the two new families: nu = 1 is empty outright (L1b,
SHEET6-L1.md-26-§4: exact calculus on Prop 8.1(iv)); the zero-chain family is dead for
--
SHEET6-L1.md-48-reduced patterns of Prop 8.1 at G_m; mu_i = mult(p, c_i) at the two
SHEET6-L1.md-49-chain orbits; l = number of q-orbits at non-roots of p ("resonant
SHEET6-L1.md-50-q-orbit family"). L1 as posed in SHEET6-2POLE §6c:
SHEET6-L1.md-51-
SHEET6-L1.md-52-    (L1) At a V_{2,a} merge vertex with mu = (1,1), l >= 1 is
SHEET6-L1.md-53-    impossible. [Then l = 0 gives M(G_m) = gcd(2nu, 2nu+1) = 1, and the
SHEET6-L1.md-54-    restored Prop 8.4 kills the merge: the whole book closes.]
SHEET6-L1.md-55-
SHEET6-L1.md:56:Sharpened by L1a (§2): mu = (1,1) and k = 0 are forced, and the merged
SHEET6-L1.md-57-pattern falls into exactly three families (both chain orbits nonzero /
SHEET6-L1.md-58-one chain at the 0-direction / nu = 1), so L1 splits into three claims:
SHEET6-L1.md-59-  (L1-IIa) nu >= 2, p = (t-a_1)(t-a_2)|_{t=eta^nu}: l >= 1 impossible.
SHEET6-L1.md-60-           M = gcd(2nu,(l+2)nu+1) | 2; = 2 iff nu, l odd.
SHEET6-L1.md-61-           [FALSE locally at the unique reachable cell (nu,l) = (3,1), §5]
SHEET6-L1.md-62-  (L1-zch) nu >= 2, p = eta(eta^nu - c^nu) (one CHAIN at 0):
SHEET6-L1.md-63-           M = gcd(nu+1, (l+1)nu+1) = gcd(nu+1, l), unbounded a priori.
SHEET6-L1.md-64-           [TRUE for everything reachable: the only in-caps cell
--
SHEET6-L1.md-120-
SHEET6-L1.md-121-## 2. L1a: printed-tier forcing along the chains
SHEET6-L1.md-122-
SHEET6-L1.md-123-**Lemma L1a.** In the two-pole (3,3) configuration:
SHEET6-L1.md-124-(a) M_{P_1} = M_{P_2} = 1;
SHEET6-L1.md-125-(b) every chain vertex strictly above G_m has M = 1, reduced pattern a
SHEET6-L1.md-126-single SIMPLE nu-orbit (dp = nu_F, dq = n nu_F + 1, some n >= 1), and
SHEET6-L1.md-127-lambda = 0;
SHEET6-L1.md:128:(c) at G_m: mu_1 = mu_2 = 1 and no NON-CHAIN root of p exists (k = 0,
SHEET6-L1.md-129-and an eta-factor is excluded UNLESS the 0-direction carries one of the
SHEET6-L1.md-130-two chains); q = eta * rad(p)-part * (l extra simple nu-orbits) (root
SHEET6-L1.md-131-law + eta law). So exactly three shapes remain: IIa(l): p =
SHEET6-L1.md-132-(eta^nu-c_1^nu)(eta^nu-c_2^nu), (dp,dq) = (2nu, (l+2)nu+1); ZCH(l): one
SHEET6-L1.md-133-chain at 0, p = eta(eta^nu-c^nu), (dp,dq) = (nu+1, (l+1)nu+1); I(l):
SHEET6-L1.md-134-nu = 1, (dp,dq) = (2, 2+l); M(G_m) = gcd(dp,dq) in each case.
SHEET6-L1.md-135-
SHEET6-L1.md-136-[The "no eta-factor" clause of the older draft claims is stated
--
SHEET6-L1.md-146-gcd(4,6), St 9.6).
SHEET6-L1.md-147-(b) Induction down each pre-merge segment. Given M = 1 at the deeper
SHEET6-L1.md-148-vertex, St 8.4 makes the chain orbit simple in the child's reduced p.
SHEET6-L1.md-149-Any OTHER root c' of that p would pass the searrow test (the chain
SHEET6-L1.md-150-orbit's own test gives deg q * 1 > deg p, so deg q * mult(p,c') > deg p
SHEET6-L1.md-151-a fortiori — St 8.2 leaves no northeast option), creating a second
SHEET6-L1.md-152-searrow V_a-branch; the vertex above c' has deg p = i * mult >= 2
SHEET6-L1.md-153-(i = deg p of the deeper chain vertex >= 2, St 3.16/St 3.17(i)), so
SHEET6-L1.md:154:Prop 6.8 manufactures a pole in a subtree disjoint from both chains — a
SHEET6-L1.md-155-THIRD pole. So p is the single simple chain orbit; this is verbatim the
SHEET6-L1.md-156-thesis's mult(p,c) = 1 case (St 9.6's proof): dq = n nu + 1 and M_child
SHEET6-L1.md-157-= gcd(nu, n nu + 1) = 1. lambda = 0 because a lambda-charge needs a
SHEET6-L1.md-158-northeast direction (St 9.3's hypothesis) and none exists. Same
SHEET6-L1.md-159-argument at a root 0 (mult i * l_0 >= 2 since i >= 2).
SHEET6-L1.md-160-(c) At G_m, repeat (b)'s third-pole argument for every non-chain root of
SHEET6-L1.md-161-p (extra orbits, and 0 when neither chain sits there); mu_i | M_{H_i} =
SHEET6-L1.md-162-1 (St 8.4); c_1, c_2 lie in distinct nu-orbits (Prop 5.6's proof /
--
SHEET6-III.md-97-  two roots separate exactly at F. Q realizes a direction F ∗ c* with
SHEET6-III.md-98-  c* = c_{n'}(Q) ≠ 0 ⟹ c* is a nonzero root of p_F (St 3.18) ⟹ k ≥ 1 in the
SHEET6-III.md-99-  pattern, and under regularity the branch H := F + c* ∈ T_a% gives the
SHEET6-III.md-100-  thesis's λ_F ≥ 1 (St 9.3/9.4). [This is the thesis's entire printed use.]
SHEET6-III.md-101-  Side effect: St 8.5 (M-divisibility, p.42) requires parent ∉ V_{2,a}, so it
SHEET6-III.md-102-  can NEVER be applied against case III — no extra kill from 8.5.
SHEET6-III.md-103-- **(S3) p-pattern** [St 3.16 part 2]: p_F(η) = η^l p̃(η^{ν_F}) with l =
SHEET6-III.md-104-  mult(p_F,0), nonzero roots in full ν_F-orbits, exactly one direction per
SHEET6-III.md:105:  orbit (St 3.18 unique-ε). Regularity (St 6.2): other existing directions have
SHEET6-III.md-106-  mult < μ; thesis pattern takes the k orbits simple:
SHEET6-III.md-107-  **p(η) = η^μ (η^ν − c_1^ν)…(η^ν − c_k^ν)**, deg p = μ + kν, ν := ν_F.
SHEET6-III.md-108-- **(S4) q-pattern** [Prop 8.1(iv)]: ord_0 of δpq′ − (1−u)p′q = p forces
SHEET6-III.md-109-  mult(q, 0) = 1 exactly (l_q ≥ 2 gives ord > μ, l_q = 0 gives ord μ−1 with
SHEET6-III.md-110-  non-cancelling coefficient), and the Galois structure gives q = η q̃(η^ν):
SHEET6-III.md-111-  **deg q ≡ 1 (mod ν_F)**. The thesis (p.53/60) additionally takes q's orbit
SHEET6-III.md-112-  set equal to p's (deg q = 1 + kν, cited to St 8.2); the engine inherits that
SHEET6-III.md-113-  (pre-existing, part of H1/AF surface — unchanged here).
--
SHEET6-AF2.md-8-(text layer verified with pdftotext for every formula quoted below).
SHEET6-AF2.md-9-
SHEET6-AF2.md-10-VERDICT:
SHEET6-AF2.md-11-- **IIb is NOT free and NOT flat-1.** Derived price (§2-3), per solved cell:
SHEET6-AF2.md-12-  λ_IIb ≥ k·max(1, ⌈gap⌉) + max(1, ⌈gap/ν_F⌉), gap := D_F/i − κ̄_F —
SHEET6-AF2.md-13-  the k extra orbits price EXACTLY like I/IIa_k/III extra roots (same
SHEET6-AF2.md-14-  St 9.3 (24) mechanism), and the 0-root adds its own ν_F-discounted term.
SHEET6-AF2.md-15-  There is NO coherent free reading: for gap > 0 the extra directions are
SHEET6-AF2.md:16:  forced to climb by St 6.2 alone (regularity not even needed), they land in
SHEET6-AF2.md-17-  Y(F) by Notation 9.3, and (24) prices them; λ_F is by DEFINITION the sum.
SHEET6-AF2.md-18-- **Both sanctioned residual classes are EXCLUDED**: the single IIb μ=4 k=1
SHEET6-AF2.md-19-  step at r10/M4 that carries both has gap = 12 − 5 = 7, so λ_F ≥ 8 > 3 =
SHEET6-AF2.md-20-  td−2 ((26)/St 9.5 alone; ψ-budget not needed). The kill is sign-robust
SHEET6-AF2.md-21-  (§4): under the PRINTED (mis-signed) (24) the bound is 17 > 3.
SHEET6-AF2.md-22-- **Composed sanctioned residual (single-pole, td ≤ 6) = 0. SF1 residual = 0.
SHEET6-AF2.md-23-  AF3-superset book: 13 → 4** (§5).
SHEET6-AF2.md-24-- **AF2's general rule is now DERIVED from St 9.3 (24)** (§2), modulo one
--
SHEET6-AF2.md-75-Setting: one chain step G = F + c (Prop 9.3; F = G° ∈ V_a ∩ T_a↘ the new
SHEET6-AF2.md-76-node, G the ↘ continuation, c the special root, mult(p,c) = μ | M_G). The
SHEET6-AF2.md-77-reduced pattern p of Prop 8.1 has roots: the c-orbit (mult μ), possibly 0
SHEET6-AF2.md-78-(mult 1; exactly the IIb/III patterns), and k extra ν_F-orbits c_1..c_k
SHEET6-AF2.md-79-(templated simple). For any root c* of p with direction ≠ that of G:
SHEET6-AF2.md-80-
SHEET6-AF2.md-81-- (R1) F ∗ (εc*) exists (St 3.18) and H₁ := F + c* ∈ T_a⁺ (Prop 6.7;
SHEET6-AF2.md-82-  deg p_F > 1 whenever p has > 1 root, i.e. except the μ=1 M=1-kill).
SHEET6-AF2.md:83:- (R2) THE CLIMB. By St 6.2 (applied to the pair H₁ = F + c*):
SHEET6-AF2.md-84-  H₁ ∈ T_a↘ ⟺ d_F < (1−π(F))·mult(p_F, c*). Multiplying by κ_F > 0 and
SHEET6-AF2.md-85-  using D_F = κ_F d_F, κ̄_F = κ_F(1−π(F)), mult(p_F,c*) = i·w (Prop 8.1(i),
SHEET6-AF2.md-86-  w := mult(p, c*)):
SHEET6-AF2.md-87-      **H₁ ∈ T_a↘  ⟺  D_F/(i·w) < κ̄_F  ⟺  gap(c*) := D_F/(i·w) − κ̄_F < 0.**
SHEET6-AF2.md-88-  So if gap(c*) > 0, H₁ ∉ T_a↘, hence H₁ ∈ T_a↗ (St 6.1) — UNCONDITIONALLY,
SHEET6-AF2.md-89-  no regularity needed. If gap(c*) ≤ 0, H₁ ∈ T_a↗ still follows from
SHEET6-AF2.md-90-  regularity (Not 9.2: G is the only ↘ V_a vertex over F; H₁ ∈ V_a, H₁° = F,
SHEET6-AF2.md-91-  H₁ ≠ G since directions at F are distinct vertices) — this is the thesis's
--
SHEET6-AF2.md-121-## 3. Case dictionary: I/IIa/III reproduce AF2 exactly; IIb was underpriced
SHEET6-AF2.md-122-
SHEET6-AF2.md-123-Where the extra roots sit, per Prop 9.3 case (patterns pp. 52-54, verbatim):
SHEET6-AF2.md-124-- **I** (ν_F = 1): p = (η−c)^μ(η−c₁)…(η−c_k), k ≥ 1 (St 3.16). No 0-root.
SHEET6-AF2.md-125-  λ ≥ k·max(1,⌈gap⌉). Engine: identical. (Thesis prints only the floor
SHEET6-AF2.md-126-  λ ≥ 1, p. 54.)
SHEET6-AF2.md-127-- **IIa** (pattern (a)): p = (η^ν−c^ν)^μ Π_k. No 0-root. k ≥ 1:
SHEET6-AF2.md-128-  λ ≥ k·max(1,⌈gap⌉) — the thesis's own p. 53 λ ≥ 2/≥ 3/≥ 2 (A)/(B)/(C)
SHEET6-AF2.md:129:  are exactly this rule (§1). k = 0: no extra root, λ = 0 possible
SHEET6-AF2.md-130-  (9.6(v), printed). Engine: identical.
SHEET6-AF2.md-131-- **III**: p = η^μ Π_k (the S1 structure, SHEET6-III §2: c = 0 IS the ↘
SHEET6-AF2.md-132-  direction). Extra roots = the k ≥ 1 nonzero orbits: λ ≥ k·max(1,⌈gap⌉).
SHEET6-AF2.md-133-  No 0-term (0 is the continuation, not a climbing root). Engine (E5
SHEET6-AF2.md-134-  arithmetic in hiii_compose): identical.
SHEET6-AF2.md-135-- **IIb** (pattern (b)): p = η(η^ν−c^ν)^μ Π_k. The ↘ direction is the
SHEET6-AF2.md-136-  c-orbit (μ ≥ 2 > 1), so BOTH the 0-root AND the k orbits are climbing
SHEET6-AF2.md-137-  extras:
--
SHEET6-AF2.md-155-entry Q(G) = (4j,4j,4,4,9) --IIb μ=4, k=1, ν_F=7-->:
SHEET6-AF2.md-156-  pattern (b): deg p = 5·7+1 = 36, deg q = 2·7+1 = 15 (l = 0);
SHEET6-AF2.md-157-  i = deg(p_G)/μ = j; ratio (b): 36/15 = 4(1+n)/(9+n) ⇒ n = 11 (≡ 3 ≡
SHEET6-AF2.md-158-  −κ̄_G mod ν_G ✓); child Q(F) = (12j, 36j, 7, 3, 5) — St 9.7's own
SHEET6-AF2.md-159-  hypothesis shape (R1); R2 = (2/3,3s+2,3,2s+2) is its λ=0 IIa_0 child.
SHEET6-AF2.md-160-The step's price:
SHEET6-AF2.md-161-  gap = D_F/i − κ̄_F = 12 − 5 = **7**;   gap/ν_F = 1.
SHEET6-AF2.md-162-  - Climb: by (R2), the c₁-direction is in T_a↘ iff 12 < 5 — FALSE; the
SHEET6-AF2.md:163:    0-direction identically; both climb by St 6.2 + St 6.1 + Prop 6.7,
SHEET6-AF2.md-164-    NO regularity input.
SHEET6-AF2.md-165-  - Price: corrected (24): the two curve vertices contribute ≥ 7 and ≥ 1;
SHEET6-AF2.md-166-    λ_F ≥ 8. Integer bounds — no ⌈·⌉/integrality needed.
SHEET6-AF2.md-167-  - Budget: St 9.5/(26): Σ λ_{F_i} ≤ td − 2 = 3 over ANY characteristic
SHEET6-AF2.md-168-    sequence of a td=5 counterexample. 8 > 3 (already 7 > 3 on the orbit
SHEET6-AF2.md-169-    term alone). The step is impossible; R1 is never created, R2 never
SHEET6-AF2.md-170-    reached. **Both sanctioned residual classes EXCLUDED.**
SHEET6-AF2.md-171-  - Sign-robustness: under the PRINTED (uncorrected) (24) the bound is
--
SHEET6-AF2.md-263-
SHEET6-AF2.md-264-Engine change: sheet6_campaign.py IIB_DERIVED flag (default False) in
SHEET6-AF2.md-265-child_from — IIb λ = k·max(1,⌈gap⌉) + max(1,⌈gap/ν_F⌉) per-t with the
SHEET6-AF2.md-266-existing family-singleton/OPEN machinery; hiii_compose.py `iib` CLI arg.
SHEET6-AF2.md-267-Both runs re-executed this audit: baseline diff vs the promoted output is
SHEET6-AF2.md-268-empty; the `iib` run's only deltas are kills (survivor sets shrink, no new
SHEET6-AF2.md-269-OPEN kinds, frontier 0 everywhere). §4's step arithmetic hand-verified in
SHEET6-AF2.md-270-an inline exact script (child Q-datum, n = 11, M_F = 3, gap = 7, both
SHEET6-AF2.md:271:St 6.2 climb tests, 8 > 3 and 17 > 3).
--
SHEET6-2POLE.md-61-(Prop 9.2) are °-descents ending at (0,y); ° is deterministic, so they
SHEET6-2POLE.md-62-coalesce at a unique meet G_m and share the suffix from G_m to (0,y).
SHEET6-2POLE.md-63-Structure facts (all from printed statements):
SHEET6-2POLE.md-64-- (i) G_m is NOT a pole vertex: Prop 5.3(v) (p. 25) makes p squarefree at
SHEET6-2POLE.md-65-  pole vertices, while the incoming chain orbit has mult(p_{G_m}, c_i) =
SHEET6-2POLE.md-66-  deg(p_{H_i}) >= 2 (St 3.17(i), p. 18; H_i in Va so deg p_{H_i} >= 2 by
SHEET6-2POLE.md-67-  St 3.16). So each pre-merge segment has >= 1 edge (H_i = P_i allowed).
SHEET6-2POLE.md-68-- (ii) Regularity fails EXACTLY at G_m (over both H_1, H_2) and nowhere
SHEET6-2POLE.md:69:  else: a second regularity failure would manufacture a third pole via
SHEET6-2POLE.md-70-  Prop 6.8. Two sub-cases: interior merge (G_m != (0,y), G_m in V_{2,a})
SHEET6-2POLE.md-71-  or root merge (G_m = (0,y); then p_{(0,y)} has >= 2 roots, so (0,y) in
SHEET6-2POLE.md-72-  V_{2,a} — (0,y) in V_{1,a} is impossible — and BOTH terminal steps are
SHEET6-2POLE.md-73-  Prop 9.3 case (I), never case (IV): the case-IV hypothesis
SHEET6-2POLE.md-74-  "F not in V_{1,a} cup V_{2,a}" fails).
SHEET6-2POLE.md-75-- (iii) M=1 kill PARTIALLY RESTORED: for F on {G_m} cup (suffix), the
SHEET6-2POLE.md-76-  descent from F is regular at every step and (0,y) is regular over the
SHEET6-2POLE.md-77-  shared H := F_{n-1} (a second predecessor of any suffix vertex would be a
--
SHEET6-2POLE.md-225-  (ν,κ̄,D) = (1, 1, l_f) (St 9.2), so κ̄_i + n_i = ν_i, i.e. BOTH parents
SHEET6-2POLE.md-226-  need κ̄ < ν (the case-IV condition (j) reappears); ψ = ceil(k_f/l_f)−1
SHEET6-2POLE.md-227-  with k_f = i(μ_1+μ_2+k)·[+ other roots], l_f = D_root.
SHEET6-2POLE.md-228-
SHEET6-2POLE.md-229-### 4c. Two rigidity facts inside the calculus (exact)
SHEET6-2POLE.md-230-
SHEET6-2POLE.md-231-1. μ = 1 chains are λ-free but IIa_0-only: with μ = 1 the searrow test
SHEET6-2POLE.md-232-   for the chain orbit reads dq > dp, while a northeast extra needs
SHEET6-2POLE.md:233:   dq < dp — so k = 0 and the only admissible shapes are IIa_0-like
SHEET6-2POLE.md-234-   (dp = ν, dq = (l+1)ν+1), λ = 0. (I/IIb/III-like shapes force
SHEET6-2POLE.md-235-   dp/dq = 1 = ratio, impossible since ρ < κ̄.) Consequence: M=1 ancestry
SHEET6-2POLE.md-236-   (μ=1 forced, §2c) descends λ-free — the budget CANNOT kill M=1
SHEET6-2POLE.md-237-   pre-merge segments; only the merge-time M-kill (§4b) can.
SHEET6-2POLE.md-238-2. Root-merge ratio rigidity at μ_1 = μ_2 = 1: the I-like merged ratio is
SHEET6-2POLE.md-239-   (2+k)/(k+2) = 1 — impossible. So two M=1 chains can never terminate
SHEET6-2POLE.md-240-   together at (0,y); an M=1 chain must merge INTO an interior vertex.
SHEET6-2POLE.md-241-   Root merges need μ_1 + μ_2 + k > k + 2, i.e. some μ_i >= 2, i.e. at
SHEET6-2POLE.md-242-   least one chain arrives with M >= 2 at a κ̄ < ν vertex.
SHEET6-2POLE.md-243-
SHEET6-2POLE.md-244-## 5. Budget arithmetic and engine runs (cases/twopole_check.py)
SHEET6-2POLE.md-245-
SHEET6-2POLE.md-246-### 5a. The obstruction attack FAILS: minimum spend is 0, not > 4
SHEET6-2POLE.md-247-
SHEET6-2POLE.md-248-Per-pole pre-merge minimum: 0 (λ_{pole} = 0 automatically, §2a; H_i = P_i
SHEET6-2POLE.md-249-allowed, §1c(i): the chains may merge at the FIRST step). Merge minimum: 0
SHEET6-2POLE.md:250:(k = 0 merged patterns carry no northeast extras; the other chain's orbit
SHEET6-2POLE.md-251-is searrow and never λ-charged, §4a). So min(Σλ) = 0 + 0 + 0 + suffix, and
SHEET6-2POLE.md-252-the shared budget Σλ <= 4 (§2b.3) kills nothing a priori. The arithmetic
SHEET6-2POLE.md-253-reason the single-pole engine's μ=1 auto-kill (M_F = gcd(ν, (l+1)ν+1) = 1)
SHEET6-2POLE.md-254-fails here: at a merge vertex the second orbit doubles the p-degree,
SHEET6-2POLE.md-255-M(G_m) = gcd(2ν, (l+2)ν+1) = 2 for ν odd, l odd — the M=1 cascade that
SHEET6-2POLE.md-256-disposes of every μ=1 branch in the single-pole bash is broken exactly at
SHEET6-2POLE.md-257-V_{2,a} vertices. This is THE mechanism by which the two-pole configuration
SHEET6-2POLE.md-258-escapes the machine.
--
SHEET6-A3L1-REVIEW.md-40-
SHEET6-A3L1-REVIEW.md-41-- Not 8.1 (p. 39) verbatim: "Set F ∈ T_a, m = m_F, h_i = h_{i,F}
SHEET6-A3L1-REVIEW.md-42-  (i = 0,...,m) (cf Proposition 4.2). Define M_F := gcd(deg p_F,

exec
/bin/zsh -lc "rg -n -C 6 \"Prop 6\\.7|Proposition 6\\.7|6\\.7\" SIGRAY-AUDIT.md SHEET6-*.md | head -n 220" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
SHEET6-AF2.md-60-Supporting cast, all read on-page: Not 9.3 (p. 49): λ_F := Σ_{H∈Y(F)}
SHEET6-AF2.md-61-κ_H(π(H)−1), Y(F) = curve vertices over F on branches through F. St 9.4
SHEET6-AF2.md-62-(25)/(26) + St 9.5 (p. 49-50): Σ_i λ_{F_i} ≤ td−1−ψ, ≤ td−2 over the
SHEET6-AF2.md-63-characteristic sequence. St 7.1 (p. 35): H ∈ T_{a,cv} ⇒ π(H) > 1. St 7.3
SHEET6-AF2.md-64-(p. 35): a branch with a T_a↗ vertex has a T_{a,cv} vertex. Cor 7.1
SHEET6-AF2.md-65-(p. 39): global budget. St 6.1/6.2 (p. 29): ↘/↗ dichotomy on T_a⁺ and the
SHEET6-AF2.md:66:step criterion "F = G + c ∈ T_a↘ iff d_G < (1−π(G))mult(p_G,c)". Prop 6.7
SHEET6-AF2.md-67-(p. 33): F ∈ T_a↘, deg p_F > 1 ⇒ every F∗c ∈ T_a⁺. Prop 8.1(i) (p. 39-40):
SHEET6-AF2.md-68-(ξ^δ p(η))^i = f_F⁺, i = deg(p_F)/M*_F — hence mult(p_F, c*) = i·mult(p, c*)
SHEET6-AF2.md-69-for EVERY root (true multiplicities are the reduced pattern's times i).
SHEET6-AF2.md-70-St 8.4 (p. 42): mult(p,c) | M_G. St 3.18 (p. 18): every root of p_F yields
SHEET6-AF2.md-71-exactly one direction (unique ε per ν_F-orbit; F∗0 exists iff 0 is a root).
SHEET6-AF2.md-72-
--
SHEET6-AF2.md-75-Setting: one chain step G = F + c (Prop 9.3; F = G° ∈ V_a ∩ T_a↘ the new
SHEET6-AF2.md-76-node, G the ↘ continuation, c the special root, mult(p,c) = μ | M_G). The
SHEET6-AF2.md-77-reduced pattern p of Prop 8.1 has roots: the c-orbit (mult μ), possibly 0
SHEET6-AF2.md-78-(mult 1; exactly the IIb/III patterns), and k extra ν_F-orbits c_1..c_k
SHEET6-AF2.md-79-(templated simple). For any root c* of p with direction ≠ that of G:
SHEET6-AF2.md-80-
SHEET6-AF2.md:81:- (R1) F ∗ (εc*) exists (St 3.18) and H₁ := F + c* ∈ T_a⁺ (Prop 6.7;
SHEET6-AF2.md-82-  deg p_F > 1 whenever p has > 1 root, i.e. except the μ=1 M=1-kill).
SHEET6-AF2.md-83-- (R2) THE CLIMB. By St 6.2 (applied to the pair H₁ = F + c*):
SHEET6-AF2.md-84-  H₁ ∈ T_a↘ ⟺ d_F < (1−π(F))·mult(p_F, c*). Multiplying by κ_F > 0 and
SHEET6-AF2.md-85-  using D_F = κ_F d_F, κ̄_F = κ_F(1−π(F)), mult(p_F,c*) = i·w (Prop 8.1(i),
SHEET6-AF2.md-86-  w := mult(p, c*)):
SHEET6-AF2.md-87-      **H₁ ∈ T_a↘  ⟺  D_F/(i·w) < κ̄_F  ⟺  gap(c*) := D_F/(i·w) − κ̄_F < 0.**
--
SHEET6-AF2.md-157-  i = deg(p_G)/μ = j; ratio (b): 36/15 = 4(1+n)/(9+n) ⇒ n = 11 (≡ 3 ≡
SHEET6-AF2.md-158-  −κ̄_G mod ν_G ✓); child Q(F) = (12j, 36j, 7, 3, 5) — St 9.7's own
SHEET6-AF2.md-159-  hypothesis shape (R1); R2 = (2/3,3s+2,3,2s+2) is its λ=0 IIa_0 child.
SHEET6-AF2.md-160-The step's price:
SHEET6-AF2.md-161-  gap = D_F/i − κ̄_F = 12 − 5 = **7**;   gap/ν_F = 1.
SHEET6-AF2.md-162-  - Climb: by (R2), the c₁-direction is in T_a↘ iff 12 < 5 — FALSE; the
SHEET6-AF2.md:163:    0-direction identically; both climb by St 6.2 + St 6.1 + Prop 6.7,
SHEET6-AF2.md-164-    NO regularity input.
SHEET6-AF2.md-165-  - Price: corrected (24): the two curve vertices contribute ≥ 7 and ≥ 1;
SHEET6-AF2.md-166-    λ_F ≥ 8. Integer bounds — no ⌈·⌉/integrality needed.
SHEET6-AF2.md-167-  - Budget: St 9.5/(26): Σ λ_{F_i} ≤ td − 2 = 3 over ANY characteristic
SHEET6-AF2.md-168-    sequence of a td=5 counterexample. 8 > 3 (already 7 > 3 on the orbit
SHEET6-AF2.md-169-    term alone). The step is impossible; R1 is never created, R2 never
--
SHEET6-AF2.md-223-  (deg q = (k+1)ν+1 ⇒ power 1), with its solutions (21,15)/(20,16), with
SHEET6-AF2.md-224-  M_F = gcd(21,15) = 3, and with 9.7/9.8's printed patterns (power 1).
SHEET6-AF2.md-225-
SHEET6-AF2.md-226-Trust perimeter of the two kills (§4): Prop 9.3 (a)-(d) + Prop 8.1 +
SHEET6-AF2.md-227-St 3.17 arithmetic (= H1, the layer that produced the cell), the cell's own
SHEET6-AF2.md-228-(b)-template, corrected-or-printed (24) (sign-robust), St 6.1/6.2, Prop
SHEET6-AF2.md:229:6.7, St 7.3, Not 9.3, St 7.1, St 9.5/(26). NOT engaged: regularity (H4's
SHEET6-AF2.md-230-wlog), the St 9.4-integrality line, ψ/H3q, N1/H5a/H5b, AF3, Prop 8.4.
SHEET6-AF2.md-231-
SHEET6-AF2.md-232-Honesty items (no new standing hypothesis is introduced — **no H6**):
SHEET6-AF2.md-233-- The max(·,1) floors on gap ≤ 0 roots (used by the general rule, NOT by
SHEET6-AF2.md-234-  §4's kills) still ride H4-regularity, exactly as the thesis's own λ ≥ 1
SHEET6-AF2.md-235-  floors do (pp. 53-54); the ⌈·⌉ on fractional gaps still rides the
--
SHEET6-L1.md-74-  ⊖p, delta = d_F/i, u = pi(F); (v) M_F = gcd(deg p, deg q). [(iv) is
SHEET6-L1.md-75-  (11) under p_F = p^i, p_{h,F} = p^k q, k = i(mu_F - 1); exponent check
SHEET6-L1.md-76-  done exactly.]
SHEET6-L1.md-77-- Cor 6.1 (p. 32): at V_a searrow vertices != (0,y), case (16) always
SHEET6-L1.md-78-  holds: deg p_{h,F} = (d_{h,F}/d_F) deg p_F; reduced: deg q =
SHEET6-L1.md-79-  (1-u) deg p_F / d_F; equivalently the top of (iv) cancels at rho :=
SHEET6-L1.md:80:  delta/(1-u) = deg p/deg q. (Its proof also derives, via Prop 6.7 and
SHEET6-L1.md-81-  the (12)/(13)-vs-(14) dichotomy, the count deg q >= (mu-1)deg p + #roots.)
SHEET6-L1.md-82-- Prop 6.2/6.3 (pp. 29-31): (14) holds at every root whose deeper vertex
SHEET6-L1.md-83-  is searrow.
SHEET6-L1.md-84-- St 8.2 (p. 41): searrow test deg(q) mult(p,c) > deg(p).
SHEET6-L1.md-85-- St 8.4 (p. 42): mult(p,c) | M_G (G = F + c deeper). St 8.5 (p. 42):
SHEET6-L1.md-86-  M_G | M_F for G = F° not in V_{2,a} (proof line: p_{h,G} = eta r(eta^nu)).
--
SHEET6-H3.md-30-
SHEET6-H3.md-31-## 1. Ground truth: the thesis's own root-vertex argument (Prop 8.4 proof)
SHEET6-H3.md-32-
SHEET6-H3.md-33-Read on-page (pp. 44-45). Structure of the proof of Prop 8.4 (single pole,
SHEET6-H3.md-34-assume some M_F = 1):
SHEET6-H3.md-35-- Build the sequence F_0 = F, F_{i+1} = F_i° while pi(F_i) != 0; by Props
SHEET6-H3.md:36:  6.7/6.8 all F_i in T_a^searrow, so F_n = (0,y). Set H := F_{n-1}.
SHEET6-H3.md-37-- Prop 8.3 + induction: M_H = 1. St 8.1 (p. 39, verbatim): "there exist
SHEET6-H3.md-38-  N, N_0, ..., N_m ... in Z with M_F = N deg(p_F) + N_0 deg(p_{h_0,F}) +
SHEET6-H3.md-39-  ... + N_m deg(p_{h_m,F})" — i.e. M_F is the gcd of the h-family degrees
SHEET6-H3.md-40-  (definition directly above St 8.1 on p. 39). With M_H = 1: pick N, N_i
SHEET6-H3.md-41-  with 1 = N deg(p_H) + sum_i N_i deg(p_{h_i,H}).
SHEET6-H3.md-42-- Transport to the root: (k,l) := N(deg p_{(0,y)}, d_{(0,y)}) +
--
SHEET6-H3.md-185-In particular any characteristic sequence whose terminal step is case IV
SHEET6-H3.md-186-with sum lambda_{F_i} > td - 1 - psi is contradictory.
SHEET6-H3.md-187-
SHEET6-H3.md-188-Proof. By (l) (p. 51), d_F < deg(p_G), so R > 1 and psi >= 1. By the §2a
SHEET6-H3.md-189-chain (Lemma 2.1(i), St 3.12, St 3.17(i)): k_f >= deg(p_G) and l_f = d_F,
SHEET6-H3.md-190-hence k_f/l_f >= R > psi, i.e. psi l_f < k_f. The F_i are pairwise
SHEET6-H3.md:191:different elements of V_a cap T_a^searrow (Props 6.7/6.8/9.2 — same use as
SHEET6-H3.md-192-St 9.5). Statement 9.4, inequality (25), applied with THIS psi (not just
SHEET6-H3.md-193-psi = 1 as in (26)/St 9.5) gives (*). QED.
SHEET6-H3.md-194-
SHEET6-H3.md-195-Remarks.
SHEET6-H3.md-196-- (*) uses only printed thesis statements; the sole "new" content is
SHEET6-H3.md-197-  noticing that case IV's own condition (l) certifies the hypothesis
--
SHEET6-A2P-REVIEW.md-26-- Front 5 (merge legality / 8.4 entry points): **CONFIRMED** (8.4's proof
SHEET6-A2P-REVIEW.md-27-  audited line-by-line: singleton enters ONLY via the two Prop 8.3
SHEET6-A2P-REVIEW.md-28-  invocations; no statement forbids the lambda=0 merge; St 8.5 explicitly
SHEET6-A2P-REVIEW.md-29-  exempts V_{2,a})
SHEET6-A2P-REVIEW.md-30-- Front 6 (exhibit + sweep): **CONFIRMED** (full hand re-chase passes;
SHEET6-A2P-REVIEW.md-31-  52389/50097/1373/336/3/9/0 all reproduce; one cosmetic slip: "96.6%"
SHEET6-A2P-REVIEW.md:32:  is actually 95.6% of solved, 96.7% of killed)
SHEET6-A2P-REVIEW.md-33-- Front 7 (cross-consistency): **WEAKENED (bookkeeping only)** — the
SHEET6-A2P-REVIEW.md-34-  two-pole run used LEGACY IIb pricing (flag never set): under the
SHEET6-A2P-REVIEW.md-35-  AF2-derived rule the book drops 3 residues/9 IV classes -> 2 residues/
SHEET6-A2P-REVIEW.md-36-  6 IV classes (verified by re-run: A' repriced out, B loses both
SHEET6-A2P-REVIEW.md-37-  Sigma=3 classes); plus a new sharper-AF3 observation
SHEET6-A2P-REVIEW.md-38-  (M_pole = gcd(deg p, deg p_g)) that would kill residue B at entry and
--
SHEET6-A2P-REVIEW.md-78-hunt, and is now BETTER supported than the doc itself states.
SHEET6-A2P-REVIEW.md-79-
SHEET6-A2P-REVIEW.md-80-- (R1) re-verified: St 3.18 (p. 18, verbatim): "If 0 is a root of p_F,
SHEET6-A2P-REVIEW.md-81-  then F*0 exists. If c in C* is a root of p_F, then there exists a
SHEET6-A2P-REVIEW.md-82-  unique nu_F-th root of unity eps such that F*eps c exists." Prop 3.2
SHEET6-A2P-REVIEW.md-83-  (p. 18) defines F + c := G*c — direction vertices ARE V_a vertices, so
SHEET6-A2P-REVIEW.md:84:  St 6.2's standing hypothesis (F,G in V_a cap T_a^+) is met; Prop 6.7
SHEET6-A2P-REVIEW.md-85-  (p. 33) gives T_a^+ membership (deg p_F > 1 holds: 36j).
SHEET6-A2P-REVIEW.md-86-- (R2) re-verified: St 6.2 (p. 29) is an iff; multiplying by kappa_F > 0
SHEET6-A2P-REVIEW.md-87-  turns it into gap(c*) < 0, so gap > 0 forces the climb through St 6.1's
SHEET6-A2P-REVIEW.md-88-  dichotomy (Prop 6.1: d != (1-u)deg) with NO regularity. Independent
SHEET6-A2P-REVIEW.md-89-  cross-check: St 8.2 (p. 41) is a second printed form of the same test
SHEET6-A2P-REVIEW.md-90-  (its proof shows sign(d_F - (1-pi)mult) = sign(deg p - deg q * w)); on
--
SHEET6-A2P-REVIEW.md-187-
SHEET6-A2P-REVIEW.md-188-## 5. Front 5 — merge legality; Prop 8.4's proof line by line
SHEET6-A2P-REVIEW.md-189-
SHEET6-A2P-REVIEW.md-190-Verdict: **CONFIRMED** on both halves.
SHEET6-A2P-REVIEW.md-191-
SHEET6-A2P-REVIEW.md-192-- Prop 8.4 proof (pp. 44-45), full inference inventory: (1) sequence
SHEET6-A2P-REVIEW.md:193:  F_0..F_n descends and lands at (0,y) — Props 6.7/6.8, unconditional;
SHEET6-A2P-REVIEW.md-194-  (2) "From Proposition 8.3, and by induction we have M_H = 1" — the ONLY
SHEET6-A2P-REVIEW.md-195-  consumer of the singleton hypothesis, via 8.3's regularity hypothesis;
SHEET6-A2P-REVIEW.md-196-  (3) Bezout representation of M_H = 1 — St 8.1, unconditional; (4) the
SHEET6-A2P-REVIEW.md-197-  (k,l) transport — Cor 6.1 + Prop 6.3, unconditional; (5) k = 1 uses
SHEET6-A2P-REVIEW.md-198-  deg = mult at (0,y), i.e. 8.3(iii)'s one-root p_{(0,y)} — the SAME
SHEET6-A2P-REVIEW.md-199-  entry point (last induction step); (6) l in N contradicts Thm 6.1.
--
SHEET6-A2P-REVIEW.md-259-  slack 1 — robust to lambda_root >= 1, as claimed.
SHEET6-A2P-REVIEW.md-260-- Sweep reproduction (this review's run): phase 1: 163 shapes, 5 OPEN
SHEET6-A2P-REVIEW.md-261-  III-kinds; phase 2: 52389 solved, kills 50097 (restored-8.4) + 1373
SHEET6-A2P-REVIEW.md-262-  (suffix DEAD) + 336 (N1), residue = 3 classes (A, A', B) with 9
SHEET6-A2P-REVIEW.md-263-  deduped IV classes (engine prints 10 rows; (2/3,3s+2,3,2s+2)@3 is
SHEET6-A2P-REVIEW.md-264-  shared by A' and B — dedup 9, matching §6b); phase 3: 0 root merges.
SHEET6-A2P-REVIEW.md:265:  COSMETIC SLIP: 50097/52389 = 95.6% (or 96.7% of the 51806 kills) —
SHEET6-A2P-REVIEW.md-266-  the doc's "96.6%" matches neither; absolute counts all exact.
SHEET6-A2P-REVIEW.md-267-- Hand spot-checks: survivors — residue A (fully, above) and residue B's
SHEET6-A2P-REVIEW.md-268-  merge (mu = (2,2): 2(1+5)/(5+5) = 6/5 = 30/25, M_m = gcd(30,25) = 5,
SHEET6-A2P-REVIEW.md-269-  kap = 5, gap = 6-5 = 1, lambda_m = 1; its self-IV data (j) 5<6, (k)
SHEET6-A2P-REVIEW.md-270-  36/6 = 6, R = 5, (m) 1, psi = 4, 1 <= 1 boundary). Kills — (i) the
SHEET6-A2P-REVIEW.md-271-  mu=(1,1) l=0 family: n = 8nu-1 (parity ok) solves for every nu and
--
SHEET6-HIII-REVIEW.md-35-  d_{(0,y)} = l_f. Hence k_f/l_f >= R := deg(p_G)/d_F > 1 by (l).
SHEET6-HIII-REVIEW.md-36-- psi := ceil(R)-1 satisfies psi >= 1 and psi < R, so psi*l_f < R*d_F =
SHEET6-HIII-REVIEW.md-37-  deg(p_G) <= k_f STRICTLY — exactly St 9.4's hypothesis "psi in N,
SHEET6-HIII-REVIEW.md-38-  psi l_f < k_f" (p. 49, verbatim, with proof; (25) is genuinely a
SHEET6-HIII-REVIEW.md-39-  one-parameter family, (26) = psi=1 specialization). Applying (25) to
SHEET6-HIII-REVIEW.md-40-  F_0..F_n: pairwise-different membership in V_a cap T_a^searrow is printed
SHEET6-HIII-REVIEW.md:41:  in Prop 8.4's proof (Props 6.7/6.8, p. 45); (0,y) in V_a (Def 3.4) and in
SHEET6-HIII-REVIEW.md-42-  T_a^searrow (Thm 6.1); St 9.5's printed proof applies 9.4 to the whole
SHEET6-HIII-REVIEW.md-43-  sequence. No gap found.
SHEET6-HIII-REVIEW.md-44-- Suspected flaw #1 (chart orientation): checked — transported Thm 6.1 reads
SHEET6-HIII-REVIEW.md-45-  d_{(0,y)} < deg(p_{(0,y)}), SAME direction as (l); the repaired argument
SHEET6-HIII-REVIEW.md-46-  uses no sign clash, only the magnitude transport, which this review
SHEET6-HIII-REVIEW.md-47-  re-derived from p. 28 + p. 32 independently of the H3 doc's §2a chain.
--
SHEET6-MULTIPOLE.md-67-**OBSTRUCTION O (honest half; sharp).** The verbatim multi-pole analogue of Prop 8.4 is FALSE at printed tier: at td = 6, m = 2, both poles are row 1 of table (23) (p. 46) with M_P = gcd(2,3) = 1 *forced*, all pre-merge vertices have M = 1 *forced* (MP5), and the resonant jump (r,ν,l) = (2,3,1) with M = 2 solves the printed identity Prop 8.1(iv) *exactly* with rigid coefficients (a₁/a₂ = 2±√3; cases/l1_ode_check.py; SHEET6-L1 §5, SHEET6-2POLE §6a, machine-verified), at Σλ(pre-merge ∪ merge) = 0, passing every located printed constraint. The L1 §3 blind spot is r-uniform: the l extra q-orbits sit at non-roots of p, carry no tree vertex, no puncture, no cv vertex, no λ, no pole — nothing printed sees them except deg q. At pattern level the escape is m-uniform: for every m, choosing lν ≡ −1 (mod m), ν odd, gives M_{G\*} = m at spend 0 (arithmetic existence only; r-edge H1 ratio-consistency unverified for m ≥ 3). Hence the MP7 residual is irreducible from the printed statement list, and MP0–MP9 is the exact printed-tier frontier.
SHEET6-MULTIPOLE.md-68-
SHEET6-MULTIPOLE.md-69----
SHEET6-MULTIPOLE.md-70-
SHEET6-MULTIPOLE.md-71-## 3. Derivation
SHEET6-MULTIPOLE.md-72-
SHEET6-MULTIPOLE.md:73:All page numbers: refs/sigray_full.pdf, printed page = pdf page. The printed inventory used is listed once: St 2.1/Not 2.4 (pp. 8–9); Not 3.3 (p. 12); St 3.9 (p. 15); St 3.16 (p. 17); Prop 3.2/St 3.17/3.18 (p. 18); Prop 4.2 (p. 19); Prop 5.1/Not 5.1–5.2 (pp. 23–25); Prop 5.3 (p. 25); St 5.2 (p. 26); Props 5.5–5.8 (pp. 26–28); Thm 6.1 (p. 28); Not 6.1/St 6.1–6.2 (p. 29); Props 6.7/6.8 (pp. 33–34); Not 7.1/St 7.1–7.3 (p. 35); Prop 7.2 (p. 36); Prop 7.5 (22) (p. 38); Cor 7.1, Not 8.1, St 8.1, Prop 8.1 (pp. 39–41); St 8.2–8.5 (pp. 41–43); Cor 8.1, Props 8.2–8.4 (pp. 43–45); table (23) (p. 46); Not 9.1–9.2, St 9.1–9.4 (pp. 48–49); Prop 9.2 (p. 50).
SHEET6-MULTIPOLE.md-74-
SHEET6-MULTIPOLE.md-75-### D1 (MP0)
SHEET6-MULTIPOLE.md:76:(⊇) Each C_i ⊆ Ta& ∩ Va: the printed Prop 8.4 proof line (p. 45) "From Propositions 6.7 and 6.8, we obtain F_0,…,F_n ∈ Ta&" applies from F_0 = P_i — nothing in the construction uses |T_{a,pole}| = 1 (2POLE §1b); poles are in Ta& (d > 0 and deg p ≥ 2 by Prop 5.3(iv)–(v) + St 3.16), and Va-membership descends via Not 3.3(i).
SHEET6-MULTIPOLE.md-77-(⊆) Any H ∈ Ta& ∩ Va \ {(0,x),(0,y)} has deg p_H ≥ 2 (St 3.16: p has more than one root). Prop 6.8 (p. 34, verbatim: "there exist P, u, v: F = I_P(u), v ≥ u, I_P(v) ∈ T_{a,pole}" — the pole lies above H on the SAME branch) gives I_P(v) = P_s. Not 3.3's ° enumerates every Va-vertex of I_P([0,v)) in decreasing order, branch-independently; H is one of them, so H ∈ C_s.
SHEET6-MULTIPOLE.md-78-Leaves: a chain predecessor H of P_j would give deg p_H = mult(p_{P_j}, c) ≥ 2 (St 3.17(i) + St 3.16), contradicting squarefreeness of p_{P_j} (Prop 5.3(v)). So poles have in-degree 0; every non-pole U-vertex is some F°; leaves(U) = {P_1,…,P_m}. ∎
SHEET6-MULTIPOLE.md-79-
SHEET6-MULTIPOLE.md-80-### D2 (MP1)
SHEET6-MULTIPOLE.md-81-U is a finite tree: every vertex except (0,y) has the unique out-edge F → F° (Not 3.3 deterministic). Counting edges: Σ_G (r(G) − 1) = −1 over all of U with r = 0 exactly at the m leaves, so Σ_{r ≥ 2}(r − 1) = m − 1. By D1 the Not 9.2-predecessor set of G equals its U-predecessor set, so regularity ⇔ r(G) = 1. No merge strictly below G\*: below the meet all chains coincide (° deterministic; Not 3.3 betweenness excludes side entries from ≥ G\*); r(G\*) ≥ 2 by maximality of G\*. Unique-predecessor at suffix vertices (A2's complement): a second predecessor H′ of a suffix vertex S would, by St 3.16 + Prop 6.8, lie under some pole P_j; C_j visits H′ and continues to S (Prop 3.2 determinism), yet C_j also passes through G\* and reaches S through the trunk — a characteristic sequence is a simple descending path and cannot contain two predecessors of one vertex. Contradiction. ∎
SHEET6-MULTIPOLE.md-82-
--
SHEET6-R6-REVIEW.md-12-Verdicts:
SHEET6-R6-REVIEW.md-13-- Front 1 (L2 exactness of vertex transport): **CONFIRMED, citation
SHEET6-R6-REVIEW.md-14-  corrected** — the equality IS printed (St 3.17(i) p. 18; verbatim
SHEET6-R6-REVIEW.md-15-  "mult(p_G,c) = deg(p_F)" in St 8.3's proof p. 41); and the six-case
SHEET6-R6-REVIEW.md-16-  kill does not even need it (second, vertex-local route).
SHEET6-R6-REVIEW.md-17-- Front 2 (L4 dead-member mult law): **CONFIRMED on-page, twice**
SHEET6-R6-REVIEW.md:18:  (Prop 8.1 proof p. 40 via Prop 6.3; Cor 6.1 proof p. 32 via Prop 6.7);
SHEET6-R6-REVIEW.md-19-  both level-0 cross-checks exact.
SHEET6-R6-REVIEW.md-20-- Front 3 (μ₂ = 3/2 + (k1−1)r): **CONFIRMED** (Prop 4.2(iv)+(9) p. 19,
SHEET6-R6-REVIEW.md-21-  α_0 = 0; all 8 values recomputed).
SHEET6-R6-REVIEW.md-22-- Front 4 ((2,3)/(2,5) h2 pole-edge kill): **REFUTED** — d_h1@P = 1/7,
SHEET6-R6-REVIEW.md-23-  not 1/21; the h1-side (not the f-side) wins h2's top at P on the
SHEET6-R6-REVIEW.md-24-  ENTIRE window; deg p_h2@P = 2k1, and (D) then PASSES (4 ≤ 5, 4 ≤ 7).
--
SHEET6-R6-REVIEW.md-77-- Prop 8.1's proof, p. 40: "from Proposition 6.3, we obtain that for
SHEET6-R6-REVIEW.md-78-  any root of p_F c, one has mult(p_{h_F},c) − (μ−1)mult(p_F) = 1" —
SHEET6-R6-REVIEW.md-79-  i.e. mult(p_{h_m,F},c) = (μ_F−1)mult(p_F,c) + 1 for ANY root c of
SHEET6-R6-REVIEW.md-80-  p_F. Also on p. 40: the dead-member level formula d_{h,F} =
SHEET6-R6-REVIEW.md-81-  (μ_F−1)d_F + 1 − u (first substitution of the "constant l" line) —
SHEET6-R6-REVIEW.md-82-  used below in front 4/5 arithmetic.
SHEET6-R6-REVIEW.md:83:- Cor 6.1's proof, p. 32 (via Prop 6.7): "for any root of p, say c one
SHEET6-R6-REVIEW.md-84-  has mult(q,c) = (μ−1)mult(p)+1" (q := p_{h,F}), driving the printed
SHEET6-R6-REVIEW.md-85-  "k = 1, so F ∉ V_a" root-count contradiction — the same mechanism the
SHEET6-R6-REVIEW.md-86-  R6 kills re-use.
SHEET6-R6-REVIEW.md-87-- Cross-checks recomputed: G_m level-0: (3/2−1)·2+1 = 2 = mult(pq,c_i)
SHEET6-R6-REVIEW.md-88-  (1+1, E5) ✓; F_s: (25/6−1)·12+1 = 39 = 19·2+1 (E4/E7 banked pattern
SHEET6-R6-REVIEW.md-89-  p^19·q with mult(q,c_m) = 1) ✓. Engine assert line correct. The
--
SHEET6-R1.md-542-Phi42 roots mod p (p == 1 mod 42; roots via x^((p-1)/42) sampling, no
SHEET6-R1.md-543-scans) — ring coefficients become {tail7: 24-int vectors} with
SHEET6-R1.md-544-POINTWISE z-multiplication (no convolution, no ZRED); converted back
SHEET6-R1.md-545-to the za-basis by inverse Vandermonde at fold end, so cWG.<p>.pkl
SHEET6-R1.md-546-format and the CRT+holdout+scalar verification stack are unchanged.
SHEET6-R1.md-547-Entry counts agree with the pair representation at every checkpoint
SHEET6-R1.md:548:(19263 @ 11/21, 106592 @ 16/21 and 21/21). f^3 fold: 606.7 s/prime

exec
/bin/zsh -lc "sed -n '1,155p' SHEET6-MP-REVIEW.md && sed -n '217,330p' SHEET6-MP-REVIEW.md" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
# SHEET6-MP-REVIEW.md — Adversarial review of SHEET6-MULTIPOLE.md (0827409), the Theorem MP synthesis

Reviewer: Claude (adversarial synthesis-grafting pass, 2026-08-12). Status:
COMPLETE. Scope: the SYNTHESIS layer only — the per-angle A1/A2 contents were
adversarially voted inside the workflow (3/3 each) and their records are NOT
in the repo; this review therefore audits (a) the doc's own provenance map
(§3 D-derivations + §9 grafting record) clause by clause, (b) whether the
grafted clauses COMPOSE, by full re-derivation at the concrete instance
(m, td) = (2, 6) against the promoted SHEET6-2POLE/SHEET6-L1 record, (c) the
six load-bearing page citations on-page, (d) the obstruction witness, (e) the
reduction/finiteness rider. Ground truth: refs/sigray_full.pdf re-read
on-page this session (pp. 26–28, 34, 38–52). Engines re-run:
cases/twopole_check.py phases 1–4 (all counts byte-match SHEET6-L1 §6:
133 / 47970 / 552 / 0 root; phase 4: 26 / 18427 / 17199 / 601 / 276 / 351,
unique residue child (ρ,ν,M,κ̄) = (1/2,3,2,5)), cases/l1_ode_check.py
(families A/B/B-η/Z/C reproduced exactly). PLUS an independent exact checker
written for this review (/tmp/mp_check.py; no shared code): MP6(d) menu,
MP7 kill, MP9 parity + log-residues, MP7 root pin, and a raised-caps
κ̄-vs-ν sweep over the M=1 chain tree. ALL CHECKS PASS.

Verdicts:
- Front 1 (clause provenance + quarantine): **CONFIRMED, two flags** (no
  §7 leak found; every MP clause has an in-doc derivation D1–D9 standing on
  printed statements + sanctioned P1/P2, so provenance risk is contained
  even where the panel record is truncated; flags in §1)
- Front 2 (composition at m = 2, td = 6): **CONFIRMED with one citation
  correction** (MP4→MP5→MP6→MP7 reproduces the promoted record exactly —
  entry row 1, μ=(1,1), the 3-shape menu clause-for-clause, merged child
  (6,12,3,2,5) unique; the MP9 root-meet td=6 citation names the wrong
  ground — kill re-established independently here, §2c)
- Front 3 (page fidelity, 6 citations): **CONFIRMED, 6/6 verbatim** (§3)
- Front 4 (obstruction half): **CONFIRMED** (witness located, re-verified,
  b_i = 1 doubly forced, and it IS the promoted residue-A object) (§4)
- Front 5 (reduction claim): **DEMOTED** — the "finite book per (m, td)"
  rider (§0, §5 of the doc) is proven only per parent frame; global
  finiteness needs an unproven chain-closure lemma, and the doc's own MP8
  shows no printed budget can supply it (§5; parameterization spec §5c)
- Front 6 (mechanization): **DONE, ALL PASS** (/tmp/mp_check.py, §6)

Net: **MP0–MP8 stand as printed. MP9 stands with its root-meet ground
corrected. Theorem O stands. The finite-book rider is the one demotion.**

## 1. Front 1 — clause provenance and quarantine integrity

Provenance map assembled from §3/§9 of the doc and checked against the
promoted sheets:

| clause | source per §9 | independent in-doc derivation | promoted-record anchor |
|---|---|---|---|
| MP0 | A1/A2 (cross) | D1: Prop 6.8 + St 3.16/3.17(i) + Prop 5.3(v) | 2POLE §1b/§1c |
| MP1 | A2 (unique-predecessor adopted) | D2: edge count Σ(r−1) = −1 + m leaves (verified: gives m−1) | 2POLE §1c(ii) at m=2 |
| MP2/MP3 | A1.T2 = A2(4); A1.T3 correction | D3: P1 + 8.3(iii) single-root + p.45 Bezout | 2POLE §1c(iii) |
| MP4 | A2(1) ⊇ A1's β-minimal | D4: (19) + St 5.2 + St 2.1 arithmetic (re-done here, §3b) | L1a(a)/A3L1 fronts 1–2 |
| MP5 | A1/A2 (k=0 manufacture in both, §9) | D5: St 8.4/8.2 + Prop 6.8 same-branch | L1a(b) |
| MP6 | A1.T4/T5 = A2(3) = A3.P4 | D6: St 3.17(i)/8.1(i)/(v) + gcd arithmetic | L1a(c) 3-shape menu |
| MP7 | A1/A2 | D7: gcd + (iv) degeneration + St 9.2(ii) | L1 §0/§4 |
| MP8 | A1.T7 = A2.Prop B | D8: (22) itemization + F*_P argument | LROOT §1–2 |
| MP9 | A1/A2 + D9's new residue closed form | D9 | L1 §4–§6, 2POLE §4b/§5b |

- **Quarantine honored.** The three §7 blocks (prime-partition kill,
  RH-lemma kills, OB extension (3,5,1)/(4,7,1)) were grepped against
  MP0–MP9, §0, §5, §6, §8. No leak. The two near-misses are clean:
  (i) MP4's prime-Λ clause overlaps A3's quarantined P2 *statement*, but §9
  attributes it to A2(1) and D4 derives it in full from (19)+St 5.2(ii)
  (re-verified on-page, §3b below) — the A3-unique *partition* consequences
  (8=3+5 etc.) stay in §7. (ii) Theorem O's m-uniform escape claims
  "arithmetic existence only" (lν ≡ −1 mod m ⇒ gcd(m, lν+1) = m — trivially
  checkable) and expressly does NOT claim (iv)-solvability for m ≥ 3; A3's
  quarantined OB (which claims solvability at (3,5,1)/(4,7,1)) is cited
  only as §8 future work. Correctly firewalled.
- **Flag 1.** §4's record caveat (i) admits A2's third vote flagged one
  *unnamed* subsidiary sub-claim as failing plus one unflagged
  record-contradiction. Because the failing sub-claim is not identified, a
  reviewer cannot verify it stayed out of the graft. Containment: every MP
  clause carries a D-derivation from printed statements, and this review
  re-verified the load-bearing ones — so nothing in MP *depends* on
  unexamined A2 record content. Still, the synthesis should name the failed
  sub-claim. (Action item A1 below.)
- **Flag 2.** The A1/A2/A3 panel records are not preserved in the repo;
  provenance is auditable only through the doc itself. Acceptable given the
  D-derivations, but the record should be archived if it still exists.
- Grafting upgrades audited: A1's "M_G | gcd(r, lν+1)" → equality (D6d) —
  proved both directions here and machine-swept (§6): exact. A1.T6's
  ψ = r+l−1 vs A2(5R)'s ψ = l+1 at r = 2: identical. A1's G\* = A2's
  G_last: same object (max ∩C_i).

## 2. Front 2 — the composition re-derived at m = 2, td = 6

### 2a. Clause-by-clause against the promoted record

- **MP4 entry.** td = 6 = mβ; Λ = 3+3, Prop 9.1's 1 < α < β ≤ 6 pins
  (α,β) = (2,3); Λ_i = 3 = β is both β-minimal AND prime — b_i = 1 forced
  by either MP4 route. (deg p, deg p_g) = 1·(2,3), M = gcd(2,3) = 1 = row 1
  of (23) (re-read on-page: unique Λ=3 row, ν=2). Matches L1a(a)/2POLE §2d
  exactly. MP4's b-formula reproduces all 11 rows of (23) (b = 1 except
  rows 4, 8, 9: gcd(4,6)=2, gcd(6,15)=3, gcd(6,10)=2 — same gcds as
  A3L1-REVIEW front 2).
- **MP5 propagation.** Single simple ν-orbit, dp = ν, dq = nν+1, λ = 0,
  μ_i = 1 at arrival = L1a(b) verbatim; engine phase 4: 26 pre-merge
  shapes, all M=1/λ=0. Match.
- **MP6 menu at r = 2.** IIa: (2ν,(l+2)ν+1), M = gcd(2, lν+1); ZCH:
  (ν+1,(l+1)ν+1), M = gcd(ν+1, l); I: (2, 2+l), M = gcd(2, l). All three
  reduce EXACTLY to L1a(c)'s menu (checked by hand: (l+1)ν+1 ≡ −l mod ν+1;
  gcd(2,2+l) = gcd(2,l)) and machine-swept (§6). Match, including the
  equal-quotient i = 2 (exhibit's i₀ = P_i/μ_i = 2, realized absolutely).
- **MP7 + MP9 interior meet.** M = gcd(2, lν+1) = 2 iff l, ν both odd
  (parity swept §6); l = 0 → M = 1 → MP2 kill; ν = 1 killed by D9's
  log-obstruction (even l) + MP2 (odd l). Survivor menu IIa(l odd, ν ≥ 3
  odd)/ZCH(gcd(ν+1,l) ≥ 2) = L1 §0's post-L1b state; reach then pins the
  unique in-caps cell (r,ν,l) = (2,3,1), n = (5,5), dp/dq = 6/10 → merged
  child Q = **(6,12,3,2,5) @ Σλ = 0** — engine re-run this session:
  351 parent pairs, every depth, single residue child (1/2,3,2,5),
  byte-matching L1 §6 and 2POLE §6a. deg p_full = i·dp = 2·6 = 12,
  M = gcd(6,10) = 2, κ̄ = (5+5)/2 = 5. **The MP machinery reproduces the
  promoted record exactly; no mismatch found.**
- **MP8.** Σλ = 0 through pre-merge + merge = 2POLE §5a's min-spend-0;
  witness total Σλ = 2 ≤ 6−1−2 = 3 (St 9.4 (25) at ψ = 2, on-page). Match.
- **D9's log-obstruction upgrade** (all even l at ν = 1, beyond L1's engine
  caps): the residue identity C(−n, n−1) = (−1)^{n−1}C(2n−2, n−1) ≠ 0 and
  the partial-fraction residue of p^{−n} were re-verified exactly for
  n = 2..12 (§6), against L1's l=2 value ∓2/(a₁−a₂)³. The claim is sound:
  LHS (s·p^{−l/2})′ is a derivative, residue-free; RHS has nonzero simple
  residues; c′ = 0 forced, contra ⊖ ≠ 0. The η-variant cap flag (l ≤ 4)
  correctly survives as the doc states.

### 2b. MP1/MP3 at m = 2

Σ(r−1) = 1: exactly one merge, r = 2, G\* = G_m; escape set = the two
pre-merge segments = 2POLE §1c(iii). Consistent.

### 2c. The one composition flaw: MP9's root-meet citation

MP9 (root meet) claims "Empty at td = 6 by reach (2POLE §5b phase 3)". Two
problems with that citation: (i) phase 3's printed grounds fail for the
very family MP9 leaves open — ground (i)'s searrow failure and the ratio
rigidity (2+k)/(k+2) = 1 both presuppose the *l-free* I-like root pattern
(dq = k+2); with l ≥ 1 extras dq = 2+l, the searrow test passes and the
ratio is 2/(2+l) ≠ 1 — indeed MP9 itself proves l = 1 *locally solvable*;
(ii) the engine's phase-3 MENU is l-free (`dp, dq = mu1+mu2+k, k+2`,
twopole_check.py:253), so it never enumerated the l ≥ 1 root family at all.
**The kill is nevertheless real and was re-established here on an
l-INDEPENDENT ground:** the terminal edge into (0,y) is Prop 9.3 case (I)
(root merge ⇒ (0,y) ∈ V_{2,a}, case (IV) hypothesis fails — 2POLE
§1c(ii)), and (d) with child κ̄ = 1 (St 9.2(iii), on-page) forces
n_e = ν_e − κ̄_e ≥ 1, i.e. **κ̄ < ν at both parents, whatever the pattern
shape**. Independent raised-caps sweep (/tmp/mp_check.py check 5: ν ≤ 48,
l ≤ 8, depth ≤ 8 vs the engine's 24/4/6): 50 reachable M=1/λ=0 chain
shapes from the row-1 entry, **zero with κ̄ < ν**. So td = 6 root meets
with μ = (1,1) are reach-dead. Required fix: MP9's citation should read
"κ̄ < ν unreachability along M=1/λ=0 chains (Prop 9.3(d) at child κ̄ = 1;
engine sweep)", and the phase-3 root menu should gain the l-family before
any reuse at general td (where the doc correctly marks the residual OPEN).
Same tier as before (H1 + capped sweep) — no tier change, no new survivor.

## 3. Front 3 — page fidelity (all six re-read on-page this session)
## 5. Front 5 — the reduction claim (the review's main deliverable)

### 5a. What is actually proven

Finitely many at printed tier, per (m, td): types and entries (D4:
partitions td = ΣΛ_i, Λ_i ≥ β; finitely many (a_i,b_i,ν_i) per Λ_i via
(19) + St 5.2(ii)); tree shapes (MP1: ≤ m−1 merges, Σ(r−1) = m−1, r ≤ m);
merge-local anatomy (MP6: μ⃗ = 1 at all-M=1 merges, k = 0, family ∈
{IIa, ZCH, I}, M from the gcd menu, M | r ≤ m outside ZCH, gcd(M,ν) = 1);
root cells (ν = 1, l ≤ td−2 via ψ = r+l−1 and (25) — finite per td). At H1
tier, the per-edge Prop 9.3 equations make (l, n_e, ν) **finite per parent
frame**: for the all-μ=1 IIa jump, cross-multiplying (b) gives
ν·(rκ̄_e − (r+l)ρ_e − l·n_e) = ρ_e + n_e, so n_e ≤ (rκ̄_e − (r+l)ρ_e −1)/l,
l ≤ (r(κ̄_e − ρ_e) − 1)/(ρ_e + 1), and each admissible (l, n_e) DETERMINES
ν. This is real and enumeration-ready.

### 5b. What is NOT proven: the demotion

The frames themselves are generated from the finitely many entries by the
H1 chain-step map, and **nothing bounds the generation depth**: κ̄ evolves
by κ̄′ = (κ̄+n)/ν (Prop 9.3(d)) and demonstrably GROWS along admissible
M=1/λ=0 chains (the engine's own parent list at td = 6 contains κ̄ = 5, 6,
8, 10; my raised-caps sweep reached 50 frames and was cap-, not
constraint-, terminated). At pattern level the survivor menu is already
infinite (IIa: all l odd, ν ≥ 3 odd). Worse, the doc's own **MP8 proves
no printed budget can charge the M=1 region — so no printed statement can
bound pre-merge chain depth either**: the obstruction half structurally
undermines the reduction half's finiteness. Empirically the merged-child
datum was depth-invariant at td = 6 (351/351 pairs, one child), which
suggests a *child-invariance/closure lemma* exists — but none is stated or
proved in MP0–MP9, §5, or the quarantined §7. **Demotion: §0's "reduces
… to a finite book of jump-vertex cells" and Theorem O's "the finite book"
are theorem-grade only in the per-frame sense; globally the book is
finitely *generated* (finite alphabet, finite branching per frame) with
unbounded frame depth, conditional on an unproven closure lemma or a
cap-stability protocol.** notes.md's "finite-book at every level"
(2026-08-12 entry) inherits this demotion.

### 5c. The jump-book parameterization, as handed to the enumeration engine

    BOOK(m, td), m ≥ 2, 3m ≤ mβ ≤ td:
    E. Entry layer (printed; finite): type (α,β), 2 ≤ α < β, gcd = 1,
       mβ ≤ td; partition td = Σ_{i=1..m} Λ_i, Λ_i ≥ β (Props 5.7/5.8);
       per pole (a_i, b_i, ν_i): Λ_i = a_i b_i αβ/ν_i, ν_i | α or ν_i | β
       (St 5.2(ii) + (19)); entry datum Q(P_i) = (D = a_iα, deg p = b_iα,
       ν_i, M = b_i, κ̄ = a_i(α+β)), λ = 0. b_i = 1 forced if Λ_i = β or
       Λ_i prime (MP4).
    T. Tree layer (printed; finite): rooted trees, m leaves, merge
       vertices G with r(G) ≥ 2, Σ(r−1) = m−1, no merge below G*.
    C. Chain layer (H1; the unbounded direction): per edge, step frames
       (ρ, ν, κ̄, M) evolve by Prop 9.3(a)–(d) with n ≥ 1,
       n ≡ −κ̄ (mod ν); M = 1 segments are forced single-simple-orbit,
       λ = 0 (MP5); depth cap OR closure lemma REQUIRED here.
    J. Jump cells (printed anatomy + H1 reach; finite per frame):
       family ∈ {IIa: (dp,dq) = (rν,(r+l)ν+1), M = gcd(r, lν+1);
       ZCH: ((r−1)ν+1,(r−1+l)ν+1), M = gcd((r−1)ν+1, l);
       I: (r, r+l), M = gcd(r,l)}; constraints: μ_e | M_{H_e} (= 1 on
       all-M=1 ancestry), k = 0, common i ≥ 2 with deg p_{H_e} = iμ_e,
       l ≥ 1, M ≥ 2, gcd(M,ν) = 1, M | r ≤ m outside ZCH; per-edge reach:
       dp/dq = μ_e(ρ_e+n_e)/(κ̄_e+n_e), n_e ≥ 1, n_e ≡ −κ̄_e (mod ν_e),
       common child (κ̄, D, i) — bounds n_e, l and determines ν per frame
       (§5a). Coefficient layer: Prop 8.1(iv) rigid solve (à la
       l1_ode_check families A/Z), then the §8-item-3 coefficient-vs-ratio
       match (never yet run).
    R. Root cells (printed + H1; finite per td): ν = 1, all-μ=1, l odd,
       l ≤ td−2, k_f = (r+l)l_f, ψ = r+l−1, both parents κ̄ < ν (Prop
       9.3(d) at child κ̄ = 1 — l-independent, §2c), Prop 9.3 case (I).
    S. Suffix (printed): restored M ≠ 1 kill (MP2) + single-pole engine +
       St 9.4: Σλ ≤ td − 1 − ψ over the union, shared suffix once.

## 6. Front 6 — mechanization (/tmp/mp_check.py, exact, no shared code)

(1) MP6(d) identities on r ≤ 9, ν ≤ 12, l ≤ 12 + mixed μ-sums to 3r:
IIa/ZCH/I gcd equalities, gcd(M,ν) = 1, M | r, M | Σμ — all exact both
directions. (2) MP7: gcd(rν, rν+1) = 1 at l = 0, all cells; ZCH/I l = 0
degree degeneration. (3) MP9 parity: gcd(2, lν+1) = 2 ⇔ l, ν odd — swept.
(4) Root pin: k_f = (r+l)l_f and ψ = r+l−1 on a grid i ≤ 19, r ≤ 7,
l ≤ 11. (5) Log-obstruction: C(−n,n−1) closed form + exact Laurent residue
of p^{−n}, n = 2..12. (6) The κ̄ < ν sweep of §2c. ALL PASS. (§7's action
item — rebuilding A3's /tmp/mpm_check.py under cases/ — remains open and is
NOT covered by this file.)

## 7. Required fixes (none demote MP0–MP8)

1. **MP9 root-meet citation** → replace "(2POLE §5b phase 3)" by the κ̄ < ν
   ground of §2c; add the l-family to the phase-3 root menu before any
   general-td reuse (latent enumeration gap, currently masked by the κ̄ < ν
   filter at td = 6).
2. **§0/§5 finiteness rider** → reword per §5b: "finitely generated book;
   finite per parent frame; global finiteness conditional on chain-depth
   closure (empirically depth-invariant at td = 6)". Add the closure lemma
   to §8's next steps — it is arguably the cheapest high-value target: the
   351-pair child-invariance suggests it is provable at H1 tier.
3. **Name A2's failed subsidiary sub-claim** in §4 caveat (i), or archive
   the panel record; quarantine §7 already handles A3 correctly.
4. Cosmetic: doc §1 cites Not 8.1 at "p. 39" correctly, but 2POLE §2c says
   "p. 38" — fix in 2POLE, not here.

## 8. Reproduction

    cd cases && python3 twopole_check.py   # phases 1-4; byte-matches L1 §6
    python3 l1_ode_check.py                # witness families; ~5 s
    python3 /tmp/mp_check.py               # this review's checker; ~2 s
    # PDF: pp. 26-28, 34, 38-52 re-read on-page for §3.

codex
## 1. STRESS TEST

1. **The “fully adjudicated book” is not exhaustive.** [BOOK-ENUM.md](/Users/dc/code/math/jc72108/BOOK-ENUM.md:35) explicitly leaves every entry multiset containing \(b_i\ge2\)—hence \(M_{\rm entry}\ge2\)—uncalculated; mixed \(\mu\ge2\) merges are also quarantined. Yet [BOOK-BASH-R2.md](/Users/dc/code/math/jc72108/BOOK-BASH-R2.md:222) declares \(td=7,11,13\) fully excluded. Those prime panels are entirely “off-axis,” not empty. A counterexample there never enters the 421-cell enumeration. The \(td=6\) all-\(M=1\) book is unaffected, but the advertised \(td\le14\) completeness is false.

2. **The mass identity \(td=\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)\) is unproved at the strength consumed.** [SIGRAY-AUDIT.md](/Users/dc/code/math/jc72108/SIGRAY-AUDIT.md:74) reconstructs Proposition 5.8 only for generic \(a\), not “every \(a\).” This identity supplies every entry partition, \(m\le td/3\), the \(3+3\) reduction at \(td=6\), the prime theorem, and the book’s layer E. A generic-fiber reformulation may repair it, but that argument is presently missing.

3. **“The full JC2 program is finite at every level” confuses pointwise finiteness with termination.** Finiteness for each fixed \((m,td)\) gives infinitely many books; only \(td\le14\) was enumerated and the degree farm stops at 150. Moreover, killing residue-A would still leave four single-pole \(td=6\) classes, while the composite single-pole residual grows to 212 classes at \(td=16\). There is no uniform \(td\)-bound, induction, or stabilization theorem. Thus “one template away from JC2” is not justified.

Theorem A is not a weak point: its leading-degree/kernel-subtraction proof is sound. Its reach is simply depth-2 strip geometry, not general JC2.

## 2. NEW AVENUES

Ranked by expected decisiveness per effort; none appears in `RECON.md` or `notes.md`.

1. **Relative pole-divisor proof of Proposition 5.8.**  
   On a resolution \(X\) of \((f,g)\), prove for a generic fiber \(C_a\)
   \[
   td=\deg(g|_{C_a})=C_a\cdot(g)_\infty=\sum\Lambda(F).
   \]
   First lemma: the horizontal pole divisor of \(g\) is finite flat over an open subset of the \(f\)-line, with local intersection multiplicity exactly \(\Lambda(F)\). Then determine whether specialization proves the every-fiber version or whether the campaign must work generically.

2. **Resolved-pencil Noether/Cremona test of residue-A.**  
   For the degree-168 pencil, form
   \[
   D=168H-\sum m_iE_i.
   \]
   First computation: extract the pinned multiplicity cluster and test \(D^2=0\), \(D\!\cdot K_X=2g-2\), and all proximity inequalities; enumerate the narrowly constrained B/x tails, then apply unloading/Hudson reduction. This tests actual plane-curve effectivity, not merely splice or genus consistency.

3. **Teissier–Plücker polar budget.**  
   Compute the local polar numbers \(\mu_p+m_p-1\) from the pinned Puiseux pairs and test
   \[
   \deg C^\vee=168\cdot167-\sum_p(\mu_p+m_p-1)\ge0,
   \]
   together with Plücker integrality and inflection constraints. First run the two pinned pole branches alone, then optimize over admissible B/x tails.

4. **Bounded Hermite–Padé algebraization.**  
   Test whether the formal \(42\)-conjugate Puiseux orbit satisfies any polynomial relation with the prescribed Newton support. First computation: at depth \(N=\#(\Delta_f\cap\mathbb Z^2)+20\), compute the monomial-evaluation matrix modulo two good primes on the saturated residue-A locus. Uniform full rank kills algebraization; a one-dimensional kernel reconstructs \(f\), after which \(J(f,g)=1\) is linear in the coefficients of \(g\).

5. **Camacho–Sad/Baum–Bott audit of \(df=0\).**  
   Since \(df\) has no affine singularities, all foliation indices lie on the resolved boundary. First lemma: express the local eigenvalue ratios at \(R,F_s,G_m,P_i\) from the multiplicity ladder; test componentwise \(\sum CS(E,\mathcal F)=E^2\) and the global Baum–Bott total. Any failed rational identity kills the template independently of Sigray’s combinatorics.

## 3. VERDICT

My estimate is
\[
\Pr(\mathrm{JC2\ true})\approx 0.68,
\]
with a plausible \(0.55\)–\(0.80\) range.

The program’s likeliest genuine breakthrough is a **global algebraization obstruction** for the residue-A template—effectivity, polar data, or coefficient transport at the resonant direction—not another vertex-local identity. The template has survived too many exact local, coefficient, and topological checks to expect an easy kill.

Its likeliest stall is larger R1-style Gröbner bands: repeated parser, saturation, relaxation, and memory failures show that this layer scales poorly. Even success there would leave the off-axis \(M\ge2\) sector, the single-pole composite residual, and the absence of a uniform \(td\)-reduction.
tokens used
267,769
## 1. STRESS TEST

1. **The “fully adjudicated book” is not exhaustive.** [BOOK-ENUM.md](/Users/dc/code/math/jc72108/BOOK-ENUM.md:35) explicitly leaves every entry multiset containing \(b_i\ge2\)—hence \(M_{\rm entry}\ge2\)—uncalculated; mixed \(\mu\ge2\) merges are also quarantined. Yet [BOOK-BASH-R2.md](/Users/dc/code/math/jc72108/BOOK-BASH-R2.md:222) declares \(td=7,11,13\) fully excluded. Those prime panels are entirely “off-axis,” not empty. A counterexample there never enters the 421-cell enumeration. The \(td=6\) all-\(M=1\) book is unaffected, but the advertised \(td\le14\) completeness is false.

2. **The mass identity \(td=\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)\) is unproved at the strength consumed.** [SIGRAY-AUDIT.md](/Users/dc/code/math/jc72108/SIGRAY-AUDIT.md:74) reconstructs Proposition 5.8 only for generic \(a\), not “every \(a\).” This identity supplies every entry partition, \(m\le td/3\), the \(3+3\) reduction at \(td=6\), the prime theorem, and the book’s layer E. A generic-fiber reformulation may repair it, but that argument is presently missing.

3. **“The full JC2 program is finite at every level” confuses pointwise finiteness with termination.** Finiteness for each fixed \((m,td)\) gives infinitely many books; only \(td\le14\) was enumerated and the degree farm stops at 150. Moreover, killing residue-A would still leave four single-pole \(td=6\) classes, while the composite single-pole residual grows to 212 classes at \(td=16\). There is no uniform \(td\)-bound, induction, or stabilization theorem. Thus “one template away from JC2” is not justified.

Theorem A is not a weak point: its leading-degree/kernel-subtraction proof is sound. Its reach is simply depth-2 strip geometry, not general JC2.

## 2. NEW AVENUES

Ranked by expected decisiveness per effort; none appears in `RECON.md` or `notes.md`.

1. **Relative pole-divisor proof of Proposition 5.8.**  
   On a resolution \(X\) of \((f,g)\), prove for a generic fiber \(C_a\)
   \[
   td=\deg(g|_{C_a})=C_a\cdot(g)_\infty=\sum\Lambda(F).
   \]
   First lemma: the horizontal pole divisor of \(g\) is finite flat over an open subset of the \(f\)-line, with local intersection multiplicity exactly \(\Lambda(F)\). Then determine whether specialization proves the every-fiber version or whether the campaign must work generically.

2. **Resolved-pencil Noether/Cremona test of residue-A.**  
   For the degree-168 pencil, form
   \[
   D=168H-\sum m_iE_i.
   \]
   First computation: extract the pinned multiplicity cluster and test \(D^2=0\), \(D\!\cdot K_X=2g-2\), and all proximity inequalities; enumerate the narrowly constrained B/x tails, then apply unloading/Hudson reduction. This tests actual plane-curve effectivity, not merely splice or genus consistency.

3. **Teissier–Plücker polar budget.**  
   Compute the local polar numbers \(\mu_p+m_p-1\) from the pinned Puiseux pairs and test
   \[
   \deg C^\vee=168\cdot167-\sum_p(\mu_p+m_p-1)\ge0,
   \]
   together with Plücker integrality and inflection constraints. First run the two pinned pole branches alone, then optimize over admissible B/x tails.

4. **Bounded Hermite–Padé algebraization.**  
   Test whether the formal \(42\)-conjugate Puiseux orbit satisfies any polynomial relation with the prescribed Newton support. First computation: at depth \(N=\#(\Delta_f\cap\mathbb Z^2)+20\), compute the monomial-evaluation matrix modulo two good primes on the saturated residue-A locus. Uniform full rank kills algebraization; a one-dimensional kernel reconstructs \(f\), after which \(J(f,g)=1\) is linear in the coefficients of \(g\).

5. **Camacho–Sad/Baum–Bott audit of \(df=0\).**  
   Since \(df\) has no affine singularities, all foliation indices lie on the resolved boundary. First lemma: express the local eigenvalue ratios at \(R,F_s,G_m,P_i\) from the multiplicity ladder; test componentwise \(\sum CS(E,\mathcal F)=E^2\) and the global Baum–Bott total. Any failed rational identity kills the template independently of Sigray’s combinatorics.

## 3. VERDICT

My estimate is
\[
\Pr(\mathrm{JC2\ true})\approx 0.68,
\]
with a plausible \(0.55\)–\(0.80\) range.

The program’s likeliest genuine breakthrough is a **global algebraization obstruction** for the residue-A template—effectivity, polar data, or coefficient transport at the resonant direction—not another vertex-local identity. The template has survived too many exact local, coefficient, and topological checks to expect an easy kill.

Its likeliest stall is larger R1-style Gröbner bands: repeated parser, saturation, relaxation, and memory failures show that this layer scales poorly. Even success there would leave the off-axis \(M\ge2\) sector, the single-pole composite residual, and the absence of a uniform \(td\)-reduction.
