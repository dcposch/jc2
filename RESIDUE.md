# RESIDUE.md — Is R_{k,d2} a residue?

Subject: R_{k,d2} = sum_j (-1)^j C(j,k+2) a2^(2d2-j) b_j (from SURPLUS-EXT.md).
Question: is R a residue in a precise sense (Grothendieck residue / constant-term
extraction / Koszul obstruction), and does that give a coordinate-free proof?

## 0. Setup and data (from repo)
Sources read: SURPLUS-EXT.md (§1.2-1.3, §2 Steps 3-4), SURPLUS.md (block
cascade, scope map), LEMMA.md §3 (tower/valuation reading), paper1/main.tex
§6 (conj:R).
- Block ODEs (units a1=c1=1): (I) AC' - kA'C = 1 (col k+1);
  (II) AE' - (k+1)A'E = -(2BC' - kB'C) =: -G (col k+2).
  A = P col 1 (deg d2, A(0)=1), B = P col 2 (y^{d2}..y^{2d2}, coeffs b_j),
  C = Q col k (val 1), E = Q col k+1 (val d2+1... val >= 3 at d2=2).
- On binomial locus A = 1 + a2 y, z := 1 + a2 y, beta(z) := B(y(z)):
  E = -(1/a2) z^{k+1} int_1^z [2 beta w^{-3} - beta' w^{-2} + beta' w^{-(k+2)}] dw.
  Obstruction = coefficient of w^{-1} in beta'(w) w^{-(k+2)}, i.e.
  beta'_{k+1} = (k+2) beta_{k+2} (z-basis coeff). Repo asserts
  beta'_{k+1} ≐ R_{k,d2} = sum_{j=k+2}^{2d2} (-1)^j C(j,k+2) a2^{2d2-j} b_j
  up to unit * a2-power. NOTE b_j here = P-col-2 coefficient a_{(2,j)}.
- KEY OBSERVATION (starting point): R is BY CONSTRUCTION a residue at w=0
  of the 1-form beta'(w) w^{-(k+2)} dw — the repo's derivation already says
  so. The real question is whether this lifts to a residue of a form built
  COORDINATE-FREELY from (P,Q) themselves (interp (a)/(b)), not from the
  solved column's integrand. Also: Res_{w=0} beta' w^{-(k+2)} dw =
  Res_{w=infty} too (sum of residues = 0 on P^1, only poles 0, infty)?
  beta' has deg 2d2-1, so at infty pole order (2d2-1)-(k+2)+2; nonzero
  residue at infty iff k+1 <= 2d2-1: SAME dichotomy. To check.
- Proved cells with exact data: (2,2) [R = b4 = a6, obstruction
  -(1/5)a2^2 a6]; (2,3) [R = a2^2 b4 - 5 a2 b5 + 15 b6, unit a2^3/21];
  (2,4) [R4, unit -a2^4/55]; certified (3,3) [-a2^6/99], (4,3)
  [2a2^9/1001], (3,4) [-a2^8/364]; (5,3) empty sum, all outer vanish.
- Machine layer to reuse: cases/surplus_ext.py wide_setup (general (k,d2)
  column-ODE solve, exact Fractions).

## 1. Explicit R in proved cells
Machine: cases/residue_check.py (exact Fractions; reuses surplus_ext.py;
run 2026-08-07, exit 0, 48 checks OK). T0 anchors the direct binomial-locus
solve against the repo's general-solve-then-restrict (binom_outer) at
(2,2),(2,3),(3,3): identical extras.
Cells computed (11): (2,2),(2,3),(2,4),(3,3),(4,3),(3,4),(5,3) [repo grid]
+ (4,4),(5,4),(2,5),(3,5) [NEW, beyond repo grid]. Surviving outer extra
on the binomial locus, all cells (T5, exact):
  extra_0 = (-1)^{k+(k+1)(d2-1)} * (k+2)/C((k+1)d2, k+1) * a2^{(k-1)d2} * R
  (2,2): -(4/20) a2^2 b4        = -(1/5) a2^2 a6      [= repo theorem]
  (2,3): +(4/84) a2^3 R         = (a2^3/21) R          [= repo]
  (2,4): -(4/220) a2^4 R        = -(a2^4/55) R         [= repo]
  (3,3): -(5/495) a2^6 R        = -(a2^6/99) R         [= repo]
  (4,3): +(6/3003) a2^9 R       = (2 a2^9/1001) R      [= repo]
  (3,4): -(5/1820) a2^8 R       = -(a2^8/364) R        [= repo]
  (5,3): R = empty sum, extra_0 = 0                    [= repo]
  NEW  (4,4): -(6/C(20,5)) a2^12 (a2^2 b6 - 7 a2 b7 + 28 b8)
  NEW  (5,4): -(7/C(24,6)) a2^16 (-a2 b7 + 8 b8)
  NEW  (2,5): +(4/C(15,3)) a2^5 (-5a2^5 b5 + 15a2^4 b6 - 35a2^3 b7
              + 70a2^2 b8 - 126a2 b9 + 210 b10)
  NEW  (3,5): -(5/C(20,4)) a2^10 R_{3,5}
DEFINITION CORRECTION found at (2,5): the sum must run
j = max(k+2, d2)..2d2 (b_j exists only for j >= d2); the repo's lower
limit k+2 is correct only when k+2 >= d2, which held on its whole grid.
The mystery unit denominators 5,21,55,99,1001,364 are (k+2)/C((k+1)d2,k+1)
— the moment mu(n0) of the residue functional at the top pivot (see §4b).

## 2. Interpretation (a): Grothendieck/global residue of a rational form
CANDIDATE (a1). Let P = xA + x^2 B (+ higher cols), A = (P/x)|_{x=0} the
edge polynomial on the toric boundary divisor D = {x=0} (origin end of the
strip), y0 a simple root of A (binomial locus: y0 = -1/a2, the unique point
of {P=0} n D). Q = x^k C + x^{k+1} E + ... with C the solved col k. Claim:
  Res2 := Res_x Res_y [ dP ^ dQ / (x^{k+2} A^{k+2}) ]  (iterated at (0,y0))
       ?= (k+2) (-1)^k a2^{-2d2-1} R_{k,d2},
INDEPENDENT of E and of deeper columns of P and Q (their contributions are
exact forms / wrong x-order). Refutation control (a2-variant): the naive
  dP ^ dQ / P^{k+2}
should give iterated residue == 0 identically (omega = d(-(1/(k+1))
P^{-(k+1)} dQ) is exact), i.e. pure P,Q-power denominators canNOT see R;
the toric factor x^{k+2} (boundary divisor) and edge polynomial A are
essential. TEST: T3a (identity Jac(P,x^k C) = x^k + x^{k+1} G), T3b
(E-part (AE'-(k+1)A'E)/A^{k+2} = (E/A^{k+1})' has residue 0), T3c
(P^{k+2}-variant total residue == 0).
VERDICT: VERIFIED (T3a,b,c OK on all 11 cells). (a1) holds: R is the
iterated Grothendieck residue of dP ^ dQ at the boundary point
p* = {P=0} n {x=0}, against the pair (x^{k+2}, A^{k+2}); by T3b it is
independent of Q col k+1 (any E: exact form) and of deeper columns of
both polynomials (wrong x-order) — so the FULL pair (P,Q), any strip
lengths, can be used in the numerator. The naive dP^dQ/P^{k+2} is
REFUTED exactly as predicted: its total residue is 0 identically
(the form is d(-(1/(k+1)) P^{-(k+1)} dQ)); pure powers of P,Q cannot
carry R — the toric boundary factor x^{k+2} is what breaks exactness.

## 3. Interpretation (b): constant-term / CT extraction identity
CANDIDATE (b1, 1-variable residue; the core formula). With G := 2BC'-kB'C
= (Jac(P, x^k C) - x^k)/x^{k+1} (Jacobian connection):
  Res_{y=y0} [ G(y) / A(y)^{k+2} ] dy  ?=  (k+2)(-1)^k a2^{-2d2-1} R_{k,d2}.
Equivalently CT form: R ≐ [w^{k+1}] beta'(w) = coefficient extraction in
w = A(y) (shifted variable), beta = B as function of w.
CANDIDATE (b2, residue theorem / CT at infinity): the only poles of
G A^{-(k+2)} dy on P^1 are y0 and infinity, so
  Res_{y0} = -Res_{infty}:  R ≐ -(coeff of y^{-1} of the Laurent expansion
of G A^{-(k+2)} at infinity) — a CT identity in the pair data alone.
TEST: T1 (exact, cells (2,2),(2,3),(2,4),(3,3),(4,3),(3,4),(5,3)); T2.
VERDICT: VERIFIED (T1, T2 OK on all 11 cells, with the max(k+2,d2)
lower-limit correction of §1 at (2,5)). Exact identity, every cell:
  Res_{y=-1/a2}[(2BC'-kB'C)/A^{k+2}] dy = (k+2)(-1)^k a2^{-2d2-1} R_{k,d2},
and Res_{y0} = -Res_infty (residue theorem on P^1; the CT-at-infinity
path is an independent binomial-series computation). The obstruction
dichotomy k+1 <= 2d2-1 (paper1 §6) is the degree count for the pole of
beta' w^{-(k+2)} at w = infty. Jacobian connection: G is literally
(Jac(P, x^k C) - x^k)/x^{k+1} (T3a), so R ≐ residue of the Jacobian
defect against A^{k+2} — the classical Jacobian-as-residue, localized
at the strip's boundary root.

## 4. Interpretation (c): Koszul / syzygy obstruction
CANDIDATE (c1). L := A d/dy - (k+1)A' = ad-operator E -> [xA, x^{k+1}E]
/ x^{k+1} on column spaces (source: E-support y^{d2+1}..y^{(k+1)d2};
target: eq window). The moment functional mu(y^n) := Res_{y0}[y^n A^{-(k+2)}
dy] = (-1)^{n-k-1} C(n,k+1) a2^{-(n+1)} satisfies mu o L = 0 (row identity
m C(m-1,k+1) = (m-k-1) C(m,k+1)) — mu spans the G-reachable part of
coker(L)^*, and the obstruction system on the binomial locus is EQUIVALENT
to mu(G) = 0. TEST: T4 (mu.L == 0 as exact matrix identity; coker rank;
second cokernel functional unreachable by G via degree count).
VERDICT: VERIFIED (T4 OK on all 11 cells; a2 specialized to 3/7 and 5/3
for the exact rank computations, mu o L = 0 checked as the integer
identity m C(m-1,k+1) = (m-k-1) C(m,k+1), all m in the window — hand-
provable, so this step is a general theorem, not per-cell). Findings:
L is injective; coker on the window is 2-dimensional, spanned by mu and
one functional supported in degrees > deg G (invisible to every
inhomogeneity); so the block obstruction on the binomial locus is
EXACTLY mu(G) = 0, one residue condition. This is the precise syzygy
statement: R generates the annihilator of im(ad_{xA}) restricted to the
reachable window — a cokernel-of-Koszul-differential interpretation
with ad_{xA}(x^{k+1}E) = [xA, x^{k+1}E] the (1-variable shadow of the)
Koszul/Lie differential of the near-origin block.

## 4b. DERIVED (paper calc, to machine-verify): uniform outer theorem
Chain S1-S5 (see §5) predicts, for ALL k,d2 >= 2 on the binomial locus:
extras t>=1 == 0 by pure degree count (deg G = 2d2+k-1 < (k+1)d2 + 1);
surviving extra_0 = a2 (k+1)(d2-1) e_top; and applying mu to the solved
system: extra_0 = mu(G)/mu(n0), n0 = (k+1)d2, giving CLOSED FORM
  extra_0 = (-1)^{k+(k+1)(d2-1)} * (k+2)/C((k+1)d2, k+1) * a2^{(k-1)d2} * R.
Checks against ALL repo units: 1/5 (2,2) [C(6,3)=20, 4/20], 1/21 (2,3)
[4/84], 1/55 (2,4) [4/220], 1/99 (3,3) [5/495], 2/1001 (4,3) [6/3003],
1/364 (3,4) [5/1820]; signs all match (-1)^{k+(k+1)(d2-1)}. The mystery
denominators are C((k+1)d2, k+1): binomial from the moment mu(n0).
VERDICT: VERIFIED — T5 OK on all 11 cells (including the 4 new ones).
Proof chain, each step GENERAL (not per-cell):
 S1 deg G <= 2d2+k-1 < (k+1)d2, since (k-1)(d2-1) > 0  [degree count]
 S2 hence extras t>=1 see neither G nor E: identically 0
 S3 extra_0 = G_{n0} + a2(k+1)(d2-1) e_top = a2(k+1)(d2-1) e_top
 S4 apply mu to the solved system: mu(L E_solved) = 0 (interp (c)),
    equations < n0 hold, so extra_0 * mu(n0) = mu(G)
 S5 mu(G) = (k+2)(-1)^k a2^{-2d2-1} R  [interp (b), Step-3 integrand:
    exact part 2 beta w^{-3} - beta' w^{-2} contributes 0, residue term
    beta'_{k+1} = (k+2) beta_{k+2}, beta_{k+2} = (-1)^k a2^{-2d2} R]
Every step is either a two-line general argument (S1-S4, S5's beta
expansion) or the verified exactness lemma; so this is a UNIFORM
THEOREM for all k >= 2, d2 >= 2 at depth 2, machine-verified at 11
cells. It upgrades paper1 conj:R's outer half from per-cell certificate
to closed form, explains all unit factors, and yields NEW exact outer
certificates at the open cells (4,4), (5,4), (2,5), (3,5).

## 5. Coordinate-free conjecture (and what it would prove)
STATEMENT (coordinate-free residue form of the obstruction). Let (P,Q)
be a reduced strip pair of type (k,d2) satisfying (i), gap-killed, with
x | P; let D = {x=0} be the toric boundary divisor at the origin end,
A := (P/x)|_D the edge polynomial of P on D. On the rigidity locus
(deg A <= 1, i.e. {P=0} meets D in at most one point p*, transversally):
the depth-2 near-origin block is solvable iff
    Res2_{p*} [ dP ^ dQ / (x^{k+2} A^{k+2}) ] = 0,
where Res2 is the iterated (Grothendieck) residue at p*, Q may be taken
with FULL support (independence of col k+1 and deeper columns: §2), and
the value equals (k+2)(-1)^k a2^{-2d2-1} R_{k,d2}. If A has no root on D
(a2 = 0), there is no residue and no obstruction — matching the {a2=0}
branch of conj:R. Conjecture conj:R thus REDUCES to its rigidity half:
"the inner column forces deg A <= 1". Residue reformulation of that
half too: (I) solvable in C with val >= 1 iff all local residues of
dy/A^{k+1} at roots of A vanish AND the valuation normalization holds;
perfect powers A = (1+uy)^delta pass the residue test (single pole,
sum-of-residues) but fail the valuation — explaining exactly why the
repo's divisibility argument must carry both halves (squarefreeness +
divisibility). Not closed here; honest status: open as before.
BEYOND THE GRID. Proved uniformly by §4b: the outer half at ALL
(k,d2), k,d2 >= 2, depth 2 — no more per-cell certificates; empty-sum
rule k+2 > 2d2 <=> no obstruction (k>=3,d2=2 theorem is its shadow).
NOT removed: the strip hypothesis (column/window structure and gap-kill
are load-bearing in S1-S4), the gap condition (ii), the rigidity half,
and depth >= 3. PREDICTION for depth D >= 3: the D-th column's operator
is ad_{xA} at weight k+D with cokernel functional Res[ . A^{-(k+D+1)} dy],
so each deeper column should contribute one residue functional
R^{(D)} ≐ Res_{p*}[dP ^ dQ / (x^{k+D+1} A^{k+D+1})] — consistent with
SURPLUS.md's observed "one torus-solvable leftover per deeper column";
untested here, proposed as the next check.

## 6. Verdict
REAL STRUCTURE, not coincidental shape. Three mutually consistent
formalizations all verify exactly on 11 cells (7 repo + 4 new):
(b) R ≐ Res_{y0}[(Jac(P,x^kC)-x^k)/(x^{k+1} A^{k+2})]dy, with CT/
    at-infinity form via the residue theorem — the alternating-binomial
    shape IS the residue expansion (w-1)^j |-> (-1)^{j-k-2} C(j,k+2);
(a) equivalently an iterated Grothendieck residue of dP ^ dQ at the
    point where {P=0} meets the toric boundary {x=0}, twisted by the
    boundary equation — and provably NOT expressible with pure P,Q
    powers (dP^dQ/P^{k+2} is exact: residue 0);
(c) equivalently the generator of the cokernel pairing of ad_{xA} on
    the block window (syzygy/Koszul reading), which is what makes the
    elimination collapse to ONE functional.
The payoff is not just interpretation: the S1-S5 chain turns the
per-cell "outer identity" into a uniform closed-form theorem
  extra_0 = (-1)^{k+(k+1)(d2-1)} (k+2)/C((k+1)d2,k+1) a2^{(k-1)d2} R_{k,d2}
for all k,d2 >= 2, explaining every unit factor in SURPLUS-EXT §1.3 and
extending exact outer certificates to (4,4),(5,4),(2,5),(3,5). Limits,
honestly: rigidity half of conj:R still open (residue view reformulates
but does not close it); strip + gap hypotheses still required; depth
>= 3 untouched (prediction stated in §5). One repo correction: R's sum
starts at j = max(k+2, d2), visible first at (2,5).

## 7. Files
- cases/residue_check.py — all tests, exact arithmetic (exit 0 = OK).
- RESIDUE.md (this file).
