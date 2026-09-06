# BOUNDED FOLLOW-UP (your own OPEN 4 from the exact-contact report, charged; ≤ 90 min): the packet calculus's sibling-tower closure (sibling_tower*.py in box/exact-contact-20260906/) killed six family-B rows modulo a depth ≤ 2 cap and left four rows — R039, R040, R048, R063 — that "survive only through a genuinely new sibling tower" (T3 residue). TASK: (1) run the same closure on those four rows with the depth cap LIFTED as far as the printed bounds allow (state the bound that limits depth: Def 5.1(2)'s window, the p.174 effective truncation, the gcd lattice) — enumerate every candidate sibling tower exhaustively in W, orbit shape and partition; (2) for each candidate apply the integrality test I_M ∈ Z, Xu Thm 5.1 (I_M ≥ I_m with exact packets), and Lemmas A/B; (3) VERDICT per row: DEAD (no admissible sibling tower survives — typed with the exact depth searched and why deeper is impossible) / ALIVE via a named tower (list it, with I_M, I_m) / depth-capped (say the cap); (4) also state, for the six rows already killed mod depth ≤ 2, whether the same lifted search confirms them unconditionally. FALLACY-v2 (a cap is a hypothesis; a configuration is not a pair; keep the f/g orientation explicit). DISK DISCIPLINE: report + JSON ≤ 1 MB; no fleet. ≤ 100 min; no ledger edits; no jc2-lean; no ideation-* input. Drivers to box/t3-residue-20260906/.
Report: xmodel/t3-residue-closure-opus5-20260906.md
Seal (<!-- BODY-END -->); 6-16KB; 100 min.
charged_input=xmodel/exact-contact-r009-r050-opus5-20260906.md
charged_input=xmodel/residual65-structure-fable5-20260905.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/t3-residue-closure-opus5-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4bb981374dbfbc202ecdbf944c0791f325abaa1974cde694cffe2a6e3e56c105  {{LANE_INPUTS}}/exact-contact-r009-r050-opus5-20260906.md
7d3ffbba4791a64c7c7d9e28546de67190d96edd3a47b431c116fec35394c927  {{LANE_INPUTS}}/residual65-structure-fable5-20260905.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
