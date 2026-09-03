# Hostile review + experiment lane: PS-GROWTH identities (different-model gate) and EXPERIMENT NEXT-COEFF — are the n − m − 1 global trace identities computable as resultant coefficients over Q?

Charged Opus flagship ps-growth-opus5-20260903.md (drivers
box/psgrowth-drivers-20260903/) claims, PROVED-HERE: PS-0; LEMMA EJ
(Tr_{A/R}(h/g_y) = [y^{n−1}](h mod (g − c)), A = C[x,c][y]/(g − c), g monic);
PS-1' dP_{k+1}/dx = (k+1)[y^{n−1}](J f^k mod (g − c)) with NO hypothesis on J
(= equality of mixed partials of log χ, χ = Res_y(g − c, T − f)); PS-1c
dP_k/dc = [y^{n−1}]((f^k)_y mod (g − c)); PS-2/PS-3/PS-3+ (deg_x R_k ≤
⌊(k+1)c_max⌋ − 1, c_max = max branch growth of f); PS-3-SHARP c_max = q_max/e
from D1-PIN; THEOREM RESIDUE-LEAD: the bottom-disc leading coefficient of
R_k is (d/κ)·p̃_{k+1}, the power sum of the Davenport–Stothers star; the
NEGATIVE reading (PS-3 generically attained; K = gcd(m,n) invisible; no
D-ceiling); RES-DEGREE corrected (deg_x Res_y(g − c₂, f − c₁) = N; witness
g = y³ + xy, f = y + 1 refutes the charged form); all 12 census (d,e,V) stars
exist (saturated Gröbner; a sympy.solve "no (2,3,2) star" artefact retracted);
the tree-free c_max certificate from the Newton polygon of χ.
PART A — hostile review: CONFIRMED / GAP / REFUTED per item with line and
repair; rerun every driver (psgrowth.py 20, leadcheck.py, resdeg.py,
existence.py, genfun.py, trio105.py; report counts); attack specifically:
(a) LEMMA DEG's quantifier order (per-k choice of c₂ avoiding three finite
sets) — is the bound on deg_x really independent of c₂; (b) PS-3's use of
JAC-FIBRE at proper branches and the non-proper case (ord_t g_y = −δ⁰ < −1);
(c) RESIDUE-LEAD's step ord_t g_y = λ_g − δ₁ = c − 1 ("this IS Φ(δ₁) = 1") and
the cross-orbit survival condition 1 − (k+1)c_max ∈ Z; (d) the claim that K is
invisible — construct the explicit dependence of (m, n, q_max, e) on the tower
and confirm no quantity in the family sees d₂ = K beyond e = n/K;
(e) the RES-DEGREE witness; (f) OPEN[PS3-NEG]: exhibit a non-Keller monic
pair with deg_x R_k > (k+1)c_max − 1 or prove PS-3 needs no (KEL).
PART B — EXPERIMENT NEXT-COEFF (the lane's charge §6): for the Keller controls
(y, x + y^k) k = 2..6, (x + y², y + (x + y²)³), (x + y³, y + (x + y³)²),
(x + y⁵, y + (x + y⁵)³), expand R_k = [y^{n−1}](f^k mod (g − c)) COMPLETELY in
x (all coefficients, exact over Q) for k ≤ 20, and likewise the weighted
residues R_k^{(w)} := [y^{n−1}](w·f^k mod (g − c)) for w = s_r(τ̂) (elementary
symmetric functions of the OTHER roots — i.e. the coordinator's trace
identities Tr(f s_r/g_y), computable via the driver's residues(..., weight=w)
or via Lagrange). Identify, order by order in x, which tower level each
coefficient depends on (use the known towers of the controls: e.g. the
composition has five conjugate bottom discs at level 1 under one D₂). DECIDE:
is the coefficient at x-order (k+1)c_max − 1 − j a function of the tower data
down to level j only (so that the n − m − 1 global moment identities of the
promoted framework (delta 17(l)) are resultant coefficients over Q, computable
with no Puiseux expansion, no exponent semigroup and no outer/inner split)?
Gate: on (x + y², y + (x + y²)³) the level-2 data is known — check the level-2
prediction. Report the answer as YES (with the exact dictionary coefficient ↔
level, and a proposal for re-basing globalinterp.py onto Res_y) / NO (with the
first coefficient that mixes levels) / PARTIAL.
Discipline: PROVED-HERE/UNREVIEWED; bounded quantity + cheapest test of every
OPEN; desk-scale (< 20 min one core, < 4 GB); no ledger edits; no jc2-lean;
do not read ideation-20260903T1015Z-* files or other running lanes' reports.
Drivers to box/nextcoeff-drivers-20260903/.
Report: xmodel/next-coeff-psreview-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/ps-growth-opus5-20260903.md
charged_input=box/psgrowth-drivers-20260903/psgrowth.py
charged_input=box/psgrowth-drivers-20260903/leadcheck.py
charged_input=box/psgrowth-drivers-20260903/resdeg.py
charged_input=box/psgrowth-drivers-20260903/existence.py
charged_input=box/psgrowth-drivers-20260903/genfun.py
charged_input=xmodel/global-interpolation-sol56-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/exact-n-rigidity-opus5-20260902.md
charged_input=box/tfe-drivers-20260902/bottomode.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
9ef022e87f7f0193861e667a6bdaf22df58c4200cafe0d96c73122291e5c3e83  {{LANE_INPUTS}}/ps-growth-opus5-20260903.md
ecc304f044bfef291b9ec619d342c0b1d6c68cf48cde66667ca5da0dfc906c1b  {{LANE_INPUTS}}/psgrowth.py
7c3ea309a8e929f4907b52cbaf6818d086adf6fe796a3ad3d8b6c64d7b720f09  {{LANE_INPUTS}}/leadcheck.py
b08b201ee6d53467ab93732d4702d5544c470f3f26e3f41d2aa519bc5eae82c0  {{LANE_INPUTS}}/resdeg.py
7800a756991f56cb7cc48831f7629238981b03d3d1c525e12df5d479de424281  {{LANE_INPUTS}}/existence.py
2d6d7495e33908cf0bd49877384c95581d8254ce471f30324eb2b18a0aa62aad  {{LANE_INPUTS}}/genfun.py
20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6  {{LANE_INPUTS}}/global-interpolation-sol56-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
e639fdbf5cdbdf0756d9d8287b52c0183b07e2bf8ab7d4b293c242ea2c35f37c  {{LANE_INPUTS}}/exact-n-rigidity-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
```
