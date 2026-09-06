# CERTIFICATE LANE, round 3 (≤ 240 min wall): the frozen r2 report certified 7/10 K=7 β-strata cover charts over Q (rational cofactor identities or exact-Q reduced basis {1}); THREE charts remain msolve-signal only: **b9 q0, b9 q1, b10 q1** (r2 §6 records the failed exact-Q dp/redSB/slimgb attempts and budgets). TASK: obtain theorem-tier certificates for these three. Use the fleet worker 172.30.0.108 (r7i.8xlarge, 256 GB; owned by the r1/r2 lanes, now free; do NOT launch or terminate instances; scratch on the worker; host writes ≤ 2 MB). For each chart, in parallel where memory allows: (a) Singular exact-Q slimgb/std under at least two orderings (dp; a weighted/block order matching the chart's bigrading from the frozen strata gate) with ≥ 180 min each; (b) box/lib/guided_gb.py (Hilbert-seeded modular + CRT + rational reconstruction) and, if it returns a cofactor vector, CHECK the identity by fresh exact multiplication in the full original ring (the only acceptable form); (c) the exact-Q(v83)-style triangular pre-reduction that made r2's lifts tractable — apply it to these charts first. Accept ONLY: an explicit rational cofactor identity verified by exact multiplication, or a completed exact-Q reduced basis literally {1}. A timeout, modular result, or protocol fragment is not a certificate. VERDICT per chart: CERTIFIED-Q (with the identity's hash and check time) / STILL-SIGNAL-ONLY (with the exact resource wall: time, RSS, degree reached); then the strata status: which of b9, b10 become UNCONDITIONAL. FALLACY-v2. No ledger edits; no jc2-lean; no ideation-* input. Custody JSON to box/k7-cofactors-20260906/r3-custody.json.
Report: xmodel/k7-cofactors-sol56-r3-20260906.md
Seal (<!-- BODY-END -->); 6-14KB; 240 min.
charged_input=xmodel/k7-cofactors-sol56-r2-20260906.md
charged_input=box/k7-cofactors-20260906/r2-custody.json
charged_input=xmodel/k7-strata-gate-sol56-20260905.md
charged_input=xmodel/k8-b11-q1-sol56-20260905.md
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k7-cofactors-sol56-r3-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
1ffd191ae1ce427ddaa6941c2b80664e0d30e6520cf07ba50e82a65d03135aac  {{LANE_INPUTS}}/k7-cofactors-sol56-r2-20260906.md
913167e2a53e60eb5da58ce122339e3754badc460ae8c90038f40cdcf7ac026f  {{LANE_INPUTS}}/r2-custody.json
78edece02efa7223d9130aa334416339f69c10de6d3cf4c6b7873581b791e1f8  {{LANE_INPUTS}}/k7-strata-gate-sol56-20260905.md
c16199138f4e93d3babdde1372e0000fb02ef831e1dd2b9e143d486bb0a6b6ac  {{LANE_INPUTS}}/k8-b11-q1-sol56-20260905.md
95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826  {{LANE_INPUTS}}/guided_gb.py
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
