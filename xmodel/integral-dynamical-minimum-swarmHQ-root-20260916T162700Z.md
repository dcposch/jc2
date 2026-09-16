# An integral dynamical spectrum still does not give degree lowering

Producer: swarmHQ ROOT (gpt-6-astra), September16,2026 UTC.
Evidence: MANUAL with classical Jung generation import.
Lifecycle: PRODUCER-CHECKED; different-model FIRST required for promotion.
Basis: 96916fef71b178a1a9917b04b09d10079013e7db.
No CAS, degree search, worker or numerical evidence.
Native Astra independently checked the literal map and uniform proof,
then was observed COMPLETED before intake at16:28 UTC. This is same-model
corroboration, not different-model FIRST. ROOT is the report author.

## Exact statement

Over C put

    h=x^2*y^2+y,       F=(P,Q)=(h^2+x,h^3+x).

Then F is a dominant quasi-finite polynomial map of generic degree6.
For EVERY pair alpha,beta of polynomial automorphisms of A2,
lambda1(alpha F beta) is an integer, and

    min_{alpha,beta} lambda1(alpha F beta)=10>6.

The same assertions hold when both automorphisms have determinant1.
The minimum is attained by the identity changes. The map is NON-KELLER:

    J(P,Q)=h*(3h-2)*(2x^2*y+1).

This refutes the proposed implication that quasi-finiteness plus an
attained integral dynamical minimum forces that minimum to be at most
the generic mapping degree. Even integrality in EVERY polynomial frame
does not suffice. It does not refute a Keller-specific lowering theorem,
give a Keller counterexample, or resolve JC2.

## History and changed hypothesis

The [earlier quasi-finite control](quasifinite-dynamical-minimum-swarmHQ-root-20260916T043600Z.md)
has degree2 and minimum1+sqrt2, hence does not test the added integrality
hypothesis. Its [different-model review](quasifinite-dynamical-review-swarmHQ-sol-20260916T044500Z.md)
confirms the all-automorphism cone lemma used below. The reviewed
[Keller minimization report](keller-dynamical-minimization-swarmHQ-root-20260914.md)
supplies integral attained minima >=d only for normalized Keller maps;
its source-specific lowering gap remains open. Historical lifecycle
headers are not being used in place of the current accepted scopes.

The initially tempting pair ((xy)^2+x,(xy)^3+x) contracts x=0 and is
ineligible for this test. The term +y in the present h prevents this
failure: at x=0, h=y. No family enlargement or coordinate search follows.
Scoped historical comparison is not a literature-novelty determination.

## 1. Finite fibers and exact generic degree

For a target(p,q), every preimage supplies a value z=h satisfying

    z^3-z^2=q-p,       x=p-z^2,
    x^2*y^2+y-z=0.                                      (1)

There are at most three choices for z. For each, x is fixed and the last
polynomial in y is NEVER identically zero, because its linear coefficient
is1. It has at most two roots; at x=0 it becomes y-z=0. Thus every fiber
has at most six points, without discarding vanished quadratic leaders.
This proves quasi-finiteness of the finite-type morphism.

For the exact generic degree, factor through (x,z)=(x,h). Over C(x), h
is a quadratic polynomial in y, so

    [C(x,y):C(x,h)]=2.

Next C(x,z)=C(p,z) since p=x+z^2. The other coordinate satisfies
q=p+z^3-z^2, which has degree3 in z over C(p). Hence

    [C(x,h):C(P,Q)]=3,       [C(x,y):C(P,Q)]=6.

These are actual field inclusions, not degree multiplication inferred
from numerical fibers. They also prove dominance. The displayed Jacobian
follows from J(x,h)=2x^2*y+1 and
J_(x,z)(x+z^2,x+z^3)=3z^2-2z; it vanishes, for example, at(0,0).

## 2. Uniform automorphism lemma

Use positive weights on independent variables U,V with

    wt(U)=2k,       wt(V)=3k,       k>0.

For every NONAFFINE polynomial automorphism gamma, its two weighted
leaders are nonzero multiples of T^a,T^b, where T is one of U,V,
a,b>=1 and max(a,b)>=2. In particular each leader is a unique monomial.

For completeness, Jung generation and the two-cell Bruhat decomposition
of GL2 give a reduced expression

    gamma=L H_r ... H_1 A,
    H_i(U,V)=(b_i V+c_i, a_i U+R_i(V)),
    a_i*b_i!=0,       deg R_i>=2,

with affine automorphisms A,L and r>=1. This is the same elementary
normal-form argument in the earlier reviewed report; it does not assume
that gamma is conjugate to a generalized Henon map.

Each component of A has weight2k or3k, with a unique variable leader.
At H_1 the term R_1(A_2) has weight at least4k>3k, so strictly outweighs
a_1 A_1. Both resulting leaders are powers T,T^m of the same variable,
m>=2. Each subsequent H_i changes unequal exponent weights(r,s), s>r,
to(s,m_i*s). The final affine L either retains the larger term or leaves
the smaller term; its invertibility retains the larger in at least one
output. Unequal weights cannot cancel. Translations do not affect these
strict comparisons. This proves the assertion for arbitrary lengths and
degrees, not merely a bounded automorphism list.

## 3. Corner monomials and exact iteration

A corner monomial x^a*y^b means that every other exponent vector is
coordinatewise <=(a,b), with at least one strict inequality. If each
component of a map G has a corner with both exponents positive, let M
have those exponent rows. Composition multiplies the corner matrices:
a lower outer monomial has strictly smaller weight after substitution,
and the unique product of inner corners has nonzero coefficient. Thus
G^n has matrix M^n and

    deg(G^n)=max_i sum_j (M^n)_(ij).                       (2)

For a positive rank-one matrix M=v*w^T, its exponential growth is
w^T*v, directly from M^n=(w^T*v)^(n-1)*M.

Here h has corner x^2*y^2, P has corner x^4*y^4, and Q has corner x^6*y^6.
For any positive source weights(s,t), their weights are4(s+t),6(s+t),
exactly the ratio in section2. After substitution, a strictly lower
monomial in U,V has strictly smaller diagonal corner exponent; the lower
terms of P,Q remain coordinatewise smaller. Hence the leaders given by
section2 really are corners of gamma F.

If gamma is nonaffine, its corner matrix is one of

    [[4a,4a],[4b,4b]],     lambda1=4(a+b)>=12;
    [[6a,6a],[6b,6b]],     lambda1=6(a+b)>=18.

Every value is integral. If gamma is affine, each output containing V
has corner Q, and an output without V has corner P. Invertibility rules
out two P rows. All possibilities, including translations and arbitrary
nonzero leading scalar multiples, are therefore

    (P,Q): [[4,4],[6,6]], lambda1=10;
    (Q,P): [[6,6],[4,4]], lambda1=10;
    (Q,Q): [[6,6],[6,6]], lambda1=12.

Equation(2) proves these growth rates and their existence. For example,
deg(F^n)=12*10^(n-1) for n>=1; the ordinary degree12 is not mistaken for
the dynamical degree10. Nonaffine output changes cannot lower the latter.

Finally, beta(alpha F beta)beta^-1=(beta alpha)F. Conjugating an iterate
by a fixed polynomial automorphism changes its degree by at most a
constant factor in either direction. Thus the two-sided spectrum equals
the left-composition spectrum just computed. The reduction also works
within determinant-one automorphisms; identity already attains10 there.

## Scope, checks and next-action consequence

Any remaining Keller-minimization argument needs an additional actual-source
constraint. Neither finite fibers, attainment, nor the integrality of the
entire coordinate-change spectrum supplies the missing lowering step.
The new pair has a genuine critical divisor. Its absence for Keller maps
has not been replaced by these weaker dynamical properties.

Controls include the failed contracted-line seed, the linear degeneration
of the quadratic in(1), the identity frame attaining10, and the explicit
nonzero/vanishing Jacobian formula. An automorphism itself has minimum1
by composing with its inverse. No surrogate is claimed to be an actual
Keller map. No formalization, finite computation, primary-theorem reproof
or new criterion equivalent to JC2 is asserted. No automatic higher-degree,
parameter, coordinate or countercontrol successor is selected.

The only classification import in this proof is classical Jung generation.
The earlier producer/FIRST supplies the reduced-word derivation; section2
spells out the swapped weight-order specialization. ROOT's separate
selected reading of Favre--Jonsson's introduction and Propositions2.5--2.8
does not supply a lowering theorem and is not a dependency of this proof.

Hashes recorded after whole historical report reads, not claimed as
pre-read pins:

- Earlier quasi-finite producer: 0005828cec9ecf9800754beccd2d39825841afb51f3b6def019f286155e1cd9b.
- Earlier Sol review: 2af1daa69a2a70d8156871deee06b4c3d774db3239111817936347ef50e88092.
- Keller minimization: 84837d2d29fd8b60c6e10a7de6cf7fa10d7b428a8e02c46a494e4b8ae3e24957.
- FALLACY-v2: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- COORDINATION: 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.

## OPENS RAISED

None. The existing actual-Keller lowering gap remains unchanged.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Trusted collision scan completed; no scientific novelty claim is
inferred from this lexical result.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9052`.
- Body SHA-256:
  `66ff4791e5f2bd55ea018e17dc38d1698b54499add880b8ce4648d65ef11363b`.
- Frozen basis: `96916fef71b178a1a9917b04b09d10079013e7db`.
