# SHEET6-CLASSICAL.md — four classical kill-tests on the two-pole template

Status: COMPLETE (2026-08-12, UNREVIEWED). Mission: run four independent
CLASSICAL kill-tests (topology/combinatorics, no Groebner) on the sheet-6
two-pole counterexample template (ground truth SHEET6-TEMPLATE.md sec 1;
class 2P-R3a of SHEET6-LROOT.md sec 4). Engine: cases/classical_tests.py
(new, additive; exact Fraction arithmetic; 22 checks, 0 FAIL).

VERDICT SUMMARY:
  T1 SPLICE / LINK AT INFINITY:  PASS — edge dets positive, all pinned
     node multiplicities l_v > 0 (168/294/2022/4664), and the
     Seifert/Euler (genus) balance closes as an EXACT IDENTITY with all
     unpinned tail data cancelling (sec 1c). Full kill power, zero slack.
  T2 ABHYANKAR-MOH / VALUATION:  PASS at poles (exact, ord_t f_y = -39
     forced == computed); KILLS the x-side slack-1 branch pi_G = 4;
     new sharp windows on B-/x-tails (secs 2b, 2c).
  T3 BMY / LOG-SURFACE:          NEEDS-DATA for full (K+D)^2 <= 3e_orb
     (B/x resolution tails unpinned); its chi-shadow (delta ledger)
     PASSES identically; integral witnesses exist (sec 3a).
  T4 JELONEK:                    PASS — mu(F) = 6 exact by Bezout;
     A(F) nonempty curve, >= 2 component families, total asymptotic
     excess Sum(e_p - 1) = 2g + 6 >= 6; degree ceiling passes.
  Coverage: all four verdicts use only the shared (f,g) genome and
  transfer verbatim to the surviving variants (1,2), (2,3)-chain,
  (2,5)-chain.

## 0. Shared input data (from SHEET6-TEMPLATE.md sec 1, LROOT sec 3-4)

Generic fiber C = {f = a}, deg 168, irreducible (f primitive: J(f,g)=1
kills f = h(p)). Newton corner (deg_y, deg_x) = (126, 42); g: (189, 63),
deg g = 252. Places at infinity of C:

Y-side point at infinity (x = infty, y -> c0), 126 local series
y = c0 + sum c_j x^{-j}, j in (1/42)N:
  - P_1: 1 place, 42 conjugate series, Newton pairs (7,2)(3,10)(2,5)
    [char exponents 12/42 < 32/42 < 37/42 in u = 1/x], g-pole order 3.
  - P_2: same shape (a2-side).
  - B-side: 42 series, 6 per direction of the 7-element B-orbit at F_s
    (split from A-side at exponent 12/42); g FINITE there; place
    partition below F_s NOT pinned (each place degree divisible by 7);
    LROOT ledger: one orbit cluster, price D/i - kbar = 42/6 - 5 = 2 =
    Sigma-lambda.
  - Contact table (exponent of first difference, in units of 1/42):
    same-(A-dir, cube-dir) +/- pair: 37; same A-dir, diff cube-dir: 32;
    diff A-dir (incl. all A-vs-B and B-vs-B diff dir): 12;
    same B-dir pairs: > 12, unpinned.
X-side point at infinity ([0:1:0], y = infty, x -> c0'), l_f = 42 series
  x = c0' + c1' y^{-1} + c2' y^{-2} + (split at height >= 3): single
  cluster, one cv vertex, kappa_G = 1, pi_G in [3,4] (LROOT LR2);
  pairwise contact >= 3 in y^{-1}; g finite; carries psi = 2.
Pole bookkeeping: td = 6 = Lambda(P_1) + Lambda(P_2) = 3 + 3; g has NO
  other poles at infinity on C, so ghat: Cbar -> P^1 has degree 6.

Variant transfer: the surviving branches (1,2), (2,3)-chain, (2,5)-chain
(SHEET6-R6.md) differ only in the h-TOWER exponents (k_j,l_j); the
Puiseux/Eggers-Wall data of f and g (the genome above) is SHARED. All
four tests below use only (f,g)-genome data, so every verdict transfers
verbatim to all surviving variants unless explicitly noted.

## 1. T1 — Splice diagram / link at infinity

VERDICT: **PASS — and the Seifert/Euler compatibility closes as an exact
identity with all unpinned data cancelling** (sec 1c). One chart subtlety
matters and is recorded (1c-i).

Criteria used (stated in full before applying):
- (EN-1) [Eisenbud-Neumann, Ann. Math. Studies 110, Thm 11.2] A graph
  multilink is fibered iff the multiplicity l_v = sum over link components
  L_i of m_i lk(L_i, S_v) is nonzero at EVERY node v (S_v = virtual
  component at v). Necessary condition applied here with all m_i = 1.
- (EN-2) [EN, splice positivity for germs] The splice subtree of a LOCAL
  germ of an algebraic branch has all edge determinants positive; for a
  Puiseux chain with Newton pairs (p_i, q_i) the consecutive edge
  determinant equals q_{i+1}, so positivity == q_{i+1} > 0.
- (N-3) [Neumann, Invent. math. 98 (1989)] The link at infinity of a
  reduced algebraic curve is determined by the splice diagram computed
  from the Puiseux data at infinity; for a REGULAR (generic) fiber the
  multilink at infinity is fibered (regular links at infinity), so (EN-1)
  positivity at every node is necessary for the template.
- (RH) Riemann-Hurwitz for ghat: Cbar -> P^1 of degree 6 (poles only at
  P_1, P_2, order 3 each), with NO affine ramification: J(f,g) = 1 makes
  dg|_{fiber} nowhere zero on the affine part (dg/dt = -(dx/dt)/f_y along
  the fiber). Hence g(Cbar) = -3 + (1/2) Sum_{finite punctures}(e_p - 1),
  e_p = ord_t(g - c_p) at puncture p.

### 1a. Splice data (engine sec 7)

P_i-branch Newton pairs, affine chart (u = 1/x): (7,2)(3,10)(2,5),
reproducing char exponents 12/42 < 32/42 < 37/42; cabling weights
(a_1,a_2,a_3) = (2, 52, 317). Local chart at [1:0:0] (all 126 y-series
enter P^2 at ONE point, tangent to L_infty; coordinates (1/x, y/x); every
contact shifts by +1): local pairs (7,9)(3,10)(2,5), cabling
(9, 199, 1199). Edge determinants along both P-chains: q_2, q_3 = 10, 5
> 0: PASS. B-arm and x-arm edge determinants are of the same q-form and
are positive for ANY admissible tail (grid increments are positive), so
edge positivity cannot kill the surviving variants either.

### 1b. Node multiplicities l_v (engine sec 8)

l_v = lk(C, curvetta_v) computed by Bezout: lk = deg C * deg gamma_v
minus intersections at infinity in correct local charts. Curvettas:
truncation curves (e.g. at F_s: x^2(y-c0)^7 = eta^7, deg 9).

    node:  root(L_infty)  F_s   G_m   P_i
    l_v:   168            294   2022  4664

All strictly positive: no EN-fiberedness obstruction at any pinned node.
B-internal and x-internal nodes are not pinned; their l_v are finite
sums of positive contact terms minus the same Bezout correction and were
not evaluated (NEEDS-DATA for those nodes only).

### 1c. Seifert/Euler compatibility = the genus balance (engine sec 5)

The link-at-infinity fiber surface Euler characteristic must agree with
the algebraic fiber; in Euler form this is: genus from the degree-genus
formula (tree side) == genus from (RH) (fibration side). With
  SigS = total B-side same-direction contact sum (units 1/42),
  SigU = total x-side contact sum, r_B, r_X = numbers of B-/x-places:
tree side: g = 13861 - delta_Y - delta_X, delta_Y = (T_Y - 126 + 2 +
r_B)/2 with T_Y = 4890 + 126*125 + SigS/42 (the 126*125 is the local
chart +1 shift), delta_X = (SigU + 42*41 - 42 + r_X)/2;
fibration side: g = -3 + [(11844 - SigS)/42 + (5250 - SigU) - r_B -
r_X]/2, using the T2 valuation formulas e_p = n_p(282 - S_p)/42 (B) and
e'_p = n'_p(125 - U_p) (x-side).

**The two sides agree IDENTICALLY: every unpinned symbol cancels and the
constants match exactly** (engine: all five coefficients zero). Closed
form, new pin for ALL surviving branches:

    g(Cbar) = 2763 - (SigS/42 + SigU + r_B + r_X)/2.

This test had full kill power: the constants absorb the pinned contact
table (597/624/504/432 in 1/42 units), both Newton corners, Lambda = 3,
and deg ghat = 6; any one of them off by any amount breaks the identity.
It closes with zero slack.

(1c-i) Chart caveat, recorded for review: contacts must be taken in the
local coordinates (1/x, y/x) at [1:0:0] (resp. (1/y, x/y) at [0:1:0]),
NOT in the affine series chart; the +1 shift contributes
(126*125 + 42*41)/2 = 8736 to the delta ledger, exactly the amount by
which the naive-chart computation fails. A naive-chart reading would
report a spurious kill.

## 2. T2 — Abhyankar-Moh / semigroup arithmetic

VERDICT: **PASS at the poles with zero slack (exact valuation identity);
one auxiliary branch KILLED (x-side slack-1, pi_G = 4); sharp new pins
on the B-side and x-side tails.**

Criteria used:
- (AM-1) [Abhyankar-Moh, J. reine angew. Math. 276 (1975) / semigroup
  paper 1977] For a curve with ONE place at infinity the semigroup
  condition (delta-sequence, n_i delta_i > delta_{i+1}) holds; corollary
  relevant to Jacobian pairs: if J(f,g) in C* and the pair were a
  counterexample, deg f does not divide deg g and vice versa.
  Honest scope: the template fiber has >= 4 places at infinity, so the
  one-place semigroup chain does NOT apply to it directly; per-place
  germ data alone carries no A-M obstruction (any Puiseux germ arises on
  some algebraic curve). What survives at multi-place level is (AM-2).
- (AM-2) (classical, valuation form of J(f,g) = 1 along a fiber) On the
  smooth fiber f = a, dg/dt = -(dx/dt)/f_y and dg/dt = (dy/dt)/f_x for
  any local parameter t. At each place at infinity this pins
  ord_t(f_y) resp. ord_t(f_x) against ord_t(g) — pure arithmetic in the
  contact tree, this is the two-term Abhyankar valuation bookkeeping.
- (AM-3) [Moh, J. reine angew. Math. 340 (1983)] No counterexample with
  max(deg f, deg g) <= 100. (Consistency only.)

### 2a. Pole places: exact pass (engine sec 3)

At P_1 (u-degree 42): sum of contacts of one P_1-series against the
other 125 y-series = (597 + 624 + 504)/42 = 1725/42. With
lc_y(f-a) = gamma x^42(1+..): ord_t f_y = 42(-42 + 1725/42) = -39.
(AM-2) requires ord_t f_y = ord_t(dx/dt) - ord_t(dg/dt) = -43 - (-4)
= -39 given Lambda(P_1) = 3. **Exact match, zero slack** — this couples
the entire pinned contact table to the pole order of g. Independent
crosscheck: g along a P_1-branch by the product formula over g's 189
series (contacts 171@12, 15@32, 3@37, lc_g = gamma_g x^63):
ord_u g = -63 + 2643/42 = -1/14, i.e. Lambda = 3 recovered from g's own
tree. Same at P_2 by the sqrt3-conjugation symmetry. Parity audit:
mu(P_i) = 2278 even, delta(P_i) = 1139 (a branch must have even Milnor
number): PASS.

### 2b. B-side pin (engine sec 4)

For a B-series with same-direction contact sum S_i (5 pairs, units
1/42): ord_u(g - c_p) = (282 - S_i)/42, so a B-place of degree n_p has

    e_p = n_p (282 - S_p)/42,  integer, 1 <= e_p, and <= 6 by the
    degree budget of ghat (per asymptotic value).

Consequences: S_p = 282 - 42 e_p/n_p in [246, 281]; the B-side
same-direction contacts are FORCED to average approx (49..56)/42 per
pair — deeper than the pole depth 37/42. The template's unmodeled
B-tail is not free: its split depths are pinned to a narrow window.

### 2c. x-side pin and a kill (engine sec 4)

For an x-series with contact sum U_i (41 pairs, units 1, all >= 3):
ord_v(g - c'_p) = 125 - U_i, so e'_p = n'_p(125 - U_p) >= 1 forces

    123 <= U_p < 125,  hence  pi_G <= U_p/41 < 125/41 = 3 + 2/41.

**LROOT LR2's slack-1 alternative pi_G = 4 is DEAD** (it would force
U >= 164, i.e. a g-POLE of order >= 39 at every x-place, contradicting
td = 6 = 3 + 3 exhausted at P_1, P_2). The x-side cv vertex is pinned to
pi_G in [3, 3 + 2/41): essentially the slack-0 position. Also
e'_p <= 2 n'_p automatically (contacts >= 3), a new ceiling on the
x-side dicritical multiplicities.

### 2d. Degree-pair conditions (engine sec 10)

168 does not divide 252 (AM-1 corollary): PASS. gcd = 84, type (2,3);
min degree 168 > 100 (AM-3): consistent, outside Moh's verified range.
All of sec 2 uses only the shared genome: transfers to all surviving
variants.

## 3. T3 — BMY / log-surface ledger

VERDICT: **NEEDS-DATA for the full (K+D)^2 <= 3 e_orb comparison; the
Euler-characteristic shadow of the test (delta/genus ledger) is fully
computable and PASSES identically; integrality/feasibility of the
ledger PASSES with explicit witnesses.**

Criteria:
- (BMY-1) [Miyaoka, Math. Ann. 268 (1984); Kobayashi, Math. Ann. 289
  (1990), orbifold form] For a log-canonical pair (X, D), D reduced NC,
  with kappa(K_X + D) >= 0: (K_X + D)^2 <= 3 e_orb(X \ D).
  Honest scope: X \ D = C^2 has kappa = -infty, so the inequality does
  NOT apply to the plain compactification; the Orevkov-style application
  needs the auxiliary log surface built from the resolved pencil of f
  (vertical boundary + sections), and building THAT graph requires the
  B-internal and x-internal resolution data — exactly the unpinned tail
  of the template. No honest verdict is possible on the pinned skeleton
  alone; what IS computable is the Euler-number arithmetic that any such
  surface must satisfy, namely the delta/genus ledger.
- (BMY-2) degree-genus + delta additivity over the two singular points
  at infinity (Serre; delta = (T - n + r)/2 per point, validated on
  (t^2,t^3), (t^3,t^5), (t^4, t^2+t^3) in-engine).

### 3a. What was computed (engine secs 2, 5, 9)

Pinned local data at [1:0:0]: delta(P_i) = 1139, (P_1 . P_2) = 2388,
(P_i . B) = 2268 each, local Newton pairs (7,9)(3,10)(2,5) per P-branch:
the input for the (future) full dual graph. Ledger identity: sec 1c
(shared with T1): the delta/genus balance closes identically; the
resolution-graph Euler numbers cannot produce a contradiction at
chi-level no matter how the B/x-tails resolve. Feasibility with all
integrality/budget constraints: nonempty; witnesses include
(r_B, e_B, r_X, e'_X, g) = (1,1,6,2,0) [rational fiber, genus 0] and
(1,3,6,2,1), (2,1,6,2,0), etc.

### 3b. Missing data for a decisive T3

(i) B-side place partition (r_B in {1..6}, degrees in 7Z) and split
depths (S_p already windowed by T2b); (ii) x-side partition r_X and
split heights (windowed by T2c); (iii) then a finite continued-fraction
computation gives the full dual graph, K^2, e, and (BMY-1) on the
fibered log surface. Given (i)+(ii) this is a mechanical extension of
cases/classical_tests.py.

## 4. T4 — Jelonek asymptotic variety

VERDICT: **PASS (consistent), with exact geometric degree mu(F) = 6 and
a quantified non-properness excess >= 6.**

Criteria:
- (J-1) [Jelonek, Ann. Polon. Math. 58 (1993)] For a dominant polynomial
  F = (f,g): C^2 -> C^2 the non-properness set A(F) is empty or a curve;
  every irreducible component is the image of a polynomial map C -> C^2
  (hence a rational curve with ONE place at infinity). A Keller
  counterexample is non-proper (a proper Keller map is invertible), so
  A(F) is a nonempty curve.
- (J-2) [Jelonek, degree bound; Testing sets for properness, 1999-2002]
  deg A(F) <= (deg f * deg g - mu(F)) / min(deg f, deg g), mu(F) =
  geometric degree. (Bound form quoted from memory; only used as a
  sanity ceiling, nothing below depends on its exact shape.)

### 4a. Computations (engine secs 6, 9)

mu(F) = 6 EXACT by Bezout with infinity corrections: 168*252 = 42336;
(C.{g=c}) at [1:0:0] = 126*252 - 6 = 31746 (the -6 is the two g-poles,
order 1/14 in u each over 42 conjugates); at [0:1:0] = 42*252 = 10584;
affine remainder 42336 - 31746 - 10584 = 6. Note mu(F) = 6 = td =
deg ghat: three independently defined 6's agree — a real consistency
hit, not bookkeeping.

Structure of A(F) implied by the template: at least two component
families — B-side (punctures with (f,g) -> (a, c_p(a)), Sigma-lambda = 2
charge) and x-side (psi = 2 charge); each carries multiplicity drop
e_p >= 1 with Sum_{p over a value} e_p <= mu(F) = 6 (per-value swallow
ceiling). (RH) forces the TOTAL excess Sum(e_p - 1) = 2g + 6 >= 6: at
least 6 units of asymptotic multiplicity excess, so A(F) has either
several components or high-multiplicity ones — consistent with, and now
quantifying, the lambda/psi charge bookkeeping. Feasible assignments
exist (engine sec 9), e.g. one B-place with e = 1 plus six x-places with
e' = 2 gives g = 0 (rational fiber). (J-2) ceiling 251: passes with
enormous slack, no kill possible from it here.

Future leverage: each A(F) component is a ONE-place rational curve, so
(AM-1) applies to the COMPONENTS; once R1/R5 pins the component degrees
(from the c_p(a) correspondence), the A-M semigroup chain on A(F) is a
fresh kill test not run here.

## 5. Cross-test synthesis and honest gaps

1. **No classical kill on the shared genome.** All four tests close on
   the pinned data; the sharpest one (genus/Seifert balance, sec 1c) is
   an exact identity with every unpinned symbol cancelling — the same
   zero-slack behavior the coefficient sweep (TEMPLATE sec 2c) showed.
   The template survives classical machinery it was never engineered
   against; this is genuine (the constants had full kill power).
2. **One auxiliary kill:** the x-side slack-1 position pi_G = 4 is dead
   (T2c); the x-side cv vertex is squeezed into [3, 3 + 2/41).
3. **New pins for the R1/R5 endgame:** B-side split-depth window
   S_p in [246, 281] (units 1/42, avg pair contact ~50/42); x-side
   U_p in [123, 125); the genus formula g = 2763 - (SigS/42 + SigU +
   r_B + r_X)/2 with g = -3 + Sum(e_p - 1)/2 >= 0 an integer; e-budget
   <= 6 per asymptotic value.
4. **Variant transfer:** every computation above uses only f's contact
   tree, the Newton corners, and g's pole data — all shared by the
   (1,2), (2,3)-chain, (2,5)-chain variants (they differ only in
   h-tower exponents). All verdicts, the pi_G = 4 kill, and the pins
   transfer verbatim.
5. **Honest gaps:** (i) T1 fiberedness at B/x-internal nodes not
   evaluated (data-free); (ii) T3's full log-BMY needs the B/x
   resolution tails (sec 3b); (iii) (J-2)'s exact constant quoted from
   memory (harmless here); (iv) (N-3) fiberedness-of-regular-links is
   used only as motivation — every applied inequality is from (EN-1),
   (EN-2), (RH), Bezout, or Serre's delta formula.
6. Assumptions inherited from the template, stated: corner monomials
   x^42 y^126 (f) and x^63 y^189 (g) present; off-grid dead-stretch
   coefficients vanish (else Q changes); B place degrees in 7Z ("6 per
   direction" + denominator-7 argument); LROOT LR2 for the x-side;
   td = 6 exhausted at P_1, P_2 (g finite at B- and x-places).

## 6. Reproduction

    cd cases && python3 classical_tests.py   # 22 checks, 0 FAIL, exact
