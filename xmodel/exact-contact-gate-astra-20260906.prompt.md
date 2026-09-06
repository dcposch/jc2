# HOSTILE GATE (a new printed test, two new lemmas, six claimed row kills; different model from the producer): the frozen exact-contact report (Opus) builds an exact packet calculus for necessary towers from Moh Prop 4.6(2),(3), Def 5.1(4) and Xu (Def 4.3/4.6, Lemmas 4.1/4.4, Thm 5.1) and claims: (a) NEW TEST — I_M = deg_x Res_y(f_ξ, g) must be an INTEGER (Xu §2 + Thm 5.1), which kills 924 of the 1,080 tower configurations of the 66 rows that Cor 5.3 retains; (b) Lemma A (primitivity of the reduced pattern) and Lemma B (cross-tower consistency: d_D | M for every ancestor); (c) R009 (192,128) and R050 (196,56) are pinned to UNIQUE configurations with I_M = I_m = 8 exactly (alive, margin 0); (d) the six two-major-tower family-B rows R025–R028, R057, R058 are DEAD modulo a depth ≤ 2 cap on the sibling-tower closure with Lemmas A, B — residual 65 → 59; (e) R001 dies only WITH Lemma B; (f) exact Xu is ℓ-sensitive (the p.171 Remark shifts 1 → 1+ℓ), hence not descent-invariant. GATE: (1) is I_M literally deg_x of a resultant for a realized pair (Xu §2 — cite the line), hence an integer — and is the calculus's I_M the SAME quantity (same normalization, same f/g orientation — the report swaps to Xu's convention) so that non-integrality is a genuine contradiction and not a normalization artifact? re-derive I_M on Xu's four worked cases §6.1–6.2 and on R009/R050 yourself; (2) Lemmas A and B: prove or refute them from the print (Lemma B's divisibility d_D | M for every ancestor — from p.150's lattice? state the exact claim and check it on 20 random census rows); (3) the six kills: recompute the sibling-tower closure for R025–R028, R057, R058 and state precisely what the "depth ≤ 2 cap" excludes — can it be lifted (is depth > 2 impossible for these rows by a printed bound, or merely unexplored)? if lifted, are the six DEAD unconditionally?; (4) the pruning count 924/1,080: reproduce mechanically; (5) VERDICT per item: CONFIRMED / CONFIRMED-WITH-FIX / REFUTED; overall: is the residual 59 (and R009/R050 pinned) promotable? FALLACY-v2 (a non-integer from a wrong normalization is not a kill; a cap is a hypothesis). DISK DISCIPLINE: ~5 GB free — report + JSON ≤ 2 MB; scratch on a worker if any. ≤ 150 min; no ledger edits; no jc2-lean; no ideation-* input. Notes to box/exact-contact-gate-20260906/.
Report: xmodel/exact-contact-gate-astra-20260906.md
Seal (<!-- BODY-END -->); 12-25KB; 150 min.
charged_input=xmodel/exact-contact-r009-r050-opus5-20260906.md
charged_input=xmodel/residual65-structure-fable5-20260905.md
charged_input=xmodel/census-coverage-gate-opus5-20260905.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/exact-contact-gate-astra-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4bb981374dbfbc202ecdbf944c0791f325abaa1974cde694cffe2a6e3e56c105  {{LANE_INPUTS}}/exact-contact-r009-r050-opus5-20260906.md
7d3ffbba4791a64c7c7d9e28546de67190d96edd3a47b431c116fec35394c927  {{LANE_INPUTS}}/residual65-structure-fable5-20260905.md
502abb3b2c2cffd255e114bc6ccdd89a76571b72ac47c44867b1e142a01d5e6f  {{LANE_INPUTS}}/census-coverage-gate-opus5-20260905.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
