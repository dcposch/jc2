# Proof-attack lane (the uniform K = 16 statement in its sharpest banked form): Lemma SQUARE (your own 17(wwww)) reduces (V0) — hence (8.1), hence theorem (T) on the whole K = 16 ray — to the non-vanishing of the weighted multivariate resultant Res_w(R_1, …, R_{t−1}) of a SQUARE weighted-homogeneous system in the t − 1 variables (b₄, q_{2,0}, …, q_{t−1,0}) of weights (1, 2, …, t−1), with R_r of weight 4t+4+2r; the resultant is ONE element ρ_t ∈ A_t = Q[y]/(H_t) per t. Compute ρ_t (or a certified nonzero multiple/divisor, or its norm N(ρ_t) ∈ Q) exactly at t = 3, 4, 5 (and modular at 6, 7), find its structure in t, and attack the uniform statement ρ_t ≠ 0 structurally (Macaulay resultant of the leading forms; degeneration to a monomial/binomial system with the same weights; toric/BKK count on the weighted Newton polytopes; or an explicit Bézout-type non-vanishing via a witness point at infinity that the system misses). Also weigh the alternative of Lemma SQUARE at the b₄ = 0 boundary (the initial forms R_r|_{b₄=0} in q alone: if THEIR resultant is nonzero for all t the weighted-homogeneous system has no solution at b₄ = 0, which combined with the finiteness of the b₄ = 1 fibre gives (V0) only if the b₄ = 1 fibre is empty — say precisely what the boundary resultant buys)

OPERATIONAL: skeleton first; every job in the foreground with `timeout
1800`; never end the turn with a job running; ≤ 3 cores. Tools: your charged
drivers (box/k16toptail-20260903/, box/k16terminal-fable5-20260903/); the
properness instrument (17(kkkk)) for modular → char-0 promotion of dim = 0
statements; Singular `resultant` / `mres`, Macaulay-matrix construction by
hand for the weighted case (the weights are pairwise-distinct — use the
substitution b₄ = z, q_{j,0} = z^j q̃_j to homogenise? — no: state the correct
weighted Macaulay theory you use, or work with the standard resultant of
the un-weighted dehomogenised system on b₄ = 1 and the boundary system on
b₄ = 0 separately). Deliverables: (1) exact ρ_t or N(ρ_t) at t = 3, 4, 5 with
the method; modular non-vanishing at t = 6, 7; (2) the factor structure
(does ρ_t factor over A_t? which factor vanishes at the y = 1/5 fibre of t = 2
where the cone is the b₃-axis? — the t = 2 control must show ρ_2(1/5) = 0 or
explain why the t = 2 case is outside the lemma); (3) the uniform attack
with a proof or the exact residual; (4) controls and FALLACY-v2 audit.
≤ 180 min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress
lane reports. Drivers to box/k16res-20260903/.
Report: xmodel/k16-square-resultant-fable5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-30KB; 180 minutes.
charged_input=xmodel/k16-toptail-quadratics-fable5-20260903.md
charged_input=xmodel/k16-hilbert-regseq-sol56-20260903.md
charged_input=xmodel/k16-chain-gate-grok46-20260903.md
charged_input=xmodel/k16-properness-gate-opus5-20260903.md
charged_input=xmodel/k16-terminal-proof-fable5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16toptail-20260903/norm_check.py
charged_input=box/k16toptail-20260903/stageB_F4_t5_mod_p32009_b0.sing
charged_input=box/k16toptail-20260903/stageA_t3_exact.sing
charged_input=box/k16toptail-20260903/stageB_D4_t3_exact.sing
charged_input=box/k16toptail-20260903/stageA_t5_exact.sing
charged_input=box/k16toptail-20260903/stageB_E1_t4_exact.sing
charged_input=box/k16hilb-20260903/decode_hilbert.py
charged_input=box/k16hilb-20260903/emit_hilbert_job.py
charged_input=box/k16hilb-20260903/emit_preexpanded_cone_job.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-square-resultant-fable5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
638f5e2ed6755b32b92944830e32f6b4a67d321a9e442adca9a59f2f4ba5b05c  {{LANE_INPUTS}}/k16-toptail-quadratics-fable5-20260903.md
69ea2475c0471ff2254d39d177f35029068d31fea53b29ba7bd35565ec9c29e7  {{LANE_INPUTS}}/k16-hilbert-regseq-sol56-20260903.md
f58585ad6276461e531c5850158a57446d39fb77b74676ac74db0224e7d861f0  {{LANE_INPUTS}}/k16-chain-gate-grok46-20260903.md
f4d071a18cff25c4bdade4508f53c58bc39d20a26907fa619410622bfb91ccf6  {{LANE_INPUTS}}/k16-properness-gate-opus5-20260903.md
16d5112ae6ed9a6de0c504b11df2e19c97ed031a1715a3916fd8d207cdf0d961  {{LANE_INPUTS}}/k16-terminal-proof-fable5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
9370bfe7204975cd0b1b37e83de7bef0bb196fb4603f3d777210768063f6df39  {{LANE_INPUTS}}/norm_check.py
238edab95b9acdcc1d9f13a33a11bfe3ca56e680df3b14069921cd6af003a97b  {{LANE_INPUTS}}/stageB_F4_t5_mod_p32009_b0.sing
b836d47e31bbe2b49a33590716e1323b684d7fe6988a75f4c3afc260d9986b5a  {{LANE_INPUTS}}/stageA_t3_exact.sing
877b666414bc30919afc2751448af9e4fb17379cfdff5397d18e9bf54914362d  {{LANE_INPUTS}}/stageB_D4_t3_exact.sing
8d6368a7c70b05305d35ecebdbf163e33295b4bc32b34058298433e1af2c3a8b  {{LANE_INPUTS}}/stageA_t5_exact.sing
e6a12cc6fa4ec360f2157de3495ae83e8fb1474dcf15eea006412530e69c541a  {{LANE_INPUTS}}/stageB_E1_t4_exact.sing
1cd32e12f4a6181402363445a8c24f68b2265af8b325da26bee7363d7fdef9ee  {{LANE_INPUTS}}/decode_hilbert.py
1dc349d9c38db9de0a0c95cc211a836af66d7de6433d071f971e2ccc633cb4fc  {{LANE_INPUTS}}/emit_hilbert_job.py
28e53f84eb470e6556aca430c2bce32530e71dbf245810e431ec75125095bcfb  {{LANE_INPUTS}}/emit_preexpanded_cone_job.py
```
