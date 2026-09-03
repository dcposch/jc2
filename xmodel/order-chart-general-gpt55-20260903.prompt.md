# Instrument lane: the GENERAL two-point ORDER CHART — generalise the K = 16 generator (Theorem-1.2 order bounds on every coefficient of the approximate-root tower + the three safe target gauges + Lemma 2.1 support), which cut the K = 16 charts to 9t + 9 unknowns, to an arbitrary two-point descended datum (n', m', M₂', V₂', k) with symbolic top-face slopes (partition strata), validate it against the banked kills, and run the smallest open large row (25,15; 21; 2; k = 2)

OPERATIONAL: write the skeleton first; every Singular job in the foreground
with `timeout`; never end the turn with a job running; ≤ 2 cores (the box is
loaded). Context (banked): the generic "corrected support" charts of the seven
large open two-point rows (AUDIT deltas 17(kkk), (bbbb), (oooo)) have 135–276
unknowns and rows of 42–180 MB — intractable even for native Q*-pivoting —
whereas the K = 16 charts (17(mm), (oo), (ww), (ddd)) were tractable because
t_order_system.py imposes the Theorem-1.2 ORDER bounds (Moh p.149: for the
approximate-root tower z = π − γ, B = πz + b₁π + b₂, A = πB + b₃, h = πA + b₄
[for d₂' = 4] the coefficient spaces S_i = ⟨1⟩, ⟨1, A⟩, ⟨1, A, B⟩, … by weight)
and the three target gauges (const(β_q) = 0, α_t = 0, const(α_e) = 0), giving
P = h^e + Σα_i h^{e−i}, Q = h^q + Σβ_j h^{q−j} with tiny coefficient spaces; the
GPT-5.5 gate's independent generator (t2_independent_order_system.py,
charged) derives the chart from the descended data alone (radii by Φ,
Theorem 1.2 order bound λ_P/e = λ_Q/q, filtration dimensions). Task: (1)
generalise t2_independent_order_system.py to arbitrary (n', m', M₂', V₂', k)
with d₂' = gcd(n', m') and u' = d₂' − V₂': the approximate-root tower of depth
d₂' (h of π-degree d₂' with top face y^{V₂'}·Π(y − a_i x)^{e_i}, Σe_i = u', symbolic
slopes a_i and the Ω non-degeneracy saturation as in 17(rr)/(vv)), the Φ radii
(closed form 17(ff)), the Theorem-1.2 common coefficient bound, the
coefficient spaces per h-deficit (the filtration), Lemma 2.1 support, the
three gauges (state which are safe for general k — the K16 gauges assumed
k = 1; derive the general safe set), the h-adic Jacobian identity and monic
division, the h⁰ remainder = c·x^k, Rabinowitsch, the deg_x J sanity gate;
(2) VALIDATE: (16,12; 13; 3; 1) and (28,20; 25; 3; 1) must reproduce the banked
charts (unknown/equation counts and [1]); (33,22; 30; 8; 1) strata [3], [2,1]
and (45,30; 42; 11; 1) [4], [3,1], [2,2] must be [1] with FEWER unknowns than the
A/B charts (report the counts — this is the instrument's value); (15,10; 11;
3; 2) and (21,14; 18; 5; 1) [1]; the actual pair (π, π − γ²/2) fails the tuple;
(3) run (25,15; 21; 2; 2) strata [3], [2,1], [1,1,1] in the order chart: report
unknowns (expect far below 135), modular over three primes, exact where it
finishes (≤ 20 min each), with the preprocessing (Q*-pivots, grading, slice)
if needed; (4) if time remains, the δ₁' = 0 rows (21,14; 15; 6; 4) etc. (the
order chart at δ₁' = 0 — is it degenerate? report); (5) verdict per stratum
and the instrument's status; FALLACY-v2 applies (a gauge you cannot justify
for general k is a slice — say so). ≤ 150 min; no ledger edits; no jc2-lean;
no ideation-* files; no in-progress lane reports. Drivers to
box/orderchart-20260903/.
Report: xmodel/order-chart-general-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 150 minutes.
charged_input=box/k16t2-gate-20260903/t2_independent_order_system.py
charged_input=box/k16T-drivers-20260903/t2_order_system.py
charged_input=box/k16t3-20260903/t3/t_order_system.py
charged_input=xmodel/k16-t2-gate-gpt55-20260903.md
charged_input=xmodel/topface-license-sol56-20260903.md
charged_input=box/topface-20260903/topface_cases.py
charged_input=xmodel/strata-rerun-corrected-gpt55-20260903.md
charged_input=box/chartfix-20260903/shape.py
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=xmodel/preprocess-native-gpt55-20260903.md
charged_input=box/preprocess-native-20260903/prep.sing
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/order-chart-general-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
7ee7e29eca86dadecf4cffdc996539fc875851ce5803ad7ddaf68b888624f823  {{LANE_INPUTS}}/t2_independent_order_system.py
55067a8c74d6c360c72aaa40243dde7e8e1a804158b3c78abf523d77a25cb5e2  {{LANE_INPUTS}}/t2_order_system.py
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
692fd869d8a11b3a984d1fe8c4ccb4b42de7326567c130b8babae1571ca6e863  {{LANE_INPUTS}}/k16-t2-gate-gpt55-20260903.md
53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae  {{LANE_INPUTS}}/topface-license-sol56-20260903.md
369bafb1341f96708f6886e79c93fb9bdad8e70abb1ae4c69ddd1dd6a9c62082  {{LANE_INPUTS}}/topface_cases.py
bdfa5aafe15d0de03f9069806f3af40a89db1d455d2019e3f6143afcf0901926  {{LANE_INPUTS}}/strata-rerun-corrected-gpt55-20260903.md
ba25cd10fa5cc998017688db455094bcd3b7a8e870085dd2db64fb4f66b098de  {{LANE_INPUTS}}/shape.py
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
ef8d2c5d7207476887bd8b55d13bc63a4557f226353efba56aba9b7f56ffa4a0  {{LANE_INPUTS}}/preprocess-native-gpt55-20260903.md
cd77209b88c8cca6cf08db7fb1c9ea7a67110653935041fe3b2d35efc438652c  {{LANE_INPUTS}}/prep.sing
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
