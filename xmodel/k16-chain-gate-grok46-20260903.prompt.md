# Hostile gate (no long jobs): the tail-of-chain theorems of AUDIT delta 17(nnnn) (Opus) on the K = 16 terminal cone — Lemma CHAIN, Theorem Q-PLANE (eight closed-form units for t ≥ 3; √(I_{t,+}|_S) = (q_{t−1,0}, b₃) on S = {b₄ = q_{2,0} = … = q_{t−2,0} = 0}), Lemma UNIQUE-POWER (for t ≥ m(1+r), q_{t−r,0}^m is the only monomial of weight m(t−r) in the chain residual), the r = 1..5 chain steps (C_{t−r}) for t ≥ 3R + 3, and the PROVED failure of the initial-form upgrade (dim⟨in_w(gens)⟩ = 2, 3, 3, 4 at t = 4..7)

Rules: every CAS check in the FOREGROUND with `timeout 600` (sympy/Singular;
these are symbolic identities and small exact computations — no background
jobs; never end the turn with a job running). Charged: the Opus report with
its drivers (sq_engine.py etc.), the Sol spine/terminal reports (the
recurrence), the cone gate (17(jjjj)). Task: (1) Lemma CHAIN: re-prove the
equivalence (dim I = 0 ⇔ an ordering v₁..v_n with v_i ∈ √(I + (v₁..v_{i−1}))) for a
weighted-homogeneous ideal over the algebra A_t (both directions; note the
split-index product-algebra case); confirm that a sub-chart statement is a
TAIL step and that the head (b₄) cannot be reached by sub-charts (the
argument, not the slogan); (2) Theorem Q-PLANE: re-derive symbolically in t
the five scalars, the eight surviving (band, monomial) coefficients on S, and
their unit-ness (norms Res_y(H_t, ·) as polynomials in t; integer roots), and
the two closed forms T_{t,2t−1}|_S = α_t b₃², T_{t,t+4}|_S = A₂ q_{t−1,0}³; check on
the exact records t = 3, 4, 5 (charged JSON); (3) Lemma UNIQUE-POWER: prove it
(the weight arithmetic) and check the index ranges; (4) the r = 1..5 steps:
replay the closed forms A₂^{(1..5)} and HYP(1)..HYP(5); (5) the initial-form
failure: reproduce dim⟨in_w(gens)⟩ at t = 4, 5 (small exact std); (6) verdict
per item CONFIRMED / GAP / REFUTED; type every claim; FALLACY-v2 applies.
≤ 75 min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress
lane reports (k16-toptail-quadratics-fable5, k16-t6-sol56, k16-t11-cone, order-
chart-general, g9966-*). Drivers to box/k16chaingate-20260903/.
Report: xmodel/k16-chain-gate-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-14KB; 75 minutes.
charged_input=xmodel/k16-subchart-q-opus5-20260903.md
charged_input=xmodel/k16-cone-gate-gpt55-20260903.md
charged_input=xmodel/k16-terminal-proof-sol56-20260903.md
charged_input=xmodel/k16-middle-spine-sol56-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16subchart-20260903/s8_plane_dim.py
charged_input=box/k16subchart-20260903/s7_initial.py
charged_input=box/k16subchart-20260903/s10_unique.py
charged_input=box/k16subchart-20260903/fixed_r1.json
charged_input=box/k16subchart-20260903/s5_engine_control.py
charged_input=box/k16subchart-20260903/s6_axes.py
charged_input=box/k16subchart-20260903/s11_ansatz_range.py
charged_input=box/k16subchart-20260903/sq_engine.py
charged_input=box/k16spine-20260903/terminal_laurent_t4.json
charged_input=box/k16spine-20260903/terminal_laurent_t5.json
charged_input=box/k16spine-20260903/terminal_laurent_t3.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-chain-gate-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
918b561a8e5a22a763e82a2a6319846eabc582b4fc04cf3cf7dbfd0a9783c784  {{LANE_INPUTS}}/k16-subchart-q-opus5-20260903.md
444d1a9f5194f764ec7073d990f42d7c014b2c311431f84805015f2bdefcb080  {{LANE_INPUTS}}/k16-cone-gate-gpt55-20260903.md
401d374ecec0c556c7f7400ccade98571e1c1e93faf2daa1dd706f3b38c46391  {{LANE_INPUTS}}/k16-terminal-proof-sol56-20260903.md
c0b12fd69bc1209e2b63e3d823d6748cd83675b8c63d714880d2368d50f343c4  {{LANE_INPUTS}}/k16-middle-spine-sol56-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
8af58a59328dbde0b4a0626f315be9f0c588a6548e748bc0858722a865046eb4  {{LANE_INPUTS}}/s8_plane_dim.py
340ae13169dce039a4f948e8217e62e8e9062c1aa84854468bc2ef38e4be4dab  {{LANE_INPUTS}}/s7_initial.py
b83dcbbb436fe025d90901b7613eb9c476bb3449ab8c459826fa3c65d99316a7  {{LANE_INPUTS}}/s10_unique.py
de9c6b078e9e1a93f511efb437dc4339faa9e09417df44d3e1579b1f10013eff  {{LANE_INPUTS}}/fixed_r1.json
266db765b6b50fe11c313d48152b68ec65aa3d5a6e011a4f03575c026d843154  {{LANE_INPUTS}}/s5_engine_control.py
6bb9fc94431ac3a046cdd83a4a0e10aa6942506a05fd8734d112ba672d6e3028  {{LANE_INPUTS}}/s6_axes.py
16ae91a6f758c90149336ebd4093888a961f67412bfc87d24bd048d583985f7e  {{LANE_INPUTS}}/s11_ansatz_range.py
dfeeb494f2fc16ed183d2c1251e892e676f492204f5d0b9056eaecaa6cb6876f  {{LANE_INPUTS}}/sq_engine.py
0c6adb555b07624bac34ed2862ea259a4258f099d54a84f09d5b3824bda5858a  {{LANE_INPUTS}}/terminal_laurent_t4.json
f68a4666afb25490ceb62ec2b2f9ebe9b22b61c415cbf66edc074eb50a650689  {{LANE_INPUTS}}/terminal_laurent_t5.json
6490d1923d8a14652d36ef77e47a2122410f30f6137a44b28af9807ca076b926  {{LANE_INPUTS}}/terminal_laurent_t3.json
```
