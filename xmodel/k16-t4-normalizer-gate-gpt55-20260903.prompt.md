# Hostile gate: (a) theorem (T) at t = 4 on the K = 16 ray — (52,36; 49; 3; J = cγ) exact eight-generator basis [1] over Q(√15); (b) the ALL-t NORMALIZER LEMMA (closed H_t(y), c_t(y), uniform grading, x = 1 slice, c a unit in A_t = Q[y]/(H_t) for every t)

Charged (k16-uniform-structure-sol56-20260903.md §1–§3; AUDIT delta 17(xx)
PROVED-HERE/UNREVIEWED). Task: (1) mechanical replay of t = 4: regenerate the
gauged chart (9·4 + 9 = 45 unknowns incl. c, 14·4 + 9 = 65 equations) from the
charged generator, run the charged normalisation to the eight-generator
system over Q(√15) and confirm [1] (Singular; report the program hashes and
times); independently, confirm the three modular [1] results at GF(32003),
GF(65521), GF(1000003) on the full chart; (2) audit the t = 4 covering chain
exactly as in the t = 3 gate (charged k16-t3-gate §4): Q*-pivots only, the
grading, x ≠ 0 forced by (C), the torus slice, the quadratic factor and both
conjugates (here H_4 = 12·81y² − 12·9·5y + 5·14 = 972y² − 540y + 70 → check the
content and the field Q(√15): disc 48·81·5 = 19440 = 1296·15 ✓), unit pivots
(norms/resultants recorded), and the final [1] — any pivot-zero branch or
missing conjugate?; (3) audit the ALL-t normalizer lemma as a formula proof:
verify with sympy over Q(t) that E1–E4 give g₁ = rx, g₂ = ry + C(r,2)x², g₃ =
2C(r,2)xy + C(r,3)x³ with r = e/q = (3t+1)/(2t+1), that E4 and E0 give (H) and
(C) as displayed, that the weighted grading is positive and that (C) + c ≠ 0
forces x ≠ 0, that the normalised H_t, c_t are as displayed with disc_y H_t =
48(2t+1)²(t+1), and that the image of c is a unit in A_t = Q[y]/(H_t) for every
integer t ≥ 1 (compute Res_y(H_t, numerator of c_t) symbolically in t and show
it has no positive integer root; note H_t is not primitive at every t —
handle the content); check the 3t + 4 Q-constant pivots claim at t = 1..6 by
running the charged extractor; (4) verdict per item CONFIRMED / GAP /
REFUTED with scope (the lemma is uniform in t; the t = 4 kill is fixed-t);
type every claim; FALLACY-v2 applies. ≤ 90 min; 2 cores; no ledger edits; no
jc2-lean; no ideation-* files; no in-progress lane reports (k16-middle-spine,
moh9966-branchB, chart-fix-d1zero, bigrows-preprocess). Drivers to
box/k16t4-gate-20260903/.
Report: xmodel/k16-t4-normalizer-gate-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-16KB; 90 minutes.
charged_input=xmodel/k16-uniform-structure-sol56-20260903.md
charged_input=xmodel/k16-t3-gate-gpt55-20260903.md
charged_input=xmodel/k16-t3-uniform-sol56-20260903.md
charged_input=box/k16t3-20260903/t4/t4_order_system.py
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=FALLACY-v2.md
charged_input=box/k16uniform-20260903/t4_affine_reduce.py
charged_input=box/k16uniform-20260903/uniform_binomial_identities.py
charged_input=box/k16uniform-20260903/t4_emit_residual.py
charged_input=box/k16uniform-20260903/t2_t1_normalized_audit.py
charged_input=box/k16uniform-20260903/t3_normalization_replay.py
charged_input=box/k16uniform-20260903/t4_normalization_probe.py
charged_input=box/k16uniform-20260903/uniform_extract_normalizers.py
charged_input=box/k16uniform-20260903/t4_emit_exact_certificate.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-t4-normalizer-gate-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
90d4068583ec1801641f8e346f0fdd19d21c5d68901d5ee4f7aec8ddb7e3f1cb  {{LANE_INPUTS}}/k16-uniform-structure-sol56-20260903.md
5593aa5443dd755cadedca4b0d284a3dec4048f7cd5822da576587552f36aba6  {{LANE_INPUTS}}/k16-t3-gate-gpt55-20260903.md
f16dc4bcb7183bf2e699981dce639d3e824b7b63457189de1f2d98172501fa20  {{LANE_INPUTS}}/k16-t3-uniform-sol56-20260903.md
db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee  {{LANE_INPUTS}}/t4_order_system.py
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
66463156f99204648456ddf0105273517b64252ce6e792f92c051d13b2a3591f  {{LANE_INPUTS}}/t4_affine_reduce.py
39469e4e4b4cfab455aea9a919d595a3e05e9d666913c5285862198b927e4707  {{LANE_INPUTS}}/uniform_binomial_identities.py
b2a2596d9ab7edc284401689ca9f88b638564e631a3769b9da216476bb10bd25  {{LANE_INPUTS}}/t4_emit_residual.py
0b51819c0c04d07ef652fbe0888bfea86d7ee15eee7a4e0b716dccddc8c669d7  {{LANE_INPUTS}}/t2_t1_normalized_audit.py
37faa716222a98644a1eed997566e31fb1fb4079181e6f2487af1d339c1360f2  {{LANE_INPUTS}}/t3_normalization_replay.py
085aac73eafda284514bb2f10478f242d3535cca16ef7249043ed85b30a27faf  {{LANE_INPUTS}}/t4_normalization_probe.py
81d084feac20192c2fb972c5d03faa4362f72429cc5976cc27968fbafb74e625  {{LANE_INPUTS}}/uniform_extract_normalizers.py
42bfd85b39665717c6a885ba5c4b538f59020021b3ef9ad900bd06cb67db7312  {{LANE_INPUTS}}/t4_emit_exact_certificate.py
```
