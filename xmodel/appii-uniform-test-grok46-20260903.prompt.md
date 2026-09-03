# Research lane (bounded computation): the cheapest test of CONJ[APPII-UNIFORM] — run Moh's p.210 Appendix II reduction with the DESCENDED order conditions on G2 (15,10; 4; 1; X⁴), on the control family P = π⁵ − γ⁵, Q = P³ + aπ (must SURVIVE), and on Moh's (15,10; 11; 3; X²) (must be SATURATED-EMPTY, with ERRATUM[APPII-GAMMA-B])

Context: prop55k-opus5-20260903.md (charged; PROVISIONAL, delta 17(z)) proves the
radii rule Φ (δ^{(k)} = (k+1)δ^{(0)}) with closed form δ₂' = −(k+1)/R, δ₁' =
(k+1)(ΠU₂' − R)/(R(ΠV₂' − 1)); shows PROP 5.5(k) is sharp for k ≥ 1 and does
NOT give theorem (T); names the filling datum as CONJ[APPII-UNIFORM] (§4.2):
with h the approximate root of P of degree d₂' = gcd(n', m'), P = h^{m*} +
Σ_{i≥2} β_i h^{m*−i}, Q = h^{n*} + Σ_{i≥1} α_i h^{n*−i}, deg_π α_i, β_i < d₂',
the pair is excluded by (a) the order conditions ord α_i(σ) ≥ i·δ₁', ord β_i(σ)
≥ i·δ₁' forced by the descended δ₁' (Moh's "ord α_i(σ) ≥ i(−1/4)", p.208),
(b) the remainder-degree bounds (deg γ < d₂', deg ε, δ < d₂' − 1 at the second
level), (c) the minor-disc root split of P inside D₂ forced by the inverse of
Prop 6.3 (for (15,10): 2, 2, 6), together with polynomiality of Q
(cancellation of the π^{-1}-tail). Cheapest test named by the producer:
instantiate (a)–(c) on G2 (15,10; M₂' = 4; V₂' = 1; X⁴; d₂' = 5, n* = 3,
m* = 2, δ₁' = 5/4, δ₂' = −1/2) — i.e. the (15,10)-shaped p.210 reduction with
order conditions from δ₁' = 5/4 instead of 1/2 — and on one member of the
control family that must NOT die (P = π⁵ − γ⁵, Q = P³ + aπ; d₂' = 5, n* = 3,
m* = 1; J = −5aγ⁴). Task: (1) SOURCE-READ pp.207–211 (page images, pdftoppm
-r 200; name the pages); write the reduction as a general routine (inputs:
n', m', M₂', V₂', k, δ₁', δ₂' from the closed form; output: the polynomial
system in the α_i, β_i coefficients after (a),(b), the π^{-1}-tail
cancellation, and the root-split (c) where licensed) in
box/appii-uniform-20260903/; (2) positive control: Moh's (15,10; 11; 3; X²)
must come out SATURATED-EMPTY (reproduce the campaign's corrected Case 2 —
ERRATUM[APPII-GAMMA-B], see the charged descent-radii report §4 and the
m2descent controls); second positive control: (16,12; 13; 3; X) SATURATED-
EMPTY; (3) negative control: the family member P = π⁵ − γ⁵, Q = P³ + aπ must
SURVIVE every step of (a),(b) and the tail cancellation (if it dies, the
routine over-constrains — say which step); (4) G2: run the routine; report
SATURATED-EMPTY (certificate: the ideal, saturation by leading coefficients,
Gröbner basis {1}, size/time) or SURVIVES (print the component and a point; is
it a genuine pair with J = cγ⁴? — check by direct differentiation) or
COUNTING-BOUND (exact unknown/equation counts and what exceeds one core);
note that (c) is only licensed if the inverse-descent split is derived, not
assumed — run with and without (c); (5) verdict on CONJ[APPII-UNIFORM] at
this instance and what generalises; bounded quantity + cheapest test for
every OPEN. Type every claim; FALLACY-v2 applies (no promotion of controls;
G2 is a D = 105 descendant and D = 105 is already TREE-empty — a G2 kill
proves the METHOD, not a frontier theorem; say so). Desk-scale; ≤ 75 min one
core; sympy (Singular/Macaulay2 if present — check `which Singular M2`);
no ledger edits; no jc2-lean; no ideation-20260903T1200Z-* files; no
in-progress lane reports.
Report: xmodel/appii-uniform-test-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 75 minutes.
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=box/prop55k-drivers-20260903/prop55k.py
charged_input=box/prop55k-drivers-20260903/control_pairs.py
charged_input=xmodel/descent-radii-grok46-20260903.md
charged_input=box/descentradii-drivers-20260903/g2_fullh_mohbeta.py
charged_input=box/descentradii-drivers-20260903/g2_case_p0.py
charged_input=box/descentradii-drivers-20260903/g2_highy.py
charged_input=box/m2descent-drivers-20260903/moh_1510_control2.py
charged_input=box/m2descent-drivers-20260903/moh_1510_controls_pm.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/appii-uniform-test-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
802aaf1e3450fd460a9d5c0aa998720c8da2fabedfea3df3c69e0407869ee34d  {{LANE_INPUTS}}/prop55k.py
9e0ea7b64cae7c2e5d46712520843139b040f4a17e11aa702991e453e8f13d44  {{LANE_INPUTS}}/control_pairs.py
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  {{LANE_INPUTS}}/descent-radii-grok46-20260903.md
69a884c81cdc1d68f45e9b75aa2c9ee4f64bd24cdb49f90bc7c7d43784bdfdd6  {{LANE_INPUTS}}/g2_fullh_mohbeta.py
d59456f74d712aee9ad0ef35ff2bbb22263243b09ffecdddd2f1bbd795ccdde9  {{LANE_INPUTS}}/g2_case_p0.py
a438aee4ba19c9bb1c36a8298784d4aee8bbaf97ec71adade2bc2b744a490871  {{LANE_INPUTS}}/g2_highy.py
5ea3845b6e6f7022a59b0620b22f017c632ef08e6e5d0675f9c3d0274032566b  {{LANE_INPUTS}}/moh_1510_control2.py
add00ccc08951cc356891e3198bb39bf8ae5b55ffd182354ace7ba8a8ef3aa8a  {{LANE_INPUTS}}/moh_1510_controls_pm.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
