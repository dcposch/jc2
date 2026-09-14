# Exact Liouville plane curves have unbounded genus

Producer: ROOT/swarmHQ, coordinator. Evidence: MANUAL.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED. No different-model FIRST.
Basis: 7bc1fdfbad16daef6b5c8bf2c9469953691cfd1d.

## Target and disposition

The proposed all-degree shortcut was: a smooth closed irreducible affine
plane curve with exact restricted Liouville form must have genus zero, or
at least uniformly bounded genus. It was a fresh candidate, not a promoted
campaign premise. An actual Keller pair has polynomial dS=x dy-f dg; on
f=c this gives x dy=d(S+c g). A valid genus-zero implication would therefore
have a genuine generic-fiber client. The curve-only implication is FALSE.

For every odd integer n>=3 and every c in C*, put

    p_n(x,y)=x^2+x^(3n+2)y^n,
    C_(n,c)={p_n=c},
    t=x^3 y.

Then C_(n,c) is smooth, closed, irreducible, and has geometric genus
(n-1)/2. Its restricted x dy is the differential of the REGULAR function

    S_(n,c)=[t+(3n+2)t^(n+1)/(2(n+1))]/c.

Thus every smooth generic fiber of this fixed polynomial pencil is exact,
with no genus ceiling. The c=0 fiber is critical and nonreduced, so these
are not Keller pairs or a counterexample to JC2. Generic-fiber exactness
does not supply a nonsingular whole-plane pencil or a common polynomial
Keller coframe. No genus/control-family successor is selected.

## Exact ring maps and smoothness

Let R=C[x,y]/(x^2(1+t^n)-c), with t=x^3 y. Here x is a unit: its inverse
is x(1+t^n)/c. Define v=1/x. There is an explicit isomorphism

    R = C[t,v,v^(-1)]/(c v^2-1-t^n),
    t=x^3 y,  v=1/x;
    x=1/v,    y=t v^3.

The displayed substitutions compose to the identity on every generator.
In particular, the inverse image of p_n is v^(-2)(1+t^n)=c. No missing
points or unproved normalization identification enter this isomorphism.

The polynomial 1+t^n is squarefree and is not a square in C(t), so the
quadratic function field is irreducible. The affine equation c v^2=1+t^n
is smooth on v!=0 because its v derivative is 2c v, a unit there. Hence
the literal closed plane curve, not just its normalization, is smooth and
irreducible. One may also check the plane gradient directly: if x!=0 and
the y derivative vanishes, then y=0 and the x derivative is 2x!=0.

## Genus and exact differential

The smooth projective completion has degree-two map t to P1, ramified at
the n distinct roots of 1+t^n and at infinity (n is odd). Riemann--Hurwitz
gives 2g-2=-4+(n+1), hence g=(n-1)/2. Inverting v removes the n finite
ramification points; the affine chart already omits the point at infinity.
Deleting these points does not change geometric genus.

On the curve,

    x dy = v^(-1)d(t v^3) = v^2 dt+3t v dv,
    2c v dv=n t^(n-1)dt.

Consequently

    x dy=(1/c)[1+(3n+2)t^n/2]dt=dS_(n,c).

The primitive is polynomial in t with constant coefficients for each
c!=0; since t=x^3 y, it belongs to the actual coordinate ring R, not just
the function field or normalization. This is full algebraic exactness,
not residue vanishing alone or holomorphic local exactness.

The smallest positive-genus example is

    C: x^2+x^11 y^3=1,
    t=x^3 y,
    x dy=d(t+11t^4/8),
    C isomorphic to {v^2=1+t^3, v!=0}.

## Controls and the missing actual-source hypothesis

For every n>=3 above, the critical locus of p_n on the whole plane is
exactly x=0, with critical value 0. Both partial derivatives vanish on
that line. Away from x=0, vanishing of the y derivative forces y=0 and
then the x derivative is nonzero. No polynomial g can satisfy
J(p_n,g)=1, because its Jacobian would vanish on x=0. No accepted degree
bound or Keller theorem is needed for this exclusion.

The expression S_(n,c) contains 1/c. Treating c as p_n gives a rational
function with a genuine pole along 1+t^n=0: at t^n=-1 its numerator is
-n*t/(2(n+1)), nonzero. It is not a common polynomial potential on A2.
The exact primitive on each smooth fiber therefore cannot be substituted
for the actual identity dS=x dy-f dg with fixed polynomial S and g.

As a negative exactness control, the smooth closed hyperbola xy=1 has
x dy=-dx/x, whose nonzero residue prevents even a rational primitive.
Exactness is not automatic for smooth plane curves, including rational
ones. At n=1 the same construction gives genus zero and the same displayed
differential identity; the positive-genus conclusion explicitly needs n>=3.

The scope stop is only the proposed curve-only or generic-fiber-only
genus inference. Nonsingular polynomial pencils with Keller-compatible
global potentials remain outside the counterexample's hypotheses. No
refutation of a promoted genus theorem or closing statement for JC2.

## Discovery, history and evidence limits

ROOT derived this family from the weighted vector field E=x*d_x-3y*d_y.
For h=x^2 Q(x^3 y), E(h)=2h and div(E)=-2, so
div(((h-1)/2)E)=1. Integrating the resulting Liouville-form identity on
h=1 suggested the explicit curve. The displayed ring and differential
calculation above is the complete proof, not an appeal to this motivation.

Astra independently announced a different elliptic example before ROOT
sent this family: its defining polynomial uses a rational translation of
the derivative of v^2=x^3-x. ROOT did not read its live report. Astra then
manually checked the simpler example after disclosure; that is corroboration,
not independent discovery of this family and not different-model FIRST.

The original 2014 Shende/Bryant discussion at
https://mathoverflow.net/questions/180815/what-are-the-exact-holomorphic-lagrangians-in-complex-2-space
was read in full as a discovery lead. The construction (a,db/da) there
does not by itself prove that its plane image is smooth or embedded, or
that the primitive descends to that image. No such general implication is
used here; the explicit ring isomorphism supplies those missing properties.
The illustrative parametrization (t^2,t^3-t) is nodal at the images of
t=1 and t=-1, so it would not alone test this report's smooth-curve target.
No literature novelty claim or classification theorem is made.

Targeted canonical and report-filename searches for exact Liouville curves,
Legendrian genus and the precise example found no identical campaign
treatment before this task. A later broad genus pattern clipped its output;
it supplies no exhaustive history claim. The existing APPROACHES Section8
genus, Brieskorn and canonical-potential gaps remain, including their
actual-source restrictions. The older S-family residue idea was separately
stopped by its known one-line injectivity argument in notes, September12
08:56; it was not commissioned anew.

Local evidence scope: manual ring substitutions, derivation and ramification
count; no CAS, scientific Python, tests, degree search, cloud computation,
external contact or different-model mathematical review. Administrative
artifact finalization and hashing are not scientific execution. No raw
source PDF or computational certificate is claimed. The report is an
unpromoted stop for one proposed shortcut, not a new positive proof route.

## COLLISIONS

EMPTY (manual). No new machine-tagged OPEN is raised. The broad collision
scanner was not run; the scoped history checks above are not a complete
corpus audit. No automatic control-family or genus-bound successor.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7291`.
- Body SHA-256:
  `8eaf6159fe2588727c21d0db1ed388ad247224ccb644653fe2ed0c3c33dd7e51`.
- Frozen basis: `7bc1fdfbad16daef6b5c8bf2c9469953691cfd1d`.
