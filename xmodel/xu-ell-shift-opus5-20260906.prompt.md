# DERIVATION lane (the ℓ-shifted Xu calculus — needed by the exact-contact gate and by the R063 child kill): the exact-contact report (frozen, PROVISIONAL) and its replay (frozen) apply Xu's intersection calculus to LICENSED CHILDREN of Prop 6.3 descent, where the Jacobian is J = c·x^ℓ (ℓ = v_s − u_s − 1; ℓ = 1 on R009/R050/R063), not a constant; the report states that Xu Lemma 4.1's right side becomes −t^{−ℓ−2} and "the whole calculus shifts 1 → 1+ℓ" (final major: δ = λ^f + λ^g + 1 + ℓ; minor: δ > 1 + ℓ; Prop 4.6(3)*: λ = (−1−ℓ+δ)/(n−M_r), the p.171 Remark verbatim) and raises OPEN 2: the child's I_m has NO printed inequality — "derive the ℓ-analogue of (4.3),(4.4) verbatim from Lemma 4.1 with J = x^ℓ". TASK: (1) derive, from Xu's printed proofs (Lemma 4.1 chain rule, Lemma 4.4(i),(ii), Thm 4.7, Thm 5.1, Cor 5.3 — cite lines) with J = c·x^ℓ in place of a constant, the exact ℓ-analogues of (4.3), (4.4), the major/minor dichotomy thresholds, I_M and I_m — every step written; state precisely which statements survive verbatim, which shift by ℓ, and which need a NEW argument (and supply it or type it OPEN); (2) apply the result to R063's licensed child (own data via box/lib/descend_own.py and the replay's child_xu.py): recompute I'_M and I'_m with the correct ℓ-shift — is I'_M = 71/4 (non-integer ⇒ R063 DEAD as a necessary configuration) or does the shift restore integrality?; same for R009 and R050's children; (3) VERDICT: the ℓ-shifted calculus is PROVED (with the exact statements) / partly proved (name the gap); R063: DEAD-by-child-integrality (typed, printed lines) / survives / undecided. FALLACY-v2 (a shifted formula without its printed derivation is not a theorem; the child datum is a necessary configuration, not a pair). DISK DISCIPLINE: report + JSON ≤ 1 MB; no fleet. ≤ 150 min; no ledger edits; no jc2-lean; no ideation-* input. Notes to box/xu-ell-shift-20260906/.
Report: xmodel/xu-ell-shift-opus5-20260906.md
Seal (<!-- BODY-END -->); 10-20KB; 150 min.
charged_input=xmodel/exact-contact-r009-r050-opus5-20260906.md
charged_input=xmodel/im-descent-replay-grok46-20260906.md
charged_input=box/lib/descend_own.py
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/xu-ell-shift-opus5-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4bb981374dbfbc202ecdbf944c0791f325abaa1974cde694cffe2a6e3e56c105  {{LANE_INPUTS}}/exact-contact-r009-r050-opus5-20260906.md
81dda41bebc3c88782eb94a3238ccf72ee982f18bf39e2edf0946104f3c8b473  {{LANE_INPUTS}}/im-descent-replay-grok46-20260906.md
3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2  {{LANE_INPUTS}}/descend_own.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
