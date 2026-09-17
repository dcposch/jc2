# Integral back coordinates obstruct rational Keller donors

Producer: swarmHQ ROOT (Astra assigned context; hosted identity not exposed).
Date: September 17, 2026 UTC.
Basis: 92e7761f6d4e4bcb87c5a0d500506d1fe675d3e2.
Evidence: MANUAL characteristic-zero proof with named classical imports.
Lifecycle: PRODUCER-CHECKED, PROVISIONAL pending different-model review.
Native Astra supplied an independent same-model manual co-check; not FIRST.
Claim: INTEGRAL-BACK-COORDINATE-DONOR-1. No literature-novelty claim.

## 1. Exact criterion

Let p,q be rational functions in C(x,y), with

    J_(x,y)(p,q)=c in C*,       A=C[p,q] subset C(x,y).

Assume BOTH x and y are integral over A. For every dominant rational map
sigma:A2_(s,z) --> A2_(x,y), if

    H=(p composed sigma, q composed sigma)

is polynomial on the WHOLE source A2 and has nonzero constant Jacobian,
then sigma is a polynomial Keller map and (p,q) is a polynomial
AUTOMORPHISM. In particular a genuinely rational donor satisfying the
two integrality hypotheses cannot be repaired by ANY finite-degree
rational source substitution. Dominance of a rational map between these
planes already makes its function-field inclusion finite.

This does NOT say sigma is an automorphism. If the donor is an
automorphism, H can still carry whatever unresolved Keller problem sigma
already carries. No assertion places arbitrary Keller maps or rational
constant-Jacobian pairs in the integral-back-coordinate class.

## 2. Proof of the criterion

Write sigma=(u,v), with u,v in C(s,z), and R=C[s,z]. Dominance makes
substitution an injective field homomorphism C(x,y) -> C(s,z).
A monic equation for x over A therefore becomes a monic equation for u
whose coefficients lie in C[H1,H2] subset R. Likewise v is integral over
R. Since R is integrally closed in C(s,z), BOTH u,v lie in R.
This is not an assumption that a rational source substitution was regular.

The chain rule in the rational function field now gives

    J(H)=c*J(u,v).

Consequently sigma is polynomial with nonzero constant Jacobian and is
etale. Its image is a Zariski-open subset of A2. The closed complement
contains no irreducible curve: if V(b) were omitted, for an irreducible
nonconstant b in C[x,y], then b(u,v) would be a nowhere-zero polynomial
on C2, hence a nonzero constant. Injectivity of substitution forbids this.
Thus the complement of the image is finite. This uses etaleness for
openness; dominance alone does not imply cofinite image.

Here is the pole argument explicitly. Suppose p=a/b in reduced form and
b is nonconstant. Polynomiality of p(u,v) means

    a(u,v)=b(u,v)*H1

as polynomials. Choose an irreducible factor beta of b and a point
Q in V(beta) outside V(a) and the finite omitted set. Such Q exists:
coprimality makes V(beta) intersect V(a) finite. Take a preimage of Q
under sigma and evaluate the identity, obtaining a(Q)=0, a contradiction.
Therefore p is polynomial; the same argument makes q polynomial.

We can now regard A as a subring of C[x,y]. Its two integral generators
x,y make C[x,y] a FINITE A-module. Hence G=(p,q):A2 -> A2 is finite
and etale. A finite connected etale cover of the complex affine plane
has degree one (analytically C2 is simply connected); a finite birational
map to the normal affine plane is an isomorphism. Thus G is a polynomial
automorphism. This is the classical finite-etale endpoint, not an
assumption of the Jacobian Conjecture.

The pole argument is the same elementary lemma already independently
reviewed in [the fixed-source quotient review, section D](running-torus-quotient-review-swarmHQ-sol-20260916T011400Z.md).
The new composition here uses both integral back coordinates to obtain
an actual polynomial etale source map before applying that lemma.

## 3. Uniform Weierstrass multiplication application

Fix ANY a in C. In the rational plane field let

    t=y^2-x^3-a*x,
    E_t : Y^2=X^3+a*X+t over C(t),
    (U_m,V_m)=[m](x,y),         integer m>=2.

The discriminant -16*(4*a^3+27*t^2) is nonzero in C(t), including a=0.
This is the generic smooth elliptic curve, not a claim that all closed
fibers are smooth. Its function field is C(x,y), with the indicated
embedding of C(t). Multiplication gives rational functions U_m,V_m.
They satisfy

    V_m^2-U_m^3-a*U_m=t.                           (1)

The standard invariant-differential identity is RELATIVE over C(t):

    [m]^*(dX/(2Y))=m*dx/(2y) modulo dt.

Wedging on the right by dt eliminates that ambiguity. Since
dt=2y*dy-(3x^2+a)*dx and, by (1),
dt=2V_m*dV_m-(3U_m^2+a)*dU_m, it gives

    dU_m wedge dV_m=m*dx wedge dy,
    J(U_m,V_m)=m.                                 (2)

For integrality use the classical division-polynomial formulas, before
substituting t as a plane function. There are polynomials

    phi_m(X;a,t), Psi_m(X;a,t) in C[a,t][X]

with U_m=phi_m(x;a,t)/Psi_m(x;a,t), where phi_m is MONIC of
X-degree m^2 and Psi_m=psi_m^2, after eliminating Y^2, has X-degree
m^2-1 and leading coefficient m^2. This includes even m: psi_m itself
may involve Y, but its square is a polynomial in X. For m=2,
Psi_2=4*(X^3+a*X+t), not an incorrectly degree-one denominator.

Set A_m=C[U_m,V_m]. Equation (1) puts t in A_m. Therefore

    phi_m(T;a,V_m^2-U_m^3-a*U_m)
      -U_m*Psi_m(T;a,V_m^2-U_m^3-a*U_m)=0 at T=x   (3)

is a MONIC polynomial in the independent unknown T over A_m.
Its leading term cannot cancel, since the second summand has smaller
T-degree. Thus x is integral over A_m. The monic equation

    y^2=x^3+a*x+t

then makes y integral over A_m[x], hence over A_m by transitivity.
No discriminant, x, y, t or division polynomial is inverted in this
integrality conclusion. Integrality is over the actual ring A_m, not
merely its fraction field.

Finally U_m is not polynomial on the original A2. Over an algebraic
closure of C(t), any nonzero m-torsion point belongs to the affine
curve E_t minus {O}, but [m] sends it to O. The target coordinate X has
a pole at O, so its pullback U_m has a pole at that affine point.
A polynomial in x,y would restrict to a regular function on the entire
affine generic curve, even after scalar extension. This is a contradiction.
Nonzero m-torsion exists in characteristic zero for EVERY m>=2.

The criterion consequently excludes EVERY dominant rational sigma with
(U_m,V_m) composed sigma a whole-plane polynomial Keller pair, for all
fixed a and all m>=2. The same holds for negative m with |m|>=2 by the
polynomial target involution (U,V)->(U,-V). Normalizing V_m by 1/m
does not change A_m and gives the same exclusion.

## 4. Classical imports and source read scope

- Etale maps are open; a finite connected etale cover of complex A2 is
  trivial; polynomial rings are normal. These standard algebraic-geometric
  facts are explicitly used, not new campaign claims.
- Division polynomials and their leading terms: Naskrecki--Verzobio,
  [Common valuations of division polynomials](https://doi.org/10.1017/prm.2024.7),
  published online February 26, 2024, section 2, properties (A)--(C).
  ROOT read these selected identities/degree statements and the defining
  formulas, not its valuation theorem or whole proof. The universal
  polynomial dependence is also given by the usual recurrence formulas.
- Elliptic multiplication, torsion and invariant differentials: Milne,
  [Elliptic Curves, second edition](https://www.jmilne.org/math/Books/EC2.pdf),
  II section 6, especially 6.1/6.3, and III 3.9--3.14. Selected statements
  were read, not the whole book. Invariant differentials pull back by m
  because the tangent map of [m] at the identity is multiplication by m;
  the calculation in (2) is then an absolute two-form calculation.

No CAS, scientific Python, prime sampling or numerical evidence is used.
This is MANUAL with named classical imports, not proof-assistant verification.

## 5. Controls, comparison and scope limits

The nonzero CONSTANT condition on J(G) matters. If it is dropped, take

    G(x,y)=(x,y/x),        sigma(s,z)=(s,s*z).

Then H is the identity and both x=p and y=p*q lie in C[p,q], yet G is
not polynomial. Here J(G)=1/x and J(sigma)=s: cancellation occurs before
sigma becomes etale. Thus integrality alone is not the criterion.

For the positive control G is any polynomial automorphism and sigma is
the identity. The criterion correctly allows H=G. On the elliptic side
m=1 is the identity and m=-1 is (x,-y); the exclusion deliberately does
not include them. No claim of non-polynomiality is made for these cases.

The a=0 elliptic conclusion overlaps the old
[September14 isotrivial test](../notes.md#2026-09-14-2052-utc--elliptic-multiplication-fails-the-normalization-screen),
which used positive grading and torsion divisor class group. The
[fixed Legendre-tripling exclusion](legendre-tripling-source-obstruction-swarmHQ-root-20260916T093800Z.md)
uses a different parametrization and a ramified target line. Neither is
reverified or contradicted here. The present monic-integrality argument
also covers nonisotrivial fixed a!=0, every multiplication order and
arbitrary finite rational source substitutions, without a coefficient farm.

The criterion can be applied again after a target change ONLY if its
actual new target ring still makes BOTH back coordinates integral and
its rational Jacobian remains a nonzero constant. Polynomial target
automorphisms preserve those hypotheses. Arbitrary birational target
changes need not preserve them; no such extension is asserted.
No general elliptic family, arbitrary isogeny or arbitrary rational
constant-Jacobian donor is excluded. No candidate plane counterexample
or all-source integrality theorem is supplied; JC2 remains unresolved.
Stop this multiplication construction. No next multiplier, parameter,
division-polynomial search, normalization calculation or automatic
target-repair family follows.

## OPEN(S) RAISED

None. The general source-integrality/properness gap remains unchanged;
this report raises no new bounded experiment or successor family.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10101`.
- Body SHA-256:
  `a4cb7c23123c2dc4eb6e6d1401d7d0c5d1a08dfd8922e4c4c212b6ad95b54061`.
- Frozen basis: `92e7761f6d4e4bcb87c5a0d500506d1fe675d3e2`.
