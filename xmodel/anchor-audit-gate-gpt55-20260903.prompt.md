# Hostile gate (fast): OPEN[DESCENT-ANCHOR] closure by Moh's p.174 normalisation — is Φ_eff sourced, and do the counts reproduce?

Charged claim (descent-anchor-audit-grok46-20260903.md §0–§5; AUDIT delta 17(y)
PROVISIONAL): (a) Def 5.1(3) as printed at p.179 carries the factor
1/(n − M_s − 1); (b) Moh p.174 Definition–Remark drops M_h = n − 1 from the
characteristic sequence (the last effective exponent is M_s) and Lemma 2.1
forces every Jacobian pair to have M_h = n − 1, so a descended child with
M'_{s'} = n' − 1 is the generic termination, not a degeneration (Prop 5.1(1):
coinciding discs, finite radius); (c) Prop 6.3/6.4 hypotheses never mention
the child's anchor, so the 38 (n ≤ 100) / 12 (n = 108) anchor-zero rows are
neither undefined nor killed; (d) Φ_eff := after the Prop 6.3 image, drop
M'_{s'} if it equals n' − 1, set V_{s*+1} = d_{s*+1}, then δ' = (k+1)·Def
5.1(3)(effective tuple); no-op on all five p.207 rows (10/10 rationals
MATCH), and dropping the factor instead breaks (15,10); (e) counts: n ≤ 100
658 → 58, 57 descendable, 38 anchor-zero, 0 undefined after the drop, u_s > 1
residue 1/58 = (99,66); n = 108: 217 → 21 → 20, 19 descendable, 12 anchor-zero,
0 undefined, residue 1/20; s_eff = 2 on 29/57 and 12/19, s_eff = 3 on 14/57.
Task: (1) open Moh pp.173–179, 196–198 as page images (pdftoppm -r 200 on the
charged PDF; name the pages opened) and check (a)–(c) against the print —
in particular whether p.174's drop is a definition that applies to the
DESCENDED (non-Keller, monomial-Jacobian) pair as well, whether Lemma 2.1's
"M_h = n − 1" statement is for J = const only or also for J = cγ^k (state
what the print says; do not fill the gap), and whether setting V_{s*+1} =
d_{s*+1} on the truncated dictionaries is Moh's convention or the lane's
choice; (2) replay measure_anchor.py on the frozen drivers and reproduce
the counts in (e), plus the 10/10 p.207 control and the (15,10) negative
control; (3) verdict per item CONFIRMED / GAP / REFUTED; state whether Φ_eff
can be PROMOTED as the descent radii rule (scope: s' ≤ ?, k ≥ ?) and what
its producer_scope / reviewed_scope are. Desk-scale; no ledger edits; no
jc2-lean; do not read any ideation-20260903T1200Z-* file other than the
charged Opus submission (its H1/§13 only), nor in-progress lane reports.
Drivers to box/anchor-gate-20260903/.
Report: xmodel/anchor-audit-gate-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-14KB; 60 minutes.
charged_input=xmodel/descent-anchor-audit-grok46-20260903.md
charged_input=box/anchor-audit-20260903/measure_anchor.py
charged_input=box/anchor-audit-20260903/measure_anchor.json
charged_input=box/anchor-audit-20260903/anchor_zero_rows.txt
charged_input=xmodel/ideation-20260903T1200Z-opus5.md
charged_input=xmodel/descent-radii-grok46-20260903.md
charged_input=box/descentradii-drivers-20260903/phi_delta.py
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/anchor-audit-gate-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
5c5d0e132196b3110c9027d220244534b5763a7d311bcc8efb7219ac596bfa77  {{LANE_INPUTS}}/descent-anchor-audit-grok46-20260903.md
4a5866d5e655add9ee37c6d684e2e12b017da3d8d5a52040d5b4e89a2ac372f6  {{LANE_INPUTS}}/measure_anchor.py
611c0588c28bf9bcb718386f8c046561ca4fc6c77c5e93743fa15eab6aaa39f7  {{LANE_INPUTS}}/measure_anchor.json
62525b610fc2011ba88730fe4ebbfd9a897243052b29c9e198067a2516a93967  {{LANE_INPUTS}}/anchor_zero_rows.txt
2e4e817267cbfdba97607a41df0433b11f3d4542dbb5418226aa48982830accd  {{LANE_INPUTS}}/ideation-20260903T1200Z-opus5.md
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  {{LANE_INPUTS}}/descent-radii-grok46-20260903.md
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  {{LANE_INPUTS}}/phi_delta.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
