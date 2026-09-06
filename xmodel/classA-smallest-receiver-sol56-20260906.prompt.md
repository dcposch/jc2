# COMPUTE PROBE (≤ 200 min wall): the residual at n ≤ 200 is 64 necessary rows; class A = the 44 rows at u_s = 1 (roster provenance own_route_state NONEMPTY, descent LICENSED, u_s = 1) with 100 < n ≤ 200 — their only remaining instrument is the source-support order-chart receiver (G_i-only emitter, coefficient rows + (Tc−1)). The 70-unknown Moh ≤100 chart did not finish in 170 min by four methods (frozen 17(lllllllll) disposition; the guided_gb failure there was an instrument bug since PATCHED: Hilbert-seed stage + typed timeout contract). TASK: (1) from the frozen chart-counts.json 'classes' (unknown counts per receiver class) and roster.jsonl, identify the SMALLEST receiver class that covers at least one class-A row with 100 < n ≤ 200 (state the row(s), the class id, unknowns, generator count); cite the row program path under box/gi-only-20260905/classes/ (uncharged; read-only; verify its coefficient_coordinate_sha256 against chart-counts.json before use); (2) on the IDLE fleet worker 172.30.0.163 (r7i.8xlarge, 256 GB; use the jc2-fleet key via ops/fleet/fleet.sh conventions; do NOT launch new instances; do NOT terminate anything; write scratch on the WORKER, host writes ≤ 2 MB), run THREE bounded jobs, each ≤ 150 min, in parallel: (a) box/lib/guided_gb.py (patched) on (I : c^∞) with the weighted block order; (b) msolve 0.10.1 AVX-512 F4 modular (-g 2, p = 1073741827) on the c = 1 section; (c) Singular exact-Q std(I + (Tc−1)) with the T-block; record for each: completion or typed timeout, peak RSS, degree reached (F4 step log), basis size; (3) if ANY finishes: a modular [1] is a SIGNAL (type it so; a c = 1 unit still needs the homogeneous lift to a c^N identity, cone lemma); an exact-Q [1] on the full ideal with Tc−1 is a KILL of that receiver class — state which rows it kills and whether their charts are source-COMPLETE per the frozen h-support gate; a nonunit basis is a SURVIVAL of this screen only; (4) VERDICT: typed compute disposition per job + the F4 degree wall (the highest degree step completed and its matrix size) so the next lane can size the worker. FALLACY-v2 (floor ≠ attainment; a modular unit is a signal, not a certificate; a row needs its printed line). DISK DISCIPLINE: host ≤ 2 MB; `df -h /` before writing; scratch on the worker only; clean the worker scratch at the end but leave the instance running. No ledger edits; no jc2-lean; no ideation-* input. Notes to box/classA-smallest-20260906/.
Report: xmodel/classA-smallest-receiver-sol56-20260906.md
Seal (<!-- BODY-END -->); 6-14KB; 200 min.
charged_input=box/residual66-20260905/chart-counts.json
charged_input=box/residual66-20260905/roster.jsonl
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/classA-smallest-receiver-sol56-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4f9382b1c39e2a0b39e2dc14757607f0051969aefc331f3eb2efacd2c1a61d44  {{LANE_INPUTS}}/chart-counts.json
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826  {{LANE_INPUTS}}/guided_gb.py
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
