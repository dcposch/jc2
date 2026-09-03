# Derivation lane (pure algebra, no background jobs; the one OPEN blocking the D = 108 band run — AUDIT delta 17(ssss) §6): rerun the charged (99,66) outer-bridge derivation for the D = 108 row (108,72; M = (−72,81,106); d = (108,36,9,1); V = (7,7); tower y-degrees 9 ⊂ 36 ⊂ 108/72; d₂/d₃ = 4) to produce the D₂ weight cut and the D₁ boundary bands under A₂ = 4, A₁ = 2, weight = 4r + 6q — i.e. OPEN[108-OUTER-WEIGHTS]

Context (banked): at (99,66) the outer bridge (charged Grok report) derived
the Theorem-1.2 order rows in the h-chart, the D₂ support preblock and the
D₁ boundary bands with exact weights and counts, and the engine reproduced
its 5,774 outer pivots; the D = 108 classification (charged Opus report, §3)
gives every engine constant DERIVED except the outer weights. Task: (1) from
Moh Thm 1.2 / Prop 6.2 (charged PDF) and the (108,72) tower, derive the
weight cut for D₂ (the top two-line form's support under A₂ = 4) and the D₁
boundary bands under A₁ = 2 with weight 4r + 6q: exact band indices, the
number of unknowns per band, the number of order rows per band, and the
expected outer rank (state the general formula in (n, m, d₂, d₃) and specialise
to both (99,66) — must reproduce the charged numbers — and (108,72)); (2) the
h₃ → h₂ step with d₂/d₃ = 4 (not 3): write the Theorem-1.2 rows for the
9 ⊂ 36 inclusion explicitly (count the unknowns: 8,694 monic coefficients per
the classification; check); (3) list the DERIVED engine constants for
(108,72) in the same table format as the (99,66) design (charged Sol design
report) so that an engine lane can consume them mechanically (JSON to
box/g108bridge-20260903/constants.json); (4) controls: the (99,66)
specialisation reproduces the charged bridge numbers exactly; (64,48)
specialisation is stated; (5) FALLACY-v2 audit; verdict DERIVED / PARTIAL
with the exact residual. Pure derivation with small exact scripts (sympy /
python, foreground, ≤ 10 min each); no long jobs; ≤ 90 min; no ledger edits;
no jc2-lean; no ideation-* files; no in-progress lane reports (g108-joint-band,
g9966-*, k16-*, order-chart-general).
Report: xmodel/g108-outer-bridge-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-16KB; 90 minutes.
charged_input=xmodel/g108-minor-classification-opus5-20260903.md
charged_input=xmodel/g9966-outer-bridge-grok46-20260903.md
charged_input=xmodel/g9966-global-design-sol56-20260903.md
charged_input=xmodel/g9966-global-band-sol56-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/g9966outer-20260903/controls.json
charged_input=box/g9966outer-20260903/outer_order_bands.py
charged_input=box/g9966outer-20260903/driver.py
charged_input=box/g9966outer-20260903/outer_order_bands.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g108-outer-bridge-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
8b97a8972cff0dfccfa9396bae8849dbda4318fb47150645e76d55785d9decd3  {{LANE_INPUTS}}/g108-minor-classification-opus5-20260903.md
7facb109db6eb21b73970c2b6a0d4339bc51c7b73f3ce16782950550508e2674  {{LANE_INPUTS}}/g9966-outer-bridge-grok46-20260903.md
a81ff0263cf379a297b8d1812ebfa26eb95f7e58d91ef4edc62a3a68edf2d782  {{LANE_INPUTS}}/g9966-global-design-sol56-20260903.md
0c8dc291e306f15806e6c14099ab69feda9d1532abcbc22e79e55b02df427701  {{LANE_INPUTS}}/g9966-global-band-sol56-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
b59498485cdb36c37d454e74c7cb1a2ca9d24256a9fbc92b48fa5bbc50ce63bc  {{LANE_INPUTS}}/controls.json
5b51e91b820a623c614622626f4df7e3c8144bfff3603a030a771de7b1e77421  {{LANE_INPUTS}}/outer_order_bands.py
12d8f9d09cb41e1e0a27a9654ce12da1304ad4baff7286ff7a28a16b946bab8c  {{LANE_INPUTS}}/driver.py
b7a4540dc609ada9f9d6af7ad99a312afed25d69fa1bec4ddb8eb7434324516b  {{LANE_INPUTS}}/outer_order_bands.json
```
