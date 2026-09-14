# Cube deformation: the same nonzero scalar leading term on all seven branches

MANUAL co-research, not FIRST/promotion. First action2026-09-13
02:07:28.891429159UTC; reserve02:19/HARD02:22 unchanged. All five named
input/context pins and the unchanged finalizer matched before bodies. No
scientific execution, new code, network, worker or live peer input.

## Result

Put delta=t-5/3. On EVERY one of the seven leading Puiseux branches,

    B = -14/(75*5103^2) * delta^2 + O(delta^(15/7)).       (1)

The same nonzero rational coefficient occurs on all seven, not merely a real
branch. Thus the scalar is a unit on the whole leading algebra for all
sufficiently small nonzero complex delta, and for all sufficiently large
actual integers r. This proves generic coprimality, but gives NO effective
radius or integer cutoff and does not cover every r>=2. The finite all-r
exception question remains open: NO_CLOSING_DISCRIMINATOR for the complete
selected all-integer task. No code swap or parameter farm follows.

## 1. Boundary algebra and all seven branches

Use a=X-1/3 and c=Y-1/27-a/3. At t0=5/3, the charged formulas give

    U=3a^2, V=a^2(a+1/9),
    f1=d6/binomial(t,3)=a^3-9c^2,
    f2=(d7-(t-2)d6)/binomial(t,3)=3a^2c.

Consequently P(t0,X)=U^2 f1(X,V/U)=9a^7 as a polynomial identity.
This verifies the coalescence observation, but NOT a boundary isomorphism
with Q[a]/(a^7): U loses its inverse. The original boundary algebra is
Q[a,c]/(a^3-9c^2,a^2c), of length seven, with basis
1,a,a^2,a^3,a^4,c,ac. Both descriptions have seven coalescing generic sheets;
the specialized algebras are not identified through a forbidden U inverse.

The constant delta-derivatives at a=c=0 can be obtained without expanding
source rows. Since phi=(1+u/3)^3 there,

    partial_t d6 = 3*binomial'(5,6)/3^6 = 1/1458,
    partial_t d7 = 3*binomial'(5,7)/3^7 = -1/30618,
    binomial(5/3,3)=-5/81.

Thus for weights wt(a,c,delta)=(2,3,7),

    f1 = a^3-9c^2 + terms of weight >=7,
    f2 = 3a^2c-delta/315 + terms of weight >7.           (2)

The first constant delta term of f1 is -delta/90. ROOT's advisory constants
agree with this independent coefficient differentiation; they are not used
as an assumed identity or independent blind evidence.

Set delta=eta^7, a=eta^2 A, c=eta^3 C. Divide f1 by eta^6 and f2 by eta^7.
At eta=0 the equations are

    A^3=9C^2,       A^2 C=1/945.

Hence A^7=1/99225=1/315^2 and C=1/(945 A^2). There are seven distinct
solutions (alpha,beta), all nonzero. The Jacobian of the two rescaled
equations is 21 alpha^4, nonzero. The analytic implicit-function theorem
therefore gives seven convergent branches

    a=alpha eta^2+O(eta^3), c=beta eta^3+O(eta^4).

They exhaust the punctured leading algebra: U=3alpha^2 eta^4+O(eta^5)
is nonzero, and the degree-seven P already has these seven distinct roots.
This does not assume reducedness at delta=0 or choose a coefficient field
factor to discard the other six branches.

## 2. Scalar leading calculation in the reciprocal cubic

Write z=v-1/3, so q(z)=v^3+a v+c. On one branch its three roots are
v=eta lambda+O(eta^2), where lambda^3+alpha lambda+beta=0.
This cubic is separable: its discriminant is -63 beta^2, not zero.
The charged universal trace identity for the SAME scalar is

    B=-Tr(z A_s(z) A_b(z)),
    A_h(z)=z^7 T_h(1/z), s=2t-1, b=4-t.

At t0 both exponents are7/3. Polynomial-part expansion at infinity gives

    A_(7/3)=v^7+(7/3)a v^5+(7/3)c v^4+(14/9)a^2 v^3
             +(28/9)ac v^2+((14/9)c^2+(14/81)a^3)v
             +(14/27)a^2c.                            (3)

It is the polynomial part of (v^3+av+c)^(7/3); taking polynomial part
commutes with translation z=v-1/3. Every displayed term has weight seven.
The exponent derivative supplies one further leading contribution. At the
cube root z=-1/3,

    A_h(-1/3)=3^-7 * binomial(3h-1,7),
    L=partial_h A_h(-1/3)|_(h=7/3)=1/5103.

The finite alternating-binomial identity proves this formula directly. Since
s=7/3+2delta and b=7/3-delta, all three root evaluations satisfy

    A_s=eta^7(F(lambda)+2L)+O(eta^8),
    A_b=eta^7(F(lambda)-L)+O(eta^8),                    (4)

where F is (3) with v,a,c replaced by lambda,alpha,beta. All other terms
from exponent differentiation have strictly higher weight.

## 3. Explicit trace and the uniform nonzero coefficient

Reduce (3) modulo lambda^3+alpha lambda+beta. Before using the cusp relation,

    F=(4/9)alpha beta lambda^2
       +((2/9)beta^2-(4/81)alpha^3)lambda+(8/27)alpha^2 beta.

Put h=alpha^2 beta=1/945. Since alpha^3=9beta^2, this becomes

    F=(4/9)alpha beta lambda^2-(2/9)beta^2 lambda+(8/27)h.

The Newton sums are Tr(lambda)=0, Tr(lambda^2)=-2alpha,
Tr(lambda^3)=-3beta and Tr(lambda^4)=2alpha^2. Directly squaring this
quadratic therefore gives

    Tr(F)=0,
    Tr(F^2)=(136/729)h^2=(136/25)L^2,
    L=(5/27)h=1/5103.

This calculation uses all three roots of the auxiliary cubic, on each of
the seven leading branches. From (4), and z=-1/3+O(eta),

    B=eta^14*(Tr(F^2)-6L^2)/3+O(eta^15)
     =-14/(75*5103^2)*eta^14+O(eta^15).

Since eta^7=delta this proves (1). Equivalently the leading coefficient is
-2/279006525. The value is independent of alpha, although the subleading
terms need not agree across branches. ROOT's later in-task advisory arrived
with the same residue and leading coefficient; this is shared same-model
co-research, not blind independence or different-model validation.

The error bound is algebraic/analytic, not heuristic weight matching.
At delta=0, (3) is exactly homogeneous of weight7. Its substitutions along
the convergent branches give eta^7 F+O(eta^8). The derivative with respect
to an exponent is polynomial in the finite coefficients and analytic in
(v,a,c); only its constant L has weight0. Multiplication by delta thus gives
the sole additional weight7 term; all remaining terms have weight>=8.
The auxiliary roots lift analytically because their rescaled cubic has
nonzero discriminant. Product and trace then leave no term below weight14,
and their displayed weight14 coefficient is nonzero. No branch positivity
or assumption that complex points are real enters this argument.

## 4. What this decides, and what it does not

There is a common punctured complex neighborhood of delta=0 on which ALL
seven B-values are nonzero: there are finitely many convergent branches and
each has the same nonzero leading coefficient. The original guards hold
there since Y tends to1/27 and d5 to3^-5, while U has the nonzero leading
term already given. Thus this is whole-algebra unitness near the boundary,
not just generic nonzero in one embedding.

In particular gcd(P,U^7 B(t,X,V/U))=1 over Q(t)[X]. A generic common factor
would give a zero on at least one of these seven nearby branches. More
precisely, the norm of B on the rank-seven algebra has initial term

    (-14/(75*5103^2))^7 * delta^14.

The next possible norm order is at least15: the product of all branches
is invariant under eta->zeta_7 eta, so its convergent expansion has integer
powers of delta. This proves a nonzero norm but does not produce the exact
global norm polynomial or its other zeros.

For actual r, delta=1/(9r+3). The neighborhood statement consequently proves
existence of an unspecified R0 such that all integer r>=R0 pass. It does
NOT prove a bound for R0, an effective zero-free real interval reaching
delta=1/21, or the finitely many remaining actual r. No numerical tail bound,
unproved monotonicity or silent finite sampling supplies these missing steps.
The first-and-last interval endpoints must not be confused: delta=0 itself
has B=0 and is no finite r.

The all-r elimination can now regard a generic common factor as ruled out
by this MANUAL candidate theorem, subject to independent review. Its required
effective rational-exception exclusion remains. No measured improvement in
symbolic time, degree or certificate size follows, and no accepted source
or runtime is changed. STOP this deformation attack here: it gives a genuine
all-branch asymptotic constraint, not a closing all-r criterion or authority
to start a bounded-r farm.

## Inputs, controls and custody

Five input/context objects: reduction7b8545a6, reciprocal trace6c357b0b,
ROOT intake47dcaf21, own earlier reporte8bf9ecf (four freshly WHOLE reads),
and COORD33cfa610 (same-agent exact-byte WHOLE reuse after current pin,
from the completed September12 20:05-20:14UTC review). The intake's correction
det(G)=-Y Delta^2 is binding; the old -Y^3 Delta^2 is not used. The rejected
universal B/(Delta J) identity is not revived. The proof uses the reciprocal
trace rather than either determinant expression.

ROOT's adapted-coordinate and later leading-term messages are disclosed
advisory inputs within this task; no new file, live report or peer body was
read. The constants in (2), the seven-branch Jacobian, exponent derivative
and final trace were manually checked. The U=0 boundary, all branches,
repeated cube root, exponent perturbations and effective-radius gap are
explicit controls. No canonical OPEN, shared edit, network or scientific
interpreter/CAS/import/AST/test/fixture action occurred. Publication uses only
text/hash/date/apply_patch and the unchanged administrative finalizer.

Own targets were absent. Own WHOLE readback and unchanged postpins precede
the unique final marker. Custody is the last authored file, with exact
expected-manifest verification and actual start-to-IDLE elapsed in the
terminal metadata, not token, CPU or billing estimates. No downstream claim,
source exclusion, REG, all-F10 or JC2 consequence is promoted here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9601`.
- Body SHA-256:
  `379722d2c6925a6f4598b3c904dac2c6faaab27873a963c353210665aec96b20`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
