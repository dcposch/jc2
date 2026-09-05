# COMPUTE lane (extend theorem (T) on the K16 ray from t≤7 to t=8 via the ONE-EVALUATION certificate, AUDIT 17(vvvvvv) OPEN[K16-ONE-POINT-T8]): the Γ-Galois lane proved the fixed-t certificate of (V0)-tail is "(i)_t ∧ one simple lifted F_p-point of Γ_t with W ≠ 0" (Lemmas 3.1, 3.7; validated t=3..6 vs Singular), and left t=8 READY: the CI system (7 forms, 52,140 points) mod 32003 is exported (box/k16galois-20260905/msolve_t8_mod_p32003_b0_ci.sing + _minors.sing), the boundary of Γ_8 has six points with W≠0 (boundary_t8_*.sing), the verify job (verifypoint_*, validated at t=6) is ready. FINISH IT: obtain ONE simple affine F_32003-point of Γ_8 (b₄≠0) and verify W ≠ 0 there (+ the étale-lift hypotheses), giving clause (ii)_8 — with (i)_8 (B-HSOP, banked through t=8, 17(rrrrr)) this certifies (V0)-tail at t=8 ⇒ (8.1) ⇒ theorem (T) at t=8

OPERATIONAL: Grok — FOREGROUND jobs only (setsid/nohup on a WORKER if long, then
poll; never a background job you don't wait for); the fleet: ~/.ssh/jc2-fleet,
c7i workers 172.30.0.7/.18/.28 (64GB each); msolve + Singular + guided_gb on
them; rsync box/k16galois-20260905 to the worker. Task: (1) the CI point
system: at seal msolve F4 was at degree 14 (45739×81237) on a shared worker —
run it to completion on a DEDICATED worker (msolve, 8+ threads, timeout 3 h)
OR, faster, use the boundary/minors route: the lane found six boundary points
with W≠0 mod 32003 — if a boundary (or any) simple point of Γ_8 on the flat
model satisfies Lemma 3.7's étale-lift hypotheses, it suffices; determine
whether an AFFINE (b₄≠0) point is required or a boundary point already
certifies (ii)_8 per the lane's Prop 7.1 (clause (ii) via the modular cone
V(I₂+(W))={0} + flatness); (2) run the verify job at the obtained point: W ≠ 0,
simplicity (Jacobian rank), the good-reduction hypotheses of Lemmas 3.3–3.5 at
p=32003 for t=8 (A_8 = Q(√27)=Q(√3)); (3) if certified: state (V0)-tail at t=8
⇒ (8.1)_8 ⇒ (T) at t=8, with (i)_8 cited (17(rrrrr) B-HSOP through t=8) — this
EXTENDS the ray's proved range to t=1..8; (4) if the CI solve does not finish
in budget and no boundary point suffices: report the deepest degree reached +
OPEN with the exact remaining job; (5) controls: re-run the t=6 verify
(verifypoint_t6_*, must reproduce); a perturbed W (must FAIL). FALLACY-v2 (a
modular one-point nonvanishing is char-0 only via the étale lift Lemma 3.7 with
its hypotheses checked at t=8 — check them, do not assume). ≤ 180 min; no
ledger edits; no jc2-lean; no ideation-*. Drivers to box/k16t8-20260905/.
Report: xmodel/k16-t8-onepoint-grok46-20260905.md
Seal (<!-- BODY-END -->); 12-24KB; 180 min.
charged_input=xmodel/k16-gamma-galois-fable5-20260905.md
charged_input=xmodel/k16-rank-criterion-fable5-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=FALLACY-v2.md
charged_input=box/k16galois-20260905/boundary_t8_mod_p32003_b0.sing
charged_input=box/k16galois-20260905/msolve_t8_mod_p32003_b0_ci.sing
charged_input=box/k16galois-20260905/msolve_t8_mod_p32003_b0_minors.sing
charged_input=box/k16galois-20260905/pattern_t8_mod_p32003_b0_dimonly.sing
charged_input=box/k16galois-20260905/verifypoint_t6_mod_p32003_b0.err
charged_input=box/k16galois-20260905/verifypoint_t6_mod_p32003_b0.out
charged_input=box/k16galois-20260905/verifypoint_t6_mod_p32003_b0.sing
charged_input=box/k16galois-20260905/verifypoint_t6_mod_p32003_b0.time
charged_input=box/k16galois-20260905/crosscheck_f4.py
charged_input=box/k16galois-20260905/msolve_point.py
charged_input=box/k16galois-20260905/analyze_patterns.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k16-t8-onepoint-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
6a9eecf596423b9a7c965fdeae4c3d24727821848a449f5899086102a8ae7ad0  {{LANE_INPUTS}}/k16-gamma-galois-fable5-20260905.md
7cfa230c0c9ec1b4124b9581b1c461cb19ef004e8a36c2820e7efece0fb185c5  {{LANE_INPUTS}}/k16-rank-criterion-fable5-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
e712e119f03e09b4da560565655a423ddb937b8a085e4a5522769319665bdb78  {{LANE_INPUTS}}/boundary_t8_mod_p32003_b0.sing
4b2b0340c90809d6d5c1165cea3abca7636b19d935072e182199cb73294b9686  {{LANE_INPUTS}}/msolve_t8_mod_p32003_b0_ci.sing
a1b94a0d7eb2f5d54668c5615d4606fcd7f4092c3b185fa92e7f6d833d65c5f1  {{LANE_INPUTS}}/msolve_t8_mod_p32003_b0_minors.sing
1c9e00b1e66cee127b49c0218857f96bd524b424aeaffc0483f3316f7b86159d  {{LANE_INPUTS}}/pattern_t8_mod_p32003_b0_dimonly.sing
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  {{LANE_INPUTS}}/verifypoint_t6_mod_p32003_b0.err
6b87efdd1b671a76270f6bf341a57d886acb9347274dcb0582ba563849d6a2ef  {{LANE_INPUTS}}/verifypoint_t6_mod_p32003_b0.out
565985fc1445bdb944ee008cf03547bf01d3a68c68192efec2ac692c5bad27b5  {{LANE_INPUTS}}/verifypoint_t6_mod_p32003_b0.sing
2bb6e1673e75e0957eb1e9c9233b83589540103a9c4d63a9b87a8685795c7aff  {{LANE_INPUTS}}/verifypoint_t6_mod_p32003_b0.time
703b457b365d72cbf303fdbc2f3d2503ff0f1213be408a7f5b9158e029b08694  {{LANE_INPUTS}}/crosscheck_f4.py
17b825c32dc4379281cf8680eb44d7d8038c645aeddc757ca6b41a664fa7ef27  {{LANE_INPUTS}}/msolve_point.py
70043e51029daa0e3f542d1ea5e8e96476b1d15f3ecfa7733f486ada7a646963  {{LANE_INPUTS}}/analyze_patterns.py
```
