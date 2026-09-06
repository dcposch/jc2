# CERTIFICATE LANE, round 3 relaunch (≤ 240 min wall). The r3 attempt was blocked: its mandated worker 172.30.0.108 had been terminated (04:17Z) before CAS work; nothing was run. WORKER AUTHORIZATION: launch YOUR OWN worker with `sh ops/fleet/fleet.sh launch r7i.8xlarge` (it Owner-tags the instance with your lane tag; run `fleet.sh wait` which installs msolve 0.10.1); do NOT reuse unowned instances; at the end run `sh ops/fleet/fleet.sh term <id>` on YOUR instance only. Scratch on the worker; host writes ≤ 2 MB; `df -h /` before writing.
GOAL: theorem-tier certificates over Q for the three K=7 β-strata cover charts still msolve-signal only: **b9 q0, b9 q1, b10 q1** (frozen r2 report §6 records the failed exact-Q attempts: b9 q0 241 rows / b9 q1 124-row guide core / b10 q1 48 rows, each stopped ~16–22 min at 1.0–1.5 GB RSS with rc=1 — i.e. they were CUT OFF by the lane closeout, not by memory). Methods per chart, in parallel where memory allows, ≥ 180 min each: (a) Singular exact-Q slimgb and std under two orderings (dp; a weighted/block order matching the chart bigrading from the frozen strata gate), option(redSB), fully delimited output; (b) the exact-Q(v83)-style triangular pre-reduction that made r2's lifts tractable (r2 §3), then lift; (c) msolve exact over Q where feasible (-P 2 rational parametrization is not needed — you need the unit: use msolve modular runs ONLY as guides and then produce the rational cofactor identity by lifting the modular cofactors via CRT + rational reconstruction with your OWN driver — note the charged guided_gb.py does NOT emit cofactor vectors, it reconstructs scalar invariants only — and CHECK the identity by fresh exact multiplication in the full original ring). Accept ONLY: an explicit rational cofactor identity verified by exact multiplication, or a completed exact-Q reduced basis literally {1}. VERDICT per chart: CERTIFIED-Q (identity hash, check time) / STILL-SIGNAL-ONLY (exact resource wall); strata status: which of b9, b10 become UNCONDITIONAL. FALLACY-v2. No ledger edits; no jc2-lean; no ideation-* input. Custody JSON to box/k7-cofactors-20260906/r3-custody.json.
Report: xmodel/k7-cofactors-sol56-r3b-20260906.md
Seal (<!-- BODY-END -->); 6-14KB; 240 min.
charged_input=xmodel/k7-cofactors-sol56-r2-20260906.md
charged_input=box/k7-cofactors-20260906/r2-custody.json
charged_input=xmodel/k7-strata-gate-sol56-20260905.md
charged_input=xmodel/k8-b11-q1-sol56-20260905.md
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k7-cofactors-sol56-r3b-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
1ffd191ae1ce427ddaa6941c2b80664e0d30e6520cf07ba50e82a65d03135aac  {{LANE_INPUTS}}/k7-cofactors-sol56-r2-20260906.md
913167e2a53e60eb5da58ce122339e3754badc460ae8c90038f40cdcf7ac026f  {{LANE_INPUTS}}/r2-custody.json
78edece02efa7223d9130aa334416339f69c10de6d3cf4c6b7873581b791e1f8  {{LANE_INPUTS}}/k7-strata-gate-sol56-20260905.md
c16199138f4e93d3babdde1372e0000fb02ef831e1dd2b9e143d486bb0a6b6ac  {{LANE_INPUTS}}/k8-b11-q1-sol56-20260905.md
95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826  {{LANE_INPUTS}}/guided_gb.py
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
