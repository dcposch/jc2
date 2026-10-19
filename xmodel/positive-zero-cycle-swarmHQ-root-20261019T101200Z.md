# A positive-zero multibranch obstruction to rational Darboux coordinates

STATUS: UNPROMOTED / manual producer; independent FIRST required.
OWNER: swarmHQ-root. Frozen basis: e4f4714c476847ae672834d8f1962f2ffb8b5736.
Scope: rational two-forms on surfaces and a conditional finite-cover application.
Not a JC2 proof, a general normalization theorem, or an unrestricted A5 exclusion.

## 1. Precise surface statement

Let S be a smooth projective complex surface, omega a nonzero rational two-form,
and E an irreducible curve with ord_E(omega)>0. Suppose E has at least two
geometric branches at a point z of S, and omega is regular on a neighborhood
of z (there is no polar component through z). Then there are no rational
coordinates u,v with C(S)=C(u,v) and omega=c du wedge dv for c in C*.

The nonzero constant and the full field equality are essential to the asserted
scope. This is a birational-coordinate obstruction, not an obstruction to
arbitrary finite source-field embeddings. The point z is smooth by hypothesis.

## 2. Proof

Resolve the branches of E over z by point blowups. The strict transform of E
has at least two distinct attachments to the connected exceptional tree over z.
Consequently its vertex and the path between two attachments give a cycle in
the dual multigraph; parallel edges count as a cycle. The global irreducibility
of E is what makes the two attachments return to the same vertex.

Every exceptional curve introduced over z has strictly positive order in the
pulled-back omega. Indeed a point blowup of a regular two-form creates order
1 plus the multiplicity of its local coefficient at the center; this is at
least1. Later pullbacks are still regular over z. The strict transform of E
retains its positive generic order. Thus every component of this cycle has
positive order. All its intersection points lie over z, where the pulled-back
form is regular. Further point blowups at those intersections subdivide cycle
edges with positive-order components; blowups elsewhere do not destroy the cycle.

Suppose omega=c du wedge dv with C(S)=C(u,v). Take a common smooth resolution W
of this resolved S and P2_(u,v), with birational morphism h:W->P2_(u,v).
The positive cycle just constructed survives on W by the preceding calculation.
On P2, div(du wedge dv)=-3 L_infinity and has no positive component. Therefore
EVERY positive-order curve on W must be h-exceptional: a noncontracted prime
has the same generic valuation and differential order as its image prime.

The connected cycle is consequently contained in a single exceptional fiber
of h. A birational morphism between smooth projective surfaces factors into
point blowups, and the exceptional dual graph over any one point is a tree.
It cannot contain that cycle. This contradiction proves the statement.

Imports: characteristic-zero surface/embedded resolution, common resolution,
and factorization of birational morphisms of smooth surfaces into point
blowups. These are the standard surface imports already used in the A5
producer and independent FIRST below; no new external source is imported.

## 3. Conditional finite-cover consequence

Let pi:X->Y be a finite dominant map of normal projective complex surfaces.
Suppose x in X and y=pi(x) in Y are smooth, and an irreducible ramification
curve E in X has at least two branches at x. Let eta be a nonzero rational
two-form on Y that is regular and nowhere zero on a neighborhood of y.
Then pi*eta has positive order e_E-1 along E and is regular near x. Resolving
X away from this smooth neighborhood reduces to section1. Hence there are
no coordinates u,v generating C(X) with pi*eta=c du wedge dv, c in C*.

In particular, if eta=dp wedge dq for rational coordinates p,q of C(Y),
then no birational target pair P,Q generating the same field and satisfying
  dP wedge dQ=a dp wedge dq, a in C*,
can have nonzero constant Jacobian in ANY birational source coordinates u,v.
This excludes even rational constant-Jacobian representatives at that fixed
area-form scope, not merely polynomial representatives in a specified open.
It does NOT cover a larger finite source field or nonconstant target Jacobian.

## 4. Relation to the A5 cover and earlier criteria

The accepted [A5 producer](a5-pentagon-chart-obstruction-swarmHQ-root-20261018T221810Z.md)
and [independent FIRST](a5-pentagon-chart-review-swarmHQ-sol56-root-20261018T222155Z.md)
construct one irreducible ramification E with two tangent branches at a smooth
pentagon point of X=S/A4; its image in Y=S/A5 is also smooth. Section3 applies
IF the chosen target area form is regular and nowhere zero at that image.
No particular global target-coordinate pair with this property is supplied here.
The completed local quotient parameters in the A5 proof are not silently
identified with global birational coordinates. There is no claim for all
arbitrary choices of target area form or all birational target models.

The [zero-free branch-model FIRST](zero-free-branch-model-review-swarmHQ-sol-20260917T044800Z.md)
uses a globally zero-free TARGET form and smooth target branch components,
and covers arbitrary finite rational source embeddings for polynomial outputs.
Here the obstruction is a multibranch positive-zero SOURCE curve at a pole-free
point, and the source-field identification must be birational. Neither theorem's
missing hypotheses are supplied by the other. No general eligible-model or
actual-normalization existence argument follows.

## 5. Hostile checks and scope traps

A positive exceptional order alone does NOT force its center outside an affine
plane: blowing up its origin gives x=s,y=s*t and dx wedge dy=s ds wedge dt.
The exceptional curve has order1 but center an interior point. The proof above
uses the WHOLE cycle and the tree structure of exceptional fibers, not that
incorrect per-component inference.

The pole-free neighborhood is used at every cycle-edge subdivision. With poles
through the selected intersection, a new exceptional coefficient can vanish
and this proof does not apply. Smooth single-branch zero curves, including the
campaign's non-Keller affine-extension controls, do not meet the hypothesis.
No finite-cover lift of the cycle is asserted. Novelty is unknown; historical
queries were bounded lexical discovery, not a literature-wide absence proof.
This is manual reasoning, not computation or formalization. No exit-price
assertion is made. No JC2 proof/counterexample, automatic donor family, or
successor is authorized by this report. Independent review precedes use.

OPEN(S) RAISED: None.

## COLLISIONS

status: EMPTY

- NONE -- no explicitly tagged OPEN entries are raised.

Corpus basis: e4f4714c476847ae672834d8f1962f2ffb8b5736 (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6736`.
- Body SHA-256:
  `d65fbc37cb3a10ee063dffb335143c69ac04d9a0d3a0f0e4ce4ba57160392176`.
- Frozen basis: `e4f4714c476847ae672834d8f1962f2ffb8b5736`.
