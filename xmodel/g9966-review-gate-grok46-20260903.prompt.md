# Hostile gate (page images): the three DERIVED-SOURCE facts of the (99,66) source review (AUDIT delta 17(iii)) — (1) Moh's Prop 6.1 proof as an exact order identity ord g(σ) = (n/d_s)(u_sδ − v_s) = 9(3δ − 8) with the ceiling δ < v_s/u_s = 8/3; (2) the exhaustive split-order classification δ ∈ {2, 5/2} with the forced partition [2,1] / multiplicity vector (25,14) at δ = 2 and the Galois-forced [1,1,1], p = π(π² − c) at δ = 5/2; (3) the tree-blind identity of Theorem 3.4 + 4.7(i) at (99,66) (difference 30) and the exact Im = 6 / 7 vs IM = 16

Charged: g9966-source-review-opus5-20260903.md (Opus) §1–§5, §7 (N1–N15). These
facts now steer the (99,66) program (the joint decider at δ = 5/2 and the
branch-B point). Task: (1) open Moh pp.190–196 (Prop 6.1 and its proof, the
p.190 dichotomy major/minor with V_r = u_s, Prop 6.2) and p.202 (the table), and
Xu pp.10–13 (§7.3, Prop 7.3, Cor 7.5, §8) as page images (pdftoppm -r 200; name
pages); re-derive (1): does Prop 6.1's proof, read with the MINOR multiplicity
V_r = u_s = 3 (not the major V₃ = 8), give exactly ord g(σ) = 9(3δ − 8)? check
against Moh's printed t⁻¹⁸ at δ = 2 and Xu's five displayed orders (f: 6(−8+3δ),
g: 9(−8+3δ), T₂: 5(−8+3δ), (T₃)_f: 22(−8+3δ), T₃: 13(−8+3δ) − 1 + δ) — all must
follow; state the general formula's hypotheses; (2) re-derive the
classification: the ceiling δ < 8/3, Xu Prop 7.3 (δ > 1), den(δ) ≤ u_s = 3 (Xu
asserts — is a proof exhibited? if not, mark SOURCE-ASSERTED and say whether
the classification survives without it), and the face-ODE degree/resonance
budget that excludes each other candidate order (list them: 4/3, 5/3, 2, 7/3,
8/3 excluded by ceiling, 5/2, and the integers) — reproduce the exclusion of
each with sympy; at δ = 2 confirm that only [2,1] with (25,14) survives (the
review says "forced" — by what? the ODE q = p¹³(π − c) argument? replay); at
δ = 5/2 confirm the μ₂ action π ↦ −π (where does it come from? the
ramification of the δ = 5/2 place, t^{1/2}) forces [1,1,1] and p = π(π² − c)
and excludes the ODE-admissible [2,1] vectors; (3) replay the tree-blind
identity: for the two admissible trees compute Σ_{P_m}|D_σ|(δ_σ − 1) and the
Theorem 3.4 principal term and confirm the difference is 30 for both; compute
IM and exact Im (6 and 7) and confirm Cor 5.3 passes; (4) verdict per fact:
CONFIRMED / GAP / REFUTED, with scope; note any consequence for the running
decider (e.g. if the (25,14) vector or the p = π(π² − c) form is not forced, the
decider's ansatz is a slice). Type every claim; FALLACY-v2 applies. ≤ 75 min;
no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane
reports (g9966-delta52-joint, g9966-global-design, g9966-hurwitz, k16-*,
bigrows, r3-preprocess). Drivers to box/g9966revgate-20260903/.
Report: xmodel/g9966-review-gate-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-16KB; 75 minutes.
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/minor-dichotomy-sol56-20260903.md
charged_input=xmodel/xu-delta52-lift-gpt55-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/g9966rev-20260903/g9966rev_driver.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-review-gate-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
184a689f3cd63405d922b8118632c7e17f96f471a0bc71f9a50cd161b8a87ad1  {{LANE_INPUTS}}/minor-dichotomy-sol56-20260903.md
1e3aafcae25d811f033a8deeff8daaee022735f9f09a9d4bd20499a56a44c899  {{LANE_INPUTS}}/xu-delta52-lift-gpt55-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
37a7b0e806dfb9f51f36af3d4854ac477b21b684ee81d0d7888f2f91c41c733e  {{LANE_INPUTS}}/g9966rev_driver.py
```
