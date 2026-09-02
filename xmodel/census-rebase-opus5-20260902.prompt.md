# Computation lane: CENSUS-REBASE — recover Moh's search conditions (8)–(11) verbatim and rebase the campaign skeleton census on Moh's true admissible space

The charged calibration report (PROPOSAL; treat as such) found that the
campaign's skeleton enumerator (box/moh_skeleton_N.py and its
descendants d1floor.py / general.py) implements Moh 1983's search
conditions (1)–(7) and the Def 5.1(2) windows but NOT (8)–(11); it
PROVED the level-1 congruence (10)₁: eV₂ ≡ 0 or 1 (mod Δ₁) with
Δ₁ = den(L₁δ₁), L₁ = lcm{den δ_s, …, den δ₂} (the order-Δ₁ Galois
automorphism of the bottom star permutes the a₁ = eV₂ simple roots of
p_g), and RECONSTRUCTED (OCR-damaged source) (10) at j ≥ 2 as
Δ_j V_j ≤ V_{j+1} d_j/d_{j+1}, WITHOUT the α = 0 alternative (11). With
both: D ≤ 120: 10,637 groups → 287 → 233 knapsack-alive; D = 105: 264 → 3;
D = 48, 66, 78 emptied. Everything in integration #17's filter tables
was computed on the superset.
YOUR TASK (source-critical, then computational):
(1) RECOVER (8)–(13) VERBATIM. Render Moh 1983 pp.200–202 (PDF pages
    61–63 of refs/moh1983_jram340_configurations_of_roots.pdf, hash it)
    at ≥ 200 dpi with pdftoppm and READ THE IMAGES (the OCR in
    box/depth-drivers-20260902/moh.txt is unrecoverable there). Transcribe
    conditions (8), (9), (10), (11), (12), (13) exactly as printed, with
    every symbol defined from Moh's text (Δ_j, L_j, the α ≠ 0 / α = 0
    branches, the multiplicity V_{r−1} form). State where the
    calibration lane's (10)₁ and its reconstructed (10) at j ≥ 2 agree
    with, sharpen, or DIFFER from the printed conditions; recover (11).
(2) IMPLEMENT (8)–(13) exactly (both branches where Moh has two) in a
    copy of moh_skeleton_N.py (box/moh_skeleton_full.py) with a
    fail-closed control: Moh's published table of surviving skeletons
    at n ≤ 100 (pp.202 and 207, read the images) must be reproduced —
    every printed row survives your (1)–(13), and the count of survivors
    at each printed n matches Moh's "25 values" / his table to the unit
    (the N-ON-THE-TREE report calibrated the (1)–(7) census to 2410 at
    n ≤ 100; state what the full (1)–(13) count is).
(3) RERUN the integration-#17 programme on the true space at D ≤ 120,
    one core: per degree V-assignments / groups after (1)–(13); after the
    pinned-N integrality knapsack (N ∈ Z, N ≥ 6; and [6,16]) in both
    (UNI) and mixed form; degrees emptied (state whether any D > 100
    empties — do NOT expect it); the surviving D ∈ {105,108,112,117,120}
    groups LISTED in full (n, m, M_*, V_*, δ_*, q, achievable N); and for
    each of the six Moh published survivor rows, confirmation that it
    passes (1)–(13) (it must — those rows were killed only by his
    Appendix II).
(4) Extend the count (no knapsack) to D ≤ 200 if it fits in 20 min.
Discipline: PROVED-HERE / MEASURED typing; quote Moh with page and
line for every condition; desk-scale (one core, < 4 GB); state the
bounded quantity of every OPEN you raise; do not edit canonical
ledgers or the existing enumerators in place; do not inspect jc2-lean.
Report: xmodel/census-rebase-opus5-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 25-40KB.
charged_input=xmodel/time-function-calibration-d48-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/n-on-the-tree-opus5-20260902.md
charged_input=box/moh_skeleton_N.py
charged_input=box/tfcal-drivers-20260902/d1floor.py
charged_input=box/d1sub-drivers-20260902/general.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
db8a10c986a8a8a7b83c285585e299d887c72e52417b76ea7fca8c4fd0dbff2a  {{LANE_INPUTS}}/time-function-calibration-d48-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967  {{LANE_INPUTS}}/n-on-the-tree-opus5-20260902.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
e7d7d2e6f108f7a50392f530f7f561c30685dd17c8cfeed3d01e57ce97865b28  {{LANE_INPUTS}}/general.py
```
