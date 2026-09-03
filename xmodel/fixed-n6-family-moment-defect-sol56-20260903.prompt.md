# Research lane: FIXED-N6 FAMILY — the explicit unbounded (1)–(13) family with pinned N = 6, its first global moment/parity-check page for L = 5, 13, 21, 29, and the valuated rank defect as a candidate cofinal invariant

From the blind Sol submission of round 20260903T1015Z (charged; §2.3, §3.3,
Card 2): for every a ≥ 0, L = 8a + 5, the skeleton n = 21L, m = 14L,
M = (−14L, 7(3L+1)/4, 21L − 2), s = 3, V₂ = 1, V₃ = 5 passes Moh's printed
(1)–(13) with d₂ = 7L, d₃ = 7, δ = (−1, 2(3L−1)/(3(5L−1)), 7/12), A₂ =
3(5L−1)/4, q = 1/2, u = 5L; the formal (UNI) packet k = 12 gives N = 6
(degrees 105, 273, 441, …; first 21 members machine-checked). CORRECTION
from branch-orbits v2 (charged, PROVED-HERE/UNREVIEWED): (UNI) is not a
theorem; a bottom-disc Galois orbit has size |O| = ∏_{j=2}^{s−1} ω_j with
ω_j = A_j on a (10)-level and 1 on an (11)-level; at s = 3 the packing
Σ|O|V₂ ≤ u is exact — so the family's admissible packets are k ∈ |O|·Z with
|O| = A₂ (if the D₂ → D₁ split is (10)-only) and N = k/2: state the
orbit-admissible N for each L (at L = 5, D = 105 group A, k = 18, N = 9).
The global interpolation conditions (Sol framework lane, charged, sealed):
for the n roots τ_i of g − c₂ with primitives H_i = ∫dx/g_y(τ_i) + a_i,
the moments M_r = Σ_i H_i τ_i^r/D_i (D_i = ∏_{j≠i}(τ_i − τ_j)) satisfy
M_0 = … = M_{n−m−2} = 0 and M_{n−m−1} = 1 (DEG; n − m − 1 = 7L − 1
homogeneous rows growing with L while the bottom packet stays fixed), plus
polynomiality (POLY) and NO-RESIDUE; the driver
box/globalinterp-drivers-20260902/globalinterp.py emits the exact system
for a DECORATED skeleton (tree, orbits, templates, sharing, guard).
YOUR TASK:
(1) VERIFY the family: (1)–(13) membership and the δ, A, q, u formulas
    symbolically in L (not only numerically), and the orbit-admissible
    packets/N per branch-orbits v2; type PROVED-HERE with the algebra.
(2) DECORATE the family member for L = 5, 13, 21, 29 (single-orbit packet,
    the (2,3,V₂ = 1) rigid bottom star p_g = π³ − π, p_f = π² − 2/3 at each
    of the k discs; the unique D₂ with all ue = 15L major roots; the minor
    block of NONPROPER-COUNT e(K − ΣV₂) roots) and EMIT with globalinterp.py
    the associated-graded moment matrix on the first bottom-separation page
    (the first z-orders at which (DEG) rows are non-vacuous): for each L
    report (unknowns, equations, exact rank over Q or over three good primes
    with rational reconstruction, cokernel), the minimum-weight (tropical)
    bases from the tree valuations, and whether the rank defect GROWS with
    L, is constant, or is repaired by the non-proper block (report the Schur
    complement of the non-proper coordinates separately).
(3) READING: is there a stable minor / left-kernel functional across L
    whose valuation and leading coefficient can be conjectured in closed
    form (the valuated-MDS defect)? If yes, state the conjectured cofinal
    obstruction as a theorem to prove; if the non-proper block always
    repairs, name the interface the counterexample lane needs.
Controls: the tame pairs (y, x + y^k) must pass at the same page; the
g-alone negative control y² − x² − x must fail at t-order 1; a decoration
with a partial orbit must be REFUSED by the driver (custody check).
Discipline: PROVED-HERE/UNREVIEWED; bounded quantity + cheapest test of
every OPEN; desk-scale CAS (< 30 min one core, < 6 GB — the L = 29 case has
202 vanishing rows; if it exceeds the cap, stop at the largest L that fits
and say so); do not edit canonical ledgers; do not inspect jc2-lean; do not
read other ideation-20260903T1015Z-* files than the charged Sol one; do not
read other running lanes' reports. Drivers to box/fixedn6-drivers-20260903/.
Report: xmodel/fixed-n6-family-moment-defect-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 25-40KB; 150 minutes.
charged_input=xmodel/ideation-20260903T1015Z-sol56.md
charged_input=xmodel/global-interpolation-sol56-20260902.md
charged_input=box/globalinterp-drivers-20260902/globalinterp.py
charged_input=xmodel/branch-orbits-v2-grok46-20260903.md
charged_input=box/branch-orbits-v2-20260903/knapsack.py
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=xmodel/integration17-coordinator-fable51-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
20f290f7e33a3b8a4f97d303751633b9d9b2df50ca8cbd0a46498856be5d5b2f  {{LANE_INPUTS}}/ideation-20260903T1015Z-sol56.md
20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6  {{LANE_INPUTS}}/global-interpolation-sol56-20260902.md
49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588  {{LANE_INPUTS}}/globalinterp.py
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  {{LANE_INPUTS}}/branch-orbits-v2-grok46-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  {{LANE_INPUTS}}/knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
```
