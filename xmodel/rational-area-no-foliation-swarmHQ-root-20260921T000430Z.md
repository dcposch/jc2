# The fixed rational exact-area map has no invariant foliation

Producer: swarmHQ (ROOT, gpt-6-astra).
Date: September 21, 2026 UTC.
Basis: 80a39666a7f1ddb4f6a127a63e6d4f7cef179ad7.
Evidence tier: MANUAL with named classification/dynamical-degree imports.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model FIRST.

## Statement and scope

Over C, let

    F(x,y) = (y/(2x), y^4/(16x^4) - x^2).

The earlier reviewed RATIONAL-AREA-NO-PENCIL-1 proves that F is a dominant
RATIONAL map, has Jacobian determinant 1 and generic degree 2, and that no
positive iterate preserves a rational pencil. This report proposes two
strict additions for that SAME fixed map:

1. Its first dynamical degree is exactly 4.
2. No positive iterate of F preserves an algebraic foliation on P2.

An algebraic foliation here means a singular holomorphic rank-one
foliation after projective compactification, equivalently a saturated
rational differential direction, NOT a merely formal or local analytic
direction. Birational transport of such foliations is allowed.

F has a pole along x=0. It is NOT a polynomial Keller map, NOT a JC2
counterexample, and this is NOT a proof of polynomialization impossibility.
There is no finite-web claim. The proposed result excludes an inference
from rational exact-area preservation alone to an invariant foliation;
the actual polynomial-source existence premise remains missing.

## Dependencies and prior work

The [reviewed no-pencil integration](rational-area-no-pencil-integration-swarmHQ-root-20260920T215300Z.md)
and its [producer](rational-area-no-pencil-swarmHQ-root-20260920T211700Z.md)
establish the rational map, degree 2, birational conjugacy and no-pencil
claim. That result proves only lambda1>=3, not the two additions here.
The conditional [polynomial invariant-foliation result](invariant-foliation-keller-swarmHQ-root-20260920T100525Z.md)
uses primitive POLYNOMIAL forms; this rational-map proof does not inherit
its constant-multiplier argument.

Named imports:

- Favre--Pereira, [Foliations invariant by rational maps](https://www.cmls.polytechnique.fr/perso/favre.charles/ratfol6.pdf),
  author PDF dated July 8, 2009, Theorems 4.3 and 4.4 and the exhaustive
  reduction in Section 4.5, printed pages 10, 11 and 16.
- Dinh--Nguyen, [Comparison of dynamical degrees for semi-conjugate
  meromorphic maps, arXiv:0903.2621v1](https://arxiv.org/pdf/0903.2621v1),
  Theorem 1.1: the product formula. This report uses both its curve-base
  case and its same-dimensional, generically finite semiconjugacy case.
  Birational invariance, powers under iteration and topological-degree
  interpretation are the standard properties attached in the old review.

Source-read limits: ROOT read Favre--Pereira body pages 1--3,10--12,16--17
for this comparison, not the entire classification dependency proof.
Theorem/section-heading navigation also emitted headings on pages14--15.
The same cached PDF has SHA256
fb63dcf42b7ebe436f819749751011aadbfc6a59e5e790c2be4af41ac2cb2f9a.
No new Dinh--Nguyen acquisition occurred in this producer tranche.
Its same-dimensional application is an EXPLICIT additional source-fit
obligation for FIRST, not a claim that the old pencil review checked it.
Both frozen campaign and HQ histories were compared before commissioning;
this distinguishes the new stability/classification argument without
claiming exhaustive literature novelty.

## 1. Algebraic stability and exact dynamical degree

The previously checked birational change T(x,y)=(x,y/(2x)) gives

    G = T F T^-1,    G(u,v) = (v, v^3/2 - u^2/(2v)).

In coordinates [U:V:Z] with u=U/Z and v=V/Z, its homogeneous presentation is

    G[U:V:Z] = [2 V^2 Z^2 : V^4 - U^2 Z^2 : 2 V Z^3].             (1)

The tuple has degree4 and no common polynomial factor: a common factor
of the first and third coordinates divides VZ, whereas neither V nor Z
divides the second. Its simultaneous zeroes are exactly

    b0=[0:0:1],    binf=[1:0:0].

Indeed Z=0 forces V=0; on Z!=0 the third coordinate forces V=0 and
then the second forces U=0. Off VZ=0, the image is affine, its first
coordinate fixes v, and its second fixes u^2. Every fiber there is finite.
Thus any irreducible contracted curve is one of the two lines V=0,Z=0.
At their generic points both lines map to

    a=[0:1:0].

Substitution in (1) gives G(a)=a, and a is not a basepoint. Therefore
neither contracted curve, nor its forward point orbit, meets indeterminacy.

For completeness, the no-cancellation implication can be seen directly.
A common divisorial factor in the composed homogeneous tuple for G o G^n
would mean that some curve, at its generic point where G^n is defined,
is mapped by G^n to b0 or binf. Track its successive generic images.
Until the first contraction these are curves; that first contraction
must be one of the two lines just listed, so the image is a and remains
a thereafter. Hence it cannot be b0 or binf. Inductively there is no
common factor at any composition. Starting with degree4, we get

    deg(G^n)=4^n    for every n>=1,    hence lambda1(G)=4.         (2)

This is a proof of algebraic stability, not a fitted list of degrees.
Birational invariance gives lambda1(F)=4. The reviewed generic degree
gives lambda2(F)=lambda2(G)=2; thus for every m>=1 the pair is

    (lambda1(G^m),lambda2(G^m))=(4^m,2^m).                       (3)

## 2. Transfer to the classification covers

Fix m>=1 and suppose G^m preserves a foliation. If it has an algebraic
first integral, normalize the function field of the connected generic
leaf space. Its projective base is a rational curve because it is
dominated by P2. Preservation of the foliation induces a dominant map
on that base. This is a preserved rational pencil and contradicts the
accepted no-pencil result, including positive iterates.

Otherwise Favre--Pereira Section4.5 reduces to kodaira dimension0 or1;
the modular case cannot support the required noninvertible map. Their
Theorems4.3/4.4 apply after birational modifications and a finite cyclic
cover. Let fhat denote the lifted map on the resulting projective surface.
If a model needs resolution, compose the covering map with that resolution;
we still have a dominant generically finite semiconjugacy to G^m.

The same-dimensional case of the Dinh--Nguyen product formula gives

    lambda_j(fhat)=lambda_j(G^m),    j=1,2.                      (4)

There is only relative index0 in that formula. Its relative dynamical
degree is1: the degree-zero pullback is the constant1, so the relevant
mass is constant in n and its nth root tends to1. The GENERIC DEGREE of
the covering itself is not an extra dynamical factor. If a lifting
formulation requires an additional iterate, replace m by that multiple;
the following contradictions are unchanged.

## 3. Exhausting the seven normal forms

The relevant classification interfaces are:

| Case | Feature used |
| --- | --- |
| kappa0(1) | Linear map of a two-dimensional complex torus |
| kappa0(2), kappa0(3) | Ruled surface over an elliptic curve; base fibration preserved |
| kappa0(4) | Product map (x,y)->(x^k,ky) on P1xP1 |
| kappa0(5) | Monomial map with nonsingular integral 2x2 exponent matrix |
| kappa1(1) | (x,y)->(lambda*x,x^m*y^k), preserving x-fibration |
| kappa1(2) | Product map on P1 times an elliptic curve |

We need not descend these fibrations through the finite group. Any
surface map preserving a fibration has, by the curve-base product
formula, lambda1=max(a,b) and lambda2=ab with a,b>=1. Thus lambda1<=lambda2.
Equations(3)--(4) exclude every row except the torus and monomial rows.

### Torus row

Write the lift on C2 as a nonsingular complex linear map L with
eigenvalues alpha,beta, ordered by |alpha|>=|beta|. It preserves the
rank4 lattice. Consequently alpha,beta and their conjugates are roots
of the characteristic polynomial of an integral4x4 matrix and are
algebraic integers. Any affine translation has no effect on this argument.

For a complex torus, lambda1=|alpha|^2 and
lambda2=|alpha*beta|^2. One can verify the first identity using a
translation-invariant positive Hermitian form: the mass of its pullback
by L^n is comparable to the squared norm of L^n, whose nth-root limit
is |alpha|^2. The second identity is the real lattice determinant,
equivalently the topological degree. Diagonalizability is in the normal
form, but even polynomial Jordan factors would not change these limits.

Equations(3)--(4) now force

    beta*conjugate(beta) = lambda2/lambda1 = 2^-m.

The left side is an algebraic integer. The right side is a rational
noninteger, impossible since a rational algebraic integer is an integer.

### Monomial row

Let M be the nonsingular integral2x2 exponent matrix. The generic degree
is |det M|. On the torus, the iterate has matrix M^n. After compactifying
on P1xP1, the pullback bidegrees of its coordinate divisors are the pairs
of absolute values of the corresponding exponent entries; an ample
degree sums these entries and is comparable to a matrix norm of M^n.
It follows that

    lambda1=rho(M),    lambda2=|det M|,

where rho denotes spectral radius. If the eigenvalues were nonreal they
would be conjugate, and |det M|=rho(M)^2=16^m, not2^m. They are therefore
real. One of them is +/-4^m and the other is +/-2^-m by the determinant.
Again an eigenvalue of an integral matrix would be a rational noninteger
algebraic integer, impossible. No additional classification case remains.

This proves the proposed no-foliation conclusion conditional only on the
stated named imports at their precise scope. It is not yet independently
reviewed and is not promoted by this producer report.

## Replay and negative controls

Desk-only over C; no CAS, code experiment, degree interpolation, primes,
random seed or cloud computation. Formula(1), its basepoints, finite
fibers and exceptional images are manually reconstructible above.
Artifact/hash/collision checks are custody tooling, not mathematical tests.

The integrality of lambda1 is essential to this numerical argument.
For M=[[3,1],[1,1]], the monomial map (x^3*y,x*y) has degree2 and
lambda1=2+sqrt(2)>2, while it preserves logarithmic eigen-foliations.
This single hand-check demonstrates why the OLD lower bound lambda1>=3
alone cannot justify the new classification exclusion. No parameter
family or counterexample search is performed. Also the old area map
D=(x^2,y/(2x)) preserves the x-pencil; exact rational J1 alone is not
being confused with the degree4/no-foliation calculation for F.

## Limitations and next test

FIRST must independently attack (1)--(4), all exceptional curves and
composition cancellations, the actual finite-cover lift and exhaustive
classification, same-dimensional source hypotheses, torus/monomial
spectral computations, and the all-positive-iterate quantifier.
No promotion before that check. A GAP stops the claim at its surviving
scope; it does not authorize a new family, web upgrade or donor repair.
The no-web question is outside this report. No polynomial Keller
invariant-structure existence premise is supplied.

## OPENS RAISED

None. The fixed report has a bounded independent proof-review obligation,
not a new campaign-wide mathematical open or scientific descendant.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author whole-body readback completed September21 00:06:56 UTC; final
clarification of the bidegree wording and custody footer followed.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11477`.
- Body SHA-256:
  `985358ee5d6a8d8c306ff433a1768ba960e8e170a931dbd52be093cd0de29036`.
- Frozen basis: `80a39666a7f1ddb4f6a127a63e6d4f7cef179ad7`.
