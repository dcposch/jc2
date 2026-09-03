# Computation lane: the δ = 5/2 principal-minor split of (99,66) — Xu's open case — lift it from the explicit leading data (p(π) = π(π² − c), q = p¹⁰q₁, q₁ = −2∫p³ dπ) through the full coefficient system, Appendix-II style, and decide it

Context (banked, AUDIT delta 17(zz); Xu arXiv:1604.07683v4 §8, pp.12–13, charged
PDF): for (99,66) (M₂ = 77, M₃ = 97, V = (8,8), δ₂ = 1/3, δ₁ = 4/9, −μ₂ = 55, −μ₃ =
145; principal minor roots of multiplicity 3·(something) with u₃ = 3) the only
principal-minor split orders not excluded are δ = 2 (Moh's two-root case, being
lifted in another lane) and δ = 5/2, where Xu derives: p(π) = π(π² − c) (deg 3),
T₃(σ) = q(π)t^{13(−8+3δ)−1+δ} with q = p¹⁰q₁, deg q₁ = 10, and the reduced
Jacobian equation ∂(q₁(π), p(π)t^{−1/2})/∂(t,π) = −p(π)⁴t^{−3/2}, solved by
q₁ = −2∫p³ dπ for ANY p — hence "open". The face data are therefore fully
explicit at δ = 5/2 (f(σ) = p⁶t^{6(−8+3δ)} = p⁶t^{−3}, g(σ) = p⁹t^{−9/2}, T₂(σ) =
p⁵t^{−5/2}, (T₃)_f(σ) = p²²t^{−11}, T₃(σ) = q·t^{−13−1+5/2} = q t^{−23/2}). Task:
(1) SOURCE-READ Xu §7–8 (page images of pp.10–13; name pages) and Moh pp.196–
199, 207–209: state exactly Xu's derivation of the δ = 5/2 data and of q₁ =
−2∫p³ (verify it symbolically: with p = π(π² − c), compute q₁ and check the
reduced equation), and what "open" means (which further equations he did not
impose); (2) set up the NEXT level: the σ-expansion σ = Σ_{j<5/2} a_j t^j + πt^{5/2}
with the principal-minor centre (the a_j through order 2 are the centre of the
minor disc — determined by the tower? state what is determined: the leading
form y − a₁x with the multiplicity data, and the unknown lower centre
coefficients), and write f, g, T₂, T₃ = the effective quasi-approximate roots
in Xu's sense (T_i ∈ K[f,g] with deg T_i = −μ_i) as polynomials in (x, y) whose
π-root expansions at σ have the prescribed leading terms; the Jacobian
condition J(f,g) = 1 in the ORIGINAL coordinates (no Ω here) then gives, order
by order in t beyond the reduced equation, a system in the coefficients of
p, q₁ and the lower terms — impose the next two orders (the terms Xu did not
use) and saturate by c ≠ 0 (p must have three distinct roots: c ≠ 0) and by the
Jacobian constant; report whether the next orders are consistent (family
dimension) or inconsistent (then the δ = 5/2 split is EXCLUDED — give the
certificate, and (99,66) reduces to Moh's δ = 2 branch B); (3) if the orders
you impose stay consistent, continue as far as the budget allows using the
weighted-grading / triangular preprocessing of the charged K = 16 drivers
(Q*-pivots, torus slice), reporting the deepest consistent order and the
family dimension there (COUNTING-BOUND), or reach a full polynomial pair
(print it; check J directly; degrees (99,66); type REPRESENTATIVE — a genuine
Keller pair would be a counterexample: do not claim without the direct check
and an independent recomposition); (4) controls: Xu's own excluded cases must
come out excluded by your machinery at the first inconsistent order (the
[1,1,1] at δ = 2 via the same setup; and a δ ∉ {2, 5/2} order, e.g. δ = 7/3);
wrapper controls; (5) verdict with typed scope; FALLACY-v2 applies. ≤ 150 min;
2 cores; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane
reports (moh9966-B-lift, k16-middle-spine, k16-t4-normalizer-gate, chart-fix-
d1zero, bigrows-preprocess). Drivers to box/xu52-20260903/.
Report: xmodel/xu-delta52-lift-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 150 minutes.
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/moh9966-branchB-sol56-20260903.md
charged_input=xmodel/minor-dichotomy-sol56-20260903.md
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/xu-delta52-lift-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
8338a702448a61ef10af214e5d156e0c14ad117ef231ae34aee462fb36fa649f  {{LANE_INPUTS}}/moh9966-branchB-sol56-20260903.md
184a689f3cd63405d922b8118632c7e17f96f471a0bc71f9a50cd161b8a87ad1  {{LANE_INPUTS}}/minor-dichotomy-sol56-20260903.md
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
