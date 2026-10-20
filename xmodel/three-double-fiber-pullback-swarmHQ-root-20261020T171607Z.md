# Three double-fiber values: a pullback-primitivity extension

PROVISIONAL / MANUAL / UNREVIEWED. ROOT producer; THREE1708.
No external novelty claim. No proof or counterexample to JC2.
Basis: 9d71ad3b0e788d6fd31b58720a1497966d29bcef.

## Proposed statement

Let F=(P,Q):A2_C -> A2_C be polynomial Keller. Identify
K=C(u,v) with its image in L=C(x,y). Let a,b in C[u,v]
be coprime and algebraically independent, and put f=a/b.
Assume C(f) is relatively algebraically closed in K.

For finite lambda, the affine fiber divisor is div(a-lambda*b);
for infinity it is div(b). Empty divisors are reduced.
Suppose at most THREE of these fiber divisors are nonreduced,
and EVERY component of EACH of these nonreduced divisors has
multiplicity at most TWO.

Then C(f) is relatively algebraically closed in L.
Affine basepoints are allowed. No generic-genus hypothesis is imposed.

This is an additional sufficient criterion, not a replacement for
[TWO1323](two-bad-fiber-review-swarmHQ-astra-root-20261020T134316Z.md),
which allows arbitrary multiplicities at its at-most-two bad values.

## Proof

Suppose a finite intermediate curve field E strictly contains C(f)
inside L. A suitable source line dominates its smooth projective
curve model. Riemann-Hurwitz implies that curve is rational.
Write E=C(H), f(P,Q)=R(H), with R:P1 -> P1 of degree d>1.

The following two elementary facts are the same ones used in TWO1323;
they are recalled here to make the new counting step's inputs explicit.

First, F is dominant, etale and quasi-finite. Pullback of any target
prime polynomial is nonconstant, hence has a source prime divisor.
Quasi-finiteness prevents contraction of that divisor to a point.
Etaleness gives index one. Thus EVERY target affine prime is
detected with the same multiplicity; reduced divisors stay reduced.
Likewise a(P,Q),b(P,Q) are coprime: a common prime would be
contracted into their finite base locus. They remain independent.

Second, EVERY H-fiber has an affine divisor. Indeed write H=c/e
in coprime polynomials. An empty pole fiber makes e constant.
An empty finite alpha fiber makes c-alpha*e a nonzero constant.
Either case gives a polynomial Mobius generator T of C(H).
Writing R(H)=U(T)/V(T), with U,V coprime in C[t], gives coprime
U(T),V(T) by Bezout. Uniqueness of reduced fractions implies
a(P,Q)=gamma*U(T), b(P,Q)=gamma*V(T), gamma in C*,
contradicting their algebraic independence.

Take a ramification point alpha of R, above lambda. A prime
component of H=alpha has positive multiplicity m; on that prime,
the composite fiber has multiplicity e_alpha(R)*m. This also
holds at infinity using reciprocal local parameters. Prime detection
and the assumed target multiplicities give e_alpha(R)<=2.
Moreover lambda is one of the at-most-three nonreduced fiber values.
Every ramification index is therefore TWO, and all branching is
over at most THREE values.

Each branch fiber contains at most floor(d/2) ramification points,
each contributing one. Riemann-Hurwitz yields

    2d-2 <= 3 floor(d/2).

For d=2k+1 this gives 4k<=3k, hence d=1.
For d=2k it gives 4k-2<=3k, hence d=2 or d=4.
The hypothetical d>1 is therefore 2 or 4.

If d=2, there are exactly two distinct branch values, each with
one point of multiplicity two. If d=4, equality holds above:
there are exactly three branch values, and each corresponding
fiber consists of two points of multiplicity two.

In either case select two such values lambda_0,lambda_infinity
and a Mobius map M sending them to 0,infinity. The rational function
M(R(z)) has an even divisor on P1, so is a square in C(z);
this follows directly by factoring its numerator and denominator,
including the valuation at infinity, and taking a complex constant root.
Consequently M(f(P,Q)) is a square in L.

Index-one detection of EVERY target affine prime now shows that
each target valuation of M(f) is even. Unique factorization in
C[u,v], allowing negative exponents and constant square roots,
gives M(f)=h^2 for h in K. Since h is nonconstant,
[C(h):C(h^2)]=2, contradicting relative algebraic closedness of
C(f)=C(M(f)) in K. This excludes d>1 and proves the claim.

## Scope and construction consequence

A rational donor whose pullback of such a target f is composite
cannot become polynomial Keller by a dominant rational SOURCE
substitution preserving the target functions: the strict algebraic
intermediate extension survives the source-field embedding.
This also covers finite rational source enlargement. It does NOT
cover arbitrary birational TARGET changes.

The three-value multiplicity bound is componentwise, not merely
a bound on the gcd of each fiber's multiplicities. No field-degree
bound for an arbitrary Keller map is asserted.
No suitable pencil or compositeness relation is constructed from
a nonempty normalization boundary. No surjectivity, B=R or JC2
conclusion follows. No automatic higher-fiber-count extension.

Imports are those already used in TWO1323: the Jacobian criterion,
quasi-finiteness, projective curve models/line restriction,
Riemann-Hurwitz, and polynomial/rational-function factorization.
No monodromy classification or additional external source is used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5183`.
- Body SHA-256:
  `e58da5534c11384e4d9eb83f0b1a063487ceef02f1597ec955ba199040c707bb`.
- Frozen basis: `9d71ad3b0e788d6fd31b58720a1497966d29bcef`.
