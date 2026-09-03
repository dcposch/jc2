# Proof-attack lane (the last blocker on the ray): OPEN[T-UNIFORM-MIDDLE] — prove the SECOND AFFINE SPINE of the K = 16 normalised systems by induction on the band index in A_t = Q[y]/(H_t), prove or refute the terminal family (2t rows in t variables, bands 0..2t−1, degrees 4t+1..2t+2), and find the terminal recurrence that ends in a nonzero constant — i.e. theorem (T) on the ray for every t

Context (banked, AUDIT delta 17(xx)): the all-t normalizer lemma is proved
(charged k16-uniform-structure §1–2): uniform chart with 9t + 9 unknowns and
14t + 9 equations; 3t + 4 Q-constant pivots from band 4t+1 down to 2t; the
closed relations (H) and (C); the x = 1 slice; H_t(y) = 12(2t+1)²y² −
12(2t+1)(t+1)y + (t+1)(3t+2), c_t(y) = t(3t+1)y((t+1) − 6(2t+1)y)/(6(2t+1)³), c a
unit in A_t for all t. After H/c the exact reductions at t = 2, 3, 4 show:
9t + 2 rows in 6t + 2 auxiliaries; 5t + 2 affine pivots (elements u_{t,j}(y)
of A_t); 2t zero/duplicate rows; a terminal system of 2t rows in t variables
from bands 0..2t−1 with degrees 4t+1 … 2t+2; and the terminal ideal is [1] at
t = 1, 2, 3, 4. What is missing (§4.2, §5): a closed formula or recurrence for
the pivots u_{t,j}, the proof that each is a unit (Res_y(H_t, u_{t,j}) ≠ 0 for
every band and every t ≥ 1), the duplicate/zero recurrence, and the
identification of the terminal ideal with a proof that it contains a nonzero
constant of A_t for every t. The coefficient-space boundaries move at band t
and at offset t, which is where consecutive charts first differ. Task: (1)
extract, from the charged drivers, the exact post-H/c systems at t = 2, 3, 4,
5, 6 (compute t = 5, 6 fresh; modular is fine for discovery, exact for the
recorded pivots) in a CANONICAL pivot order (fix the order by band index and
by a deterministic variable order so that names are comparable across t);
tabulate the pivots u_{t,j}(y) ∈ A_t and the terminal rows as explicit
polynomials in y and the t auxiliary variables with coefficients in Z[t]
where possible; (2) find the recurrence: express u_{t,j} as a closed form in
(t, j, y) (try: polynomial in t and y of bounded degree; or a linear
recurrence in j with coefficients in Z[t][y]) — verify it against t = 2..6 and
PROVE it from the banded h-adic identity (charged k16-t3-uniform §1.3 and
§4.2 high-side recurrence) by induction on the band index, the same way the
first spine (bands 4t+1 → 2t) was proved; record Res_y(H_t, u_{t,j}) as a
polynomial in t and show it is nonzero for all positive integers t (or name
the exceptional t and handle them exactly); (3) the terminal family: give
its closed form for general t; then prove it is inconsistent for all t —
candidates: (a) a triangular structure in the t variables ending in an
equation of the form (nonzero element of A_t) = 0; (b) a resultant/elimination
in one variable whose value is a nonzero polynomial in t times a unit; (c)
an induction on t relating the terminal systems at t and t+1; if you cannot
prove it, prove the largest sub-statement you can (e.g. the terminal system
is triangular with unit leading coefficients for all t, reducing (T) to a
single explicit univariate identity in t) and state the exact residual
statement with its cheapest test; (4) controls: the specialisations t = 1..4
of every uniform formula must reproduce the banked exact objects; the point
Q = h^q + B, P = h^e + 2π − γ, c = −1 must satisfy all low levels through 2t−1
and fail at bands 2t and 3t+1 (as charged); FALLACY-v2: a generic-t identity
specialises only where its denominators D(t) and the leading coefficient of
H_t are nonzero — record D(t) and handle its integer roots; the split set
t = 3s² − 1 (H_t reducible) is handled in the product algebra, never by
inverting a zero divisor; (5) verdict: (T) on the ray PROVED for all t ≥ 1
(full proof, typed PROVED-HERE), or PARTIAL with the precise remaining
statement. ≤ 180 min; 4 cores; no ledger edits; no jc2-lean; no ideation-*
files; no in-progress lane reports (k16-t4-normalizer-gate, moh9966-branchB,
chart-fix-d1zero, bigrows-preprocess). Drivers to box/k16spine-20260903/.
Report: xmodel/k16-middle-spine-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 16-32KB; 180 minutes.
charged_input=xmodel/k16-uniform-structure-sol56-20260903.md
charged_input=xmodel/k16-t3-uniform-sol56-20260903.md
charged_input=xmodel/k16-t3-gate-gpt55-20260903.md
charged_input=box/k16t3-20260903/t3/t_order_system.py
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
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-middle-spine-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
90d4068583ec1801641f8e346f0fdd19d21c5d68901d5ee4f7aec8ddb7e3f1cb  {{LANE_INPUTS}}/k16-uniform-structure-sol56-20260903.md
f16dc4bcb7183bf2e699981dce639d3e824b7b63457189de1f2d98172501fa20  {{LANE_INPUTS}}/k16-t3-uniform-sol56-20260903.md
5593aa5443dd755cadedca4b0d284a3dec4048f7cd5822da576587552f36aba6  {{LANE_INPUTS}}/k16-t3-gate-gpt55-20260903.md
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
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
