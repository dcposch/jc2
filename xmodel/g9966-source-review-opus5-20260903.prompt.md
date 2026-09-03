# Fresh-eyes source review (page images): (99,66) — is there a route in Moh 1983 or Xu 2022 that excludes the two surviving branches (Moh's δ = 2 two-root cubic; Xu's δ = 5/2 split) which today's lanes missed? And what is the correct global object?

Context (banked today; read the charged reports first): Moh's degree ≤ 100
theorem is complete for (64,48), (84,56), (75,50) and OPEN at (99,66) (Xu
arXiv:1604.07683 §8 says so explicitly); today's lanes: branch A's linear-
power predecessor SATURATED-EMPTY; branch C (three simple cubic roots)
SATURATED-EMPTY at radius two; branch B ([2,1] cubic, packets 18 + 9) survives
its leading-face ODE and a banded zero-jet lift through band 5 with growing
dimension; Xu's δ = 5/2 split survives its local lift through s⁴; Moh's
(16,12) control dies under the same machinery; the Xu screen (IM ≥ Im with the
sharpened principal floor) does not kill (99,66) (IM_max = 16 vs Im_min = 8/3).
Task (hostile, source-first): (1) open Moh pp.190–199 (Props 6.1–6.4 and the
discussion between them), pp.207–211, and Xu pp.4–13 as page images (pdftoppm
-r 200; name every page you open) and look for ANY printed statement that
constrains the principal minor roots of a (99,66) pair beyond what the lanes
used — e.g. Prop 6.2 (what does it say? the lanes never cite it), the minor-
disc radius bound as a function of the major data (Lemma 5.2 / Def 5.1(3)
applied to the minor packet), Xu's Cor 7.5 and Prop 7.3 in their general
form (do they bound the split order from above/below? the denominator ≤ u_s
argument — does it exclude δ = 5/2 = 5/2 with denominator 2 ≤ 3? evidently not,
but check the exact statement), Xu's Theorem 4.7(i) applied with the exact
I(f_ξ, f_y) (Theorem 3.4) at (99,66) — compute both sides for each surviving
branch's split tree (the [2,1] tree at δ = 2 with the double packet unsplit
until final; the δ = 5/2 tree) and check whether EQUALITY constraints (not
just the inequality) exclude either; also the genus / Milnor-number
identities the campaign holds (AUDIT: MF-DEFECT, the unramified fibre map
identity of Fable's 1200Z §5.2, delta 17(x): g_gen ≥ 1) evaluated on the
(99,66) split trees; (2) state, as a typed list, every necessary condition
on a (99,66) pair that is now known, which branch each one leaves open, and
the single cheapest computation that would decide (99,66) (be concrete:
which system, how many unknowns, which tool); (3) fresh eyes on the global
object: the local lifts at one π-root stay consistent with growing freedom
while (16,12) dies — explain structurally why (what closes (16,12): the
π^{-1} tail = polynomiality in the ORIGINAL coordinates at the SAME point at
infinity; at (99,66) branch B the closing constraint must come from the
OTHER point at infinity or from the total degree/Newton polygon of f, g);
propose the exact joint object and its expected size; (4) verdict: the
(99,66) status after this review, typed, with bounded quantities and
cheapest tests; FALLACY-v2 applies. Desk-scale (≤ 75 min); no ledger edits;
no jc2-lean; no ideation-* files; no in-progress lane reports (g9966-global-
design, k16-middle-spine, bigrows-preprocess, strata-rerun-corrected, r3-
preprocess, xu-sametree). Drivers to box/g9966rev-20260903/.
Report: xmodel/g9966-source-review-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 75 minutes.
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=xmodel/moh9966-B-lift-sol56-20260903.md
charged_input=xmodel/xu-delta52-lift-gpt55-20260903.md
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/moh9966-branchB-sol56-20260903.md
charged_input=xmodel/xu-principal-floor-sol56-20260903.md
charged_input=xmodel/minor-dichotomy-sol56-20260903.md
charged_input=xmodel/ideation-20260903T1200Z-fable5.md
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-source-review-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
1d4ff2c76301705fbfa0f324862fe8f8065d57840fbb3094bce596f54c6651c6  {{LANE_INPUTS}}/moh9966-B-lift-sol56-20260903.md
1e3aafcae25d811f033a8deeff8daaee022735f9f09a9d4bd20499a56a44c899  {{LANE_INPUTS}}/xu-delta52-lift-gpt55-20260903.md
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
8338a702448a61ef10af214e5d156e0c14ad117ef231ae34aee462fb36fa649f  {{LANE_INPUTS}}/moh9966-branchB-sol56-20260903.md
759d54a7c346c0a063f88421d4bdf94dec438f4a7df219c5403b3770afc271e2  {{LANE_INPUTS}}/xu-principal-floor-sol56-20260903.md
184a689f3cd63405d922b8118632c7e17f96f471a0bc71f9a50cd161b8a87ad1  {{LANE_INPUTS}}/minor-dichotomy-sol56-20260903.md
8d16a66112afda4aafa4b81a55a07602677d3707d60a150e3d13edb8be467e80  {{LANE_INPUTS}}/ideation-20260903T1200Z-fable5.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
