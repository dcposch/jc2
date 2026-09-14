# Smooth rational finite cubic donors: adjunction and a local pole bound

ROOT, September12,2026. MANUAL / UNPROMOTED. Original report opened
02:36UTC; publication reserve02:49/HARD02:52UTC, no extension.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d. JC2 unresolved.

## Exact claim

SMOOTH-CUBIC-DONOR-1: let Y be a smooth rational projective complex
surface and phi:Y->P2 a finite morphism of degree3. For every target
line ell, put U=Y minus (Supp Ram(phi) union Supp phi^*ell).
There is no dominant everywhere-defined regular morphism A2->U,
of any degree. Finiteness and smoothness of Y are essential hypotheses
of this argument. No singular normalization or merely generically finite
completion is covered, and no universal JC2 conclusion follows.

The proof splits on the sectional genus of L=phi^*O(1). Positive genus
uses adjunction and a local ramification pole bound. Genus zero reduces
to the already reviewed CUBIC-SCROLL-DONOR-1 on F1. These are exhaustive
for this stated family, not for arbitrary cubic block quotients.

## Positive sectional genus

The ample globally generated divisor L has L^2=3. A general member of
|L| is smooth connected, hence irreducible, by Bertini and connectedness
of ample effective divisors. Write its genus as

    g=1+(K_Y+L).L/2 >=0,       R=Ram(phi) ~ K_Y+3L.

R is the effective divisor of det(dphi), WITH multiplicities. Since Y
is rational, chi(O_Y)=1. Surface Riemann--Roch and Serre duality give

    chi(K_Y+L)=g,       h^2(K_Y+L)=h^0(-L)=0.

If g>=1, a nonzero section sigma of K_Y+L exists. Its cube gives a
nonzero section tau of 2K_Y+R, since 2K_Y+R ~ 3(K_Y+L).
Viewed as a rational tensor-square two-form, tau has poles bounded by R.
Counting reduced boundary coefficients on Y alone is insufficient: the
ramification curve can be singular. The next local check handles every
exceptional valuation created when resolving that boundary.

### Local finite-cubic lemma: (Y,R/2) is log canonical

A finite map between smooth surfaces is flat: a finite module from a
Cohen--Macaulay source over a regular local target of the same dimension
is free. Thus every complete fibre has length3. At an individual point
its local length n is at most3. The differential cannot have rank zero.
Indeed the two pulled-back target parameters would lie in m^2 in a
regular two-dimensional local ring. A quotient of length<=3 would then
have basis 1,s,t, forcing m^2 into their two-generated ideal. Modulo
m^3 this would require two quadratic initial forms to span the
three-dimensional vector space m^2/m^3, impossible.

Consequently analytic local coordinates put phi in the form
(s,t)->(s,h(s,t)), with ord_t h(0,t)=n<=3 after centering the target.
The ramification equation is h_t. For n=1 this is a unit; for n=2
it is smooth. For n=3, Weierstrass preparation and completing the square
express it up to a unit as

    r=t^2+a(s).

The case a identically zero is allowed: a doubled smooth divisor.
Coordinate changes have unit Jacobian and do not affect discrepancies.

Here is an elementary valuation check, avoiding a singularity-classification
import. Let v be a divisorial valuation centered at the local surface
point, evaluated on a smooth model at its generic divisor. Put
a0=v(s), b0=v(t), A_v=1+ord_v(ds wedge dt). For regular local functions
f,g, expansion in a generic divisor uniformizer gives

    ord_v(df wedge dg) >= v(f)+v(g)-1.                 (1)

The candidate leading terms in the normal differential cancel; further
cancellation only raises the order. Applying (1) to s,t gives
A_v>=a0+b0. The exact identity dr wedge ds=2t dt wedge ds gives

    v(r)+a0-1 <= b0+A_v-1,
    v(r) <= A_v+b0-a0 <= 2A_v.                       (2)

Units in the local equation do not affect v(R). Thus every exceptional
divisor satisfies A_v-v(R)/2>=0. At strict divisors on Y, R has
multiplicity at most2 (also the tame generic formula e-1 with e<=3),
so the same inequality holds. For smooth simple ramification the regular
coordinate inequality A_v>=v(s)+v(t) suffices directly. Points off R
are automatic. Analytic local coordinates test these same algebraic
divisorial orders. This proves precisely log canonicity of (Y,R/2).

### Logarithmic extension and the A2 contradiction

Take a log resolution rho:Y'->Y of the reduced boundary
Supp(R) union Supp(phi^*ell), with all centres in that boundary, and
let B' be its reduced total inverse image. On an exceptional divisor
E the coefficient of

    2(K_Y'+B') - rho^*(2K_Y+R)                       (3)

is 2A_E-v_E(R)>=0. On a strict R component it is 2-mult_R>=0;
other strict boundary components have coefficient2. Off the boundary
it is zero. Hence (3) is effective and rho^*tau is a nonzero global
section of 2(K_Y'+B'). This includes ramified target lines, nonreduced
line pullbacks and arbitrary contacts: their only role is enlarging
the actual boundary, not imposing a generic-position assumption.

Suppose f:A2->U is dominant regular. Resolve its rational extension
from P2 to Y' by point blowups outside A2, giving f':Z->Y' and the
reduced SNC boundary B_Z=Z-A2. Since f'^{-1}(B') is supported on B_Z,
pullback takes logarithmic two-forms to logarithmic two-forms, and
likewise their tensor squares. Locally this follows by writing each
pulled-back boundary equation as a unit times a boundary monomial;
its logarithmic differential has only simple poles. Therefore
f'^*rho^*tau is a nonzero section of 2(K_Z+B_Z). Dominance and
characteristic zero ensure nonvanishing of the differential pullback.

On A2 this section is h(x,y)(dx wedge dy)^2 with h a nonzero polynomial.
At the generic point of the strict original infinity line its pole
order is deg(h)+6>=6: use x=1/t,y=s/t and
dx wedge dy=-t^-3 dt wedge ds. The line bundle 2(K_Z+B_Z) permits
pole order at most2. Point blowups leave this generic valuation unchanged.
This contradiction proves the entire positive-sectional-genus case.

## Genus zero

If g=0, then K_Y.L=-5. Riemann--Roch gives chi(L)=5, while
h^2(L)=h^0(K_Y-L)=0 because (K_Y-L).L=-8 and L is ample.
Thus h^0(L)>=5. The complete linear series defines a finite morphism
psi:Y->Z subset P^r, r=h^0(L)-1>=4: a contracted curve would have
L-degree zero, and proper quasi-finite maps are finite. Give the image
its reduced irreducible structure; it is nondegenerate. The degree
bound for a nondegenerate projective surface and the projection formula
give

    deg(Z)>=r-1,        3=L^2=deg(psi)*deg(Z).

It follows that r=4, deg(Z)=3 and deg(psi)=1. The classification of
varieties of minimal degree now says that Z is the scroll S(1,2) or
S(0,3), the cone over a rational normal cubic. Linear spaces, quadrics
and Veronese-type cases have the wrong degree/dimension. The two scroll
parameters are nonnegative and sum to3, so these are exhaustive.

Both scrolls are normal. S(1,2) is smooth. The cone S(0,3) is smooth
away from its vertex and its vertex chart is the third Veronese subring
of C[u,v], the invariant ring of scalar mu_3; it is normal. A finite
birational morphism onto a normal variety is an isomorphism, so psi
is an isomorphism. Smoothness of Y rules out the singular cone.
Hence Y is the smooth cubic scroll F1, with polarization E+2f.

Invoke the already independently reviewed CUBIC-SCROLL-DONOR-1, whose
quantifiers cover every finite degree3 morphism on F1 and every target
line, with a regular dominant A2 first leg of arbitrary degree. The
identification Y=F1 does not require the given three-dimensional net
to be generic. That theorem handles both the squarefree and double-root
net types. It therefore excludes the remaining g=0 case.

## Dependencies, controls, source history and scope

This report imports the following standard foundations, not newly formalized
or reproved here: surface Riemann--Roch and Serre duality; Bertini and
ample-divisor connectedness; finite flatness in the smooth equidimensional
case; analytic inverse function/Weierstrass preparation; surface resolution
and resolution of rational maps; finiteness of proper quasi-finite maps;
the projection formula and finite-birational-to-normal isomorphism.
The local discrepancy bound and the infinity-pole contradiction are
explicitly proved above. The minimal-degree classification is a separate
named external theorem, not a classification of all triple planes.

Primary source: Eisenbud--Green--Hulek--Popescu,
[Small Schemes and Varieties of Minimal Degree](https://arxiv.org/pdf/math/0404517),
version5 November15,2004, printed pp1--2, inequality(*) and Theorem0.1.
Those TWO pages were read completely by PDF-to-stdout; the remaining
25 pages and the historical classification proof were not audited.
Frozen PDF box/smooth-cubic-adjunction-astra-20260912/eghp-minimal-degree.pdf
SHA39c85a00fe9b133134acadddbeb0bdaeafbffb5d1bcb9f71536624e8597032b4.
No theorem beyond the stated degree bound and classification is charged.

Accepted internal dependency, freshly read WHOLE before composition:
[Cubic-scroll producer](cubic-scroll-donor-exclusion-root-20260912.md)
SHAf5abd9086559b1cfdd6900baafcf339c1a8ad394917ab3141d23bc999403545a;
[different-model Fable gate](cubic-scroll-donor-gate-fable5-20260912.md)
SHAc2f52680637bec1c7d7570bd07466eb408ba012dd6912c7ce89a6413677ec2cc.
The gate confirms A--E at manual-proof tier with its named standard
imports. This new report uses exactly that statement, not a wider
interpretation or a fresh assurance gate on the already accepted theorem.

Controls and failed stronger readings:

- g=0 has no adjoint section from the RR argument; the old F1 theorem
  is genuinely needed. Its double-root example has an A2 etale locus
  before deleting a target line, so one must not omit phi^*ell globally.
- A local degree4 map (s,t)->(s^2,t^2) has rank zero at the origin.
  Thus the finite-cubic rank argument cannot be silently used in all
  degrees. The example controls this lemma, not a counterexample to a
  broader donor-exclusion statement.
- Resolving a singular finite cubic normalization need not leave a
  FINITE map to P2. Its exceptional curves are contracted, their local
  fibre lengths are not bounded by3, and the local argument above no
  longer applies. No exclusion of all cubic intermediate fields follows.
- A merely rational map from A2 is not covered: its indeterminacy may
  lie inside A2, destroying the strict-infinity-only argument.

For a genuine factorization of a plane Keller map through such a Y,
the chain rule forces the first leg to avoid Ram(phi), while its target
affine image forces avoidance of phi^*ell. The first leg is dominant
because the composite is dominant and phi is finite. Thus the theorem,
if confirmed, excludes precisely this smooth finite cubic donor route.
Rationality of Y is explicitly assumed; no additional unirational-surface
classification is required by the stated claim.

History and decision: the F1/all-line result is already known in this
campaign; log plurigenera and minimal-degree classification are classical.
The new attachment is positive-genus ramification control plus an
exhaustive reduction within the stated smooth rational finite family.
Selected canonical and scoped xmodel checks did not find this exact
attachment; no corpus-wide or external novelty claim is made. No global
strategy reranking, proof of JC2, actual scalar pair or counterexample.
One different-model FIRST gate is required before promotion. No singular
normalization or higher-degree descendant is authorized by this report.

QUANTITY: dominant regular A2 first-leg existence for every stated
smooth finite cubic donor. CHEAPEST TEST: manual local fibre length,
valuation inequality, RR and exact theorem-interface composition.
No code/CAS/scientific execution, numerical wall estimate or AWS allocation.
No new canonical OPEN is created. The singular/nonfinite boundary is an
explicit scope limit, not an implicit missing step in the stated theorem.

Astra's positive-genus co-research is separately active under its original
02:51/02:54 clocks; its live body is NOT an input to this ROOT proof.
ROOT supplied its own frozen valuation delta, so neither author claims
blind independence from that mathematical hint. Same-model agreement is
not the different-model promotion gate. Terminal report intake, if any,
is recorded separately after both frozen proofs exist.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12300`.
- Body SHA-256:
  `cf8089fa710c0f5828c1e82801e10ad1a7c2f3a5e271f8cd51bf6d8b9e2d6180`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
