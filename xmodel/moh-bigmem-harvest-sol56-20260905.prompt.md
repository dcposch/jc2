# HARVEST lane (round 3 of the big-memory Moh solves; rounds 1–2 on Grok both exited after ~20 min of polling without a report — the SOLVES are fine and still running, detached, on eight workers Grok launched at 13:49Z: r7i.24xlarge 172.30.0.108/.183/.190/.202 and x2idn.16xlarge 172.30.0.121/.125/.45/.55; the round-2 draft report_draft.md and harvest/t1432, t1445 polls are charged/available in box/moh-bigmem-20260905/). Targets: m12_m2_5/V1_1_6 (77 params), 2_9/V3_8 (111), m15_14/V1_9 (129), 2_9/V1_8 (136) on the SOURCE-COMPLETE charts (h-support gate §8 consumption rule: exact-Q UNIT on any one completed fibre kills its class); msolve native/graph presentations and guided Singular std, per the round-1 launch records (launched-workers.json, custody/, *_native.manifest.json, run_guided_job.py). YOUR JOB, and only this: (1) poll each worker every 10 minutes (ssh -i ~/.ssh/jc2-fleet; ps/RSS/etimes; the job status files; use harvest_one.sh) and append to box/moh-bigmem-20260905/harvest/; (2) harvest every FINISHED run with custody (input SHA, rows, ring, order, solver, rc, wall, peak RSS, output file SHA): a modular UNIT ⇒ immediate exact-Q confirmation on the identical generators (or a rational identity) before it is called a kill; a basis (NONUNIT) ⇒ dimension/degree + a sample point, reported loudly; alloc-fail/timeout ⇒ recorded as such; (3) HARD STOP: at 16:50Z (180 min after launch) — or earlier if every run has ended — stop remaining jobs (dispatch.sh kill / pkill on the worker), record their last state, then TERMINATE all eight workers with `sh ops/fleet/fleet.sh term <ID>` (IDs: i-0baedea1d34e4b978 i-0193dc1295fc5234a i-0ce9ea50559403c22 i-0e95f8ff97f6462ce i-043f250f1956bd34b i-02efd7ecd26becc5a i-018484399fd100293 i-0780c67ecdc79cb0a) and verify with `sh ops/fleet/fleet.sh ips`; never touch any other instance; (4) SEAL the report: per target/presentation/worker table, verdicts, the honest compute picture (which presentation got furthest, RSS curves, F4 degree reached). If a run is clearly within minutes of finishing at 16:50Z you may wait up to 20 more minutes. FALLACY-v2 (a first-prime [1] is not a char-0 certificate; a stopped run is not a result). ≤ 200 min; no ledger edits; no jc2-lean; no ideation-*. Continue in box/moh-bigmem-20260905/.
Report: xmodel/moh-bigmem-harvest-sol56-20260905.md
Seal (<!-- BODY-END -->); 8-18KB; 200 min.
charged_input=box/moh-bigmem-20260905/report_draft.md
charged_input=box/moh-bigmem-20260905/launched-workers.json
charged_input=box/moh-bigmem-20260905/harvest_one.sh
charged_input=xmodel/moh-hsupport-gate-astra-20260905.md
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/moh-bigmem-harvest-sol56-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
24d9dd7ff97d827a157f80e7dbee8e41eb98758d34a7b2e0bf9815538717aed3  {{LANE_INPUTS}}/report_draft.md
c5b71fba6ebb91be1bbf8ef5162e578311d35c7f160e51ff63dac1c680fb5c99  {{LANE_INPUTS}}/launched-workers.json
06b3b7e52960793da2c58991532f21239d9ab7c3f2e0c94c9e4a7187eef694cd  {{LANE_INPUTS}}/harvest_one.sh
4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354  {{LANE_INPUTS}}/moh-hsupport-gate-astra-20260905.md
ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
