# DECOUPLED LONG-SOLVE LAUNCH (≤ 90 min of YOUR time; the solves run ~20 h unattended). The K=7 β-strata cover chart **b9 q0** (72 vars / 241 rows; chart SHA 15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275 per the frozen r3b report §2) is the LAST chart keeping stratum b9 conditional: four full exact-Q runs hit 180-min walls (rc 124) with no basis; its msolve unit is only a modular signal. TASK: (1) launch YOUR OWN r7i.8xlarge (256 GB) via `sh ops/fleet/fleet.sh launch r7i.8xlarge` + `fleet.sh wait`; regenerate the b9 q0 chart bytes from the frozen r3b/r2 custody (the generator source and ring map recorded there) and verify the chart SHA EXACTLY (stop and report if it differs); (2) start, DETACHED (systemd-run or nohup + setsid), THREE capped jobs with 72,000 s (20 h) walls and RSS watchdogs (≤ 70 GB each): (a) Singular exact-Q slimgb, dp, option(redSB); (b) Singular exact-Q std under the weighted/block order matching the chart's bigrading (from the frozen strata gate); (c) the exact-Q(v) triangular pre-reduction route that certified the other charts (r2 §3, r3b §5), then slimgb on the reduced system — each writing runner.rc, time.txt, caprun.json and fully delimited stdout under /home/ubuntu/k7-b9q0-longsolve/runs/<job>/; (3) write box/k7-b9q0-longsolve-20260906/custody.json on the host (≤ 100 KB): instance id, IP, start times, caps, chart SHA, binary SHAs, exact commands, paths a harvest lane must read, expected end time; DO NOT terminate the worker (the harvest lane will); (4) confirm all three are running, then SEAL immediately. Type the result LAUNCHED[b9 q0 long solve; harvest due ~+20 h] — no mathematical verdict. FALLACY-v2. DISK: host writes ≤ 2 MB; `df -h /` before writing. No ledger edits; no jc2-lean; no ideation-* input.
Report: xmodel/k7-b9q0-longsolve-sol56-20260906.md
Seal (<!-- BODY-END -->); 3-8KB; 90 min.
charged_input=xmodel/k7-cofactors-sol56-r3b-20260906.md
charged_input=box/k7-cofactors-20260906/r3-custody.json
charged_input=xmodel/k7-cofactors-sol56-r2-20260906.md
charged_input=box/k7-cofactors-20260906/r2-custody.json
charged_input=xmodel/k7-strata-gate-sol56-20260905.md
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k7-b9q0-longsolve-sol56-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
372455ba342085b8c85dba305f42b2b75f1b534c2d753ebf21dcd610b368261f  {{LANE_INPUTS}}/k7-cofactors-sol56-r3b-20260906.md
df4096e241ed10a147ee7bbb17f8058d507b248f9e3d3aaddad25171eaa9eaba  {{LANE_INPUTS}}/r3-custody.json
1ffd191ae1ce427ddaa6941c2b80664e0d30e6520cf07ba50e82a65d03135aac  {{LANE_INPUTS}}/k7-cofactors-sol56-r2-20260906.md
913167e2a53e60eb5da58ce122339e3754badc460ae8c90038f40cdcf7ac026f  {{LANE_INPUTS}}/r2-custody.json
78edece02efa7223d9130aa334416339f69c10de6d3cf4c6b7873581b791e1f8  {{LANE_INPUTS}}/k7-strata-gate-sol56-20260905.md
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
