# HOSTILE GATE + CROSSWALK (promotion gate for Sol's all-degree split-window theorem, plus the mechanical crosswalk that determines the operative residual): the frozen report proves that every realized early principal-minor split (u_s ≥ 2, ρ < v_s/u_s) lies in a finite set given by (2.2) rational window with denominator ≤ u_s, (G) Puiseux–Galois covariance with its conjugated group action, and (L) local-exponent feasibility from the split-face Jacobian ODE — and CORRECTS 17(iiiiii) (your own model's batch-3 result): (L) depends on W = (−μ_s−2)/d_s in general (29 missed leaves on 28 rows). GATE: (1) the denominator bound Q ≤ u_s and the window 1 < ρ < v_s/u_s — derive them from Moh's contact structure (pp.183–194) / Xu §7; is the bound on the denominator of ρ really u_s (or lcm/branch-count)? (2) (G): is the covariance a NECESSARY condition on any realized face (with the group element written), or does it assume a normalization (e.g. a specific Puiseux root chosen)? (3) (L): re-derive the split-face Jacobian ODE coefficient system (§4.1) and the nonnegativity of the cancelled exponent — is the W-dependence correct, and does the W-independent version of 17(iiiiii) over-kill or under-kill on (99,66)? Recompute (99,66) S1–S4, S7, S8 from your own implementation (66 → 54/12; 12 → 2) and the 28 W-sensitive rows; (4) run the frozen tool on 3 random census rows and re-derive their survivor lists by hand. VERDICT per component: CONFIRMED / CONFIRMED-WITH-FIX / REFUTED. CROSSWALK (mechanical, do it regardless): take the 1,420 OPERATIVE rows (C_FULL_TREE_POLYNOMIAL_ODE ∧ XU, box/scopeleaks-20260905/ and box/child-data-20260905/ partitions: 310 rows with u_s ≥ 2), apply the split-window tool (box/split-window-20260905/) to each: how many of the 310 have NO G+L survivor (⇒ descent D2 forced ⇒ they join the u_s ≥ 2 DESCENDED family whose child-top convention is OPEN[CHILD-TOP-AT-US-GE-2]) vs. retain typed ES leaves (list them with (ρ,λ) and total leaf count)? Also for the 174 live u_s=1 rows nothing changes (no split) — confirm. Deliver the corrected operative partition (rows by: u_s=1 live / u_s≥2 descent-forced / u_s≥2 with ES leaves) — this is the exact residual of the all-degree program at n ≤ 200. FALLACY-v2. ≤ 120 min; no ledger edits; no jc2-lean; no ideation-*. Notes to box/split-window-gate-20260905/.
Report: xmodel/split-window-gate-opus5-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 120 min.
charged_input=xmodel/split-window-alldeg-sol56-20260905.md
charged_input=xmodel/g9966-n1-batch3-opus5-20260903.md
charged_input=xmodel/child-data-tests-opus5-20260905.md
charged_input=xmodel/scope-leaks-opus5-20260905.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/split-window-gate-opus5-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4874b3e43f34a5271612d3e93ddaf71ce34bea3bc9d6d35db1a935a661eff0e5  {{LANE_INPUTS}}/split-window-alldeg-sol56-20260905.md
c9f853dc490dba611d8b229aea43d293a7bcbfee151c6c1f16b4655bc676c545  {{LANE_INPUTS}}/g9966-n1-batch3-opus5-20260903.md
219faa47b435222511168ffaa1cc4f0c33be7744209a29626999f464d66c9cff  {{LANE_INPUTS}}/child-data-tests-opus5-20260905.md
c3dd95b11ea3e12ba88e813860ecab703a275f745ce429944c8aeb04a5095eda  {{LANE_INPUTS}}/scope-leaks-opus5-20260905.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
