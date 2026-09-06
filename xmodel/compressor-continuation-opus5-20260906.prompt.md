# ADOPTION + INSTRUMENT + PROOF LANE (≤ 200 min). The Astra compressor lane died on a Codex usage limit at ~08:05Z, leaving worker i-0b019d96be51d78a4 (172.30.0.156, r7i.8xlarge) RUNNING with its work under /home/ubuntu/classA-compressor-20260906/ (R005 exact-Z native stream 53,209,262 terms, SHA b4a4160c…; ordinary stream 2,902,778 terms, SHA c437d0a1…; a Singular substitution chain 'classA-compress-R005-v2' that had pivoted A1_1_7, A1_2_5, A1_3_3 …). You are AUTHORIZED to adopt that worker (and must terminate it with `sh ops/fleet/fleet.sh term i-0b019d96be51d78a4` when done). TASK: (1) ssh in; determine whether the Singular chain is still running (systemctl/ps); read its log; record where it got to (pivot count, generators, terms); (2) CONTINUE the compression to completion for R005: recursive exact substitution of arithmetic variables defined by rows monic-linear in them; report the final semantic variable count, generator count, term count; (3) PROVE the compression is sound: state the lemma (substituting a variable v by the polynomial q(other vars) from a row v − q = 0 is an isomorphism of the zero set onto the projection; no row used as pivot may contain v nonlinearly; the order of pivots does not matter) and CHECK mechanically that every pivot row was linear-monic in its pivot; (4) with the compressed R005 system, run patched msolve 0.10.1 (build from the frozen patches; the compressor lane's msolve-provenance.json records the source commit) F4 modular (-g 2 -t 32, p = 1073741827) on the c = 1 section, ≤ 60 min: report F4 degree telemetry, matrix sizes, and a [1] as SIGNAL only; (5) copy ONLY compact results (≤ 2 MB: counts, SHAs, the compression pivot list, F4 log head) to box/compressor-continuation-20260906/; (6) VERDICT: compression ratio (typed), lemma, telemetry, next-worker sizing; if the compressed system is ≤ 600 variables and F4 progresses, say so plainly. WORKER RULES: ssh as ubuntu with the jc2-fleet key (-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null); never reuse unowned instances; scratch on the worker; host writes ≤ 2 MB; `df -h /` before writing. No ledger edits; no jc2-lean; no ideation-* input. FALLACY-v2 (a modular unit is a signal; a compressed presentation must be PROVED equivalent).
Report: xmodel/compressor-continuation-opus5-20260906.md
Seal (<!-- BODY-END -->); 8-14KB; 200 min.
charged_input=xmodel/classA-smallest-receiver-sol56-20260906.md
charged_input=box/classA-compressor-20260906/compress_receiver.py
charged_input=box/classA-compressor-20260906/sparse_ordinary_r005.py
charged_input=box/classA-compressor-20260906/sparse-ordinary.json
charged_input=box/classA-compressor-20260906/singular-superseded.json
charged_input=box/classA-compressor-20260906/msolve-provenance.json
charged_input=box/t2t3-direct-20260906/msolve-0.10.1-heap-sort-permutation.patch
charged_input=box/t2t3-direct-20260906/msolve-0.10.1-int64-input-offset.patch
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/compressor-continuation-opus5-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
eab3d61b3fac63aedf2bfa3eb0479e2a6affbace70dc5920ad9b496ccd156cc2  {{LANE_INPUTS}}/classA-smallest-receiver-sol56-20260906.md
9994abaf4c901568e89212241481eff9dff411f59b7c75073a9bbf737cb68f19  {{LANE_INPUTS}}/compress_receiver.py
22fc47b7e3f86112a9d80b65a1fcf6698215b79a611f78d9966006ef23c6b2ab  {{LANE_INPUTS}}/sparse_ordinary_r005.py
6c0541fa6f4cd9d85a85501579f912056be9e8e75096614b4f642fa993b6d37a  {{LANE_INPUTS}}/sparse-ordinary.json
6ea9ec0c65646cdc39ea70645d62ef2cf1de6adbf3201bd9b130fafad2486bb7  {{LANE_INPUTS}}/singular-superseded.json
fc9e0252413d01830cfbf3c15ec543a1aa9b385f8e4207e73f5718e92efeb39c  {{LANE_INPUTS}}/msolve-provenance.json
c49a9fb322c3c6518ff2234a7e521de3aa6a372efbe27dc4c9aa9360db3b2242  {{LANE_INPUTS}}/msolve-0.10.1-heap-sort-permutation.patch
4f2e723575ff2acbfcee4144d4c2e47cd314f6f25d1241bd1286c202c3863055  {{LANE_INPUTS}}/msolve-0.10.1-int64-input-offset.patch
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
