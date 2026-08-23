# The −1 lemma for open_8_28_c2 chartG

Discharges the AUDIT.md claim-7 / notes.md TODO: identify equation #3,
reconstruct its substitution chain, interpret it, attempt a generalization.
System: `SystemA("open_8_28_c2", cornersP, cornersQ, x², nonvanish="nonorigin",
fix_ones=[("P",(8,16)),("Q",(12,24))])`; `Cascade3(level_dir=(2,1))`; then
`two_chart`. Re-runnable analysis: cases/eq3_anatomy.py, cases/eq3_chain.py
(the latter replays the full pipeline with per-equation provenance tracking
and reproduces the AUDIT claim-7 census **symbolically**, not just at points).

## 1. Which bracket coefficient equation #3 is

Equations are the coefficients of [P,Q] − x², ordered by sorted bracket
support; the support begins (verified):

    index:   0      1      2      3      4    ...      (92 keys total)
    key  : (1,0)  (1,1)  (1,2)  (2,0)  (2,1) ...

**Equation #3 is the coefficient of the right-hand-side monomial x² itself**
(key (2,0)). Since coeff_{(i,j)}[P,Q] = Σ_{p+q=(i+1,j+1)} det(p,q)·a_p·b_q,
eq #3 lives at Minkowski point (3,1). Geometry (P = hull{(0,0),(1,0),(8,14),
(8,16)}, Q = hull{(0,0),(2,1),(12,21),(12,24)}):

- Both polygons are narrow strips along the direction d = (1,2). With
  w := 2i−j: P occupies w ∈ {0,1,2} (w=0 top edge (0,0)–(8,16), w=2 bottom
  edge (1,0)–(8,14)); Q occupies w ∈ {0,1,2,3} (w=0 top edge (0,0)–(12,24),
  w=3 bottom edge (2,1)–(12,21)). Both top edges lie on lines through the
  origin, so the extreme stratum w_key = −1 of the bracket vanishes
  identically (det of proportional points).
- N(P)+N(Q) = hull{(0,0),(1,0),(3,1),(20,35),(20,40)}. **(3,1) is a vertex**
  — the lower endpoint of the long Minkowski edge (3,1)→(20,35) of direction
  (1,2) (17 primitive steps = the concatenation of the two parallel bottom
  edges: 7 steps from P, 10 from Q).
- (3,1) has the **unique decomposition** (1,0)+(2,1) = (bottom corner of P) +
  (bottom corner of Q), with det((1,0),(2,1)) = 1. Both are saturated
  corners: a1 := coeff_P(1,0), b3 := coeff_Q(2,1) are unit variables.

Hence

    eq #3  =  a1·b3 − 1        (two terms; the −1 is the rhs −x²)

i.e. eq #3 is the **vertex normalization**: x² must be attained at the bottom
vertex of the parallel-edge tower, forcing a1·b3 = 1 (both bottom corners
nonzero, product 1). In the w-grading, x² has w = 4 = w_max(P)+w_max(Q)−1:
it is reachable only by bottom-edge × bottom-edge pairs, and at the vertex
only by the corner pair.

## 2. The substitution chain

Structural fact: eq #3 contains only unit variables (a1, b3), so Cascade3
never substitutes into it and never pops it — **eq #3 passes through the
entire cascade verbatim**. The whole collapse is carried by ONE other
equation. Verified chain (cases/eq3_chain.py output):

1. **Immediate M2 zeroing (before any elimination).** The sub-vertex keys
   (1,0), (1,1) (Minkowski column 2, strictly between the y-axis and the
   vertex column) read a1·b1 = 0 and 2·a1·b2 = 0 with a1 a unit
   ⇒ **b1 = coeff_Q(1,1) := 0, b2 = coeff_Q(1,2) := 0** — Q's entire column
   x=1 (the "gap column" wedged between origin and Q's bottom corner (2,1))
   is annihilated. Key (1,2) then vanishes identically.
2. **Level-(2,1) cascade, 41 unit-pivot eliminations,** consuming Q's columns
   from x=12 down to x=2 (all non-corner b's). Every pivot coefficient is a
   unit corner coefficient times a nonzero lattice determinant: the far
   eliminations pivot on the top corners P(8,16)=1 / P(8,14) (source keys
   (15..19,·)); the rest pivot on a1 via the equation at Minkowski point
   (1,0)+q (source key q−(0,1)), pivot constant det((1,0),q) ≠ 0.
   Three M2 zeroings interleave; the relevant one: key (2,4) reduces to
   (unit)·a3 ⇒ **a3 = coeff_P(1,2) := 0** (P's top-edge point in column 1).
3. **The culprit equation: original key (3,6)** (Minkowski point (4,7) =
   (1,1)+3·(1,2), on the second-highest stratum w_key = 0; column = vertex
   column + 1). Originally
   3a2·b10 − a3·b9 + 2a5·b6 − 2a6·b5 + a8·b2 − 3a9·b1, it is touched by
   exactly 10 events — zero(b1), zero(b2), elim b10(3,6), b9(3,5), b8(3,4),
   b7(3,3) [Q column 3, sources keys (3,2)..(3,5)], elim b6(2,4), b5(2,3),
   b4(2,2) [Q column 2, sources keys (2,1)..(2,3)], zero(a3) — after which it
   is the single monomial

        (−1/5)·a2²·a6·ia1²·b3  = 0        (a2 = P(1,1), a6 = P(2,4))

   All eliminated b's were expressed back in P-data; the surviving factor is
   b3 times the non-unit a-monomial a2²a6.
4. **two_chart.** For b3 this equation is the best pivot (|coeff|=1,
   |rest|=0): on the generic chart the coefficient is inverted and
   **b3 := 0**. (The b43-inversion is vacuous — its pivot is the adjoined
   b43·ib43 = 1.) Substituting b3 = 0 into the untouched vertex equation:

        eq #3  =  a1·0 − 1  =  **−1**.

   The −1 is literally the transcription of −x²; no other arithmetic touches
   it. Full symbolic census after cascade+chart: 51/92 originals ≡ 0, 40
   remain polynomial, and **eq #3 is the unique constant** — the exact
   symbolic upgrade of AUDIT claim 7's 6-point numeric audit.

Equivalent ideal statement (chart-free): the derivation shows
**unit·a2²·a6·b3 ∈ I(core)**; since the vertex equation makes b3 a unit,
a2²·a6 ∈ I(core) — the core variety lies in {a2=0} ∪ {a6=0}, which is
precisely the cCa2/cCa6 complement split, and the generic chart (a2, a6
inverted) is empty. Denominator hygiene: the chain's pivot constants are
{−8,−6,−4,−2,2,3,…,16,18,20,22} (lattice determinants det(corner, q)); the
final coefficient only carries 1/5 — so the derivation is valid over any
field in which the pivot constants are invertible: all char-0 fields, and
all F_p with p ∉ {2,3,5,7,11,13} (conservative superset of the primes
dividing any pivot constant).

## 3. Valuation interpretation

The level function ℓ = 2i+j orders lattice points along the strips; the
cascade is exactly the classical tower argument "Q is determined by P":
solving the bracket coefficients from the top of the filtration downward
expresses each Q-coefficient at level ℓ through P-data, pivoting on the two
invertible corner coefficients (the fixed top corners, then the bottom
corner a1). The GGV-style reading of the collapse:

- The vertex equation at the Minkowski vertex p₀+q₀ = (1,0)+(2,1) is the
  **corner normalization**: for [P,Q] = x², the valuation of x² selects the
  bottom vertex of the (1,2)-tower, forcing a_{p₀} b_{q₀} = 1, in particular
  b_{q₀} ≠ 0.
- Because Q's bottom corner q₀ = (2,1) does not lie in the first support
  column, there are bracket coefficients **below/left of the vertex**
  (Minkowski column 2 = keys (1,·)) which must vanish but involve only
  a1·(Q-gap column); invertibility of a1 kills the gap column b1, b2.
- With the gap dead, the near-origin block of tower relations becomes
  **overdetermined by one**: the block keys (2,0)..(2,4), (3,2)..(3,6) are
  the vertex equation plus 9 tower relations for 8 eliminable unknowns
  (b4..b10 and a3); the surplus relation — the
  top-stratum key (3,6), the "would-be tower relation" that in a consistent
  tower would define the next Q-coefficient — has no free Q-coefficient left
  to define. Back-substitution turns it into (unit)·a2²·a6·b_{q₀} = 0: the
  tower forces the bottom corner of Q to vanish, **inconsistent with the
  corner normalization**. So yes: eq #3's collapse is a recognizable
  principle — a corner/tower inconsistency at the parallel-edge direction,
  localized entirely in the O(1) neighbourhood of the origin end of the
  strips.

## 4. Candidate general lemma, and the regression test

**Candidate Lemma (vertex–gap obstruction).** Let (P,Q) be a reduced pair
with [P,Q] = x^k, N(P) and N(Q) lattice strips of widths ≤ w_P, w_Q along a
common primitive direction d, top edges through the origin parallel to d,
bottom edges E_P from p₀, E_Q from q₀ (corners saturated). Assume:

  (i) *(vertex normalization)* x^k sits at the Minkowski vertex p₀+q₀ with
      unique decomposition p₀+q₀ and det(p₀,q₀) = ±1, giving the vertex
      equation a_{p₀} b_{q₀} = ±1;
  (ii) *(gap condition)* N(Q) has support columns strictly between the
      y-axis and x = (q₀)_x — equivalently (q₀)_x ≥ 2 — so the bracket has
      sub-vertex coefficients, and each such coefficient is a1-times-linear
      in the gap column (automatic when (p₀)_x = 1), forcing the gap
      column to vanish;
  (iii) *(surplus condition)* after the gap dies, the level-ordered
      elimination of the near-origin block (Q-columns (q₀)_x … (q₀)_x+1,
      P-columns 1 … 2) has one more vanishing bracket coefficient than
      eliminable unknowns; the surplus is the block's top-stratum key
      (here Minkowski point (1,1)+3d) and its back-substituted form is
      (unit)·(a-monomial)·b_{q₀}.

Then the bracket coefficient **at the rhs monomial itself** (position rule:
the key x^k, i.e. the Minkowski vertex p₀+q₀) reduces on the chart where the
surplus a-monomial is inverted to the nonzero constant −1, hence the generic
stratum is empty, and the whole variety lies in the vanishing locus of the
surplus a-monomial's non-unit support.

**Test against the solved family reg_9_24_c3** (P = hull{(0,0),(1,1),(6,16),
(6,18)}, Q = hull{(0,0),(1,0),(9,24),(9,27)}, [P,Q] = x; strips along
d = (1,3); verified by cases/eq3_chain.py reg_9_24_c3):

- (i) HOLDS there too: x sits at the Minkowski vertex (2,1) = (1,1)+(1,0),
  unique decomposition, det = −1; the vertex equation −a1·b1 − 1 = 0 is
  equation index **0**. So (i) alone does not discriminate.
- (ii) **FAILS**: Q's bottom corner is q₀ = (1,0), (q₀)_x = 1 — there is no
  gap column and no sub-vertex bracket coefficient (the support starts AT
  the vertex key). Nothing forces near-origin Q-coefficients to vanish.
- (iii) fails with it: the near-origin block is exactly balanced /
  underdetermined — the cascade leaves b2 = coeff_Q(1,1) completely free
  (it drops out of every equation), no surplus relation pins b1, and in
  two_chart the vertex equation itself is consumed as the *definition*
  b1 := −1/a1 (chart pivot source = key (1,0), |rest|=1). Symbolic census:
  38/69 equations ≡ 0, **no equation reduces to a constant** — matching the
  known fact that this chartG needed genuine F4 work.

**Verdict: the candidate lemma DISCRIMINATES the two families**, and the
discriminating hypothesis is sharp in the computed pair: open_8_28_c2 has
(q₀)_x = 2 (gap column {(1,1),(1,2)} killed ⇒ overdetermination ⇒ b3 pinned
to 0 against the vertex normalization), while reg_9_24_c3 has (q₀)_x = 1
(no gap ⇒ vertex equation is a definition, not a constraint).

## 5. Honest assessment

- What is proved here (re-runnably): for open_8_28_c2, −1 ∈ ideal(chartG)
  via an explicit 10-event linear substitution chain, entirely inside the
  near-origin columns; equivalently a2²a6 ∈ I(core). This upgrades AUDIT
  claim 7 from numerically-audited to symbolically re-derived
  (cases/eq3_chain.py is the committed audit script the TODO asked for).
- The candidate lemma's conditions (i)+(ii) are cheap, purely polygonal,
  and discriminate the two families examined. Condition (iii) is NOT yet a
  polygonal criterion: it is verified by running the elimination, not read
  off the corners. The counting that produces "surplus = 1" here uses the
  specific strip widths (3 and 4), (p₀)_x = 1, and (q₀)_x = 2; a
  paper-grade lemma would need to derive (iii) from these data (plausible —
  the block is O(1)-sized and explicit — but not done here).
- Generality is untested beyond the two families. For open_8_28_c1
  (pentagon polygons): condition (i) and the nonempty gap column hold
  verbatim (same bottom corners p₀=(1,0), q₀=(2,1), same vertex (3,1) with
  unique decomposition), but the y-axis support ((0,1)..(0,8) in P,
  (0,1)..(0,12) in Q) breaks the *mechanism* of (ii): the sub-vertex
  coefficients (1,j) also contain det((0,a),(2,b)) = −2a terms mixing
  P-column-0 with Q-column-2, so the gap column is not forced to zero by
  M2 alone, and whether an analogous collapse occurs is open (the c1
  analysis run — `python3 cases/eq3_chain.py open_8_28_c1`, long-running —
  was stopped after ~15 min without completing its cascade; consistent
  with notes.md on c1's two_chart swell).
- Sign/index caveat: "equation #3" is ordering-dependent bookkeeping; the
  invariant statement is "the bracket coefficient at the rhs monomial /
  Minkowski vertex p₀+q₀". In reg_9_24_c3 the same coefficient is index 0.

## Post-review corrections (2026-08-03, per LEMMA-REVIEW.md)
- Erratum §2: the M2 zeroings interleave as 2 before / 1 after the
  eliminations (not "three interleave").
- §4 sharpness CORRECTED: condition (ii) must be symmetrized —
  max((p0)_x, (q0)_x) ≥ 2. The review showed (a) under (i), k=1 forces
  (q0)_x = 1, so the k-vs-gap confound is intrinsic (untestable cell), and
  (b) the swapped-polygon family (k=2, gap on the P side) ALSO collapses
  to −1 — the obstruction is side-symmetric.
- Localization confirmed: a short-strip toy family reproduces the identical
  10-event collapse, supporting an O(1)-block derivation of condition (iii).
- Status: §§1–3 paper-ready per review; remaining for paper grade:
  symmetric-(ii) restatement + surplus-condition derivation from polygon data.
