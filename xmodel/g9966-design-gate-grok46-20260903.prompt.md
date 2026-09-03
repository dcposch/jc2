# Hostile gate: the complete joint two-point chart for (99,66) (AUDIT delta 17(ttt), Sol) — is the 7,161-coefficient chart a NECESSARY superset of the locus of degree-(99,66) Keller pairs with Moh's skeleton (M = (−66,77,97), V = (8,8)) and the principal-minor split (δ = 2 [2,1] or δ = 5/2 [1,1,1])? Audit the label reversal, the major tower rows (516 → 120), the minor incidence blocks, the direct Jacobian prefix, and the two controls, before more compute is spent on it

Charged: g9966-global-design-sol56-20260903.md with its drivers (box/g9966-
20260903/). Task: (1) §1.1 "the essential label reversal": state exactly which of
f, g is monic of which degree at which point at infinity in Moh's gauge vs the
chart's convention; confirm the tower data (M, V, d, δ = (4/9, 1/3, −1)) are
attached to the right polynomial and that the second point's leading form
y − a₁x with the principal-minor multiplicity (u_s·m/d_s = 18 for which
polynomial?) is consistent with Xu §7.3 and Moh p.190 (page images; name
pages); (2) §2.1 the major tower as finite coefficient rows: re-derive the
row counts (516 → 120 for the simultaneous h₃-D₂ / h₂-D₂ faces and the first
h₂-D₁ vanishing band below e²⁹⁶) from the Theorem-1.2 order bounds and the
approximate-root structure (h₃ of y-degree 11 inside h₂ of y-degree 33
inside f of degree 99) — is every row a NECESSARY condition (no gauge choice
that could exclude a pair)? are the fixed tops licensed (u_s = 1 at the first
point? — no: u₃ = 3 here! check what "fixed top" means at the first point for
this row and whether the delta 17(rr) partition-strata issue arises); (3)
§2.3 the two minor incidence blocks: verify the δ = 2 [2,1] common-h₃ leader
and the δ = 5/2 leader + reduced T₃ ODE (through s²⁸) against the promoted
classification (17(nnn), (rrr), (sss)); (4) §2.4/§3.4 the direct Jacobian
prefix: are the 15 independent pivots correct (replay); does the Jacobian
identity's coefficient extraction use the right total-degree structure
(deg 162 = 99 + 66 − 3 at the top? J(F,G) has degree ≤ 99 + 66 − 2 = 163 — check
the [x¹³⁵y²⁷] band arithmetic); (5) controls: replay the (64,48) → (16,12) kill
in the chart and the automorphism's survival; (6) verdict: CONFIRMED (the
chart is a necessary superset and the band computation is the right
decider) / GAP (which rows or bands are slices, or which necessary rows are
missing — e.g. the D₁ bottom (12)/(13) conditions at the first point, the
minor-disc radius bound) / REFUTED; state what the running next-band lane's
verdicts would and would not mean. Type every claim; FALLACY-v2 applies. ≤ 90
min; 2 cores; no ledger edits; no jc2-lean; no ideation-* files; no in-progress
lane reports (g9966-global-band, g9966-branchB-joint, k16-*, bridge-chart-
gate, emitter-native). Drivers to box/g9966dgate-20260903/.
Report: xmodel/g9966-design-gate-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 90 minutes.
charged_input=xmodel/g9966-global-design-sol56-20260903.md
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=xmodel/g9966-review-gate-grok46-20260903.md
charged_input=xmodel/n5-gate-gpt55-20260903.md
charged_input=xmodel/topface-license-sol56-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/g9966-20260903/joint_probe.py
charged_input=box/g9966-20260903/minor_row_count.json
charged_input=box/g9966-20260903/major_h2_probe.py
charged_input=box/g9966-20260903/joint_probe-results.json
charged_input=box/g9966-20260903/minor_row_count.py
charged_input=box/g9966-20260903/major_h2-results.json
charged_input=box/g9966-20260903/xu_joint_extension/xu_joint_extension.py
charged_input=box/g9966-20260903/xu_joint_extension/xu_joint_extension.json
charged_input=box/g9966-20260903/major_tower_joint/major_tower_structure.py
charged_input=box/g9966-20260903/major_tower_joint/major_tower_structure.json
charged_input=box/g9966-20260903/first_global_band/results.json
charged_input=box/g9966-20260903/first_global_band/first_global_band.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-design-gate-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
a81ff0263cf379a297b8d1812ebfa26eb95f7e58d91ef4edc62a3a68edf2d782  {{LANE_INPUTS}}/g9966-global-design-sol56-20260903.md
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
dc2355a81dd472993c9af0fb0f03eb5b6f3c087c3a2ed00120615b76bcf91be8  {{LANE_INPUTS}}/g9966-review-gate-grok46-20260903.md
666a1c900d7e3b14b772fec58839b8abff6f71e21ffe5852734fd80f6f983a0c  {{LANE_INPUTS}}/n5-gate-gpt55-20260903.md
53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae  {{LANE_INPUTS}}/topface-license-sol56-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
6acd8b467369aa33a07482f341c86a48686db55950666ad70455d344301dc021  {{LANE_INPUTS}}/joint_probe.py
a62385d3432555946199dba6f6189dc74227e351e7aa0da3bc32c5b690837fe0  {{LANE_INPUTS}}/minor_row_count.json
8463c689fd5251219f36e7239ab13f7e3ebd053972809e0f3720295beac07780  {{LANE_INPUTS}}/major_h2_probe.py
ed8cabc25df5dc8250f504df63444591d618380af0cf68f5378dd6ce2e97f587  {{LANE_INPUTS}}/joint_probe-results.json
4e88918b8e08f3cb63da746b1155e9fbce5c045d61b4a5fff87970c7869250b7  {{LANE_INPUTS}}/minor_row_count.py
6a4826431f03210cf4b9c13001108ba741a098aca7ddba8e53551a5fa5c7ec44  {{LANE_INPUTS}}/major_h2-results.json
007d205855af0e6b6c6c361bf71dd57933a5f391ac01edf7ae3eef143638f063  {{LANE_INPUTS}}/xu_joint_extension.py
34d0bcbe8e0dbc98ddbdf796175d7b8443553619cec98a52965c386c0c01eee0  {{LANE_INPUTS}}/xu_joint_extension.json
555af27d631772f39e6f60f7b537a952190d21fd6f05ae94bbae84e1add7dea8  {{LANE_INPUTS}}/major_tower_structure.py
77d791b33e5bfd2e2aecaff67faf72acb1c3b2560b1ff86157a22a121956989f  {{LANE_INPUTS}}/major_tower_structure.json
f4a6f39c81e01f185bc0e6aed74e844639d21ffce3d219b6a539ee110553ae66  {{LANE_INPUTS}}/results.json
9c123aaf14c8f52104f7b1ef0f0dac50fe5ae0ed294e6bf9f8a5037c175c68af  {{LANE_INPUTS}}/first_global_band.py
```
