# Proof-attack lane (a GLOBAL statement, not a sub-chart): dim I_{t,+} = 0 on the K = 16 terminal cone via a homogeneous system of parameters / regular sequence and the Hilbert series — test whether the t + 2 highest-weight rows of I_{t,+} = ⟨T_{t,1..2t−1}⟩ ⊂ A_t[b₄, q_{2,0..t−1,0}, b₃] (weights 1, 2..t−1, t+1) form a weighted-homogeneous regular sequence (complete intersection of dimension 0) at t = 3..8, and if so, formulate and attack the uniform statement on their LEADING FORMS in the weighted term order (the full weighted initial ideal in_{wp}(I_{t,+}) must contain a power of every variable)

OPERATIONAL: skeleton first; every Singular job in the foreground with
`timeout 1800`; never end the turn with a job running; ≤ 3 cores. Context
(banked, AUDIT deltas 17(cccc), (jjjj), (llll), (nnnn), (mmmm)): every sub-chart /
axis route proves radical membership modulo the remaining coordinates and
cannot reach the chain's head (the b₄ = 1 chart); the cone I_{t,+} is weighted-
homogeneous with a PROVED closed indexed generator family (Sol 17(zzz) §2;
Fable 17(iiii) §2); (V0) dim I_{t,+} = 0 holds at t = 3..7 (promoted via the
properness instrument, which also makes MODULAR dim computations on the
homogeneous ideal into characteristic-zero certificates — use it: pick a good
prime and a root of H_t as in the charged Fable/Opus drivers); the earlier
"initial-form upgrade" that failed (dim⟨in_w(gens)⟩ = 2, 3, 3, 4) was a SUB-CHART
degeneration (w = 0 on R, 1 off R), NOT the full weighted initial ideal. Task:
(1) at t = 3..8 (modular on a good prime, both fibres at split t; exact where
cheap): compute the weighted Hilbert series of A_t[b₄, q, b₃]/I_{t,+} in the
grading wp(1, 2, …, t−1, t+1) (Singular `hilb` with the weight vector) — a
finite-dimensional quotient (dim 0) shows as a polynomial numerator over
Π(1 − s^{w_j}) with the series terminating; report the Hilbert polynomial and
the vector-space dimension (the "length") of the quotient per t — the
lengths are the uniform invariant to conjecture; (2) test whether the t + 2
rows of highest weight (bands 2t−1 down to t−2, weights 4t+1 … 2t+2? — take the
actual weights of the rows from the grading) form a REGULAR SEQUENCE: compute
the Hilbert series of the ideal they generate and compare with the
complete-intersection formula Π_i(1 − s^{deg T_i}) / Π_j(1 − s^{w_j}); equality ⇔
regular sequence; if the top rows fail, search (greedy, by weight) for ANY
t + 2 rows forming a regular sequence — report the selection per t; (3)
compute the full weighted initial ideal in_{wp}(I_{t,+}) (Singular `lead` of a
std in the weighted order): list, per t, the minimal generators and check that
a pure power of each variable b₄^{a}, q_{j,0}^{a_j}, b₃^{a'} occurs — record the
exponents as functions of t (these are the uniform target; the refuted
pattern of the Fable report was for a different ideal/ordering — be explicit
about the ordering); (4) UNIFORM ATTEMPT: from the closed indexed forms, derive
the leading monomial (in wp) of each T_{t,k} symbolically in t — if the t + 2
leading monomials of a chosen subset are pairwise coprime pure powers of
distinct variables for every t, the subset is automatically a regular
sequence (coprime leading monomials ⇒ Gröbner basis ⇒ complete intersection
of dim 0) and (V0) follows for ALL t ≥ 3 — write the proof; if the leading
monomials are not pure powers, report the exact structure and the sharpest
uniform statement you can prove (e.g. the Hilbert length formula in t, verified
t = 3..8); (5) controls: the t = 2, y = 1/5 fibre (dim 1: the Hilbert series must
NOT terminate) and y = 2/5 (dim 0); verdict: (V0) for all t ≥ 3 PROVED (then (T)
on the ray for all t ≥ 1, with the full dependency chain) / PARTIAL with the
exact residual statement; FALLACY-v2 applies (a modular Hilbert series is a
char-0 statement only through the properness lemma for the dim = 0 conclusion;
the length may differ mod p — report both). ≤ 150 min; no ledger edits; no
jc2-lean; no ideation-* files; no in-progress lane reports. Drivers to
box/k16hilb-20260903/.
Report: xmodel/k16-hilbert-regseq-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 150 minutes.
charged_input=xmodel/k16-subchart-q-opus5-20260903.md
charged_input=xmodel/k16-cone-gate-gpt55-20260903.md
charged_input=xmodel/k16-properness-gate-opus5-20260903.md
charged_input=xmodel/k16-terminal-proof-fable5-20260903.md
charged_input=xmodel/k16-terminal-proof-sol56-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16terminal-fable5-20260903/analyze_rows.py
charged_input=box/k16terminal-fable5-20260903/laurent_spine.py
charged_input=box/k16terminal-sol56-20260903/singular_terminal_driver.py
charged_input=box/k16terminal-sol56-20260903/terminal_array_recurrence.py
charged_input=box/k16terminal-sol56-20260903/build_artifact_manifest.py
charged_input=box/k16spine-20260903/terminal_laurent_t2.json
charged_input=box/k16spine-20260903/terminal_laurent_t5_b4_1_exact_status.json
charged_input=box/k16spine-20260903/terminal_laurent_t4.json
charged_input=box/k16spine-20260903/terminal_laurent_t2_product_exact.json
charged_input=box/k16spine-20260903/terminal_laurent_t5.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-hilbert-regseq-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
918b561a8e5a22a763e82a2a6319846eabc582b4fc04cf3cf7dbfd0a9783c784  {{LANE_INPUTS}}/k16-subchart-q-opus5-20260903.md
444d1a9f5194f764ec7073d990f42d7c014b2c311431f84805015f2bdefcb080  {{LANE_INPUTS}}/k16-cone-gate-gpt55-20260903.md
f4d071a18cff25c4bdade4508f53c58bc39d20a26907fa619410622bfb91ccf6  {{LANE_INPUTS}}/k16-properness-gate-opus5-20260903.md
16d5112ae6ed9a6de0c504b11df2e19c97ed031a1715a3916fd8d207cdf0d961  {{LANE_INPUTS}}/k16-terminal-proof-fable5-20260903.md
401d374ecec0c556c7f7400ccade98571e1c1e93faf2daa1dd706f3b38c46391  {{LANE_INPUTS}}/k16-terminal-proof-sol56-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
18fa23e743f5fb85487f0fb0a3c7a7a33ec8a78b39e7af53ad113ce4744baee2  {{LANE_INPUTS}}/analyze_rows.py
8e8fa5fa1e7960539631ef0304f6a51799e683b06be6c553a2a7c53d006d4d7d  {{LANE_INPUTS}}/laurent_spine.py
0cc821ff59adc955d2c6c33a572766b01569d578f1034f343c4f3661cebcf8ed  {{LANE_INPUTS}}/singular_terminal_driver.py
8a935838ac01731110efd5f36652cae3d66bd00ffa23ae4450cdadaa41438001  {{LANE_INPUTS}}/terminal_array_recurrence.py
a3928a3e0d96ca44c959548d2964d01d7b0f711dc0313019edd738264701f177  {{LANE_INPUTS}}/build_artifact_manifest.py
234da78b92c8e5afd95919fa0ae4597cd2fca272653b88f3365261ac327e445a  {{LANE_INPUTS}}/terminal_laurent_t2.json
e56ee5ccb829f3b3c4279a484cdeac2ec4d0020f832e0fe1d930dfe03224bc78  {{LANE_INPUTS}}/terminal_laurent_t5_b4_1_exact_status.json
0c6adb555b07624bac34ed2862ea259a4258f099d54a84f09d5b3824bda5858a  {{LANE_INPUTS}}/terminal_laurent_t4.json
0f23c4d7996a5d915909c87e7d5f0bc1123f8fbc6677559ca188f40e002d7501  {{LANE_INPUTS}}/terminal_laurent_t2_product_exact.json
f68a4666afb25490ceb62ec2b2f9ebe9b22b61c415cbf66edc074eb50a650689  {{LANE_INPUTS}}/terminal_laurent_t5.json
```
