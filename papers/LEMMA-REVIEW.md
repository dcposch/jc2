# Adversarial review of LEMMA.md (2026-08-03)

Charge: break the −1 lemma document on five fronts. Verdicts: CONFIRMED
(claim survives attack) / REFUTED / WEAKENED. All reviewer code was written
from scratch where independence is claimed (own hull/lattice/det-formula
equations, own substitution engine, own seed); the repo pipeline was used
only to *record* the chain. Scripts: /tmp/rev_geom.py, /tmp/rev_chain.py,
/tmp/rev_extra_case.py; logs /tmp/rev_{open_run1,open_run2,reg_run1,swap,mini}.log.
Environment: CPython 3.14.6, this machine, 2026-08-03.

## Front 1 — Reproduction. Verdict: CONFIRMED

- `python3 cases/eq3_chain.py open_8_28_c2`: cascade "reduced", 3 zeroed
  (b1, b2, a3), 41 elims; census after cascade+chart: **51/92 identically
  zero, 40 polynomial, constants = [(3, (2,0), −1)]** — eq #3 the unique
  constant, exactly as claimed. Chart pivot for b3: src = original key (3,6),
  coeff = (−1/5)·a2²·a6·ia1², |rest| = 0; the 10 events touching that source
  match LEMMA §2.3 verbatim.
- `reg_9_24_c3`: **38/69 identically zero, 31 polynomial, constants = []**;
  vertex equation is index 0, consumed by the chart as the definition
  b1 := −1/a1 (coeff = −a1, |rest| = 1); b2 = Q(1,1) drops out of every
  equation (free). Exactly as claimed.
- Nondeterminism: two runs under different PYTHONHASHSEED produce
  byte-identical logs. Instrumented full candidate scan at every pivot step:
  **zero ties** in the entire cascade, and zero ties in both chart-pivot
  selections — the chain is canonical for the (level, −size) heuristic, not
  an accident of tie-breaking.
- Minor erratum: §2.2 "Three M2 zeroings interleave" is wrong as written.
  There are 3 zeroings total: b1, b2 strictly *before* any elimination
  (as §2.1 itself says) and a3 strictly *after* the last (41st) elimination.
  Nothing interleaves. Content (sources, forced vars) is correct.

## Front 2 — Geometry claims. Verdict: CONFIRMED

Independent recomputation (own monotone-chain hull, own half-plane lattice
enumeration, own det formula; /tmp/rev_geom.py):

- Minkowski hull of N(P)+N(Q) = {(0,0), (1,0), (3,1), (20,35), (20,40)} —
  matches; **(3,1) is a vertex**; edge (3,1)→(20,35) = 17·(1,2) =
  7 P-steps + 10 Q-steps as claimed.
- (3,1) has **exactly one** decomposition over the full lattice-point sets
  (not just corners): (1,0)+(2,1), det = 1. Hence eq at key (2,0) is
  a1·b3 − 1 (verified against the generated equation).
- Bracket support: 92 keys, sorted order begins (1,0),(1,1),(1,2),(2,0),
  (2,1); **key (2,0) is index 3**. reg: 69 keys, rhs key (1,0) is index 0.
- Strips: with w = 2i−j (open) resp. 3i−j (reg): P occupies w ∈ {0,1,2},
  Q w ∈ {0,1,2,3} in *both* families; all w=0 points of both polygons lie on
  the line through the origin of direction d, both families. w(x²) = 4 =
  w_max(P)+w_max(Q)−1; the w_key = −1 stratum has **0** surviving
  (det ≠ 0) pairs, i.e. vanishes identically. All as claimed.
- Bonus: all 92 original equations rebuilt from the det formula
  coeff = Σ det(p,q)·a_p·b_q match SystemA's bracket-generated equations
  term-for-term — the generator itself is corroborated for this case.
- Confound audit for Front 4: strip widths are (2,3) in BOTH families —
  width is NOT a confound. fix_ones are structurally identical (far top
  corners; torus det ≠ 0 both). The live confound is k (2 vs 1) with
  (q0)_x (2 vs 1) — see Front 4.

## Front 3 — Soundness of the chain. Verdict: CONFIRMED

Trust model: only the *recorded* (v, g) events are taken from the repo; all
checking is fresh code (/tmp/rev_chain.py).

- Legitimacy of all 44 events: each M2 zeroing's equation is a single
  monomial with nonzero constant and all cofactors unit variables (zero(b1)
  from 1·a1·b1 at key (1,0); zero(b2) from 2·a1·b2 at key (1,1); zero(a3)
  unit-cofactor form of key (2,4)). Each of the 41 elim pivots: the variable
  occurs in exactly one monomial, to the first power, all cofactors units,
  constant ≠ 0; **my independently recomputed substitute g equals the
  recorded g in all 41 cases**.
- Pivot-constant interpretation (§2.2): for every a1-pivot elimination the
  constant equals det((1,0), q) = q_y (checked b4..b14: 2,3,4,3,4,5,6,5,6,7,8),
  and the far pivots match det((8,16), q) / corner cofactors — "unit corner
  coefficient times a nonzero lattice determinant" holds.
- The 10 events touching key (3,6) are exactly: zero b1, zero b2, elim
  b10, b9, b8, b7, elim b6, b5, b4, zero a3 (my own replay, my own
  equations). Reduced form is **exactly** {a2²·a6·ia1²·b3 ↦ −1/5} — the
  claimed constant −1/5 and exponents (a2², a6¹, ia1², b3¹) verified by my
  own substitution engine.
- eq #3 is touched by **no** cascade event and equals a1·b3 − 1 at
  cascade end; the chart pivot for b3 has empty rest, so b3 := 0 and eq #3
  reduces to the constant −1. My independent full census over my own 92
  originals: 51 zero / 40 polynomial / unique constant −1 at index 3, key
  (2,0) — identical to the repo's.
- Numeric audit at 3 fresh random rational points, reviewer seed 20260803
  (ghost back-substitution through the recorded chain in reverse):
  eq(3,6) evaluates to (−1/5)·a2²·a6·b3/a1² exactly at all 3 points; all 46
  cascade-stage zeros vanish; replayed form == direct evaluation for all 92
  equations at all 3 points. 3/3 fully consistent.
- One precision the doc should state: on the chart, the adjoined relation
  b3·ib3 − 1 *also* reduces to −1 (verified: the real two_chart leaf
  contains two literal −1 generators). "eq #3 is the unique constant" is
  true **among the 92 originals**; the −1 generator in
  systems/chartG_culprit.sing is equally attributable to the unit relation.
  This does not affect soundness — both transcribe "b3 must be a unit yet
  is forced to 0".

## Front 4 — The discrimination argument. Verdict: WEAKENED
(sharpness claim as stated is REFUTED; the mechanism survives in
symmetrized form)

1. **The confound is intrinsic, not separable.** Enumeration of hypothesis
   (i): p0+q0 = (k+1,1) with nonnegative corners and det(p0,q0) = ±1 admits
   exactly two splits for every k: {p0,q0} = {(1,0),(k,1)} in either order.
   Consequences: (a) k = 1 forces (p0)_x = (q0)_x = 1 — the test cell
   "(q0)_x = 2 with k = 1" demanded by a clean 2×2 design is **geometrically
   empty** under (i); (b) k ≥ 2 ⟺ a gap column exists on exactly one side.
   So "(q0)_x ≥ 2" and "k ≥ 2" are the *same condition up to the P/Q
   labeling* — the doc's presentation of (q0)_x as the discriminating
   variable (rather than k, or the symmetric gap condition) is unfalsifiable
   within Q-gap orientations.
2. **The realizable separating family refutes the Q-centric statement.**
   swap_8_28_c2 := open case with polygons swapped (P = hull{(0,0),(2,1),
   (12,21),(12,24)}, Q = hull{(0,0),(1,0),(8,14),(8,16)}, rhs x², fix
   P(12,24), Q(8,16); this is the image of the open family under
   (P,Q) ↦ (Q,−P), hence has identical solvability). Hypothesis (i) holds
   (unique decomposition (2,1)+(1,0), det = −1, (3,1) a Minkowski vertex);
   **(q0)_x = 1**, so LEMMA's (ii) FAILS as stated. Pipeline result
   (/tmp/rev_swap.log): the collapse **still fires** — census 33/92 zero,
   58 polynomial, unique constant −1 at key (2,0); the P-side gap column
   (a at (1,1),(1,2)) is M2-killed by the sub-vertex keys, the chart pivots
   b1 = b_{q0} := 0 from reduced key (3,6) with coeff (−6)·a4·a10·ia3, and
   the vertex equation −a3·b1 − 1 → −1. So "(q0)_x = 1 ⇒ no gap ⇒ vertex
   equation is a definition, not a constraint" (§4 verdict paragraph) is
   **false in general**: it holds for reg only because there the gap is
   absent on *both* sides. The corrected discriminator is the symmetric gap
   condition max((p0)_x, (q0)_x) ≥ 2, equivalently k ≥ 2 under (i); with
   that restatement, open/swap vs reg discrimination survives.
3. **Localization corroborated.** mini_gap (same corner data as open, strips
   shortened to x ≤ 4 / x ≤ 6, fix P(4,8), Q(6,12)): the collapse
   reproduces **exactly** — the same 10 events on key (3,6), the same
   reduced coefficient (−1/5)·a2²·a6·ia1², census 29/42 zero, unique
   constant −1 at key (2,0) (/tmp/rev_mini.log). The mechanism is genuinely
   local to the near-origin block, independent of strip length — good news
   for deriving (iii), and evidence the surplus count depends only on the
   O(1) corner data, not on the "specific strip widths" hedge in §5.

## Front 5 — Denominator hygiene. Verdict: CONFIRMED

- Recorded elim pivot constants are exactly the claimed set
  {−8,−6,−4,−2} ∪ {2,…,16} ∪ {18,20,22}.
- Full sweep (fresh code): every constant used by any move (M2 coefficients
  1 and 2 and the a3-forcing unit form, all 41 elim pivot constants, both
  chart pivot coefficients incl. −1/5) and every denominator of every
  coefficient in every recorded substitute g and in every intermediate state
  of the replay of all 92 equations through cascade+chart. Primes occurring:
  **{2,3,5,7,11,13} exactly** — the claimed set is not merely a conservative
  superset, it is sharp. The F_p validity claim (p ∉ {2,3,5,7,11,13})
  stands.

## Overall verdict

**The vertex-gap mechanism stands.** The open_8_28_c2 derivation is
reproduced deterministically, re-derived symbolically with independent code
and equations, confirmed numerically at fresh points, and its geometry is
correct in every checked particular; it is robust to shortening the strips
and even fires in the swapped orientation. Nothing false was found in
sections 1–3; section 4's *sharpness* claim is the one broken piece.

**Single weakest claim:** §4's discrimination verdict — "the discriminating
hypothesis is sharp: … reg has (q0)_x = 1 (no gap ⇒ vertex equation is a
definition, not a constraint)". Refuted as stated by the swap family
((q0)_x = 1, collapse anyway); (ii) must be symmetrized to
max((p0)_x,(q0)_x) ≥ 2 (⟺ k ≥ 2 under (i)), and the doc should say
plainly that under (i) the gap condition and k ≥ 2 are inseparable, so no
family can ever isolate "(q0)_x ≥ 2" from "k = 2". (Runner-up: condition
(iii) is still verified-by-elimination, not polygonal — acknowledged in §5,
and the mini-family result shows it is at least strip-length independent.)

**Paper readiness:** the case-specific −1 lemma for open_8_28_c2 (LEMMA §§1–3
= the AUDIT claim-7 discharge) is paper-grade after minor errata (the
"three zeroings interleave" sentence; the b3·ib3−1 → −1 remark; the §5
sign/index caveat is already honest). The **candidate general lemma (§4) is
NOT ready**: it needs (a) the symmetric restatement of (ii) forced by the
swap counterexample, and (b) the surplus-condition (iii) derived from corner
data before any general statement — do the surplus derivation first; the
mini-family localization result indicates it is a finite, strip-length-free
computation on the near-origin block.
