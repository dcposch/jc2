# Instrument lane: a FAST emitter for the corrected two-point order charts — build the h-adic Jacobian coefficient systems inside Singular (or with a compiled polynomial library) instead of sympy, validate it byte-for-byte against the existing charts, then run the (25,15; 21; 2; k = 2) strata (135–137 unknowns) and the seven (24,16; 17; 2; k = 5) strata (273–276)

Context (banked, AUDIT delta 17(kkk)): with the corrected support rule (h: −i + δ₁'j ≥
V₂'δ₁' + u'δ₂'; β: deg_x ≤ k+1) and symbolic top-face slopes, the seven large open
two-point rows at D ≤ 200 have 135–276 unknowns per stratum, and the sympy
builder (box/bigrows-20260903/preprocess.py, charged; box/chartfix-20260903/,
charged) exceeds 600 s per stratum before emitting a system — the blocker is
the emitter, not Gröbner. The preprocessing that follows (Q*-pivots, grading,
torus slice, field pass) is validated (K = 16 t = 3: 36 → 23 → 6 rows → [1] in
0.07 s). Task: (1) write box/emitter-20260903/emit_chart.py + emit_chart.sing:
given (n', m', M₂', V₂', k, top-face partition with symbolic slopes), generate
the approximate-root tower, the coefficient spaces (corrected rule), and the
Jacobian coefficient equations by doing the polynomial arithmetic in
Singular (ring with the unknowns and x, y; construct h, A, B, f, g as
polynomials; compute J(f,g) − c·x^k; extract coefficients by `coeffs`/`coef`
in x, y; emit the ideal) — or with python-flint / a compiled multivariate
library if available (check `python3 -c "import flint"`); include the deg_x J
sanity gate and the Ω non-degeneracy saturation; (2) VALIDATE: on (16,12; 13;
3; 1), (28,20; 25; 3; 1) [must give 27 unknowns / 37 equations and the same
ideal up to ordering as the charged t2_order_system — compare Gröbner bases
or normal forms, not text], (33,22; 30; 8; 1) strata [3], [2,1] (28/29
unknowns, 62 equations, [1]) — report timings; (3) run (25,15; 21; 2; 2) strata
[3], [2,1], [1,1,1] (135–137 unknowns): emit, then modular standard basis over
three primes (≤ 20 min each; up to 4 cores), then the preprocessing chain and
exact where it finishes; then the (24,16; 17; 2; 5) strata in order of unknown
count; report per stratum: emit time, unknowns/equations, deg_x J, modular
verdicts, exact verdict / COUNTING-BOUND with the blocker; (4) verdict + what
the emitter enables next (the remaining five large rows; the joint (99,66)
systems); type every claim; FALLACY-v2 applies. ≤ 150 min; no ledger edits;
no jc2-lean; no ideation-* files; no in-progress lane reports (r3-preprocess,
g9966-*, k16-*). Drivers to box/emitter-20260903/.
Report: xmodel/emitter-native-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 150 minutes.
charged_input=xmodel/bigrows-preprocess-gpt55-20260903.md
charged_input=box/bigrows-20260903/preprocess.py
charged_input=xmodel/chart-fix-d1zero-gpt55-20260903.md
charged_input=box/chartfix-20260903/shape.py
charged_input=box/chartfix-20260903/twopoint_order_batch.py
charged_input=xmodel/topface-license-sol56-20260903.md
charged_input=box/topface-20260903/topface_cases.py
charged_input=box/k16T-drivers-20260903/t2_order_system.py
charged_input=box/k16t2-gate-20260903/t2_independent_order_system.py
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/emitter-native-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
3f994067f8149636fc81e57e98122261dc1435d4c0ac77f266893e58646c5273  {{LANE_INPUTS}}/bigrows-preprocess-gpt55-20260903.md
67b3735d27d8b92af2bf091566a14f9b2f49163577f51d54da751a76d22b2f2a  {{LANE_INPUTS}}/preprocess.py
0a8d1ba229ffeee3b8c6e89b103c35f5f57154c8be93edf3c06c8b498d200d4f  {{LANE_INPUTS}}/chart-fix-d1zero-gpt55-20260903.md
ba25cd10fa5cc998017688db455094bcd3b7a8e870085dd2db64fb4f66b098de  {{LANE_INPUTS}}/shape.py
16497553047222b6b16450f26286a65dc69b27b4c00f8fcd518f0cce0af6c8e5  {{LANE_INPUTS}}/twopoint_order_batch.py
53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae  {{LANE_INPUTS}}/topface-license-sol56-20260903.md
369bafb1341f96708f6886e79c93fb9bdad8e70abb1ae4c69ddd1dd6a9c62082  {{LANE_INPUTS}}/topface_cases.py
55067a8c74d6c360c72aaa40243dde7e8e1a804158b3c78abf523d77a25cb5e2  {{LANE_INPUTS}}/t2_order_system.py
7ee7e29eca86dadecf4cffdc996539fc875851ce5803ad7ddaf68b888624f823  {{LANE_INPUTS}}/t2_independent_order_system.py
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
