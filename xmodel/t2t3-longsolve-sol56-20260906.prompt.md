# DECOUPLED LONG-SOLVE LAUNCH (≤ 120 min of YOUR time; the solves run ~20 h unattended). The (99,66) δ=2 direct attained-T₂+T₃ literal certificate subset d2-z55 (449 vars, 466 generators, 6,448,959 terms; generator-stream SHA a78c6a46…; executed inputs: 99-delta2-slimgb.sing SHA 354b9293d065035f4e3b7ca2c918eb27cb5dc2ac3407eea2f02e9e467ba3ab7c, 99-delta2.ms SHA 7f593b87e40f02dbdb91f9b22aace6989f4a4d2092d9903276675b3265c7b572) timed out at 9,000 s on both engines (Singular slimgb 106 GB; patched msolve F4 at round ~11 and progressing). The worker was terminated with its streams; the inputs must be REGENERATED from the frozen drivers (build_direct.py + make_sound_prefix.py from the t2t3 lane; their outputs must reproduce the two SHAs above EXACTLY — if not, stop and report the discrepancy). TASK: (1) launch YOUR OWN r7i.16xlarge (512 GB) via `sh ops/fleet/fleet.sh launch r7i.16xlarge` + `fleet.sh wait`; build patched msolve 0.10.1 (apply the two frozen patches); regenerate the two inputs on the worker and verify the SHAs; (2) start, DETACHED (systemd-run or nohup + setsid, surviving your session), two capped jobs with 72,000 s (20 h) wall caps and per-job RSS watchdogs (Singular 200 GB; msolve 400 GB address-space cap): (a) Singular exact-Q slimgb on 99-delta2-slimgb.sing; (b) patched msolve -m 5000 -g 2 -t 64 -v 2 on 99-delta2.ms; each writing runner.rc, time.txt, caprun.json and the solver stdout under /home/ubuntu/t2t3-longsolve/runs/<job>/; (3) write a CUSTODY receipt box/t2t3-longsolve-20260906/custody.json on the host (≤ 100 KB): instance id, IP, start times, caps, input SHAs, binary SHAs, exact commands, the paths a harvest lane must read, and the expected end time — and DO NOT terminate the worker (the harvest lane will). (4) Confirm both jobs are running (ps, first F4 lines), then SEAL your report immediately. Nothing here is a mathematical verdict: type it as LAUNCHED[(99,66) δ=2 long solve; harvest due ~+20 h]. FALLACY-v2. DISK: host writes ≤ 2 MB; `df -h /` before writing. No ledger edits; no jc2-lean; no ideation-* input.
Report: xmodel/t2t3-longsolve-sol56-20260906.md
Seal (<!-- BODY-END -->); 3-8KB; 120 min.
charged_input=xmodel/t2t3-harvest-sol56-20260906.md
charged_input=xmodel/t2t3-direct-sol56-20260906.md
charged_input=box/t2t3-direct-20260906/build_direct.py
charged_input=box/t2t3-direct-20260906/make_sound_prefix.py
charged_input=box/t2t3-direct-20260906/msolve-0.10.1-heap-sort-permutation.patch
charged_input=box/t2t3-direct-20260906/msolve-0.10.1-int64-input-offset.patch
charged_input=box/t2t3-direct-20260906/msolve_m5000_wrapper.sh
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/t2t3-longsolve-sol56-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
f3fce66b5412fd80c5cc0f882c6f531b18f2a22ee39e6f597d54f1a28d32852c  {{LANE_INPUTS}}/t2t3-harvest-sol56-20260906.md
a0c3c3a0810e1765924ea06a8fdb6b0665feb3884195ea1514f01303eca8817c  {{LANE_INPUTS}}/t2t3-direct-sol56-20260906.md
77ef23b86f655e08a11913cf838a037c82adbb89cd1bc4a7e86c6471d034be3e  {{LANE_INPUTS}}/build_direct.py
92710ff81699850cd2b9fa93363bdda6d16b796db80f13365bd32e13c0174af2  {{LANE_INPUTS}}/make_sound_prefix.py
c49a9fb322c3c6518ff2234a7e521de3aa6a372efbe27dc4c9aa9360db3b2242  {{LANE_INPUTS}}/msolve-0.10.1-heap-sort-permutation.patch
4f2e723575ff2acbfcee4144d4c2e47cd314f6f25d1241bd1286c202c3863055  {{LANE_INPUTS}}/msolve-0.10.1-int64-input-offset.patch
324f4e8c8a5b112dbf6051e5bb84aff0d6de4ccc973cfca1919881766145f9b9  {{LANE_INPUTS}}/msolve_m5000_wrapper.sh
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
