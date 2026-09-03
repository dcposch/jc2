# Hostile gate: the PROVED second affine spine of the K = 16 normalised systems (AUDIT delta 17(qqq), Sol §2–§6) — verify the uniform post-H/c row skeleton, the compact closed h-adic identity, the 2t zero/duplicate recurrence, the split-safe Laurent/Euler spine with uniformly nonzero pivot norms (and the zero-divisor obstruction on t = 3s² − 1), and the closed terminal family (6.1)–(6.4); confirm that (8.1) ⟨T_{t,0..2t−1}⟩ = [1] in A_t[b₃, b₄, q_{2,0}, …, q_{t−1,0}] is EXACTLY theorem (T) on the ray (no projection, no untyped localisation)

Charged: k16-middle-spine-sol56-20260903.md with its drivers and the
terminal_laurent_t*.json records. Task: (1) re-derive §2's compact exact h-adic
identity symbolically (sympy over Q(t)) and check it against the charged
generator at t = 2, 3, 4; (2) re-derive the post-H/c support (§3) and the
duplicate recurrence — the counts 9t + 2 rows / 6t + 2 auxiliaries / 5t + 2
affine pivots / 2t duplicates — for symbolic t and check at t = 2..6; (3) audit
the spine proof (§5, 5.1): for each pivot in the Laurent/Euler order, is the
pivot's norm/resultant with H_t a nonzero polynomial in t for ALL positive
integers t (print each; find its integer roots; confirm none is a positive
integer) — and on the split indices t = 3s² − 1 confirm the proof works in
the product algebra without inverting a zero divisor; reproduce the
obstruction (the scheduled scalar pivot that is a zero divisor at split
indices) and its bypass; (4) verify the terminal family: recompute T_{t,k} =
[X^k]σ_t(E_t) at t = 2, 3, 4 from the closed form (6.1)–(6.4) and compare with
the charged JSON records and with the terminal systems of the banked
uniform-structure lane (the same ideal up to a unit and coordinate change?
— state the exact relation); confirm the terminal ideal is [1] at t = 1..4
exactly and replay the mod-1009 checks at t = 5, 6 on both fibres; (5) the
logical chain: write out why 1 ∈ ⟨T_{t,k}⟩ ⇔ the gauged order chart is empty
⇔ (T) at t (the quotient-ring isomorphisms, the grading slice, the algebra
A_t), naming every step's justification; (6) verdict: CONFIRMED (the spine
and the reduction are promotable; (T) on the ray = (8.1)) / GAP (which step;
cheapest test) / REFUTED. Type every claim; FALLACY-v2 applies. ≤ 120 min; 2
cores; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane
reports (k16-terminal-proof-*, k16-t5t6, bridge-chart-gate, g9966-*,
emitter-native, n5-denominator). Drivers to box/k16spinegate-20260903/.
Report: xmodel/k16-spine-gate-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 120 minutes.
charged_input=xmodel/k16-middle-spine-sol56-20260903.md
charged_input=xmodel/k16-uniform-structure-sol56-20260903.md
charged_input=xmodel/k16-t4-normalizer-gate-gpt55-20260903.md
charged_input=xmodel/k16-middle-spine-opus5-20260903.md
charged_input=box/k16t3-20260903/t3/t_order_system.py
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=FALLACY-v2.md
charged_input=box/k16spine-20260903/terminal_attack_pipeline.py
charged_input=box/k16spine-20260903/terminal_laurent_t2.json
charged_input=box/k16spine-20260903/terminal_b4zero_positive_mod.py
charged_input=box/k16spine-20260903/terminal_laurent_model.py
charged_input=box/k16spine-20260903/terminal_mod_full_emit.py
charged_input=box/k16spine-20260903/canonical_build_status.py
charged_input=box/k16spine-20260903/canonical_post_hc.py
charged_input=box/k16spine-20260903/canonical_import_schur.py
charged_input=box/k16spine-20260903/terminal_laurent_t5_b4_1_exact_status.json
charged_input=box/k16spine-20260903/terminal_laurent_exact_emit.py
charged_input=box/k16spine-20260903/laurent_pivot_formulas.py
charged_input=box/k16spine-20260903/compact_remainder.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-spine-gate-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
c0b12fd69bc1209e2b63e3d823d6748cd83675b8c63d714880d2368d50f343c4  {{LANE_INPUTS}}/k16-middle-spine-sol56-20260903.md
90d4068583ec1801641f8e346f0fdd19d21c5d68901d5ee4f7aec8ddb7e3f1cb  {{LANE_INPUTS}}/k16-uniform-structure-sol56-20260903.md
e868a7f2df3814caf1847411918c17cbf8e71688779819fd4764d70e9d86ae83  {{LANE_INPUTS}}/k16-t4-normalizer-gate-gpt55-20260903.md
a3ee8ca558fa04b3fd23851d609280dc04eaa35c9013e53e45dce5163a900c42  {{LANE_INPUTS}}/k16-middle-spine-opus5-20260903.md
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
1784e88338138aef509bfe3a793891e1d0ba645c429765c9cd1c129a58a1e099  {{LANE_INPUTS}}/terminal_attack_pipeline.py
234da78b92c8e5afd95919fa0ae4597cd2fca272653b88f3365261ac327e445a  {{LANE_INPUTS}}/terminal_laurent_t2.json
bd1946b72e56cd7c882f92724957f13026a1d7401df6e33c95f5a1931b49af41  {{LANE_INPUTS}}/terminal_b4zero_positive_mod.py
f900ca3a6e5537e9605a98a5135a4b7dc9eb78c2a2cdde0aeff972b348db9c29  {{LANE_INPUTS}}/terminal_laurent_model.py
ed8c13572ef0f98dc726f767887e5e571bf9f268886cfb0ff3b277372105686b  {{LANE_INPUTS}}/terminal_mod_full_emit.py
1f4235e67779576ff15a4f0215db36375408cd8f398adcc918adf1e69c6e1423  {{LANE_INPUTS}}/canonical_build_status.py
96dcc36ee2cd577cab58ee54dcd8b7c2108f70577a5cdcf84c54c84502757cd7  {{LANE_INPUTS}}/canonical_post_hc.py
373142bfe524f4d55ef4e16d48b2d29766bcdc2cb96ef45fe53c9d99d6116f47  {{LANE_INPUTS}}/canonical_import_schur.py
e56ee5ccb829f3b3c4279a484cdeac2ec4d0020f832e0fe1d930dfe03224bc78  {{LANE_INPUTS}}/terminal_laurent_t5_b4_1_exact_status.json
2b23beb946f3eaebbc90b456e0a90cc80fc63ffc8d7373ffb3bbfe252f77d891  {{LANE_INPUTS}}/terminal_laurent_exact_emit.py
2765a94a1f955fb6844ef7886ac4a9f70135fee56c4c44e39c466b3325883bb7  {{LANE_INPUTS}}/laurent_pivot_formulas.py
2400fed2b859942374730fb415b3536aea233df8411c14b500b56145353ecda2  {{LANE_INPUTS}}/compact_remainder.py
```
