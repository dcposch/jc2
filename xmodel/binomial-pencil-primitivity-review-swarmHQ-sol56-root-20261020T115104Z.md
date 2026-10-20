# Coprime binomial pencils of a Keller pair: independent FIRST

Producer: swarmHQ ROOT. Independent reviewer: retained native
`affine_radial_first_sol56_2157`, Sol5.6-assigned seat; actual hosted
model identity unverified. ROOT transcribes and integrates the review.
Mathematical terminal: 2026-10-20 11:47:18 UTC, CONFIRMED.
Required-context custody addendum: 11:51:04 UTC, gap closed, verdict unchanged.
Lifecycle: PROMOTED at the exact scope below. Evidence: MANUAL with standard
function-field, curve and UFD imports; not formalized or peer reviewed.
External novelty UNKNOWN. No JC2 proof or counterexample.

## Exact statement

Let P,Q in C[x,y] have nonzero constant Jacobian determinant. For coprime
positive integers m,n, the field C(P^m/Q^n) is algebraically closed in
C(x,y). Equivalently, this rational pencil has geometrically integral
generic fiber.

This is not a statement that C(P,Q)=C(x,y), that the generic fiber has
genus zero, or that every special fiber is irreducible.
Target translations and invertible affine target changes are covered
because they preserve the Keller condition.

## Independently reconstructed argument

Put L=C(x,y) and r=P^m/Q^n. Constant nonzero Jacobian makes P,Q
algebraically independent, individually squarefree and coprime: a common
prime factor, or a squared prime factor in either coordinate, would
divide the Jacobian determinant.

On the open set PQ != 0,

    dr = P^(m-1) Q^(-n-1) (m Q dP - n P dQ)

is nowhere zero, since dP,dQ are a basis of the cotangent module there.

Let E be the relative algebraic closure of C(r) in L. It is a finite
extension of C(r). Its smooth projective curve is dominated rationally by
A2; restriction to a suitable line supplies a nonconstant rational map
P1 to that curve. Extension of the map and Riemann-Hurwitz show genus zero.
Thus E=C(H), with H primitive in L, and r=R(H) for a rational function R.
We must show d=deg(R)=1.

Write H=A/B with coprime polynomials. A divisor-empty finite value alpha
has A-alpha B a nonzero constant; a divisor-empty infinity has B constant.
There can be at most one such value: two independent constant linear
combinations would make both A and B constant.
If one is omitted, a Mobius change sending it to infinity makes H
polynomial without changing E or its relative algebraic closedness.

If a ramification point alpha of R maps outside {0,infinity}, then alpha
must be a divisor-empty value of H. Otherwise choose a prime divisor C
of its fiber. The order of r-R(alpha) along C is at least the ramification
index, hence at least two, so dr vanishes at its generic point.
Here r is a nonzero unit, and coprimality of P,Q implies both are units.
This contradicts the displayed nonvanishing. A local parameter treats
alpha=infinity in exactly the same way.

Suppose such an off-{0,infinity} ramification point exists. Move its
omitted H-value to infinity. Then H is primitive polynomial and R(infinity)
is nonzero and finite. In particular ALL zeros and poles of the transformed
R are finite; this is essential for the following polynomial factorization.

For every finite a, the gcd of multiplicities of the irreducible components
of H-a equals one. If that gcd were k>1, unique factorization would give
H-a=c G^k. Then G is algebraic over C(H), so primitivity forces G into
C(H). The valuation at the point H=a would give 1=k ord_a(G), impossible.

A zero a of R of order e gives source divisor multiplicities
e ord_C(H-a). Because r=P^m/Q^n is reduced, each is divisible by m.
The preceding gcd-one property implies m divides e. Similarly n divides
every pole order. Therefore

    R = c0 U^m / V^n

for coprime polynomials U,V in one variable. Bezout gives that U(H),V(H)
are coprime polynomials in x,y. The equality

    P^m/Q^n = c0 U(H)^m/V(H)^n

is an equality of reduced UFD fractions. Uniqueness implies
P=c1 U(H) and Q=c2 V(H), for nonzero constants c1,c2.
This contradicts algebraic independence of P,Q. Thus no ramification of
R lies over a value outside {0,infinity}.

Let k0 and kinfinity count distinct points in the zero and pole fibers
of R:P1->P1. Riemann-Hurwitz now gives

    2d-2 = (d-k0) + (d-kinfinity).

Both counts are positive, so each is one. Consequently R is a nonzero
constant times the dth power of a Mobius function. If d>1, r is a proper
dth power in L. A prime factor of squarefree P has valuation m in r,
and a prime factor of squarefree Q has valuation -n. Thus d divides
both m and n. Their coprimality forces d=1, as required.

## Fixed-target construction obstruction

If a dominant rational donor (p,q) has p^m/q^n=R(H) with deg R>1 for
coprime positive m,n, it cannot be transformed into a polynomial Keller
pair by a dominant rational SOURCE substitution retaining these target
functions. The induced field embedding preserves the proper algebraic
subextension C(R(H)) subset C(H), contradicting the theorem for the
resulting polynomial pair.

This includes a finite source-field enlargement when the resulting
source is a rational plane and the same functions become polynomial
Keller coordinates. It does NOT allow arbitrary birational changes
of target coordinates or assert an obstruction for every donor.

## Controls, relation and remaining gaps

For noncoprime m,n, the identity pair already gives a proper power.
The NON-KELLER pair (x^2,y^2) gives a square even for coprime m,n.
The theorem includes m=n=1.

The retained ONEBAD theorem permits at most one nonreduced affine fiber
of a target rational pencil. The pencil u^m/v^n has two when m,n>1,
so that theorem does not directly supply this result. The new proof
uses primitive-polynomial fiber multiplicities and reduced-fraction
extraction after the omitted-value reduction.

No generic-genus bound, rational-pencil existence, finite-normalization
equality B=R, surjectivity, degree-one field-extension conclusion,
new degree bound, or arbitrary-target exclusion follows.

## Evidence and review custody

[Sealed producer](binomial-pencil-primitivity-swarmHQ-root-20261020T113905Z.md):
133 lines/6739 bytes, regular0444, SHA256
627b104d7d12654c9493deaebff5519417a029514b6789ea8945e13bbbbba960.
Its manifest: 696 bytes, regular0444, SHA256
805c5a765fbd93b5b0e5afb87195275f3cbf426b34a63741201411c7bf4631f9.
Producer remains unchanged with its historical UNPROMOTED label.

[ONEBAD review context](one-bad-fiber-review-swarmHQ-sol56-root-20261018T211903Z.md):
114 lines/6334 bytes, regular0444, SHA256
a170f58d59986c0dcb4e65a77e6d199f21c7affd7343565c8fdd924cdd013934.
Reviewer checked whole-set metadata before bodies, manifest first,
canonical verifier VERIFIED, then read producer and context whole.
Frozen packet112 and STATE200 were read whole; own unchanged exact-pin
completed governing reads were reused.

The original terminal disclosed that changed APPROACHES was only read
at lines1--30, despite a matching hash. No promotion was accepted then.
The separate 11:51:04 addendum completed lines31--971, reported compliant
unclipped windows, and matched the postpin: 971 lines/68771 bytes, SHA256
6586035fdc858a342cda6b56e793dd09f44231f68dfcdf30a4ca109ab4599a8d.
Original deviation is preserved; completed custody did not change the
mathematical verdict. All stipulated packet/STATE/input pre/post pins matched.
ROOT separately reverified the producer and all three scientific input
hashes/modes after receipt. No new network source, CAS, model CLI,
formalization, descendants or protected-tree access was used in this review.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7484`.
- Body SHA-256:
  `981404f78862bc744c5a07665c32a3bb211c02a75783c96fd71cfd8aba4744d8`.
- Frozen basis: `1971b4d095fa059d1d7ac3c9a120c4c93e49f244`.
