# Bounded primary-source audit of the polynomial Abel atom

Status: no external theorem found that excludes the polynomial solutions
required by the K16 atom. This note records exact failures of applicability,
not a claim that the literature contains no such theorem. No CAS was used.
The formulas compared are structural-notes.md §§4A--4B as read on 2026-09-05.

## 1. The b3=0 equation is not the equivariant subclass

Put

\[
 a=\frac{3x^3C^2}{4y^2},\quad
 s=B-2a,\quad R=\frac{a^2}{3}-Ba-\frac{3x\kappa}{y}.
\]

The equation is

\[
 2xww'=w^2+s w+R,
 \qquad B\kappa\ne0,\quad w(0)=-B.
 \tag{1}
\]

Llibre--Valls, *Polynomial Solutions of Equivariant Polynomial Abel
Differential Equations*, Advanced Nonlinear Studies 18 (2018), 537--542,
[Theorem 2 and equations (3)--(4)](https://doi.org/10.1515/ans-2017-6043),
treats the second-kind equation
`a(x)y y'=b0(x)+b2(x)y^2` and proves a sharp upper bound of seven polynomial
solutions. The general second-kind equation in their equation (3) has a
linear term; the theorem assumes that this term vanishes, so that changing
the sign of the dependent variable preserves solutions. Our linear term
is `s=B-2a`, whose constant term is the nonzero number B. Thus the theorem
does not apply. Its proof's substitution `z=y^2` produces a linear ODE
only in the equivariant subclass. Even a solution-count bound would not
exclude the single polynomial solution at issue here.

This is an exact hypothesis failure, not merely a mismatch in notation.
Translating w to complete a square changes the derivative coefficient
from w to a translated variable plus a nonconstant term; it cannot be
discarded when comparing equations.

## 2. Reciprocal substitution does not reach polynomial first-kind data

Bravo--Calderon--Fernandez--Ojeda,
[*Rational Solutions of Abel Differential Equations*](https://arxiv.org/pdf/2109.07853),
arXiv:2109.07853, studies `u'=A(x)u^3+B(x)u^2` with A,B polynomials.
Proposition 2.1 identifies invariant curves linear in u with a polynomial
divisibility equation. Theorem 2.12 bounds the number of rational solutions;
the Darboux-integrability results require sufficiently many invariant
curves. These results do not exclude one rational solution.

For (1), `u=1/w` gives instead

\[
 u'=-\frac{u}{2x}-\frac{s}{2x}u^2-\frac{R}{2x}u^3.
 \tag{2}
\]

The linear term has half-integral residue. Removing it by `x=z^2`,
`v=z u(z^2)`, yields

\[
 \frac{dv}{dz}
 =-\frac{s(z^2)}{z^2}v^2-\frac{R(z^2)}{z^3}v^3.
 \tag{3}
\]

The quadratic coefficient has the nonremovable displayed term `-B/z^2`,
and the cubic coefficient has `3*kappa/(y*z)`. They are Laurent
polynomials, not the polynomial coefficient data of the cited theorem.
The transformed solution is rational but the coefficient-ring hypothesis
fails. No extension from polynomial to Laurent coefficients is asserted.

## 3. Exact Darboux graph, but no first integral from the two visible curves

Equation (1) is the invariant graph equation for the polynomial vector
field on `(x,v)`

\[
 \mathcal D=2xv\partial_x+(v^2+s(x)v+R(x))\partial_v.
\]

If w is a polynomial solution, direct polynomial division gives

\[
 \mathcal D(v-w)
 =(v-w)\bigl(v+s+w-2xw'\bigr).
 \tag{4}
\]

Thus `v-w` is a Darboux polynomial. Also `x` is a Darboux polynomial
with cofactor `2v`. There is no nontrivial constant linear relation
between these two cofactors: its v coefficient would force
`2*lambda+mu=0`; its remaining part would force
`mu*(s+w-2xw')=0`. If mu were nonzero, equation (1) would then give R=0,
contrary to its nonzero x coefficient `-3*kappa/y`. Hence these two
curves alone supply no Darboux first integral of the form
`x^lambda*(v-w)^mu`. Further invariant curves or a special integrability
identity would be a new input.

## 4. The full atom also has an ordinary polynomial second-kind form

This is an elementary comparison transformation, derived by substitution,
not an existence result. Use structural §4B notation

\[
 r=b^2/4,\quad K=x^2C-yb,\quad
 A=\frac{3x^3C^2}{4y^2},\quad D=\frac{3bxC}{2y},
 \quad \eta=W'(0).
\]

Set `v=xW-r`, `S=B-2A+D` and

\[
 \begin{aligned}
 \mathcal R(x)={}&x^2\left[
 \frac{A(A-D)}3-B(A-D)-\frac{b\eta K}{2y}-B\eta x
 \right]\\
 &+rx(D-3B)-3r^2.
 \end{aligned}
\]

Then structural equation (F3), multiplied by x^2 and simplified, is

\[
 \boxed{2xvv'=3v^2+xSv+\mathcal R(x).}
 \tag{5}
\]

In the simplification, `2v(v+r)+(v+r)^2-4r(v+r)=3v^2-3r^2`;
the remaining r-linear terms give `rx(D-3B)`. The polynomial conditions
are

\[
 \deg v=2t+2,\quad v(0)=-r,\quad v'(0)=-B,
 \quad [x^2]v=\eta,\quad B\eta\ne0.
\]

Conversely `v(0)=-r` makes `W=(v+r)/x` polynomial, so this change does
not lose the b=0 chart or introduce a division by b. Again the linear
coefficient `xS` is nonzero because B is nonzero. The same equivariant
theorem is therefore inapplicable to the full equation, not only to its
b=0 section.

## 5. Pell and abc applicability remains an additional algebraic problem

Structural equation (A9) is a factorization

\[
 wH=\frac3{16y^4}
 \left(xA_0^4-4By^2A_0^2-16y^3\kappa\right),\qquad A_0=xC.
\]

It is not yet a polynomial Pell norm equation `P^2-DQ^2=1` on a fixed
hyperelliptic curve. To use a Pell classification one must first exhibit
the square/norm structure, specify the curve, and prove the required
torsion or divisor condition. The established coprimalities with A0 do
not say that w and H are coprime or that either is a square. No such
missing condition is supplied by the sources examined.

No generic degree or abc estimate was used to claim exclusion. The next
source-sensitive step would be a classification of polynomial invariant
graphs for (5) that uses the linked coefficient constraints `A=x^3 C^2`
and `D` proportional to `bxC`, including repeated roots. Merely placing
the equation in the broad Abel family supplies no uniform proof.
