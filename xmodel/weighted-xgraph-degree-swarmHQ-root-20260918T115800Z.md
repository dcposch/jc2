# All normalized weighted lifts: the complementary graph pair has positive Jacobian degree

Producer: swarmHQ ROOT (Astra context), with manual same-model co-check
by weighted_xgraph_degree_1157; that check is NOT different-model FIRST.
Date: September 18, 2026 UTC.
Basis: 8dab02d37124fb86e962768ec99cd39bddc2d4d9.
Evidence: MANUAL characteristic-zero polynomial proof, no scientific execution.
Lifecycle: PRODUCER-CHECKED, PROVISIONAL pending different-model FIRST.
Claim: WEIGHTED-XGRAPH-DEGREE-1. No external novelty claim.

## Exact statement

Work over C. Use the normalized weighted-lift polynomials

    p(0)=0, p(1)=-1, integral_0^1 p(w)dw=0,
    k=p'(1)!=-2, a=-(1+k)/(2+k), q(0)=0, q'=w*p',
    u=1+xy, gamma=1+a*xy+x^2*z, w=u*gamma,
    B=(1+u*p(w)/w)/x,
    A=(u+u^2*q(w)/w^2)/x^2.

Let n=deg p, alpha its leading coefficient, and beta=n*alpha/(n+1).
Then n>=2 and beta is the leading coefficient of q. The expressions
A,B are WHOLE polynomials; the displayed quotients are exact divisions.
For any h in C[y,z], put

    T_h(y,z)=(B(h(y,z),y,z), A(h(y,z),y,z)),
    J(f,g)=f_y*g_z-f_z*g_y.

If h!=0 and d=deg h (ordinary total degree), then

    deg J(T_h)=6*(n-1)*d+4*n-3 > 0.                 (1)

For h=0, T_0 is the known triangular automorphism, with J(T_0)=-1.
Thus T_h is Keller if and only if h=0. There is NO graph-invariance
assumption, target graph, support bound or bound on either n or d.

For every nonzero h, no polynomial postcomposition of T_h can be
Keller. The same exclusion holds after any polynomial parametrization
of its source graph: if sigma:A2->A2 and Psi:A2->A2 are polynomial,
Psi composed T_h composed sigma cannot have nonzero constant Jacobian.
For h=0 the graph only supplies an automorphism composed with sigma;
it does not decide an unresolved Keller problem carried by sigma.

This concerns the complementary output pair (B,A) on x=h(y,z).
It does not cover arbitrary nonlinear combinations of all three ambient
outputs, other embedded surfaces or arbitrary plane Keller maps.

## Whole polynomiality and the zero graph

Integration by parts gives q=wp-integral_0^w p, hence q(1)=-1.
At w=0, p/w and q/w^2 are polynomials. A linear p would equal -w
and violate the integral condition, so n>=2. Leading terms in q'=wp'
give deg q=n+1 and lc q=beta!=0.

Write r=p/w and s=q/w^2. At 1,

    r(1)=s(1)=-1, r'(1)=k+1, s'(1)=k+2,
    w=1+(1+a)xy+O(x^2).

The constant term of 1+u*r(w) vanishes. Its xy coefficient is
k+a*(k+1)=-1/(k+2). The constant and linear-x coefficients of
u+u^2*s(w) vanish: the latter is (k+1)+a*(k+2)=0.
This proves exact divisibility by x and x^2 respectively, before any
graph substitution, including the graph x=0. For some scalar eta,

    B(0,y,z)=-y/(k+2), A(0,y,z)=eta*y^2+(k+2)*z.

Indeed the x^2*z coefficient in the second numerator is s'(1)=k+2;
the only other terms at that x order are scalar multiples of y^2.
The determinant of the displayed ordered pair (B,A) is -1.

## Nonconstant graphs: exact highest homogeneous terms

Suppose d>=1, and let H be the nonzero degree-d homogeneous part of h.
All degrees in this section are ordinary total degrees in y,z, not
partial degrees, mapping degrees or ambient three-variable degrees.
After graph substitution, the highest terms are

    u_h: H*y,       gamma_h: H^2*z,       w_h: H^3*y*z.

The gamma leader is unique since 2d+1>d+1 and 2d+1>0.
From the exact polynomial identities

    h*B_h=1+u_h*r(w_h),
    h^2*A_h=u_h+u_h^2*s(w_h),

and deg r=deg s=n-1, the highest terms on each right side are unique.
The degree and leading-form product rules in the domain C[y,z] allow
division by the leading forms H and H^2 in THESE identities. We are
not asserting that 1/h is regular or deleting the locus h=0.
Consequently, with

    M=H^(3n-3)*y^n*z^(n-1),
    N=deg M=3*(n-1)*d+2*n-1,

the highest forms of B_h,A_h are alpha*M and beta*y*M, of degrees
N and N+1. Contributions involving a lower-degree term have Jacobian
degree at most 2N-2. The degree-(2N-1) candidate is therefore

    J(alpha*M,beta*y*M)=-alpha*beta*M*M_z
      =-alpha*beta*(n-1)*H^(6n-7)*y^(2n)*z^(2n-3)
        *(H+3*z*H_z).                              (2)

The final factor is NOT zero: if H=sum_j H_j(y)*z^j, then
H+3zH_z=sum_j(1+3j)*H_j(y)*z^j, and each 1+3j is nonzero in
characteristic zero. All other displayed factors are nonzero, with
nonnegative exponents because n>=2. Thus the top Jacobian does not
cancel and its degree is 2N-1, exactly (1).

## Nonzero constant graphs

The case h=c in C* must be computed separately, since the two linear
terms a*c*y and c^2*z of gamma now have the SAME degree. Put

    L=a*y+c*z, M=c^(2n-2)*y^n*L^(n-1).

Here u has leader c*y, gamma has leader c*L, and w has leader c^2*y*L.
Hence B_h,A_h again have leaders alpha*M,beta*y*M, with degrees
2n-1,2n. Their top Jacobian is

    -alpha*beta*M*M_z
      =-alpha*beta*(n-1)*c^(4n-3)*y^(2n)*L^(2n-3).  (3)

This is nonzero even when a=0, since c!=0. Its degree is 4n-3,
which proves (1) for d=0. No division by a or genericity of c is used.

## Postcomposition, parametrization and controls

The polynomial chain rule gives

    J(Psi o T_h o sigma)
      =J(Psi)(T_h(sigma))*J(T_h)(sigma)*J(sigma).

If this product were a nonzero constant, every factor would be a unit
in the polynomial ring. In particular J(sigma) would be nonzero, so
sigma would be dominant and pullback by sigma would be injective.
A nonconstant J(T_h) cannot become a constant under an injective
pullback: otherwise pullback kills J(T_h)-c. This is a contradiction.
No Jacobian Conjecture assumption concerning sigma is used.

The h=0 triangular pair is the essential exception, not an omitted
chart. For the fixed seed p=4w^3-5w^4, q=3w^4-4w^5, one has
n=4, alpha=-5, beta=-4, a=-7/6. Formula (2) becomes

    -60*H^17*y^8*z^5*(H+3*z*H_z),
    deg J(T_h)=18*d+13  (h!=0).

Formula (3) gives -60*c^13*y^8*(c*z-7*y/6)^5 for c!=0.
At the admissible seed p=2w-3w^2, q=w^2-2w^3 and h=y,
the two leaders are -3*y^5*z and -2*y^6*z; direct differentiation
gives -6*y^10*z, degree 11 as (1) predicts.
These symbolic specializations, the separate constant case, and the
whole x=0 evaluation are manual checks, not a finite-degree experiment.

## History and scope

The [all-seed coordinate-fiber theorem](weighted-lift-coordinate-fibers-swarmHQ-root-20260916T133700Z.md)
uses the same normalization but requires a constant ambient output.
The [all-seed tangent-graph theorem](tangent-graph-linear-projections-swarmHQ-root-20260916T182800Z.md)
uses its separately normalized q'=wp'/2 presentation, z=Z(x,y), and
constant linear outputs. Its factor 1/2 is NOT imported here.
The [fixed-seed invariant-graph theorem](invariant-quartic-graph-swarmHQ-root-20260918T103700Z.md)
has the same x=h orientation for one seed, but requires h(B_h,A_h)=C_h.
The present degree identity removes that entire invariance dependency
for the pair (B,A) and all normalized seeds. It is not a deduction from
the old invariance argument or from an ambient generic-degree claim.

All three reports were read whole. Scoped searches used frozen public
8dab02d37124fb86e962768ec99cd39bddc2d4d9 and HQ
3b7f5455537104d643a70503e1f6d131fcea69af before admission. No exhaustive
priority claim. Their full-file SHA256 values are respectively:

- eb7bb701c28f3b22683a454375098ea688e2ac210d56f8bb5f3a6921c2170041
- bc688cbf61e6e9b4adb1c93054bac5feb54d8b85feb867c4464849969824d317
- fc40c79d12f51c4c155ebad9ddd89fb6534c92fb3ff6cd3b2177a3be7092f252

This self-contained identity excludes one construction class uniformly;
it does not resolve JC2. No arbitrary-output/graph-orientation/seed
census or automatic successor is selected. No external theorem, CAS,
prime sampling, scientific Python, worker or source-access retry is
used. Hashes, collision checks and publication seals are administrative
integrity evidence, not verification of the mathematics.

## OPEN(S) RAISED

None. The global source-landing/properness problem remains outside scope.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8094`.
- Body SHA-256:
  `6c0f89f7fc0a9285119d549f04779baa6613bf73ecf44fe6e12c255abff0592a`.
- Frozen basis: `8dab02d37124fb86e962768ec99cd39bddc2d4d9`.
