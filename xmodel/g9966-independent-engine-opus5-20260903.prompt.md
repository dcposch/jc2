# Independent re-implementation gate (highest-stakes claim of the campaign): rebuild the (99,66) joint-chart band engine FROM THE DESIGN DOCUMENTS ONLY (not from the charged engine code), and re-run both branches — δ = 2 [2,1] to its stage-4 death (residue 6264) and δ = 5/2 [1,1,1] to its stage-8 death (residue 64) — so that "no Keller pair with the (99,66) skeleton" rests on two independent implementations

OPERATIONAL: skeleton first; every job in the foreground with `timeout 3000`;
never end the turn with a job running; ≤ 4 cores. Context (banked, AUDIT
deltas 17(ttt), (aaaa), (dddd), (kkkk), (pppp), (qqqq)): the joint chart imposes,
on F (degree 99 = Moh's g) and G (degree 66 = Moh's f) in Moh's gauge with the
minor line at y = 0: (i) the major tower at the first point at infinity as the
approximate-root chart h₃ = P + H, h₂ = h₃³ + C₂h₃ + C₃, F = h₂³ + A₂h₂ + A₃, G = h₂²
+ B₁h₂ + B₂ with P = y³(y − x)⁸ (so in F = P⁹, in G = P⁶) and Theorem-1.2 order
LOWER bounds on the h₃-D₂ / h₂-D₂ faces and the h₂-D₁ band (516 → 120 rows);
(ii) the outer Theorem-1.2 D₂ support preblock (5,598 unit vanishings 3r + 4q <
3(D + bound)) and the D₁ rows (225 raw slots, exact rank 176) on the A₂, A₃, B₁, B₂
blocks; (iii) the minor incidence block for the branch at the second point
(δ = 2: H = π²(π + 3), R = π²⁵(π + 3)¹⁴(π − 2), packets 18 + 9, a = 1 by scaling;
δ = 5/2: p = π(π² − c), q₁ = −2∫p³, packets 9 + 9 + 9); (iv) direct minor F, G
coefficient rows and pole rows (F,G) local powers with branch exponents
(−77/−50 for δ = 2; −181/−118 for δ = 5/2) descending by one per stage; (v) the
direct Jacobian rows J_{y,z}(F̄, Ḡ) = constant, coefficient by coefficient,
degree 162 downward ([x¹³⁵y²⁷] first, then all of J162, J161, …); the engine
eliminates by Q*-pivots only (constant coefficients), never pivots on ρ or c,
and sends any residue to Singular with Rabinowitsch; dimensions δ = 2: 6,689 →
1,065 → 1,018 → 976 → 942 → DEAD (stage 4: 118 integer constants, e.g.
stage4_J_d159_k35 = 6264); δ = 5/2: 6,687 → 1,063 → 1,016 → 974 → 940 → 913 → 894 →
880 → 869 → DEAD (stage 8: stage8_G_local16_coord0 = 64). Task: (1) from the
charged DESIGN reports (global-design §2–§3, outer-bridge §2–§4, the band
report's §3–§4 conventions) — NOT from band_engine.py, which you must not
read (it is deliberately not charged) — write your own engine: construct the
ambient coefficient ring, the tower substitution, the order-bound rows, the
outer bands, the minor block, the pole and Jacobian rows, and an exact Q*-
pivot eliminator; document every convention you had to choose (label
reversal, the minor line at y = 0, branch exponents, band order) and where the
design documents were ambiguous; (2) run δ = 2 through stage 4 and δ = 5/2
through stage 8, logging per stage the rank/dimension; compare with the
charged dimension paths — agreement at every stage is the strongest possible
confirmation; disagreement must be diagnosed (a convention difference vs a
genuine error in one engine); (3) confirm both deaths independently (your own
constant residues; Singular replay); (4) controls in YOUR engine: the (64,48) →
(16,12) kill; a tame two-point automorphism of degrees ≥ 6 must survive all
bands you can run (construct one explicitly and state the result); (5) verdict:
CONFIRMED-INDEPENDENTLY / DISAGREEMENT (which stage, which rows) / GAP. Type
every claim; FALLACY-v2 applies. ≤ 180 min; no ledger edits; no jc2-lean; no
ideation-* files; no in-progress lane reports (g9966-delta52-kill-gate,
g9966-delta52-bridge, g108-minor-classification, k16-*, order-chart-general).
Drivers to box/g9966indep-20260903/.
Report: xmodel/g9966-independent-engine-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 14-28KB; 180 minutes.
charged_input=xmodel/g9966-global-design-sol56-20260903.md
charged_input=xmodel/g9966-design-gate-grok46-20260903.md
charged_input=xmodel/g9966-outer-bridge-grok46-20260903.md
charged_input=xmodel/g9966-global-band-sol56-20260903.md
charged_input=xmodel/g9966-delta52-stage8-sol56-20260903.md
charged_input=xmodel/g9966-branchB-kill-gate-gpt55-20260903.md
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=xmodel/xu-delta52-lift-gpt55-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-independent-engine-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
a81ff0263cf379a297b8d1812ebfa26eb95f7e58d91ef4edc62a3a68edf2d782  {{LANE_INPUTS}}/g9966-global-design-sol56-20260903.md
0cbeaf0735b92f18e3a7c5050775b99c3739b658584ce0d02965a24db2c1273b  {{LANE_INPUTS}}/g9966-design-gate-grok46-20260903.md
7facb109db6eb21b73970c2b6a0d4339bc51c7b73f3ce16782950550508e2674  {{LANE_INPUTS}}/g9966-outer-bridge-grok46-20260903.md
0c8dc291e306f15806e6c14099ab69feda9d1532abcbc22e79e55b02df427701  {{LANE_INPUTS}}/g9966-global-band-sol56-20260903.md
679671e7be4aef40128b133b26ab75c083f95a7283d9ab97aebcccea5bc21b01  {{LANE_INPUTS}}/g9966-delta52-stage8-sol56-20260903.md
84b2a04cc41231eeaa3711b03b9a3d0e23630581bdf63a230799fdeafeb4d468  {{LANE_INPUTS}}/g9966-branchB-kill-gate-gpt55-20260903.md
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
1e3aafcae25d811f033a8deeff8daaee022735f9f09a9d4bd20499a56a44c899  {{LANE_INPUTS}}/xu-delta52-lift-gpt55-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
