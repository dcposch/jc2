# Design + implementation lane: the MISSING necessary rows of the (99,66) joint chart (AUDIT delta 17(aaaa)) — (a) the outer F, G Theorem-1.2 D₁ (and D₂) order bands on the A, B coefficients at the first point at infinity, and (b) the effective quasi-approximate-root bridge T₂, T₃ ∈ K[f,g] (deg T_i = −μ_i; Moh's T_i^ψ; Xu §7.3) — derive them as explicit coefficient rows, count them, implement them as an add-on to the charged chart driver, validate on Moh's (64,48) control, and report the row counts per band so the complete decider can be assembled

Context (banked): the joint chart (17(ttt)) is a necessary coordinate chart
(17(aaaa) gate) whose displayed 516 major rows use only H, C₂, C₃ and leave the
6,600 outer coordinates untouched; the gate names the missing necessary
content: (a) the outer Theorem-1.2 vanishings on A, B (the D₁ bounds on A₂,
A₃, B₁, B₂ and the h₃-adic D₂ bounds on F_j, G_j — stated in the design's §2.1
but not imposed), and (b) the effective-root bridge — T₂ and T₃ are the
approximate-root-type polynomials in K[f,g] with deg T_i = −μ_i (Moh's T_i^ψ of
pp.150–152; Xu §7.3's T_i(f,g) ∈ K[f,g], T₀ = g, T₁ = f) whose π-root data at the
second point are the ones the minor blocks constrain (the reduced T₃ ODE);
until T₃ is written as an element of K[f,g] (a polynomial in the coefficients
of F and G), the minor rows constrain a free object. Task: (1) SOURCE-READ Moh
pp.150–152 (definition of T_i^ψ via the Tschirnhausen/approximate-root
construction and deg T_i = −μ_i) and pp.164–172 (Theorem 1.2 / Prop 4.4 order
bounds at D₁, D₂), Xu §7.3 (page images; name pages); (2) for the (99,66)
skeleton in the chart's convention (F deg 99 = Moh's g; G deg 66 = Moh's f;
minor line at y = 0), derive: (a) the Theorem-1.2 order bounds for every
coefficient of the outer A, B blocks at D₁ and D₂ as explicit linear
vanishing rows (which monomials of F, G must vanish / have bounded degree) —
count them; (b) T₂ = the approximate root relation (T₂ ∈ K[F,G] of degree
−μ₂ = 55: which K[F,G]-combination? derive from the semigroup/δ-sequence:
T₂ ≡ G^{a} − (F^{b} + …) with the exponents fixed by (n, m, μ₂) and the
Tschirnhausen normalisation) and T₃ (degree −μ₃ = 145) — write them as
explicit polynomials in F, G with unknown coefficients (how many?), and
derive the rows that identify their π-root data at the second point with the
minor blocks' H and R (the (25,14) / p = π(π² − c) leaders): these are the
bridge rows; (3) implement both as an add-on module to the charged chart
driver (box/g9966-20260903/, charged) — do not modify it in place; emit the
new rows for both branches; report counts (rows, new pivots) and run the
Q*-pivot elimination on the union with the existing prefix to report the new
dimensions (expect drops); (4) VALIDATE on the (64,48) → (16,12) control (the
same construction must reproduce the Appendix II kill with the outer bands
and the bridge present — u_s = 1 there, so the bridge is trivial: say so) and
on the automorphism control (must survive); (5) verdict: the complete row
inventory of the joint chart (typed: which rows are PRINTED, DERIVED, or
still OPEN[EFFECTIVE-T2-T3-BRIDGE]), the new dimensions, and the exact next
system for the decider lane. FALLACY-v2 applies. ≤ 150 min; 4 cores; no
ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(g9966-global-band, k16-*, emitter-native). Drivers to box/g9966outer-20260903/.
Report: xmodel/g9966-outer-bridge-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 150 minutes.
charged_input=xmodel/g9966-design-gate-grok46-20260903.md
charged_input=xmodel/g9966-global-design-sol56-20260903.md
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/sibling-coefficients-sol56-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/g9966-20260903/minor_row_count.py
charged_input=box/g9966-20260903/major_h2-results.json
charged_input=box/g9966-20260903/joint_probe.py
charged_input=box/g9966-20260903/minor_row_count.json
charged_input=box/g9966-20260903/major_h2_probe.py
charged_input=box/g9966-20260903/joint_probe-results.json
charged_input=box/g9966-20260903/xu_joint_extension/xu_joint_extension.py
charged_input=box/g9966-20260903/xu_joint_extension/xu_joint_extension.json
charged_input=box/g9966-20260903/first_global_band/first_global_band.py
charged_input=box/g9966-20260903/major_tower_joint/major_tower_structure.py
charged_input=box/g9966-20260903/major_tower_joint/major_tower_structure.json
charged_input=box/g9966-20260903/first_global_band/results.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-outer-bridge-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
0cbeaf0735b92f18e3a7c5050775b99c3739b658584ce0d02965a24db2c1273b  {{LANE_INPUTS}}/g9966-design-gate-grok46-20260903.md
a81ff0263cf379a297b8d1812ebfa26eb95f7e58d91ef4edc62a3a68edf2d782  {{LANE_INPUTS}}/g9966-global-design-sol56-20260903.md
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
a00d258b0b6469a64e433747692c01bb6e113de33b95a430e4917485e782b36a  {{LANE_INPUTS}}/sibling-coefficients-sol56-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
4e88918b8e08f3cb63da746b1155e9fbce5c045d61b4a5fff87970c7869250b7  {{LANE_INPUTS}}/minor_row_count.py
6a4826431f03210cf4b9c13001108ba741a098aca7ddba8e53551a5fa5c7ec44  {{LANE_INPUTS}}/major_h2-results.json
6acd8b467369aa33a07482f341c86a48686db55950666ad70455d344301dc021  {{LANE_INPUTS}}/joint_probe.py
a62385d3432555946199dba6f6189dc74227e351e7aa0da3bc32c5b690837fe0  {{LANE_INPUTS}}/minor_row_count.json
8463c689fd5251219f36e7239ab13f7e3ebd053972809e0f3720295beac07780  {{LANE_INPUTS}}/major_h2_probe.py
ed8cabc25df5dc8250f504df63444591d618380af0cf68f5378dd6ce2e97f587  {{LANE_INPUTS}}/joint_probe-results.json
007d205855af0e6b6c6c361bf71dd57933a5f391ac01edf7ae3eef143638f063  {{LANE_INPUTS}}/xu_joint_extension.py
34d0bcbe8e0dbc98ddbdf796175d7b8443553619cec98a52965c386c0c01eee0  {{LANE_INPUTS}}/xu_joint_extension.json
9c123aaf14c8f52104f7b1ef0f0dac50fe5ae0ed294e6bf9f8a5037c175c68af  {{LANE_INPUTS}}/first_global_band.py
555af27d631772f39e6f60f7b537a952190d21fd6f05ae94bbae84e1add7dea8  {{LANE_INPUTS}}/major_tower_structure.py
77d791b33e5bfd2e2aecaff67faf72acb1c3b2560b1ff86157a22a121956989f  {{LANE_INPUTS}}/major_tower_structure.json
f4a6f39c81e01f185bc0e6aed74e844639d21ffce3d219b6a539ee110553ae66  {{LANE_INPUTS}}/results.json
```
