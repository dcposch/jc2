# CHART-REDUCTION lane (implement CQ-ELIM from the sealed Opus ideation submission, charged): PROVED-HERE identity: if Q = Φ(F, G) with Φ = v³ − u² + av² + buv + cu + dv + e₀ (the Moh Prop 3.1 family, m₁ = m/gcd(n,m) = 2) and J(F, G) = 1, then F = (bG + c − J(Q, G))/2 (E1) and the Keller condition is EQUIVALENT to the single second-order identity J(J(Q, G), G) = −2 (E2). So on every row with m₁ = 2 (44 of the 66 roster rows, incl. (99,66) where 66/33 = 2) the necessary two-point chart can be rewritten with F ELIMINATED: unknowns = the coefficients of G (degree m) and of the characteristic polynomial Q (degree D₂ = 55 for (99,66) — smaller than F's 99), plus the five Φ-constants; the Keller row (E2) is ONE identity; the two-point structure (the split face, the D2/D1 discs, the source-support envelope) is imposed on G and Q. TASK: (1) verify (E1)/(E2) symbolically yourself (generic F, G; check both directions and the m₁ = 2 hypothesis; state what happens for m₁ ≥ 3 — the (m₁−1)-valued elimination); (2) BUILD the eliminated chart for (99,66): the necessary conditions on (G, Q) — the two points at infinity (top forms of G and Q from P₀ = y³(y−x)⁸: G_top = P₀⁶, Q_top = the attained-degree-55 form), the split-face data of the δ=2 [2,1] branch (and δ=5/2 if time permits) expressed on G and Q, the source-support envelope for G's and Q's coefficients (the theorem's G_i bounds transported: Q is a polynomial in (F, G), so its support bound follows), the attainment localizer Zλ − 1 on Q's y⁵⁵ coefficient, and the Keller identity (E2) as coefficient rows — count unknowns and generators and compare with the F-based chart (median Q-block/F-block raw ratio 0.369 per the submission); (3) DECIDE, exact Q, local Singular with the bigraded weight order (abort if RSS > 12 GiB; ≤ 150 min per branch): UNIT (⇒ the branch is DEAD on the eliminated necessary chart — PROVED-HERE for gate; controls: the cone-vertex pair must be excluded by the attainment localizer alone; replay with the leading-target check) / PROPER (an existential survivor of the eliminated chart — report loudly, typed) / compute-bound (weight reached). (4) If the (99,66) chart is decided, apply the same to D=108 δ=3 (m₁ = 72/36 = 2 ✓). FALLACY-v2 (an identity for Keller pairs imposed on a necessary chart is necessary; the eliminated chart must contain every realization — argue it). DISK DISCIPLINE: the host has ~3 GB free — write only the report and JSON ≤ 1 MB; no artifact trees, no CAS dumps; check `df -h /` before any write > 10 MB. ≤ 220 min; no ledger edits; no jc2-lean; no other ideation-* input. Drivers to box/cq-elim-20260906/.
Report: xmodel/cq-elim-opus5-20260906.md
Seal (<!-- BODY-END -->); 12-25KB; 220 min.
charged_input=xmodel/ideation-20260906T0000Z-opus5.md
charged_input=xmodel/char-degree-instrument-astra-r2-20260905.md
charged_input=xmodel/g9966-corrected-engine-astra-20260905.md
charged_input=xmodel/source-support-closeout-opus5-20260905.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/cq-elim-opus5-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
a7ee66808eb8688a568d9da98ec5840e9bb55fe0c76af21e6ac9852fb5cad89f  {{LANE_INPUTS}}/ideation-20260906T0000Z-opus5.md
d9b95ce9c4588104c9f306d987f91957988611b80d2025a05f14c40568e33b45  {{LANE_INPUTS}}/char-degree-instrument-astra-r2-20260905.md
085bc31ee45d799cf5e44811d9d832eae7d75fac932c49b5a77526c609757218  {{LANE_INPUTS}}/g9966-corrected-engine-astra-20260905.md
a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c  {{LANE_INPUTS}}/source-support-closeout-opus5-20260905.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
