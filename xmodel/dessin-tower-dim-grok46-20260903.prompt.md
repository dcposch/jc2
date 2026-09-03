# Research lane: DESSIN-TOWER expected dimension — admissible covers of Moh's major-disc tree with a Davenport–Stothers (STAR-ABC) passport at every bottom vertex and Prop 4.6 passports at internal vertices; the integer expdim(S, k) per skeleton, evaluated on Moh's six rows, the 652 excess rows, the D = 105 trio and a D ≤ 120 slice

From the blind Grok submission of round 20260903T1015Z (charged; Card II,
OPEN[DT-DIM]) and the reviewed record: BOTTOM-ODE ⟺ STAR-ABC (promoted): at
each bottom-major disc the pair (p_f, p_g), deg (dV_2, eV_2), is a
Davenport–Stothers / ABC-extremal pair, i.e. p_f^e / p_g^d is a Belyi map of
degree deV_2 with passport [e^{dV_2}], [d^{eV_2}], [(d+e)V_2 − 1, 1^γ],
γ = V_2(de − d − e) + 1 (TF-DESSIN, promoted; existence for every (d,e,V)
is a GAP). The k bottom discs are a Galois orbit (or several) glued through
the Puiseux tower D_s ⊃ … ⊃ D_1 (Def 5.1; Prop 4.6 at every level r ≥ 2
requires a squarefree polynomial q of degree V_r(n − M_{r−1})/d_r > 1
containing every root of p — a DS-type condition at every level, SOURCE-
READ by the Grok lane, p.182). Question: the expected dimension of the
space of such "dessin towers" as a function of (d, e, V_*, s, k) — genus-0
admissible-cover counting (r − 3 per component minus automorphisms plus
node conditions), with the STAR-ABC passport at each bottom vertex and the
Prop 4.6 passport at each internal vertex.
YOUR TASK:
(1) DEFINE the object precisely (the cover, the marked points, which data
    are prescribed by the skeleton and which are moduli: the branch
    constants a_O per orbit, the DS moduli γ per bottom star, the outer
    coefficients shared at junctions) and derive expdim(S, k) as a closed
    formula. Type every step; where the Prop 4.6 internal passport is not
    fully determined by the printed text, say so (SOURCE-UNVERIFIED) and
    give the two natural readings.
(2) EVALUATE (desk python over box/moh_skeleton_full.py):
    (a) Moh's six p.202 rows — must be ≥ 0 (Appendix II kills them by a
        further computation, not by dimension) or the formula is wrong
        [HARD gate]; (b) the 652 excess (1)–(13) rows at n ≤ 100 — does
        expdim < 0 separate them from the six? (c) the D = 105 trio with
        k ∈ {12..24 even}, 13, 17; (d) all groups alive at N ≥ 6 in
        48 ≤ D ≤ 120 (670) — sign distribution; growth with D.
(3) Compare with (i) the (2,3,V_2 = 1) rigidity: the DS pair is unique up
    to normalisation (field of moduli Q), so a k-orbit of identical stars
    has only k gluing constants against n − m polynomiality relations —
    is that count a special case of your formula, and does it kill every
    V_2 = 1 skeleton (Opus card 3, charged §11); (ii) ORTHO-DEFECT
    2deN = Σ(e m_ν − d m'_ν)² as the infinitesimal shadow (Grok §8).
(4) READING: the trichotomy — expdim < 0 at every N ≥ 6 type (a proof
    candidate: state the theorem needed), = 0 (rigid isolated CE
    candidates: list them), > 0 growing with D (moduli: the CE list; the
    proof must be Q3(a)). Bounded quantity of every OPEN.
Controls: automorphisms (y, x + y^k) and the composition
(x + y⁵, y + (x + y⁵)³) (five bottom discs, ν = 1, outside NU-TWO) must
have expdim ≥ 0 with the expected free parameters. Desk-scale (< 20 min one
core, < 4 GB); do not edit canonical ledgers; do not inspect jc2-lean; do
not read other ideation-20260903T1015Z-* files than the two charged; do
not read other running lanes' reports. The Moh PDF is at
refs/moh1983_jram340_configurations_of_roots.pdf (page N = PDF page N−139;
read images via pdftoppm).
Report: xmodel/dessin-tower-dim-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-30KB; 120 minutes.
charged_input=xmodel/ideation-20260903T1015Z-grok46.md
charged_input=xmodel/ideation-20260903T1015Z-opus5.md
charged_input=xmodel/time-function-endgame-review-sol56-20260902.md
charged_input=xmodel/time-function-endgame-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/tfe-drivers-20260902/bottomode.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
7b56aad2c1fb067481852eedecc89ba5598cd26eeb2cf3358c3b8c2f16438015  {{LANE_INPUTS}}/ideation-20260903T1015Z-grok46.md
b13149ecac656f7f3548e6cd388b1699c514ff49a53882f7239039a2c0022562  {{LANE_INPUTS}}/ideation-20260903T1015Z-opus5.md
9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d  {{LANE_INPUTS}}/time-function-endgame-review-sol56-20260902.md
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  {{LANE_INPUTS}}/time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
