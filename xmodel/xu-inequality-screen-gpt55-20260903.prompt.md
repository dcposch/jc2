# Census lane: Xu's final-root intersection-number inequalities (arXiv:1604.07683 Theorems 3.4, 4.7, 5.1; IM ≥ Im) as a SKELETON-LEVEL SCREEN — source-read the theorems, verify them on Xu's own worked examples ((75,50) split (ii): Im = 6 > IM = 4 excluded; (84,56; M₂ = 64; V₂ = 2): Im = 5 > IM = 4 excluded; (84,56; M₂ = 72; V₂ = 5): Im = 4 ≤ IM = 10 not excluded), then apply them to the operative census (the 177 u_s > 1 groups at D ≤ 200 first, then the u_s = 1 residue)

Context (banked, AUDIT delta 17(zz)): Xu's paper (charged PDF) gives, for a
Jacobian pair with f_ξ = f − ξ generic, exact formulas and inequalities for the
intersection numbers I(f_ξ, f_y) and I(f_ξ, g) in terms of final major and
final minor π-roots (Theorem 3.4: I(f_ξ, f_y) = −Σ_σ (e(f_σ) − 1)λ_σ over split
π-roots; Theorem 4.7: final-minor inequalities; Theorem 5.1: I(f_ξ, g) from
final major roots); he applies them to Moh's table rows at skeleton level
(the quantities are computed from M, V, δ and the split data). The campaign's
operative screen C_FULL_TREE_POLYNOMIAL_ODE leaves 1,420 rows / 686 groups at
48 ≤ D ≤ 200, of which 310 rows / 177 groups have u_s > 1 (untouched by every
existing screen). Task: (1) SOURCE-READ Theorems 3.4, 4.7, 5.1 and §7.3 (page
images; name pages): state each precisely with its hypotheses, and state
EXACTLY which inputs are needed to evaluate IM and Im for a skeleton — which
are determined by (n, m, M_i, V_i, d_i, δ_i) alone, and which need the split
data of the minor roots (e.g. the number of final minor roots and their
multiplicities — is there a skeleton-level range, so that the inequality can
be applied as a fail-closed necessary condition by minimising Im over the
allowed splits and maximising IM?); (2) replay Xu's three worked cases from
the skeleton data and reproduce his numbers exactly (this is the calibration
gate: no promotion without it); (3) implement the screen (box/xuscreen-
20260903/xu_screen.py importing the frozen moh_skeleton_full.py and
full_tree_partition.py; the group key and census as in the charged post-poly
census): for every operative-census row compute the fail-closed version of
IM ≥ Im (using the skeleton-only bounds; if a split datum is needed, take the
most permissive value and say so), report the counts killed per stratum
(u_s > 1 vs u_s = 1; s; two-point or not), the list of killed groups at D ≤ 120,
and whether Moh's six survive; (4) verdict: is IM ≥ Im a new independent
skeleton screen (name what it sees that PATH-ARITH + tree + ODE + POLY do
not), what it kills, and what it does NOT touch; bounded quantity + cheapest
test per OPEN; type every claim (SOURCE-READ / DERIVED / MEASURED);
FALLACY-v2 applies (a screen is a floor; fail-closed only). ≤ 90 min; no
ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(moh9966-B-lift, k16-middle-spine, k16-t4-normalizer-gate, chart-fix-d1zero,
bigrows-preprocess). Drivers to box/xuscreen-20260903/.
Report: xmodel/xu-inequality-screen-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 90 minutes.
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/post-poly-census-grok46-20260903.md
charged_input=box/postpoly-20260903/measure_postpoly.py
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/xu-inequality-screen-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
fcddd0b0a8164f84c8aeb2ebad326fd49687094db7baca7a29f19924dfd2689b  {{LANE_INPUTS}}/post-poly-census-grok46-20260903.md
d90d21768d2082b70fe0691fe57eb806c0cc889fe2b8e5ca158506e2948a798d  {{LANE_INPUTS}}/measure_postpoly.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
