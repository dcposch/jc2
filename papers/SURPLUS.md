# SURPLUS: Deriving Condition (iii) — surplus = 1

## Phase 1: Computational validation

### Method

Script: `cases/surplus_count.py` (self-contained; no lib deps). Input: corners of
N(P), N(Q), k. Derived: primitive strip direction d=(1,d2) (top edges through
origin), widths w_P,w_Q, bottom corners p0,q0. Orientation normalized so the gap
side (bottom-corner x = max) is Q; if that requires swapping, noted (bracket sign
irrelevant to counts). Hypothesis (i) verified: p0+q0=(k+1,1), unique lattice
decomposition, |det(p0,q0)|=1.

Near-origin block := bracket keys in Minkowski columns k+1, k+2. Post-gap-kill
live pairs: P cols {1,2} x Q cols {k, k+1} (gap cols 1..k-1 of Q die first via
triangular a_{p0}-pivots on sub-vertex keys; verified structurally).

- n_keys: lattice count of block Minkowski points with >=1 live det!=0 pair,
  excluding the vertex key (k+1,1) (= rhs x^k) and identically-zero keys
  (all pairs det=0; includes the top stratum w=0).
- n_unknowns: ground truth from a tiny in-block symbolic cascade (M2 single-
  monomial zeroings + unit-cofactor eliminations, eager substitution): count of
  non-unit block coefficients zeroed or expressed. Gap-column variables excluded
  by construction. Units a_{p0}, b_{q0} invertible per (i).
- surplus := n_keys - n_unknowns = number of leftover equations; each leftover
  is classified: PINS-b_q0 (reduces to unit*(a-monomial)*b_{q0}, the
  obstruction), TRIVIAL (reduces to 0), or OTHER.
- Cross-check column: closed-form candidate n_keys = 2(w_P+w_Q)-1.

### Validation table

FINAL (depth-2 block = Minkowski cols k+1, k+2; run `python3
cases/surplus_count.py`). Leftover classes: PINS = reduces to
(unit)*(non-unit monomial)*b_q0 (the obstruction); TRIVIAL = reduces to 0.

| family       | k | d     | wP | wQ | gap? | n_keys | n_unk | surplus | leftover               | expected | verdict |
|--------------|---|-------|----|----|------|--------|-------|---------|------------------------|----------|---------|
| open_8_28_c2 | 2 | (1,2) | 2  | 3  | yes  | 9      | 8     | 1       | (4,7) PINS -1/5 a2^2a6 | 1        | MATCH   |
| swap_8_28_c2 | 2 | (1,2) | 2  | 3  | yes  | 9      | 8     | 1       | (4,7) PINS (same, normalized) | 1 | MATCH   |
| mini_gap     | 2 | (1,2) | 2  | 3  | yes  | 9      | 8     | 1       | (4,7) PINS (identical) | 1        | MATCH   |
| reg_9_24_c3  | 1 | (1,3) | 2  | 3  | no   | 9      | 8     | 1(raw)  | (3,8) TRIVIAL -> eff. 0| <=0      | MATCH*  |
| toy_k3 (new) | 3 | (1,2) | 2  | 5  | yes  | 13     | 12    | 1(raw)  | (5,9) TRIVIAL -> eff. 0| 1?       | BREAKS  |
| toy_w3 (new) | 2 | (1,3) | 3  | 5  | yes  | 15     | 11    | 4       | 4x OTHER, torus-EMPTY  | 1?       | BREAKS  |

The three known collapsing families reproduce LEMMA.md exactly: 9 forced keys,
8 eliminable (7 gap-side + 1 P-zeroed a(1,2)), surplus key (4,7), reduced form
(-1/5)*a(1,1)^2*a(2,4)*b_q0*a_p0^-2 — byte-identical incl. the 1/5.

### Notes per family

* MATCH* (reg): the raw count n_keys - n_unknowns equals 1 for reg TOO; the
  true discriminator is the leftover's CONTENT: reg's leftover (3,8) reduces
  to 0 (its P-side inputs a(1,2), a(1,3) are themselves M2-zeroed by the
  block), so the effective surplus (number of obstruction leftovers) is 0,
  matching "<= 0 for the solved shape". Condition (iii) must be stated as
  "the leftover reduces to (unit)*M*b_q0 with M nonzero", not as a bare count.
* toy_k3 (k=3, d2=2): gap condition holds, a(1,2) is still M2-forced, but the
  outer extra key (5,9) reduces IDENTICALLY to 0. Deeper blocks (D=3..5) add
  one leftover per column, all torus-SOLVABLE (numeric probe, 80 restarts):
  they merely constrain P; no empty-chart obstruction. Condition (iii) FAILS
  at k=3 even though (i)+(ii) hold: (iii) is genuinely independent.
* toy_w3 (k=2, d2=3, wP=3): no M2 ever fires (extra keys have >=2 monomials);
  2(wP-1)=4 leftovers, a 4-eqs/7-vars system among P-coefficients with NO
  torus point (numeric probe, stable D=2..5): an obstruction plausibly
  persists but NOT in the surplus=1 single-monomial form. wP=2 is load-bearing.

PHASE 1 DONE. Deliverable: table above + cases/surplus_count.py (self-checked
against LEMMA.md ground truth by assertion).

### Notes per family

## Phase 2: General counting argument

### Setup and symbolic enumeration

Standing hypotheses (LEMMA.md (i) + review-symmetrized (ii)), after the
normalization (P,Q) -> (Q,-P) if needed so the gap side is Q:

- strips along primitive d = (1,d2), d2 >= 1 (d1 = 1 assumed; d1 >= 2 gives
  sparse columns and is out of scope), top edges of both polygons on the line
  R*d through the origin; bottom corners saturated;
- (i): x^k at the Minkowski vertex p0+q0 = (k+1,1), unique det!=0
  decomposition, det(p0,q0) = +-1. By the review's enumeration this forces
  {p0,q0} = {(1,0),(k,1)}; normalized: p0 = (1,0), q0 = (k,1);
- (ii): k >= 2 (equivalently max((p0)_x,(q0)_x) >= 2);
- strip lengths: P contains columns 1,2 in full, Q contains columns k,k+1 in
  full (i.e. strips extend at least 2 resp. k+1 columns past the origin).

Derived data (not free parameters!): w(i,j) := d2*i - j >= 0, zero exactly on
the top edges; w_P = w(p0) = d2, w_Q = w(q0) = k*d2 - 1. Column x = c of P
resp. Q is the full ladder of d2*c+1 resp. lattice points between bottom and
top edge (columns are w-intervals [0,w_side], bijectively y = d2*c - w).
Units: a_{p0}, b_{q0} (vertex equation a_{p0} b_{q0} = +-1, hypothesis (i)).

GAP-KILL LEMMA. Q's columns 1..k-1 vanish on the variety. Proof: induction on
column g and, inside it, on level l = d2*x+y. The sub-vertex key at Minkowski
point p0 + (g,y) contains det(p0,(g,y))*a_{p0}*b_{(g,y)} = y*a_{p0}*b_{(g,y)}
with y >= 1 (gap points are above the bottom edge 0->q0); its other monomials
pair P col j >= 1 with Q gap points of strictly lower level or lower column,
already zero. So each key reduces to a single monomial with unit cofactor:
b_{(g,y)} = 0 (M2). No block key is consumed. QED

BLOCK. Minkowski columns k+1, k+2. Post-gap-kill the only live pairs landing
there are P cols {1,2} x Q cols {k,k+1} (anything else hits the origin column,
a gap column, or column sums outside {k+1,k+2}); conversely these pairs land
only there. The block is therefore SELF-CONTAINED: its equations involve
exactly the block variables, so counting can be done locally (this is the
localization the review's mini-family confirmed empirically).

### Key count

PROPOSITION A. n_keys = 2(w_P + w_Q) - 1, for every k >= 1, d2 >= 1.

Proof. Column x = k+1 of N(P)+N(Q) is the ladder y = 1..d2(k+1), i.e. strata
w = 0..w_P+w_Q (w = d2(k+1)-y; vertex (k+1,1) is the bottom stratum
w = w_P+w_Q). (a) A key of stratum w = 0 is identically zero: w(p)+w(q) = 0
with w >= 0 forces w(p) = w(q) = 0, so p,q are both on R*d and det(p,q) = 0.
(b) Every stratum 1 <= w <= w_P+w_Q is genuinely in the post-gap support:
for w >= w_P take the pair (p0, q), q in Q col k with w(q) = w - w_P (the
column is full), det(p0,q) = q_y >= 1; for 1 <= w <= w_P-1 take
p = (1, d2-w) in P col 1 and q = (k, k*d2) the top of Q col k, det = k*w != 0.
Distinct pairs contribute distinct monomials a_p b_q, so no cancellation.
Removing the vertex key leaves (w_P + w_Q) - 1 forced-vanishing keys.
Column x = k+2: same ladder argument (bottom of the column is (k+2, 1+d2) on
the long Minkowski edge, stratum w_P+w_Q; support witness for w >= w_P is
(p0, q), q in Q col k+1 full; for w <= w_P-1 use q = top of col k+1); no
vertex to remove: w_P + w_Q keys. Total 2(w_P+w_Q) - 1. QED
(Verified by the script on all 6 families and the 16-cell scan.)

### Unknown count

PROPOSITION B (gap-side eliminations). All 2w_Q + 1 non-corner coefficients
b_q, q in Q cols k, k+1, are unit-pivot eliminable, each from its own key
m = p0 + q; this consumes exactly the block keys of strata w in
[w_P, w_P+w_Q] (both columns, vertex excluded), leaving as remainder the
2(w_P - 1) "extra" keys of strata w in [1, w_P-1].

Proof. The key at m = p0 + q contains the monomial det(p0,q)*a_{p0}*b_q with
det(p0,q) = q_y >= 1 and unit cofactor a_{p0}; it is the only monomial of that
key containing b_q (the pair with second factor q is unique). q -> p0 + q is
injective, hits exactly strata w(m) = w_P + w(q) in [w_P, w_P+w_Q] in each
column, and misses only the vertex (q = q0). Triangularity: in any other
monomial (p',q') of the key p0+q one has l(p') > l(p0) (l = d2*x+y is
injective... l(p') = d2+j > d2 for p' = (1,j), j>=1, and l >= 2*d2 >= l(p0)+1
for p' in col 2), hence l(q') < l(q): eliminating in increasing level l(q) is
well-founded and each substitution only inserts already-defined or
lower-level variables. Count of consumed keys = count of eliminated b's =
2w_Q + 1; remainder n_keys - (2w_Q+1) = 2(w_P-1) keys, exactly the strata
w in [1, w_P-1] of the two block columns. QED

COROLLARY (raw count). n_keys - n_unknowns = 2(w_P - 1) - z, where z = number
of P-side coefficients zeroed by M2 events among the extra keys. The
CONTENT of the extra keys after back-substitution decides everything; it is
regime-dependent (Theorem below and scope map).

### Key count

### Unknown count

### Main count: n_keys − n_unknowns = 1

THEOREM (condition (iii) from polygon data, regime (k,d2) = (2,2)). Let (P,Q)
satisfy the setup with k = 2, d = (1,2) (hence w_P = 2, w_Q = 3, p0 = (1,0),
q0 = (2,1)), strips of ANY lengths containing the block columns. Then
n_keys = 9, n_unknowns = 8, surplus = 1; the surplus key is Minkowski (4,7),
and its back-substituted form is (-1/5)*a2^2*a6*b_{q0}*a_{p0}^{-2}, i.e.
(unit)*(a-monomial)*b_{q0}. With (i) this forces a2^2 a6 = 0: the chart
inverting {a2, a6} is empty. Valid over any field of char not in {2,3,5}.

Proof: explicit reduction of the 9 block keys (labels a1* = a(1,0),
a2 = a(1,1), a3 = a(1,2), a4 = a(2,2), a5 = a(2,3), a6 = a(2,4); b3* = b(2,1),
b4 = b(2,2), b5 = b(2,3), b6 = b(2,4), b7 = b(3,3), ..., b10 = b(3,6);
* = unit; all coefficients are lattice dets det(p,q)):

    (3,2)  2a1b4 - a2b3            => b4  = a2b3/(2a1)
    (3,3)  3a1b5 - 3a3b3           => b5  = a3b3/a1
    (3,4)  4a1b6 + a2b5 - 2a3b4    => b6  = -(a2a3-a2a3)b3/(4a1^2) = 0   [C1]
    (3,5)* 2a2b6 - a3b5            => -a3^2 b3/a1 = 0  => M2: a3 := 0
    (4,3)  3a1b7 - 2a4b3           => b7  = 2a4b3/(3a1)
    (4,4)  4a1b8 - 4a5b3           => b8  = a5b3/a1
    (4,5)  5a1b9 + a2b8 - 3a3b7 + 2a4b5 - 2a5b4 - 6a6b3
                                   => b9  = 6a6b3/(5a1)                  [C2]
    (4,6)  6a1b10 + 2a2b9 - 2a3b8 + 4a4b6 - 4a6b4
                                   => b10 = -a2a6b3/(15a1^2)
    (4,7)* 3a2b10 - a3b9 + 2a5b6 - 2a6b5
                                   => -(1/5) a2^2 a6 b3 a1^{-2}   SURPLUS

[C1], [C2] are the two exact cancellations that create the surplus: in (3,4),
substituting b5 = a3b3/a1 and b4 = a2b3/(2a1) into a2b5 - 2a3b4 gives
a2a3b3/a1 - a2a3b3/a1 = 0, killing b6; in (4,5), a2b8 = a2a5b3/a1 and
-2a5b4 = -a2a5b3/a1 cancel (after a3 = 0), leaving b9 proportional to a6
alone. Extra key
(3,5) then has single-monomial reduced form with unit cofactors => M2 zeroes
the P-side coefficient a3 (this is the one P-side eliminable, z = 1 =
w_P - 1). Bookkeeping: n_unknowns = (2w_Q+1) + 1 = 8 (Prop. B + a3), surplus
= 9 - 8 = 1 = 2(w_P-1) - z. The computation uses pivot constants
{2,3,4,3,4,5,6} and the final 1/5: primes {2,3,5} ONLY - a block-local
sharpening of LEMMA.md's full-chain prime set {2,3,5,7,11,13} (7,11,13 enter
only through far-column pivots, which the obstruction does not need).
Machine check: cases/surplus_count.py reproduces every line above exactly
(assertion-locked) for open, swap (after (P,Q)->(Q,-P) normalization), and
mini, independently of strip length. QED

Chart-free restatement: unit * a2^2 a6 * b_{q0} lies in the block ideal +
gap-kill ideal; with the vertex equation (b_{q0} a unit), a2^2 a6 lies in the
core ideal - exactly LEMMA.md's ideal statement, now derived from corner
data alone.

### Surplus-key position rule

The surplus key is the topmost non-identically-vanishing key of the block's
OUTER column: stratum w = 1 (one lattice step below the top edge of
N(P)+N(Q)) in Minkowski column (p0+q0)_x + 1. Coordinates:

    surplus key = (k+2, d2*(k+2) - 1)      [= (4,7) = (1,1) + 3d for open]

The inner column's w = 1 key, (k+1, d2*(k+1) - 1) = (3,5), is NOT the
surplus: it is the P-side M2 event (forces a3 = coeff_P(d) = 0). "Would-be
tower relation with no new gap-side coefficient left to define" (LEMMA sec. 3)
= our "extra key of stratum w in [1, w_P-1]" (Prop. B), made precise.

### Regimes where the count breaks

Scope map (cases/surplus_count.py scan; depth-2 block, generic lengths;
PINS/TRIVIAL exact rational arithmetic, torus verdicts numeric Gauss-Newton):

    k  d2 | wP wQ | keys unk surplus | leftover content
    2  1  |  1  1 |   3   3    0     | none (no extra keys)
    3..5,1|  1  . |   .   .    0     | none (no extra keys)
    2  2  |  2  3 |   9   8    1     | PINS -1/5 a2^2 a6      <- THE LEMMA
    3  2  |  2  5 |  13  12    1     | TRIVIAL (== 0)
    4..5,2|  2  . |   .   .    1     | TRIVIAL (== 0)
    2  3  |  3  5 |  15  11    4     | 4x OTHER, torus-EMPTY
    3  3  |  3  8 |  21  17    4     | 4x OTHER, torus-solvable
    4..5,3|  3  . |   .   .    4     | OTHER, torus-solvable
    2  4  |  4  7 |  21  15    6     | 6x OTHER, torus-EMPTY
    3  4  |  4 11 |  29  23    6     | 6x OTHER, torus-EMPTY
    4..5,4|  4  . |   .   .    6     | OTHER, torus-solvable

Recorded honestly:

1. k = 1 (reg shape): raw count is ALSO 9 - 8 = 1, but the leftover (3,8)
   reduces to 0. The bare count does not discriminate; condition (iii) must
   require the leftover CONTENT (unit)*M*b_{q0}, M != 0.
2. d2 = 1 (w_P = 1): no extra keys at all; block exactly balanced; no
   obstruction (exact).
3. k >= 3 with d2 = 2: the inner extra still M2-forces a3 = 0 (reduced form
   -a3^k b_{q0} a1^{1-k}, verified exactly k <= 5), but the outer extra
   reduces IDENTICALLY to 0; deeper columns only add torus-solvable
   P-constraints. Condition (iii) FAILS although (i)+(ii) hold: (iii) is
   genuinely independent of (i)+(ii), and the k-vs-gap confound of the review
   resolves as: the collapse needs k = 2 exactly (given d2 = 2).
4. k = 2 with d2 >= 3 (and (k,d2) = (3,4)): no M2 fires; the 2(w_P-1)
   leftovers form a multi-monomial system with NO torus point (numeric):
   chart-emptiness plausibly persists, but NOT in surplus = 1 single-monomial
   form. A correct general (iii) would be "the extra-key system has no torus
   point"; only its (2,2) cell is proved here.
5. Out of scope entirely: d1 >= 2 (sparse columns), y-axis support (the c1
   regime, where gap-kill itself fails), strips shorter than the block.
6. Numeric caveat: torus-EMPTY/solvable verdicts are 80-restart Gauss-Newton
   probes, not proofs; all PINS/TRIVIAL verdicts and both propositions are
   exact.

## Status

- Phase 1 DONE: validation table above; script cases/surplus_count.py
  (self-contained, exact arithmetic, assertion-locked against LEMMA.md's
  audited chain; modes: default = 6 families, `scan` = 16-cell scope map).
- Phase 2: Propositions A and B (key count 2(w_P+w_Q)-1; gap-side
  eliminability 2w_Q+1 and the 2(w_P-1) extra keys) PROVED for all k >= 1,
  d2 >= 1 in scope. Main theorem — condition (iii) with surplus = 1,
  surplus key (k+2, d2(k+2)-1), obstruction (unit)*a2^2*a6*b_{q0} — PROVED
  for the regime (k,d2) = (2,2) (= the open/swap/mini corner data, any strip
  lengths), char not in {2,3,5}. Outside that regime (iii) provably fails
  (k >= 3 or d2 = 1) or changes form (k = 2, d2 >= 3: system-level
  obstruction, numeric evidence only) — see scope map.
- This discharges LEMMA.md sec. 5's "condition (iii) is NOT yet a polygonal
  criterion" for the computed families, and sharpens FACE-ISOLATION TL1:
  TL1's counting claim is TRUE as stated only in the (2,2) cell; its correct
  general form is torus-emptiness of the extra-key system, not a bare count.
- Open: all-k closed form for the extra-key reductions (pattern
  -a3^k b q0 a1^{1-k} verified k <= 5); exact (non-numeric) torus verdicts
  for d2 >= 3; the d1 >= 2 and y-axis-support regimes.

## Errata (2026-08-05, per SURPLUS-REVIEW.md)
- §theorem: the chart-free "ideal membership" sentence is corrected to RADICAL
  membership (the a3-kill is quadratic; dual-number witness in review §3).
  Variety-level statement unaffected; char set {2,3,5} confirmed sharp.
- Discriminator: "leftover content == 0 for the solved shape" is observed on
  reg_9_24_c3, not general (reg_swap/nf_k1_d2 leave nonzero torus-solvable
  constraints); the robust form of (iii) is the PINS-form statement.
- Scope-map torus verdicts (2026-08-05, per SURPLUS-EXT §1.3): the numeric
  "torus-solvable" at (3,3), (4,3), (5,3) are FALSE POSITIVES (probe tol
  1e-11 vs |vars| >= 1e-4 misses multiplicity->=3 forced zeros); these cells
  are torus-EMPTY, proved by exact resultant certificates (surplus_ext.py
  phaseC3b). (4,4), (5,4) "solvable" now suspect/unresolved. The EMPTY
  verdicts at (2,3) (= toy_w3) and (2,4) are upgraded to exact theorems
  (SURPLUS-EXT §1.2-1.3); (3,4)'s EMPTY stays numeric-only for now.
