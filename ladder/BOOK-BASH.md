# BOOK-BASH.md — deep-arsenal bash of the 22-class book (td = 6..14)

Status: SYNTHESIS of the per-class bash campaign, 2026-08-12. Ground:
BOOK-ENUM.md (421 cells → 75 survivors / 22 classes / 18 panels,
systems/book/*.json), engines cases/{l1_ode_check, hiii_compose, h3_check,
sheet6_campaign, book_enum, template_lift}.py (read-only), thesis
refs/sigray_full.pdf, forced readings per SIGRAY-AUDIT.md. Arsenal, applied
in order per class: **T1** pattern algebra at the cell (SHEET6-L1 method,
Prop 8.1(iv) rigid solve), **T2** suffix chase (SHEET6-MULTIPOLE MP2 +
composed E5-III/N1/AF2-IIb/ψ-budget kill set), **T3** coefficient-level
lift (SHEET6-TEMPLATE E-mechanism), **T4** promoted w-arithmetic
(SHEET6-DEPTH) where chain context enters. Every T2/T3 harness was gated
on the promoted td=6 record before use (gate PASS in every run).

## 0. Verdict

**9 of 22 classes bashed (38 of 75 cell instances). 3 classes killed
outright + 1 panel of a 4th: 13 instances DEAD (6 review-confirmed, 7
engine-verified pending review). 6 classes survive the full deep arsenal
(25 instances), each bottoming out in a rigid one-scale coefficient
template of exactly the residue-A kind. 13 classes (37 instances: 8 ZCH +
5 family-I) NOT YET BASHED.** No new td becomes fully excluded: td = 7,
11, 13 remain the only fully-excluded degrees (TDU prime theorem on the
single-pole side + empty prime panels on the multi-pole side, unchanged),
because the residue-A class IIa(2,3,1)M2@w2 is present in every non-empty
panel and is now proven to survive tiers 1–3 in **all 10** of its panels
— and because every composite td is independently blocked by the promoted
TDU single-pole residual (§5). The multi-pole bottleneck of the ladder is
therefore a single object: the residue-A template (a1/a2 = 2±√3,
b = (2/3)σ, suffix B = (3/2)A), whose closure requires the L1 §7.2 global
layer — beyond the printed statement list.

## 1. Verdict table

Bashed classes (cell = (fam, r, ν, l) M @ w, κ̄_m, child (κ̄, D/i, ρ)):

| class | cell / child | panels | verdict | mechanism | confirmed? |
|---|---|---|---|---|---|
| IIa(2,3,1)M2@w2 (residue-A) | κ̄5, (5,3,1/2) | 10: m=2 td6(gate),8,9,10,12,14; m=3 td9,12,14; m=4 td12 | **SURVIVES** | T1/T2/T3 exhausted; T1 + shape-local T3 transfer verbatim from td=6; suffix arithmetic only loosens with td (slack 1→9; IV classes 4→5/7/9/14/20) | n/a (survival; superset-sound) |
| IIa(2,3,1)M2@w4 | κ̄10, (10,6,1) | 4: m=2/3/4 td12; m=2 td14 | **SURVIVES** | T1 identical rigid solve (frame-homogeneous); T2: 13/24 IV-survivor classes, 0 open; T3 pole collapses exact at (2,3)ν1, (2,3)ν2, (2,7)ν2; δ-ladder consistent | n/a |
| IIa(2,7,1)M2@w4 | κ̄11, (11,7,1/2) | 4: m=2/3/4 td12; m=2 td14 | **SURVIVES** | td=6 reach-kill of (7,1) does NOT transfer (cell reachable here); T1 rigid (a1/a2=(4+√7)/3); T2: 14/20 IV classes incl. residue-A quartet; T3 W-quintic + pole deg-6 collapses exact, zero slack | n/a |
| IIa(2,5,1)M2@w3 | κ̄8, (8,5,1/2) | 3: m=2 td10,12,14 | **SURVIVES** | T1 rigid (a1/a2=(3+√5)/2, b=3σ/5); T2: 9/14/20 IV classes, 0 open; T3 all count laws close with equality; E4 agreement reproduced | n/a |
| IIa(3,2,1)M3@w2 | κ̄6, (6,4,2/3) | 4: m=3 td9,12,14; m=4 td12 | **DEAD** | T1: recursion numerator r−(ν+1)=0 forces p₀=0, c̃=0 ⟹ ⊖=0 contradicts Prop 8.1(iv); degenerate pt=t(t−b)² triply inadmissible (0-root, double root, root law). Frame-free — one solve kills all 4 panels | **YES** — kill_confirmed, 2 adversarial votes (NOT REFUTED / VERIFIED, no escape found) |
| IIa(3,5,1)M3@w2 | κ̄7, (7,5,1/3) | 4: m=3 td9 / m=3,m=4 td12 / m=3 td14 | **PARTIAL** — m=3,td9 DEAD; other 3 SURVIVE | Kill at T2: cheapest IV route costs Σλ = 7 > St 9.4 cap td−1−ψ = 6 at td=9 (all 4 reachable IV shapes KILLED_ψ, 0 open, 0 frontier). td=12/14: budgets 10/12 give slack 2/4; T1 rigid solve exists; T3 vertex-local layer closes | **YES** for the td=9 kill — kill_confirmed, 2 votes (VERIFIED, PARTIAL stands / NO ESCAPE FOUND) |
| IIa(4,3,1)M4@w2 | κ̄8, (8,6,1/2) | 1: m=4 td12 | **DEAD** | T1: full-rank 4×4 system, unique solution pt=t(t−1)³ = the homogeneous branch ((ν+1) \| r degeneracy), c̃=0; quadruple-inadmissible (⊖=0, 0-root, triple root, b a root) | **YES** — kill_confirmed, 2 votes (NOT REFUTED / CONFIRMED, incl. full independent re-implementation) |
| IIa(4,7,1)M4@w2 | κ̄9, (9,7,1/4) | 1: m=4 td12 | **SURVIVES** | T1–T4 exhausted; T1 rigid quartic 128t⁴−448t³+560t²−280t+35; T2: 15 IV classes + 2 OPEN μ=3 III-E5 parametric nodes; T3 W deg 8→3 (five exact cancellations); first coefficient-consistent m=4 Theorem-O escape | n/a (note: only bashed class with OPEN suffix kinds) |
| ZCH(2,2,3)M3@w4 | κ̄6, (6,2,2/3) | 7: m=2 td9,12,14; m=3 td9,12,14; m=4 td12 | **DEAD** | T1 (family Z): triangular ladder forces unique s = t(t−a)² and C=0 ⟹ ⊖=0; triple-overdetermined (root law, eta law, MP6(c) simple-q-roots all violated). Depends only on (ν,l)=(2,3) via ρ=1/3 — frame-free, kills all 7 panels at once | **PENDING REVIEW** — record arrived truncated, no votes banked; engine cross-check re-run at synthesis: `l1_ode_check.check_ZCH(2,3)` → s=[0,1,−2,1], ct=0, const_ok=False, s_avoids_pt_and_0=False — REPRODUCED |

Not yet bashed (13 classes, 37 instances — no results supplied):

    ZCH @w4: (2,2,6)M3 κ̄5 [7 panels], (2,4,5)M5 κ̄5 [7 panels]
    ZCH @w6: (2,2,3)M3 κ̄9, (2,2,9)M3 κ̄7, (2,3,2)M2 κ̄10, (2,3,4)M4 κ̄8,
             (2,3,8)M4 κ̄7, (2,6,7)M7 κ̄7            [2 panels each: m=2,td12; m=4,td12]
    I   @w2: (3,1,3)M3 κ̄4, (3,1,6)M3 κ̄3 [4 panels each: m=3 td9,12,14; m=4 td12],
             (4,1,2)M2 κ̄6, (4,1,4)M4 κ̄4, (4,1,8)M4 κ̄3 [m=4,td12 only]

## 2. Kill records (decisive arithmetic)

- **IIa(3,2,1)M3@w2** (T1). ODE coefficient system p_{k−1}/p_k =
  b(r−(ν+1)k)/((ν+1)(r−k+1)), c̃ = −bρ·p₀ at ρ = 6/9. At (r,ν) = (3,2)
  the k=1 numerator is 3−3 = 0 ⟹ p₀ = 0 ⟹ c̃ = 0 for every b —
  contradicting the printed ⊖ ≠ 0; the residual family t(t−b)² breaks
  MP6(a)/St 3.18/root law independently. Vertex-local: no td, m, w, entry
  datum enters ⟹ all 4 panels die. Machine: /tmp/iia321_bash.py, exact
  fractions, residue-A validation gate PASS. Re-proves the quarantined
  §7 criterion "IIa l=1 exists iff (ν+1) ∤ r" at full tier.
- **IIa(4,3,1)M4@w2** (T1). Rank-4 elimination at gauge b=1: unique
  pt = t(t−1)³ with c̃ = 0 — exactly the homogeneous branch q = C·p^{1/ρ}
  existing because a = r/(ν+1) = 1 ∈ ℤ; quadruple-inadmissible. Sole
  panel m=4,td12 dies. Machine: /tmp/iia_r4_ode.py; solver validated
  against residue-A closed form and §7 exhibits.
- **IIa(3,5,1)M3@w2, panel m=3,td=9 only** (T2). From child (1/3,5,3,7):
  cheapest route to any case-IV terminal costs Σλ = 4+3 = 7; every
  reachable IV terminal has R ≥ 3 ⟹ ψ ≥ 2 ⟹ St 9.4 cap = 9−1−2 = 6 < 7.
  All four IV shapes KILLED_ψ (incl. 40-instance s-sweep + s→∞ limit);
  deeper continuations cost 8/9/11 > budget 7; opens = 0, frontier = 0.
  td-forced, not m-forced. Gate: residue-A and ZCH td=6 records
  reproduced cell-for-cell.
- **ZCH(2,2,3)M3@w4** (T1). Reduced family-Z ODE, ρ = (ν+1)/((l+1)ν+1) =
  1/3: triangular ladder s₂ = −2a, s₁ = a², s₀ = 0, C = 0 ⟹ unique
  s = t(t−a)² with ⊖ = 0; violates root law (q-mult 3 at chain orbit),
  eta law (η-mult 3), and simple-q-roots simultaneously. (ν,l)-local ⟹
  all 7 panels. Machine: /tmp/zch223_verify.py (5 gauges) + repo engine
  agreement (re-verified in this synthesis session).

## 3. Surviving-cell census — what each needs next

All six survivors terminate in rigid one-scale templates; none is
closable from the printed statement list (Theorem-O escape lν ≡ −1 mod r,
M = r, in every IIa case).

1. **IIa(2,3,1)M2@w2 (residue-A), 10 panels.** Template a1/a2 = 2±√3,
   b = (2/3)σ, suffix B = (3/2)A — identical in every panel. Needs: the
   L1 §7.2 global layer (h1-branch budget at the resonant direction, or
   Puiseux substitution transport), OR a per-panel E-mechanism context
   run: the pole-level E5/E6 lead transports exist only for td=6 row-1
   (2,3)-poles; the other 9 panels' pole rows (ν ∈ {1..6}, a ∈ {1,2,3})
   and global types ((3,4),(2,5),(4,5),(5,6),(2,7),(3,7),(6,7), tower
   h1 = g^α − s0(f−a)^β) each need a fresh ladder. Nothing tightens with
   td (St 9.4 slack grows 1,3,4,5,7,9 at td=6..14; IV residual grows
   4→5/7/9/14/20 classes, first (ν,κ̄)=(1,1) SF1 children at td ≥ 12).
2. **IIa(2,3,1)M2@w4, 4 panels.** Needs: R1 Puiseux/substitution
   transport; full E2–E4 tower/count analysis down each of the 13 (td12)
   / 24 (td14) surviving suffix routes; cascade-branch tower-depth at the
   m=3/4 final joins (R6-type variants, unrun); P-realizability.
3. **IIa(2,7,1)M2@w4, 4 panels.** Residue-A residual set at ν=7: Puiseux
   transport between the pinned levels; global h1-branch budget at
   b = (4/7)σ; deeper-tower i ≥ 4 variants (level ratio (7i+22)/(14i) < 1
   changes tower data — open for residue-A too).
4. **IIa(2,5,1)M2@w3, 3 panels.** R1 transport, R2 h-Newton budgets at
   infinity, x-side ψ realizability, absolute P-realizability; deeper
   R6-analogue tower window (k-integrality auto-satisfied, unrun).
5. **IIa(3,5,1)M3@w2, 3 remaining panels (m=3/m=4 td12, m=3 td14).**
   Sharpest single lever in the whole census: the E4-analogue collapse
   W(t) = t(t−b)⁵ − P(t)² drops only to **deg 2** at the rigid
   coefficients (residue-A's analogue hit deg 1 exactly as its count law
   demanded). If a per-panel TEMPLATE genome (absolute κ-ladder through
   the μ=3, ν_F=1 first suffix vertex) demands deg ≤ 1, **all three
   surviving panels die at once**. TEMPLATE-scale work, not vertex-local.
6. **IIa(4,7,1)M4@w2, 1 panel (m=4,td12).** Needs: global/transport tier
   — E2/E3 count-law sweep per surviving suffix class in the (m=4,td12)
   frame (is the deg-3 W-residual compatible with any of the 15 suffix
   classes' h2-branch counts?), or St 3.9 Puiseux realizability. Also
   the only bashed class with OPEN tier-2 kinds (2 parametric μ=3 III-E5
   nodes at λ ≥ 5) — resolve before any claim of suffix completeness.

Unbashed classes — next steps per BOOK-ENUM §5: ZCH cells need the
ratio-partner realizability lift (depth_closure_check.zch3_edges) + their
own family-Z T1 solves; family-I cells (r ≥ 3) await the r ≥ 3 even-l
log-obstruction analogue / Laurent residue computation C(−n, n−1), which
could kill all five outright.

## 4. Per-panel census after the bash

    panel      pre-bash | killed here | template-survivors | unbashed
    m=2,td= 6      1    |     0       |   1 (residue-A)    |   0
    m=2,td= 8      1    |     0       |   1 (residue-A)    |   0
    m=2,td= 9      4    |     1       |   1                |   2
    m=3,td= 9      8    |     3       |   1                |   4
    m=2,td=10      2    |     0       |   2                |   0
    m=2,td=12     13    |     1       |   4                |   8
    m=3,td=12     10    |     2       |   4                |   4
    m=4,td=12     21    |     3       |   5                |  13
    m=2,td=14      7    |     1       |   4                |   2
    m=3,td=14      8    |     2       |   2                |   4
    TOTAL         75    |    13       |  25                |  37

## 5. Per-td exclusion status (single-pole + this bash + prime panels)

Combining ledger. Single-pole ground truth is SHEET6-TDUNIFORM (promoted):
the PRIME THEOREM excludes single-pole at entry for every prime td,
unconditionally; at composite td the printed+composed kill set leaves an
authoritative residual of ψ/(l)/(m)-consistent case-IV terminal classes —
4/16/16/23/71/48 at td = 6/8/9/10/12/14 (TDU-t: no budget-side sharpening
removes them; closure at td ≤ 9 only conditionally under H3-strong, which
is new math). Multi-pole ground is this book + this bash.

| td | single-pole residual (TDU) | multi-pole book after bash | FULLY excluded? |
|---|---|---|---|
| 6 | 4 classes (2 slack-1, 2 slack-0) | 1 cell: residue-A only | NO |
| 7 | 0 (prime theorem) | empty (prime-panel shadow; off-axis only) | **YES** |
| 8 | 16 classes | 1 cell: residue-A only | NO |
| 9 | 16 classes | 8 cells (2 residue-A instances + 6 unbashed) | NO |
| 10 | 23 classes | 2 cells: residue-A + IIa(2,5,1)@w3, both template-rigid | NO |
| 11 | 0 (prime) | empty | **YES** |
| 12 | 71 classes | 38 cells (13 template + 25 unbashed) — the main residue | NO |
| 13 | 0 (prime) | empty | **YES** |
| 14 | 48 classes | 12 cells (6 template + 6 unbashed) | NO |

**Fully excluded: td = 7, 11, 13 — unchanged.** This bash adds no
fully-excluded td and structurally cannot: residue-A sits in every
non-empty panel and survives everywhere, and every composite td is
independently blocked by the TDU single-pole residual. On the multi-pole
side it does reduce td = 6 and td = 8 to the closure of the single
residue-A template, and td = 10 to two rigid IIa templates. Live book
instances: 75 → 62 (25 template + 37 unbashed).

## 6. Honest riders

1. **Unconfirmed kill.** The ZCH(2,2,3)M3@w4 kill (7 instances) carries
   NO banked adversarial review votes; its result record arrived
   truncated mid-derivation (the frame-transfer adjudication of the td=6
   suffix-precedent half is incomplete in the record). The mechanism is
   triple-overdetermined and was independently reproduced by the repo
   engine in this synthesis session, but it should be treated as
   ENGINE-VERIFIED, REVIEW-PENDING until refereed. All other kills
   (IIa(3,2,1) ×4, IIa(3,5,1)@td9 ×1, IIa(4,3,1) ×1) are
   kill_confirmed with 2 adversarial votes each.
2. **PARTIAL.** IIa(3,5,1)M3@w2 is killed only at m=3,td=9 (td-forced
   budget-vs-ψ arithmetic); its other 3 panels survive to a rigid
   template with a flagged TEMPLATE-scale lever (W-residual deg 2 vs
   deg ≤ 1, §3 item 5) that is promising but UNRUN.
3. **Unbanked corollary lead.** The ZCH T1 kill depends only on
   (ν,l) = (2,3) via ρ = 1/3, which is frame-free — the unbashed class
   ZCH(2,2,3)M3@w6 κ̄9 (2 panels) should die by the literally identical
   linear system. Not claimed here: it needs its own record and review.
   (The IIa (ν+1) \| r criterion has no further targets in the book.)
4. **Context halves unrun.** For every IIa survivor the tier-3
   pole-level/context half (E5/E6 lead-transport ladders per panel, and
   for @w4 the m=3/4 cascade-branch towers) is honestly UNRUN; no kill is
   claimed or expected from it without new per-panel computation, but no
   consistency verdict exists there either. IIa(4,7,1)'s 2 OPEN tier-2
   parametric nodes are unresolved.
5. **13 classes untouched.** No bash results exist for the 8 remaining
   ZCH classes and 5 family-I classes (37/75 instances) — the RESULTS
   stream ends inside the ZCH(2,2,3)@w4 record. All 37 remain live under
   the book's superset stance.
6. **Perimeter (inherited, unchanged).** Survival is superset-sound:
   P-realizability untracked; join-context existence conservative; μ_e ≥ 2
   mixed merges quarantined (m=3/4 second joins ride the any-context
   stance); off-axis (b_i ≥ 2) entry configurations — 100% of the prime-td
   panels and 27 multisets overall — sit outside the closed M=1 lemma, so
   "fully excluded" at td = 7, 11, 13 is relative to the same MP
   quarantine perimeter as the rest of the program. On the single-pole
   side, the composite-td residual (§5) additionally inherits TDU's F1–F5
   failure modes (SF1 unmodeled, III-tail opens at td ≥ 10, depth frontier
   at td ≥ 12).
7. **Do-not-rebash honored.** td=6/m=2 residue-A was used only as the
   mandatory gate in every harness (all gates PASS, cell-for-cell); the
   transfer question was answered instead: tier 1 and the shape-local
   parts of tiers 2–3 transfer verbatim, and the (td,m) frames change the
   suffix arithmetic only monotonically in the survivor's favor.

## 7. Artifacts

Session artifacts (outside repo, exact int/Fraction arithmetic, all
gate-checked): /tmp/bash_iia231.py, /tmp/bash_iia271/{suffix_run,
wcollapse, pole27, final_checks}.py, /tmp/bash_iia251.py,
/tmp/tier3_iia251.py, /tmp/iia321_bash.py, /tmp/tier1_iia_351.py,
/tmp/tier2_suffix_351.py, /tmp/tier3_steps_351.py, /tmp/iia_r4_ode.py,
/tmp/bash_iia471/{tier1_ode, tier2_suffix, tier3_collapse,
tier3_suffix_coeff}.py, /tmp/zch223_verify.py. Repo grounds (read-only):
/Users/dc/code/math/jc72108/BOOK-ENUM.md, SHEET6-L1.md,
SHEET6-MULTIPOLE.md, SHEET6-DEPTH.md, SHEET6-TEMPLATE.md,
SHEET6-TDUNIFORM.md, SIGRAY-AUDIT.md, cases/{book_enum, l1_ode_check,
hiii_compose, h3_check, sheet6_campaign, template_lift}.py,
systems/book/book_m{2,3,4}_td{6..14}.json, refs/sigray_full.pdf.