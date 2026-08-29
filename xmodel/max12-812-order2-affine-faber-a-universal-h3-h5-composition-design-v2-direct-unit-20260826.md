# Delayed-load affine-Faber `A`: direct `E*H3+H5` unit addendum

Date: 2026-08-26

Status: **CONTROLLING STRENGTHENING OF DESIGN SHA `d7dcd91c...`;
COEFFICIENTWISE HAND CHECK AGAINST THE FROZEN EXACT-Q ROWS.  COMPLETE-SOURCE
AWS CERTIFICATE AND VALUATIVE COVERAGE REVIEW PENDING.**

## Stronger raw truncation

Use the notation and exact inverse-Faber rows of the V1 design.  In the
moving repeated-root chart, direct coefficient comparison against all seven
frozen loaded-kernel source rows gives the raw congruences

```text
H3 = -(3/8)*s^30*M*X*Y -(1/16)*s^45*M^3  (mod s^46),
H5 =  (3/8)*s^30*E*M*X*Y                 (mod s^46),
```

where `E=p+O(s)`, `M=m+O(s)`, and `ord_s(X),ord_s(Y)>=6`.  These are stronger
than the V1 coefficient-by-coefficient predecessor reduction.  Every
complementary `R,S` term, moving-center/discriminant tangent, and eligible
delayed-load/target term cancels in the inverse analytic rows; no mixed-face
equation is substituted.

Consequently the single exact source-row combination satisfies

```text
[s^45](E*H3+H5) = -(1/16)*p*m^3.                    (1)
```

The `MXY` series cancels identically before coefficient extraction.  Since
`H3,H5` are exact lower-unitriangular combinations of the ordinary Faber
source rows, a source solution makes the left side of (1) zero.  It is a unit
on `D(p*m)`.  Thus, once complete-source emission and chart coverage are
certified, no case split by the coefficient `[s^15](MXY)` is necessary.

## Consequence and remaining gate

Equation (1) is uniform for every rational first transverse order `q>=6`
after ramification.  It includes the loaded `q=6` equality, the genuine mixed
K2/load-normal interval `6<q<15/2`, the half-weight `q=15/2` tie, and the
late-kernel `q>15/2` slice.  The mixed predecessor is allowed to be nonempty;
the direct grade-45 source combination kills any prolongation of it.

The theorem gate is now coverage, not another Groebner split:

1. reproduce both raw congruences and (1) from the complete frozen source on
   exact Q, with a good-prime software control;
2. prove the moving-discriminant/K2 coordinates are two-sided for arbitrary
   ramified source arcs on the repeated `A`, `D(p*m*k10_0)` chart;
3. show kernel-degree-three and higher terms cannot reach grade 45 when
   `q>=6`;
4. cover `q<6` by its separate homogeneous initial-face certificate.

The locus `m=0`, `D=0`, other load slopes, terminal/Taylor receivers, total
fan coverage, order two, maximum twelve, and JC2 remain outside this design.
