# Dossier lane (paper-grade): write the CHART-NECESSITY DOSSIER for the (99,66) joint two-point chart — the one document that turns the promoted engine kills (AUDIT 17(pppp), 17(tttt)) into the theorem "there is no Keller pair of degrees (99,66) whose Moh skeleton is the (99,66) row" — every row family sourced to a statement of Moh 1983 / Xu 2016 / a banked promoted lemma, every convention of the chart shown to be a normalisation (gauge) available without loss of generality, and every localisation (c ≠ 0, J₀ ≠ 0, Q*-pivots) justified on a Keller pair

Context (banked): the engine kills both split branches with explicit
rational certificates (δ = 2: stage-4 Jacobian row 6264; δ = 5/2: stage-8
row 64), confirmed by hostile gates and a clean-room re-implementation; the
split classification {δ = 2 [2,1]; δ = 5/2 [1,1,1]} is complete (Prop 6.1 order
identity, ceiling δ < 8/3, N5 den(δ) ≤ u_s). What is NOT yet written as one
argument is NECESSITY: that a Keller pair (F, G) of degrees (99,66) with
this skeleton satisfies every row of the chart. Task: write the dossier
(mathematics, not code): (0) the skeleton hypothesis, stated exactly (what
"the (99,66) row" means: Moh's data M, d, V, the tower, u₃ = 3; and why a
Keller pair of degrees (99,66) has SOME skeleton in Moh's census — cite the
theorem; state which other (99,66)-degree skeletons exist, if any, and their
banked status); (1) the tower h₃ ⊂ h₂ ⊂ F, G and the Theorem-1.2 order rows:
statement, source, and why the unknown coefficients form a coordinate
chart (no lost solutions: every pair with the skeleton has coordinates in
it, possibly after the gauge of §2); (2) gauges: the two fixed top forms,
the affine normalisations, the torus action — prove each is WLOG (list the
group acting and the orbit representatives); (3) the outer D₂ support
preblock and D₁ boundary bands (Moh Thm 1.2 / Prop 6.2): statement and
source, with the weight cut derived; (4) the minor-incidence block for
each branch (Xu §7–8: face p, q = p^k u, the packets): necessity on a
Keller pair, including the pullback and the truncation orders used; (5)
the pole rows and the Jacobian rows (degree 163 = 99 + 66 − 2 downward):
necessity (the Jacobian is 1, so every coefficient of J − 1 vanishes — state
which coefficients the engine used and why those are well-defined
polynomials in the chart coordinates); (6) the Q*-pivot reductions: each
pivot divides by a rational constant only (verify from the charged engine
logs: list the 66 + N pivots' coefficients); localisations c ≠ 0 and J₀ ≠ 0:
prove each is nonzero on a Keller pair; (7) the split classification's
exhaustiveness as a lemma with proof; (8) the theorem statement and the
dependency graph (banked deltas, lane reports, sourced statements); (9)
what the referee would attack: list every step you could not fully source
and type it (GAP with the exact missing statement). Desk-scale CAS only
(< 10 min per job, foreground). ≤ 180 min; no ledger edits; no jc2-lean; no
ideation-* files; no in-progress lane reports.
Report: xmodel/g9966-chart-necessity-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 25-45KB; 180 minutes.
charged_input=xmodel/g9966-global-design-sol56-20260903.md
charged_input=xmodel/g9966-global-band-sol56-20260903.md
charged_input=xmodel/g9966-delta52-stage8-sol56-20260903.md
charged_input=xmodel/g9966-outer-bridge-grok46-20260903.md
charged_input=xmodel/g9966-delta52-kill-gate-gpt55-20260903.md
charged_input=xmodel/g9966-branchB-kill-gate-gpt55-20260903.md
charged_input=xmodel/g9966-independent-engine-opus5-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-chart-necessity-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
a81ff0263cf379a297b8d1812ebfa26eb95f7e58d91ef4edc62a3a68edf2d782  {{LANE_INPUTS}}/g9966-global-design-sol56-20260903.md
0c8dc291e306f15806e6c14099ab69feda9d1532abcbc22e79e55b02df427701  {{LANE_INPUTS}}/g9966-global-band-sol56-20260903.md
679671e7be4aef40128b133b26ab75c083f95a7283d9ab97aebcccea5bc21b01  {{LANE_INPUTS}}/g9966-delta52-stage8-sol56-20260903.md
7facb109db6eb21b73970c2b6a0d4339bc51c7b73f3ce16782950550508e2674  {{LANE_INPUTS}}/g9966-outer-bridge-grok46-20260903.md
56d46a51ba7307026744cbe7c7a312e9bcc2650caab9a5b4f7bd670f74fa95ec  {{LANE_INPUTS}}/g9966-delta52-kill-gate-gpt55-20260903.md
84b2a04cc41231eeaa3711b03b9a3d0e23630581bdf63a230799fdeafeb4d468  {{LANE_INPUTS}}/g9966-branchB-kill-gate-gpt55-20260903.md
be5b5758a789415f6ed46661c257ec14add697134c6cc85a63e977866c874d18  {{LANE_INPUTS}}/g9966-independent-engine-opus5-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
