# Software + measurement lane: the SCREENED CENSUS — C_FULL_TREE (and the ODE sharpening) composed with the exact orbit-aware nested-pack knapsack, to D ≤ 400: the operative census after AUDIT delta 17(r); survivor lists at D = 108/112/120; growth with D; cofinality of the screened space

Promoted today (charged): the whole-major-tree obligation and the finite
screen C_FULL_TREE (box/mohprog-drivers-20260903/full_tree_partition.py,
candidate_eval.py, tree-independent.py; three-way row agreement; 658 → 60
at n ≤ 100 keeping Moh's six; D = 105 and D = 117 have no survivor on the
campaign space; both fixed-N rays die by a forced major zero sibling at
j = 2); the ODE sharpening (3.7) P − Qu ≠ 0 at every p-root (60 → 58);
the orbit-size law and the EXACT nested parent-indexed packing DP
(box/branch-orbits-v2-20260903/nested_pack.py; 587 / 470 alive at D ≤ 120
on the unscreened space). NOT promoted: the passport (3.8) (EXTERNAL) and the
edgewise recentring (OPEN) — report them as separate columns, never fold
them into the operative numbers.
YOUR TASK (fail-closed; Moh's six rows must survive every screen; the
unscreened columns must reproduce 1,189 / 587 / 470 at D ≤ 120 and 14,016 at
D ≤ 200):
(1) Build box/screened-census/screened_census.py composing, per (1)–(13)
    V-assignment, C_FULL_TREE (bare), C_FULL_TREE_ODE, [C_FULL_TREE_PASSPORT
    and +RECENTER as typed side columns] with the nested-pack orbit knapsack
    (N ≥ 6 and [6,16]); run 48 ≤ D ≤ 200 and extend to D ≤ 400 (state wall
    time; the tree DP must carry the higher V-tuple in its state — verify
    against the frozen drivers row-for-row at n ≤ 100 and at D ≤ 120).
(2) Report per degree: (1)–(13) groups; tree-alive; tree+ODE alive; nested-
    orbit alive at N ≥ 6 and in [6,16] after each screen; degrees EMPTIED by
    each screen; the exact survivor LISTS at D = 108, 112, 120 (m, M, V, |O|,
    packets, N) under C_FULL_TREE_ODE + nested; the smallest screened
    survivor above 100 with its full data (the new first realisation target,
    with its u_s and Prop 6.3 descent datum).
(3) COFINALITY: does the screened space (C_FULL_TREE_ODE + orbit-integral
    N ≥ 6) stay nonempty as D grows through 400 — plot counts per D and per
    divisor structure (K, e, s); identify any closed-form family that
    survives the screen for all members (test candidate rays symbolically:
    the kill mechanism for the two dead rays was b_min = P mod A₂ > h — find
    rays with P ≡ 0 mod A₂ or with b_min ≤ h, e.g. fix (d,e), s = 3 and solve
    for M₂ so that A₂ | V₃d₂/d₃); if a screened cofinal family exists, give
    it in closed form with the algebra in the parameter (as delta 17(n)'s
    reviewer did); if none is found up to D ≤ 400, say so with the search
    bound. This decides whether the screened census can be a proof program
    (Q3(f) after the screen).
(4) The residue at n ≤ 100: the 58 C_FULL_TREE_ODE rows minus Moh's six =
    52 rows; list them with u_s, (10)/(11) status and descent datum; how many
    have u_s = 1 (descend by Prop 6.3).
Typed block; bounded quantity + cheapest test of every OPEN. Desk-scale
(< 20 min one core, < 4 GB; if D ≤ 400 exceeds it, stop at the largest D
that fits and say so). No ledger edits; no jc2-lean; do not read
ideation-20260903T1015Z-* files or other running lanes' reports.
Report: xmodel/screened-census-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-25KB; 90 minutes.
charged_input=xmodel/moh-program-review-sol56-20260903.md
charged_input=xmodel/whole-tree-review-grok46-20260903.md
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/mohprog-drivers-20260903/candidate_eval.py
charged_input=box/mohprog-drivers-20260903/tree-independent.py
charged_input=box/branch-orbits-v2-20260903/nested_pack.py
charged_input=xmodel/nested-pack-dp-grok46-20260903.md
charged_input=xmodel/n6-family-review-grok46-20260903.md
charged_input=box/moh_skeleton_full.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45  {{LANE_INPUTS}}/moh-program-review-sol56-20260903.md
9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d  {{LANE_INPUTS}}/whole-tree-review-grok46-20260903.md
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553  {{LANE_INPUTS}}/candidate_eval.py
c2a27632d54576abbca54b9f268a7fa5d2b144497a1e364c93102450a066baf9  {{LANE_INPUTS}}/tree-independent.py
36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067  {{LANE_INPUTS}}/nested_pack.py
53d3464817f5c777d0cb106806d590f62556eb8a8dc18c12fc810eb2476cf065  {{LANE_INPUTS}}/nested-pack-dp-grok46-20260903.md
982c75da179e263e109d0bf6ba0e8b13e591225c80d0111d24ba32b61be67896  {{LANE_INPUTS}}/n6-family-review-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
```
