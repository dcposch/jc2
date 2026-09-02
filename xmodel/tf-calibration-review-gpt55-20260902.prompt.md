# Hostile review lane: TIME-FUNCTION CALIBRATION D = 48 — the census omission of Moh (8)–(11), the Galois congruence (10)₁, the reconstructed (10), TF-0 / TF-DESSIN / TF-NOTAME / TF-EXH, the D ≤ 120 rebased counts

The charged Opus report claims: (1) the campaign enumerator
box/moh_skeleton_N.py (and d1floor.py, general.py) implements Moh 1983's
search conditions (1)–(7) and the Def 5.1(2) windows only, NOT (8)–(11);
(2) PROVED-HERE, both branches: (10)₁ — the order-Δ₁ Galois automorphism
of the bottom star (Moh's search condition (8)) multiplies π by a
primitive Δ₁-th root of unity and permutes the a₁ = eV₂ SIMPLE roots of
p_g; at most one root is 0, hence eV₂ ≡ 0 or 1 (mod Δ₁), Δ₁ = den(L₁δ₁),
L₁ = lcm{den δ_s, …, den δ₂}; all six Moh survivor rows pass; (3)
RECONSTRUCTED (OCR-damaged p.201; the α = 0 alternative (11) not
recovered): (10) at j ≥ 2: Δ_j V_j ≤ V_{j+1} d_j/d_{j+1}; (4) TF-0: the
r = 1 clause d·Q·P′ − e·Q′·P = γ ≠ 0 forces simple roots for BOTH p_g
and p_f and gcd = 1 (refuting "intra-f clustering below δ₁ is free");
TF-DESSIN: Q^e/P^d is a genus-0 Belyi map with profile
(d^{eV} | e^{dV} | ((d+e)V − 1, 1^*)) whose dessin exists for every
(d,e,V) (a cubic plane map: a tree with V + 1 leaves, a loop per leaf),
so the leading order never kills; TF-NOTAME (L_ν injective on the
tame-silent subspace for ν ≠ 1 − δ₁; h′(C) = 0); TF-EXH (bottom-major
discs exhausting D₂, i.e. N = U, ⇒ at most ONE bottom disc); (5) the
exact order-graded decomposition (♦) of [f,g] = c at a bottom disc, with
A + B − 1 + δ₁ = 0 being D1-PIN; (6) MEASURED: D = 48 selected skeleton
(48, 32, M = (−32,−12,46), V = (1,3), δ = (−1, 7/22, 3/8), a₁ = 3, q = 3/4)
dies at order 0 by (10)₁ (Δ₁ = 4); with (10) + (10)₁ at D ≤ 120:
902,893 V-assignments → 3,760 → 329; 10,637 groups → 1,012 → 287 → 233
knapsack-alive; degrees emptied 48, 66, 78; D = 105: 264 → 3 (m = 70,
M = (28,103), V_s ∈ {5,6}; M = (40,103), V_s = 4); with (10)₁ alone at
D ∈ [48,90]: 86.7% of V-assignments, 14% of groups killed.
A parallel lane (census-rebase) is recovering (8)–(13) verbatim from
the page images; do NOT duplicate that — but DO read p.201 yourself at
≥ 200 dpi to check whether (10)₁ and the reconstructed (10) are what
Moh prints, and say exactly where they differ.
Your task, hostile: CONFIRMED / GAP / REFUTED per item with line and
repair. Mandatory: (a) verify the omission claim by reading
moh_skeleton_N.py (which of (1)–(13) are implemented, function by
function); (b) reprove (10)₁ from Moh's (8) as printed — is the
automorphism of order Δ₁ correctly identified, is Δ₁ = den(L₁δ₁) the
right modulus (why L₁?), and does "at most one root is 0" need the
star to be centred at 0 (a normalisation) or is it invariant?; (c)
reprove TF-0 and TF-DESSIN (the passport and the existence argument —
Riemann existence for the given profile; is the "cubic plane map"
description right?); (d) TF-EXH: reprove the identity Σ_{i<j} V_iV_j = 0
⇒ one disc, and state its exact hypotheses (TF-NOTAME's scope);
(e) rerun bottom_star.py / kernel_L.py and the D = 48 sweep; spot-check
(10)₁ on 20 random V-assignments at D = 105 by hand; confirm the three
D = 105 survivors under (10)+(10)₁ and say whether they also survive
(10)₁ alone; (f) the six Moh rows: confirm each passes (10)₁ and the
reconstructed (10) (two at equality). Typed verdict block; promotion
recommendation per item (mark the reconstruction as NOT promotable
until census-rebase lands); bounded quantity of any OPEN. Desk-scale;
no ledger edits; no jc2-lean.
Report: xmodel/tf-calibration-review-gpt55-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 20-30KB; 75 minutes.
charged_input=xmodel/time-function-calibration-d48-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=box/tfcal-drivers-20260902/bottom_star.py
charged_input=box/tfcal-drivers-20260902/kernel_L.py
charged_input=box/moh_skeleton_N.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
db8a10c986a8a8a7b83c285585e299d887c72e52417b76ea7fca8c4fd0dbff2a  {{LANE_INPUTS}}/time-function-calibration-d48-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
437c5b45facf61e8e24d5399da50d131310b360f8184667a25c7388c6941c09e  {{LANE_INPUTS}}/bottom_star.py
a84e7e92b7a17c85fb96ce3fc784bdc15952583cf4ce892a2ded2838ad7bf3dc  {{LANE_INPUTS}}/kernel_L.py
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
```
