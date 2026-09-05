# INSTRUMENT lane (rebuild the campaign's DESCENT with the child's OWN characteristic data; your own round-2 gate (frozen) found that descend() copies the parent's V-labels into the child, and that at (180,120) M=(−120,132,150,178) V=(2,4,5) the child's own top count is V'₃ = 1 (a 15+15 split from inverting the top root expansions), not the copied 4 — which refuted the (C-TOP) 936-row kill and made the U-NEG kills conditional on OPEN[CHILD-LEVEL2-IDENTIFICATION]). TASK: (1) specify, from the print, what the child's own Def 5.1 data ARE for a licensed Prop 6.3 descendant: M'_i (confirmed = labels), d'_i (confirmed), and V'_i := the normalized count of roots of the descended g' in the child's own disc D'_{i−1} (Def 5.1(1) p.179) — give the recipe to compute V'_i from the SOURCE row's necessary data (the forced characteristic jet + inversion of the top root expansions, as in your gate §4–5), and state precisely which V'_i are DETERMINED by the parent's necessary data and which depend on unrealized coefficients (if V'_i is not determined, the child datum is a FINITE SET of possibilities — enumerate it); (2) IMPLEMENT descend_own() in box/lib/ (Python, exact rationals; unit-tested against your gate's two worked rows and Moh's own p.207 descents of the five u_s=1 rows — those must reproduce Moh's printed child data exactly, and (99,66) must reproduce M'=(−66,77,97)-type labels wherever Moh prints them); (3) RE-DESCEND all 1,420 operative rows (box/moh_skeleton_full.py enumerator; frozen partitions in box/child-data-20260905/ and box/operative-sweep-20260905/hard-rows.jsonl for the row list) and report: how many rows have own-V' ≠ copied-V' (per level), the honest U-NEG count (V'₂ > K' under the child's own V'₂ — and whether V'₂ is even determined), the honest (C-TOP) count (V'_{s'} ≤ d'_{s'} under own data, where licensed), and the corrected partition — with every count typed as DETERMINED / SET-VALUED; (4) state what the copy error does to the receiver charts (the s'=3 compiler's V-dependent D_i inventories are DECORATIVE by 17(fffffff) — the proved G_i depends only on (n',M_s',ℓ) — so which downstream artifacts actually consume V'?). FALLACY-v2 (a label is not data; a row is necessary data, not a pair; type every count). ≤ 150 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/child-own-v-20260905/.
Report: xmodel/child-own-v-astra-20260905.md
Seal (<!-- BODY-END -->); 15-25KB; 150 min.
charged_input=xmodel/ctop-gate-astra-r2-20260905.md
charged_input=xmodel/child-data-tests-opus5-20260905.md
charged_input=xmodel/source-support-closeout-opus5-20260905.md
charged_input=box/appendix2-k16-20260903/shape.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/child-own-v-astra-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
576f3a043a94f84c6433ade1c1901d425a9f5bab493c3e1763758215196a5d46  {{LANE_INPUTS}}/ctop-gate-astra-r2-20260905.md
219faa47b435222511168ffaa1cc4f0c33be7744209a29626999f464d66c9cff  {{LANE_INPUTS}}/child-data-tests-opus5-20260905.md
a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c  {{LANE_INPUTS}}/source-support-closeout-opus5-20260905.md
d8750d4e512645366e9e0c53153484eb5daa9c785434c1cc59658986d0ab138c  {{LANE_INPUTS}}/shape.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
