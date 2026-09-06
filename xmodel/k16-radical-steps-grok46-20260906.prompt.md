# BOUNDED K16 CERTIFICATES (≤ 50 min of model time; finite-t computations from frozen bases): astra #3 and sol56 Q3.A (both sealed submissions charged) propose the SAME two-step radical certificate for the K16 uniform statement: with u = 4η + 3b·l₂ (weight 2t), r = Bη (weight 4t+1), T₂ the 4-jet quadratic (weight 4t) and u² + 4T₂ ∈ J_t (the tacnode report's identity Lpivot² = −4T₂ − 24E₂), seek bounded syzygies u³ ∈ J_t + (r) and r² ∈ J_t + (u); together they give u ∈ √J_t and then r ∈ √(J_t + (u)), i.e. (R) at that t; eliminate the L-tail first through its unit Toeplitz block. TASK: at t = 3, 4, 5 (and 6 if it fits) from the frozen exact bases (box/k16xempty-20260905/controls_t{3,4,5}_raw.sing; identity map on (c_i, b); minpoly 3d² − N): (1) verify u² + 4T₂ ∈ J_t; (2) compute the minimal exponents e₁, e₂ with u^{e₁} ∈ J_t + (r) and r^{e₂} ∈ J_t + (u) (Singular reduce/lift, exact over Q(d) or modularly with exact confirmation) and record the cofactor weights; (3) tabulate e₁(t), e₂(t) and the cofactor degrees — is there a t-uniform pattern (constant exponents, cofactors of bounded weight) that a symbolic proof in the universal recursion could target? (4) VERDICT: pattern found (state the conjectured uniform identities exactly) / exponents grow (state how). FALLACY-v2 (finite-t identities are not a theorem). DISK DISCIPLINE: ~3 GB free on the host — report + notes ≤ 2 MB; no artifact trees; df -h / before any write > 10 MB. No fleet. ≤ 55 min; no ledger edits; no jc2-lean; no other ideation-* input. Drivers to box/k16-radical-20260906/.
Report: xmodel/k16-radical-steps-grok46-20260906.md
Seal (<!-- BODY-END -->); 5-14KB; 55 min.
charged_input=xmodel/ideation-20260906T0000Z-astra.md
charged_input=xmodel/ideation-20260906T0000Z-sol56.md
charged_input=xmodel/k16-tacnode-fable5-20260905.md
charged_input=xmodel/k16-universal-series-fable5-20260905.md
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k16-radical-steps-grok46-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
2123d618bb7036b4e680859fe8bace7ac82a4408ae4eb8aa2d48d9a2ff7fcdfd  {{LANE_INPUTS}}/ideation-20260906T0000Z-astra.md
23fd5cca53b615f3d93b0fd4b1126a26916c7ea493523e4d2ed8bbd9808f13b7  {{LANE_INPUTS}}/ideation-20260906T0000Z-sol56.md
ab1c4ca249f85f3978108fe9e26f391695805e443fdb51a6be135635b2a0fa31  {{LANE_INPUTS}}/k16-tacnode-fable5-20260905.md
5ac0ff1ddcfc766dd1d5050c73e08203795f1ecc56be954b388ef0c1eaeb41bb  {{LANE_INPUTS}}/k16-universal-series-fable5-20260905.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
