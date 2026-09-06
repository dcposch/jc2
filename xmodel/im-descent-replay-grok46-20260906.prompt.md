# BOUNDED REPLAY (≤ 45 min): the exact-contact report (frozen, PROVISIONAL, under gate) built an exact packet calculus computing I_M = deg_x Res_y(f_ξ, g) for necessary tower configurations and raised OPEN 3: "I'_M = I_M on both rows: is I(f_ξ, g) preserved by the Prop 6.3 descent? run the same code on all 46 complete rows, ≤ 30 min, then a proof or a counterexample." TASK: (1) using the lane's own drivers in box/exact-contact-20260906/ (read them; do not rewrite the calculus), compute I_M for the parent configuration(s) and I'_M for the licensed child configuration(s) (own data via box/lib/descend_own.py) on all 46 complete u_s = 1 rows of the roster; where a row has several admissible configurations, tabulate all; (2) report: rows with I'_M = I_M on every configuration / rows with a difference (list the values) / rows where the child quantity is undetermined; (3) also record for each row whether the parent's I_M is an integer (the report's integrality test) and whether it satisfies I_M ≥ I_m — the counts must match the report's 1,080-configuration table where applicable; (4) VERDICT: preservation HOLDS on all defined rows (evidence for a lemma; state the candidate statement) / FAILS on named rows (a counterexample to preservation, which would itself be a descent-sensitive test). FALLACY-v2 (a replay is evidence; type counts). DISK DISCIPLINE: report + JSON ≤ 1 MB. No fleet. ≤ 50 min; no ledger edits; no jc2-lean; no ideation-* input. Drivers to box/im-descent-20260906/.
Report: xmodel/im-descent-replay-grok46-20260906.md
Seal (<!-- BODY-END -->); 4-10KB; 50 min.
charged_input=xmodel/exact-contact-r009-r050-opus5-20260906.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=box/lib/descend_own.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/im-descent-replay-grok46-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4bb981374dbfbc202ecdbf944c0791f325abaa1974cde694cffe2a6e3e56c105  {{LANE_INPUTS}}/exact-contact-r009-r050-opus5-20260906.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2  {{LANE_INPUTS}}/descend_own.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
