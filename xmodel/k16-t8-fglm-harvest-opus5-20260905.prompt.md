# HARVEST + FINISH lane (theorem (T) at t = 8 is three steps away; the frozen t=8 report §10 lists them exactly): msolve F4 of subst(G, b₄=1) over F_32003 is COMPLETE (quotient dimension 52,138 = n' = n, cone dim 1) and the FGLM + rational parametrization is RUNNING on worker 172.30.0.7 (pid 64330, `msolve -v 2 -t 16 -l 44 -u 1 -P 1`, RSS ~18 GiB, log at box/k16t8-20260905/w7/, param file w7/msolve_t8_param_t16.txt still 0 bytes at 15:2xZ; expected several hours). Worker .7 is a shared c7i (do NOT terminate it; do not kill other jobs on it; a leftover 4-thread job + I2+(W) run is on .28). TASK, in order: (1) poll pid 64330 every 10 min (ssh -i ~/.ssh/jc2-fleet ubuntu@172.30.0.7; RSS, log tail, param file size); while waiting, PREPARE step (iv): (a) from the elimination polynomial's degree pattern + Corollary 3.6 of the charged Galois report, write out exactly what would prove k₈ = 1 (one Galois orbit on Y₈), and (b) set up the affine half of Prop 7.1, vdim(I₂ + (W) + (b₄ − 1)) = 0, as a msolve/Singular job on worker .28 or a fresh c7i.4xlarge (launch via `bash ops/fleet/fleet.sh launch 1 c7i.4xlarge`; terminate it before sealing) — this is the route that certifies ALL of Y₈ at once, and it may finish before FGLM; (2) when the parametrization lands: `python3 msolve_point.py w7/msolve_t8_param_t16.txt` (validated at t = 6) → an F_p-point of Γ₈ ∩ {b₄ ≠ 0}; then `gen.py 8 --mode mod --prime 32003 --branch 0 --job verifypoint --point 1,q2,…,q7` and the evalpoint checks (local vdim 1, JACRANK 6, MINORS_ZERO, KERNEL_CONSISTENT, W ≠ 0, FITT) — full custody; (3) VERDICT: (ii)₈ CERTIFIED (one affine simple point with W ≠ 0 AND k₈ = 1 or the Prop 7.1 affine vdim = 0) ⇒ with the banked (i)₈ B-HSOP, (V0)-tail₈ ⇒ (8.1)₈ ⇒ (T) at t = 8, typed PROVED-HERE for gate / one-orbit-only (state exactly what is missing) / FGLM did not finish in budget (leave it running, record pid/state, and hand off). FALLACY-v2 (a modular point is a signal for the étale lift only under the lemmas' hypotheses; do not infer k₈ from t ≤ 6). ≤ 220 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/k16t8-20260905/ (continue there).
Report: xmodel/k16-t8-fglm-harvest-opus5-20260905.md
Seal (<!-- BODY-END -->); 10-20KB; 220 min.
charged_input=xmodel/k16-t8-onepoint-grok46-20260905.md
charged_input=xmodel/k16-gamma-galois-fable5-20260905.md
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k16-t8-fglm-harvest-opus5-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4765d55da5fe89300a204e39730bfaf132e3e970a9ae35215dbfd4b9ca93ee82  {{LANE_INPUTS}}/k16-t8-onepoint-grok46-20260905.md
6a9eecf596423b9a7c965fdeae4c3d24727821848a449f5899086102a8ae7ad0  {{LANE_INPUTS}}/k16-gamma-galois-fable5-20260905.md
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
