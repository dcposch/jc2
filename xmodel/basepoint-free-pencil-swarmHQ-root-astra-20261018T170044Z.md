# Basepoint-free rational target pencils stay primitive under Keller pullback

Producer: swarmHQ ROOT with native gpt-6-astra-assigned collaborative co-check;
hosted model identities not independently verified. Co-check is not independent FIRST.
Date: 2026-10-18 UTC.
Basis: 0702324226ef1c2bb4ba9530733288a7dae575a2.
Evidence tier: MANUAL, conditional on the explicitly named established imports below.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; independent hostile review pending.
Claim ID: BASEPOINT-FREE-PENCIL-1.

## Statement and scope

Work over C. Let F:X=A2 -> Y=A2 be a polynomial map with nonzero constant
Jacobian. Let f:Y -> P1 be a nonconstant morphism with geometrically integral
rational generic fibre. In particular f has NO affine basepoint.
Then k=C(f), embedded into L=C(X) by F*, is algebraically closed in L:
every finite field extension E/k contained in L equals k.
Equivalently the pullback pencil is primitive at the function-field level.

There is no rationality assumption on the generic fibres of f composed with F.
No assertion is made for rational pencils with affine basepoints, arbitrary
unrelated source/target pencils, existence of such a pencil for a general donor,
surjectivity or finiteness of F, or the full Jacobian conjecture.

## Dependencies and prior work

The accepted [rational-pencil integration](rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md)
(SHA256 433840900e0edd661cce65557e1f05b8fbf8acc4dd00f90ece863c9d82896926;
selected current evidence lines1–90) supplies the following imports:

1. A morphism from the actual affine plane to P1 with geometrically integral
   rational generic fibre can be resolved at infinity only. In a smooth projective
   resolution, the reduced components of every fibre are smooth rational curves.
   Consequently every reduced affine fibre component is smooth rational.
2. The nonproper-value set S_F of a generically finite polynomial plane map is
   empty or a curve whose irreducible components admit nonconstant polynomial
   parametrizations by A1. For a Keller map it has no component isomorphic to A1.
   The existing integration retains its Chau arXiv:0905.3939v3 statement-level
   source check; this report does not claim a new proof-level audit of that source.

Also used: regular function-field extensions in characteristic zero; existence
of finite normalizations; extension of finite function-field covers of smooth
projective curves; stability of finite etale covers under base change and taking
intermediate normalizations; purity of the branch locus over a smooth surface;
and triviality of connected finite etale covers of A2_C.

RATIONAL-PENCIL-UNIFICATION-1 concerns a SAME pencil invariant under F (or an
iterate), and proves automorphy. The present statement does not assume invariance
and proves only primitivity of this pullback. Earlier different-pencil reasoning
identified only divisibility of individual retained fibre-component multiplicities,
not the gcd of a whole target fibre. The present proof uses intermediate branch
loci instead of that unavailable gcd inference. External novelty is not established.

## Argument

Put K=C(Y), L=C(X), and k=C(f), with all inclusions induced by the stated maps.
Since F is Keller it is dominant and generically finite, so L/K is finite.
Since the generic fibre of f is geometrically integral, K/k is regular.

Take any finite E/k inside L and put M=KE inside L. Regularity gives linear
disjointness of K and E over k, hence [M:K]=[E:k]. Let Z be the normalization
of Y in M. It is a normal irreducible surface finite over Y.

Let C be the smooth projective curve with function field E. The inclusion k->E
gives a finite map C->P1, etale outside a finite set B of points. Over
Y minus f^{-1}(B), the base change C times_{P1} Y is finite etale and normal;
its function field is M, by the preceding linear disjointness. It agrees there
with Z. Thus every divisorial branch component of Z->Y is vertical for f.

Independently, over U=Y minus S_F, the restriction of F is finite etale.
It is the normalization of U in L. The intermediate normalization in M is
finite etale too, so Z->Y is etale over U. Every irreducible branch divisor D
is therefore contained in S_F. Since S_F is empty or purely one-dimensional,
such D is an entire irreducible component of S_F, not merely a subcurve of one.

Being vertical, D is also an irreducible reduced affine component of a fibre of f.
The genus-zero fibre import makes D smooth rational. By polynomial
parametrization of S_F, there is a nonconstant morphism A1->D. A smooth affine
rational curve is P1 with a nonempty finite set removed. If at least two points
were removed, it would have a nonconstant invertible regular function. Its
pullback along the dominant map A1->D would be a nonconstant unit on A1, impossible.
Thus D is isomorphic to A1. The Keller no-A1-component import forbids this.

It follows that Z->Y has no branch divisor. Purity, with Z normal and Y smooth,
makes this finite generically etale map etale everywhere. A2_C has no nontrivial
connected finite etale covers, so [M:K]=1. Hence [E:k]=1 and E=k, as required.

## Conditional donor consequence

Let R(s) in C(s) have degree greater than1, and consider the rational donor
D_R(s,t)=(R(s),t/R'(s)). Its old target coordinates are p,q. Permit ANY birational
target transformation T, with new target coordinates u,v, without imposing a
constant-Jacobian condition. Let f(u,v) be the expression for the old coordinate p.
Its function field has rational geometrically integral generic fibre because
C(u,v)=C(p,q)=C(p)(q). Assume additionally that f extends to a morphism
on the WHOLE new affine target A2_{u,v} to P1.

Permit ANY finite dominant rational source substitution S:A2_{x,y} --> A2_{s,t}.
If T composed with D_R composed with S extended to a polynomial Keller map on
the whole source plane, its source field would contain the proper finite extension
C(R(s)) subsetneq C(s), via S*. Its target pencil is f and its pullback is R(s).
The theorem excludes that extension. Thus no such whole-plane Keller repair exists.
This argument makes NO assumption that a finite source substitution preserves
the genus of the source-pencil fibres.

This filter extends beyond constant-Jacobian target changes only when the explicit
basepoint-free target-pencil hypothesis holds. It does not exclude every birational
target transform, arbitrary rational donors, or all possible constructions.

## Replay and negative controls

Desk-only; no CAS, experiment or computational certificate. The proof is conditional
on the named imports. A pencil with an affine basepoint is an excluded scope control:
resolving it would change the actual affine target, so the smooth-affine-component
step above would not follow. Dropping geometric integrality would remove regularity
and the degree equality. Dropping the Keller hypothesis removes the no-A1 obstruction.
No claim is made that these omitted hypotheses each admit a counterexample.
FALLACY-v2 applied; no new exit-price assertion, therefore no charge_basis declaration.

## Limitations and next test

Independent hostile review must check the intermediate finite-etale argument,
the use of the genus-zero fibre import on the actual affine target, and the donor
field embeddings. No strengthening or application is admitted before that review.
The global finite-normalization and outside-boundary descent gaps remain unchanged.

## OPENS RAISED

None. Existing affine-basepoint and general normalization questions are not new opens.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `0702324226ef1c2bb4ba9530733288a7dae575a2` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7756`.
- Body SHA-256:
  `13c84910985de858896689d0cdbf8106303114462c741b84c231a62f5abcd5c9`.
- Frozen basis: `0702324226ef1c2bb4ba9530733288a7dae575a2`.
