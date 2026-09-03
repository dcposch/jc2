# Gate + batch: (A) hostile replay of the two full-stratum kills (33,22; 30; 8; k = 1) [parent (132,88)] and (45,30; 42; 11; k = 1) [parent (180,120)] — every partition stratum with symbolic slopes; (B) run the FULL partition strata on the two PRIOR-SLICE rows (15,10; 11; 2; k = 2) [u' = 3] and (21,14; 18; 5; k = 1) [u' = 2], whose earlier kills used unlicensed fixed faces

Context (banked, AUDIT delta 17(rr)): topface-license-sol56 (charged) showed that
no source theorem licenses the descended top face; the general face is
H = y^{V₂'}·Π_i (y − a_i x)^{e_i}, Σe_i = u' = d₂' − V₂', f_top = H^{d'}, g_top =
H^{e'}, with the slopes a_i symbolic (distinct, nonzero) and Prop 4.6's cap on
distinct roots bounding the partitions; the sound computation keeps the
slopes as ring variables and saturates by their pairwise differences and
products (Ω) together with the Jacobian constant. Its driver (box/topface-
20260903/, charged) generated 30 strata over the nine open two-point rows and
killed every stratum of (33,22; 30; 8; 1) ([3], [2,1]) and of (45,30; 42; 11; 1)
([4], [3,1], [2,2]). It also flagged (OPEN[PRIOR-SLICE]) that the compiler's kill
of (15,10; 11; 2; 2) (delta 17(bb)) and the batch's kill of (21,14; 18; 5; 1)
(delta 17(pp)) used fixed faces (y²(y − x)³ resp. y⁵(y² − x²)) without licence.
Task: (A) replay the two full-stratum kills from the charged driver
(Singular; report per stratum unknowns/equations/verdict) AND re-derive one
stratum of each independently (your own generator from the descended data,
as in your k16-t2 gate: charged t2_independent_order_system.py generalised;
keep symbolic slopes); audit the Ω saturation: is every stratum saturated by
the correct non-degeneracy ideal (slopes distinct, nonzero; leading
coefficients), and does the union of strata cover every partition allowed by
deg q ≤ … (Prop 4.6 cap) — state the cap used and check it against the print
(pp.168–172 as page images); (B) for (15,10; 11; 2; k = 2): u' = 3, enumerate the
partitions [3], [2,1], [1,1,1] with symbolic slopes and saturate each (also
compare with Moh's printed bracket "15 or 13" on p.208 for V₂ = 2 — which
cases does Moh split on?); for (21,14; 18; 5; k = 1): u' = 2, strata [2] and
[1,1]; report verdicts; if every stratum dies, the prior kills are restored
as licensed; if a stratum survives, print the point and check J directly
(REPRESENTATIVE); (C) verdict per row CONFIRMED / GAP / REFUTED with scope;
type every claim; FALLACY-v2 applies. ≤ 90 min; Singular up to 2 cores; no
ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-t3-uniform, moh9966-branches, twopoint-kills-gate-fable5). Drivers to
box/strata-gate-20260903/.
Report: xmodel/strata-gate-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 90 minutes.
charged_input=xmodel/topface-license-sol56-20260903.md
charged_input=xmodel/twopoint-batch-gpt55-20260903.md
charged_input=box/twopoint-batch-20260903/twopoint_order_batch.py
charged_input=box/k16t2-gate-20260903/t2_independent_order_system.py
charged_input=xmodel/appendix2-compiler-grok46-20260903.md
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/topface-20260903/topface_cases.py
charged_input=box/topface-20260903/case_counts.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/strata-gate-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae  {{LANE_INPUTS}}/topface-license-sol56-20260903.md
52ac2f50b9c14b258b706cef4e931ca9afa1057dc542f64003c8df43a14c8a1b  {{LANE_INPUTS}}/twopoint-batch-gpt55-20260903.md
db14cb1ef39da6277ec4edcd9988a17d38d8bc0062edca244af1155b820282eb  {{LANE_INPUTS}}/twopoint_order_batch.py
7ee7e29eca86dadecf4cffdc996539fc875851ce5803ad7ddaf68b888624f823  {{LANE_INPUTS}}/t2_independent_order_system.py
dea9f5be619b9507b5ca30db51ddd88401b293e7ab7a0e75c8ae8083a5c79c27  {{LANE_INPUTS}}/appendix2-compiler-grok46-20260903.md
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
369bafb1341f96708f6886e79c93fb9bdad8e70abb1ae4c69ddd1dd6a9c62082  {{LANE_INPUTS}}/topface_cases.py
b8ce67b93c105b62966d9003583da2c7dec302125cf79862f16f5b54513d3861  {{LANE_INPUTS}}/case_counts.json
```
