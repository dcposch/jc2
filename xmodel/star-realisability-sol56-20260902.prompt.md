# Computation lane: STAR-REALISABILITY — which surviving Moh skeletons are killed because their bottom polynomial is forced to have a repeated root?

Reviewed inputs (integration #17, 2026-09-02): THEOREM D1-STAR — for a
degree-minimal Keller pair in Moh's gauge, the a_1 = eV_2 roots of g in
the last major disc D_1 separate pairwise at exactly delta_1, so Moh's
polynomial p(pi) at the bottom point sigma_1 (his Prop 4.6 / Def 4.1
operator data at r = 1) has a_1 SIMPLE roots, as a Jacobian consequence;
Prop 4.6 at r = 1 does not by itself force simple roots. The review
(sec.13) raises OPEN[STAR-REALISABILITY]: "Multiplicity partition of
p(pi) at sigma_1 (a partition of eV_2). A forced repeated root would kill
the skeleton. Not implemented." THEOREM D1-PIN: N = sum_B V_2(B) q(B),
q = (1 - delta_1)de/(d+e), sum_B V_2(B) <= u; N must be an integer >= 6
(campaign frontier; N <= 5 closed).
YOUR TASK (exact arithmetic, desk-scale):
(1) From Moh 1983 (refs/, hash; read pp.164-165 Def 4.1/Prop 4.1/4.2,
    pp.170-176 Prop 4.4/4.6, p.179 Def 5.1, pp.190-194 Prop 6.1/Lemma
    6.1 from the page images), state exactly what determines the
    multiplicity partition of p(pi) at sigma_1 in terms of the skeleton
    data (n, m, M_2..M_s, V_2..V_s, u, v, d_j, delta_j) — in particular
    whether Moh's leading-form structure at the bottom (the operator
    D(a,b,p,q), the eta-expansion of Lemma 2.1) forces a repeated root
    for some (M, V) data. If the partition is NOT determined by the
    skeleton alone, say precisely which extra datum enters and bound it.
(2) Implement the test in box/moh_skeleton_N.py's framework (the Skel
    class; census(n, with_V=True) enumerates V-skeletons) and run it on
    every V-assignment surviving the (UNI) integrality filter at the
    MOH-SHARP-2 degrees {105, 108, 112, 117, 120} with N >= 6, and then
    at D <= 120. Report per degree: assignments tested, killed by a
    forced repeated root, surviving; and whether any degree is EMPTIED.
(3) Controls: the automorphisms (y, x + y^k) (s = 1; the bottom star with
    k simple roots) must PASS; the non-Keller two-tower rows of the
    N-ON-THE-TREE report (box/nott-drivers-20260902) need not.
(4) For the smallest surviving assignment at D = 105 print the full
    skeleton, its q, V-packet, N, and the bottom partition.
Discipline: type everything PROVED-HERE/UNREVIEWED or MEASURED; state
the bounded quantity of every OPEN you raise; one core, < 4 GB, < 30
min of compute; do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/star-realisability-sol56-20260902.md
Seal-at-completion; bounded writes; target 15-25KB; 75 minutes.
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=xmodel/ideation-20260902T1608Z-synthesis.md
charged_input=box/moh_skeleton_N.py
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/d1sub-drivers-20260902/runall.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
ad1bf4467319f98a29e50de16915ced5f5c4177f7ffe28657332aba00ad18245  {{LANE_INPUTS}}/ideation-20260902T1608Z-synthesis.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
e2b4d616a6ccbd771f1eb8c1b9e37ffaf50a46e278a529c1e05c5de948fda313  {{LANE_INPUTS}}/runall.py
```
