# Rational polynomial pencils preserved by Keller maps

Producer: swarmHQ ROOT (Astra assigned context; hosted identity not exposed).
Date: September 20, 2026 UTC.
Frozen public basis: fcf9df1d0c9260ec16e936568af842ee77cf3c97.
Evidence: MANUAL with the named classical cohomology and nonproperness imports below.
Lifecycle: PRODUCER-CHECKED, PROVISIONAL; different-model FIRST pending.
No literature-novelty, arbitrary-pencil existence or JC2-resolution claim.

## 1. Exact statement

Let F:A2_C -> A2_C be polynomial with det DF=c in C*, without any
restriction on the modulus of c. Suppose h in C[x,y] is nonconstant,
C(h) is relatively algebraically closed in C(x,y), and the smooth
geometric generic affine fiber of h has genus zero. If

    h composed F = psi composed h,       psi in C[t], deg(psi)>=1,

then F is a polynomial automorphism.

The FULL generic affine fiber may have ANY finite positive number of
punctures. Reducible and nonreduced special fibers are allowed. In
particular, this includes every primitive C-star polynomial pencil,
whether its two punctures split over C(h) or not. No normal-form
classification of such pencils is assumed. The conclusion is conditional
on a preserved polynomial pencil; no such pencil is supplied for an
arbitrary Keller map, even a hypothetical noninvertible one.

## 2. Generic curve maps are finite

Let n>=1 be the number of points removed from the smooth projective
completion of the full geometric generic h-fiber. Its positivity follows
because a positive-dimensional complete curve cannot be a closed affine
curve. Over an algebraic closure of the generic base field the fiber is
P1 minus n points.

Distinguish the target parameter t=h(u,v) from the source parameter
s=h(x,y). The relation is t=psi(s). Over K=C(t), the source is a curve
whose constant algebra may split after extending K to an algebraic
closure. Since characteristic is zero, psi(s)-t has d=deg(psi) distinct
roots there. The source therefore becomes the DISJOINT union of d full
smooth geometric generic h-fibers. Each component and the target fiber
has the same n punctures. The source components are not identified with
each other or with one selected sheet.

F is quasi-finite, since it is etale. Its restriction to each component
is thus nonconstant. More generally dominance in this field setup would
suffice, but quasi-finiteness avoids any component-contraction inference.
Each restriction is a regular map

    f:P1 minus S_source -> P1 minus S_target,
    |S_source|=|S_target|=n.

It extends to a nonconstant map of projective smooth curves of degree k.
Regularity implies f^(-1)(S_target) is contained in S_source.

For n=1, after choosing the missing points as infinity, f is a nonconstant
polynomial map A1 -> A1, hence finite. For n=2, choosing the missing points
as 0 and infinity makes the map Gm -> Gm. Its coordinate is a unit of
Kbar[z,z^-1], hence a*z^m for a!=0 and nonzero integer m; this map is finite.
This coordinate choice occurs ONLY after passing to Kbar; no split pencil
over K, global monomial coordinates or polynomial source normal form is
asserted.

For n>=3, projective Riemann--Hurwitz gives total ramification 2k-2.
Ramification over S_target alone has degree

    k*n - |f^(-1)(S_target)| >= k*n-n.

Thus (k-1)*(n-2)<=0, so k=1. The projective isomorphism sends the two
puncture sets to one another, because the containment has equal finite
cardinalities. Hence the full affine curves are isomorphic and f is finite.

Consequently the entire generic-base source-to-target map is finite
after extension from K to Kbar, and is finite over K by faithfully flat
descent. This does NOT say the original plane map is already proper.

## 3. Nonproperness is confined to finitely many h-fibers

Write A=C[u,v] for the target ring and B=C[x,y] for the source ring,
with A embedded into B by F*. Let S consist of all nonzero polynomials
in the target h. Section 2 says S^-1 B is a finite S^-1 A-module, where
the element q(h) acts on B as q(psi(h)). In particular x and y satisfy
monic equations over S^-1 A.

Only finitely many base denominators occur in those two equations.
Clearing them gives one nonzero q(t) in C[t] such that x and y are
integral over A[1/q(h)]. It follows that

    B[1/q(h composed F)] is finite over A[1/q(h)].

Indeed the left algebra is generated over the right by x and y; the
inverse displayed on the left is already the image of the base inverse.
Therefore F is finite over the target open set q(h)!=0. Its nonproper
value set A_F is contained in the finite union of fibers q(h)=0.
Every irreducible curve component of A_F is consequently an entire
irreducible component of some h-fiber, by dimension and closedness.
This is an algebraic spreading argument, not an assertion that individual
fiberwise properness automatically gives properness of a family.

## 4. Fiber components of a rational polynomial are smooth

Resolve h:P2 --> P1 by point blowups over the line at infinity. There
are no affine indeterminacies, so the resulting smooth projective surface
X contains the ORIGINAL A2 as an unchanged open subset. The morphism
pi:X -> P1 has connected fibers: its generic fiber is geometrically
integral, and Stein factorization over the normal base has degree one.
Its smooth generic projective fiber is P1.

Here is a direct cohomological proof that every reduced irreducible fiber
component is smooth rational. This replacement for a ruled-surface
classification was contributed by the native Astra co-check and verified
by ROOT. Let D be any SCHEME fiber, and G a general smooth projective
fiber. Then D is linearly equivalent to G, G is nef, G^2=0, and adjunction
gives K_X.G=-2. Therefore

    (K_X+D).G=-2,
    H^0(X,O_X(K_X+D))=0:

an effective divisor cannot have negative intersection with the nef G.
Serre duality gives H^2(X,O_X(-D))=0. Since X is a point-blowup of P2,
H^1(X,O_X)=0. The exact sequence

    0 -> O_X(-D) -> O_X -> O_D -> 0

then gives H^1(D,O_D)=0. If C is any reduced irreducible component of D,
the surjection O_D -> O_C has kernel supported in dimension at most one.
Its H^2 vanishes, so H^1(D,O_D) surjects onto H^1(C,O_C). Consequently
the arithmetic genus of C is zero. Normalization expresses that genus as
the sum of its geometric genus and nonnegative singularity lengths; both
vanish. Thus C is a smooth projective rational curve. This proof handles
nonreduced D; it does not identify D with its reduced support or assert
that the whole fiber is smooth. The imports are surface Serre duality,
adjunction, birational invariance of H^1(O) for smooth surfaces, coherent
cohomology vanishing above support dimension, and the normalization genus
formula, all at their standard characteristic-zero scopes.

A corroborating primary statement is
Nguyen Van Chau, [Pencil of irreducible rational curves and Plane Jacobian
conjecture, arXiv:0905.3939v3, March 17, 2010](https://arxiv.org/pdf/0905.3939v3),
Section 2, proof of Lemma 1, printed page 4: the compactified rational
fibration has rational simple-normal-crossing fibers. ROOT checked that
passage and its setup, not the full underlying ruled-surface literature;
the smooth-component conclusion used here is also proved above.
The present application is to [h:1], whose resolution is confined to
infinity, not to a rational function with affine base points.

It follows that every reduced irreducible component of every affine
h-fiber is smooth: it is the intersection with the unchanged A2 of a
smooth irreducible pi-fiber component. No hypothesis that h is a
submersion, has reduced fibers, or has constant gradient gcd is needed.

## 5. The nonproper locus must be empty

The classical nonproperness theorem says that if A_F is nonempty then it
is a curve whose irreducible components have nonconstant polynomial
parametrizations A1 -> A2. For a polynomial Keller map none of those
components is isomorphic to A1. These are the inherited Jelonek/Chau
imports, stated together in the same [primary paper](https://arxiv.org/pdf/0905.3939v3),
Section 2(i) and Theorem 4, printed page 3. No new proof of these imported
theorems is claimed.

Let D be a component of A_F. Sections 3 and 4 make D a smooth affine
irreducible curve contained in a rational h-fiber. A polynomial
parametrization gives a nonconstant morphism A1 -> D. Write D=P1 minus T,
where T is nonempty. If |T|>=2, choose two missing points, move them to
0 and infinity, and let z be the resulting rational coordinate on P1.
Both z and 1/z are regular on D. Their pullbacks are inverse units in
C[t], so both are constants. Since z is a coordinate on the completion,
the parametrization would be constant, a contradiction. Thus |T|=1 and
D is isomorphic to A1, contradicting the Keller no-A1-component theorem.

Hence A_F is empty and F is proper. A proper quasi-finite polynomial map
is finite. A connected finite etale cover of A2_C has degree one, because
its analytification covers the simply connected space C2. Equivalently,
one may use the classical triviality of its finite etale covers. The
finite birational map to the normal plane is an isomorphism, proving the
statement in Section 1.

## 6. Scope checks and comparison

The SAME polynomial h on source and target is essential to the equal
puncture count. Different endpoint pencils do not automatically satisfy
it. A rational h with affine base points is also outside this proof:
resolving those points changes the original affine source, so Section 4
cannot be transferred back without further argument.

For the elementary non-Keller map F=(x,xy), take h=x and psi(t)=t.
Its generic fiber map is finite and its nonproper locus is the vertical
line x=0. This checks the gap between Sections 2--3 and properness:
the Keller no-A1 theorem is essential. The example has Jacobian x,
not a nonzero constant, and is neither new nor a JC2 counterexample.

The [hyperbolic moving-pencil theorem](hyperbolic-moving-pencil-swarmHQ-root-20260919T203700Z.md)
uses pointed moduli to produce a fixed rational invariant for a
degree-at-least-two base map, and its Keller corollary has exact J=1.
The present argument instead uses the rational fiber COMPONENT geometry
to remove vertical nonproperness, for any nonzero constant Jacobian and
any positive base degree. It covers the C-star case without an exhaustive
normal form, as well as the other rational generic fibers.

The [homogeneous-pencil theorem](homogeneous-pencil-composition-swarmHQ-root-20260919T175300Z.md)
has algebraically independent reduced numerator/denominator hypotheses
that a polynomial h does not satisfy. No missing pencil-existence premise
in either theorem is filled here. No general rational-pencil combination,
new counterexample construction or automatic classification successor is
promoted by this report.

Before admission, ROOT searched both frozen public evidence and the HQ
dated journal and read the nearest actual monomial, derivative-divisor
and rational-target scope calculations. No exact prior composition was
found in those bounded checks; this is not exhaustive literature novelty.
Two targeted discovery queries led to the single primary paper above.
Selected Section 2 statements/setup were read, not its cited dependency
proofs or an exhaustive source audit. No failed-source workaround was used.
All mathematics is manual; no CAS, scientific computation or proof
assistant was used. The native Astra co-check completed at01:13:38 UTC;
ROOT collected its whole final and verified COMPLETED status by01:14:43.
It independently confirmed the generic finiteness, direct localization
and no-A1 composition, and contributed Section 4's cohomological proof.
ROOT checked that proof and read back this entire report. This is
same-model co-research, NOT different-model FIRST; agreement is not the proof.

## OPEN(S) RAISED

None. No new finite search or descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author completion: 2026-09-20 01:14:43 UTC, after whole mathematical-body
readback, trusted collision check and terminal native collection.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12125`.
- Body SHA-256:
  `54e8fb878663ac88bb81ac068c96323c28fc4a8c9db6b46cb17f13fd8f7fb08a`.
- Frozen basis: `fcf9df1d0c9260ec16e936568af842ee77cf3c97`.
