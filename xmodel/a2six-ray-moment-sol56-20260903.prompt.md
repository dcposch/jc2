# Research lane: the A₂ = 6 RAY — the true fixed-N = 6 laboratory: n = 9(7t+6), orbit-pinned N = 6 for every t; the first global moment/parity-check page at D = 54, 117, 180, 243 through globalinterp.py; the valuated rank defect as a cofinal invariant

Reviewed (AUDIT delta 17(n), charged n6-family review): Sol's L = 8a+5 family
has orbit-admissible N = 15a + 9 (not 6), so it is not a fixed-N laboratory.
The reviewer's replacement (PROVISIONAL, sympy + census-emitted at t = 0..3):
for every t ≥ 0, P = 7t + 6: n = 9P, m = 6P, M = (−6P, 4P, 9P − 2), s = 3,
V₂ = 1, V₃ = 6t + 5; d₂ = 3P, d₃ = P; δ = (−1, 1/6, 7/12); A₂ = 6 constant,
A₁ = 2; Q = 18t + 15, (10)-only, (13); q = 1/2, u = 18t + 15; bottom-disc
orbit size |O| = 6 (delta 17(j) law, exact at s = 3), up to 3t + 2 copies;
orbit-admissible N = {3, 6, 9, …, 3(3t+2)} — N = 6 with k = 12 (two orbits of
six discs) for EVERY t; D = 54, 117, 180, 243, 306, …; the bottom star is the
rigid (2,3), V₂ = 1 Davenport–Stothers pair p_g = π³ − π, p_f = π² − 2/3
(STAR-ABC, promoted). The global interpolation conditions (delta 17(l),
promoted): moments M_r = Σ_i H_i τ_i^r/D_i with M_0 = … = M_{n−m−2} = 0 and
M_{n−m−1} = 1 (n − m − 1 = 3P − 1 homogeneous rows: 17, 38, 59, 80 at the four
members — growing linearly in t while the bottom packet stays k = 12, N = 6),
polynomiality (POLY), NO-RESIDUE; the driver
box/globalinterp-drivers-20260902/globalinterp.py emits the exact system for
a DECORATED skeleton (its (4.13)/(4.16) u₀ double-count is a known repair).
YOUR TASK:
(1) VERIFY the ray symbolically in t ((1)–(13) as implemented; the δ, A, q, u
    formulas; the orbit packets; d₄ = gcd(P, 2)) and by census emission at
    t = 0, 1, 2, 3; state which (n, m, M, V) row it is at each D and confirm
    D = 117's identification with branch-orbits v2's live row.
(2) DECORATE the members t = 0, 1, 2, 3 (D = 54, 117, 180, 243) with the
    k = 12 packet: two Galois orbits of six bottom discs (state the two
    orbits' lower data — identical here — and their two independent
    integration constants), the unique D₂ with all ue major roots, the
    minor block of NONPROPER-COUNT e(K − ΣV₂) roots, the rigid (2,3) star at
    each bottom disc, the tame exponent support and outer/inner sharing;
    EMIT with globalinterp.py the associated-graded moment matrix on the
    first bottom-separation page (the first z-orders at which (DEG) rows are
    non-vacuous) and, if affordable, to the D₂ junction; report per member
    (unknowns, equations, exact rank over Q or three good primes with
    rational reconstruction, cokernel), the minimum-weight (tropical) bases
    from the tree valuations, and whether the rank defect GROWS with t, is
    constant, or is repaired by the non-proper block (Schur complement
    separately). Also run the single-orbit packet k = 6 (N = 3 — below the
    frontier, a negative-control geometry) for comparison.
(3) READING: is there a stable minor / left-kernel functional across t whose
    valuation and leading coefficient can be conjectured in closed form (the
    valuated-MDS defect)? State the conjectured cofinal obstruction as a
    theorem to prove, or name the non-proper interface the counterexample
    lane needs. Compare with the D = 105 group-A member of Sol's ray
    (k = 18, N = 9) if the d105-rank-gate numbers are on disk (do NOT read
    that lane's report if it is still running: check its .run.v2 for
    final_status first).
Controls: (y, x + y^k) must pass at the same page; y² − x² − x must fail at
t-order 1; a partial-orbit decoration must be REFUSED. Discipline:
PROVED-HERE/UNREVIEWED; bounded quantity + cheapest test of every OPEN;
desk-scale CAS (< 30 min one core, < 6 GB; stop at the largest t that fits);
no ledger edits; no jc2-lean; do not read ideation-20260903T1015Z-* files or
other running lanes' reports. Drivers to box/a2six-drivers-20260903/.
Report: xmodel/a2six-ray-moment-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 25-40KB; 150 minutes.
charged_input=xmodel/n6-family-review-grok46-20260903.md
charged_input=xmodel/global-interpolation-sol56-20260902.md
charged_input=xmodel/global-interpolation-review-grok46-20260903.md
charged_input=box/globalinterp-drivers-20260902/globalinterp.py
charged_input=xmodel/branch-orbits-v2-grok46-20260903.md
charged_input=xmodel/branch-orbits-v2-review-gpt55-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=xmodel/census-rebase-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
982c75da179e263e109d0bf6ba0e8b13e591225c80d0111d24ba32b61be67896  {{LANE_INPUTS}}/n6-family-review-grok46-20260903.md
20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6  {{LANE_INPUTS}}/global-interpolation-sol56-20260902.md
f9959743d2f2169471179ccf56a44441190ddfe378a80a69635e3fcabacab381  {{LANE_INPUTS}}/global-interpolation-review-grok46-20260903.md
49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588  {{LANE_INPUTS}}/globalinterp.py
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  {{LANE_INPUTS}}/branch-orbits-v2-grok46-20260903.md
c61bb15528b25587578ac10101cb18267e83150fa6ea541e250f606e648d5418  {{LANE_INPUTS}}/branch-orbits-v2-review-gpt55-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
```
