# Third independent attack on THE LAST STATEMENT of the K = 16 ray — (8.1): ⟨T_{t,0}, …, T_{t,2t−1}⟩ = [1] in A_t[b₃, b₄, q_{2,0}, …, q_{t−1,0}] for every t ≥ 2 — now fully licensed (the second affine spine is a theorem, AUDIT delta 17(vvv)); route: generating functions / the Euler structure of E_t and σ_t, or a resultant/Sylvester argument in the single variable b₃ after the b₄-charts, rather than band-index induction (two other lanes are on that)

Context (banked, AUDIT deltas 17(qqq), (uuu), (vvv); read the charged Sol spine
report §2, §5–§8, the Opus gate, and the Grok derivation): the normalised
system reduces, by proved quotient-ring isomorphisms, to the terminal family
T_{t,k} = [X^k]σ_t(E_t), 0 ≤ k < 2t, with E_t(X) = (b₃y − LR)V' + (LS − b₃T − b₂g)U'
+ g·y (6.1), where L, R, S, T, U, V are the explicit Laurent/Euler objects of §2,
§5 (reconstruction (5.6)–(5.7b): T' = (g/2y)(5C + 3sC'), Euler inverse [L^m]S =
e_m/(y(2m+1))), σ_t the 5t + 2 unit affine substitutions, over A_t = Q[y]/(H_t),
H_t = 12(2t+1)²y² − 12(2t+1)(t+1)y + (t+1)(3t+2); the residual variables are
b₃, b₄, q_{2,0}, …, q_{t−1,0}; (8.1) holds exactly at t = 1..4, modulo 1009 at t = 5,
6; the producer's split: RESIDUAL-ZERO (b₄ = 0 chart: √⟨T_{t,1..2t−1}⟩ =
(b₃, q_{·,0}) for t ≥ 3, plus T_{t,0}(0) = −c a unit) and TOP-TAIL-UNIT (b₄ = 1
chart: ⟨T_{t,t..2t−1}⟩ = [1]). Task — a DIFFERENT route from band-index
induction: (1) write E_t and the σ_t-substituted family as coefficients of an
explicit generating function in X (or s) whose structure in t is closed —
e.g. is σ_t(E_t) the X-truncation of a product/composition of a few fixed
power series (an Euler-type exponential, a binomial series Q^{1/q}) whose
coefficients are hypergeometric in (t, k)? If so, the ideal ⟨T_{t,k}⟩ contains
the coefficients of a series identity and unit-ness may follow from a
Wronskian/resultant of two such series; (2) in the b₄ = 1 chart, eliminate the
q_{j,0} (they enter affinely in the top-tail rows? check) to reduce
TOP-TAIL-UNIT to a statement about polynomials in b₃ alone over A_t, then
prove the resultant of two of them is a unit of A_t for all t (a closed-form
resultant in t and y, with Res_y(·, H_t) a nonzero polynomial in t with no
positive integer root); (3) in the b₄ = 0 chart, prove RESIDUAL-ZERO by
showing each T_{t,k}|_{b₄=0}, k ≥ 1, is (unit)·(monomial in b₃, q_{·,0}) + (higher
terms in the ideal) — a weight/initial-form argument (the grading of 17(xx)
survives to the terminal family: state the weights); (4) verify every
uniform formula at t = 2, 3, 4 against the charged terminal_laurent_t*.json
records; handle t = 2 as the base (RESIDUAL-ZERO false there; band-zero row
a unit) and the split indices in the product algebra; list every
denominator with its integer roots; (5) verdict: (T) on the ray PROVED for all
t ≥ 1 (full proof) or the sharpest partial statement with its cheapest test;
FALLACY-v2 applies. ≤ 180 min; 4 cores; no ledger edits; no jc2-lean; no
ideation-* files; no in-progress lane reports (k16-terminal-proof-sol56,
k16-terminal-proof-fable5, k16-t5t6, bridge-chart-gate, g9966-*, emitter-
native). Drivers to box/k16terminal-opus-20260903/.
Report: xmodel/k16-terminal-proof-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 14-30KB; 180 minutes.
charged_input=xmodel/k16-middle-spine-sol56-20260903.md
charged_input=xmodel/k16-spine-gate-opus5-20260903.md
charged_input=xmodel/k16-pivot-forms-grok46-20260903.md
charged_input=xmodel/k16-uniform-structure-sol56-20260903.md
charged_input=xmodel/k16-middle-spine-opus5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16spine-20260903/terminal_attack_pipeline.py
charged_input=box/k16spine-20260903/terminal_laurent_t2.json
charged_input=box/k16spine-20260903/terminal_b4zero_positive_mod.py
charged_input=box/k16spine-20260903/terminal_mod_full_emit.py
charged_input=box/k16spine-20260903/canonical_build_status.py
charged_input=box/k16spine-20260903/canonical_post_hc.py
charged_input=box/k16spine-20260903/canonical_import_schur.py
charged_input=box/k16spine-20260903/terminal_laurent_t5_b4_1_exact_status.json
charged_input=box/k16spine-20260903/terminal_laurent_exact_emit.py
charged_input=box/k16spine-20260903/laurent_pivot_formulas.py
charged_input=box/k16spine-20260903/compact_remainder.py
charged_input=box/k16pivot-20260903/terminal_laurent_model.py
charged_input=box/k16pivot-20260903/compare_rebuild.py
charged_input=box/k16pivot-20260903/derive_pivot_forms.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-terminal-proof-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
c0b12fd69bc1209e2b63e3d823d6748cd83675b8c63d714880d2368d50f343c4  {{LANE_INPUTS}}/k16-middle-spine-sol56-20260903.md
6d3bc222fedac1c0694346d53cb3caa59ad34824b8b14cdf3448708926af3a16  {{LANE_INPUTS}}/k16-spine-gate-opus5-20260903.md
7ac6fe7a70c93049367077a696f7349f396a42f3668ebcd206d4906d02f70f09  {{LANE_INPUTS}}/k16-pivot-forms-grok46-20260903.md
90d4068583ec1801641f8e346f0fdd19d21c5d68901d5ee4f7aec8ddb7e3f1cb  {{LANE_INPUTS}}/k16-uniform-structure-sol56-20260903.md
a3ee8ca558fa04b3fd23851d609280dc04eaa35c9013e53e45dce5163a900c42  {{LANE_INPUTS}}/k16-middle-spine-opus5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
1784e88338138aef509bfe3a793891e1d0ba645c429765c9cd1c129a58a1e099  {{LANE_INPUTS}}/terminal_attack_pipeline.py
234da78b92c8e5afd95919fa0ae4597cd2fca272653b88f3365261ac327e445a  {{LANE_INPUTS}}/terminal_laurent_t2.json
bd1946b72e56cd7c882f92724957f13026a1d7401df6e33c95f5a1931b49af41  {{LANE_INPUTS}}/terminal_b4zero_positive_mod.py
ed8c13572ef0f98dc726f767887e5e571bf9f268886cfb0ff3b277372105686b  {{LANE_INPUTS}}/terminal_mod_full_emit.py
1f4235e67779576ff15a4f0215db36375408cd8f398adcc918adf1e69c6e1423  {{LANE_INPUTS}}/canonical_build_status.py
96dcc36ee2cd577cab58ee54dcd8b7c2108f70577a5cdcf84c54c84502757cd7  {{LANE_INPUTS}}/canonical_post_hc.py
373142bfe524f4d55ef4e16d48b2d29766bcdc2cb96ef45fe53c9d99d6116f47  {{LANE_INPUTS}}/canonical_import_schur.py
e56ee5ccb829f3b3c4279a484cdeac2ec4d0020f832e0fe1d930dfe03224bc78  {{LANE_INPUTS}}/terminal_laurent_t5_b4_1_exact_status.json
2b23beb946f3eaebbc90b456e0a90cc80fc63ffc8d7373ffb3bbfe252f77d891  {{LANE_INPUTS}}/terminal_laurent_exact_emit.py
2765a94a1f955fb6844ef7886ac4a9f70135fee56c4c44e39c466b3325883bb7  {{LANE_INPUTS}}/laurent_pivot_formulas.py
2400fed2b859942374730fb415b3536aea233df8411c14b500b56145353ecda2  {{LANE_INPUTS}}/compact_remainder.py
53b9b3b43eaa067f4636df75dc6092fa74a1b3ee381ddac9abb53dcd0530c42e  {{LANE_INPUTS}}/terminal_laurent_model.py
516e5c18a8de582d8517aa503ef477d49ef8bd9c1f822f3cffc3b8805356bed5  {{LANE_INPUTS}}/compare_rebuild.py
22a762c2aa9667cb379800f065b2190def9d3a711341201af412220d4d5bbaea  {{LANE_INPUTS}}/derive_pivot_forms.py
```
