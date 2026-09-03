# Instrument + review lane: DESCENT-RADII — measure the logarithmic radii δ' of a Prop 6.3-descended pair on Moh's own (15,10) and (16,12) Appendix-II shapes; close OPEN[DESCENT-RADII] (10 rationals); different-model gate on the M₂ > m refutation; then reduce the descended D = 105 problems G2/G3 to Appendix-II size

Charged: m2-descent-opus5-20260903.md (Opus; drivers box/m2descent-drivers-
20260903/: etaexp.py exact η-expansion and characteristic data, autoscan*.py
the automorphism population, descent_table.py the Prop 6.3 descent with the
p.207 gate, moh_1510_control2.py the Appendix-II (15,10) control). Its
findings: (i) M₂ > m is FALSE for Keller pairs in Moh's gauge (12 automorphism
witnesses; the n = 4, m = 2 witness printed in full: check it BY HAND from
its printed f, g: J, deg = deg_y, the η-expansion coefficients f_{−2..3} and
M = [−2, 1]); (ii) the descent rule n' = n/d_s, m' = m/d_s, M_i' = M_i/d_s,
d_i' = d_i/d_s, V_i' = V_i, Jacobian γ^{v_s−u_s−1} reproduces p.207's
(n, m, M₂, V₂, J) on all four u_s = 1 rows, but the p.207 columns
δ₂' = (−1, −1/2[−1], −1) and δ₁' = (1/4, 7/6[1/3], 1/2[4/3]) are reproduced by
NO natural candidate (Def 5.1(3) on the descended data with s' = 2 gives
−1/2, −1/4, −1/2, −1/3; the shift δ_i' = δ_{i+1} fails on (84,56); the
parameter-change law δ_new = v_s − u_sδ_old gives 11/4, 39/16 on (64,48)):
OPEN[DESCENT-RADII], 10 rationals; (iii) Moh's (15,10; M₂ = 11, V₂ = 3; X²)
case reproduced with ERRATUM[APPII-GAMMA-B] (the B-coefficient of γ is
−a₉²a₈, not −a₉²a₁₀); the kill via c₂ − 3γ ∈ k saturating to the unit ideal.
The Moh PDF: refs/moh1983_jram340_configurations_of_roots.pdf (page N = PDF
page N−139; pdftoppm -r 300; read images): Def 5.1 p.179, Props 5.1–5.4
pp.176–185 (the definition of the logarithmic radius of a disc in terms of
the pair), Prop 6.3/6.4 pp.196–198, Appendix II pp.207–211.
YOUR TASK:
(A) GATE (different model): rerun etaexp.py on the printed n = 4 witness and
    verify by hand; rerun autoscan2.py and confirm the 12/25 split; confirm
    the refutation of "M₂ > m for Keller pairs in Moh's gauge" (CONFIRMED /
    GAP / REFUTED), and check the residual claim that the witnesses fail
    (4) or (6). Rerun moh_1510_control2.py + controls_pm.py; re-derive γ by
    hand (A² ≡ (a₆x + a₇)A − a₈B mod h; Ay ≡ −a₈) and confirm the erratum.
(B) MEASURE δ'. Route (b) of the charged §4.3: take Moh's (15,10) shapes
    (5)–(6) (h = (y² − x² + a₁y + a₂x + a₃)y³ + (a₄x + a₅)y² + (a₆x + a₇)y +
    a₈; β = a₉A + a₁₀y + a₁₁x + a₁₂; f = h² + 2β; g = h³ + 3βh + (3/2)α) with
    random admissible rational a₁..a₁₂ (several draws), and the (16,12) shapes
    of p.208 (h = y³(y − x) + b₁y³ + b₂y² + b₃y + b₄; ḡ = h⁴ + α₁h³ + … + α₄,
    deg_y α_i ≤ 3; f̄ = h³ + β₂h + β₃), and COMPUTE the disc structure of the
    roots of g − c (Puiseux expansions in x → ∞ via exact Newton–Puiseux over
    Q or high-precision numerics with a rational-reconstruction check): the
    logarithmic radii of the major discs (Moh Def 4.1 / 5.1: the radius is
    the t-order of the pairwise contact of the roots in the disc, t = x^{−1}
    — state the exact convention you use, δ_s = −1 at the top), the number of
    roots per disc, and the V-data. Read off δ₂', δ₁' and compare with the
    printed p.207 values (−1, 1/2) for (15,10; V₂ = 3) and (−1, 1/4) for
    (16,12). DECIDE: (i) which convention/definition reproduces the printed
    columns — is δ' Def 5.1(3) applied to the descended data with some
    reindexing, a transformed radius (state the law), or measured only; (ii)
    the value of each of the 10 rationals (CONFIRMED-PRINTED / CORRECTED /
    UNDECIDED); (iii) the general RULE δ' = Φ(tower data) if one emerges,
    tested on all five u_s = 1 rows of p.207. Also verify on the descended
    pair that Moh's "in the major disc D₂ there are precisely three subdiscs
    which contain 2, 2, 6 roots of f" (p.210) is what the numerics show.
(C) If a rule or the measured δ₁' is in hand: apply the Appendix-II shape
    reduction to the two descended D = 105 problems G2 = (15,10; J = cx⁴;
    M₂' = 4, V₂' = 1, d₂' = 5) and G3 = (21,14; J = cx²; M₂' = 8, V₂' = 1,
    d₂' = 7) as written in the charged §4.3 (h, β, G₁, G₀ normal form; the
    monomial Lemma 2.1: g_j ∈ k for j < m' − 1, deg_x g_{m'−1} = k + 1; the
    exponent dictionary M₂ = N + (n' − m')): derive the forced shapes of h
    and β from δ₁' and the subdisc split, count the surviving unknowns, and —
    if the system is ≤ ~30 unknowns — SOLVE it exactly (Gröbner over Q,
    saturate at the unit leaders and c ≠ 0; Rabinowitsch; positive/negative
    controls on the saturation): SATURATED-EMPTY / SURVIVES (print the
    solutions) / COUNTING-BOUND. Note: AUDIT delta 17(p) (provisional) says
    the whole-tree screen already empties D = 105 — a SATURATED-EMPTY here
    would be an independent second kill; a SURVIVES would be a contradiction
    to investigate, not a counterexample.
Discipline: PROVED-HERE/UNREVIEWED; SOURCE-READ per citation; bounded
quantity + cheapest test of every OPEN; desk-scale (< 30 min one core,
< 6 GB); no ledger edits; no jc2-lean; do not read ideation-20260903T1015Z-*
files or other running lanes' reports. Drivers to
box/descentradii-drivers-20260903/.
Report: xmodel/descent-radii-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-30KB; 120 minutes.
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=box/m2descent-drivers-20260903/etaexp.py
charged_input=box/m2descent-drivers-20260903/autoscan2.py
charged_input=box/m2descent-drivers-20260903/descent_table.py
charged_input=box/m2descent-drivers-20260903/moh_1510_control2.py
charged_input=box/m2descent-drivers-20260903/moh_1510_controls_pm.py
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
eaf6b6de7a5841d628a168db4e6293fd3d3843da337e969b455cd43f310bd8bb  {{LANE_INPUTS}}/etaexp.py
e84fa92ff380f90558ace924d924b777f723f845cd1809534390fa3268a1328f  {{LANE_INPUTS}}/autoscan2.py
aad83d39a8830f2eb3ff888997394bbc9cbf58e1074fe61f3695f3e797764c87  {{LANE_INPUTS}}/descent_table.py
5ea3845b6e6f7022a59b0620b22f017c632ef08e6e5d0675f9c3d0274032566b  {{LANE_INPUTS}}/moh_1510_control2.py
add00ccc08951cc356891e3198bb39bf8ae5b55ffd182354ace7ba8a8ef3aa8a  {{LANE_INPUTS}}/moh_1510_controls_pm.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
