# STRUCTURAL proof lane (fixed-t is EXHAUSTED, 17(mmmmm)/(yyyy); the K16 ray needs an ALL-t Gröbner-free argument): prove that the terminal tail T_{t,t..2t−1} is a homogeneous system of parameters (equivalently a regular sequence / complete intersection) of S_t = A_t[b₄, q_{2,0..t−1,0}, b₃] for EVERY t ≥ 3, by deriving its complete-intersection LENGTH L_t = 2·binom(3t+1, t−1) = ∏_{d=2t+2}^{3t+1} d / ((t−1)!(t+1)) combinatorially from the CLOSED INDEXED FORMS of T_{t,k} (banked: 17(zzz) §2, 17(iiii) §2 — T_{t,k} = −[w^{4t+1−k}]σ_t(Δ), the spine substitution) and the weighted degrees (T_{t,t+j} has weighted degree 2t+2+j, j = 0..t−1; variables b₄, q_{2,0..t−1,0}, b₃ of weights 1, 2..t−1, t+1), and showing this equals the actual vector-space dimension for all t (hence dim = 0, hence (V0), hence (8.1)+(T) on the whole ray)

Context (banked, ALL of it usable): (V0) is proved t = 1..7 (17(mmmm)); the length is MEASURED-EXACT at t = 3, 4, 5, 6 (90, 572, 3640, 23256) on both fibres (17(vvvv), 17(mmmmm)); the literal "top t + 2 rows regular" is IMPOSSIBLE (17(vvvv)) but a corrected tail IS regular at t = 3..6; the tail is the b₃-elimination of nothing — it IS the t rows T_{t,t..2t−1}; the properness lemma (17(kkkk)) turns a modular length into a char-0 statement ONLY for the dim = 0 conclusion. STRATEGY (desk algebra, minimal CAS): (1) write T_{t,t+j} in the closed indexed form and extract its LEADING FORM in the weighted order wp(1, 2, …, t−1, t+1) symbolically in (t, j) — is the leading monomial a pure power of a single variable, or a product? (the round's Opus V4 and Fable E2 say the naive leading-form ideal is NOT zero-dimensional, so the tail is NOT a coprime-leading-monomial CI in the obvious order — find the RIGHT order or the RIGHT generators); (2) attempt the Fröberg/complete-intersection Hilbert-series identity: the tail is a regular sequence iff its Hilbert series is ∏_j(1 − s^{deg T_{t,t+j}}) / ∏_i(1 − s^{w_i}); prove the numerator-denominator cancellation leaves a polynomial with nonnegative coefficients summing to L_t (a combinatorial identity in t) — either by a bijection/generating-function argument or by exhibiting a regular sequence explicitly (a triangular change of generators making the leading terms coprime powers); (3) if a full regular-sequence proof is out of reach, prove the WEAKER sufficient statement for (V0): the tail has FINITELY many zeros (dim 0) for all t, via a resultant/elimination bound or a Bezout-type argument on the weighted degrees that is UNIFORM in t (the length L_t = 2·binom(3t+1, t−1) is the exact CI count — a dim-0 proof need only bound, not compute, it); (4) the t = 2, y = 1/5 obstruction MUST appear as the boundary case (dim I_{2,+} = 1 there): show your argument's hypothesis fails exactly at t = 2, y = 1/5 and holds for t ≥ 3 (or t = 2, y = 2/5); (5) verdict: (V0) FOR ALL t ≥ 3 PROVED (structural, Gröbner-free) with the full dependency chain to (T) / PARTIAL with the exact residual combinatorial identity and its t-range of verification. Desk CAS only (sympy/generating functions, foreground, ≤ 10 min per job); ≤ 180 min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports. Drivers to box/k16hsop-20260903/.
Report: xmodel/k16-hsop-length-allt-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-40KB; 180 minutes.
charged_input=xmodel/k16-hilbert-regseq-sol56-20260903.md
charged_input=xmodel/k16-square-tail-stdhilb-gpt55-20260903.md
charged_input=xmodel/k16-toptail-quadratics-fable5-20260903.md
charged_input=xmodel/k16-dep-locus-fable5-20260903.md
charged_input=xmodel/k16-terminal-proof-fable5-20260903.md
charged_input=xmodel/k16-terminal-proof-sol56-20260903.md
charged_input=xmodel/k16-properness-gate-opus5-20260903.md
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-hsop-length-allt-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
69ea2475c0471ff2254d39d177f35029068d31fea53b29ba7bd35565ec9c29e7  {{LANE_INPUTS}}/k16-hilbert-regseq-sol56-20260903.md
9b42f72d9d04b404865ab28fe9374839fe0a65a961620007a686e0fb22596afa  {{LANE_INPUTS}}/k16-square-tail-stdhilb-gpt55-20260903.md
638f5e2ed6755b32b92944830e32f6b4a67d321a9e442adca9a59f2f4ba5b05c  {{LANE_INPUTS}}/k16-toptail-quadratics-fable5-20260903.md
d564bc5c5b35a95ee146bca73e67f260e9b70600c9d6f9c931ae17263af085ae  {{LANE_INPUTS}}/k16-dep-locus-fable5-20260903.md
16d5112ae6ed9a6de0c504b11df2e19c97ed031a1715a3916fd8d207cdf0d961  {{LANE_INPUTS}}/k16-terminal-proof-fable5-20260903.md
401d374ecec0c556c7f7400ccade98571e1c1e93faf2daa1dd706f3b38c46391  {{LANE_INPUTS}}/k16-terminal-proof-sol56-20260903.md
f4d071a18cff25c4bdade4508f53c58bc39d20a26907fa619410622bfb91ccf6  {{LANE_INPUTS}}/k16-properness-gate-opus5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
