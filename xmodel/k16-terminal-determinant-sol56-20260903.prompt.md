# Proof lane (the §8 target): TOP-TAIL-UNIT for all t ≥ 2 by the finite-quotient + determinant route, and RESIDUAL-ZERO by the axis recurrence — closing (8.1) on the K = 16 ray

Context (banked, AUDIT delta 17(zzz); read the charged Sol terminal report §2–§8):
the terminal family T_{t,k} = [X^k]σ_t(E_t) now has a closed coefficientwise
symbolic-t recurrence (2.2)–(2.13) (PROVED-HERE; verified through t = 6); (8.1)
⟨T_{t,0..2t−1}⟩ = [1] in A_t[b₃, b₄, u₂, …, u_{t−1}] is proved at t = 1..5 and half
at t = 6; §8 names the cheapest proof target: (a) TOP-TAIL-UNIT (b₄ = 1 chart): prove
that a selected (t−1)-row subideal J_t of the top-tail rows has FINITE quotient
A_t[b₃, u]/J_t (a triangular / zero-dimensional structure uniform in t), then
compute the determinant of multiplication by the omitted row on that finite
quotient as a recurrence in t, with its resultant against 3d² − (t+1) — a
nonzero value for every integer t ≥ 2 proves the chart unit; (b) RESIDUAL-ZERO
(b₄ = 0 chart): specialise b₄ = 0 in the recurrence before expanding and derive
the successive one-variable coefficients modulo (b₃, u_{t−1}, …, u_{j+1}) — §6.1
finished the b₃-axis for all t ≥ 3, §6.3 gives the exact recurrence for the
next axis; execute it in coefficient pairs, factor D(t) and the norm (6.6),
check integer roots. Task: do (a) and (b) as far as they go; for each,
either a full proof with every denominator listed and every specialisation
justified (split indices in the product algebra), or the exact remaining
statement (which axis / which determinant) with its cheapest test; verify
all uniform formulas at t = 2..6 against the charged records; controls: the
t = 2 base (RESIDUAL-ZERO false, band-zero row a unit) and the split index
t = 2, 11 in the product algebra; verdict: (T) on the ray for all t ≥ 1 PROVED,
or PARTIAL with the residual statement. FALLACY-v2 applies. ≤ 180 min; 4 cores;
no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-terminal-proof-fable5, k16-terminal-proof-opus5, k16-t11-modular, k16-t5-
replay, k16-t6, g9966-*, emitter-native). Drivers to box/k16det-20260903/.
Report: xmodel/k16-terminal-determinant-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 14-30KB; 180 minutes.
charged_input=xmodel/k16-terminal-proof-sol56-20260903.md
charged_input=xmodel/k16-middle-spine-sol56-20260903.md
charged_input=xmodel/k16-pivot-forms-grok46-20260903.md
charged_input=xmodel/k16-spine-gate-opus5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16terminal-sol56-20260903/top_tail_structure_audit.json
charged_input=box/k16terminal-sol56-20260903/artifact_summary.json
charged_input=box/k16terminal-sol56-20260903/terminal_t5_exact_none.json
charged_input=box/k16terminal-sol56-20260903/top_tail_audit_t4_p1009_b0.json
charged_input=box/k16terminal-sol56-20260903/top_tail_t3_exact.json
charged_input=box/k16terminal-sol56-20260903/top_tail_fast_t3_compare.json
charged_input=box/k16terminal-sol56-20260903/terminal_t3_exact_all.json
charged_input=box/k16terminal-sol56-20260903/top_tail_fast_recurrence.py
charged_input=box/k16terminal-sol56-20260903/claim_status.json
charged_input=box/k16terminal-sol56-20260903/top_tail_audit_t5_p1009_b0.json
charged_input=box/k16terminal-sol56-20260903/residual_b3_axis_exact_audit.json
charged_input=box/k16terminal-sol56-20260903/terminal_t6_exact_residual.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-terminal-determinant-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
401d374ecec0c556c7f7400ccade98571e1c1e93faf2daa1dd706f3b38c46391  {{LANE_INPUTS}}/k16-terminal-proof-sol56-20260903.md
c0b12fd69bc1209e2b63e3d823d6748cd83675b8c63d714880d2368d50f343c4  {{LANE_INPUTS}}/k16-middle-spine-sol56-20260903.md
7ac6fe7a70c93049367077a696f7349f396a42f3668ebcd206d4906d02f70f09  {{LANE_INPUTS}}/k16-pivot-forms-grok46-20260903.md
6d3bc222fedac1c0694346d53cb3caa59ad34824b8b14cdf3448708926af3a16  {{LANE_INPUTS}}/k16-spine-gate-opus5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
dab8296abbdbd46a75ae3076aa254ea667fe97fcb88f2389dd7de7299677f7c6  {{LANE_INPUTS}}/top_tail_structure_audit.json
b61f22871087a61e6422d3a3995d302f6d78a7d4f3f299f1944455d1bc9e627f  {{LANE_INPUTS}}/artifact_summary.json
4ed4a25f8e5b9b697272412544ccb62ee2fa05b449a75924d284504d8d82a083  {{LANE_INPUTS}}/terminal_t5_exact_none.json
9b67cbdd4038c658490cfae5ebc1535aa9acd4bed12ba2256bd9f22510462acb  {{LANE_INPUTS}}/top_tail_audit_t4_p1009_b0.json
e134fc2869fd79be50729014e9a5f9dc33d32b3411e2e230e63a684febc90ece  {{LANE_INPUTS}}/top_tail_t3_exact.json
6e93de68102114fa42acc6e75c8afcea2e267269736f9a4e6e2602ad311a94c9  {{LANE_INPUTS}}/top_tail_fast_t3_compare.json
ec5b8b12020daee45e28ee6db70145806ebd36c47f260ffafcfddbe70f5e1963  {{LANE_INPUTS}}/terminal_t3_exact_all.json
b6b1db68b89685d7d98828299d2128c47381b361e94c5b2c7ba049d8907429a3  {{LANE_INPUTS}}/top_tail_fast_recurrence.py
ae9ba31352e364d90118a431017886a6edeac0cad639e996ec85d5385d2f8f7d  {{LANE_INPUTS}}/claim_status.json
eff6b6596c191dd0fe908ee39b8c96115c88be21d9df243b07a5b296afeb7bad  {{LANE_INPUTS}}/top_tail_audit_t5_p1009_b0.json
ac1458cffe3eba1e210a3a90af866c30d0d9ee72a2777faf5c242c25500e8df6  {{LANE_INPUTS}}/residual_b3_axis_exact_audit.json
9c0f529d60f944b952281570e9408989de560a915a4438640955cc44af6e3140  {{LANE_INPUTS}}/terminal_t6_exact_residual.json
```
