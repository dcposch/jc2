# Independent proof attack (different model, different strategy): OPEN[T-UNIFORM-MIDDLE] on the K = 16 ray — theorem (T) for all t via the Laurent/tuple-level bridge and an induction in t on the normalised systems, rather than band-by-band pivot recurrences

Context (banked, AUDIT deltas 17(mm)–(ww), (xx), (ddd)): on the descended K = 16
ray (12t+4, 8t+4; 12t+1; 3; J = cγ) theorem (T) is PROMOTED at t = 1..4, each by an
exact certificate on the gauged Theorem-1.2 order chart (9t + 9 unknowns, 14t + 9
equations; a necessary SUPERSET of the tuple locus because it omits the
tuple-level Laurent bridge equations — the vanishings before p₁₇ and p₁₇ ≠ 0,
where p₁₇ is the order-45 coefficient of ξ²⁸P(γ, Y(ξ)) in the reciprocal
dictionary ξ = h^{−1/4}, see k16-ray-T-newton-sol56-v3 §7); the all-t
NORMALIZER LEMMA is PROMOTED: uniform positive grading, 3t + 4 Q-constant pivots
from band 4t+1 down to 2t, closed base relation H_t(y) = 12(2t+1)²y² −
12(2t+1)(t+1)y + (t+1)(3t+2) with c_t(y) a unit in A_t = Q[y]/(H_t), the x = 1
torus slice; the exact reductions at t = 2, 3, 4 show a terminal system of 2t
rows in t variables (bands 0..2t−1) that is [1] each time, but no closed
recurrence for the middle pivots u_{t,j}(y) is proved (a parallel Sol lane is
attacking exactly that by induction on the band index — do NOT duplicate it;
its report must not be read). Your task is a DIFFERENT route: (1) source-read
Moh pp.149–152 (Theorem 1.2, Lemma 2.1) and pp.207–209 as page images (name
pages) and the charged Sol/GPT-5.5 reports; (2) attack A — the Laurent bridge:
the omitted tuple-level equations are EXTRA constraints; if adding the
vanishings before p₁₇ (and its analogue for general t — derive the index as
a function of t) to the low bands gives a fixed-size subsystem inconsistent
uniformly in t, that is a proof of (T) that the superset chart cannot give
(the charged lanes showed no fixed collection of chart bands is uniformly
inconsistent — but the bridge equations are not chart bands); derive the
bridge equations for general t explicitly (sympy, symbolic t), and test the
low-band + bridge subsystem for t = 2..6 and then symbolically; (3) attack B —
induction in t: compare the normalised systems at t and t + 1 (charged
uniform drivers) and look for a map (specialisation, or a linear change of
the auxiliary variables) sending the t-system into the (t+1)-system so that
a unit certificate propagates; or a "telescoping" structure: the terminal
2t × t system at t+1 contains the t-system's terminal after a substitution;
(4) attack C — a structural reason: the ray's descended pairs have (n*, m*) =
(3t+1, 2t+1), coprime, and M₂' = n' − 3; Lemma 2.1 gives deg_x g_{m'−1} = 2;
is there an Abhyankar–Moh / semigroup argument (the approximate roots of P
form a δ-sequence; the two-point condition δ₂' = −1 with V₂' = 3, u' = 1 means
the top disc has exactly one non-centre root) that bounds t directly — e.g.
via Xu's intersection-number identities (charged Xu screen reports) applied
to the descended pair, or via the genus of the generic fibre of the descended
pair (a monomial-Jacobian pair has generic fibre of genus computable from
its Newton data; for large t does the genus/Hurwitz identity fail?); (5)
verdict: (T) on the ray for all t (full proof), or the sharpest partial
statement with its bounded quantity and cheapest test; type every claim;
FALLACY-v2 applies (a generic-t identity specialises only where its
denominators are nonzero). ≤ 150 min; 2 cores; no ledger edits; no jc2-lean;
no ideation-* files; no in-progress lane reports (k16-middle-spine-sol56,
g9966-*, bigrows-preprocess, r3-preprocess, xu-sametree). Drivers to
box/k16spine-opus-20260903/.
Report: xmodel/k16-middle-spine-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 14-28KB; 150 minutes.
charged_input=xmodel/k16-uniform-structure-sol56-20260903.md
charged_input=xmodel/k16-t4-normalizer-gate-gpt55-20260903.md
charged_input=xmodel/k16-t3-uniform-sol56-20260903.md
charged_input=xmodel/k16-ray-T-newton-sol56-v3-20260903.md
charged_input=xmodel/k16-t2-gate-gpt55-20260903.md
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=xmodel/xu-screen-gate-fable5-20260903.md
charged_input=box/k16t3-20260903/t3/t_order_system.py
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
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
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-middle-spine-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
90d4068583ec1801641f8e346f0fdd19d21c5d68901d5ee4f7aec8ddb7e3f1cb  {{LANE_INPUTS}}/k16-uniform-structure-sol56-20260903.md
e868a7f2df3814caf1847411918c17cbf8e71688779819fd4764d70e9d86ae83  {{LANE_INPUTS}}/k16-t4-normalizer-gate-gpt55-20260903.md
f16dc4bcb7183bf2e699981dce639d3e824b7b63457189de1f2d98172501fa20  {{LANE_INPUTS}}/k16-t3-uniform-sol56-20260903.md
27f395615d37906a379f6c727c6499be6d78c711e7d7ca728ac44050f1be23e0  {{LANE_INPUTS}}/k16-ray-T-newton-sol56-v3-20260903.md
692fd869d8a11b3a984d1fe8c4ccb4b42de7326567c130b8babae1571ca6e863  {{LANE_INPUTS}}/k16-t2-gate-gpt55-20260903.md
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
73810445b86518097594ce95d478a4f96000c74c7ad0455e376eccdc5f23218b  {{LANE_INPUTS}}/xu-screen-gate-fable5-20260903.md
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
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
