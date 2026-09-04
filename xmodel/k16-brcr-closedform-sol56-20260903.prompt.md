# STRUCTURAL enabler lane (the concrete missing piece of OPEN[K16-Q-NONVANISHING-ON-GAMMA], flagged by all three K16 lanes 17(ppppp)/(rrrrr)/(uuuuu)): derive the CLOSED FORM in t of the coefficients b_r, c_r (equivalently B_r, C_r) of the split tail rows — G_r = a₀T_{t,2t−1−r} − a_r T_{t,2t−1} = B_r b₃ + C_r, and the top row T_{t,2t−1} = a₀ b₃² + b₀ b₃ + c₀ with a₀ = −α_t a unit — from the closed indexed forms of T_{t,k} (17(zzz) §2, 17(iiii) §2) and the truncated spine that already gives a_r (17(wwww): a_r involves only q_{2,0..r,0}, computed by 2r+1 scalars), then USE the closed form to attack the uniform nonvanishing of Q_t = a₀β² + b₀β + c₀ on the Eagon-Northcott curve Γ = V(I₂(N)), N = (C_r, B_r)

OPERATIONAL: skeleton first; exact CAS (sympy/generating functions), FOREGROUND
under `timeout 1200` and `stdbuf -oL` for any Singular; never end the turn with
a job running; ≤ 3 cores. This is a DERIVATION, not a Gröbner search (fixed-t is
exhausted; do NOT run large std jobs). Use the charged hsop and rank reports as
the spec (TAIL-SPLIT, FITT, EN-CURVE, the eliminant W_r, LENGTH-SPLIT). Task:
(1) from T_{t,k} = −[w^{4t+1−k}]σ_t(Δ) (the spine substitution), write T_{t,2t−1},
T_{t,2t−2}, …, T_{t,t} as explicit polynomials in b₃ over P_t = A_t[b₄, q_{2,0..t−1,0}]
at t = 3, 4, 5, 6 and EXTRACT b₀, c₀ (the b₃-linear/constant parts of the top
row) and B_r, C_r for r = 1..t−1; tabulate their supports and, crucially, their
LEADING coefficients as functions of (t, r); (2) find the CLOSED FORM in (t, r):
the truncated spine gives a_r as a rational function of (t, d) for fixed r
(17(wwww)); extend the SAME spine recursion to b_r, c_r — they are the next
two coefficients in the b₃-expansion, so they should be one and two spine-steps
deeper; derive the recursion and solve it in closed form (or identify the
generating function); (3) with b₀, c₀, B_r, C_r in closed form, restrict Q_t to
Γ: on a rank-1 point the kernel is (1:β) with (C_r, B_r) all proportional, so β
= −C_r/B_r is FORCED (same for all r on Γ — that is the rank-1 condition);
substitute β = −C_1/B_1 into Q_t = a₀β² + b₀β + c₀ and clear denominators:
Q_t vanishes on Γ ⟺ a₀C_1² − b₀B_1C_1 + c₀B_1² = W_1 vanishes on Γ (consistent
with 17(rrrrr)); now with the CLOSED forms, is W_1 (or the gcd of the W_r) a
UNIT on Γ, or does it vanish somewhere? prove the uniform nonvanishing OR find
the vanishing locus (if it vanishes, that is a candidate (V0)-failure point at
large t — check it against the cone directly); (4) the t = 2 control: b₀, c₀ at
t = 2 must reproduce the y = 1/5 (dim 1, the b₃-axis, Q_2 vanishes) vs y = 2/5
(dim 0, Q_2 nonzero) split — verify the closed form gives this; (5) verdict:
OPEN[K16-Q-NONVANISHING-ON-GAMMA] RESOLVED (Q_t nonvanishing on Γ for all t ⇒
(V0) ⇒ (T) on the whole ray — full chain) / the closed form of b_r, c_r
DERIVED with the nonvanishing reduced to an explicit one-variable statement in t
/ PARTIAL with the exact residual. FALLACY-v2 applies. ≤ 180 min; no ledger
edits; no jc2-lean; no ideation-* files; no in-progress lane reports (k4ray-
unsplit-lemma running). Drivers to box/k16brcr-20260903/.
Report: xmodel/k16-brcr-closedform-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-40KB; 180 minutes.
charged_input=xmodel/k16-rank-criterion-fable5-20260903.md
charged_input=xmodel/k16-hsop-length-allt-opus5-20260903.md
charged_input=xmodel/k16-nzd-gamma-gpt55-20260903.md
charged_input=xmodel/k16-toptail-quadratics-fable5-20260903.md
charged_input=xmodel/k16-terminal-proof-sol56-20260903.md
charged_input=xmodel/k16-terminal-proof-fable5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16rank-20260903/singular_terminal_driver.py
charged_input=box/k16rank-20260903/killmine.py
charged_input=box/k16rank-20260903/en_degree.py
charged_input=box/k16rank-20260903/tail_structure.py
charged_input=box/k16rank-20260903/hilb_compare.py
charged_input=box/k16rank-20260903/rank_driver.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-brcr-closedform-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
7cfa230c0c9ec1b4124b9581b1c461cb19ef004e8a36c2820e7efece0fb185c5  {{LANE_INPUTS}}/k16-rank-criterion-fable5-20260903.md
a2637d38f715334fec463d947c6be29d2efd93e9ee2175a57e9e6eda266edd83  {{LANE_INPUTS}}/k16-hsop-length-allt-opus5-20260903.md
fa2d48ba8174e3b19c54aeab10d6a8b5f964d3c2c4542c15cee0df18ce085e7f  {{LANE_INPUTS}}/k16-nzd-gamma-gpt55-20260903.md
638f5e2ed6755b32b92944830e32f6b4a67d321a9e442adca9a59f2f4ba5b05c  {{LANE_INPUTS}}/k16-toptail-quadratics-fable5-20260903.md
401d374ecec0c556c7f7400ccade98571e1c1e93faf2daa1dd706f3b38c46391  {{LANE_INPUTS}}/k16-terminal-proof-sol56-20260903.md
16d5112ae6ed9a6de0c504b11df2e19c97ed031a1715a3916fd8d207cdf0d961  {{LANE_INPUTS}}/k16-terminal-proof-fable5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
0cc821ff59adc955d2c6c33a572766b01569d578f1034f343c4f3661cebcf8ed  {{LANE_INPUTS}}/singular_terminal_driver.py
cb3bb83a0ee477093abc0df9581050e6803679ac455ba07e1f76889bee1bb6b2  {{LANE_INPUTS}}/killmine.py
a6c2a657132cb8da333ea7763c1a8185deaeb3e48e4925e02d222ae6e5b0bea7  {{LANE_INPUTS}}/en_degree.py
21908d554bd41347fc651faf03093a43d97e9a44aab82245d54b2e129d6a8a75  {{LANE_INPUTS}}/tail_structure.py
299ed379a67d2dd72f7c9f626f83e9e73b8c05f7cbac7d1f5f2242de21811dfc  {{LANE_INPUTS}}/hilb_compare.py
a5abc269e3ecf919e63fb2f934e5a3b8bdca5fad6bf3702621de394fff7ffdf1  {{LANE_INPUTS}}/rank_driver.py
```
