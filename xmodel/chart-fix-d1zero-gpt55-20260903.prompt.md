# Instrument-fix + re-attack lane: repair the two-point chart generator's support rule (Theorem-1.2 threshold ord h(σ₁) = V₂'δ₁' + u'δ₂', deg_x β ≤ k+1, and a mandatory level-1 ODE sanity gate: deg_x J must reach k before saturation), then re-attack the three δ₁' = 0 rows (21,14; 15; 6; k = 4), (24,16; 18; 7; k = 4), (27,18; 21; 8; k = 4) via the level-1 ODE chart R3 (31 unknowns) and the honest chart (98 unknowns)

Context (banked, AUDIT delta 17(uu)): Fable's gate (charged) showed the batch
generator's support rule (shape.py: x^i y^j ∈ h iff −i + δ₁'j ≥ −δ₁') is wrong
whenever u'(Π+1) ≠ (k+1)(V₂'+1); at δ₁' = 0 it deletes every x-term of h
below the top face and caps deg_x β ≤ 1, so J cannot reach x⁴, −c is a
generator and the "kills" were vacuous slices; the correct threshold is
ord h(σ₁) = V₂'δ₁' + u'δ₂' (Theorem 1.2 / root count; Moh p.149) and Theorem
1.2 allows deg_x β ≤ k+1; the x^k-coefficient of J is exactly Moh's r = 1 ODE
D(n', −M₁', ḡ_σ, T_{1,σ}) = nonzero constant (p.187), which survives J = cγ^k
(delta 17(ff)). Fable's honest chart for (21,14; 15; 6; 4) has 98 unknowns /
159 equations; its level-1 ODE chart R3 alone has 31 unknowns / 29 equations;
both timed out in that lane's budget; the drivers are charged (box/twopoint-
gate-20260903/indep/). Task: (1) FIX the generator: copy twopoint_order_batch.py
and shape.py to box/chartfix-20260903/, implement the Theorem-1.2 threshold
and the deg_x β ≤ k+1 cap, and add a SANITY GATE that, before any saturation,
computes deg_x J symbolically on the generic ansatz and REFUSES to run (verdict
INSTRUMENT-FAIL) unless it reaches k; re-run the four Moh controls (must
still be [1]; report whether their charts changed) and the actual pair
(π, π − γ²/2) control; (2) verify on the five non-zero-δ₁' batch kills
((16,12; 13; 3; 1), (15,10; 11; 3; 2), (21,14; 18; 5; 1), (33,22; 30; 8; 1),
(45,30; 42; 11; 1)) that the corrected chart is a superset of / equal to the
old one and that the kills persist ([1]) — or report which change;
(3) RE-ATTACK the three δ₁' = 0 rows: (a) R3 (level-1 ODE chart, 31 unknowns)
with slimgb / modStd / an elimination order, modular first, ≤ 30 min each —
an empty R3 re-kills all three at level 1 (Moh Appendix I: D(21,14; p, q) = c
with deg (18,12)); (b) the honest 98-unknown chart modular over one prime
with a 30-min cap; (c) if R3 survives, print the R3 solution set's dimension
and a point; (4) verdict per row (SATURATED-EMPTY with certificate / SURVIVES
at level 1 (REPRESENTATIVE, not a pair) / COUNTING-BOUND) and the corrected
tally of the 17-group list; type every claim; FALLACY-v2 applies (report the
sanity gate's deg_x J for every system you run). ≤ 120 min; 2 cores; no
ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-t3-gate, strata-gate, k16-uniform-structure, moh9966-branchB). Drivers
to box/chartfix-20260903/.
Report: xmodel/chart-fix-d1zero-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 120 minutes.
charged_input=xmodel/twopoint-kills-gate-fable5-20260903.md
charged_input=xmodel/twopoint-batch-gpt55-20260903.md
charged_input=box/twopoint-batch-20260903/twopoint_order_batch.py
charged_input=box/twopoint-batch-20260903/shape.py
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=xmodel/k16-t2-gate-gpt55-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/twopoint-gate-20260903/gate_chart.py
charged_input=box/twopoint-gate-20260903/gate_ode.py
charged_input=box/twopoint-gate-20260903/gate_sing.py
charged_input=box/twopoint-gate-20260903/parents/moh_skeleton_full.py
charged_input=box/twopoint-gate-20260903/indep/R1b_27_18_21_8_k4_Q.sing
charged_input=box/twopoint-gate-20260903/indep/R0_batch_ab_forced_21_14_15_6_k4_Q.sing
charged_input=box/twopoint-gate-20260903/indep/R1b_21_14_15_6_k4_Q.sing
charged_input=box/twopoint-gate-20260903/indep/R1a_corrH_ab_forced_21_14_15_6_k4_mod32003.sing
charged_input=box/twopoint-gate-20260903/indep/R2_21_14_15_6_k4_Q.sing
charged_input=box/twopoint-gate-20260903/indep/R1b_24_16_18_7_k4_Q.sing
charged_input=box/twopoint-gate-20260903/indep/R0_batch_ab_forced_21_14_15_6_k4_mod32003.sing
charged_input=box/twopoint-gate-20260903/indep/R2_24_16_18_7_k4_mod32003.sing

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/chart-fix-d1zero-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
d68d13f6078172e955e9e987e60bd145e81ee0069c8b4f16181e64f7a558b681  {{LANE_INPUTS}}/twopoint-kills-gate-fable5-20260903.md
52ac2f50b9c14b258b706cef4e931ca9afa1057dc542f64003c8df43a14c8a1b  {{LANE_INPUTS}}/twopoint-batch-gpt55-20260903.md
db14cb1ef39da6277ec4edcd9988a17d38d8bc0062edca244af1155b820282eb  {{LANE_INPUTS}}/twopoint_order_batch.py
d8750d4e512645366e9e0c53153484eb5daa9c785434c1cc59658986d0ab138c  {{LANE_INPUTS}}/shape.py
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
692fd869d8a11b3a984d1fe8c4ccb4b42de7326567c130b8babae1571ca6e863  {{LANE_INPUTS}}/k16-t2-gate-gpt55-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
630faf3c7a01864fd44d921e13fbd63c56c58a5867638bdbc7d27cb084625526  {{LANE_INPUTS}}/gate_chart.py
2db62d52d65354c16c224f14fbde64c1f40f4366a77968c6365cd021b28f4ecf  {{LANE_INPUTS}}/gate_ode.py
b9b06d6196a60101feebf9885d519b2cd26fea5f96229f4da2cb2e1dceb72894  {{LANE_INPUTS}}/gate_sing.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
66758f92f46122f4b9c494f8e155c29d6e4df7cd5308646918502e6438bc8095  {{LANE_INPUTS}}/R1b_27_18_21_8_k4_Q.sing
d02b440f2115dbcd2516d7df4b72c1e56e97eea7d54e292e0afe8c941edd2d19  {{LANE_INPUTS}}/R0_batch_ab_forced_21_14_15_6_k4_Q.sing
6627ffdc281ef647e92bb9b369b1cea32dde64534029265dd6eb80feb5859a92  {{LANE_INPUTS}}/R1b_21_14_15_6_k4_Q.sing
dc5f3c2297fdf6fc16d9be6addc49f2576576d2a93bf8f6c9a787e4e80e0ea37  {{LANE_INPUTS}}/R1a_corrH_ab_forced_21_14_15_6_k4_mod32003.sing
3eb27a68f81950446f833e3f1203c4ebe087ff90c3cd2fda51d4fa40c3993280  {{LANE_INPUTS}}/R2_21_14_15_6_k4_Q.sing
81f4bb0fa0fb050bc8167505a42de8e8aa9cfc854c62de60491a21ebb2a1e79f  {{LANE_INPUTS}}/R1b_24_16_18_7_k4_Q.sing
a8fb2b6e7be42b82b1f03ca0ac93b1bc3ac8abf6fc3de099007292ae622cbb19  {{LANE_INPUTS}}/R0_batch_ab_forced_21_14_15_6_k4_mod32003.sing
9a9927899bcb6d0b319a7cc8d10ba7667a79e89918c644dfae85d3f389d4de3b  {{LANE_INPUTS}}/R2_24_16_18_7_k4_mod32003.sing
```
