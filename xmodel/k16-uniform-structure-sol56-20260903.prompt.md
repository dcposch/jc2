# Proof-attack lane (the decisive structural question): theorem (T) on the K = 16 ray UNIFORMLY IN t — extract the structure of the normalised systems at t = 2, 3, 4 (weighted-homogeneous grading, the weighted scaling x ↦ 1, the univariate polynomial H_t(y), the residual system in (b₃, b₄, a₂₀)) and prove the pattern for all t, or isolate exactly which t-dependent object blocks it

Context (banked): (T) holds on the descended ray (12t+4, 8t+4; 12t+1; 3; J = cγ)
at t = 1 (Moh), t = 2 (PROMOTED, delta 17(oo)), t = 3 (PROVED-HERE, delta 17(ss),
gate running), t = 4 modular. Sol's t = 3 lane (charged) found: the gauged
chart's 37 residual rows are homogeneous for a positive grading wt(x) = 13,
wt(y) = 26, wt(c) = 65; on c ≠ 0 the first identity forces x ≠ 0, the weighted
action makes x = 1 and puts y in the quadratic field K = Q[y]/(147y² − 84y + 11)
with c = 10y(2 − 21y)/343 (both conjugates covered; y, 2 − 21y units in K); after
17 affine-linear eliminations six generators remain in (b₃, b₄, a₂₀) from bands
h = 0..5, whose exact reduced basis is [1]. Its §4–5 showed a constant-pivot
spine uniform in t through bands h^{4t+1} … h^{2t}, and that every FIXED
collection of low or extreme-high bands is consistent for large t — the
inconsistency lives in the t-scaling middle. Task: (1) recompute the
normalisation at t = 2 and t = 3 from the charged drivers and do it at t = 4
(modular where exact is slow; the t = 4 chart has 45 unknowns / 65 generators —
the triangular preprocessing should reduce it far below that): for each t
record the grading weights, the univariate H_t(y) (degree, discriminant), the
value of c, the number of affine eliminations, and the residual generator
set (which bands, which unknowns, degrees); (2) find the pattern: are the
weights linear in t? is H_t of fixed degree 2 with coefficients polynomial in
t? is the residual always six generators in three unknowns from bands
h = 0..5 (i.e. a FIXED-size final system whose coefficients are polynomials in
t and in a root of H_t)? If yes, that is the uniform certificate route: write
the residual system R_t over Q(t)[y]/(H_t(y)) symbolically (sympy, or Singular
with t as a parameter in the ground field Q(t)), compute its reduced basis
over Q(t) — [1] generically means empty for all but finitely many t (the
denominators' roots), and then handle those finitely many t exactly; state
the theorem and proof; if the residual size grows with t, characterise the
growth and identify the smallest t-uniform statement you CAN prove (e.g.
that the residual is a triangular system whose last equation is a nonzero
constant, by induction on the band index); (3) controls: the t = 1 row
(16,12) must fit the same pattern (or explain why not); the actual pair
(π, π − γ²/2) must fail the tuple; wrapper controls in every ring; (4) verdict:
(T) on the ray PROVED for all t ≥ 1 (with the full proof written out, typed
PROVED-HERE, and the finite exceptional set handled), or PARTIAL (exact
statement of what is uniform and what is not, and the bounded next step);
FALLACY-v2 applies (a generic-t [1] over Q(t) is a theorem only for t
outside the denominators' zero set; specialisation must be justified — the
ideal membership certificate over Q(t) specialises wherever its coefficients
are defined). ≤ 150 min; up to 4 cores; no ledger edits; no jc2-lean; no
ideation-* files; no in-progress lane reports (k16-t3-gate, strata-gate,
moh9966-branches, twopoint-kills-gate-fable5). Drivers to
box/k16uniform-20260903/.
Report: xmodel/k16-uniform-structure-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 14-28KB; 150 minutes.
charged_input=xmodel/k16-t3-uniform-sol56-20260903.md
charged_input=xmodel/k16-ray-T-newton-sol56-v3-20260903.md
charged_input=xmodel/k16-t2-gate-gpt55-20260903.md
charged_input=box/k16t2-gate-20260903/t2_independent_order_system.py
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/k16t3-20260903/t3/t_order_system.py
charged_input=box/k16t3-20260903/t3/RUN_COMMANDS.txt
charged_input=box/k16t3-20260903/t4/t4_order_system.py
charged_input=box/k16t3-20260903/t4/T4_HANDOFF.md
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=box/k16t3-20260903/preprocessed/t3_normalized_slice.py
charged_input=box/k16T-drivers-20260903/t2_order_system.py
charged_input=box/k16T-drivers-20260903/k16_symbolic.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-uniform-structure-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
f16dc4bcb7183bf2e699981dce639d3e824b7b63457189de1f2d98172501fa20  {{LANE_INPUTS}}/k16-t3-uniform-sol56-20260903.md
27f395615d37906a379f6c727c6499be6d78c711e7d7ca728ac44050f1be23e0  {{LANE_INPUTS}}/k16-ray-T-newton-sol56-v3-20260903.md
692fd869d8a11b3a984d1fe8c4ccb4b42de7326567c130b8babae1571ca6e863  {{LANE_INPUTS}}/k16-t2-gate-gpt55-20260903.md
7ee7e29eca86dadecf4cffdc996539fc875851ce5803ad7ddaf68b888624f823  {{LANE_INPUTS}}/t2_independent_order_system.py
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
24f669899596fe0e9023373a9b7ad64591d41c592114cce623ddce6e5d4a260c  {{LANE_INPUTS}}/RUN_COMMANDS.txt
db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee  {{LANE_INPUTS}}/t4_order_system.py
d95d0cff5bc06a6a9e4459da4886b61dd6a2871dc28e1710961e92810e779112  {{LANE_INPUTS}}/T4_HANDOFF.md
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7  {{LANE_INPUTS}}/t3_normalized_slice.py
55067a8c74d6c360c72aaa40243dde7e8e1a804158b3c78abf523d77a25cb5e2  {{LANE_INPUTS}}/t2_order_system.py
1d826456df0a06ec2dc78e02f8d931470a151a806a5f8e889653b120eaa0c76d  {{LANE_INPUTS}}/k16_symbolic.py
```
