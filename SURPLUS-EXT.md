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
  Added in Phase C: SURPLUS-4-COVERED = wide-strip cells whose leftover
  system is exactly solved by the surplus-4 variant theorem (§1): torus-
  empty via forced P-col-1 binomial support (NOT a PINS obstruction);
  currently (2,3), (2,4) full variety + (3,3), (4,3), (5,3) rigidity.

## 1. Target 1 — Wide strips (w_P = 3): the surplus-4 leftovers
### 1.1 Symbolic characterization of the 4 leftover constraints

Cell: (k,d2) = (2,3) (w_P = d2 = 3, w_Q = 5; toy_w3's cell; the header's
"w_P = 3" — note w_P = d2 identically, so this is the d2 = 3 column of the
scope map). Machine layer: cases/surplus_ext.py wide_setup/wide_W0/wide_W1
(run 2026-08-05, exit 0): the general-(k,d2) column-ODE solve is
cross-checked against an independent lattice-det enumeration of every block
key — eliminated keys reduce to 0, vertex to +1, and the 4 leftovers equal
the ODE extras EXACTLY (also verified at (2,2) anchor, (2,4), (3,3)).

Coordinates (units a1 = a_p0, c1 = b_q0 scaled to 1): A = 1 + a2 y + a3 y^2
+ a4 y^3 (P col 1, points (1,0)..(1,3)), B = b3 y^3 + .. + b6 y^6 (P col 2,
points (2,3)..(2,6)). Q cols 2,3 are eliminated (Prop B, 2w_Q+1 = 11 pivots).
NO M2 ever fires (z = 0): the leftover count is exactly 2(w_P-1) = 4.

Leftover positions (Prop B strata w in [1,2] of both block columns):
inner pair L1 = key (3,7) [w=2], L2 = (3,8) [w=1] — coeffs of y^6, y^7 in
A C' - 2 A' C; outer pair L3 = (4,10) [w=2], L4 = (4,11) [w=1] — coeffs of
y^9, y^10 in A E' - 3 A' E + 2 B C' - 2 B' C. Exact reduced forms:

    10*L1 =  2 a3^3 - 4 a2^2 a3^2 + 2 a2^3 a4 + 19 a2 a3 a4 - 25 a4^2
    10*L2 = -2 a2 a3^3 + a2^2 a3 a4 + 8 a3^2 a4 + a2 a4^2
    L3, L4: 18 monomials each, LINEAR in (b3..b6), coefficients in
            Q[a2,a3,a4] (not displayed; machine-held, wide_setup(2,3)).

Structure (generalizing the (2,2) machinery):
(a) B-grading: L1, L2 are B-FREE (pure P-col-1 constraints); L3, L4 are
    linear in B — same split as (2,2)'s inner -a3^2 / outer -(1/5)a2^2 a6.
(b) Weighted homogeneity: deg(a_{i+1}) = deg(B_i) = i gives deg L1..L4 =
    6, 7, 9, 10 (= the y-levels); each key is also w-stratum homogeneous.
(c) ODE meaning: L1, L2 are unit-triangular combinations of the would-be
    series continuation ctilde_7, ctilde_8 of C = a1 c1 A^2 int_0^y A^-3
    (L1 = -7 a1 ctilde_7; L2 = -(8 a1 ctilde_8 + 5 a2 ctilde_7)), so
    ideal(L1,L2) = ideal(ctilde_7, ctilde_8): "P col 1 must make the
    C-series truncate one AND two steps past deg 6". Likewise L3, L4 for
    the E-series with inhomogeneity G = 2 B C' - 2 B' C.
(d) Monomial content of the inner pair: restricted to a2 = 0 or a3 = 0 or
    a4 = 0 the pair stays a genuine 2-eq system (no M2 event, unlike
    (2,2)/(k>=3,2) where the inner extra is the single monomial -a3^k).
### 1.2 Torus-emptiness: theorem or sub-regime

THEOREM (surplus-4 variant, inner part; (k,d2) = (2,3), depth-2 block, any
strip lengths containing it; char not in {2,3,5}). The inner leftover pair
alone forces a3 = a4 = 0, i.e. V(L1,L2) = {a3 = a4 = 0}: P col 1 collapses
to the binomial a1 + a2 y (support = p0 and (1,1)). Consequently the FULL
4-leftover system has NO common zero with all block coordinates nonzero
(any zero has a3 = 0): the toy_w3 "torus-EMPTY" numeric verdict is now an
exact theorem.

Proof 1 (resultant; machine-verified, wide phaseC2, exit 0).
Res_a4(10L1, 10L2) = -3200 a3^7, and the a4-leading coefficient of 10L1 is
the CONSTANT -25, so for every fixed (a2,a3) the two polynomials in a4 have
a common root iff the resultant vanishes: any common zero has a3 = 0. Then
10L2|_{a3=0} = a2 a4^2 and 10L1|_{a3=0} = 2 a2^3 a4 - 25 a4^2: a2 a4^2 = 0
with a4 != 0 gives a2 = 0 and then L1 = -(5/2) a4^2 != 0 — so a4 = 0.
Conversely a3 = a4 = 0 kills both (every monomial contains a3 or a4).
Primes used: pivots 2..6 of the triangular solve, 3200 = 2^7 5^2, 25, 5/2:
char not in {2,3,5} suffices (denominator/pivot set audited as in (2,2)).

Proof 2 (structural: squarefree-forcing + log-free divisibility; conceptual
route, generalizes — used again at d2 = 4 in §1.3).
Extras vanish iff the polynomial identity  C'A - 2A'C = a1 c1  holds exactly
with C the solved column (deg <= 6). (i) At any root r of A of multiplicity
m >= 2 the left side is divisible by (y-r), the right side is a nonzero
constant: so A is SQUAREFREE, and at simple roots -2A'(r)C(r) = a1 c1 gives
A'(r), C(r) != 0. (ii) Differentiating the identity once/twice and
evaluating at r: C'(r) = -2A''C/A', then -C'A'' - 2A'''C - 2A''C' = 0
forces 3A''(r)^2 = A'(r)A'''(r). Hence A | N(A) := 3A''^2 - A'A'''.
(iii) Case delta := deg A: delta = 3: N = (12a3^2-6a2a4) + 60a3a4 y
+ 90a4^2 y^2 has deg 2 < 3, so N = 0: 90a4^2 = 0, impossible. delta = 2:
N = 12a3^2 != 0 constant, impossible. So delta <= 1: a3 = a4 = 0. QED

Class of the obstruction — HONEST: this is a SUPPORT-RIGIDITY statement
(a3 = coeff_P(1,2), a4 = coeff_P(1,3) are forced to 0; neither is a
saturated corner, so hypothesis (i) is untouched), NOT a PINS-form
(unit)*(monomial)*b_q0 obstruction: b_q0 stays free. What survives of the
(2,2) collapse mechanism at d2 = 3 is exactly this forced degeneration of
the P-side column; the b-side content is settled next (outer pair on the
binomial locus).

COMPLETE VARIETY (surplus-4 variant theorem, full form; machine layer
phaseC2b, W4, exit 0). On the forced locus a3 = a4 = 0 (A = a1 + a2 y):
    L4 == 0 IDENTICALLY, and  L3 = (a2^3/21) * R,
    R := a2^2 b4 - 5 a2 b5 + 15 b6      (b3 ABSENT).
Hence  V(L1,L2,L3,L4) = {a3=a4=0, a2=0}  u  {a3=a4=0, R=0}.
Mechanism of both facts (log-residue view, §2 Steps 3-4 with d2 = 3):
with z = 1 + a2 y/a1, beta(z) = B(y(z)), the only singular integrand term
is beta'_3 w^{-1} (m = k+1 = 3), so the non-polynomial part of E is
-(c1/a2) beta'_3 z^3 log z. Both outer extras are forced multiples of the
SINGLE residue beta'_3 = 4 R/a2^6 (units scaled to 1), where
R = sum_{j=4}^{6} (-1)^j C(j,4) a2^{6-j} b_j; and the two tail coefficients
of z^3 log z satisfy
11*[y^11] + 7 a2 [y^10] = 0 for the z^3 log z series (11/1320 = 7/840),
which kills the top extra L4 on the locus identically. The coefficients
1, -5, 15 are (-1)^j C(j,4), j = 4..6 — at d2 = 2 the sum degenerates to
the single term C(4,4) b4 = a6: the (2,2) PINS monomial is the d2 = 2
shadow of this residue functional.
Consequences: (1) torus-emptiness holds (via a3 = 0), settling the cell
EXACTLY; (2) on the main component (a2 != 0) the residual b-side condition
R = 0 is a 3-term linear form: solvable with all of b3..b6, b_q0 nonzero —
NO empty chart in the b-coordinates and NO PINS leftover: condition (iii)
in its (2,2) single-monomial form FAILS at (2,3); its correct analog is
"P col 1 binomial + one residue hyperplane R = 0". (3) char caveats: the
outer computation adds e-pivots 7,8,9 and denominators 21, 840, 1320
(primes {2,3,5,7,11}); the INNER rigidity (the part torus-emptiness needs)
uses only {2,3,5}.

### 1.3 The pattern in w_P: rigidity at w_P = 4 and the k-grid

Leftover COUNT: 2(w_P - 1) exactly, all cells (Prop B; z = 0 since no M2
fires for w_P >= 3 — every extra key has >= 2 monomials, seen on the whole
grid below). Scan values 4 (w_P=3), 6 (w_P=4): formula confirmed.

THEOREM (w_P = 4, cell (2,4); char 0, excluded primes within {2,3,5,7}).
V(inner extras I1,I2,I3) = {a3 = a4 = a5 = 0}: P col 1 is again forced to
the binomial a1 + a2 y, so torus-emptiness PERSISTS at w_P = 4, exactly.
On the forced locus the outer extras satisfy O2 = O3 = 0 IDENTICALLY and
O1 = -(a2^4/55) R4, R4 := a2^4 b4 - 5 a2^3 b5 + 15 a2^2 b6 - 35 a2 b7
+ 70 b8 (machine: phaseC3/W5-W6, exit 0). So
  V(all 6 leftovers) = {a3=a4=a5=0, a2=0} u {a3=a4=a5=0, R4=0},
same shape as (2,3): support rigidity + ONE residue hyperplane; no PINS.
Proof of the inner part (structural route of §1.2 Proof 2, now with the
delta = 4 divisibility case; every identity machine-asserted in phaseC3):
extras vanish iff C'A - 2A'C = a1 c1 exactly => A squarefree and
A | N(A), N := 3A''^2 - A'A'''. Writing A = 1 + py + qy^2 + ry^3 + sy^4:
  N - 336 s A = E0 + 60 E1 y + 30 E2 y^2   (top two coeffs cancel), with
  E0 = 12q^2 - 6pr - 336s, E1 = qr - 6ps, E2 = 3r^2 - 8qs.
delta = 4 (s != 0): divisibility means E0 = E1 = E2 = 0; the identities
  9s E0 = 84 s (q^2 - 36 s) - 3 q E2 + 9 r E1,
  27 r^2 - 2 q^3 = 9 E2 - 2 q (q^2 - 36 s)
give q^2 = 36s, 27r^2 = 2q^3, and (via E1, q != 0) r = pq/6; these force
(p,q,r,s) = (4u, 6u^2, 4u^3, u^4), i.e. A = (1 + u y)^4 — NOT squarefree
(u = 0 would give s = 0): contradiction. delta = 3 (s = 0, r != 0):
N = (12q^2 - 6pr) + 60qr y + 90r^2 y^2 has degree 2 < 3, so N = 0:
90 r^2 = 0, impossible. delta = 2: N = 12q^2 != 0 constant, impossible.
Hence delta <= 1. QED (perfect powers (1+uy)^delta satisfy the
divisibility for every delta >= 4 — squarefreeness is what kills them;
any general-d2 proof must keep both halves).

GRID (phaseC3b, exit 0). Inner rigidity V(inner) = {A binomial} is also
CERTIFIED at (k,3) for k = 3, 4, 5 by a uniform two-resultant certificate:
Res_a4(J1,J2) = c a3^m with CONSTANT a4-lead of J1 (=> a3 = 0), then on
the slice Res_a2 = c' a4^N with pure-a4 a2-lead (=> a4 = 0); exponents
(m,N) = (7,8), (15,12), (26,34), (40,44) for k = 2,3,4,5. Combined with
d2 = 2 (inner = -a3^k, k <= 10) and (2,4): rigidity holds on the ENTIRE
computed grid k in 2..5, d2 in 2..4 except (3,4)/(4,4)/(5,4) (inner not
yet eliminated there; (3,4) numeric-EMPTY is consistent with rigidity).

SCAN CORRECTION (erratum to SURPLUS.md scope map + §2.2 caveat (b)):
the numeric "torus-solvable" verdicts at (3,3), (4,3), (5,3) are FALSE
POSITIVES of the Gauss-Newton probe: rigidity proves these cells
torus-EMPTY. Defect: tolerance 1e-11 with |vars| >= 1e-4 cannot see
forced zeros of multiplicity >= 3 (at a3 = a4 = 1e-4 all leftovers
evaluate ~1e-12). The (4,4), (5,4) "solvable" verdicts are now equally
suspect (unresolved). Numeric torus verdicts should not be trusted for
these systems; the resultant certificates replace them.

OUTER structure on the binomial locus, whole grid: exactly ONE outer
extra survives and equals (unit * a2-power) * R_{k,d2},
  R_{k,d2} = sum_{j=k+2}^{2 d2} (-1)^j C(j, k+2) a2^{2 d2 - j} b_j,
the z^{k+1} log-residue functional (§2 Step 3 with beta' singular at
m = k+1); the higher outer extras vanish identically there. Verified:
(2,3) u=a2^3/21, (3,3) -a2^6/99, (4,3) 2a2^9/1001, (2,4) -a2^4/55,
(3,4) -a2^8/364; and (5,3): ALL outer extras vanish — the sum is EMPTY
iff k + 2 > 2 d2, which at d2 = 2 is exactly §2's k >= 3 identically-zero
outer, and at d2 = 2, k = 2 degenerates to the single monomial
C(4,4) b4 = a6: the (2,2) PINS obstruction is the one-term case of R.

CONJECTURE (w_P pattern, k >= 2, d2 >= 2; evidence above + d2 <= 4
proofs): V(leftover system) = {A binomial} n ({a2 = 0} u {R_{k,d2} = 0}).
Consequences: leftover count 2(w_P-1); torus-EMPTY at EVERY such cell;
PINS form iff (k,d2) = (2,2); no b-side obstruction for d2 >= 3 (R is a
multi-term linear form, torus-solvable in b), none at all when
k > 2d2 - 2. Open: rigidity at (3,4), (4,4), (5,4) and d2 >= 5 (the
perfect-power component makes a uniform proof nontrivial).

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
to the wide-strip regime of §1). [CORRECTED 2026-08-05: the d2=3 "solvable"
scan verdicts were false positives; (3,3),(4,3),(5,3) are torus-EMPTY,
proved — see §1.3 SCAN CORRECTION.] (c) char excluded set is proof-technical
(denominators s <= 2k+3, k, m-k-1, a2-chart), as in the (2,2) theorem.
PHASE B COMPLETE (verdict: no k>=3 near-origin obstruction at d2=2).

## 3. Target 3 — Coverage of GGV admissible corner families
### 3.1 Family -> regime cell mapping
Source: GGV5 = arXiv:1708.07936 §7 (/tmp/jcrefs/1708.07936.tex, lines
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
  than strip. No reduction data exists for these (SECTION4-AUTOMATION
  unimplemented) — honest cell: MECHANISM-ABSENT if strip-with-d2=2;
  SURPLUS-4-COVERED if strip-with-d2=3 (cells (3,3), (4,3) now exact,
  §1.3 — Phase C upgrade of the former "unproven wide cell" caveat);
  UNKNOWN if d2>=4 ((3,4)/(4,4) rigidity open).
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
PHASE C UPDATE (2026-08-05): SURPLUS-4-COVERED cells (2,3), (2,4), (3,3),
(4,3), (5,3) are now exactly settled (§1), removing "NEEDS-COMPUTATION"
as a REGIME for w_P = 3 and for (2,4). Rows moving into the new cell on
CURRENT reduction data: 0 of 34 (every k=2 row has d2* = 2 or y-axis
flag; every k>=3 row is y-axis flagged) — the change is to the
CONDITIONAL branches only: the 4 k>=3 rows' hypothetical d2=3 strip
reductions are covered (see amended bullet above), as would be any
future k=2 reduction landing at d2 in {3,4}. Firm counts unchanged.

## 4. Validation scripts
- cases/surplus_ext.py (exact Fractions throughout; exit 0 = all checks):
  Phase B: selftestV1, phaseB (V1-V4, §2). Phase C: wide_setup (general
  (k,d2) column-ODE solve), wide_W0/W1 (anchor + independent lattice-det
  cross-check), phaseC2 (W2 resultant -3200 a3^7, W3 slices), phaseC2b
  (W4 outer factorization (2,3)), phaseC3 (W5 (2,4) rigidity identities,
  W6 outer), phaseC3b (d2=3 grid certificates k=2..5 + outer survey).
  Resultants via exact Sylvester determinants (presultant/pdet).
- cases/surplus_count.py (Phase-1 engine; its numeric torus_probe verdicts
  at (3,3),(4,3),(5,3) are superseded — §1.3 SCAN CORRECTION).

## 5. Summary
Phase A (§3): 34 GGV deg<=150 rows classified from corner arithmetic;
(2,2) theorem's only confirmed client is open_8_28_c2; no wide-strip
client exists on current data.
Phase B (§2): k >= 3, d2 = 2 verdict is a THEOREM (log-residue dichotomy:
obstruction <=> k+1 <= 2 d2 - 1); no near-origin obstruction there.
Phase C (§1): the wide-strip cells are exactly solved. Surplus-4 variant
theorem at (2,3): V(4 leftovers) = {a3=a4=0} n ({a2=0} u {R=0}),
R = a2^2 b4 - 5 a2 b5 + 15 b6; torus-empty exactly (two independent
proofs: resultant certificate; squarefree+divisibility). Same at (2,4)
with R4 (coefficients C(j,4)); inner rigidity also certified at (3,3),
(4,3), (5,3). The forced content is P-SUPPORT RIGIDITY (col 1 binomial),
not a PINS b_q0-obstruction: condition (iii)'s single-monomial form is
special to (2,2), where the residue functional R_{k,d2} =
sum_{j=k+2}^{2d2} (-1)^j C(j,k+2) a2^{2d2-j} b_j collapses to one term.
Scan erratum: three "torus-solvable" cells were numeric false positives.
Open: rigidity at (3,4), (4,4), (5,4), d2 >= 5; deeper columns D >= 3.
