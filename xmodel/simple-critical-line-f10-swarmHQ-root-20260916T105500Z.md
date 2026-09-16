# A simple critical line maps birationally onto its image: the F10 client

Producer: swarmHQ ROOT (gpt-6-astra), independently co-checked by native
Astra task affine_target_planes, terminal 2026-09-16 10:49:15 UTC.
Date: 2026-09-16 UTC.
Basis: a125c638733b96acc89d8dd169482fb7a4628d1e.
Evidence tier: MANUAL, with standard normalization and Luroth inputs.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model review.

## Statement and scope

C1. Let P,Q belong to C[g,p], with J_(g,p)(P,Q)=c*g, c!=0.
Assume (P(0,p),Q(0,p)) is nonconstant. Its map from A1_p to the
normalization of its image is an isomorphism. In particular
C(P(0,p),Q(0,p))=C(p).

C2. Every intrinsically singular branch of this image, parametrized at
p=p0, has initial orders (m,m+1), m>=2, after an invertible linear
target change and translation. This is a statement about one branch;
a smooth branch through a multibranch singular point is not asserted
to have that pair. The image curve need not be smooth or embedded.

C3. The divisorial valuation g=0 of C(g,p) has ramification index2 and
residue degree1 over its image curve in C(P,Q).

C4. For EVERY complex solution of the literal compact F10 contract
linked below, its receiver A(g,p),B(g,p) satisfies C1--C3. The image
coordinates have degrees 7m and 7n in p, where m=3r+1, n=5r+2.
The reconstructed Keller source has these image values as nonproper
values. This identifies one actual boundary valuation, not all of them.

No solution of that contract, degree exclusion, unique-dicritical
theorem, full passport, new trace inequality, or JC2 conclusion follows.
No literature-novelty claim is made.

## Dependencies and prior work

The exact conditional source interface is
[the compact sufficient contract](f10-compact-counterexample-contract-coordinator-20260909.md),
SHA256 6c6fe089033832c9d33639f8438a43c3dbfd8a28d06e05ef76ee141438de6d7f.
Its sections1--4 explicitly supply receiver polynomiality, J=c*g and
the source substitution. C4 is conditional on its literal equations;
we do not strengthen any necessary-direction source imports.

[The old one-dicritical trace client](trace-place-one-dicritical-astra-20260911.md),
SHA256 c4175ed757a69c6d57fc4f41542cedd6be55f88b6ba88ebe0d974c9fcd7e9663,
STIPULATES normal index2 and tangential degree1. This proof supplies
these two numbers for the specified F10 divisor; it does not discharge
that client's separate one-dicritical assumption or global transport gap.
The compact contract and its coalesced reference do not themselves give
the critical parametrization's primitivity. This is the useful dependency
delta, not an exclusion or a changed all-F10 closing test.

September15 smooth-critical-support controls in notes.md have higher
Jacobian multiplicity; support smoothness is not the first-order condition
used here. Bounded history searches do not establish exhaustive novelty.

Classical inputs: normalization of an affine curve is finite in this
setting; Luroth's theorem for an intermediate subfield of C(p); extension
of a finite map of smooth affine curves to their smooth projective
completions. The local proof and F10 degree calculation are given below.
No contemporary source theorem, scientific computation or external
unreviewed claim supplies the new implication.

## Proof of C1 and C2

Write the expansion in g as

    P=a(p)+g*b(p)+g^2*d(p)+...,
    Q=A(p)+g*B(p)+g^2*D(p)+....

The constant and linear coefficients of the full Jacobian identity give

    b*A' - a'*B = 0,                                      (1)
    b*B' - b'*B + 2*d*A' - 2*D*a' = c.                   (2)

At a point p0 where the critical-line map has zero differential,
a'(p0)=A'(p0)=0. Equation(2) implies (b(p0),B(p0))!=(0,0).
After swapping outputs if necessary, b(p0)!=0; the sign of c changes
under this swap, but its nonvanishing is unchanged. Locally (1) gives

    lambda=A'/a'=B/b,
    lambda'(p0)=c/b(p0)^2 != 0.                           (3)

The first ratio is meromorphic initially. The second makes it regular.
Here a cannot be locally constant: (1) and b!=0 would then force A
constant too, contradicting the nonconstant polynomial image.

Let tau be a local parameter on the image normalization at the branch
in question. If the induced normalization map ramified at p0, then
tau=tau(p) would have tau'(p0)=0. Since a,A are functions of tau,
lambda=dA/da is a meromorphic function of tau. It has no pole, because
its pullback B/b is regular; orders multiply under the nonconstant
local parameter map. Thus lambda is regular in tau, and its derivative
with respect to p vanishes at p0. This contradicts (3). At an immersive
point the normalization map cannot ramify either. It is therefore
unramified at every finite p.

The map to the image curve is finite: a nonconstant coordinate
polynomial makes p integral over C[a,A]. Its lift to the normalization
is finite as well (a finite set of generators over the smaller ring
also generates over the intermediate normalization). That normalization
is rational by Luroth. On projective completions the finite map from
P1_p has every preimage of an omitted target point among the sole
source point at infinity. There is exactly one omitted target point:
at most one by surjectivity, and at least one since the target curve is
affine. Hence its normalization is A1. Our map is a polynomial
A1->A1, everywhere unramified, so its derivative is a nonzero constant.
Its degree is one. This proves C1.

For C2, at an intrinsically singular branch the now-primitive
parametrization has zero differential. Translate p0 and the target
point to zero and retain the above choice b(p0)!=0. Put ord(a)=m>=2.
The regular lambda implies that a has minimal coordinate order.
Equation(3) says ord(lambda-lambda(0))=1; consequently

    (A-lambda(0)*a)'=a'*(lambda-lambda(0))

has order m. Integration in characteristic zero gives
ord(A-lambda(0)*a)=m+1, proving the claimed pair. No assertion about
different branches being disjoint is needed.

## Proof of C3 and the F10 attachment

At a generic smooth point of the image curve choose a target local
equation h transverse to it and a coordinate v along it. Their target
Jacobian is a unit. Write h(P,Q)=g^e*w with w a unit at the generic
point of g=0. The restriction of v(P,Q) has nonzero p derivative,
since the critical-line map is nonconstant in characteristic zero.
Thus the order of J_(g,p)(h(P,Q),v(P,Q)) is e-1. The chain rule and
J(P,Q)=c*g make that order1, so e=2. C1 identifies the residue fields,
proving residue degree1. This is a valuation statement, not finiteness
of the whole polynomial map.

For C4 use exactly the compact contract's orientation:

    z=p^2-g+ell*p-u, R=p*z^3-z^2+u*z, t=z^-1,
    A(g,p)=Ahat(R,t), B(g,p)=Bhat(R,t).

Full inverse polynomiality, not just a truncation, makes A,B ordinary
and gives J_(g,p)(A,B)=c*g. On g=0 put d=p^2+ell*p-u. Then
z=d, deg_p R=7 with leading coefficient1, and deg_p t=-2 as a
rational function. For either output with exponent e=m or n, every
allowed monomial R^i*t^k satisfies i+r*k<=e and hence

    deg_p(R^i*t^k)=7*i-2*k<=7*e-(7*r+2)*k.

The sole monic R^e term has degree7e; all other terms have strictly
lower degree. Cancellation cannot remove it. The now-proved polynomial
restriction therefore has degree7e. In particular it is nonconstant,
and C1--C3 apply. A naive degree argument alone only gives residue
degree dividing gcd(7m,7n)=7; the new local argument rules out7.

Finally the exact source map is U=g^2*(1+g*p), V=g^-1.
For each fixed finite p0 and g tending to0 through nonzero values,
V tends to infinity while the reconstructed outputs tend to
(A(0,p0),B(0,p0)). Thus those image points really are nonproper
values. We do NOT enumerate other source-at-infinity valuations or
identify this curve with the entire nonproperness set.

## Replay and negative controls

Desk-only, characteristic zero, no CAS or computational certificate.
Re-expand the two g coefficients (1)--(2), then the rational degree
inequality. There are no random seeds, modular primes or solver claims.

For every m>=2, the explicit pair
P=g+p^m, Q=g*p+(m/(m+1))*p^(m+1) has J=g and critical image
(p^m,(m/(m+1))*p^(m+1)). It checks C2 and refutes a false assertion
that simple critical support forces a smooth image. The pair (g,g*p)
also has J=g but contracts the critical line, checking the indispensability
of the nonconstant-image hypothesis. If J has higher g multiplicity,
the right side of (2) becomes zero: the present proof then supplies no
nonzero Gauss derivative. This is a scope control, not a claimed
counterexample to birationality under every weaker hypothesis.

## Limitations and next test

The bounded tranche closes with this source bridge. No coefficient job,
scalar/r3 restart, control-family extension or provisional descendant
is selected. Before use, different-model review must attack (1)--(3),
the normalization argument, exact F10 top terms and the one-divisor scope.
Uniqueness of the omitted divisor and the old global transport gap remain
unsupplied; no new global closing test has been obtained.

## OPENS RAISED

None. Existing global gaps are not reissued as a fresh work queue.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9278`.
- Body SHA-256:
  `cd6c5a0d0761db43f5c07481b7085a26b19e50df730d54960d5913bcdb66d975`.
- Frozen basis: `a125c638733b96acc89d8dd169482fb7a4628d1e`.
