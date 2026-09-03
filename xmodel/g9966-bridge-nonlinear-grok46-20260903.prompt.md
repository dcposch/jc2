# Computation lane: OPEN[EFFECTIVE-T2-T3-BRIDGE] for (99,66) — write the residuals of T₂(G,F) = G³ − F² + c₀G² + (a₁F + a₀)G + (b₁F + b₀) and T₃(G,F) = G⁹ − F⁶ + Σ α_i(F)G^{9−i} on the ACTUAL minor jets of F, G at the second point at infinity (both branches), and match them to the minor leaders T₂(σ) ∼ p⁵ and T₃(σ) ∼ R = π²⁵(π + 3a)¹⁴(π − 2a) (δ = 2) / p¹⁰q₁ (δ = 5/2) — the nonlinear bridge rows the joint chart still lacks

OPERATIONAL (mandatory): write the report skeleton first; launch long jobs
with caps; poll them in a loop; never end your turn with a job running.
Context (banked, AUDIT deltas 17(ttt), (aaaa), (dddd)): the joint chart's linear
content is now complete (outer Theorem-1.2 bands: 5,774 pivots; relaxation
930 / 928 free coefficients); the effective quasi-approximate roots have the
printed shapes above (Moh p.152, Xu §7.3; chart convention F = Moh's g of
degree 99, G = Moh's f of degree 66; T₀ = F, T₁ = G; deg_y T₂ = 55, T₃ = 145;
4 + 34 unknown coefficients after Tschirnhausen); the minor blocks constrain
the π-root data of T₂, T₃ at the second point (the radius-two leaders), but
after the monic cancellations the Tschirnhausen span on the LEADING pair
(F,G) ∼ (p⁹, p⁶) contains neither p⁵ nor the degree-40 shapes — the leaders are
residuals of SUBLEADING F, G jets, so the bridge rows are nonlinear in the
chart coordinates. Task: (1) SOURCE-READ Moh pp.150–152 (T_i^ψ construction)
and Xu §7.3 (page images; name pages); confirm the shapes and the Tschirnhausen
normalisation; (2) in the chart's coordinates at the second point (the minor
line y = 0; the principal-minor π-root σ with the branch's split datum: δ = 2
[2,1] H = π²(π + 3a), R as above, packets 18 + 9; δ = 5/2 p = π(π² − c), q =
p¹⁰q₁, q₁ = −2∫p³), expand F(σ), G(σ) to the order needed (the minor jets: which
chart coefficients of F, G appear at each t-order at the second point — list
them; these are the "subleading jets"), substitute into T₂(G,F) and T₃(G,F),
and impose: ord T₂(σ) and its leading polynomial ∼ p⁵ (Xu: T₂(σ) = p⁵t^{5(−8+3δ)}
+ …), ord T₃(σ) = 13(−8+3δ) − 1 + δ with leading polynomial ∼ R (δ = 2) / p¹⁰q₁
(δ = 5/2); the resulting equations in (the 4 + 34 T-coefficients, the chart's
minor-jet coefficients, a or c) are the bridge rows — emit them; count
unknowns and equations; report which are linear in the chart coordinates
(after fixing the T-coefficients) and which are not; (3) add them to the
reduced relaxation (the 930/928 space of the charged outer-bridge lane:
box/g9966outer-20260903/ add-on + the charged chart driver) and run Q*-pivot
elimination followed by modular standard bases (three primes, ≤ 20 min
each; 4 cores) on the union for each branch; report the new dimension or a
kill certificate; (4) controls: on (64,48) → (16,12) (u_s = 1) the bridge must
be trivially satisfied (report); on the automorphism control degrees (1,1)
NOT-APPLICABLE — construct instead a second control with a genuine second
point at infinity in degrees ≥ 6 (compose triangular automorphisms so that
the leading form has two distinct linear factors) and check the bridge rows
are satisfied by it (must SURVIVE); (5) verdict per branch (SATURATED-EMPTY /
COUNTING-BOUND with dimension and next system / REPRESENTATIVE only with a
full pair and a direct Jacobian check); FALLACY-v2 applies. ≤ 150 min; no
ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(g9966-global-band, k16-*, preprocess-native). Drivers to
box/g9966bridge-20260903/.
Report: xmodel/g9966-bridge-nonlinear-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 150 minutes.
charged_input=xmodel/g9966-outer-bridge-grok46-20260903.md
charged_input=xmodel/g9966-design-gate-grok46-20260903.md
charged_input=xmodel/g9966-global-design-sol56-20260903.md
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md
charged_input=box/g9966outer-20260903/controls.json
charged_input=box/g9966outer-20260903/outer_order_bands.py
charged_input=box/g9966outer-20260903/driver.py
charged_input=box/g9966outer-20260903/outer_order_bands.json
charged_input=box/g9966outer-20260903/controls.py
charged_input=box/g9966outer-20260903/t2t3_bridge.json
charged_input=box/g9966outer-20260903/results.json
charged_input=box/g9966outer-20260903/t2t3_bridge.py
charged_input=box/g9966-20260903/joint_probe.py
charged_input=box/g9966-20260903/minor_row_count.json
charged_input=box/g9966-20260903/major_h2_probe.py
charged_input=box/g9966-20260903/joint_probe-results.json
charged_input=box/g9966-20260903/minor_row_count.py
charged_input=box/g9966-20260903/major_h2-results.json
charged_input=box/g9966-20260903/major_tower_joint/major_tower_structure.py
charged_input=box/g9966-20260903/major_tower_joint/major_tower_structure.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-bridge-nonlinear-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
7facb109db6eb21b73970c2b6a0d4339bc51c7b73f3ce16782950550508e2674  {{LANE_INPUTS}}/g9966-outer-bridge-grok46-20260903.md
0cbeaf0735b92f18e3a7c5050775b99c3739b658584ce0d02965a24db2c1273b  {{LANE_INPUTS}}/g9966-design-gate-grok46-20260903.md
a81ff0263cf379a297b8d1812ebfa26eb95f7e58d91ef4edc62a3a68edf2d782  {{LANE_INPUTS}}/g9966-global-design-sol56-20260903.md
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
b59498485cdb36c37d454e74c7cb1a2ca9d24256a9fbc92b48fa5bbc50ce63bc  {{LANE_INPUTS}}/controls.json
5b51e91b820a623c614622626f4df7e3c8144bfff3603a030a771de7b1e77421  {{LANE_INPUTS}}/outer_order_bands.py
12d8f9d09cb41e1e0a27a9654ce12da1304ad4baff7286ff7a28a16b946bab8c  {{LANE_INPUTS}}/driver.py
b7a4540dc609ada9f9d6af7ad99a312afed25d69fa1bec4ddb8eb7434324516b  {{LANE_INPUTS}}/outer_order_bands.json
cb616b8ee886097ace1f74a8f0c5307d1882f8a9ecd54742839577833f2f66a7  {{LANE_INPUTS}}/controls.py
3071eac0fbc2215d2b18e9d3bb423722e341ab4a501a69dd49a42dd04753ccfe  {{LANE_INPUTS}}/t2t3_bridge.json
6060b0e86b285e4a55cdaa1ba13652953b6357f7377c8ba89eee274bf7d23ff9  {{LANE_INPUTS}}/results.json
8c4251c5958b8f9cad6089d16c6b1d49786a0db35c90b9ec6755559a19822349  {{LANE_INPUTS}}/t2t3_bridge.py
6acd8b467369aa33a07482f341c86a48686db55950666ad70455d344301dc021  {{LANE_INPUTS}}/joint_probe.py
a62385d3432555946199dba6f6189dc74227e351e7aa0da3bc32c5b690837fe0  {{LANE_INPUTS}}/minor_row_count.json
8463c689fd5251219f36e7239ab13f7e3ebd053972809e0f3720295beac07780  {{LANE_INPUTS}}/major_h2_probe.py
ed8cabc25df5dc8250f504df63444591d618380af0cf68f5378dd6ce2e97f587  {{LANE_INPUTS}}/joint_probe-results.json
4e88918b8e08f3cb63da746b1155e9fbce5c045d61b4a5fff87970c7869250b7  {{LANE_INPUTS}}/minor_row_count.py
6a4826431f03210cf4b9c13001108ba741a098aca7ddba8e53551a5fa5c7ec44  {{LANE_INPUTS}}/major_h2-results.json
555af27d631772f39e6f60f7b537a952190d21fd6f05ae94bbae84e1add7dea8  {{LANE_INPUTS}}/major_tower_structure.py
77d791b33e5bfd2e2aecaff67faf72acb1c3b2560b1ff86157a22a121956989f  {{LANE_INPUTS}}/major_tower_structure.json
```
