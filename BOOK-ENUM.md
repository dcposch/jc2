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

