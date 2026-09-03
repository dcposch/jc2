# Software lane: MOHSIEVE leaderboard + DESCENT engine — one typed predicate harness over box/moh_skeleton_full.py, and Moh's Prop 6.3 descent as a machine, gated on the p.207 table

Round 20260903T1015Z produced THREE independent candidate sieves for
OPEN[MOH-PROGRAM] (bounded 652 excess rows at n ≤ 100), each keeping Moh's
six p.202 rows and each emptying D = 105 (charged submissions):
  Opus:  MOH-INCREMENT (A_j ≥ 2, j = 1..s−1); NOT-ALL-(11); MAJOR-MULT
         (V_j ≥ 2, j = 2..s) — 658 → 391 → 247 → 86 (V_2 ≥ 2) → 51 (all j);
  Fable: M2-ABOVE-M (M_2 > m) — 658 → 94 rows / 32 classes; + integral N ≥ 6
         (UNI) → 33 rows, 28 beyond Moh's table; AM semigroup AUTOMATIC;
  Grok (own round submission, charged): Card I — the Prop 4.6 PARTITION
         predicate: at each level j = s−1..2 with Q = V_{j+1} d_j/d_{j+1},
         a partition of Q into parts, one = V_j, the others major parts
         satisfying (10)∨(11) or minor parts ≤ d_j/(n − M_j), a ≠ 0 parts in
         Galois orbits of size A_j (untested);
  coordinator: SECOND-POINT — joint admissibility of the L_2 tower (v roots,
         u ↔ v) with the same (n, m, d_j) data (untested).
YOUR TASK (software, fail-closed):
(1) box/mohsieve/mohsieve.py — a predicate registry over
    box/moh_skeleton_full.py (name, source type PRINTED | DERIVED |
    CONJECTURE | SOURCE-UNVERIFIED, lambda) with gates: (G1) all six p.202
    rows survive [HARD]; (G2) the (75,50) residue is exactly
    {M_2 = 55, V_2 ∈ {2,3}} after integrality; (G3) rows/classes at n ≤ 100
    vs 6/4; (G4) groups and emptied degrees at 48 ≤ D ≤ 200; (G5) the
    pinned-N knapsack (uni_hits / mixed_hit, N ≥ 6 and [6,16]) downstream.
    Negative control: the EMPTY conjunction reproduces 658/63 and 1,189 /
    14,016 exactly; every predicate reports its SOLO kill count (a predicate
    whose solo count equals the base is visibly vacuous). Register the six
    predicates above (implement Card I and SECOND-POINT; for SECOND-POINT
    state precisely what "the L_2 tower" is from Def 5.1 with u ↔ v and
    which conditions are shared — if it cannot be defined from the printed
    text, register it as UNDEFINED and say why). Print the LEADERBOARD: every
    single predicate and every pairwise/triple conjunction of the passing
    ones, with (rows n ≤ 100, classes, 6/6?, (75,50) residue, groups D ≤ 200,
    degrees emptied, D = 105/108/112/117/120 alive at N ≥ 6, D = 108 rows in
    [6,16]). Also: are M2-ABOVE-M and MAJOR-MULT logically related on the
    census (implication either way? measure the four cells of the 2×2).
(2) box/mohsieve/descent.py — Moh's Prop 6.3/6.4 descent as a machine
    (Fable §5): for a (1)–(13) group with u_s = d_s − V_s = 1 emit the
    descended datum (n' = n/d_s, m' = m/d_s, M_i' = M_i/d_s, d_i' = d_i/d_s,
    Jacobian exponent k = v_s − 2), recurse while u_{s'} = 1 re-running the
    (1)–(7) gcd/window checks on the descended data and re-checking
    M_2' > m'; gates: (G6) Moh's six rows reproduce the p.207 transformed
    table to the unit — (64,48) → (16,12, M_2' = 13; X), (84,56) →
    (21,14, 16[18]; X), (75,50) → (15,10, 11; X²) — HARD fail-closed; (G7)
    every M_i'/d_s integral; (G8) the engine must NOT by itself empty
    D = 64, 75, 84, 99. Output the terminal table (n', m', k, inherited
    data, status) for all groups at 48 ≤ D ≤ 200 with u_s = 1, and the
    fraction with u_s > 1 (needing the p.209 minor-disc dichotomy). Cross-
    check GPT-5.5's Appendix-II signatures (charged): (16,12,13; X),
    (21,14,16[18]; X), (15,10,11; X²), and the (99,66) fourth-case X⁴ branch.
(3) Run the D = 105 trio through both tools; print G2 → (15,10; γ⁴, M_2' = 4)
    and G3 → (21,14; γ², M_2' = 8) explicitly, and G1's status.
(4) Reproducibility: exact replay commands, hashes, wall-clock; unit tests
    for every gate; `python3 -O` replay with an assert scan or an
    ordinary-only label (COORDINATION.md). No claim that any predicate IS
    Moh's program: the leaderboard is MEASURED; provenance stays typed.
Desk-scale (< 15 min one core, < 4 GB). Do not edit canonical ledgers; do
not inspect jc2-lean; do not read other ideation-20260903T1015Z-* files
than the three charged; do not read other running lanes' reports.
Report: xmodel/mohsieve-descent-engine-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-25KB; 120 minutes.
charged_input=xmodel/ideation-20260903T1015Z-opus5.md
charged_input=xmodel/ideation-20260903T1015Z-fable5.md
charged_input=xmodel/ideation-20260903T1015Z-grok46.md
charged_input=xmodel/ideation-20260903T1015Z-gpt55.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/mohsieve-drivers-20260903/moh4.py
charged_input=box/mohsieve-drivers-20260903/battery.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
b13149ecac656f7f3548e6cd388b1699c514ff49a53882f7239039a2c0022562  {{LANE_INPUTS}}/ideation-20260903T1015Z-opus5.md
486b0192d6cb1f3e064e00d16b57877ed67a2360543d8ec662c837afe5fc6456  {{LANE_INPUTS}}/ideation-20260903T1015Z-fable5.md
7b56aad2c1fb067481852eedecc89ba5598cd26eeb2cf3358c3b8c2f16438015  {{LANE_INPUTS}}/ideation-20260903T1015Z-grok46.md
5e1646f507e946b831dcb77d542f7ab367eb398227a3032b96bcd7a45d2f320d  {{LANE_INPUTS}}/ideation-20260903T1015Z-gpt55.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
cdf5eeb7d9e40021642837805bf97c307fcfe8b2900ce50ec4a510e712d083d2  {{LANE_INPUTS}}/moh4.py
d6e40234299f21ba7c7c08433f5bc219f7f139003756ad90cebd05f29f251685  {{LANE_INPUTS}}/battery.py
```
