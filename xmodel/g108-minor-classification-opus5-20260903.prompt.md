# Source + design lane (packet Q3 in advance): the SECOND u_s > 1 CLIENT of the joint-chart engine — the D = 108 row (108,72; M = (−72,81,106); d = (108,36,9,1); V = (7,7); u₃ = 2; v₃/u₃ = 7/2; major radii (3/8, 1/4, −1)) — classify its admissible principal-minor split orders (the (99,66) recipe: Prop 6.1 order identity ord g(σ) = (n/d_s)(u_sδ − v_s) and the ceiling δ < v_s/u_s = 7/2; Xu Prop 7.3 δ > 1; N5 den(δ) ≤ u_s = 2 [PROMOTED]; the face-ODE budget and the Galois argument for each candidate δ ∈ {3/2, 2, 5/2, 3}), determine the faces (partition, leaders, rigidity), and DESIGN the joint chart for the survivors so the band engine can run it

OPERATIONAL: skeleton first; CAS jobs in the foreground with `timeout`; never
end the turn with a job running; ≤ 2 cores. Context (banked): at (99,66) the
classification {2 [2,1], 5/2 [1,1,1]} was derived by exactly this recipe
(17(iii), (nnn), (rrr), (sss)) and the joint-chart engine then killed the δ = 2
branch (17(pppp)); the D = 108 u_s = 2 row is the first u_s > 1 skeleton above 100
under the operative screen (17(qq): only δ* ≥ 1 known; OPEN[MINOR-RADIUS-108])
and the natural second client. Task: (1) SOURCE-READ (page images; name pages)
Moh pp.190–194 (Prop 6.1 and the minor/major dichotomy at the top disc) and
Xu §7.3/§8 (charged reports transcribe them); compute for this row the
principal-minor data: n/d_s = 12, u_s = 2, v_s = 7, so ord g(σ) = 12(2δ − 7) for
a split of order δ, detector iff δ < 7/2; the leading polynomial p(π) of degree
u_s = 2 (so partitions [2] (unsplit = linear power, Moh's branch-A analogue) and
[1,1]); the Xu-type orders of f, g, T₂, T₃ at σ (derive the analogues of the
five displayed orders — from the effective quasi-approximate-root
multiplicities (−μ_i)u_s/d_s: compute μ₂, μ₃ for this skeleton from the
semigroup data (Moh p.150: q₁ = M₁, q₂ = M₂ − M₁, λ₂ = q₁d₁ + q₂d₂, μ₂ = λ₂/d₂; and
λ₃, μ₃)); (2) for each candidate δ with den ≤ 2 in (1, 7/2) — 3/2, 2, 5/2, 3 —
run Xu's ODE exclusion (equation (7.1) at that order: q = p^{l−1}(π − c) forms,
the degree budget, the Galois action of the ramified parameter t^{1/2} at
half-integral δ) and decide EXCLUDED / SURVIVES, with the surviving faces
(p, q₁ or R) in closed form and their rigidity (dimension mod gauge); (3)
DESIGN the joint chart for each surviving face: the major tower rows (h₃ of
y-degree 9 ⊂ h₂ of degree 36 ⊂ f of degree 108 — Theorem 1.2 order bounds on
the approximate-root tower; the outer D₂/D₁ bands as in 17(dddd)), the minor
incidence block for the face, the Jacobian rows; count the ambient
coefficients and estimate the first prefix dimensions (do not run the full
bands — that is the engine lane's job); state what must be adapted in the
charged band_engine.py (the (99,66)-specific constants: degrees, root counts,
the pole exponents −77/−50 etc.) to run this row; (4) controls: replay the
(99,66) classification with your code (must give {2 [2,1], 5/2 [1,1,1]}); (5)
verdict: the D = 108 split classification (typed), the faces, the chart
design, and the exact next lane; FALLACY-v2 applies. ≤ 120 min; no ledger
edits; no jc2-lean; no ideation-* files; no in-progress lane reports. Drivers
to box/g108minor-20260903/.
Report: xmodel/g108-minor-classification-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-22KB; 120 minutes.
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=xmodel/g9966-review-gate-grok46-20260903.md
charged_input=xmodel/n5-denominator-grok46-20260903.md
charged_input=xmodel/n5-gate-gpt55-20260903.md
charged_input=xmodel/minor-dichotomy-sol56-20260903.md
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/g9966-global-design-sol56-20260903.md
charged_input=xmodel/g9966-design-gate-grok46-20260903.md
charged_input=xmodel/g9966-outer-bridge-grok46-20260903.md
charged_input=box/g9966band-20260903/band_engine.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/g108-minor-classification-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
dc2355a81dd472993c9af0fb0f03eb5b6f3c087c3a2ed00120615b76bcf91be8  {{LANE_INPUTS}}/g9966-review-gate-grok46-20260903.md
7652748ebe24a50345b0450744851ee8f920440d00307d0dd7c7fac074674816  {{LANE_INPUTS}}/n5-denominator-grok46-20260903.md
666a1c900d7e3b14b772fec58839b8abff6f71e21ffe5852734fd80f6f983a0c  {{LANE_INPUTS}}/n5-gate-gpt55-20260903.md
184a689f3cd63405d922b8118632c7e17f96f471a0bc71f9a50cd161b8a87ad1  {{LANE_INPUTS}}/minor-dichotomy-sol56-20260903.md
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
a81ff0263cf379a297b8d1812ebfa26eb95f7e58d91ef4edc62a3a68edf2d782  {{LANE_INPUTS}}/g9966-global-design-sol56-20260903.md
0cbeaf0735b92f18e3a7c5050775b99c3739b658584ce0d02965a24db2c1273b  {{LANE_INPUTS}}/g9966-design-gate-grok46-20260903.md
7facb109db6eb21b73970c2b6a0d4339bc51c7b73f3ce16782950550508e2674  {{LANE_INPUTS}}/g9966-outer-bridge-grok46-20260903.md
3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9  {{LANE_INPUTS}}/band_engine.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
