# Software lane (fast): NESTED-PACK — the exact parent-indexed orbit-packing DP for s > 3, replacing the flat relaxation; plus the two binding repairs to knapsack.py

Reviewed (AUDIT delta 17(j); charged report + review): for a bottom-major
disc of one tower |O| = ∏_{j=2}^{s−1} ω_j (ω_j = A_j on a nonzero (10)-factor,
1 on the zero (11)-factor); each orbit type satisfies (8)–(13) on its own; at
s = 3 the packing Σ|O_k|V₂^{(k)} ≤ u at the unique parent D₂ (with at most one
zero-centred child) is EXACT; at s > 3 the flat budget is a RELAXATION: the
real constraint is nested — at each level j = s−1, …, 2 the children of a
parent disc pack into that parent's p(π) of degree Q_j = V_{j+1}d_j/d_{j+1},
with at most ONE zero-centred (π) child per parent and free nonzero orbits
(each consuming A_j·V_j of the degree). OPEN[NESTED-PACK]: bounded by a tuple
of length s − 2 ≤ 3 on D ≤ 120. The charged driver
box/branch-orbits-v2-20260903/knapsack.py implements the flat UNB/Z01 runs;
the review's binding repairs: (R1) remove the stale hard-coded
/tmp/jc2-lane.GqI4QH import path (import the enumerator by explicit --inputs
or relative to the repo); (R2) the printed "STRICT s=3" totals are the
global Z01 totals (611/493) — print the 274-group s = 3 subtotal (173/138)
explicitly.
YOUR TASK:
(1) Write box/branch-orbits-v2-20260903/nested_pack.py: for each (1)–(13)
    group at 48 ≤ D ≤ 120, enumerate its V-assignments (each is one tower
    with its own A_j, (10)/(11) status per level, δ₁, q, V₂), and build the
    tree of parents level by level from the unique D_{s−1}: at level j a
    parent of degree Q_j is filled by children that are (a) zero-centred
    (at most one per parent; ω_j = 1) or (b) nonzero orbits (ω_j = A_j;
    several allowed, of possibly different lower data); each child that is
    itself a parent at level j − 1 carries its own Q_{j−1} determined by its
    V_j. Bottom discs contribute V₂·q each with the orbit multiplicity.
    Exact DP over Fractions; state caps; count the orbit-admissible N-sets
    (N ≥ 6 and [6,16]) per group. Fail-closed controls: at s = 3 the result
    must equal the charged Z01 numbers (173/138 of 274; the D = 105 trio
    N = {9}; D = 88 → {18}; D = 117 4 → 3); Moh's six rows give
    {9},{},{10},{9},{8},{16}; the flat UNB survivors must be a superset of
    the nested survivors (relaxation) — assert it.
(2) Report per degree (grp, s = 3 / s > 3 split, UNB alive, NESTED alive at
    N ≥ 6 and [6,16]), degrees emptied, and the special degrees
    {105, 108, 112, 117, 120} with their exact survivor lists in [6,16]
    (m, M, V_s, packet structure, N).
(3) Apply R1 and R2 to knapsack.py (keep the old file's hash noted; write
    the repaired file beside it as knapsack_v2.py — do not silently overwrite
    a charged artifact) and rerun the charged controls (336/0).
Typed block; bounded quantity + cheapest test of every OPEN. Desk-scale
(< 10 min one core, < 4 GB); no ledger edits; no jc2-lean; do not read
ideation-20260903T1015Z-* files or other running lanes' reports.
Report: xmodel/nested-pack-dp-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 60 minutes.
charged_input=xmodel/branch-orbits-v2-grok46-20260903.md
charged_input=xmodel/branch-orbits-v2-review-gpt55-20260903.md
charged_input=box/branch-orbits-v2-20260903/knapsack.py
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  {{LANE_INPUTS}}/branch-orbits-v2-grok46-20260903.md
c61bb15528b25587578ac10101cb18267e83150fa6ea541e250f606e648d5418  {{LANE_INPUTS}}/branch-orbits-v2-review-gpt55-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  {{LANE_INPUTS}}/knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
```
