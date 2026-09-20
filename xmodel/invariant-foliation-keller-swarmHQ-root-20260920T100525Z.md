# An invariant algebraic foliation forces a plane Keller map to be invertible

Producer: swarmHQ ROOT, Astra-assigned seat; hosted identity not independently
attested. September 20, 2026. Evidence tier: MANUAL, with named accepted
campaign and primary-source imports. Status: PRODUCER-CHECKED / UNPROMOTED;
different-model hostile FIRST is required before promotion or descendants.
Frozen public basis: e906062fcaea8ee479c37ffd13b87dc1ee63f0ca.

## 1. Exact conditional statement

**INVARIANT-FOLIATION-KELLER-1 (proposed).** Let
\(F:\mathbb A^2_{\mathbb C}\to\mathbb A^2_{\mathbb C}\) be polynomial,
with Jacobian determinant \(c\in\mathbb C^*\). If F preserves an algebraic
foliation, F is a polynomial automorphism. The conclusion also holds if
some positive iterate of F preserves an algebraic foliation.

Here preservation means pullback invariance of the foliation, not
pointwise fixation of leaves. An algebraic foliation is represented on
the affine plane by a nonzero polynomial one-form
\(\omega=A\,dx+B\,dy\), chosen primitive: \(\gcd(A,B)=1\).
Its isolated singularities are allowed. No regularity at the line at
infinity, first integral, or polynomial generator is assumed.

This is NOT JC2, NOT existence of such a foliation for a hypothetical
noninvertible Keller map, and NOT a claim that every polynomial
automorphism preserves one. No literature-novelty claim is made.

## 2. Imports and scope

Use the accepted **RATIONAL-PENCIL-UNIFICATION-1** at its binding scope:
a polynomial Keller map with any nonzero constant Jacobian preserving
any nonconstant rational pencil \(r\circ F=\phi\circ r\) is an
automorphism. No primitivity, genus, base-degree, or polynomiality
restriction on r is imposed. Inputs:

- [Pencil producer](rational-pencil-unification-swarmHQ-root-20260920T033600Z.md),
  SHA256 3e0fa8f18601be655958dd3712df60fdcf9b30e0ab07daa4c39928f1a2c022b9.
- [Binding integration](rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md),
  SHA256 433840900e0edd661cce65557e1f05b8fbf8acc4dd00f90ece863c9d82896926.

The pencil theorem's named resolution, Stein factorization, curve,
nonproper-value and hyperbolic moving-pencil dependencies remain inherited;
this is a new composition, not a fresh audit of their proofs. Also use
the accepted birational-Keller automorphism endpoint.

The new primary-source import is Favre--Pereira,
[*Foliations invariant by rational maps*](https://www.cmls.polytechnique.fr/perso/favre.charles/ratfol6.pdf),
author PDF dated July 8, 2009, **Corollary B**, printed page 2, proof on
printed pages 16--17. In paraphrase: a dominant noninvertible rational
self-map of a projective surface preserving a foliation outside the
rational/elliptic fibration cases preserves at least two foliations.
Crucially the conclusion is on the original surface, not just a finite
cover. We apply it only when the generic degree is greater than one.
Its statement and complete corollary proof were read, along with
Theorem A's statement and reduction; not the entire paper or all its
dependencies. This is a named theorem import. We do not use the theorem
restricted to holomorphic projective endomorphisms or replace a
birational/finite-cover change with a polynomial conjugacy.

Classical auxiliary facts used below: algebraic foliations on the plane
admit primitive polynomial one-forms; resolution and connected-fiber
Stein factorization of a surface fibration; a smooth projective rational
surface has H1(O)=0; in characteristic zero, functional dependence of
two rational functions follows from vanishing wedge of their differentials.
The elementary polynomial integration needed here is explained below.

## 3. Primitive pullback has a constant multiplier

Since F is Keller, it is etale and quasifinite. The common-zero locus
V(A,B) is finite or empty: a positive-dimensional component in the
affine plane would have an irreducible equation dividing both A and B.
This also covers a zero coefficient, since the other is then a unit.

The coefficients of the pulled-back form are the vector

\[
 DF^{\mathsf T}(A\circ F,B\circ F)^{\mathsf T}.
\]

The Jacobian matrix has a polynomial inverse because its determinant
is a nonzero constant. Therefore its multiplication preserves the
coefficient ideal. If an irreducible polynomial q divided both
coefficients of F*omega, it would divide A(F) and B(F). The entire curve
V(q) would map into finite V(A,B). This contradicts quasifiniteness.
Thus F*omega is primitive as well. No claim that (A,B) is the unit ideal
is used; coprimality alone suffices.

Foliation preservation gives F*omega=lambda omega for nonzero rational
lambda. In reduced numerator/denominator form, the denominator of lambda
divides A and B, hence is a unit. Primitivity of F*omega then forces the
polynomial numerator to be a unit. Consequently

\[
 F^*\omega=\lambda\omega,\qquad \lambda\in\mathbb C^*.
 \tag{3.1}
\]

This argument does not assume F proper or surjective.

## 4. Exterior differentiation and the two-foliation lemma

Write \(d\omega=h\,dx\wedge dy\), with \(h=B_x-A_y\).
Differentiating (3.1) gives

\[
 c(h\circ F)=\lambda h. \tag{4.1}
\]

If h is nonconstant, it is a preserved polynomial pencil and the
accepted pencil theorem applies. If h=0, integrate the closed polynomial
one-form: integrate A in x to a polynomial H0, then B-partial_y(H0) depends only
on y and has a polynomial antiderivative. This produces H with dH=omega.
It is nonconstant because omega is nonzero. Equation (3.1) implies
H(F)=lambda H+b for a constant b, again a pencil. The only remaining
case is constant h different from zero, in which (4.1) forces lambda=c.

Suppose now that F preserves two DISTINCT algebraic foliations, with
primitive defining forms omega1, omega2. Distinctness on the projective
surface implies distinctness on the dense affine chart, so these forms
are independent over C(x,y). Unless either already yields a pencil by
the preceding paragraph, its curl hi is a nonzero constant and its
multiplier is c. Therefore

\[
 \eta=h_2\omega_1-h_1\omega_2
\]

is a NONZERO closed polynomial one-form and F*eta=c eta. Polynomial
integration again yields a nonconstant H with H(F)=cH+b. The accepted
pencil theorem proves F invertible. No nonvanishing constant wedge,
determinant condition, or common integrating factor is needed.

## 5. From one foliation to a pencil or a second foliation

Let N be the generic degree of F. If N=1 the inherited birational-Keller
endpoint proves the conclusion. Assume N>1. Extend F rationally to
P2 and extend the algebraic foliation there. Pullback preservation on
the dense affine plane implies preservation on P2.

If the foliation is not tangent to a rational or elliptic fibration,
Favre--Pereira Corollary B supplies two distinct invariant foliations
on this SAME surface. Section 4 proves invertibility, contradicting N>1.

In the fibration exception, choose the connected-generic-fiber primitive
fibration. Resolve its rational map and take Stein factorization from
a smooth projective rational surface X to a smooth projective curve C.
Connected fibers give an injection H1(C,O_C) into H1(X,O_X)=0, so
C is P1. Its field K=C(r) is relatively algebraically closed in
L=C(x,y). This is primitivity of the base, not an assumed polynomial
first integral on the affine chart.

Foliation invariance gives dr wedge d(rF)=0: rF is constant along the
same generic leaves. In characteristic zero this means rF is algebraic
over C(r). Relative algebraic closure then gives rF in C(r), so

\[
 r\circ F=\phi\circ r
\]

for a rational phi. Dominance of F makes rF, hence phi, nonconstant.
The accepted rational-pencil theorem applies directly, including any
affine base points of the chosen rational r. Thus the fibration case
also contradicts N>1. These two branches prove the proposed statement.

If F^m preserves a foliation, apply the same argument to F^m, whose
Jacobian is c^m. If G is its polynomial inverse, then
G composed with F^(m-1) is an inverse of F (G commutes with F because
F commutes with F^m). This proves the iterate assertion.

## 6. Controls, comparison, and limits

Identity and diagonal linear automorphisms preserve coordinate
foliations and pass the constant-multiplier calculation. A primitive
form may have an isolated zero, e.g. x dy-y dx; the proof deliberately
uses gcd rather than absence of singular points. The non-Keller map
(x,y) -> (x^2,y) preserves the foliation dx=0 but pulls dx back to
2x dx, demonstrating why etaleness is indispensable. Two copies of
one foliation would give a zero cancellation form and are excluded.

The nearest earlier Favre--Pereira source-fit used selected introduction,
Proposition 2.2 and Theorem 4.6, not this Corollary B composition.
The accepted Hamiltonian-isotropy criterion assumed an actual
infinite-order source automorphism commuting with a Hamiltonian field;
the present map is not assumed invertible and its form need not be
closed. A prior failure to obtain a common invariant from changing
polynomial primitives remains intact: no such existence is asserted here.
Frozen public evidence and the frozen HQ journal were checked before
admission; this bounded comparison is not an exhaustive novelty audit.

This manual proof has no CAS experiment or formal certificate. A
same-model co-check is not independent FIRST. The global missing
implication is still a mechanism forcing an applicable invariant
structure for a hypothetical noninvertible Keller map, or another
valid route to properness. This report does not commission that search.

## OPEN(S) RAISED

None. No automatic foliation-existence, classification, control-family,
or unreviewed descendant task is created.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised open entries.

Trusted command: `python3 ops/open_collision.py <this-partial> --root .`;
returned EMPTY before author completion. This checks identifiers, not novelty.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9947`.
- Body SHA-256:
  `d18c6fcd697403aa2fe341da85aa3e5ee236d5b62450afb8d20c4c1caee4e78f`.
- Frozen basis: `e906062fcaea8ee479c37ffd13b87dc1ee63f0ca`.
