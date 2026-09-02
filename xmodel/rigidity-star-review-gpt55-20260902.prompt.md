# Batch hostile review: EXACT-N-RIGIDITY (Opus) and STAR-REALISABILITY (Sol) — the Φ-lemma, the floor L, COROLLARY NO-RESIDUE, the A_bot witness, the mixed/single integrality counts; the Prop 4.6/A.5 squarefree bottom

Both charged reports are PROVED-HERE/UNREVIEWED and sit on top of
integration #17 (reviewed: JAC-FIBRE, FRONTIER-EXACT, D1-PIN, D1-STAR,
PIN-NOT-CEILING). Do not re-review #17; review what is NEW.
EXACT-N-RIGIDITY claims: (1) Φ(δ) := δ − λ_f(δ) − λ_g(δ) along a root of
g is non-increasing (slope 1 − a − b); LEMMA DICT: Φ(δ⁰) ≥ 1 at every
proper frontier; Φ(δ₁) = 1 by RADIUS-ORDER at r = 1 with M₁ = −m; hence
Φ ≡ 1 on [δ₁, δ⁰] and a + b ≡ 1 (the star as one sandwich); (2) the
r = 1 identity is not an artefact of Def 5.1(3) (Moh Prop 5.3 defines
δ_{r−1} geometrically and proves the formula; four explicit Keller pairs
verify Φ(δ₁) = 1 from the joint tree); (3) A_bot is not a skeleton
function: witness (x + y⁵, y + (x + y⁵)³) with five conjugate bottom
discs (ν = 1); EXACT-N = the two-sided window L = eV₂d(1−δ₁)/(d+e) ≤ N ≤
U = ude(1−δ₁)/(d+e), L/U = V₂/u, plus integrality; L never exceeds 3.32
to D ≤ 190; (4) MEASURED D ≤ 140: U < 6 kills 3.9%, EXACT-N MIXED 29.2%
(D = 105: 159 of 264, exact), SINGLE 66.4%; D ≤ 190 SINGLE 65.0%; no
degree emptied; (5) COROLLARY NO-RESIDUE: the x⁻¹ coefficient of
d/dx f(x, τ(x)) vanishes for ANY Puiseux series τ, so for a Keller pair
the x⁻¹ coefficient of 1/g_y(x, τ) vanishes on every branch of every
fibre of g — a necessary condition on g alone; negative control
g = y² − x² − x with [x⁻¹] = ±1/2 and δ⁰ = 1.
STAR-REALISABILITY claims: (6) Moh Prop 4.6 at r = 1 gives
D(n, −M₁, g_{σ₁}(π), T^ψ_{1,σ₁}(π)) = c ≠ 0, which by Prop A.5 (p.207;
invoked by Moh on p.184) forces the product squarefree, so the bottom
partition is (1^{eV₂}) for every skeleton; the forced-repeated-root
obstruction kills nothing (9,553 assignments at D ≤ 120, 0 killed);
correction: "Prop 4.6 at r = 1 does not force simple roots" is false
as an implication; (7) the campaign-order smallest (UNI) D = 105 row:
n = 105, m = 70, M = (−70, −63, 103), V = (1,4,1), (d,e) = (2,3),
(u,v) = (20,15), q = 3/10, N = 6.
Your task, hostile: CONFIRMED / GAP / REFUTED per item with line and
repair. Mandatory: (a) reprove the Φ-lemma (monotonicity and Φ(δ⁰) ≥ 1
from JAC-FIBRE) and Φ(δ₁) = 1; (b) reprove NO-RESIDUE — is "vanishes for
ANY Puiseux series" right for series with fractional exponents (the
x⁻¹ term of a derivative of Σ c_k x^{k/ℓ}), and is the negative control
correctly computed?; state exactly what NO-RESIDUE adds beyond Moh's
search conditions (which are its leading-order consequences) and
whether it is a SKELETON condition at any order; (c) the A_bot witness:
verify five conjugate bottom discs and N = 1 for (x + y⁵, y + (x + y⁵)³)
by resultant; (d) rerun exactn.py at D ≤ 100 and confirm the MIXED
count at D = 105 (159/264) against GPT-5.5's exact-packet-filter
(125 hits at N ≥ 6, 105 in [6,16]; xmodel/exact-packet-filter-gpt55-
20260902.md) — reconcile the two counts exactly (which variant each
computes); (e) Prop 4.6 → A.5: read pp.184 and 207 from the page
images and confirm the squarefree conclusion and its scope (r = 1,
"all-roots subcase"?); (f) the D = 105 row of (7): recompute q and N.
Typed verdict block; promotion recommendation per item; bounded
quantity of any OPEN. Desk-scale CAS; no ledger edits; no jc2-lean.
Report: xmodel/rigidity-star-review-gpt55-20260902.md
Seal-at-completion with the standard <!-- BODY-END --> marker;
bounded writes; target 20-30KB; 75 minutes.
charged_input=xmodel/exact-n-rigidity-opus5-20260902.md
charged_input=xmodel/star-realisability-sol56-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=box/exactn-drivers-20260902/dictionary.py
charged_input=box/exactn-drivers-20260902/exactn.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e639fdbf5cdbdf0756d9d8287b52c0183b07e2bf8ab7d4b293c242ea2c35f37c  {{LANE_INPUTS}}/exact-n-rigidity-opus5-20260902.md
16728d4ae6b877c7321217c9c133bb68a5d2c05dbca85070dfc35296efce7bbd  {{LANE_INPUTS}}/star-realisability-sol56-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
8081141ad4b545dc27fccce1046e49f650efc54b717a11adcf70af966a8b477d  {{LANE_INPUTS}}/dictionary.py
d1f3529f0daa99fa5f5d4011f65601349d4206222b229fc779c852e1392f8f36  {{LANE_INPUTS}}/exactn.py
```
