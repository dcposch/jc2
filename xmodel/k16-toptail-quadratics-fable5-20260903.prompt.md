# THE HEAD OF THE CHAIN — the last statement on the K = 16 ray: prove (C0) b₄ ∈ √I_{t,+}, equivalently I_{t,+}|_{b₄=1} = (1) for every t ≥ 3, through the handle (7.1): on b₄ = 1 the top tail T_{t,t..2t−1} consists of t QUADRATICS in b₃ (with coefficients in A_t[q_{2,0}, …, q_{t−1,0}]) whose topmost has the UNIT leading coefficient α_t — a resultant / elimination problem in one variable b₃ over the q-ring, uniform in t

OPERATIONAL: write the report skeleton first; every CAS job in the foreground
with `timeout`; never end the turn with a job running; the box is loaded — use
≤ 2 cores. Context (banked, AUDIT deltas 17(cccc), (jjjj), (llll), (nnnn)): the
terminal cone I_{t,+} = ⟨T_{t,1..2t−1}⟩ ⊂ A_t[b₄, q_{2,0..t−1,0}, b₃] is weighted-
homogeneous (wt b₄ = 1, wt q_{j,0} = j, wt b₃ = t + 1); (T) at t ⇔ (8.1) ⇐ (V0)
dim I_{t,+} = 0; Lemma CHAIN: dim = 0 iff there is an ordering of the residual
variables with v_i ∈ √(I + (v₁..v_{i−1})); every TAIL step is proved uniformly
(Q-PLANE, UNIQUE-POWER, B3-AXIS: for t ≥ 3R + 3 the cone meets {b₄ = q_{2,0} = … =
q_{t−R−1,0} = 0} only at the origin, with explicit units) — the HEAD of the
chain, b₄ ∈ √I_{t,+}, is the whole b₄ = 1 chart and is not a sub-chart
statement; the sharpest handle (Opus 17(cccc) (7.1), re-stated 17(nnnn) §9): on
b₄ = 1 the top tail T_{t,t}, …, T_{t,2t−1} are t quadratics in b₃ whose topmost
T_{t,2t−1} has leading coefficient α_t, a unit of A_t for t ≥ 3; the closed
coefficientwise recurrence for T_{t,k} (Sol, charged) gives every coefficient
symbolically in t. Task: (1) from the charged recurrence, write the t
quadratics Q_k(b₃) := T_{t,t+k}|_{b₄=1} = a_k b₃² + b_k b₃ + c_k, k = 0..t−1, with
a_k, b_k, c_k ∈ A_t[q] in closed indexed form (which q_{j,0} appear in each,
with what weights: by homogeneity Q_k has weight t + k after setting b₄ = 1 …
— careful: b₄ = 1 breaks homogeneity; instead use the grading to bound the
q-monomials that can appear in each coefficient; list them); verify at t = 3..7
against the charged records; (2) the elimination: the resultants Res_{b₃}(Q_k,
Q_{2t−1−t}) and the subresultant structure — since a_{t−1} = α_t is a unit, b₃
is INTEGRAL over A_t[q]/(Q_{t−1}) and I|_{b₄=1} ∩ A_t[q] contains
Res_{b₃}(Q_{t−1}, Q_k) for every k; compute these resultants symbolically (each
is a polynomial in the q's with A_t-coefficients); show that the ideal they
generate, together with the lower rows T_{t,1..t−1}|_{b₄=1}, is the unit ideal —
strategy: find a chain in the q's analogous to the proved tail (the
resultants are weighted-quasi-homogeneous in the q's after the b₄ = 1
dehomogenisation with a shifted weight — check whether the q-grading survives:
if I_{t,+} is homogeneous and b₄ has weight 1, then I|_{b₄=1} is the
dehomogenisation and the q-ideal obtained is filtered, not graded; its
"top-weight part" is a homogeneous ideal in the q's alone whose emptiness of
cone would give the unit ideal — compute that top-weight part (the initial
forms with respect to the weight filtration) and test dim = 0 for t = 3..7
(cheap) and then uniformly by the same sub-chart machinery); (3) if (2) works
uniformly, assemble: (C0) for all t ≥ 3 ⇒ with the proved tail, dim I_{t,+} = 0
⇒ (V0) ⇒ (8.1) ⇒ (T) for all t ≥ 1 on the ray — write the full proof with every
denominator and the split indices; if not, deliver the sharpest partial
statement (e.g. (C0) for all t ≥ some t₀, or modulo one explicit unit test in
t) and the cheapest test; (4) controls: t = 2 (both fibres; note at y = 1/5 the
cone is the b₃-axis — (C0) must still hold there? check: b₄ ∈ √I at t = 2?), the
exact t = 3, 4 cones; FALLACY-v2 applies (denominators; split indices in the
product algebra; no sub-chart-to-full-radical fallacy). ≤ 180 min; no ledger
edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-t6-sol56, k16-t11-cone, g9966-*, preprocess-native). Drivers to
box/k16toptail-20260903/.
Report: xmodel/k16-toptail-quadratics-fable5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 14-30KB; 180 minutes.
charged_input=xmodel/k16-subchart-q-opus5-20260903.md
charged_input=xmodel/k16-terminal-proof-opus5-20260903.md
charged_input=xmodel/k16-terminal-proof-sol56-20260903.md
charged_input=xmodel/k16-b4-axis-sol56-20260903.md
charged_input=xmodel/k16-cone-gate-gpt55-20260903.md
charged_input=xmodel/k16-properness-gate-opus5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16subchart-20260903/sq_emit_dim.py
charged_input=box/k16subchart-20260903/sq_chart_model.py
charged_input=box/k16subchart-20260903/sq_load.py
charged_input=box/k16subchart-20260903/s12_symbolic_check.py
charged_input=box/k16subchart-20260903/s4_records_subchart.py
charged_input=box/k16terminal-sol56-20260903/singular_terminal_driver.py
charged_input=box/k16terminal-sol56-20260903/terminal_array_recurrence.py
charged_input=box/k16terminal-sol56-20260903/build_artifact_manifest.py
charged_input=box/k16terminal-sol56-20260903/validate_claim_artifacts.py
charged_input=box/k16b4-20260903/coeff-exact-axis.py
charged_input=box/k16b4-20260903/axis_exact.py
charged_input=box/k16b4-20260903/validate_axis_records.py
charged_input=box/k16spine-20260903/terminal_laurent_t2.json
charged_input=box/k16spine-20260903/terminal_laurent_t5_b4_1_exact_status.json
charged_input=box/k16spine-20260903/terminal_laurent_t4.json
charged_input=box/k16spine-20260903/terminal_laurent_t2_product_exact.json
charged_input=box/k16spine-20260903/terminal_laurent_t5.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-toptail-quadratics-fable5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
918b561a8e5a22a763e82a2a6319846eabc582b4fc04cf3cf7dbfd0a9783c784  {{LANE_INPUTS}}/k16-subchart-q-opus5-20260903.md
cc6782b0f5db5c7a48c41a33328b16ffef144abdd6d45834e7e10ff26d1aae90  {{LANE_INPUTS}}/k16-terminal-proof-opus5-20260903.md
401d374ecec0c556c7f7400ccade98571e1c1e93faf2daa1dd706f3b38c46391  {{LANE_INPUTS}}/k16-terminal-proof-sol56-20260903.md
a5b07c7c51d4914df96eb3acc9166bc83049a66732915e1bce0958752a57f480  {{LANE_INPUTS}}/k16-b4-axis-sol56-20260903.md
444d1a9f5194f764ec7073d990f42d7c014b2c311431f84805015f2bdefcb080  {{LANE_INPUTS}}/k16-cone-gate-gpt55-20260903.md
f4d071a18cff25c4bdade4508f53c58bc39d20a26907fa619410622bfb91ccf6  {{LANE_INPUTS}}/k16-properness-gate-opus5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
068d506c309ff1c4cbf8d0d25001c04a186c0d498ca9024acf977b6bc272a034  {{LANE_INPUTS}}/sq_emit_dim.py
fbbdb788efad0f3fbdf6aa6bbecb0bd3c1d78cd57287edff101ba9642b3cf671  {{LANE_INPUTS}}/sq_chart_model.py
b18a0bf54e4c26a109dda1e7dabd242930087486c1c95737c0f757a7ad333f6a  {{LANE_INPUTS}}/sq_load.py
d662026a9c5c00c2eb5b36ef0aa8000469483fdc69da154abd36d3d4d6478d98  {{LANE_INPUTS}}/s12_symbolic_check.py
b8ce4f1c8ff3d4ee02434363abeb92d47795b22049a185057c65d209d01a2452  {{LANE_INPUTS}}/s4_records_subchart.py
0cc821ff59adc955d2c6c33a572766b01569d578f1034f343c4f3661cebcf8ed  {{LANE_INPUTS}}/singular_terminal_driver.py
8a935838ac01731110efd5f36652cae3d66bd00ffa23ae4450cdadaa41438001  {{LANE_INPUTS}}/terminal_array_recurrence.py
a3928a3e0d96ca44c959548d2964d01d7b0f711dc0313019edd738264701f177  {{LANE_INPUTS}}/build_artifact_manifest.py
abf0f851b80c5ecc1df707764aed08d62e0eefc36cbd0228934f91bd88df0216  {{LANE_INPUTS}}/validate_claim_artifacts.py
96a24eb2e7e477d14e18b1ddd76f3d1ecab49ccbdd92b804b94f9f53ff1c3e99  {{LANE_INPUTS}}/coeff-exact-axis.py
dcd518e90296c6fb565555b952609db42e39c367cf61ba6f988c71a6b31afbd7  {{LANE_INPUTS}}/axis_exact.py
9aeef23dcf1d6569fc77246ac6275275445e2ef94c2342e1d9b5565fd0839420  {{LANE_INPUTS}}/validate_axis_records.py
234da78b92c8e5afd95919fa0ae4597cd2fca272653b88f3365261ac327e445a  {{LANE_INPUTS}}/terminal_laurent_t2.json
e56ee5ccb829f3b3c4279a484cdeac2ec4d0020f832e0fe1d930dfe03224bc78  {{LANE_INPUTS}}/terminal_laurent_t5_b4_1_exact_status.json
0c6adb555b07624bac34ed2862ea259a4258f099d54a84f09d5b3824bda5858a  {{LANE_INPUTS}}/terminal_laurent_t4.json
0f23c4d7996a5d915909c87e7d5f0bc1123f8fbc6677559ca188f40e002d7501  {{LANE_INPUTS}}/terminal_laurent_t2_product_exact.json
f68a4666afb25490ceb62ec2b2f9ebe9b22b61c415cbf66edc074eb50a650689  {{LANE_INPUTS}}/terminal_laurent_t5.json
```
