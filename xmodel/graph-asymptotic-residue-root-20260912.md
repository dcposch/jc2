# A finite-target asymptotic residue for graph subalgebras

ROOT manual producer report, September12,2026. INTERNAL-UNREVIEWED; one
different-model FIRST required. No computation. This test uses ONE source
curve r_H=0, not a collision correspondence or a degree/parameter farm.

## Exact statement

Write v=xy and define the literal polynomials

    P=z(1+v)^3+y^2(1+v)(3v+4),
    Q=y+3xz(1+v)^2+3xy^2(3v+4),
    R=2x-3x^2y-x^3z.

Let c!=0 and h(v) be a NONZERO polynomial. Restrict to
H=c+y^2 h(xy), giving phi_H=(p_H,q_H,r_H) and B_H=C[p_H,q_H,r_H].
Put

    f(v)=2-3v-v^2 h(v),  m=deg f>=2,
    f(v)=f_m v^m+f_{m-1} v^(m-1)+... .

Claim: if f_{m-1}!=0, no polynomial target one-form alpha has
d(phi_H^*alpha)=dx wedge dy, and no pair in B_H has nonzero constant
Jacobian, at ANY polynomial degree.

For h=k constant nonzero, this excludes every H=c+k y^2 because
f_2=-k and f_1=-3. For deg h=d>=1 it excludes precisely the parameters
tested by h_{d-1}!=0, since m=d+2, f_m=-h_d, f_{m-1}=-h_{d-1}.
If such a nonconstant h admits a Keller pair in B_H, this proof requires
h_{d-1}=0. It does NOT prove that the remaining parameters admit a pair,
or that any arbitrary JC2 source can be put into this graph family.

## 1. Actual source curve and finite target

On x!=0 set t=1/x and v=xy, so x=1/t,y=t v. Direct substitution gives

    r_H=f(v)/t-c/t^3.

Take the algebraic curve t^2 f(v)=c, with t invertible. It is an ACTUAL
source curve with r_H=0, not a merely numerical infinity profile. The
source maps x=1/t,y=t v lie on the specified graph by definition. They
satisfy

    p_H=t^2(v+1)(v+2), q_H=t(4v+6), r_H=0.       (1)

For a direct polynomial check, replacing c by t^2 f(v) in p_H,q_H uses

    f(v)(v+1)^2+v^2[(v+1)^2 h(v)+3v+4]=v+2.

All h terms cancel; expanding (2-3v)(v+1)^2+v^2(3v+4) leaves v+2.
This proves (1) without an ambient Jacobian identity or an image theorem.

Choose an irreducible component of this curve and a place over v=infinity
on its normalized projective model. Such places exist explicitly. If m
is even, let w=1/v and t=w^(m/2) A(w), where

    A(w)^2=c/[f_m+f_{m-1}w+...+f_0 w^m], A(0)!=0.

The square root exists as a formal power series over C; its coefficients
are recursively determined since2A(0)!=0. This is an algebraic local
branch of the displayed curve, with ramification1. A globally split curve
causes no problem: choose either component containing such a branch.

If m is odd, use v=w^-2 and t=w^m A(w), with the analogous denominator
f_m+f_{m-1}w^2+... . The branch is algebraic and normalized with
ramification2 over v=infinity: the valuation of c/f(v) on the base is
odd, so the quadratic function-field extension is not split. In both
cases write e=1 or2 for this ramification index.

Then ord(t)=em/2 and ord(v)=-e. Since m>=2, formula (1) has NO pole:
ord(p_H)>=e(m-2)>=0 and ord(q_H)>=e(m/2-1)>=0. Hence the target map
extends regularly across this place to a FINITE point of A3. For m>2
the target point is(0,0,0); for m=2 it is finite but need not be in the
image of a finite source point. No second source branch is required.
The source itself has a pole because x=1/t, so this is genuinely an
asymptotic place, not a constant map or a finite source endpoint.

## 2. Source primitive and residue

The source polynomial primitive alpha0=x dy restricts to

    alpha0=dv+v dlog t=dv-(v/2)(f'(v)/f(v))dv.    (2)

This rational one-form descends to the v-line. Put A=f_{m-1}/f_m. The
expansion at infinity is

    f'/f=m/v-A/v^2+O(v^-3),
    alpha0=(1-m/2)dv+(A/2)dv/v+O(v^-2)dv.

Since Res_infinity(dv/v)=-1 and dv is exact, the base residue is -A/2.
On the actual normalized source curve it is

    Res(alpha0)=-e*f_{m-1}/(2f_m).               (3)

This is nonzero exactly under the claimed coefficient condition. For
h=k!=0 it is -3/(2k), e=1. For nonconstant h it is
-e*h_{d-1}/(2h_d). This computation treats the ACTUAL normalization and
does not mistakenly transfer a base residue unchanged through odd degree.

## 3. Why a target-polynomial primitive is impossible

Suppose polynomial alpha on A3 has d(phi_H^*alpha)=dx wedge dy. Then
phi_H^*alpha-alpha0 is a closed polynomial one-form on A2, so it equals
dF for a polynomial F(x,y). This elementary polynomial Poincare identity
follows by homogeneous radial contraction; all divisions are by positive
integer degrees in characteristic zero.

Pull back to the actual normalized source curve. The target coordinates
in(1) are regular at the selected place, so the pullback of ANY polynomial
target alpha is regular there and has zero residue. Also dF has zero
residue: F(1/t,tv) is a rational function, and differentiation of its
Laurent expansion never produces a nonzero dw/w coefficient. Equation(3)
is therefore incompatible with the assumed target primitive if A!=0.

If F0,G0 in B_H have J(F0,G0)=j!=0, write F0=F1(p_H,q_H,r_H) and
G0=G1(p_H,q_H,r_H). The target-polynomial form F1 dG1/j gives the
forbidden primitive. Thus the conclusion excludes ALL polynomial degrees.
No finiteness, normality or injectivity of phi_H is assumed. It is enough
that THIS source curve has a normalized place with finite target.

## 4. Honest zero-residue control and stop

For h(v)=k v^d with k!=0,d>=1, the coefficient A is zero. This is a
genuine member of the same family, not an abstract surface control. The
chosen infinity places then have zero residue. More strongly, subtracting
the exact derivative (1-m/2)d(xy) from the GLOBAL source primitive makes
its restriction to this curve O(v^-2)dv, regular at v=infinity and at
both normalized cover types. Thus further principal-part calculations at
these same places cannot restore this residue obstruction. This adjusted
primitive has SOURCE coefficients, not a constructed target-polynomial
primitive; no B_H pair or exactness conclusion follows for A=0.

For h=0, m=1 and the finite-target check fails; the separate constant-graph
collision theorem is not a premise here. Likewise c=0 destroys the unit
curve equation used above. Neither excluded limit is silently included.
No extra r_H levels, other poles, degree tests or runtime is selected.
The remaining source/general-graph attachment and the A=0 stratum remain
undecided. This is a fixed-family coefficient restriction, not JC2.

## Provenance, checks, and closeout

Scientific literal source: constant-graph-subalgebra-control-astra-20260912.md,
SHA590609a7a6f52f72e940a01604c5e6f0c1444277c54bfbb9c69e0fa0c55fd679,
reused from ROOT's exact-pin WHOLE read in the preceding turn; current
prepin matched. Only the literal P,Q,R are used, independently substituted
above. The prior collision and quadratic reports are not theorem premises.
ROOT derived the single-curve simplification while Astra independently
completed the quadratic collision argument; that alternative is not the
review of this broader assertion. No literature novelty claim.

History checksum: canonical APPROACHES/AUDIT/PROGRESS/REDUCTION and named
recent graph reports searched for the specific mechanism/quantity; no
broader corpus absence is claimed. Previously displayed nonclosed beta,
Jacobian module membership and ramified double-curve residue are distinct
arguments, not a proof of this source-local finite-target criterion.

Manual polynomial expansion, local square-root construction, both parity
cases, residue sign and genuine zero-coefficient graph control are the
producer checks. No mathematical interpreter/CAS/helper/code execution,
network or AWS. Existing administrative transaction only; own complete
readback and source postpin precede marker LAST. No shared canonical OPEN.

## COLLISIONS

status: EMPTY

- Own scope/identifier check only. Quantity is the stated coefficient
  obstruction, decided manually; cheapest test was the exact r_H=0 curve
  and one infinity residue, with no measured compute/runtime claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7847`.
- Body SHA-256:
  `865942fd2192eca8330ed7252940525fa4e265e8824310028f6c361076e06782`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
