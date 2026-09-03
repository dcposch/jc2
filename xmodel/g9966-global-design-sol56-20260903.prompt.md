# Design + computation lane: THE JOINT SYSTEM FOR (99,66) — a Keller pair f, g ∈ k[x,y] (monic in y, deg = deg_y, degrees 99, 66, J = 1) must satisfy Moh's major-tower conditions at the first point at infinity (M = (−66,77,97), V = (8,8), d = (99,33,11,1), radii δ = (4/9, 1/3, −1)) AND the principal-minor split conditions at the second point (either Moh's δ = 2 two-root cubic branch or Xu's δ = 5/2 split) SIMULTANEOUSLY, with finite support — build that joint object, count it, and decide as far as the budget allows

Context (banked, AUDIT deltas 17(qq), (tt), (yy), (zz), (aaa), (ggg)): every LOCAL
computation at (99,66) — branch A's predecessor (dead), branch C (dead), branch B's
banded lift (consistent through band 5, fibre dimension 59), Xu's δ = 5/2 lift
(consistent through s⁴, dimension 4) — shows that conditions at ONE π-root are
satisfiable with growing freedom, exactly as delta 17(ee) found for node-local
sibling conditions on the major tree; Moh's (16,12) control DIES under the same
banded lift (17(ggg) §7.3), so the machinery is sound: the difference at (99,66)
is that no lane has imposed the two points at infinity jointly with global
polynomiality. Task: (1) DESIGN: write the most economical exact ansatz for
(f, g): (a) the major-tower side — Moh's Appendix II style approximate-root
chart for the tower (M, V, d, δ) at the first point at infinity (the campaign's
two-point order chart generalised to s = 3: h₃ (degree 11 = d₃ in y) ⊂ h₂
(degree 33 = d₂) ⊂ f, with the Theorem-1.2 order bounds from the radii and the
Lemma 2.1 support), (b) the minor side — the leading form at the second point
y − a₁x with multiplicity data from Xu §7.3 (principal minor roots: multiplicity
u_s·m/d_s = 3·66/11 = 18 for f? — derive) and the split datum (δ = 2 [2,1] or
δ = 5/2 with p = π(π² − c)), (c) J(f,g) = 1; count unknowns and equations of the
joint system at the first few bands on each side and identify WHERE the two
sides first share coefficients (the common jet: the coefficients of f, g that
appear in both expansions — these are the global constraints); (2) COMPUTE as
far as possible with the campaign's preprocessing (Q*-pivots, weighted
grading, torus slice; charged K = 16 drivers): impose both sides' first bands
and the shared coefficients; report the dimension of the joint family band by
band and whether/when it becomes INCONSISTENT (that would be the (99,66)
kill for that branch — give the certificate) or stays consistent to the
budget (report the deepest band, the dimension, and the next system); do
both branches (δ = 2 [2,1], δ = 5/2); (3) calibration: run the same joint
design on Moh's (16,12)-parent (64,48) [s = 3, u_s = 1, the minor side trivial]
and confirm it reproduces the Appendix II kill; and on a genuine
automorphism of degrees with two points at infinity in Moh's gauge (construct
one: a composition of two triangular automorphisms; it must SURVIVE — the
negative control); (4) verdict + typed scope + bounded quantity + cheapest
test; FALLACY-v2 applies (no claim of a pair without the direct Jacobian
check; a lift that stops at budget is COUNTING-BOUND). ≤ 180 min; 4 cores;
no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-middle-spine, g9966-source-review, bigrows-preprocess, strata-rerun-
corrected, r3-preprocess, xu-sametree). Drivers to box/g9966-20260903/.
Report: xmodel/g9966-global-design-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 16-32KB; 180 minutes.
charged_input=xmodel/moh9966-B-lift-sol56-20260903.md
charged_input=xmodel/xu-delta52-lift-gpt55-20260903.md
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/moh9966-branchB-sol56-20260903.md
charged_input=xmodel/minor-dichotomy-sol56-20260903.md
charged_input=xmodel/sibling-coefficients-sol56-20260903.md
charged_input=xmodel/jet-edge-1612-sol56-20260903.md
charged_input=xmodel/k16-uniform-structure-sol56-20260903.md
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/moh9966lift-20260903/h_curved_center.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-global-design-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
1d4ff2c76301705fbfa0f324862fe8f8065d57840fbb3094bce596f54c6651c6  {{LANE_INPUTS}}/moh9966-B-lift-sol56-20260903.md
1e3aafcae25d811f033a8deeff8daaee022735f9f09a9d4bd20499a56a44c899  {{LANE_INPUTS}}/xu-delta52-lift-gpt55-20260903.md
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
8338a702448a61ef10af214e5d156e0c14ad117ef231ae34aee462fb36fa649f  {{LANE_INPUTS}}/moh9966-branchB-sol56-20260903.md
184a689f3cd63405d922b8118632c7e17f96f471a0bc71f9a50cd161b8a87ad1  {{LANE_INPUTS}}/minor-dichotomy-sol56-20260903.md
a00d258b0b6469a64e433747692c01bb6e113de33b95a430e4917485e782b36a  {{LANE_INPUTS}}/sibling-coefficients-sol56-20260903.md
8d45fccf43d6b1928b4ae00a08ffaa7efc88f5b92a21392dca85ba17a5393704  {{LANE_INPUTS}}/jet-edge-1612-sol56-20260903.md
90d4068583ec1801641f8e346f0fdd19d21c5d68901d5ee4f7aec8ddb7e3f1cb  {{LANE_INPUTS}}/k16-uniform-structure-sol56-20260903.md
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
a699075f825bd8d13c44d35ce68f13e708e029c156dddd9d6e9a2179e8166291  {{LANE_INPUTS}}/h_curved_center.py
```
