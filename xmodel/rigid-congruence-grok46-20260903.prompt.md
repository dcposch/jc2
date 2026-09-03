# Software + measurement lane (fast): (A) intersect the 19 rigid dessin assignments (expdim 0) with the whole-tree screen; (B) the congruence form of the screen — A_j | P_j along the tree — and whether a screened cofinal ray can be CONSTRUCTED by solving it

From the blind Opus submission of round 20260903T1200Z (charged; §0 H3–H4,
§7, §10 Card 2, §13): (H3) the packet's "uniform kill b_min = P mod A₂ > h ⇒
Prop 5.6" is REFUTED as an all-degree statement — 25 of the 60 C_FULL_TREE
survivors at n ≤ 100 have b > h and survive (the kill is a three-way
conjunction with the path-dependent danger flag; Opus's second gate has since
also shown the Prop 5.6 step is gapped — AUDIT delta 17(u): use the GAP-FREE
screens partition + siblings + (12)/(13) [+ ODE + passport] as the operative
ones, and report the gapped C_FULL_TREE as a side column); (H4) the threshold
h = d_j/(n − M_j) equals P_j/Q_j identically, so on the stratum Q_j > P_j "no
forced major zero at node j" is exactly the divisibility A_j | P_j — the
screen is a system of congruences along the tree, and congruence systems are
cofinally satisfiable unless obstructed; the two dead rays died because
A₂ ∤ P₂ with constant nonzero residue. (Card 2) dessin-tower-dim-grok46 §6.4
lists 19 assignments with expdim = 0 in 48 ≤ D ≤ 120 (rigid: no continuous
freedom; the coefficient system is expected zero-dimensional) — nobody has
intersected them with the tree screen.
YOUR TASK:
(A) RIGID ∩ SCREEN: take the 19 rigid assignments (charged dessin-tower
    report §6.4) and run each through the gap-free screens and, as a side
    column, the gapped C_FULL_TREE(_ODE) (box/mohprog-drivers-20260903/
    full_tree_partition.py; candidate_eval.py's predicates); list survivors
    with full data (n, m, M, V, |O|, packets, N, u_s, descent datum if
    u_s = 1). If nonempty: those are the campaign's most concrete CE
    candidates (zero-dimensional coefficient systems) — for each survivor
    with u_s = 1 emit its descended datum and the Appendix-II-size system
    size estimate; if empty: state "the screen kills the rigid stratum"
    with the killing node per row.
(B) THE CONGRUENCE SCAN (Opus §7, §13 OPEN[SCREEN-CONGRUENCE-RAY]): for the
    screened survivors at D = 108, 112, 120 (from candidate-results.json /
    the tree drivers), emit per node the tuple (A_j, P_j, Q_j, P_j mod A_j,
    h_j = P_j/Q_j) along the selected path and for every forced sibling
    (TreePartition.level_data); then ATTEMPT THE CONSTRUCTION: for one-
    parameter linear families (n(t), m(t), M_i(t), V_i(t)) extending a
    D = 108 survivor (vary V₂ and V₃ linearly; keep (d, e) and s), compute
    A_j(t) (reduced denominators of L·δ_j from Def 5.1(3)) and P_j(t)
    symbolically/along t = 0..30, and decide whether b_j(t) = P_j(t) mod
    A_j(t) can be driven to 0 (or ≤ h) at every node on an arithmetic
    progression of t — i.e. whether a SCREENED cofinal ray exists in closed
    form (give it with the algebra, checked by the drivers at ≥ 6 members,
    and verify (1)–(13) + the gap-free screen + orbit-integral N ≥ 6 on each
    member), or whether the residue is provably constant and nonzero along
    every linear extension (then state the resulting all-degree kill
    mechanism as a conjecture with its exact hypothesis).
(C) Also compute the post-screen fraction of u_s > 1 rows at 48 ≤ D ≤ 200
    (Opus §3: pre-screen 4,012/14,016; the post-screen number is a 10-minute
    job) and the anchor-zero count (M_{s−1} = n − d_s) among screened u_s = 1
    survivors at D ≤ 200 — the domain of theorem (T).
Typed block; bounded quantity + cheapest test of every OPEN; fail-closed
(Moh's six rows survive every screen; the unscreened counts reproduce).
Desk-scale (< 20 min one core, < 4 GB); no ledger edits; no jc2-lean; do not
read ideation-20260903T1200Z-* files other than the charged Opus one, nor
other running lanes' reports. Drivers to box/rigid-congruence-20260903/.
Report: xmodel/rigid-congruence-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-25KB; 90 minutes.
charged_input=xmodel/ideation-20260903T1200Z-opus5.md
charged_input=xmodel/dessin-tower-dim-grok46-20260903.md
charged_input=xmodel/whole-tree-review-opus5-20260903.md
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/mohprog-drivers-20260903/candidate_eval.py
charged_input=box/mohprog-drivers-20260903/candidate-results.json
charged_input=box/wholetree-drivers-20260903/opus5_probe.py
charged_input=box/branch-orbits-v2-20260903/nested_pack.py
charged_input=box/moh_skeleton_full.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
2e4e817267cbfdba97607a41df0433b11f3d4542dbb5418226aa48982830accd  {{LANE_INPUTS}}/ideation-20260903T1200Z-opus5.md
693b206806a75a557bfb02683fc7b937d0529a677b4b7476cac3b4c9a151cd0e  {{LANE_INPUTS}}/dessin-tower-dim-grok46-20260903.md
27551a88ab6ee9f62a5606010adcd9d4a1fd4411a09d97c699e13a67c84f7096  {{LANE_INPUTS}}/whole-tree-review-opus5-20260903.md
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553  {{LANE_INPUTS}}/candidate_eval.py
01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2  {{LANE_INPUTS}}/candidate-results.json
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  {{LANE_INPUTS}}/opus5_probe.py
36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067  {{LANE_INPUTS}}/nested_pack.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
```
