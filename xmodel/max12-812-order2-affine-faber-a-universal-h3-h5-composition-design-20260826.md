# Delayed-load affine-Faber `A`: universal `H3/H5` composition candidate

Date: 2026-08-26

Status: **EXACT HAND IDENTITY SUGGESTED BY THE COMPLETE SOURCE ROWS;
PRODUCER/VALUATIVE REVIEW REQUIRED.  NO `A`-FACE EXCLUSION YET.**

## 1. Purpose

The empty relative-order-six face does not by itself cover
`6<q<15/2`: at the first quadratic kernel grade, a delayed load-normal jet
can cancel the even K2 obstruction.  Enumerating every rational `q` is
unnecessary if the complete rows satisfy the following uniform grade-45
composition.

Work on the repeated-root `A` chart and on `D(p*m*k10_0)`.  After the exact
moving-discriminant coordinate change, let `X(s),Y(s)` be the two transverse
K2-kernel series and let

```text
M(s)=m+m1*s+m2*s^2+...,
W(s)=M(s)*X(s)*Y(s).
```

Assume `ord_s(X),ord_s(Y)>=6`, allowing either series to be zero.  Retain
the complementary `R,S` series, all moving `a,e,M` tangents, every delayed
load jet, and every target.  No leading mixed-face equation is substituted
in the identities below.

## 2. Inverse-Faber rows

For the seven ordinary source rows `P1,...,P7`, put `b=4*a` and use the exact
inverse connection

```text
H3 = P3-(b/2)*P2+(5*b^2/32-e/4)*P1,

H5 = P5-b*P4+(21*b^2/32-3*e/4)*P3
       +(-5*b^3/16+3*b*e/4)*P2
       +(195*b^4/2048-45*b^2*e/128+5*e^2/32)*P1.
```

Here `ord_s(b)=5`.  Along a source arc, every coefficient of every `P_i`
vanishes.  Therefore all positive-`b` connection terms that could reach
absolute grade 45 multiply already-zero predecessor coefficients.  At that
grade the effective combinations are the `b=0` parts, but this conclusion is
modulo the raw predecessor source ideal, not a frozen-center specialization.

## 3. Candidate exact convolution identity

Direct collection from the complete grade-42--45 source rows gives, modulo
the source coefficients of lower absolute grade,

```text
[s^(30+n)] H3 = -(3/8)*[s^n]W                  for n=12,13,14,

[s^45] H3      = -(3/8)*[s^15]W -(1/16)*m^3,
[s^45] H5      =  (3/8)*p*[s^15]W.
```

The first line is visible coefficientwise in the frozen loaded-kernel
producer.  For example, subtracting `(e/4)P1` from `P3` cancels every
complement and moving-tangent term, leaving exactly the convolution
`-(3/8)MXY`.  In `H5`, the combination

```text
P5-(3*e/4)*P3+(5*e^2/32)*P1
```

cancels the same complement terms.  Its kernel contribution is
`(3/8)e*MXY`; predecessor vanishing reduces the grade-15 coefficient to
`(3/8)p*[s^15]W`.  The cubic terms
`-3*p*m^3/64` from `P5` and `+3*p*m^3/64` from `-(3e/4)P3` cancel exactly.
Delayed-load and target jets occur in the ordinary rows but have no surviving
component in these two inverse analytic rows at this grade; a producer must
verify this from the frozen source rather than assume parity.

Since the source equations give the first line equal to zero, the lower
coefficients `[s^12]W,[s^13]W,[s^14]W` vanish.  The grade-45 `H5` equation
then forces `[s^15]W=0` on `D(p)`, and the grade-45 `H3` equation becomes
`-m^3/16=0`, impossible on `D(m)`.

## 4. Valuative consequence if verified

The identity is independent of the first kernel order `q` once `q>=6`:

- `q=6` is included, although it already dies at the loaded grade-42 face;
- for `6<q<15/2`, it bypasses the genuine mixed K2/load-normal predecessor
  without calling that predecessor empty;
- at `q=15/2`, it specializes to the preregistered half-weight formulas;
- for `q>15/2`, `[s^15]W=0` automatically and `H3` is the ordinary cubic
  unit.

After a ramified base change `s=t^e`, the same convolution statements use
indices `12e,...,15e`; no integrality of `q` is needed.  A complete proof
must establish that the moving-discriminant/K2 coordinates form a two-sided
formal chart for every retained source arc, and that no term of kernel degree
three or higher enters through grade 45 when `q>=6`.

The separate `q<6` homogeneous initial face must still be covered by its own
complete-source unit certificate.  The locus `m=0`, other load slopes,
`D=0`, terminal/Taylor receivers, total fan coverage, order two, maximum
twelve, and JC2 are not addressed.

## 5. Required acceptance client

1. Rebuild all seven frozen source rows with formal `X,Y` coefficients whose
   product is retained through relative grade 15, arbitrary `R,S,a,e,M`, and
   all load/target jets capable of reaching absolute grade 45.
2. Form the exact `H3,H5` connection inside the compiler and reduce only by
   the raw lower source coefficients.
3. Emit the three displayed identities over exact Q; use a good prime only
   as a software control.
4. Supply a ramified convolution proof and a two-sided coordinate/coverage
   argument.  Hostile review must attack higher kernel powers, load-normal
   leakage, fractional `q`, and use of predecessor equations.

Until all four gates pass, this file is a design and no whole-`A` theorem may
consume it.
