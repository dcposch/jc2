# THE LAST STATEMENT ON THE K = 16 RAY: prove (8.1) — ⟨T_{t,0}, …, T_{t,2t−1}⟩ = [1] in A_t[b₃, b₄, q_{2,0}, …, q_{t−1,0}] for every integer t ≥ 2, where T_{t,k} = [X^k]σ_t(E_t) with E_t(X) = (b₃y − LR)V' + (LS − b₃T − b₂g)U' + g·y and σ_t the proved Laurent/Euler spine — via the two sharpened lemmas RESIDUAL-ZERO and TOP-TAIL-UNIT, or directly; this is theorem (T) on the only known cofinal screened family, uniformly in t

Context (banked, AUDIT delta 17(qqq); read the charged Sol report §2–§8 first,
and the charged Opus bridge report for the alternative 6t + 5 chart): after the
promoted normalizer lemma (17(xx)/(ddd)) and the proved second affine spine, the
gauged Theorem-1.2 order chart of the descended K = 16 pair (12t+4, 8t+4; 12t+1;
3; J = cγ) is empty iff the terminal family (8.1) generates the unit ideal;
this holds exactly at t = 1, 2, 3, 4 and mod 1009 on both fibres of H₅, H₆; the
producer's sharpened targets: RESIDUAL-ZERO: √⟨T_{t,1}, …, T_{t,2t−1}⟩|_{b₄=0} =
(b₃, q_{2,0}, …, q_{t−1,0}) for t ≥ 3 (then T_{t,0}(0) = −c = −5qg₅ is a unit and
closes the b₄ = 0 chart); TOP-TAIL-UNIT: ⟨T_{t,t}, …, T_{t,2t−1}⟩|_{b₄=1} = [1]
(closes b₄ ≠ 0); base cases: RESIDUAL-ZERO proved at t = 3, 4; TOP-TAIL-UNIT at
t = 2, 3, 4; at t = 2 RESIDUAL-ZERO is false but the band-zero row is a unit.
FALLACY-v2 constraints: a certificate must be an indexed recurrence (proved
by induction on k or t) or carry a specialisation denominator D(t) whose
integer roots are checked separately; on split indices t = 3s² − 1 work in the
product algebra A_t ≅ Q(√(3(t+1))) × … (never invert a zero divisor); A_t is a
rank-two algebra, not a field. Task: (1) compute the closed form of T_{t,k} as
polynomials in (t, y, b₃, b₄, q_{j,0}) — from (6.1)–(6.4) and the spine
substitutions (the charged drivers produce them per t; derive the symbolic-t
form: degrees in the auxiliaries, coefficient polynomials in t and y; verify
against t = 2..6); (2) TOP-TAIL-UNIT: at b₄ = 1, the top-tail rows T_{t,t..2t−1}
— find the triangular / weighted structure (which auxiliary each row
introduces with a unit leading coefficient in A_t), and prove by induction on
the row index that the ideal contains successive auxiliaries and finally a
unit; record every leading coefficient's resultant with H_t as a polynomial
in t with its integer roots; (3) RESIDUAL-ZERO: at b₄ = 0, prove the radical
statement (e.g. show each T_{t,k}|_{b₄=0} for k ≥ 1 is a monomial-times-unit in
the auxiliaries plus terms in the ideal (b₃, q_{·,0}), by induction); handle
t = 2 as the base; (4) assemble the proof of (8.1) for all t ≥ 2 with every
denominator listed, or deliver the sharpest partial result with the exact
remaining statement and its cheapest test; (5) controls: specialise every
uniform formula to t = 2, 3, 4 and match the banked exact objects; check the
proof at a split index (t = 2 is one: 3·3 − 1... no: t = 3s² − 1 gives t = 2 (s = 1),
11, 26 — so t = 2 IS a split index: confirm the argument there in the product
algebra, and check t = 11 numerically mod a prime); (6) verdict: (T) on the ray
PROVED for all t ≥ 1 (full proof, typed PROVED-HERE), or PARTIAL. ≤ 180 min; 4
cores; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane
reports (k16-spine-gate, the other terminal-proof lane, k16-t5t6, bridge-
chart-gate, g9966-*, emitter-native, n5-denominator). Drivers to
box/k16terminal-sol56-20260903/.
Report: xmodel/k16-terminal-proof-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 14-30KB; 180 minutes.
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
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-terminal-proof-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

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
