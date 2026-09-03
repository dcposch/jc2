# Hostile gate + computation: the BRIDGE NORMAL FORM chart for the K = 16 ray (AUDIT delta 17(ooo)) — verify the proof of (BNF) P = [Σ_{k=0}^{e} a_k Q^{(e−k)/q}]_{h ≥ 0} with scalar a_k, verify that the bridge chart is a SUBSET of the charged Theorem-1.2 order chart (hence still a necessary superset of the tuple locus), replay t = 1, 2, then RUN the bridge chart at t = 3, 4, 5, 6, 7, 8 (6t + 5 unknowns) and record the terminal data

Charged (k16-middle-spine-opus5-20260903.md §2–§5, §8; box/k16spine-opus-
20260903/bridge_chart.py, moh_p209_control.py): on the descended ray (12t+4,
8t+4; 12t+1; 3; J = cγ) with e = 3t+1, q = 2t+1, the reciprocal parameter η̃ has
η̃⁻⁴ = Q^{1/q} exactly; the tuple vanishings for j ≤ 0 < N force Σ_k a_k Q^{(e−k)/q}
= Σ_k a_k η̃^{−n+4k} to be exactly the non-positive-exponent part of P's η̃-
expansion; since a term c·h^i with deg_π c < 4 has ord_η̃ ≥ −4i − 3, every
h-negative term has positive η̃-exponent, so ord_η̃(P − S_{≥0}) > 0 while P − S_{≥0}
is a polynomial in π of some degree d with ord_η̃ = −d ≤ 0 — hence P = S_{≥0}
(BNF); the a_k = p_{−n+4k} are scalars by Lemma 2.1 in the reciprocal parameter
(k16-ray-T-newton-sol56-v3 §1, charged); gauges: a_t, a_e, a_{e−1} (Moh's
f − (3/4)a₃ at t = 1); unknowns 4 (b's) + (3t+2) (β) + (3t−2) (a's after gauges)
+ c = 6t + 5; control: every α_i of the bridge-built P lands in the charged
space S_i (t = 1, 2), so bridge chart ⊆ order chart ⊆ tuple-locus superset;
kills: t = 1 (12 vars / 24 gens, 0.03 s), t = 2 (18 / 59, 2.04 s); source
correction: Moh's displayed p.209 formula differs from (BNF) at t = 1 by
(2/3)a₂β₂. Task: (1) audit the (BNF) proof line by line: the exactness of
η̃⁻⁴ = Q^{1/q} (definition of η̃ — state it; is it the charged reciprocal
dictionary's η̃? does Q^{1/q} exist as a Laurent series in η̃ with the right
leading term?), the ord_η̃ bound for h-negative terms (deg_π c < 4 — is that
forced for all coefficients in the chart, including the β's?), the
polynomial-degree argument, the scalar claim for a_k (which j-range of Lemma
2.1 applies; is the reciprocal Lemma 2.1 a theorem or the charged
conditional?); name any gap; (2) verify the subset claim at t = 1..4 by
running bridge_chart.py and checking every α_i ∈ S_i and every β_j ∈ S_j
against the charged order-chart spaces (t_order_system.py); (3) replay the
t = 1, 2 kills (wrapper controls; actual pair (π, π − γ²/2) fails the tuple);
(4) RUN t = 3, 4, 5, 6, 7, 8 on the bridge chart: modular over three primes,
then exact over Q (with the charged normalisation if needed: Q*-pivots,
grading, x = 1 slice, A_t); record per t: unknowns, generators, wall time,
verdict, and — crucially, as data for the spine — the terminal system after
the normalisation in a CANONICAL pivot order (band-descending; print the
terminal rows over A_t with coefficients in Z[t] where possible); (5) verify
the Moh p.209 discrepancy (2/3)a₂β₂ from the page image (pdftoppm -r 200;
name the page): is it a misprint in Moh or a difference in normalisation?
(6) verdict: (BNF) CONFIRMED / GAP / REFUTED; (T) at t = 5..8 PROVED-HERE on
the bridge chart or MEASURED-MODULAR; the t-pattern of the terminal systems
(MEASURED). Type every claim; FALLACY-v2 applies. ≤ 120 min; 4 cores; no
ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-middle-spine-sol56, k16-t5t6-grok46, g9966-*, emitter-native, n5-
denominator). Drivers to box/bridgegate-20260903/.
Report: xmodel/bridge-chart-gate-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-22KB; 120 minutes.
charged_input=xmodel/k16-middle-spine-opus5-20260903.md
charged_input=xmodel/k16-ray-T-newton-sol56-v3-20260903.md
charged_input=xmodel/k16-uniform-structure-sol56-20260903.md
charged_input=xmodel/k16-t4-normalizer-gate-gpt55-20260903.md
charged_input=box/k16t3-20260903/t3/t_order_system.py
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/k16spine-opus-20260903/e4_phi4_identity.py
charged_input=box/k16spine-opus-20260903/jac_tail_identity.py
charged_input=box/k16spine-opus-20260903/bridge_chart.py
charged_input=box/k16spine-opus-20260903/bridge_graded.py
charged_input=box/k16spine-opus-20260903/ray_numeric_screens.py
charged_input=box/k16spine-opus-20260903/moh_p209_control.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/bridge-chart-gate-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
a3ee8ca558fa04b3fd23851d609280dc04eaa35c9013e53e45dce5163a900c42  {{LANE_INPUTS}}/k16-middle-spine-opus5-20260903.md
27f395615d37906a379f6c727c6499be6d78c711e7d7ca728ac44050f1be23e0  {{LANE_INPUTS}}/k16-ray-T-newton-sol56-v3-20260903.md
90d4068583ec1801641f8e346f0fdd19d21c5d68901d5ee4f7aec8ddb7e3f1cb  {{LANE_INPUTS}}/k16-uniform-structure-sol56-20260903.md
e868a7f2df3814caf1847411918c17cbf8e71688779819fd4764d70e9d86ae83  {{LANE_INPUTS}}/k16-t4-normalizer-gate-gpt55-20260903.md
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
83f846f184ea367cd6564788fcfbcb002b74ac644f714dc3c1eaf4c6194578f1  {{LANE_INPUTS}}/e4_phi4_identity.py
e5560372ca54abd397548b2c217576ea381c39f81dd736f86dceebb997830aea  {{LANE_INPUTS}}/jac_tail_identity.py
34e6f380532943539f8686255986c551fe96534ff46109fd00fd8cc9c9e97d9e  {{LANE_INPUTS}}/bridge_chart.py
bc51bcd64831d2623742b2bff49f7e3fcde3646dd9d8021294d2ce25d88c29a3  {{LANE_INPUTS}}/bridge_graded.py
34de47f291253c324cef6440bd1cb9a0d13a5808c48c4bf23b635de2679292af  {{LANE_INPUTS}}/ray_numeric_screens.py
9fa7dc7a82aa722fc5b7da641379a374815cdfb0b6e2fb2e7f5112fbd20f206c  {{LANE_INPUTS}}/moh_p209_control.py
```
