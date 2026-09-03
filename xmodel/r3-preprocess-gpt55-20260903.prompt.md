# Computation lane: the three δ₁' = 0 two-point rows — (21,14; 15; 6; k = 4), (24,16; 18; 7; k = 4), (27,18; 21; 8; k = 4) — attack the level-1 ODE chart R3 (31 unknowns, 29 equations, deg_x J = 4) and the honest Theorem-1.2 chart with the triangular / weighted-torus / field-normalisation preprocessing that closed the K = 16 t = 3, 4 charts in milliseconds

Context (banked, AUDIT deltas 17(uu), (bbb)): the A/B ansatz cannot represent
these rows (deg_x J = 2 < 4: INSTRUMENT-FAIL, correctly); Fable's honest chart
has 98 unknowns / 159 equations; the level-1 ODE chart R3 — Moh's r = 1 ODE
D(n', −M₁', ḡ_σ, T_{1,σ}) = nonzero constant (p.187) in the descended
coordinates, i.e. the x⁴-coefficient of J — has 31 unknowns / 29 equations and
timed out four ways at 1800 s (slimgb dp/elim over GF(32003) and Q; modStd
aborted). Empty R3 re-kills all three rows at level 1 (the necessary level-1
datum). The K = 16 charts at t = 3 (36 unknowns) and t = 4 (45) were closed by:
Q*-pivot affine eliminations → positive weight grading of the residual →
torus slice (a variable forced nonzero by c ≠ 0) → univariate base polynomial
→ number field → triangular elimination → [1] (charged: triangular_preprocess.py,
the t = 3 and t = 4 gate reports §4 covering arguments). Task: (1) take Fable's
R3 systems (charged R3ode_*.sing and gate_ode.py in box/twopoint-gate-
20260903/indep and box/chartfix-20260903/indep) — verify deg_x J = 4 on the
generic ansatz — and apply the preprocessing: eliminate affine Q*-pivot rows,
solve the positive-grading LP, identify the forced-nonzero variable, slice,
factor the base polynomial, work over each irreducible factor's field,
saturate by c and by the leading coefficients you divided by (record every
pivot's norm/resultant so the reduction is a covering chain as in the K = 16
gates §4), and run the final system (Singular; modular then exact); do this
for all three rows; (2) if R3 is EMPTY for a row, that row is SATURATED-EMPTY
at level 1 (state the theorem: no monomial-Jacobian pair with the descended
datum satisfies Moh's r = 1 ODE with the required constant) — give the
certificate; if R3 has a solution component, print its dimension and a point
and continue to the honest 98-unknown chart with the same preprocessing on
that component (≤ 30 min per row); (3) controls: the preprocessing must
reproduce the t = 3 K = 16 result ([1]) and the actual pair (π, π − γ²/2) must
pass the level-1 ODE and fail the tuple; wrapper controls; (4) verdict per
row; type every claim; FALLACY-v2 applies (a kill after an unjustified pivot
division is a slice — every division must be by a proven unit or branch on
zero). ≤ 120 min; 2 cores; no ledger edits; no jc2-lean; no ideation-* files;
no in-progress lane reports (bigrows-preprocess, strata-rerun-corrected, k16-
middle-spine, moh9966-B-lift, xu-screen-gate). Drivers to box/r3pre-20260903/.
Report: xmodel/r3-preprocess-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-16KB; 120 minutes.
charged_input=xmodel/chart-fix-d1zero-gpt55-20260903.md
charged_input=xmodel/twopoint-kills-gate-fable5-20260903.md
charged_input=box/twopoint-gate-20260903/gate_ode.py
charged_input=box/twopoint-gate-20260903/gate_chart.py
charged_input=box/chartfix-20260903/shape.py
charged_input=box/chartfix-20260903/twopoint_order_batch.py
charged_input=xmodel/k16-t3-gate-gpt55-20260903.md
charged_input=xmodel/k16-t4-normalizer-gate-gpt55-20260903.md
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=FALLACY-v2.md
charged_input=box/twopoint-gate-20260903/indep/R3ode_21_14_15_6_k4_Q.sing
charged_input=box/twopoint-gate-20260903/indep/R3ode_21_14_15_6_k4_mod32003.sing
charged_input=box/twopoint-gate-20260903/indep/R3ode_24_16_18_7_k4_Q.sing
charged_input=box/twopoint-gate-20260903/indep/R3ode_24_16_18_7_k4_mod32003.sing

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/r3-preprocess-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
0a8d1ba229ffeee3b8c6e89b103c35f5f57154c8be93edf3c06c8b498d200d4f  {{LANE_INPUTS}}/chart-fix-d1zero-gpt55-20260903.md
d68d13f6078172e955e9e987e60bd145e81ee0069c8b4f16181e64f7a558b681  {{LANE_INPUTS}}/twopoint-kills-gate-fable5-20260903.md
2db62d52d65354c16c224f14fbde64c1f40f4366a77968c6365cd021b28f4ecf  {{LANE_INPUTS}}/gate_ode.py
630faf3c7a01864fd44d921e13fbd63c56c58a5867638bdbc7d27cb084625526  {{LANE_INPUTS}}/gate_chart.py
ba25cd10fa5cc998017688db455094bcd3b7a8e870085dd2db64fb4f66b098de  {{LANE_INPUTS}}/shape.py
16497553047222b6b16450f26286a65dc69b27b4c00f8fcd518f0cce0af6c8e5  {{LANE_INPUTS}}/twopoint_order_batch.py
5593aa5443dd755cadedca4b0d284a3dec4048f7cd5822da576587552f36aba6  {{LANE_INPUTS}}/k16-t3-gate-gpt55-20260903.md
e868a7f2df3814caf1847411918c17cbf8e71688779819fd4764d70e9d86ae83  {{LANE_INPUTS}}/k16-t4-normalizer-gate-gpt55-20260903.md
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
09aa99706819c08a433e1e21df94003865d2026787297168b0fa7ad6795500fa  {{LANE_INPUTS}}/R3ode_21_14_15_6_k4_Q.sing
719e094cbdc3fdd35b20c766755b5c826743082c2d5d012cf1f79c1760cd8752  {{LANE_INPUTS}}/R3ode_21_14_15_6_k4_mod32003.sing
0268e3d47b99c0892b89d229960648e95beeeb860a3d9ff2b37f0d4461fe38fb  {{LANE_INPUTS}}/R3ode_24_16_18_7_k4_Q.sing
af4a1cca33cd6bded366fcdb65a8eef63215a1365f024556889bbedde6f7cd3a  {{LANE_INPUTS}}/R3ode_24_16_18_7_k4_mod32003.sing
```
