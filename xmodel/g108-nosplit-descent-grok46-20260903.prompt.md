# Derivation lane (pure algebra, no background jobs): close OPEN[DESCENT-SUPPORT/VARIABLE-MAP] for the D = 108 row's NO-SPLIT alternative — the D = 108 row (108,72; M = (−72,81,106); d = (108,36,9,1); V = (7,7); u₃ = 2, v₃ = 7) has its only split branch DEAD (PROMOTED, AUDIT 17(ddddd)); on the no-split alternative the minor radius satisfies δ* ≥ v_s/u_s = 7/2, so Moh Prop 6.3's hypothesis holds and the pair DESCENDS. Make the descent rigorous: the exact descended datum (the charged Sol report gives (24,16; M₂' = 18, V₂' = 7; k = v_s − u_s − 1 = 4) — verify or correct), the variable map (how the (108,72) chart coordinates map onto the descended (24,16) chart, and which support conditions the descended pair inherits), and then decide the descended row: is (24,16) a banked-dead row (check the census/AUDIT: the (24,16)-type rows and their status), or does the charged compiler's DEAD diagnostic (26 rows, exact Q) become a kill once the variable map is sourced?

Context: Moh 1983 Prop 6.3 / 6.4 (charged PDF; page N = PDF page N−139) give
the descent of a Keller pair under a minor-radius hypothesis to a pair of
lower degrees with explicit new data; the banked descent machinery
(charged m2-descent and descent-radii reports; the Φ radii rule δ' = (k+1)·
Def 5.1(3) is a theorem) is the reference. Task: (1) state Prop 6.3's
hypothesis and conclusion exactly for this row, check δ* ≥ 7/2 is what the
no-split alternative gives (via Xu Prop 7.3 / the classification 17(ssss):
when no principal-minor split occurs the minor radius is ≥ v_s/u_s), and
derive the descended datum (n', m', M', V', d', k) — compare with the Sol
report's (24,16; M₂' = 18, V₂' = 7; k = 4); (2) the variable map: write the
descent as a substitution on the tower coordinates (h₃, h₂, F, G → the
descended tower) and list which coefficients of the (108,72) chart become
coefficients of the descended chart, and which descended coefficients are
forced (support conditions); (3) with the map sourced, evaluate: the
descended (24,16) datum — its height, whether it is a two-point (s' = 2) row
of the census, and its banked status (grep AUDIT/APPROACHES; the K = 16 ray
descendants (12t+4, 8t+4) are analogous — is (24,16) the t = 5/3 member? no —
say exactly which family it belongs to); if the descended row is banked
DEAD (or killed by the general order chart 17(zzzz)), the no-split
alternative is DEAD and the whole D = 108 row is closed at skeleton level —
state the dependency chain; (4) controls: replay the descent on (99,66)'s
no-split alternative (banked: branch A dead) and on (64,48) → (16,12)
(Appendix II); (5) FALLACY-v2 audit; verdict DEAD[D108-NOSPLIT] /
CONDITIONAL with the exact residual / OPEN. Small exact scripts only
(foreground, ≤ 10 min each); ≤ 120 min; no ledger edits; no jc2-lean; no
ideation-* files; no in-progress lane reports.
Report: xmodel/g108-nosplit-descent-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 120 minutes.
charged_input=xmodel/g108-joint-band-sol56-20260903.md
charged_input=xmodel/g108-minor-classification-opus5-20260903.md
charged_input=xmodel/g108-delta3-kill-gate-gpt55-20260903.md
charged_input=xmodel/order-chart-general-gpt55-20260903.md
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=xmodel/descent-radii-grok46-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md
charged_input=box/g108band-20260903/descent.stdout.json
charged_input=box/g108band-20260903/descent-run/descent.json
charged_input=box/orderchart-20260903/order_chart.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g108-nosplit-descent-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
02f18bfef26ba5d3b75b8a5e53f0eaa90d707d14ca55b24870077b77382a6d70  {{LANE_INPUTS}}/g108-joint-band-sol56-20260903.md
8b97a8972cff0dfccfa9396bae8849dbda4318fb47150645e76d55785d9decd3  {{LANE_INPUTS}}/g108-minor-classification-opus5-20260903.md
7c14a90a47485d8ac7461a2b0019989dc09cc580cd33fb23a67b08afae48fe3b  {{LANE_INPUTS}}/g108-delta3-kill-gate-gpt55-20260903.md
4cdae04635f99bb35520b21c9c03d969f0d8bcc51412c51be274abf0efc05723  {{LANE_INPUTS}}/order-chart-general-gpt55-20260903.md
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  {{LANE_INPUTS}}/descent-radii-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
363ceec278582c4c503e8d717234684b75182c6371038e17d03e4667cfe9a01f  {{LANE_INPUTS}}/descent.stdout.json
363ceec278582c4c503e8d717234684b75182c6371038e17d03e4667cfe9a01f  {{LANE_INPUTS}}/descent.json
811a763816879e1205d224d7624237428a750fe17126d3d0e6b97fedf915f51e  {{LANE_INPUTS}}/order_chart.py
```
