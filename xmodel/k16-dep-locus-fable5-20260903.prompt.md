# Decisive lane (Card C of your own round submission, coordinator-adopted; it decides what "the uniform K16 statement" IS): test CONJECTURE DEP — V(I_{t,+}) ∩ {τ_t = 0} = { ansatz pairs (P,Q) of the chart with J(P,Q) ≡ 0 } = { P = φ(H), Q = ψ(H) } — and, if it holds, test DEP-EMPTY at t = 8 by the direct dependent-pair system, which is far smaller than the Gröbner-exhausted cone

OPERATIONAL: skeleton first; every job in the foreground with `timeout
1800`; never end the turn with a job running; ≤ 3 cores. The round is over
(all five 20260904T0000Z submissions are sealed; you may read them, in
particular Opus's V5/V6: b₃, b₄ ARE Moh's p. 208 h-tower coefficients and the
K16 terminal cone is the coefficient system of an approximate-root tower
with (deg_h ḡ, deg_h f̄) = (3t+1, 2t+1) — use this reading if it helps
rebuild (P,Q)). Steps: (1) at t = 2, y = 1/5, take a b₃-axis cone point
(banked: the cone is the b₃-axis there, τ_2 vanishes on it, 17(cccc)),
rebuild the actual ansatz pair (P,Q) of the chart from the residual point
(the chart definition is in the charged Sol/Fable terminal-proof reports
and the terminal_laurent_t2.json record), and compute J(P,Q) exactly: DEP
predicts J ≡ 0. If J ≠ 0, DEP is false — report the value, withdraw §1.2's
reading, and say what the τ = 0 part of the cone is instead; (2) if J ≡ 0,
exhibit H with P = φ(H), Q = ψ(H) (Gordan–Noether/Schinzel; gcd of fibres) and
verify; also do the same at one t = 3 point if any cone point with τ = 0
exists there (there is none: dim 0 and τ ≠ 0 at the origin only — state
it); (3) re-derive line by line whether Δ ≡ 0 together with (D1)–(D3) is
literally J(P,Q) ≡ 0 for the chart's polynomial pair (your own flagged gap:
the scalar g = g₃ in (D1)–(D3)); (4) at t = 8: set up the DEPENDENT-PAIR
SYSTEM — H = h + Σ ε_j h^{−j} in the chart's support, φ, ψ univariate of
degrees 3t+1, 2t+1 (linear in φ, ψ for fixed H), intersected with the order
rows and the gauges — and solve it (modular first, exact if cheap): DEP-EMPTY
at t = 8 ⇒ (V0) is not refuted there; DEP-EMPTY fails at t = 8 with a witness
⇒ (V0) FAILS at t = 8 (report the witness and check it against the cone rows
directly) and the campaign retargets to (8.1) — either outcome is decision-
grade; (5) if time permits, t = 9, 10; (6) FALLACY-v2 audit; verdict DEP
CONFIRMED/REFUTED at t = 2; DEP-EMPTY at t = 8 HOLDS/FAILS/TIMEOUT with the
exact system size. ≤ 170 min; no ledger edits; no jc2-lean; no in-progress
lane reports (k16-square-resultant, k16-square-tail-stdhilb, g9966-chart-
necessity, minor-residue-formula, row2515-order-gate, g108-nosplit-descent
are running). Drivers to box/k16dep-20260903/.
Report: xmodel/k16-dep-locus-fable5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 170 minutes.
charged_input=xmodel/ideation-20260904T0000Z-fable5.md
charged_input=xmodel/ideation-20260904T0000Z-opus5.md
charged_input=xmodel/k16-terminal-proof-fable5-20260903.md
charged_input=xmodel/k16-terminal-proof-sol56-20260903.md
charged_input=xmodel/k16-cone-gate-gpt55-20260903.md
charged_input=xmodel/k16-toptail-quadratics-fable5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16spine-20260903/terminal_laurent_t2.json
charged_input=box/k16spine-20260903/terminal_laurent_t5_b4_1_exact_status.json
charged_input=box/k16spine-20260903/terminal_laurent_t4.json
charged_input=box/k16spine-20260903/terminal_laurent_t2_product_exact.json
charged_input=box/k16terminal-fable5-20260903/structure_rows.py
charged_input=box/k16terminal-fable5-20260903/b3_axis_closed_form.py
charged_input=box/k16terminal-fable5-20260903/finalize_report.py
charged_input=box/k16terminal-fable5-20260903/modstd_cert.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-dep-locus-fable5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
8da94c77300dddc8b6d3b9a548afa9be7e87b4eba361401c68d3543613f53457  {{LANE_INPUTS}}/ideation-20260904T0000Z-fable5.md
16bebf7d108bb280f46d854749f5d0531f8321da49fd9155b9360e36fb5f8f3f  {{LANE_INPUTS}}/ideation-20260904T0000Z-opus5.md
16d5112ae6ed9a6de0c504b11df2e19c97ed031a1715a3916fd8d207cdf0d961  {{LANE_INPUTS}}/k16-terminal-proof-fable5-20260903.md
401d374ecec0c556c7f7400ccade98571e1c1e93faf2daa1dd706f3b38c46391  {{LANE_INPUTS}}/k16-terminal-proof-sol56-20260903.md
444d1a9f5194f764ec7073d990f42d7c014b2c311431f84805015f2bdefcb080  {{LANE_INPUTS}}/k16-cone-gate-gpt55-20260903.md
638f5e2ed6755b32b92944830e32f6b4a67d321a9e442adca9a59f2f4ba5b05c  {{LANE_INPUTS}}/k16-toptail-quadratics-fable5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
234da78b92c8e5afd95919fa0ae4597cd2fca272653b88f3365261ac327e445a  {{LANE_INPUTS}}/terminal_laurent_t2.json
e56ee5ccb829f3b3c4279a484cdeac2ec4d0020f832e0fe1d930dfe03224bc78  {{LANE_INPUTS}}/terminal_laurent_t5_b4_1_exact_status.json
0c6adb555b07624bac34ed2862ea259a4258f099d54a84f09d5b3824bda5858a  {{LANE_INPUTS}}/terminal_laurent_t4.json
0f23c4d7996a5d915909c87e7d5f0bc1123f8fbc6677559ca188f40e002d7501  {{LANE_INPUTS}}/terminal_laurent_t2_product_exact.json
733bc7b3f6a06b1afc463d325d8e2e42e84227551f071171be8a2af69f0343ab  {{LANE_INPUTS}}/structure_rows.py
17857b1b0da4ea4166c1712fbac1f02e1fc70b3c991e69163db186db00f9a20b  {{LANE_INPUTS}}/b3_axis_closed_form.py
05a648ed2de67394bb2069ec6a85f34a557eadf94045937348d2bec2ba5d0ac1  {{LANE_INPUTS}}/finalize_report.py
688b46890a8079bb778062022f7d3bc87dc428fae443a0ebd467010bf98dba2e  {{LANE_INPUTS}}/modstd_cert.py
```
