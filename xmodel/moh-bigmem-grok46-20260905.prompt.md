# COMPUTE lane (brute-force the four smallest SOURCE-COMPLETE Moh ≤100 fibres on the biggest memory the fleet allows; every prior solve alloc-failed at 8–48 GiB — the h-support gate's final charts are the first COMPLETE charts, so a UNIT here is a genuine class kill under its §8 consumption rule): charts in box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes/ (read its README/manifests; msolve_chart.py / source_complete_emit.py there; the gate's ops/final-solve-summary.json records exactly what failed and how). TARGETS in order: m12_m2_5/V1_1_6 (77 params, s'=4 control, its 425-generator union chart), 2_9/V3_8 (111), m15_14/V1_9 (129), 2_9/V1_8 (136). For each: (a) r7i.24xlarge (768 GB) or x2idn.16xlarge (1 TB) worker, msolve 0.10.1 -t 32 with the native presentation + Tc−1 first (fewer rows than the graph presentation), then the graph presentation; a 3-hour watchdog per run, RSS logged; (b) in parallel on a second worker, Singular guided std (box/lib/guided_gb.py, Hilbert-hinted modular+CRT, y-first block order as in builder_fix) with the control battery; (c) any modular UNIT → immediate exact-Q confirmation on the identical generators (or the rational identity) before it is called a kill; (d) if a target finishes NONUNIT (a basis), report the dimension/degree and a sample point (that is a genuine over-approximation survivor and the biggest news possible). Report per target: input custody (chart SHA, rows, ring, order), solver, wall, peak RSS, rc, verdict. FALLACY-v2 (a first-prime [1] from msolve is not a char-0 certificate; header-only/timeout/halt is not a result). FLEET: launch your own workers with `sh ops/fleet/fleet.sh launch 1 r7i.16xlarge` (512 GB; r7i.24xlarge=768 GB, x2idn.16xlarge=1 TB allowed) — `fleet.sh ips`, `ops/fleet/dispatch.sh run <IP> <CLASS> <STEM>` (detached, survives disconnect), `dispatch.sh poll`; workers carry Singular/msolve 0.10.1/qqideal/msolveio; TERMINATE every worker you launch before sealing (`fleet.sh term <ID>`); do not touch workers you did not launch. ≤ 240 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/moh-bigmem-20260905/.
Report: xmodel/moh-bigmem-grok46-20260905.md
Seal (<!-- BODY-END -->); 10-25KB; 240 min.
charged_input=xmodel/moh-hsupport-gate-astra-20260905.md
charged_input=xmodel/moh14-fix-solve-opus5-20260905.md
charged_input=box/lib/guided_gb.py
charged_input=box/moh14-charts-20260905/builder_fix.py
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/moh-bigmem-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354  {{LANE_INPUTS}}/moh-hsupport-gate-astra-20260905.md
2372687402bdb5b83a9ecd28d206f215abb834508f9a937b94c81350a54f42e2  {{LANE_INPUTS}}/moh14-fix-solve-opus5-20260905.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b  {{LANE_INPUTS}}/builder_fix.py
c0ea96034bf12b7445aa123f00cf600baaca81751f36a91855987f44fd6311e3  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
