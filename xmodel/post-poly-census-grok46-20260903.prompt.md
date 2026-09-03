# Census lane (bounded, desk): the operative screen is now C_FULL_TREE_POLYNOMIAL_ODE — re-base every live target on it and emit the new target list with Φ_eff descent data

Context (banked today): LEMMA[ZERO-FACTOR-CENTRE] (AUDIT delta 17(hh)) makes the
ungated Prop 5.6 zero-chain kill a theorem and the recentring rule (17(gg)) is
promoted, so the operative screen is C_FULL_TREE_POLYNOMIAL_ODE as implemented in
the charged full_tree_partition.py (POLY rule fires only at integral δ = 0;
ungated Prop 5.6). Known: n ≤ 100: 20 rows / 7 classes (14 excess, all s ≥ 4,
u_s = 1); 48 ≤ D ≤ 200: 1,420 rows / 686 groups / 459 UNI. The descent radii
rule is Φ_eff (17(dd)): after the Prop 6.3 image (n' = n/d_s, m' = m/d_s,
M_i' = M_i/d_s, V_i' = V_i, k = V_s − u_s − 1), drop a terminal M'_{s'} = n' − 1
and set V_{s*+1} = d_{s*+1}, then δ' = (k+1)·Def 5.1(3) (closed form of 17(ff) at
s' = 2). Task, all MEASURED with the frozen drivers (copy to
box/postpoly-20260903/; do not modify in place): (1) the K = 16 ray (n = 48t+16,
m = 32t+16, M = (n−12, n−2), V = (3,3)) for t = 1..8 and the (d,e)-fixed ray of
rigid-congruence §4.1 (extending (108,72; M = (84,104,106); V = (8,8,3)) on
t = 6 + 9k, k = 0..5; use construct_ray.py) under the POLY screen — survive or
die, with the killing node if any; (2) the 19 rigid expdim-0 assignments
(dessin-tower-dim §6.4 / rigid-congruence §2) under POLY, and for the
survivors the Φ_eff descent state (n', m', M', V', k, s_eff, δ'); (3) the
D = 108 survivors: of the 20 C_FULL_TREE_ODE rows, which survive POLY; for each
survivor u_s, and the Φ_eff descent state; (4) the full 48 ≤ D ≤ 200 POLY+ODE
residue tabulated by (u_s = 1 vs > 1) × s_eff after Φ_eff × (two-point δ₂' = −1
vs not), with counts of rows/groups, and the list of the two-point s_eff = 2
u_s = 1 groups (the Appendix II compiler's direct clients) — these are the new
target list; also which degrees D are now empty; (5) the 14-row residue at
n ≤ 100 with its Φ_eff descent states (expected all u_s = 1; s_eff after drop;
which are two-point); (6) sanity: Moh's six survive every column; report
runtime. No theorem claims; type everything MEASURED; FALLACY-v2 applies
(screen survival ≠ existence). ≤ 45 min one core; no ledger edits; no
jc2-lean; no ideation-* files; no in-progress lane reports.
Report: xmodel/post-poly-census-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-16KB; 45 minutes.
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/moh_skeleton_full.py
charged_input=box/branch-orbits-v2-20260903/nested_pack.py
charged_input=box/rigid-congruence-20260903/construct_ray.py
charged_input=box/rigid-congruence-20260903/ray-B-verified.json
charged_input=box/anchor-audit-20260903/measure_anchor.py
charged_input=box/descentradii-drivers-20260903/phi_delta.py
charged_input=xmodel/rigid-congruence-grok46-20260903.md
charged_input=xmodel/dessin-tower-dim-grok46-20260903.md
charged_input=xmodel/descent-anchor-audit-grok46-20260903.md
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/post-poly-census-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067  {{LANE_INPUTS}}/nested_pack.py
360a7baae7d148edd34ad2769f95d996af0a7e31ec4165bbc9295fa4ab7a42b3  {{LANE_INPUTS}}/construct_ray.py
17b03f70564ae7c621c55e4a80f607d821f2d2ede305109f78cf23223b4fce7e  {{LANE_INPUTS}}/ray-B-verified.json
4a5866d5e655add9ee37c6d684e2e12b017da3d8d5a52040d5b4e89a2ac372f6  {{LANE_INPUTS}}/measure_anchor.py
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  {{LANE_INPUTS}}/phi_delta.py
0a77eb88048fbc50dd4c09391376c6e79d03e410a0e614f8e43c59cd0e40713e  {{LANE_INPUTS}}/rigid-congruence-grok46-20260903.md
693b206806a75a557bfb02683fc7b937d0529a677b4b7476cac3b4c9a151cd0e  {{LANE_INPUTS}}/dessin-tower-dim-grok46-20260903.md
5c5d0e132196b3110c9027d220244534b5763a7d311bcc8efb7219ac596bfa77  {{LANE_INPUTS}}/descent-anchor-audit-grok46-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
