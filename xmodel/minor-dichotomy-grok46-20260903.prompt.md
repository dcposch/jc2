# Source lane (page images + desk): OPEN[MINOR-DICHOTOMY] — what Moh does when u_s = d_s − V_s > 1 (p.209's two minor-disc alternatives), applied to the two live u_s > 1 clients (99,66; V = (8,8); d_s = 11; u_s = 3) and (108,72; M = (−72,81,106); V = (7,7); d_s = 9; u_s = 2), and what it means for the 177 u_s > 1 groups at D ≤ 200

Context (banked): under the operative screen C_FULL_TREE_POLYNOMIAL_ODE the
residue at 48 ≤ D ≤ 200 is 1,420 rows / 686 groups, of which u_s > 1 is 310
rows / 177 groups — untouched by every screen and by the descent (Prop 6.3
needs δ*_{s−1} ≥ v_s/u_s, supplied automatically by Prop 6.4 only when
u_s = 1). Moh's own table has one u_s > 1 row, (99,66), which he handles on
p.209 by a case split on the minor discs ("MINOR-DICHOTOMY"); the campaign
has never source-read that split. T-ladder-sol56 §7 item 5 names the
cheapest test: for each client compute the actual minor radius and compare
with v_s/u_s; if the bound fails, enumerate Moh's two minor-disc branches
rather than applying Prop 6.4. Task: (1) open Moh pp.196–199 (Props 6.3,
6.4 and the u_s > 1 remark), pp.207–209 (the (99,66) treatment) and any page
the (99,66) case cites, as images (pdftoppm -r 200; name the pages; quote
the decisive sentences); state EXACTLY what Moh does for (99,66): which
alternatives, which is excluded by which argument (arithmetic? coefficient?
minor-disc count?), and whether the argument is specific to (99,66) or is a
template for u_s > 1; (2) for (99,66) and the D = 108 u_s = 2 row, compute
the tower data (d, V, u_s, v_s, the minor-disc bound v_s/u_s, δ*_{s−1} as far
as it is determined by Def 5.1 / Prop 4.4 — say what is and is not
determined by the skeleton), and decide whether Prop 6.3's hypothesis can
hold, fails, or is undetermined; if undetermined, enumerate Moh's branches
for the D = 108 row as he does for (99,66) and type each branch's outcome
(KILLED by which source step / OPEN with the datum needed); (3) state the
u_s > 1 template as a typed procedure (inputs from the skeleton; outputs:
descend-with-modified-hypothesis / branch A / branch B / OPEN) and estimate
from the charged post-poly census which fraction of the 177 groups it
decides at the skeleton level (run it on the D ≤ 120 u_s > 1 groups: list
them from full_tree_partition + moh_skeleton_full with the POLY screen);
(4) verdict + bounded quantity + cheapest test per OPEN; type every claim;
FALLACY-v2 applies. ≤ 75 min; no ledger edits; no jc2-lean; no ideation-*
files; no in-progress lane reports. Drivers to box/minordich-20260903/.
Report: xmodel/minor-dichotomy-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 75 minutes.
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=xmodel/t-ladder-sol56-20260903.md
charged_input=xmodel/post-poly-census-grok46-20260903.md
charged_input=box/postpoly-20260903/measure_postpoly.py
charged_input=xmodel/rigid-congruence-grok46-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/minor-dichotomy-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
5159eadea60527ef3580a9a9353d803721e2280418f865bb5ef7145f82c65726  {{LANE_INPUTS}}/t-ladder-sol56-20260903.md
fcddd0b0a8164f84c8aeb2ebad326fd49687094db7baca7a29f19924dfd2689b  {{LANE_INPUTS}}/post-poly-census-grok46-20260903.md
d90d21768d2082b70fe0691fe57eb806c0cc889fe2b8e5ca158506e2948a798d  {{LANE_INPUTS}}/measure_postpoly.py
0a77eb88048fbc50dd4c09391376c6e79d03e410a0e614f8e43c59cd0e40713e  {{LANE_INPUTS}}/rigid-congruence-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
