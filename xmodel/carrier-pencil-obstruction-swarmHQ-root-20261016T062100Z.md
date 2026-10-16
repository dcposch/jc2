# A pencil obstruction to constant direction perturbations

Producer: swarmHQ coordinator ROOT. Date: 2026-10-16.
Evidence: MANUAL, PRODUCER-CHECKED; independent review pending.
Claim ID: CARRIER-PENCIL-OBSTRUCTION-1. External novelty UNKNOWN.

## Statement and scope

Work over C. Set R=C[U,V], p=UV^3-V, and
B=C[U,UV,UV^2,p] inside R. Write J(A,B)=A_U B_V-A_V B_U.
For every nonzero pair (a,b) in C^2, the polynomial aU+bp^2 has
no Q in B with J(aU+bp^2,Q) a nonzero constant.
If ab!=0, it has no such Q even in the rational field C(U,V).

Consequently, for every H in B and alpha,beta in C, the pair

    P=p^2+alpha H,  Q=U+beta H

has no nonzero constant Jacobian. This is a constant-vector-direction
perturbation, not every deformation with dependent increments and not
an exclusion of all pairs in B. No general JC2 conclusion follows.

The [reviewed finite-carrier control](finite-moment-review-integration-swarmHQ-sol56-root-20261016T010647Z.md)
identifies this B with the global ring of the marked two-chart surface,
and (p^2,U) with a finite degree-six NON-KELLER map. Its Jacobian is
-2p(3UV^2-1). Finiteness is context, not a premise needed in the proof below.

## The generic fibre of a mixed pencil member

For lambda!=0 put T=U-lambda p^2. The rational change of variables

    g=1/V,  U=g^2+g^3p,  V=1/g

identifies C(U,V)=C(g,p), with dU wedge dV=g dg wedge dp.
Thus T=g^2+g^3p-lambda p^2. Let t be transcendental over C,
and work on the generic fibre T=t over K=C(t). With

    w=2lambda p-g^3

its function field is

    K(g,w),  w^2=S(g)=g^6+4lambda g^2-4lambda t.

Conversely p=(w+g^3)/(2lambda), so this is an equality of function fields,
not only a map from an auxiliary curve. Over the algebraic closure of K,
S is squarefree: a repeated root r satisfies
2r(3r^4+4lambda)=0. If r=0 then t=0; otherwise r is in C and S(r)=0
would make t constant. Both contradict transcendence of t.
In particular S is not a square and this generic fibre is geometrically
integral. The possible special values of t play no role in this argument.

Suppose J(T,Q)=kappa!=0 for Q in C(U,V). In (g,p) coordinates this is

    T_g Q_p-T_p Q_g=kappa g,  T_p=g^3-2lambda p=-w.

Taking the differential along T=t gives

    dQ=(Q_g-Q_p T_g/T_p) dg=kappa g dg/w.

The rational identity remains valid across points where that displayed
coordinate calculation divides by T_p, by equality of rational differentials.

## The differential has no rational primitive

On the smooth compactification of w^2=S(g), the differential eta=g dg/w
is regular at every point. At a finite point with w!=0 this is immediate.
At a simple root r of S, w is a uniformizer and
dg/w=2 dw/S'(g), which is regular. At g=0, S(0)=-4lambda t!=0,
so eta merely has a zero.

There are two points at infinity. In the coordinates s=1/g and z=w s^3,

    z^2=1+4lambda s^4-4lambda t s^6,  eta=-ds/z.

At s=0, z=+1 or -1, so eta is regular and nonzero there.
These finite and infinite charts cover the smooth compactification.
This checks regularity at all places, not just on the affine curve.

A rational function with a pole of order m>0 on a smooth curve has
differential with a pole of order m+1 in characteristic zero: if
q=c zeta^(-m)+higher terms, then dq=-mc zeta^(-m-1) d zeta+higher terms.
Therefore a rational primitive of a regular differential on a smooth
projective integral curve has no poles and is constant, so its differential
is zero. Since eta is nonzero, dQ=kappa eta is impossible.
This proves the stronger rational-mate exclusion for every mixed member.
The calculation needs no assumption that a period basis is invariant or
that a local primitive extends globally.

## The two endpoint members

For U, a polynomial Q with J(U,Q)=kappa must be Q=kappa V+h(U),
where h is in C[U]. Every generator of B becomes polynomial in (g,p):

    U=g^2+g^3p,  UV=g+g^2p,  UV^2=1+gp,  p=p.

But kappa V+h(U)=kappa/g+h(g^2+g^3p) has a pole at g=0.
It cannot belong to B. This exclusion is B-specific: V in R is indeed
a mate of U, so the rational-mate statement must not include this endpoint.

For p^2, J(p^2,Q)=2p J(p,Q) for every Q in R. Since p is a nonunit,
this cannot be a nonzero constant. This proves the needed polynomial
endpoint exclusion, without claiming that p^2 has no rational mate.
For example J(p,-1/(2V^2))=1, hence
J(p^2,-1/(4pV^2))=1 in C(U,V).

Rescaling aU+bp^2 reduces ab!=0 to the mixed case, and the remaining
nonzero pairs to these two endpoint cases.

## Constant direction perturbations

If (alpha,beta)!=(0,0), the nonzero polynomial
L=beta P-alpha Q=beta p^2-alpha U is a pencil member above.
If J(P,Q)=kappa!=0 and beta!=0, then J(L,Q)=beta kappa!=0.
If beta=0, then alpha!=0 and J(L,P)=alpha kappa!=0.
Both contradict the pencil statement because P,Q are in B.
If alpha=beta=0, the original nonconstant Jacobian excludes the pair directly.

This closes only this single perturbation mechanism, for arbitrary degree H.
It supplies neither a new counterexample nor polynomial termination for a
general deformation. No further perturbation family or computation is proposed.

## Historical comparison and checks

The seed ring and finite map are the reviewed FINITE-MOMENT-CARRIER-CONTROL-1.
The generic Moser/formal-deformation route already lacks a uniform polynomial
degree bound; see frozen notes.md39704--39751 at basis
4eb6f7792a1b87006b5fa365e8d74b97cd39fca5. This proof instead tests one fixed
pencil by its exact generic-fibre differential; it claims no repair of that gap.
The earlier elliptic compact-lattice design concerned a different invariant-
lattice question, not this rational-exactness calculation.

Producer checks are the explicit inverse field substitution, squarefreeness,
Jacobian sign, both infinity points, pole-order test, both endpoint controls,
and preservation of the pencil by the stated perturbation. No CAS was used.
The only geometric fact used after the displayed local computations is that
a regular function on a projective integral curve is constant.
Two bounded history queries per repository covered the frozen public corpus
and both HQ archives plus journals; selected outputs are not exhaustive novelty
coverage. Independent hostile review remains required before promotion.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `4eb6f7792a1b87006b5fa365e8d74b97cd39fca5` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6423`.
- Body SHA-256:
  `b38e88422b66cba86f632418a8e61567b6ae2d79cd8af9281bcaa3d9e7f434fe`.
- Frozen basis: `4eb6f7792a1b87006b5fa365e8d74b97cd39fca5`.
