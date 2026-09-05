# RESUME lane (round 2 of moh-bigmem-grok46-20260905: the round-1 CLI exited after ~17 min WITHOUT writing its report, but it HAD launched the solves — they are RUNNING NOW on eight workers it launched at 13:49Z: r7i.24xlarge 172.30.0.108/.183/.190/.202 and x2idn.16xlarge 172.30.0.121/.125/.45/.55 (msolve at 45–75 GB RSS on .108/.183/.202; Singular on the others; see the charged launched-workers.json and box/moh-bigmem-20260905/{assemble_and_launch.sh, extract_native.sh, custody/, circuit-src/}). YOUR JOB: ADOPT AND HARVEST, then TERMINATE. (1) Read round 1's launch records to learn which target (m12_m2_5/V1_1_6 77 params; 2_9/V3_8 111; m15_14/V1_9 129; 2_9/V1_8 136), presentation (native / graph), solver and limits run on which worker; ssh (~/.ssh/jc2-fleet) and poll each: alive (pid, etimes, RSS, /usr/bin/time output if finished), finished (rc, output file), OOM/alloc-fail; (2) any FINISHED msolve/Singular result: harvest with custody (input SHA, rows, ring, order, solver, rc, wall, peak RSS); a modular UNIT ⇒ immediate exact-Q confirmation on the identical generators (or the rational identity) before calling it a kill; a basis (NONUNIT) ⇒ dimension/degree + a sample point, reported loudly; (3) let live runs continue up to a total of 180 min from THEIR start (13:49Z–14:00Z ⇒ hard stop ≈ 17:00Z; if a run is clearly progressing at that point and RSS is stable you may extend to 200 min of lane time, then stop); (4) TERMINATE all eight workers (`sh ops/fleet/fleet.sh term <ID>`; IDs in launched-workers.json) before sealing — verify with `fleet.sh ips`; never touch .7/.18/.28/.67/.86/.127/.163 or lean-01/lean-02/math-hq; (5) report per target as the round-1 prompt required. FALLACY-v2 (a first-prime [1] from msolve is not a char-0 certificate; header-only/timeout/halt is not a result). ≤ 150 min; no ledger edits; no jc2-lean; no ideation-*. Continue in box/moh-bigmem-20260905/.
Report: xmodel/moh-bigmem-grok46-r2-20260905.md
Seal (<!-- BODY-END -->); 8-20KB; 150 min.
charged_input=box/moh-bigmem-20260905/launched-workers.json
charged_input=box/moh-bigmem-20260905/assemble_and_launch.sh
charged_input=xmodel/moh-bigmem-grok46-20260905.prompt.md
charged_input=xmodel/moh-hsupport-gate-astra-20260905.md
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/moh-bigmem-grok46-r2-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
c5b71fba6ebb91be1bbf8ef5162e578311d35c7f160e51ff63dac1c680fb5c99  {{LANE_INPUTS}}/launched-workers.json
3b937a4a65b8c830f078995454c250b7267156301c9b3cc1bbd8a970830f5b0b  {{LANE_INPUTS}}/assemble_and_launch.sh
226d5f87d42b8e054313d88977c9fccd3915d9761dcd40fef405718170f2a633  {{LANE_INPUTS}}/moh-bigmem-grok46-20260905.prompt.md
4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354  {{LANE_INPUTS}}/moh-hsupport-gate-astra-20260905.md
c0ea96034bf12b7445aa123f00cf600baaca81751f36a91855987f44fd6311e3  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
