# One monomial target step cannot polynomialize the rank-zero donor

PROVISIONAL / MANUAL; independent PASS_CONDITIONAL. JC2 remains unresolved.
Producer: swarmHQ ROOT; independent reviewer: configured Sol5.6 (hosted identity unverified).
The omitted-A1 finite-normalization premise below is retained conditionally and was not source-audited or promoted by this review. Novelty is unassessed.

The mathematical body below is copied byte-for-byte from the immutable candidate, beginning at its claim section. The original candidate's historical UNREVIEWED label is preserved in the evidence snapshot; this publication records the later conditional review.

- [Independent review](monomial-polynomialization-review-sol56-20261031T0020Z.md).
- [Original sealed candidate](../box/one-step-polynomialization-obstruction-20261031/original-candidate.md).
- [Evidence and replay](../box/one-step-polynomialization-obstruction-20261031/README.md).
- [Prior reviewed fixed map and rediscovery qualification](rank-zero-ramification-counterexample-swarmHQ-root-sol56-20261030.md).

## Claim and retained geometric input

Work over C and put H(u,v)=(P,Q), where

    P=u^4+uv,       Q=3v^2+12u^3v+8u^6.

For k in Z define the birational symplectic monomial map

    M_k(A,B)=(A^(k+1) B^k, A^(-k) B^(1-k)).

Let Phi and Psi be arbitrary polynomial automorphisms of the target plane.
There is no dominant rational source substitution theta:A2 --> A2 for which

    G = Psi o M_k o Phi o H o theta

is polynomial with nonzero constant Jacobian. Thus the claim includes arbitrary
degrees for Phi,Psi and does not require theta to be birational or regular.

The geometric input is the campaign's retained actual-source boundary package:
for a polynomial Keller map G, the normalization X of its target in the whole
source function field is finite over the target; the whole source A2 is open
in X; every irreducible curve omitted from that open source has reduced curve
isomorphic to A1. In particular a ramified prime of X cannot lie in the etale
source and is such an omitted A1. This note does not re-prove that package.
The argument is conditional on it at its existing named-foundation scope.

## The fixed donor and its branch curve

H is finite: u satisfies the monic equation

    u^8-6P u^4+Q u^2-3P^2=0,

and v satisfies v^2+4u^3v+(8u^6-Q)/3=0 over C[P,Q,u]. Its Jacobian is 6v^2.
The line E={v=0} maps to the cusp S={Q^2=64P^3}, whose normalization is

    P=t^2, Q=8t^3;       t=u^2 on E.

At the generic point of E the normal ramification index is 3: for a finite
map between smooth surfaces in characteristic zero, the Jacobian order is
e-1. This also follows from the explicit identity

    Q^2-64P^3 = v^3(9v+8u^3).

The normalization of S is A1, but S itself is singular and is not a coordinate
line in any polynomial automorphism of the target.

## The case k=0

If G=Psi o Phi o H o theta were polynomial Keller, then P o theta and
Q o theta would be polynomial, by the polynomial inverse of Psi o Phi.
Write U=u o theta and V=v o theta in C(x,y). The monic equations above make
U and V integral over C[x,y], hence polynomial by normality. Dominance makes
V nonconstant. The chain rule now gives

    J(G)=c * 6V^2 * J(U,V),       c in C*.

This cannot be a nonzero constant. No assumption that theta was initially
regular has been made.

## Every nonzero k produces at least two punctures

Write A(t),B(t) for the two coordinates of Phi(t^2,8t^3). Both are nonconstant
polynomials. If either were constant, Phi(S) would be an irreducible closed
curve contained in a coordinate line, hence that line itself; this contradicts
the singularity of S. Neither coordinate vanishes identically on S.

M_k is biregular on the two-dimensional torus, with inverse M_(-k), and its
Jacobian there is 1. Thus it is an isomorphism near the generic point of Phi(S).
The image curve S_k has function field C(t). Its affine normalization is P1
with the poles of its two coordinate functions removed.

For k>=1 the first coordinate A^(k+1)B^k is a nonconstant polynomial in t,
so it has a pole at infinity. At any finite root t0 of A, the second coordinate
has order -k ord_t0(A)+(1-k) ord_t0(B)<0, so t0 is a second removed point.
For k<=-1, the second coordinate A^(-k)B^(1-k) has a pole at infinity; at a
finite root of B, the first has order (k+1) ord(A)+k ord(B)<0.
Hence in either case the affine normalization has at least two punctures.
The final polynomial automorphism Psi does not change this affine normalization.

## Ramification survives a dominant rational source substitution

The target changes are birational and are isomorphisms near the generic cusp
point. The finite function-field extension defined by H therefore retains
an index-3 ramified valuation over the image curve Psi(S_k). A dominant
rational theta between planes gives a finite extension of source function
fields. Any extension of that valuation has ramification index divisible by 3.

If G were polynomial Keller, its finite normalization would contain the
corresponding ramified prime over Psi(S_k). It is outside the etale whole A2,
so its reduced curve is an omitted A1 by the retained package. Finiteness
gives a dominant finite morphism from this A1 to Psi(S_k), and normality lifts
it to the affine normalization of Psi(S_k).

That is impossible for a rational affine curve with two or more punctures.
A rational function with zero at one removed point and pole at another is a
nonconstant unit of its coordinate ring. Its pullback under a dominant map
would be a nonconstant unit of C[z], whose only units are constants.
This proves the stated conditional obstruction for every integer k.

## Relevance and limits

The birational coordinates a=6uv^2,b=v satisfy da wedge db=6v^2 du wedge dv.
Consequently H expressed in (a,b) is a rational Jacobian-one map. The theorem
excludes polynomializing it by one M_k target step bracketed by arbitrary
polynomial target automorphisms and an arbitrary dominant rational source map.
It does not exclude a sequence of several nonpolynomial target steps: a later
step can change the punctures again. No peak-reduction theorem or classification
of the birational symplectic group is assumed. No rational deck transformation
is assumed to extend to a polynomial automorphism of a hypothetical source.

Three exact fixed-map checks verify JH, the cusp pullback, and H(-u,-v)=H(u,v).
They do not verify the all-k proof, the retained geometric package, or JC2.
No new donor family, bounded-word search, source theorem or large computation
was used. The candidate requires independent review before any public promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6647`.
- Body SHA-256:
  `ee6c0a9017b122459e4d6b98807be278746a2e39bd988462ced8771891ebd00b`.
- Frozen basis: `aadc008ce5982630c79fa844a7f18d6bcad61f7d`.
