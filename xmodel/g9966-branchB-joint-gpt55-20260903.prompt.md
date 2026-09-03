# Computation lane: (99,66) BRANCH B (δ = 2, [2,1], multiplicity vector (25,14), face = a single point mod gauge) — run the same Prop 6.2 high-z joint system that was built for δ = 5/2 (charged driver), now with NO free face parameter, as deep as the budget allows; then extend BOTH branches' joint systems downward by two more z bands

Context (banked, AUDIT deltas 17(iii), (nnn), (ppp)): the δ = 5/2 high-z joint
system (Ḡ unknowns on the top z-adic bands, Prop 6.2 bidegree boxes, μ₂-
equivariance, Jacobian constant; charged driver box/g9966d52-20260903/
g9966_delta52_joint_driver.py) is NON-UNIT through depth 6 (dimension 16);
the branch-B fallback was not run because its trigger ("if δ = 5/2 dies") did
not fire. Branch B's face is rigid: p = π²(π + 3a), q = π²⁵(π + 3a)¹⁴(π − 2a)
(a gauged), packets 18 + 9 at the radius-two place (Moh p.209; Grok gate
17(nnn): not a slice). Task: (1) adapt the charged driver to branch B: the
principal-minor leading data at δ = 2 (H = z²(z + 3a) cubic with a double
root; T₃ leader R = z²⁵(z + 3a)¹⁴(z − 2a); the (25,14) multiplicity vector),
the Prop 6.2 boxes, the Jacobian constant; no free face parameter after the
gauge; (2) run depth 4, 5, 6 (and deeper if fast) over GF(32003), GF(32009),
GF(32027) and Q with the wrapper, non-empty and unsaturated-non-unit
controls; report per depth: equations, unknowns, basis size, verdict, family
dimension; (3) for BOTH branches, extend the joint system by the next two
lower z bands (the depth-7 and depth-8 bands) — this is where the lower
coefficients of Ḡ and F̄ interact with the major side's 4/9 centre: state what
new unknowns enter (the effective T₂ ∈ K[f,g] relation's coefficients? the
centre a₁, a₂ of Ω?) and impose what the charged sources license; report
whether the dimension drops, stays, or the system becomes inconsistent;
(4) controls as in the charged lane (Moh (64,48) kill; the automorphism
F = x + y⁶, G = y + (x + y⁶)⁷ survives); (5) verdict per branch (SATURATED-
EMPTY with certificate / COUNTING-BOUND with dimension and the next system);
FALLACY-v2 applies (no SURVIVES without a full pair and a direct Jacobian
check). ≤ 150 min; 4 cores; no ledger edits; no jc2-lean; no ideation-* files;
no in-progress lane reports (g9966-global-design, k16-*, emitter-native,
n5-denominator, bridge-chart-gate). Drivers to box/g9966B-20260903/.
Report: xmodel/g9966-branchB-joint-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 150 minutes.
charged_input=xmodel/g9966-delta52-joint-gpt55-20260903.md
charged_input=box/g9966d52-20260903/g9966_delta52_joint_driver.py
charged_input=box/g9966d52-20260903/g9966_delta52_joint_results.json
charged_input=xmodel/g9966-review-gate-grok46-20260903.md
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=xmodel/moh9966-B-lift-sol56-20260903.md
charged_input=xmodel/moh9966-branchB-sol56-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g9966-branchB-joint-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
789b31978fe9c66e5540e48aa0e748af991daa8844946970d6065dbba38e6c80  {{LANE_INPUTS}}/g9966-delta52-joint-gpt55-20260903.md
5c01e6971993935fcf9f96924a411dfc19e9093449ddaeb8bdb059744ee0d3a8  {{LANE_INPUTS}}/g9966_delta52_joint_driver.py
cfd4515d9afe771cd8c30ae9095c888a58d2f46226ad9ed8c28ca63c59814483  {{LANE_INPUTS}}/g9966_delta52_joint_results.json
dc2355a81dd472993c9af0fb0f03eb5b6f3c087c3a2ed00120615b76bcf91be8  {{LANE_INPUTS}}/g9966-review-gate-grok46-20260903.md
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
1d4ff2c76301705fbfa0f324862fe8f8065d57840fbb3094bce596f54c6651c6  {{LANE_INPUTS}}/moh9966-B-lift-sol56-20260903.md
8338a702448a61ef10af214e5d156e0c14ad117ef231ae34aee462fb36fa649f  {{LANE_INPUTS}}/moh9966-branchB-sol56-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
