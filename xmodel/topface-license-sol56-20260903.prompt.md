# Source + derivation lane: LICENSE THE TOP FACE OF A DESCENDED PAIR FOR u' = d₂' − V₂' ≥ 3 — the inverse-Prop-6.3 minor-disc split that Moh derives by hand on p.210 ("there are precisely three subdiscs which contain 2, 2, 6 roots of f"), as a general procedure from the descended datum; this unlocks 7 of the 10 COUNTING-BOUND two-point rows at D ≤ 200

Context (banked): the Theorem-1.2 two-disc order chart (delta 17(oo), 17(pp))
kills a descended two-point row only when the top face (the leading form of
the pair at the top disc, y^{V₂'}·(split of the u' remaining roots)) is fixed:
u' = 1 → y^{V₂'}(y − x), u' = 2 → y^{V₂'}(y² − x²) (Moh p.210's 2,2,6 for
(15,10; V₂ = 3) is the u' = 2 instance). For u' ≥ 3 the batch ran D1-only
charts with 41–230 unknowns (COUNTING-BOUND): (25,15;21;2;k=2) u' = 3;
(33,22;30;8;1) u' = 3; (35,20;31;2;2) u' = 3; (45,30;42;11;1) u' = 4;
(24,16;17;2;5) u' = 6; (49,14;46;4;1) u' = 3; (50,30;47;7;1) u' = 3; plus
(35,25;31;3;2) u' = 2 and (30,24;25;4;3) u' = 2 "fixed-if-licensed". Moh's
p.210 sentence: "the inverse transformation implies that there is a minor
disc, thus in the major disc D₂ there are precisely three subdiscs which
contain 2, 2, 6 of roots f" — i.e. the split of the u' non-π roots of the
top polynomial is forced by the ORIGINAL pair's minor discs pulled back
through Prop 6.3 (the descended pair is the image of the Keller pair; its
top-disc root configuration is the image of the original D_s configuration:
V_s roots at the centre π = 0 and u_s = d_s − V_s others, distributed in the
minor discs of D_s). Task: (1) SOURCE-READ pp.196–199 (Prop 6.3/6.4 and the
description of the minor discs of D_s for u_s ≥ 1), p.207 (the transformed
table's columns), pp.210–211 (the 2,2,6 derivation): state exactly what the
inverse transformation gives about the u' non-centre roots — their number,
their grouping into minor subdiscs, the multiplicities, and whether their
mutual distances (radii) are determined by the original tower data (Def
5.1 radii of D_s and its minor discs — Prop 4.4/4.6 at D_s) or are free;
(2) derive the general rule: given the ORIGINAL skeleton (n, m, M, V, d_s,
V_s, u_s) with u_s = 1, the descended top face is y^{V₂'}·Π(y − a_i)^{e_i}
with Σe_i = u' — determine (e_i) and any forced coincidences from the source
(if the minor-disc distribution is a free datum, say so: then the top face is
a FINITE CASE SPLIT over partitions of u', and the chart must be run per
case — count the cases for each of the 9 rows); (3) verify on the two Moh
instances: (15,10; V₂ = 3) must give 2,2,6 (i.e. u' = 2 split as two simple
roots — reconcile Moh's "2,2,6 of roots f" with y³(y² − x²)) and (16,12) must
give the single root; also the K = 16 t = 2 row (u' = 1); (4) emit, for each of
the 9 rows, the licensed top face(s) as explicit polynomials and the
resulting chart unknown counts (use the charged batch generator's counting
mode: python3 twopoint_order_batch.py --count or read the driver), so the
next batch can run them; if the case split makes a row cheap, RUN it
(Singular, modular then Q, ≤ 10 min each) and report; (5) verdict + bounded
quantity + cheapest test per OPEN; type every claim (SOURCE-READ / DERIVED /
MEASURED); FALLACY-v2 applies (a top face you cannot license is a slice).
≤ 90 min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress
lane reports (k16-t3-uniform, minor-dichotomy, twopoint-kills-gate). Drivers
to box/topface-20260903/.
Report: xmodel/topface-license-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 90 minutes.
charged_input=xmodel/twopoint-batch-gpt55-20260903.md
charged_input=box/twopoint-batch-20260903/twopoint_order_batch.py
charged_input=box/twopoint-batch-20260903/results.json
charged_input=xmodel/appii-uniform-test-grok46-20260903.md
charged_input=xmodel/appendix2-compiler-grok46-20260903.md
charged_input=box/appendix2/shape.py
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=xmodel/post-poly-census-grok46-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/topface-license-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
52ac2f50b9c14b258b706cef4e931ca9afa1057dc542f64003c8df43a14c8a1b  {{LANE_INPUTS}}/twopoint-batch-gpt55-20260903.md
db14cb1ef39da6277ec4edcd9988a17d38d8bc0062edca244af1155b820282eb  {{LANE_INPUTS}}/twopoint_order_batch.py
f42e463a190f4c2fbdc2bade7e33edb6554018c5831e07844f4276f181b458ae  {{LANE_INPUTS}}/results.json
f5ace7bc8fcf8554169154354f0f0972641aeaeb82dcfa42a7f4035b39d4e1b5  {{LANE_INPUTS}}/appii-uniform-test-grok46-20260903.md
dea9f5be619b9507b5ca30db51ddd88401b293e7ab7a0e75c8ae8083a5c79c27  {{LANE_INPUTS}}/appendix2-compiler-grok46-20260903.md
d8750d4e512645366e9e0c53153484eb5daa9c785434c1cc59658986d0ab138c  {{LANE_INPUTS}}/shape.py
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
fcddd0b0a8164f84c8aeb2ebad326fd49687094db7baca7a29f19924dfd2689b  {{LANE_INPUTS}}/post-poly-census-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
