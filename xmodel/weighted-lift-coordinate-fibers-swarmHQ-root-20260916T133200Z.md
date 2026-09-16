# Coordinate-fiber obstruction for normalized weighted lifts, in every seed degree

Producer: swarmHQ ROOT (gpt-6-astra), September16,2026 UTC.
Basis: 31be14b00ca62ad7391d9c0025004c9fde4edf6a.
Evidence: MANUAL characteristic-zero algebra and surface geometry.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model FIRST.
Native Astra independently checked the B-fiber completion argument; that
same-model co-check is not FIRST. No literature-novelty claim.

## Exact statement

Work over C. Let p in C[w] satisfy

    p(0)=0, p(1)=-1, integral_0^1 p(w)dw=0,
    k=p'(1)!=-2.

Define q(0)=0, q'(w)=w*p'(w), and put

    a=-(1+k)/(2+k),
    u=1+xy, gamma=1+a*xy+x^2*z, w=u*gamma,
    r(w)=p(w)/w, s(w)=q(w)/w^2,
    alpha=u+u^2*s(w), beta=1+u*r(w),
    F=(A,B,C)=(alpha/x^2, beta/x, x*gamma).             (1)

These expressions define polynomials on the WHOLE source A3, not just
the open x*gamma!=0. Both r and s are nonconstant polynomials.

For every scalar level, the only irreducible component of any of the
three literal coordinate fibers of F that admits an everywhere-defined
dominant morphism from A2 is the plane x=0 in C=0. On that plane the
remaining pair (A,B) is a triangular polynomial automorphism in (y,z).

Consequently, if an everywhere-defined polynomial j:A2->A3 has
two-dimensional image and one coordinate of F composed with j is
constant, then that coordinate is C, its value is zero, and j has
image in x=0. Writing j=(0,j_y,j_z), the remaining plane pair equals a
polynomial automorphism composed with (j_y,j_z). It is Keller exactly
when (j_y,j_z) is Keller, and invertible exactly when (j_y,j_z) is.
Thus this coordinate-fiber mechanism creates no plane Keller
counterexample not already carried by the initial parametrization.

Quantifiers cover all complex seeds satisfying (1), all their degrees,
all levels, all irreducible surface components and arbitrary regular
dominant A2 first legs. They do NOT cover a non-coordinate target
surface, arbitrary output projections, target coordinate changes,
stabilizations/compositions or a rational first leg with interior poles.
There is no theorem placing every plane Keller map in this construction.

## Provenance and polynomial identities

The displayed normalization was retrieved September16,2026 from
[the author's weighted-lift exposition, sections2 and4](https://github.com/dasjoms/jacobian-conjecture-counterexample-exploration/blob/main/corollary-s/docs/corollary_surjective_keller_onepage.md),
which attributes the construction to Gallagher. We use the explicitly
restated formulas only. Its separate surjectivity, generic-degree and
certificate claims are NOT imported or independently certified here.
No contributed code was run. The argument below allows every seed
satisfying the displayed conditions, not only the page's special p_d.

Integration by parts gives

    q(w)=w*p(w)-integral_0^w p(t)dt,
    q(1)=-1, q'(1)=k.

The first relation at w=0 proves that q is divisible by w^2. A linear
p would be -w and would violate the integral condition, so deg p>=2.
If deg p=n, then deg q=n+1 and deg r=deg s=n-1>=1.
At w=1,

    r(1)=s(1)=-1, r'(1)=k+1, s'(1)=k+2.

Expand in x, keeping y,z arbitrary. The constant coefficient of beta
is zero; its coefficient of xy is k+a*(k+1)=-1/(k+2). The constant
coefficient of alpha is zero; its coefficient of xy is
(k+1)+a*(k+2)=0. Its coefficient of x^2*z is k+2. Therefore B and A
are polynomials and, for a scalar eta depending only on p,

    B(0,y,z)=-y/(k+2),
    A(0,y,z)=eta*y^2+(k+2)*z.                         (2)

As an optional normalization check, on x*gamma!=0 introduce

    P=B*C=gamma+p(w), Q=A*C^2=w*gamma+q(w).

Then det d(P,Q)/d(w,gamma)=-gamma, using q'=wp'. Hence
det d(C,P,Q)/d(x,u,gamma)=-gamma^3, while
det d(C,P,Q)/d(A,B,C)=-C^3 and
det d(x,u,gamma)/d(x,y,z)=x^3. The chain rule gives det JF=1
on this dense open, hence everywhere as a polynomial identity.
No surjectivity or mapping-degree assertion is needed for the theorem.

## Two obstruction principles

First, an irreducible affine variety with a nonconstant regular unit
cannot admit a dominant morphism from A2: the induced injective ring
map would send that unit to a unit in C[t1,t2], hence a constant.

Second, use the accepted
[corrected MORPHIC rational-forest theorem](bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md):
if a smooth quasi-projective complex surface S admits an everywhere-
defined dominant A2 morphism, every smooth projective strict-SNC
completion S=X minus D has a rational-forest boundary dual MULTIGRAPH.
Parallel intersections count as separate edges. No surjectivity,
properness or etaleness of the first leg is required. Rational
domination alone does not imply this conclusion.

We consume the corrected theorem at its accepted tier, not reprove it.
We also use standard completion/resolution of smooth complex surfaces
without altering the given smooth open, and factorization of a proper
birational morphism of smooth projective surfaces into point blowups.

## A-fibers: units on every component

Since x^2*A=u*(1+u*s(w)) and x,u are coprime, there is a polynomial D
with

    A=u*D, x^2*D=1+u*s(w).                           (3)

For A=c!=0, u is a regular unit on every component. For A=0, a
component either lies in u=0, where xy=-1 makes x a nonconstant unit,
or in D=0, where (3) gives u*s(w)=-1 and makes u a unit.

Here u cannot be constant on a surface component of an A-fiber unless
u=0. Indeed, if its value is u0!=0, that component must be a surface
component of V(u-u0). If u0!=1, this is the irreducible surface
xy=u0-1 with x invertible and gamma freely varying. There

    A=u0*(1+u0*s(u0*gamma))/x^2

is nonconstant in gamma because s is nonconstant. If u0=1, the only
surface possibilities are x=0 or y=0. Formula(2) makes A nonconstant
on x=0; on y=0 it is (1+s(1+x^2*z))/x^2, nonconstant in z.
Both contradict containment in a constant A-fiber. Finally V(u) is
irreducible and isomorphic to Gm times A1, so its unit x is nonconstant.
Every A-fiber component is excluded by the unit principle.

## B-fibers: units at zero and a boundary cycle otherwise

In the independent plane with coordinates (u,gamma), define

    h(u,gamma)=1+u*r(u*gamma), H=V(h).

On H, u*r(w)=-1, with w=u*gamma. The mutually inverse formulas

    w=u*gamma,
    u=-1/r(w), gamma=-w*r(w)

identify H with Spec C[w,1/r(w)]. In particular H is a smooth
irreducible rational curve, whose smooth completion P1 has

    e=1+#distinct complex roots of r >=2

points outside H. These are its places over the line at infinity
in the (u,gamma) plane. At a root of r the projective limit is
[1:0:0], while w=infinity has limit [0:1:0]; repetitions among roots
are allowed and do not remove the two distinct limiting points.

Let S_b=V(B-b) in the original A3. Its x=0 locus is the line
y=-b*(k+2), by(2), so no two-dimensional component can be supported
there. The derivative B_y=-1/(k+2) on that line proves smoothness
there.

If b=0, the open x!=0 in S_0 is Gm_x times H, using

    y=(u-1)/x, z=(gamma-1-a*(u-1))/x^2.

It is smooth and irreducible; the preceding one-dimensional
complement gives a smooth irreducible S_0. The global identity
xB=h gives u*r(w)=-1 on S_0. Thus u is a unit, nonconstant already
on Gm times H because r is nonconstant. The unit principle applies.

If b!=0, the regular morphism

    pi=(u,gamma):S_b -> A2_(u,gamma)

identifies S_b minus V(x) with A2 minus H. The inverse is

    x=h(u,gamma)/b,
    y=(u-1)/x, z=(gamma-1-a*(u-1))/x^2.               (4)

The line at x=0 maps entirely to (1,1), which lies on H. As above,
the open is smooth irreducible and no surface component lies in the
complement, so S_b is smooth irreducible and pi is birational.

Choose a smooth projective completion X of S_b extending pi to a
proper birational morphism f:X->P2, with D=X minus S_b strict SNC.
For example take graph closure into a projective completion times
P2, then resolve its singularities and boundary only outside S_b.
Let L be the line at infinity and T=(f^(-1)(L))_red. Since pi maps
all of S_b into the affine plane, every component of T belongs to D.
Factoring f into point blowups shows that T is a connected rational
tree: a blowup over L adds a leaf or subdivides an edge; one away
from L does not change T.

Let Htilde be the strict transform of the projective closure of H.
Its generic point is not in S_b, since pi(S_b) meets H only at(1,1),
so Htilde is a boundary component. It is smooth, rational, and maps
as the normalization of that closure. It meets T at the e distinct
points corresponding to the e places at infinity. The strict-SNC
condition makes each meeting an ordinary edge in the boundary
multigraph; no triple point merges these edges.

Thus the subgraph consisting of T and Htilde has first Betti number
e-1>=1. Extra boundary components cannot erase its cycle. This
contradicts the MORPHIC rational-forest theorem if an everywhere-
defined dominant A2->S_b exists. No assumption that every modification
occurs over(1,1) was made; arbitrary boundary blowups are allowed.

## C-fibers and the surviving plane

For C=c!=0, x is a nonconstant unit; explicitly this fiber is
Gm_x times A1_u with gamma=c/x and the inverse y,z formulas above.
For C=0 the components are x=0 and gamma=0. On gamma=0, x is a
nonconstant unit since x*(a*y+x*z)=-1; this component is again
Gm_x times A1_y. The remaining component x=0 is a literal A2 and
is therefore dominated by A2. Formula(2) gives its remaining pair

    G(y,z)=(eta*y^2+(k+2)*z, -y/(k+2)),
    G^(-1)(A,B)=(-(k+2)*B,
                 (A-eta*(k+2)^2*B^2)/(k+2)).

Its Jacobian in (y,z) is 1. The composition assertion in the exact
statement now follows by taking the closure of j(A2), which must be
an irreducible surface component of the chosen coordinate fiber.

## Scope checks and prior results

The [fixed cubic-core tower theorem](low-fiber-tower-transfer-root-20260913.md)
and [Keller right-factor invariance](low-fiber-keller-factor-invariance-root-20260913.md)
address full factorizations through chains with low mapping-degree
steps. This result instead has arbitrary seed degree and arbitrary
regular first legs, but restricts to literal coordinate fibers.
It neither extends the tower's degree bound nor supplies its general
factorization hypotheses. The old Picard obstruction for a
P1 times P^(d-1) construction is not the argument used here.

Removing the whole-plane requirement defeats the obstruction:
(4) parametrizes the nonzero B-fiber from the punctured plane A2
minus H. A rational A2 first leg can therefore exist; calling this
an entire-plane map would be the already corrected morphic/rational
fallacy. Also, the zero C-fiber really does have an A2 component;
excluding every fiber without that exception would be false.

There was no CAS, numerical, modular or coefficient search. Manual
replay consists of the Taylor identities, the explicit inverse maps,
the component/unit checks and the boundary graph argument. No exit
price or new foundational degree bound is asserted. This closes one
uniform construction mechanism, not JC2 or all higher-dimensional
descent. There is no automatic projection/target-change successor.

## OPEN(S) RAISED

None. Existing general construction and source-landing gaps retain
their previous scope; no new search family is commissioned.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11394`.
- Body SHA-256:
  `bdf40c173af52c416ddbf7e4066ec9f67aed869221198a8198d9f7221102ae1e`.
- Frozen basis: `31be14b00ca62ad7391d9c0025004c9fde4edf6a`.
