# STRUCTURAL proof lane (the (H1) flagship theorem route, from 17(iiiii) Card B): the one uniform residue on the u_s ≥ 2 principal-minor-split stratum is R = disc(p_red), p_red = squarefree part of Xu Cor 7.5's shared leader p(π), the split partition = its multiplicity vector; R equals the declared localisation in 3/3 charged branches ((99,66) δ = 2 and δ = 5/2, D = 108 δ = 3, where the kill IS R ∈ I: the [1,1] partition collapses to [2]). GOAL: turn "the chart dies iff R = disc(p_red) is a unit" from a 3/3 observation into a THEOREM — prove that for EVERY admissible split datum (a genuine principal-minor split, u_s ≥ 2, partition ≠ [1,1,…], i.e. p_red having ≥ 2 distinct roots as forced by the split), the necessary joint two-point system contains disc(p_red) (or a unit multiple) and hence is the unit ideal — OR find the exact obstruction

Context (banked): the split forces p(π) = ∏(π − c_i)^{m_i} with the partition (m_i) = the multiplicity vector, and a GENUINE split (Xu Prop 7.3 / 17(rrr) N5) means ≥ 2 distinct roots (disc(p_red) ≠ 0 is the genuineness condition); the ladder law (17(iiiii)) c(p,k) = ±[eA(K−p) − n(k−k₀)] gives the killing Jacobian rows in closed form; the certificate slices (17(lllll)) are 7–10 rows with provenance; the necessity dossier (17(hhhhh)) has the chart bijection and the pivot closed form 9(99 − 3n − 11i). STRATEGY (mathematics, desk CAS to check): (1) state precisely, from Xu §7–8, how the shared leader p(π) enters the joint chart's minor-incidence rows: the two (or u_s) packets are the roots of p, they share the tower leader, and Theorem 1.2 assigns them independent order weights — write the incidence rows as a linear (or low-degree) system in the packet coordinates whose SOLVABILITY is governed by disc(p_red) (a resultant/discriminant of the shared-leader system); (2) prove: genuine split (disc(p_red) ≠ 0, ≥ 2 distinct roots) ⇒ the incidence system + the Jacobian ladder rows are inconsistent (unit ideal). The D = 108 case (17(ddddd): p = (π − j₁²)², [1,1] → [2] collapse; the three residues r71 = −2j₂, r81 = 2j₁², r80 = −c − j₁⁴ + 9j₁j₂²) is the SMALLEST instance — generalise its three-line contradiction to arbitrary (u_s, partition, V, δ); (3) the (99,66) instances (u_s = 3): show the same disc-driven mechanism produces the unit (the ladder rows 6264, 64 as disc/resultant values); (4) if the theorem holds, state MINOR-EMPTY with the precise hypothesis and the disc(p_red)-unit condition, and what remains (is disc(p_red) ≠ 0 ALWAYS implied by "genuine split", making the condition automatic? — then MINOR-EMPTY is unconditional on the split stratum); if it fails, the exact obstruction and the datum where the mechanism breaks; (5) controls: the (16,12) u_s = 1 case (disc empty, must NOT be covered — 17(iiiii)); a tame two-point automorphism (u_s = 1) survives; FALLACY-v2 applies (a 3/3 fit is not a proof — the theorem is the general derivation). Desk CAS only (foreground, ≤ 10 min per job); ≤ 180 min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports (k16-hsop-length-allt running).
Report: xmodel/minor-empty-disc-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-40KB; 180 minutes.
charged_input=xmodel/minor-residue-formula-opus5-20260903.md
charged_input=xmodel/two-place-obstruction-core-sol56-20260903.md
charged_input=xmodel/g9966-chart-necessity-opus5-20260903.md
charged_input=xmodel/g108-delta3-kill-gate-gpt55-20260903.md
charged_input=xmodel/g108-minor-classification-opus5-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md
charged_input=box/obscore-20260903/d108_certificate.py
charged_input=box/obscore-20260903/delta2_certificate.py
charged_input=box/obscore-20260903/filtered_obstruction.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/minor-empty-disc-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
b009dee9b3aee4c48ab97a4c0a4f61d41c3430923461b7fce22077fb9eb2547f  {{LANE_INPUTS}}/minor-residue-formula-opus5-20260903.md
3f16d1f776a6bd37525302f4a9c15639db5bee03f3b4bc3cd29063c2fa252a11  {{LANE_INPUTS}}/two-place-obstruction-core-sol56-20260903.md
37beed7ace5aafced312725fcca2e43aa316c19cecc387ef5aafa1c0809bb628  {{LANE_INPUTS}}/g9966-chart-necessity-opus5-20260903.md
7c14a90a47485d8ac7461a2b0019989dc09cc580cd33fb23a67b08afae48fe3b  {{LANE_INPUTS}}/g108-delta3-kill-gate-gpt55-20260903.md
8b97a8972cff0dfccfa9396bae8849dbda4318fb47150645e76d55785d9decd3  {{LANE_INPUTS}}/g108-minor-classification-opus5-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
e271a767abc4d4052ec510a68b06ddc1ca2653c11bdb55d4fa91372b6e9ac2ed  {{LANE_INPUTS}}/d108_certificate.py
916f430726b60b2a87dc89f474ce8412984f545e8cbe703380a14755a31deb77  {{LANE_INPUTS}}/delta2_certificate.py
f386e644efee0785c6f8e1a07ba5a56b39d1b908431f204a7a02c845f6a6311e  {{LANE_INPUTS}}/filtered_obstruction.py
```
