# FOUNDATION lane (OPEN[CENSUS-COVERAGE-ALL-DEGREE] — the statement the whole all-degree program rests on, and the one no lane has attacked): the First-Separation lemma (PROMOTED, 17(aaaaaaa)) puts every minimal plane Keller counterexample into Moh's p.194 setup with M_s = n−2 and the two-point top form (FS). The campaign's census (box/moh_skeleton_full.py) enumerates skeletons (n,m; M; d; V; s; u_s, v_s) by Moh's pp.200–201 list "(1)–(13)" — but the promotion gate showed that list is Moh's BOUNDED-SEARCH normalization list: item (1) contains n ≤ 100 and item (6) contains s ≤ 5, and other items may encode further n ≤ 100-specific pruning. So the campaign has never proved that its cap-free enumerator (Kmin, n ≤ 200, "full=True") COVERS every Moh-admissible datum at all degrees. TASK: (1) go through items (1)–(13) on printed pp.200–201 ONE BY ONE (PDF page = printed − 139; render the pages): for each, classify it as (A) a THEOREM valid for all n (cite the proposition it follows from — Moh's Theorem p.200 (1)–(7), Prop 5.x/6.x, Xu), (B) a consequence of n ≤ 100 or s ≤ 5 only, or (C) a normalization requiring a group element (state it); (2) compare with what box/moh_skeleton_full.py actually IMPOSES (read the code: every filter, every inequality, every gcd/parity condition, Kmin) and produce the exact table "code condition ↔ printed item ↔ class A/B/C"; any code condition of class B that is applied without the n ≤ 100 hypothesis is a COVERAGE LEAK — enumerate the leak (what admissible data at n ≤ 200 would be wrongly excluded; if you can, count them by relaxing the condition in a copy of the enumerator); any class-A condition NOT in the code is missed pruning (harmless for coverage); (3) also check the C_FULL_TREE_POLYNOMIAL_ODE ∧ XU "operative" screen (the 1,420-row filter): is each of its conditions a proved necessary condition on a realized datum (cite), and is the Xu screen applied only where Xu's hypotheses hold (Cor 7.5's strict cutoff)?; (4) VERDICT: COVERAGE THEOREM (the cap-free census with the operative screen contains every Moh-admissible all-degree minimal-counterexample datum at n ≤ 200, with the printed justification of each condition) / LEAK (exact conditions, exact count of wrongly excluded rows at n ≤ 200, and the repaired enumerator) / UNDECIDABLE-FROM-PRINT for named items. FALLACY-v2 (a printed search normalization is not a theorem; cite the line). ≤ 150 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/census-coverage-20260905/.
Report: xmodel/census-coverage-astra-20260905.md
Seal (<!-- BODY-END -->); 15-25KB; 150 min.
charged_input=xmodel/first-separation-gate-opus5-20260905.md
charged_input=xmodel/first-separation-lemma-sol56-20260905.md
charged_input=xmodel/scope-leaks-opus5-20260905.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/census-coverage-astra-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
e2e97236489ff54f39d4555a65fe4a4f0ae915832f6de0a6fb0cc6816d1f9832  {{LANE_INPUTS}}/first-separation-gate-opus5-20260905.md
43fe44eb8bebb46c23b612d586f266c73e4d632a22835a6324c4497e129aba1c  {{LANE_INPUTS}}/first-separation-lemma-sol56-20260905.md
c3dd95b11ea3e12ba88e813860ecab703a275f745ce429944c8aeb04a5095eda  {{LANE_INPUTS}}/scope-leaks-opus5-20260905.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
