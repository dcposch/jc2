# INSTRUMENT + PROOF LANE (≤ 200 min): the 44 class-A residual rows (u_s = 1, roster) have source-support order-chart receivers that are COMPUTE-BOUND even at their smallest — R005 (source (135,90); class n27_m18_Mlast20_ell2; 307 unknowns, 484 generators) has ~53,209,262 terms in 306 c = 1 variables (frozen probe): Singular std reaches degree 55 at 124 GB/150 min with no basis; msolve segfaults pre-F4 (int64 offset; the t2t3 patches were not applied); guided_gb's Hilbert seed does not complete. On the split charts, the frozen t2t3-direct lane PROVED a direct-substitution compressor: recursive exact substitution of acyclic arithmetic variables took 7,136 circuit variables to 449 semantic variables (2,754 generators) with no constraint variable pivoted and j ∈ k^× a theorem. TASK: (1) read how the class-A receiver is emitted (the G_i-only emitter path referenced in chart-counts.json; the roster's row program; the h-support gate's source-complete charts) and identify its acyclic/arithmetic structure: which unknowns are defined by earlier ones (triangular), which are genuine free coefficients of the G_i envelopes, which rows are the Jacobian coefficient rows J(P,Q) − c·x^ℓ; (2) PORT the compressor: a driver box/classA-compressor-20260906/compress_receiver.py that, for a given class, performs recursive exact substitution (sympy/Singular exact-Q; stream, do not materialize 53M-term intermediates on the host — use a worker: launch your OWN r7i.8xlarge via `sh ops/fleet/fleet.sh launch r7i.8xlarge` + `fleet.sh wait`, terminate it with `fleet.sh term <id>` at the end; never reuse unowned instances) and reports the semantic variable count, generator count, term count for R005 FIRST, then (if time) R006 (322) and R008 (370); (3) PROVE the compression is an isomorphism of the ideal's zero set (substitution of a variable defined by a monic-in-that-variable row is a coordinate change; state the exact lemma and check no row is used as a pivot for a variable that appears nonlinearly); (4) if the compressed R005 system is small enough (say ≤ 600 variables and ≤ 10^6 terms), run msolve F4 modular (WITH the two t2t3 patches applied: box/t2t3-direct-20260906/msolve-0.10.1-*.patch) on the c = 1 section for ≤ 60 min and report the F4 degree telemetry (a [1] is a SIGNAL only); (5) VERDICT: compression ratios (typed), the isomorphism lemma, the F4 telemetry, and a sizing statement for the next worker. FALLACY-v2 (a modular unit is a signal; a compressed presentation must be proved equivalent, not asserted). DISK: host writes ≤ 2 MB; `df -h /` before writing; scratch on the worker. No ledger edits; no jc2-lean; no ideation-* input.
Report: xmodel/classA-compressor-astra-20260906.md
Seal (<!-- BODY-END -->); 8-16KB; 200 min.
charged_input=xmodel/classA-smallest-receiver-sol56-20260906.md
charged_input=xmodel/t2t3-direct-sol56-20260906.md
charged_input=box/t2t3-direct-20260906/build_direct.py
charged_input=box/t2t3-direct-20260906/make_sound_prefix.py
charged_input=box/t2t3-direct-20260906/msolve-0.10.1-heap-sort-permutation.patch
charged_input=box/t2t3-direct-20260906/msolve-0.10.1-int64-input-offset.patch
charged_input=box/residual66-20260905/chart-counts.json
charged_input=box/residual66-20260905/roster.jsonl
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/classA-compressor-astra-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
eab3d61b3fac63aedf2bfa3eb0479e2a6affbace70dc5920ad9b496ccd156cc2  {{LANE_INPUTS}}/classA-smallest-receiver-sol56-20260906.md
a0c3c3a0810e1765924ea06a8fdb6b0665feb3884195ea1514f01303eca8817c  {{LANE_INPUTS}}/t2t3-direct-sol56-20260906.md
77ef23b86f655e08a11913cf838a037c82adbb89cd1bc4a7e86c6471d034be3e  {{LANE_INPUTS}}/build_direct.py
92710ff81699850cd2b9fa93363bdda6d16b796db80f13365bd32e13c0174af2  {{LANE_INPUTS}}/make_sound_prefix.py
c49a9fb322c3c6518ff2234a7e521de3aa6a372efbe27dc4c9aa9360db3b2242  {{LANE_INPUTS}}/msolve-0.10.1-heap-sort-permutation.patch
4f2e723575ff2acbfcee4144d4c2e47cd314f6f25d1241bd1286c202c3863055  {{LANE_INPUTS}}/msolve-0.10.1-int64-input-offset.patch
4f9382b1c39e2a0b39e2dc14757607f0051969aefc331f3eb2efacd2c1a61d44  {{LANE_INPUTS}}/chart-counts.json
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
