# HOSTILE GATE (promotion gate for the five K=7 β-strata closures; different model from the producer): the frozen strata-solve report (Opus) claims K=7 strata b = 9, 10, 11, 12, 13 are exact-Q units of I_light on BOTH cover charts (ten charts): msolve -g 2 reduced Gröbner bases over Q equal to [1] from Singular-emitted, denominator-cleared integral generators (box/k4ray-strata-solve-20260905/), and that since I_light drops only MASTER-cutoff ROWS (never unknowns) a unit of I_light kills the theorem-cut ideal, so the K=7 residual band shrinks to 6 ≤ b ≤ 8. GATE: (1) CHART: rebuild each of the ten charts from the charged pinned_chart.py + the beta-strata report's construction (LEVEL-4 top band with two scalars above b_min, lower β-block the exact box) and confirm byte-for-byte or generator-for-generator agreement with the frozen emitted generators; confirm NO unknown was dropped by any floor and that I_light ⊂ I_full is a ROW subset (list the dropped rows and the printed licence for the MASTER cutoff they came from); (2) CERTIFICATE: re-run the exact-Q computation on the identical integral generators with an INDEPENDENT engine (Singular std over Q with `option(redSB)`, or guided_gb exact-Q, or msolve over Q from a fresh emission) — for every chart the result must be [1]; if an engine times out (≤ 40 min each) record it and rely on a second independent msolve build only with an explicit statement; also produce, for at least three of the ten, an explicit cofactor identity Σ a_i g_i = 1 (Singular `lift`) checked by direct multiplication; (3) NEGATIVE CONTROL: the b = 8 stratum (open) must NOT return [1] under the same pipeline within the same budget (or record its actual status); (4) the LOGIC: does "all strata b = 9..13 dead" + the banked b = b_min = 5 unit + the 3b ≤ 2K floor + the composite arm (deg β = 0) leave exactly b ∈ {6,7,8} open for the K=7 row — recompute b_min/b_max for K=7 from the degree-tower report; (5) VERDICT: CONFIRMED (⇒ promote the five closures) / CONFIRMED-WITH-FIX / REFUTED per chart. FALLACY-v2. A fleet worker is allowed (`bash ops/fleet/fleet.sh launch 1 r7i.8xlarge`; TERMINATE before sealing). ≤ 150 min; no ledger edits; no jc2-lean; no ideation-*. Notes to box/k7-strata-gate-20260905/.
Report: xmodel/k7-strata-gate-sol56-20260905.md
Seal (<!-- BODY-END -->); 10-18KB; 150 min.
charged_input=xmodel/k4ray-strata-solve-opus5-20260905.md
charged_input=xmodel/k4ray-beta-strata-grok46-20260905.md
charged_input=xmodel/k4ray-degree-tower-opus5-20260903.md
charged_input=box/k4raypinned-20260903/pinned_chart.py
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k7-strata-gate-sol56-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
2af3e012dd4157669308f3855a22582967e2fffdc25cad3bf825b1050f25be4c  {{LANE_INPUTS}}/k4ray-strata-solve-opus5-20260905.md
689e3ed80af53c683a38c47ba666ca49151dbea2d6b451787fd74cb310d508ae  {{LANE_INPUTS}}/k4ray-beta-strata-grok46-20260905.md
2befb3cac8e51305e65ab0e48de485a7098ba104a3620d8b174927791a896a2a  {{LANE_INPUTS}}/k4ray-degree-tower-opus5-20260903.md
eed2cdf5cc5b85e3358013416bca7f6f6bd272138533ff0c065a86afb4c47e43  {{LANE_INPUTS}}/pinned_chart.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
