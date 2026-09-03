# Derivation lane (short, decisive for the spine): derive the closed high-E_t pivot forms (5.9)–(5.15) of the K = 16 second affine spine SYMBOLICALLY in (t, j) — b_j = g₃(3t+2−3j)/(2y(t−j)), d_j = (g₂(t+1−2j) + b_j(t+1+j))/(y(4t−2j+1)), n_j = −g₁(t+j) + (j−t)d_j + 2q·b_j, and the analogous dq_j, nq_j — by the perturbation calculation the Opus gate prescribes; this closes the one gap in AUDIT delta 17(qqq)/(uuu)

Context (banked): the Sol spine report (charged) proves the second affine
spine for t ≥ 2 by a Laurent/Euler recurrence whose pivot coefficients are
given by closed forms (5.9)–(5.15) in laurent_pivot_formulas.py (charged);
the Opus gate (charged §3, §8) confirmed everything else and found that those
closed forms are ASSERTED — verified against exact nonlinear records at t =
2, 3, 4, 5 (32 coefficients) — but not derived; the structural argument is
sound (each new elimination variable sits in its own weight, so its affine
coefficient has weight zero and lies in A_t = Q[y]/(H_t), hence equals its
value at the homogeneous origin), and the missing step is the symbolic (t, j)
propagation of a perturbation through T' = (g/2y)(5C + 3sC') (identity
(5.7b)), the Euler inverse [L^m]S = e_m/(y(2m+1)), and the E_t coefficient
[s^{4t+1−j}]. Task: (1) read the charged spine report §2, §5 (5.1), §6 and the
gate §3, §8; load laurent_pivot_formulas.py and terminal_laurent_model.py
(the fixed-t builder); (2) redo the fixed-t build at t = 2, 3 to understand
the recurrence; (3) implement the SYMBOLIC version: over Q(t, j)[d]/(3d² − t − 1)
(the algebra A_t in the gate's parametrisation; keep d as the algebra
generator, never invert a zero divisor), perturb C by ε·s^{t−1−j} (resp. U by
ε·s^{q−j}), propagate band by band through T' via (5.7b), through the Euler
inverse for S, read [s^{4t+1−j}] of E_t, and differentiate in ε at ε = 0; the
result must be the asserted b_j, d_j, n_j (and dq_j, nq_j) as rational
functions of (t, j, y, g₁, g₂, g₃, q) — print the derived forms and the
differences with the asserted ones (must be 0 identically); handle the index
ranges (j from … to … as in the spine order) and the boundary cases (j = t?
j = 0?); (4) specialise to t = 2..6 and compare with the exact nonlinear
records (the charged terminal_laurent_t*.json) — must match up to rational
associates; (5) verdict: (5.9)–(5.15) DERIVED (then the spine for t ≥ 2 is a
theorem and the reduction (T) ⇔ (8.1) is PROMOTED) / GAP; type every claim;
FALLACY-v2 applies (denominators: list every one and its integer roots in t
and j). ≤ 60 min; 1–2 cores; no ledger edits; no jc2-lean; no ideation-*
files; no in-progress lane reports (k16-terminal-proof-*, k16-t5t6, bridge-
chart-gate, g9966-*, emitter-native). Drivers to box/k16pivot-20260903/.
Report: xmodel/k16-pivot-forms-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 6-14KB; 60 minutes.
charged_input=xmodel/k16-spine-gate-opus5-20260903.md
charged_input=xmodel/k16-middle-spine-sol56-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16spine-20260903/terminal_laurent_t2.json
charged_input=box/k16spine-20260903/terminal_laurent_model.py
charged_input=box/k16spine-20260903/terminal_laurent_t5_b4_1_exact_status.json
charged_input=box/k16spine-20260903/laurent_pivot_formulas.py
charged_input=box/k16spine-20260903/compact_remainder.py
charged_input=box/k16spine-20260903/terminal_laurent_t4.json
charged_input=box/k16spine-20260903/terminal_laurent_t2_product_exact.json
charged_input=box/k16spine-20260903/terminal_laurent_t5.json
charged_input=box/k16spine-20260903/terminal_laurent_t3.json
charged_input=box/k16spinegate-20260903/gate3_norms.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-pivot-forms-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
6d3bc222fedac1c0694346d53cb3caa59ad34824b8b14cdf3448708926af3a16  {{LANE_INPUTS}}/k16-spine-gate-opus5-20260903.md
c0b12fd69bc1209e2b63e3d823d6748cd83675b8c63d714880d2368d50f343c4  {{LANE_INPUTS}}/k16-middle-spine-sol56-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
234da78b92c8e5afd95919fa0ae4597cd2fca272653b88f3365261ac327e445a  {{LANE_INPUTS}}/terminal_laurent_t2.json
f900ca3a6e5537e9605a98a5135a4b7dc9eb78c2a2cdde0aeff972b348db9c29  {{LANE_INPUTS}}/terminal_laurent_model.py
e56ee5ccb829f3b3c4279a484cdeac2ec4d0020f832e0fe1d930dfe03224bc78  {{LANE_INPUTS}}/terminal_laurent_t5_b4_1_exact_status.json
2765a94a1f955fb6844ef7886ac4a9f70135fee56c4c44e39c466b3325883bb7  {{LANE_INPUTS}}/laurent_pivot_formulas.py
2400fed2b859942374730fb415b3536aea233df8411c14b500b56145353ecda2  {{LANE_INPUTS}}/compact_remainder.py
0c6adb555b07624bac34ed2862ea259a4258f099d54a84f09d5b3824bda5858a  {{LANE_INPUTS}}/terminal_laurent_t4.json
0f23c4d7996a5d915909c87e7d5f0bc1123f8fbc6677559ca188f40e002d7501  {{LANE_INPUTS}}/terminal_laurent_t2_product_exact.json
f68a4666afb25490ceb62ec2b2f9ebe9b22b61c415cbf66edc074eb50a650689  {{LANE_INPUTS}}/terminal_laurent_t5.json
6490d1923d8a14652d36ef77e47a2122410f30f6137a44b28af9807ca076b926  {{LANE_INPUTS}}/terminal_laurent_t3.json
c6c3d933f0fedfc330dcd388e5cca96d8254324299c43102e382d9ea8fd312d3  {{LANE_INPUTS}}/gate3_norms.py
```
