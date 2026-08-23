# MONDELLO-CHECK: arXiv:2608.02634 verification

Status: DONE (2026-08-06). VERIFIED; out-of-regime; char-2 failure = even det pivots {2,4,6}.

## 1. Paper claim (extracted)
Fetched abs page 2026-08-06; matches RECON.md Delta item 9.
- k = F̄₂ (works over F₂). P = x + x²y + x⁴ + x⁶y²; Q = y + x⁵ + x⁶y + x⁷y² + x⁸y³.
- Claim: det J(P,Q) = 1; the three distinct points (0,1), (1,0), (1,1) share one image.
- Claim: [k(x,y):k(P,Q)] = 3, separable (3 prime to char 2); F not an automorphism.
- Derived from a coordinate-permuted 3-variable char-2 map of Huq-Kuruvilla.

## 2. Independent verification (char 2)
Script: `cases/mondello_verify.py` (lib/jc.py exact-Z bracket reduced mod 2 + independent GF(2^m) bitmask evaluator). All checks PASS:
- [P,Q] over Z has 8 terms, all even except constant 1; mod 2 exactly 1. (Hand check: P_x≡1, P_y≡x², Q_x≡x⁴+x⁶y², Q_y≡1+x⁶+x⁸y²; 1·(1+x⁶+x⁸y²) − x²(x⁴+x⁶y²) = 1.)
- (0,1),(1,0),(1,1) all map to (0,1) over F₂: collision confirmed.
- Fiber histograms over F_{2^m}, m=4,6,8: all fibers ≤ 3 points; size-3 fibers dominate (e.g. m=8: 10929 fibers of size 3, 32749 of size 1); fiber over (0,1) has exactly 3 points ⇒ generic degree 3.
- Separability: [P,Q]=1≠0 ⇒ dP∧dQ=dx∧dy≠0 ⇒ separating transcendence basis ⇒ separable (also 3 odd = prime to 2).

**VERDICT: VERIFIED.** Genuine char-2 plane Keller pair, det J = 1, non-injective, degree-3 separable.

## 3. Newton polygons vs strip-pair regime
Structure (char 2, u := 1+xy): P = xu + (x²u)², Q = y + x⁵u³ — a genuine **strip pair along common primitive d = (1,1)** (transversal w' := i−j; P on lines w' ∈ {1,4}, Q on w' ∈ {−1,5}; hulls: N(P) = hull{(1,0),(4,0),(6,2),(2,1)}, N(Q) = hull{(0,1),(5,0),(8,3)}; parallel (1,1)-edges {(1,0),(2,1)} ∥ {(4,0)..(6,2)} in P, {(5,0)..(8,3)} in Q).
- **Vertex normalization (i): HOLDS verbatim.** rhs monomial 1 at Minkowski vertex (1,1) = (1,0)+(0,1), unique decomposition, det = +1, corners saturated (vertex eq a·b = 1).
- **Gap condition (ii): FAILS.** In SURPLUS.md normalization this is the cell (k,d2) = (0,1): rhs = x⁰, {p₀,q₀} = {(1,0),(0,1)} so max((p₀)_x,(q₀)_x) = 1 < 2; no gap columns. Also d2 = 1 = the scope-map row with "no extra keys, no obstruction", and the top edges are NOT through the origin (Q straddles the direction line: offsets −1, 5).
- Verdict: **NEAR our setting (strip pair + exact condition (i)) but strictly OUTSIDE the proved (k,d2) = (2,2) obstruction cell** — so no tension with our char-0 theorems even before characteristic considerations.

## 4. Char-2 failure point in our machinery
Script: `cases/mondello_collapse.py` (machinery-style level-ordered M2/unit-pivot elimination over Q, every pivot logged; modes: exact support, and `hull` = generic member of his polygons).

**Over Q the machinery EMPTIES his data at the M2/gap-kill stage** (pre-block, LEMMA.md §2 step 1 / SURPLUS.md GAP-KILL analogue). Sparse run: 13 keys; after vertex normalization (pivot det((1,0),(0,1)) = +1, odd), the sub-vertex single-monomial keys force a(2,1) = 0 [pivot **+2**], a(4,0) = 0 [pivot **+4**], a(6,2) = 0 [pivot **+6**], then b(7,2) = 0 [pivot **+2**], b(6,1) = b(8,3) = 0 (odd pivots 1, 3): full collapse to the elementary automorphism P = a1x, Q = b0y + b1x⁵. Hull run agrees: strip corners a(2,1), a(6,2) killed by pivots +2, +6; Q-corner b(8,3) then dies; residual = triangular x-axis family (automorphisms). So **no char-≠2 Keller pair realizes these Newton polygons** — his example must live where those pivots die.

**The exact failing constants: the even lattice-determinant pivots det(p, q₀) = det((2,1),(0,1)) = 2, det((4,0),(0,1)) = 4, det((6,2),(0,1)) = 6** (and det((1,0),(7,2)) = 2 on the b(7,2) key). Mod 2, 10 of the 12 non-vertex bracket keys of his support are IDENTICALLY zero (every contributing det even; u-basis law [x^a u^b, x^c u^d] = (ad−bc)x^{a+c}u^{b+d−1} gives dets det((1,1),(4,2)) = −2, det((1,1),(5,3)) = −2, det((4,2),(5,3)) = 2, plus d((x²u)²) = 2(x²u)d(x²u) ≡ 0: the Frobenius-square strip is differentially invisible); the two surviving keys are cancellation identities his all-ones coefficients satisfy. The M2 stage never fires; the strips live.

Same prime in our own theorems: LEMMA.md §2 step 1's M2 key reads 2·a1·b2 = 0, and the SURPLUS.md (2,2) block chain divides by pivots {2,3,4,5,6} (first even: b4 = a2b3/(**2**a1) at key (3,2)) with char-exclusion set {2,3,5} declared sharp. Mondello's example is an existence proof that excluding char 2 there is NECESSARY, and it fails our machinery in exactly the predicted way: an explicit division by 2 in the pivot constants, nothing else (the −1/5 and R_{k,d2} binomials are not reached at his (k,d2) = (0,1) cell).

## 5. Suggested Paper 1 remark
> **Remark.** The characteristic restrictions in our results are not an artifact of the method. Mondello's plane Keller pair P = x + x²y + x⁴ + x⁶y², Q = y + x⁵ + x⁶y + x⁷y² + x⁸y³ over F₂ (arXiv:2608.02634) has Jacobian determinant 1, sends the three distinct points (0,1), (1,0), (1,1) to a common image, and generates a degree 3 separable field extension, so even the separable Jacobian conjecture fails in characteristic two. Its Newton polygons form a strip pair along the direction (1,1) satisfying our vertex normalization, and in any characteristic other than two our near-origin eliminations, whose pivot constants at this polygon data are the lattice determinants 2, 4, and 6, force the strip corners to vanish and reduce any such pair to an elementary automorphism. In characteristic two every one of these determinants vanishes, the corresponding bracket equations become identically zero, and the strips survive; this is precisely the escape that Mondello's example exploits.

## Verdict
- **VERIFIED** (bracket, collisions, degree, separability — independent exact computation).
- **Not in-regime**: strip pair along d=(1,1) with vertex normalization (i) exact, but cell (k,d2) = (0,1) — outside the proved (2,2) obstruction cell (no gap columns, d2=1, top edges off origin). No contradiction with our char-0 theorems.
- **Char-2 failure point**: the even M2/gap-kill pivot constants det((2,1),(0,1)) = 2, det((4,0),(0,1)) = 4, det((6,2),(0,1)) = 6 (and det((1,0),(7,2)) = 2); mod 2 these keys are identically zero, so the collapse that over Q reduces his polygons to an elementary automorphism never starts. Matches the 2 in our own pivot sets {2,3,4,5,6} / {2,3,5,7,11,13}: char-2 exclusion is necessary.
- Artifacts: `cases/mondello_verify.py`, `cases/mondello_collapse.py` (both re-runnable, exact arithmetic).
