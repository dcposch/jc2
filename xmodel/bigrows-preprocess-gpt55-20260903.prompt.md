# Batch lane: apply the triangular / weighted-torus / field-normalisation preprocessing (which reduced the K = 16 t = 3 chart from a 36-unknown Gröbner timeout to an exact [1] in 0.04 s) to the six LARGE open two-point rows at D ≤ 200 — (25,15; 21; 2; k = 2), (35,20; 31; 2; 2), (35,25; 31; 3; 2), (30,24; 25; 4; 3), (49,14; 46; 4; 1), (50,30; 47; 7; 1) — and to the unfinished strata of (24,16; 17; 2; 5)

Context (banked): under the operative screen the two-point s_eff = 2, u_s = 1
residue at D ≤ 200 is 17 groups; 7 are dead (deltas 17(oo), (vv), (ww) and Moh),
3 await honest charts (δ₁' = 0 rows; chart-fix lane running), and the six
rows above are COUNTING-BOUND because their symbolic partition strata
(topface-license-sol56 §5.2, charged: faces H = y^{V₂'}Π(y − a_i x)^{e_i} with
symbolic slopes, 143–228 unknowns in the D1-only count) exceed direct Gröbner.
The K = 16 t = 3 certificate (k16-t3-uniform-sol56 + k16-t3-gate-gpt55, charged)
succeeded by: (i) a first pass of quotient-ring isomorphisms using only Q*
pivots (affine-linear rows solved for distinct variables, verified inverses);
(ii) observing that the residual rows are homogeneous for a positive weight
grading and that c ≠ 0 forces a chosen variable nonzero, so the weighted
torus action (an automorphism of the saturated locus over Q̄) sets it to 1;
(iii) a univariate polynomial H(y) then appears; passing to K = Q[y]/(H)
(covering all conjugates), the rest triangularises and the final small
system is [1] in milliseconds. Task: (1) build a REUSABLE preprocessing
driver (box/bigrows-20260903/preprocess.py) implementing (i)–(iii) generically:
detect Q*-pivot affine rows and eliminate; solve the positive-grading LP for
the residual; identify a variable forced nonzero on c ≠ 0 (from the
generators: a generator of the form c − (monomial)·(unit) or the Jacobian's
leading coefficient); scale; factor the univariate base equation; work over
Q[y]/(factor) for EACH irreducible factor (all conjugates covered); saturate
by slopes' non-degeneracy ideal and c; record every step so a hostile reader
can verify the chain of quotient-ring isomorphisms (print the covering
argument as in the charged gate §4); (2) controls: the t = 3 K = 16 chart must
reproduce (36 → residual → K quadratic → [1]); the actual pair (π, π − γ²/2)
must fail the tuple; wrapper controls in every ring; (3) run the driver on
the strata of the six rows (use the charged topface driver box/topface-
20260903/topface_cases.py to emit each stratum's system with the CORRECTED
support rule of delta 17(uu): ord h(σ₁) ≥ V₂'δ₁' + u'δ₂' and deg_x β ≤ k+1 —
implement that correction in your emitter and PRINT deg_x J on the generic
ansatz as a sanity gate (must reach k); order the strata by unknown count;
≤ 20 min per stratum, 2 cores; modular first (three primes) when exact is
slow); table per stratum: unknowns before/after preprocessing, grading
weights, H degree/factors, verdict (SATURATED-EMPTY with the covering chain
/ SURVIVES with a point and a direct Jacobian check, REPRESENTATIVE /
COUNTING-BOUND with what blocked); (4) also run the four unfinished strata
of (24,16; 17; 2; 5) ([3,1,1,1], [2,2,2], [2,1,1,1,1], [1⁶]) and the three that
timed out ([4,1,1], [3,2,1], [2,2,1,1]); (5) verdict per ROW (all strata dead
→ SATURATED-EMPTY for the row; else list the surviving/open strata) and the
resulting tally; type every claim; FALLACY-v2 applies. ≤ 150 min; no ledger
edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-uniform-structure, moh9966-branchB, chart-fix-d1zero). Drivers to
box/bigrows-20260903/.
Report: xmodel/bigrows-preprocess-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 150 minutes.
charged_input=xmodel/k16-t3-gate-gpt55-20260903.md
charged_input=xmodel/k16-t3-uniform-sol56-20260903.md
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=box/k16t3-20260903/preprocessed/t3_normalized_slice.py
charged_input=box/k16t3-20260903/t3/t_order_system.py
charged_input=xmodel/topface-license-sol56-20260903.md
charged_input=box/topface-20260903/topface_cases.py
charged_input=box/topface-20260903/case_counts.json
charged_input=xmodel/strata-gate-gpt55-20260903.md
charged_input=box/strata-gate-20260903/strata_gate.py
charged_input=xmodel/twopoint-kills-gate-fable5-20260903.md
charged_input=box/twopoint-batch-20260903/twopoint_order_batch.py
charged_input=box/twopoint-batch-20260903/shape.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/bigrows-preprocess-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
5593aa5443dd755cadedca4b0d284a3dec4048f7cd5822da576587552f36aba6  {{LANE_INPUTS}}/k16-t3-gate-gpt55-20260903.md
f16dc4bcb7183bf2e699981dce639d3e824b7b63457189de1f2d98172501fa20  {{LANE_INPUTS}}/k16-t3-uniform-sol56-20260903.md
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7  {{LANE_INPUTS}}/t3_normalized_slice.py
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae  {{LANE_INPUTS}}/topface-license-sol56-20260903.md
369bafb1341f96708f6886e79c93fb9bdad8e70abb1ae4c69ddd1dd6a9c62082  {{LANE_INPUTS}}/topface_cases.py
b8ce67b93c105b62966d9003583da2c7dec302125cf79862f16f5b54513d3861  {{LANE_INPUTS}}/case_counts.json
4a2e31602ced3fe8799195ec9cb5cbb29fa0ba23f57e0df4d0403cc4a53ba36b  {{LANE_INPUTS}}/strata-gate-gpt55-20260903.md
e0e84581323f97bdee0df10290440548ed4474178cfaafebbd28e5e172df0898  {{LANE_INPUTS}}/strata_gate.py
d68d13f6078172e955e9e987e60bd145e81ee0069c8b4f16181e64f7a558b681  {{LANE_INPUTS}}/twopoint-kills-gate-fable5-20260903.md
db14cb1ef39da6277ec4edcd9988a17d38d8bc0062edca244af1155b820282eb  {{LANE_INPUTS}}/twopoint_order_batch.py
d8750d4e512645366e9e0c53153484eb5daa9c785434c1cc59658986d0ab138c  {{LANE_INPUTS}}/shape.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
