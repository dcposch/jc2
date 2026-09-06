# ADOPTION LANE (≤ 120 min of YOUR time). The Sol long-solve launch lane died on a Codex usage limit after launching worker i-07e1212591a6acae9 (172.30.0.63, r7i.16xlarge 512 GB) at 07:55Z; it is UNKNOWN whether it regenerated the inputs or started the detached solves. You are AUTHORIZED to adopt that worker. GOAL: the (99,66) δ=2 direct attained-T₂+T₃ literal certificate subset d2-z55 (449 vars, 466 generators, 6,448,959 terms) must be under two DETACHED 20 h solves: (a) Singular exact-Q slimgb on 99-delta2-slimgb.sing (SHA 354b9293d065035f4e3b7ca2c918eb27cb5dc2ac3407eea2f02e9e467ba3ab7c) and (b) patched msolve -m 5000 -g 2 -t 64 -v 2 on 99-delta2.ms (SHA 7f593b87e40f02dbdb91f9b22aace6989f4a4d2092d9903276675b3265c7b572). TASK: (1) ssh in; inventory /home/ubuntu (any t2t3-longsolve dir, inputs, runs/, running processes); (2) if the inputs exist, verify the two SHAs; if not, regenerate them from the frozen drivers (build_direct.py + make_sound_prefix.py, per the frozen t2t3-direct report §5–§7) and verify the SHAs EXACTLY (stop and report on mismatch); build patched msolve 0.10.1 (apply both frozen patches; the wrapper msolve_m5000_wrapper.sh is charged); (3) if the solves are NOT running, start them DETACHED (systemd-run --user or nohup+setsid) with 72,000 s wall caps and RSS watchdogs (Singular 200 GB; msolve 400 GB address-space), writing runner.rc, time.txt, caprun.json and stdout under /home/ubuntu/t2t3-longsolve/runs/<job>/; if they ARE running, do not restart — record their start times and caps; (4) write box/t2t3-longsolve-20260906/custody.json on the host (≤ 100 KB: instance id, IP, start times, caps, input/binary SHAs, exact commands, harvest paths, expected end time) and DO NOT terminate the worker; (5) confirm both jobs running (ps + first F4 lines), then SEAL immediately: LAUNCHED[(99,66) δ=2 long solve; harvest due ~+20 h]. WORKER RULES: ssh as ubuntu with the jc2-fleet key (-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null); never reuse unowned instances; scratch on the worker; host writes ≤ 2 MB; `df -h /` before writing. No ledger edits; no jc2-lean; no ideation-* input. FALLACY-v2 (a modular unit is a signal; a compressed presentation must be PROVED equivalent).
Report: xmodel/t2t3-longsolve-adopt-opus5-20260906.md
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
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/t2t3-longsolve-adopt-opus5-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

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
