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
(TBD: exact values from repo data, cases/residue_check.py)

## 2. Interpretation (a): Grothendieck/global residue of a rational form
(TBD: statement, test, verdict)

## 3. Interpretation (b): constant-term / CT extraction identity
(TBD: statement, test, verdict)

## 4. Interpretation (c): Koszul / syzygy obstruction
(TBD: statement, test, verdict)

## 5. Coordinate-free conjecture (if any interpretation verifies)
(TBD)

## 6. Verdict
(TBD: real structure vs coincidental shape)
