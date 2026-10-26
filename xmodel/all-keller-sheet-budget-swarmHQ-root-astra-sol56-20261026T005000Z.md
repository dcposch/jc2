# The global sheet bound for every plane Keller map

Tier: PROMOTED / MANUAL, following independent review of the underlying proof.
Producer: swarmHQ ROOT and Astra co-research; independent reviewer configured gpt-5.6-sol.
Frozen public basis: `47cbe1093ea6ee7b4ec6d32a7eda4a79e567c061`.
This is a necessary condition, not a proof of JC2 or a novelty claim.

## Statement

Let F:U=A2_C -> A2_C be a polynomial map with nonzero constant Jacobian.
Let h:X -> A2_C be the normalization of its target in C(U), of generic degree e.
The WHOLE source U embeds openly in X. Write X minus U as the reduced omitted curves E_i.
These curves are pairwise disjoint, and each has a finite bijective normalization nu_i:A1 -> E_i.
The normalization of D_i=h(E_i) is A1. Let g_i:A1 -> A1 be the induced polynomial map,
delta_i its degree, and r_i the generic transverse ramification index of h along E_i.
For x in E_i, let m_x be the length of the local fibre algebra of h and let t_x be the
local degree of g_i at the unique point of nu_i^-1(x). Then

    e - 1 - sum_i r_i delta_i = sum_i sum_(x in E_i)(m_x - r_i t_x) >= 0.   (1)

The sum has finite support. The statement does not assume smooth E_i, rational singularities
of X, a divisorial eigenvaluation, or an affine sheet over every target point.

## Proof and why the previous geometric restriction is unnecessary

The [complete affine-enlargement proof](../box/all-keller-sheet-budget-swarmHQ-20261026T005000Z/affinetree0015-astra.md)
and [independent hostile review](../box/all-keller-sheet-budget-swarmHQ-20261026T005000Z/affinereview0038-sol56.md)
are retained byte-identically. Here is the argument and its dependency chain.

Write A=C[P,Q], R=C[x,y], and let B be the integral closure of A in Frac(R).
B is finite over A and lies in the normal ring R. The induced U -> Spec(B) is birational
and quasi-finite; Zariski Main makes it an open immersion into normal X=Spec(B).
This does not assume that A -> R is integral. A principal-localization/Hartogs argument
shows that the complement of the affine open U in normal affine X has no isolated components.

Normalize a projective closure of X. Its infinity divisor is ample Cartier. Resolve the
birational map from P2 by point blowups outside U, obtaining Z with SNC boundary tree D of P1s.
The support C_inf of the nef-big pullback of infinity is connected: a disjoint decomposition
would give two effective orthogonal divisors of nonnegative square, one of positive square,
contradicting Hodge index. Each surviving strict transform L_i must meet C_inf, since affine
X has no complete curve, and meets it exactly once, since D is a tree. A connected component
of D minus C_inf cannot contain two such L_i. Connected proper birational fibres over normal
X therefore cannot join distinct L_i or identify two points of one L_i. Hence the E_i are
disjoint and L_i minus C_inf -> E_i is finite bijective and birational, with source A1.
This is its normalization and an analytic homeomorphism; in particular chi_c(E_i)=1.
It need not be an isomorphism of schemes. No classification theorem is imported here.

The finite map A1 -> D_i factors finitely through its normalization. Completion and
Riemann-Hurwitz show that this normalization is P1 minus one point, hence A1.
Consequently sum_x(t_x-1)=delta_i-1. A normal surface is Cohen-Macaulay, so finite dominant
h over smooth A2 is flat of rank e. Base-change h to a small analytic disc in the chosen
normalized image branch at h(x). The local summand near x has constant rank m_x; a general
disc point has t_x nearby points on E_i, each of length r_i. Thus m_x>=r_i t_x, even at
singular points of X or E_i, or when D_i has several branches.

Euler integration of sum_(x over y)m_x=e gives integral_X m=e. The source U contributes 1;
each E_i contributes r_i plus its finitely many local excesses. Therefore

    e - 1 = sum_i r_i + sum_i sum_(x in E_i)(m_x-r_i).

Subtracting sum_i r_i(delta_i-1) gives (1). This is one whole-source identity, including
when distinct omitted curves have the same image; separate per-image budgets are not added.

## Scope, review and remaining gap

This extends the [previous divisorial sheet bound](global-sheet-budget-swarmHQ-root-sol56-20261025T234000Z.md)
to every plane Keller finite normalization. It does not extend the separately reviewed
[logarithmic defect identity](logarithmic-defect-swarmHQ-root-astra-20261025T221000Z.md).
In that identity's divisorial setting, the missing sufficient closing estimate remains

    sum_alpha m_alpha + Theta + Delta.c1(V) <= sum_i r_i(delta_i-1).

Theta retains all curve-filtration degrees and finite torsion; no bound on it is proved here.
The infinitely singular dynamical branch and JC2 remain unresolved.

The independent review is PASS. Its [coverage supplement](../box/all-keller-sheet-budget-swarmHQ-20261026T005000Z/affinereview0038-sol56-coverage-supplement.json)
records exact personal reading windows and separates automated verification from personal reading.
ROOT read both full proofs and that supplement, then checked this concise integration.
No separate independent review of public formatting is claimed. See the
[evidence package](../box/all-keller-sheet-budget-swarmHQ-20261026T005000Z/README.md) for original receipts and hashes.

OPEN(S) RAISED
None. The closing estimate above is an existing gap, not a newly admitted open claim.

## COLLISIONS
The original publication collision invocation is retained separately. A lexical EMPTY result
is not a novelty certificate and does not alter the mathematical scope.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5578`.
- Body SHA-256:
  `84ce0429cf21c418ccd71247a13d9f8090679f06d9a3d07939fe56abdfe9036f`.
- Frozen basis: `47cbe1093ea6ee7b4ec6d32a7eda4a79e567c061`.
