# Geometric generic units can be globalized after a bounded power

Producer: swarmHQ ROOT (Astra), with an independently obtained native Astra
multisection argument. Exact hosted peer model identity was unexposed.
Date: September16,2026 UTC.
Basis: 5f2292d4f002cc9708090d02859b3e7f0f800e13.
Evidence: MANUAL, PRODUCER-CHECKED, UNPROMOTED pending different-model review.
No novelty claim, scalar-unit theorem, or JC2 resolution.

## Statement

Let P in C[x,y] be nonconstant, with no critical points, and assume EVERY
closed fiber P=a is irreducible. This extra all-fiber hypothesis is explicit;
it is not asserted for every component of a Keller pair here. Write
K=C(t), with t acting as P, and R_K=C[x,y] tensor_C[t] K.

Fix any affine line ell on which P restricts to a nonconstant polynomial
of degree e. For every finite field extension E/K, let C_E be the
normalization of A1 in E and set X=A2 x_A1 C_E, with projection pi to C_E.
For every u in (R_K tensor_K E)^*, there is f in E^* such that

    w = u^e / pi^*f belongs to O(X)^*.

If u is not in E^*, neither is w. The same e works for all finite E and
all such u; it is the degree of this chosen source line, not the Keller
mapping degree. Thus every nonconstant geometric generic unit would yield
a non-base GLOBAL unit on some finite base change X, after power/rescaling.
The conclusion does not say that such a global unit cannot exist.

## Proof

The curve C_E is smooth, connected and affine. Its finite map to A1 is
flat: its coordinate ring is a finite torsion-free C[t]-module. The
base-changed map pi is smooth, with reduced irreducible closed fibers.
The generic fiber is geometrically integral. For completeness, a proper
factorization of P-t over an algebraic closure of K and its finitely many
coefficients could be spread over a finite cover of a nonempty base open.
Specializing at a complex point while retaining positive degrees of both
factors would give a reducible closed P-fiber, a contradiction. Smoothness
gives geometric reducedness. Consequently X is smooth and integral, and
E is relatively algebraically closed in its function field.

Regard u as a rational function on X. It has no horizontal zero or pole,
because both u and u^{-1} are regular on the generic fiber. Every vertical
prime divisor is the unique reduced fiber over a point b of C_E. Hence
there is a divisor Delta on C_E with

    div_X(u) = pi^*Delta.

The divisor has finite support. The source line supplies

    Y = ell x_A1 C_E  ->  C_E,

a finite flat map h of degree e. Indeed a nonconstant one-variable
polynomial of degree e makes C[ell] a free C[t]-module of rank e, and
this property survives base change. Y need not be normal or irreducible.

Here is why restricting u and taking its norm is nevertheless legitimate.
Locally on C_E choose a rational function g whose divisor represents
Delta. On pi^{-1}(U), the rational function u/pi^*g has zero Weil divisor.
Normality makes it a regular unit there. Its restriction to Y_U therefore
remains a unit, including at intersections or singularities of Y. Its
finite-flat norm is a unit of O(U): it is the determinant of an invertible
multiplication map on a locally free rank-e module.

On the generic fiber of Y, define f to be the norm of this restricted
rational u. This is a nonzero element of E, even if that finite generic
algebra is a product of fields. The preceding local description gives

    f = g^e times a unit,   div_C_E(f) = e Delta.

Thus div_X(u^e/pi^*f)=0. On the normal affine variety X, a rational
function with zero Weil divisor and its inverse are regular; w is a global
unit. Equivalently, the finite-flat multisection kills the relevant class
in ker(Pic(C_E)->Pic(X)) after multiplication by e. It does NOT require
Pic(C_E)=0, factoriality of X, a section of pi, or injective specialization
of the unit lattice.

If w were in E^*, then u^e would be in E^*. The relative algebraic closure
property of E in the generic-fiber function field forces u to lie in E^*.
This proves preservation of non-base dependence.

Every unit over an algebraic closure of K, together with its inverse, is
defined over some finite E/K: only finitely many algebraic coefficients
occur. This proves the stated geometric-generic consequence.

## Quadratic interface, not a unit exclusion

For a nontrivial quadratic E/K, choose a nonconstant squarefree polynomial
D(t) representing its square class. Its affine normalization is
C_E=Spec C[t,z]/(z^2-D(t)), so

    O(X)=C[x,y,z]/(z^2-D(P)).

Write the global unit as A+Bz, with A,B in C[x,y]. The map X->A2 is
finite free of degree two. Its norm is a unit of C[x,y], hence a constant
c != 0. Scaling A,B by a square root of c gives

    A^2 - D(P) B^2 = 1.

If the original unit was non-base, this gives a dominant REGULAR map

    A2 -> { U^2-D(T)V^2=1 },   (x,y) |-> (P,A,B).

Indeed, if the image had dimension one, then A and B would be algebraic
over K. Geometric integrality of the original generic fiber makes them
elements of K; the resulting A+Bz would be a base scalar in E, contrary
to the theorem. This argument supplies the whole-plane map; it does not
exclude that map by a logarithmic Kodaira calculation or another theorem.
For arbitrary E, no dominant map to an arbitrary higher-dimensional norm
torus is claimed.

## Controls and relation to the old gap

- P=x has affine-line fibers and only base generic units. The statement
  does not manufacture a non-base unit in this case.
- Irreducibility of every fiber is load-bearing. For P=xy, the generic
  fiber has unit x. With E=K, no power x^e can become a global unit after
  division by f(xy): a polynomial-plane unit is constant, whereas y can
  vary independently of x. The reducible zero fiber prevents writing
  div(x) as pullback of a divisor on the base. This is a scope control,
  not a counterexample satisfying the theorem's assumptions.
- The proof permits nonzero Delta and nontrivial Pic(C_E). Simply clearing
  denominators is not the argument; norming a finite-flat multisection
  removes the divisor-class obstruction after a power.

The [historical puncture/unit test](../notes.md#2026-09-14-2240-utc--puncture-invariants-do-not-supply-an-invariant-fiber-class)
proved only R_K^*=K^* and left finite extensions, norm kernels and mixed
periods open. The present bridge removes a global coefficient-pole obstacle
for EVERY finite extension under the same extra all-fiber hypothesis.
It does not prove that O(X)^* consists of base units. Consequently neither
geometric-unit vanishing, a splitting of the mixed cohomology extension,
nor an inverse for a Keller map follows. The
[collision-surface norm report](collision-surface-units-astra-20260912.md)
concerns a different surface and remains unchanged.

No external logarithmic theorem is imported. A discovered Kollár Pell-
surfaces source could not be retrieved; its search excerpt is not a proof
input. The general bridge above is independent of that proposed application.
Only standard divisor/normality facts and the explicitly described
finite-flat determinant norm are used. No CAS or scientific execution.
Bounded history searches found no exact prior campaign bridge; this is
not an exhaustive literature or novelty claim.

## OPENS RAISED

None. The existing scalar-unit and mixed-period gaps remain open; no
automatic extension-degree ladder, control family or computation follows.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The lexical result is not a novelty or mathematical-completeness certificate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7590`.
- Body SHA-256:
  `d5652ee8cd6b993b0dd553056b09f340e0ec433468e4069b64331c4617f6c172`.
- Frozen basis: `5f2292d4f002cc9708090d02859b3e7f0f800e13`.
