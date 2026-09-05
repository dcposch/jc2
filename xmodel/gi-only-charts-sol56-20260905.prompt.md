# CHART lane (the SMALLEST proved chart for the Moh ≤100 residual): the closeout report (frozen) makes the source-support theorem citable with (H1)–(H3) and states that the PROVED chart is the envelope G_i = {0 ≤ a < K, 0 ≤ b ≤ ⌊d(iK−a)⌋} ALONE (in the φ = (x, y+η) coordinate, with β₁ = 0 and the α_e/β_q constants gauged) — the raw D1 inventory D_i in the source-complete union S_i = D_i ∪ G_i is DECORATIVE and G_i is smaller than D_i on five of six classes. Every solve so far ran on S_i (77–487 parameters) and alloc-failed. TASK: (1) for each of the 12 fibres (box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes/, its support-completion.json and the compiler's coeff_inventory_source_complete), EMIT the G_i-ONLY chart: h = y^K + Σ_{G₁} h_ba x^b y^a, α_i, β_i on G_i, β₁ = 0, the ring Q[y, x, params, c] with y-first block order via builder_fix (unknowns in the polynomial ring), extract the coefficient ideal of J(P,Q) − c·x^ℓ plus Tc − 1; COUNT unknowns and generators per fibre and per class-union (G_i is class-uniform, so ONE chart per class suffices for the kill — state it); (2) VERIFY the emitter against the theorem: the G_i-only chart must be the image of the S_i chart under "set every D_i∖G_i coordinate to 0" (specialization map) and the frozen verify_source_complete.py logic must confirm G_i ⊆ S_i blockwise; (3) SOLVE, smallest class first, exact-Q (guided_gb / Singular std with the control battery; msolve modular as a screen only) with a 600 s watchdog per run on fleet workers (launch ≤ 4 c7i.8xlarge / r7i.8xlarge via `bash ops/fleet/fleet.sh launch`; dispatch.sh; TERMINATE them before sealing; never touch other workers); (4) VERDICT per class: DEAD (exact-Q UNIT on the G_i chart, full custody — a valid (T)-kill by the theorem) / basis found (dimension + sample point, loudly) / compute-bound (unknowns, equations, wall, RSS) — and the honest comparison of chart sizes S_i vs G_i. FALLACY-v2 (a chart smaller than G_i in any block is NOT a kill; a modular unit is a screen). ≤ 180 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/gi-only-20260905/.
Report: xmodel/gi-only-charts-sol56-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 180 min.
charged_input=xmodel/source-support-closeout-opus5-20260905.md
charged_input=xmodel/moh-hsupport-gate-astra-20260905.md
charged_input=box/moh14-charts-20260905/sprime3_compiler.py
charged_input=box/moh14-charts-20260905/builder_fix.py
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/gi-only-charts-sol56-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c  {{LANE_INPUTS}}/source-support-closeout-opus5-20260905.md
4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354  {{LANE_INPUTS}}/moh-hsupport-gate-astra-20260905.md
7e6cfeedcee999a0163df9a23fd03fea695ca55a5de64e2e85b883a2fd4e1833  {{LANE_INPUTS}}/sprime3_compiler.py
d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b  {{LANE_INPUTS}}/builder_fix.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
