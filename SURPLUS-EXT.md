# SURPLUS-EXT: Extending the vertex-gap theorem beyond (k,d2)=(2,2)

Status: SKELETON — sections filled incrementally.

## 0. Setup and conventions
Recap (SURPLUS.md, LEMMA.md); notation fixed for this file:
- Reduced pair: [P,Q] = x^k; N(P), N(Q) strips along primitive d = (1,d2),
  top edges through origin; bottom corners saturated; hypothesis (i) forces
  {p0,q0} = {(1,0),(k,1)}; normalized so gap side is Q: p0=(1,0), q0=(k,1).
  Widths w_P = d2, w_Q = k*d2 - 1. RHS exponent from GGV corner data:
  k = ceil(b/a) - 2 for family corner A0=(a,b), b>a (SECTION4-AUTOMATION §1).
- Depth-2 block = Minkowski cols k+1, k+2; live pairs P cols {1,2} x Q cols
  {k,k+1}; self-contained. n_keys = 2(w_P+w_Q)-1 (Prop A); 2w_Q+1 unit-pivot
  eliminations (Prop B); 2(w_P-1) extra keys, strata w in [1, w_P-1].
- Column-ODE view (new here, used in §§1-2): write P col 1 as A(y) =
  sum_{i=0}^{d2} a_{(1,i)} y^i (a_{(1,0)} = a_{p0} unit), P col 2 as B(y)
  (monomials y^{d2}..y^{2 d2}), Q col k as C(y) (y^1..y^{k d2}, coefficient
  of y^1 = b_{q0} unit), Q col k+1 as E(y) (y^{d2+1}..y^{(k+1) d2}).
  Post-gap-kill, bracket Minkowski column k+1 as a poly in y is
  A C' - k A' C, column k+2 is A E' - (k+1) A' E + 2 B C' - k B' C;
  key (X,s) = coefficient of y^{s-1}. Vertex equation = y^0 coeff of col k+1.
  (To be machine-verified against cases/surplus_count.py by surplus_ext.py.)
- Cell labels used in §3: THEOREM-COVERED = (k,d2)=(2,2) gap regime (proved
  theorem, SURPLUS.md); MECHANISM-ABSENT = k<=0 / k=1 (no gap) / d2=1 (no
  extra keys) / k>=3 verdict cells (see §2); NEEDS-COMPUTATION = wide strips
  w_P>=3 and other unresolved cells; OUT-OF-SCOPE = y-axis support (c1
  shape, gap-kill fails) or d1>=2; UNKNOWN = reduction data unavailable.

## 1. Target 1 — Wide strips (w_P = 3): the surplus-4 leftovers
### 1.1 Symbolic characterization of the 4 leftover constraints
(TBD)
### 1.2 Torus-emptiness: theorem or sub-regime
(TBD)

## 2. Target 2 — k >= 3: why leftovers vanish
### 2.1 The cancellation mechanism

Machine verification first (cases/surplus_ext.py, exact Fractions, symbolic
in a2..a6, units a1 = c1 = 1 scaled out; run 2026-08-04, exit 0):
- V1: the column-ODE key layout matches surplus_count.py enumeration.
- V2 (k = 2..10, extends SURPLUS's k<=5): inner extra key (k+1, 2k+1)
  reduces to exactly -a3^k (i.e. -a3^k b_q0 a1^{1-k} with units restored).
- V3 (k = 2..10): after a3 := 0, outer extra key (k+2, 2k+3) reduces to
  0 IDENTICALLY for every k >= 3; at k = 2 it is -(1/5) a2^2 a6 and the
  top Q-coefficient is -(1/15) a2 a6 — byte-matching the (2,2) theorem's
  b10 = -a2 a6 b3/(15 a1^2) and surplus -(1/5) a2^2 a6 b_q0 a_p0^{-2}.
- V4 (k = 3..10): with a3 = 0 the whole solved column E has
  deg_y E <= k+3 (at k = 2 it has deg 6 = 2k+2 instead — the log tail).

Mechanism (why, now proved for ALL k >= 3 at depth 2 — see §2.2 for the
precise statement). Write the block in the column-ODE form of §0 with
d2 = 2: A = a1 + a2 y + a3 y^2, B = a4 y^2 + a5 y^3 + a6 y^4,
C = Q col k (val >= 1, deg <= 2k), E = Q col k+1 (val >= 3, deg <= 2k+2):
    (I)  A C' - k A' C = a1 c1        (col k+1; vertex eq = y^0 coeff)
    (II) A E' - (k+1) A' E = -(2 B C' - k B' C) =: -G   (col k+2)
Step 1 (inner extra). (I) has the 1-dim solution space
C = A^k (kappa + a1 c1 int_0^y A^-(k+1)); val >= 1 forces kappa = 0 and the
lower keys of col k+1 define c_2..c_2k as this series; the inner extra key
equals -(2k+1) a1 ctilde_{2k+1} (the would-be next series coefficient).
Closed form ctilde_{2k+1} = a3^k c1 / ((2k+1) a1^k): VERIFIED k <= 10 (V2),
general k NOT closed here (stated honestly; not needed for §2.2). M2 then
forces a3 = 0 on the variety (k-th power: radical membership, as in the
review's (2,2) erratum).
Step 2 (a3 = 0 collapses (I) to a binomial). With a3 = 0, A = a1 + a2 y and
the EXACT solution of (I) is the degree-k POLYNOMIAL
    C = (a1 c1/(k a2)) [ (1 + a2 y/a1)^k - 1 ]   (deg k <= 2k: fits N(Q)).
(a2 = 0 too: C = c1 y, same conclusion.)  So all col-(k+1) keys hold.
Step 3 (log-residue dichotomy for (II)). Assume a3 = 0, a2 != 0; substitute
z := 1 + a2 y/a1 (so A = a1 z, y = (a1/a2)(z-1)) and set beta(z) := B(y(z)),
a polynomial of z-degree 4 with beta(1) = B(0) = 0. Then C' = c1 z^{k-1},
G = c1 [2 beta z^{k-1} - beta'(z)(z^k - 1)], and the unique val>=3 solution
of (II) is E = -A^{k+1} int_0^y G A^-(k+2) du, i.e.
  E = -(c1/a2) z^{k+1} int_1^z [ 2 beta w^-3 - beta' w^-2 + beta' w^-(k+2) ] dw.
The first two integrand terms are EXACT: 2 beta w^-3 - beta' w^-2 =
-(d/dw)(beta w^-2), contributing beta(1) - beta(z) z^-2 = -beta(z) z^-2.
The third term, with beta' = sum_{m=0}^3 beta'_m w^m, integrates to
sum_m beta'_m (z^{m-k-1} - 1)/(m-k-1) — NONSINGULAR iff m != k+1.
Since m <= 3 = deg beta', for k >= 3 no singular term exists and
  E = (c1/a2) [ beta(z) z^{k-1} - sum_m beta'_m (z^m - z^{k+1})/(m-k-1) ],
a polynomial of z-degree (= y-degree) <= k+3 <= 2k+2: it fits N(Q)'s
column k+1, its val >= 3 is forced by the ODE (G has val 2), and EVERY key
of column k+2 — including both extras — holds identically. QED (k >= 3).
Step 4 (k = 2 contrast = the theorem's obstruction, re-derived). For k = 2
the m = k+1 = 3 term is singular: int beta'_3 w^-1 = beta'_3 log w with
beta'_3 = 4 a6 (a1/a2)^4. The log tail z^{k+1} log z contributes to y^6 the
coefficient -(c1/a2) 4 a6 (a1/a2)^4 (a2/a1)^6 [t^6](1+t)^3 log(1+t) =
-(c1/a2) 4 a6 (a2^2/a1^2)(1/60) = -a2 a6 c1/(15 a1^2) = b10, and the outer
extra -(1/5) a2^2 a6 c1 a1^-2 — the (2,2) surplus monomial. So the entire
(k, d2=2) row of the scope map is governed by ONE residue:
  obstruction  <=>  the logarithmic residue at m = k+1 survives
               <=>  k + 1 <= deg_z beta' = 2 d2 - 1  (d2=2: k <= 2).
Char caveat: the derivation divides by s*a1 (s <= 2k+3), k, (m-k-1), a2;
valid over char 0 (or char > 2k+3); a2 = 0 handled separately in Step 2/
directly: A = a1 gives E = -int G/a1, polynomial of deg 5 <= 2k+2. All of
Steps 2-4 are also machine-checked coefficient-wise by V3/V4 for k <= 10.

### 2.2 Impossibility / verdict for k >= 3

THEOREM (no near-origin obstruction, k >= 3, d2 = 2, depth-2 block; char 0
or char > 2k+3). For every k >= 3, arbitrary a2, a4, a5, a6 (a2 = 0
allowed), arbitrary unit values a1 = a_p0, c1 = b_q0, the assignment
a3 := 0, C := (a1 c1/(k a2))[(1 + a2 y/a1)^k - 1], E := the Step-3 closed
form, satisfies EVERY key of the depth-2 block. Consequences:
(1) The block variety maps onto the whole a3 = 0 slice of P-coefficient
    space with b_q0 a free unit: NO leftover of PINS form
    (unit)*(monomial)*b_q0 exists, and no chart in the coordinates
    {a2, a4, a5, a6} is emptied. Condition (iii) FAILS for all k >= 3,
    d2 = 2 — proved, upgrading SURPLUS.md note 3 from "computed k <= 5"
    to all k (the TRIVIAL verdict on the outer extra is now a theorem:
    by uniqueness of the triangular solve, the cascade's reduced outer
    extra evaluates at the explicit solution to 0 for a Zariski-dense set
    of (a2, a4, a5, a6), hence is the zero polynomial).
(2) The only near-origin restriction on P is the support restriction
    a3 = coeff_P(1,2) = 0. Proved-for-all-k part: the inner-extra locus
    CONTAINS {a3 = 0} (the series for C truncates at degree k there).
    Sharp form "inner extra = -a3^k b_q0 a1^{1-k}" (hence the locus is
    exactly {a3 = 0}, by radicality of the k-th power): verified
    exactly for k <= 10 (V2); general-k induction not closed — flagged.
    Either way a3 = 0 is no corner-contradiction: a3 is not a saturated
    corner, so hypothesis (i) is untouched (same phenomenon as reg's
    forced a(1,2) = a(1,3) = 0, SURPLUS-REVIEW Front 2).
(3) Verdict line: NO near-origin obstruction exists for k >= 3 (d2 = 2);
    the k = 2 obstruction is precisely the m = k+1 logarithmic residue,
    which dies for k >= 3 because deg_z beta' = 3 < k + 1.
Caveats, honestly: (a) depth 2 only — deeper columns (D = 3..5) add one
leftover per column, numerically torus-solvable (SURPLUS toy_k3), each a
residue-type condition linear in the fresh P-column coefficients; not
proved here. (b) d2 = 2 only — the k >= 3, d2 >= 3 cells stay numeric
(scan: solvable except the (3,4) cell, which is numeric-EMPTY and belongs
to the wide-strip regime of §1). (c) char excluded set is proof-technical
(denominators s <= 2k+3, k, m-k-1, a2-chart), as in the (2,2) theorem.
PHASE B COMPLETE (verdict: no k>=3 near-origin obstruction at d2=2).

## 3. Target 3 — Coverage of GGV admissible corner families
### 3.1 Family -> regime cell mapping
Source: GGV5 = arXiv:1708.07936 §7 (/tmp/jcpapers/1708.07936.tex, lines
1794-1875): all 34 admissible cases max(deg P,deg Q) <= 150 (13 from the §6
(m,n)-families F1..F24 + 9 length-1 + 11 length-2 + 1 length-3 chains).
Derived per row (pure corner arithmetic, SECTION4-AUTOMATION §1 rule):
j = ceil(b/a) for corner A0=(a,b); RHS = x^k with k = j-2. d2* = a/(ja-b) =
the strip slope IF the family reduces to the SURPLUS strip shape (verified
against all reduced cases: (9,24)->3, (8,28)->2, matches cases/emit.py).
b/a integer => the A0-corner maps onto the y-axis under psi_j => strip shape
impossible for subcases keeping that corner (c1/pentagon regime). Widths in
the strip shape: w_P = d2, w_Q = k*d2-1 (SURPLUS Prop A scope).

| A0 (family) | (m,n) deg | k | d2* | shape flag |
|---|---|---|---|---|
| (4,12) F1 | (3,4) 64; (5,7) 112 | 1 | - | y-axis |
| (5,20) F2 | (2,3) 75; (3,5) 125 | 2 | - | y-axis |
| (5,20) F3 | (3,2) 75 | 2 | - | y-axis |
| (6,15) F7 | (2,7) 147 | 1 | 2 | strip possible |
| (6,15) F8 | (3,7) 147 | 1 | 2 | strip possible |
| (7,21) F9 | (2,3) 84; (3,5) 140 | 1 | - | y-axis (4.4: quad shape) |
| (7,21) F11 | (2,5) 140 | 1 | - | y-axis |
| (9,24) F17 | (2,3) 99 | 1 | 3 | strip subcase c3 (reg_9_24_c3) |
| (8,24) F22 | (2,3) 96 | 1 | - | y-axis; DISCARDED (GGV5 Prop 7.x) |
| (8,24) F24 | (3,4) 128 | 1 | - | y-axis |
| (7,35) L1 | (2,3) 126 | 3 | - | y-axis |
| (7,42) L1 | (3,2) 147; (2,3) 147 | 4 | - | y-axis |
| (8,28) A1=(7/4,3) | (3,4) 144 | 2 | 2 | strip possible (unreduced) |
| (8,28) A1=(11/4,7) | (3,2) 108 | 2 | 2 | REDUCED: c1 pentagon, c2 strip |
| (9,36) L1 | (3,2) 135; (2,3) 135 | 2 | - | y-axis |
| (11,33) L1 | (2,3) 132 | 1 | - | y-axis |
| (12,33) L1 | (2,3) 135 | 1 | 4 | strip possible |
| (8,32) L2 | (3,2) 120 | 2 | - | y-axis; DISCARDED (GGV22 §3) |
| (8,40) L2 | (3,2) 144 | 3 | - | y-axis |
| (9,27) L2 | (2,3) 108 | 1 | - | y-axis (4.1: pentagon reg_9_27) |
| (9,36) L2 | (2,3) 135 | 2 | - | y-axis |
| (10,40) L2 x2 | (3,2) 150 both | 2 | - | y-axis |
| (12,30) L2 | (3,2) 126 | 1 | 2 | strip possible |
| (12,36) L2 x4, L3 x1 | (2,3)x4 144; (3,2) 144 | 1 | - | y-axis |

Row count check: 13 + 9 + 11 + 1 = 34; k-histogram k=1:19, k=2:11,
k=3:2, k=4:2 (script check 2026-08-04, this machine).
### 3.2 Coverage table
Reduced-case ground truth (cases/emit.py corner sets, GGV22 §4):
reg_9_27, reg_9_24_c1, reg_9_24_c2, open_8_28_c1: pentagons (y-axis
support) -> OUT-OF-SCOPE shape (gap-kill fails; SURPLUS note 5).
reg_7_21: quadrilateral with x- and y-axis edges -> OUT-OF-SCOPE shape.
reg_9_24_c3: strip, k=1, d=(1,3), wP=2, wQ=3, no gap -> MECHANISM-ABSENT.
open_8_28_c2: strip, k=2, d=(1,2), wP=2, wQ=3, gap -> THEOREM-COVERED.

Classification of the 34 rows (cells per §0; flags from §3.1):
- THEOREM-COVERED: 1 row, (8,28)+(11/4,7)+(3,2) — PARTIAL: its strip
  subcase c2 is the proved (2,2) theorem; its sibling subcase c1 is
  pentagon-shaped, OUT-OF-SCOPE for the vertex-gap mechanism (still open,
  handled in repo by msolve lane).
- MECHANISM-ABSENT (no-gap, k=1): 19 rows (F1 x2, F7, F8, F9 x2, F11, F17,
  F22, F24, (11,33), (12,33), (9,27), (12,30), (12,36) x5). Basis: k is
  pure corner data; under hypothesis (i), k=1 forces both bottom corners
  to x=1 in ANY strip reduction, so condition (ii) fails (LEMMA §4
  symmetrized). Caveat: "leftover content 0" at k=1 is observed-only and
  labeling-dependent (SURPLUS-REVIEW §4); absence of the PINS mechanism is
  the proved part. Pentagon-shaped reductions are out of scope separately.
  F22 additionally discarded by GGV5 Prop (caso antisimetrico).
- MECHANISM-ABSENT (k>=3, conditional): 4 rows ((7,35) k=3, (8,40) k=3,
  (7,42) x2 k=4). Basis: §2 verdict (proved for strip shape with d2=2 at
  depth 2). CONDITION: all four have b/a integer, so if the A0-corner
  survives reduction the shape is pentagon/y-axis = OUT-OF-SCOPE rather
  than strip; and d2>=3 strips would land in the unproven wide cell. No
  reduction data exists for these (SECTION4-AUTOMATION unimplemented) —
  honest cell: MECHANISM-ABSENT if strip-with-d2=2, else UNKNOWN.
- DISCARDED (not a possible pair at all): 1 row, (8,32)+(3,2) (GGV22 §3
  one-paragraph argument; regression gate G2).
- UNKNOWN (k=2, reduction not done): 9 rows — F2 x2, F3, (8,28)+(7/4,3)
  +(3,4), (9,36) x2 (len-1), (9,36) (len-2), (10,40) x2. Of these,
  (8,28)+(7/4,3) has d2*=2: if it strip-reduces it lands in the PROVED
  (2,2) cell; the other 8 have b/a integer (y-axis flag), so strip
  reduction is impossible where A0 survives — expected OUT-OF-SCOPE.

COUNTS (34 rows): THEOREM-COVERED 1 (partial: 1 of 2 subcases);
MECHANISM-ABSENT 23 (19 no-gap k=1 + 4 conditional k>=3);
NEEDS-COMPUTATION 0 firm (the wide-strip cell w_P>=3 matches NO deg<=150
family on current data); DISCARDED 1; UNKNOWN 9.
Headline: the proved (2,2) theorem covers exactly the open_8_28_c2 corner
data among all deg<=150 admissible families; no deg<=150 family is known
to need the wide-strip extension (§1); the k>=3 extension (§2) has no
confirmed strip-shaped client at deg<=150 (both k>=3 corners are y-axis
flagged). PHASE A COMPLETE.

## 4. Validation scripts
- cases/surplus_ext.py (TBD)

## 5. Summary
(TBD)
