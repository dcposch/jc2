# BOUNDED DATA AUDIT (≤ 50 min): the frozen actual-stabilizer census replay found the sound-convention operative set is 90 rows = the 65 roster rows + 25 "finite-pole" rows (E0022 E0053 E0097 E0120 E0127 E0301 E0344 E0354 E0355 E0383 E0415 E0452 E0467 E0468 E0475 E0483 E0489 E0608 E0724 E0771 E0773 E0939 E0946 E1263 E1279; JSON actual_rows). Those 25 are NOT in the 66-row roster, so the own-data reduction (frozen roster + descend_own) removed them. The campaign has just learned (frozen six-rows report) that an instrument can be premature: an "empty closure" or fractional child sum is only valid if EVERY above-average packet is carried by Prop 5.3 to the prescribed level. TASK: for each of the 25 rows, (1) state the EXACT clause of descend_own / own_v_routes / the roster pipeline that removed it (cite code lines and the roster/JSON field), and the printed line it rests on; (2) classify the removal: (a) own-V′ contradiction among printed necessary conditions at the child (which clause), (b) an empty own-route set, (c) a depth/closure termination — and for (b)/(c) check whether the Prop 5.3 carry rule was applied to every above-average packet (replay with the rule if not); (3) report any of the 25 whose removal does NOT survive that check (they would rejoin the residual — type it as OPEN, not as a promotion); (4) VERDICT: DATA — for each row: removal clause; STANDS / OPEN[PREMATURE-CLOSURE] / OPEN[other]. FALLACY-v2 (a convention change is not a kill; a row needs its printed line). DISK: report + JSON ≤ 1 MB; no fleet; ≤ 55 min; no ledger edits; no jc2-lean; no ideation-* input. Driver to box/finite-pole-25-20260906/.
Report: xmodel/finite-pole-25-audit-grok46-20260906.md
Seal (<!-- BODY-END -->); 4-10KB; 55 min.
charged_input=xmodel/actual-stabilizer-census-grok46-20260906.md
charged_input=box/actual-stabilizer-census-20260906/actual-stab-census.json
charged_input=xmodel/six-rows-child-sum-sol56-20260906.md
charged_input=xmodel/residual66-roster-sol56-20260905.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=box/lib/descend_own.py
charged_input=box/lib/own_v_routes.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/finite-pole-25-audit-grok46-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
dae79e6e4e2d71b9b688f39fd7f9529ee6ed0bbc3b474bfece1b26dbfa9c464a  {{LANE_INPUTS}}/actual-stabilizer-census-grok46-20260906.md
247b100b308d548a81d7e4677f625b744c87b71cada865f981bc9bc6776f169b  {{LANE_INPUTS}}/actual-stab-census.json
20e01ccd41b0df8f58439698538023010a74c018fa2eab9aaef1d8af1f89fe09  {{LANE_INPUTS}}/six-rows-child-sum-sol56-20260906.md
54ed1d3e5d965e270b8e07137e356196435ea67e1c317f7e5bcf13ae8c378260  {{LANE_INPUTS}}/residual66-roster-sol56-20260905.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2  {{LANE_INPUTS}}/descend_own.py
f07dd9b0e38118132ed2ec2e5e7e972f98ba8f223213062fed356a30188b3bf3  {{LANE_INPUTS}}/own_v_routes.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
