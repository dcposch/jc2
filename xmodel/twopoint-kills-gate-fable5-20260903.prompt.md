# Hostile gate (fast): the three NEW two-point kills of the D ≤ 200 batch — (21,14; 15; 6; k = 4), (24,16; 18; 7; k = 4), (27,18; 21; 8; k = 4) — replay, chart audit, and the δ₁' = 0 question

Charged (twopoint-batch-gpt55-20260903.md; AUDIT delta 17(pp)): the generic
two-point order-chart generator (box/twopoint-batch-20260903/
twopoint_order_batch.py) returns reduced basis [1] over three primes and Q on
the descended rows (21,14; 15; 6; k = 4) [parent (147,98)], (24,16; 18; 7;
k = 4) [parent (168,112), drop 1], (27,18; 21; 8; k = 4) [parent (189,126),
drop 1] with 12/13/14 unknowns, u' = 1 fixed top face y^{V₂'}(y − x), and —
notably — δ₁' = 0 on all three (the closed form gives (k+1)((e'+d')u' − R)/
(R((e'+d')V₂' − 1)) = 0 since (e'+d')u' = R = 5). Task: (1) mechanical
replay of the three Singular runs from results.json/summary.tsv and the
driver (`which Singular`); (2) audit: (a) is δ₁' = 0 legitimate for a
descended monomial-Jacobian pair — Moh's Def 5.1(3) requires δ_{s−1} > δ_s
= −1 and Prop 5.5's proof (p.187) uses 0 < δ₁ < 1 with A > 1; with δ₁' = 0 the
Theorem-1.2 coefficient bound B = V₂'δ₁' + u'δ₂' = −1 and A₁ = 1 — does the
A/B chart then have a licensed finite form, or does δ₁' = 0 mean the
descended tower degenerates (the D₁ disc is integral; p.190 recentring
applies) so that the chart is a different object; decide from the print
(pp.179, 187–190, 196–198 as page images; name pages) whether the kill is a
theorem about the descended datum or an artefact of an inapplicable chart;
(b) re-derive the chart for (21,14; 15; 6; k = 4) yourself from the descended
data (e' = 3, d' = 2, d₂' = 7, u' = 1, R = 5) and saturate independently
(Singular); (c) check that k = 4 with u' = 1 gives J = cγ⁴ and that the parent
rows really have u_s = 1 with V_s − u_s − 1 = 4 (replay from moh_skeleton_full
+ full_tree_partition on (147,98), (168,112), (189,126)); (d) the two
drop = 1 rows use the p.174 effective tuple — confirm the drop is applied
correctly (Φ_eff, delta 17(dd)); (3) verdict per row CONFIRMED / GAP /
REFUTED with the precise theorem statement and scope; type every claim;
FALLACY-v2 applies. ≤ 60 min; no ledger edits; no jc2-lean; no ideation-*
files; no in-progress lane reports. Drivers to box/twopoint-gate-20260903/.
Report: xmodel/twopoint-kills-gate-fable5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-14KB; 60 minutes.
charged_input=xmodel/twopoint-batch-gpt55-20260903.md
charged_input=box/twopoint-batch-20260903/twopoint_order_batch.py
charged_input=box/twopoint-batch-20260903/results.json
charged_input=box/twopoint-batch-20260903/summary.tsv
charged_input=xmodel/k16-t2-gate-gpt55-20260903.md
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=xmodel/descent-anchor-audit-grok46-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/twopoint-kills-gate-fable5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
52ac2f50b9c14b258b706cef4e931ca9afa1057dc542f64003c8df43a14c8a1b  {{LANE_INPUTS}}/twopoint-batch-gpt55-20260903.md
db14cb1ef39da6277ec4edcd9988a17d38d8bc0062edca244af1155b820282eb  {{LANE_INPUTS}}/twopoint_order_batch.py
f42e463a190f4c2fbdc2bade7e33edb6554018c5831e07844f4276f181b458ae  {{LANE_INPUTS}}/results.json
3eca97dd36f2eb4b41d8473d67566d3db8359aee4a286a3081f1d9bce1fd8d4a  {{LANE_INPUTS}}/summary.tsv
692fd869d8a11b3a984d1fe8c4ccb4b42de7326567c130b8babae1571ca6e863  {{LANE_INPUTS}}/k16-t2-gate-gpt55-20260903.md
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
5c5d0e132196b3110c9027d220244534b5763a7d311bcc8efb7219ac596bfa77  {{LANE_INPUTS}}/descent-anchor-audit-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
