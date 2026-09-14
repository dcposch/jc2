# The closed collision control is the existing pseudo-plane relation

ROOT, September12,2026,16:01UTC. MANUAL/PRODUCER-CHECKED, UNPROMOTED.
KNOWN control after a source sign change; new campaign cross-identification,
not a new family, source obstruction, scalar pair or JC2 conclusion.

## Exact identification

Put S=Spec C[A,U,Z]/(U^2-A-A^2 Z), and define on the WHOLE plane

    pi(x,y)=(x^2, x^3 y-x, x^2 y^2-2y).

The relation holds by expansion. S is smooth: at A=0 its defining
polynomial has partial derivative with respect to A equal to -1; at A!=0
its Z derivative -A^2 is nonzero.

The map pi is surjective. For A!=0 choose x with x^2=A and then
y=(U+x)/x^3. The relation gives the stated Z. For A=0 necessarily U=0,
and the preimage is the single point x=0,y=-Z/2. Thus the generic degree
is2; no finiteness is asserted. The generic two-point fibre becomes a
one-point fibre on A=0, so a finite etale interpretation would be false.

It is etale everywhere. On A!=0 use target coordinates A,U, with
Jacobian J(A,U)=2x^4. Near A=0 use target coordinates U,Z, since the
A partial above is a unit; direct differentiation gives

    J(U,Z)=2+4x^2(x^2 y^2-2y)=2+4AZ,

which is2 when x=0. No deleted source boundary is used in this argument.

If two source points have equal pi image, u^2=x^2. On x!=0, the same-sign
branch is the diagonal and the opposite-sign branch is exactly

    u=-x,                 x^2(y+v)=2.                 (L)

The Z equality follows from these equations. If x=0 then u=0 and Z
equality forces y=v, so there is no off-diagonal point there. Both fibre
square and L are smooth/reduced; the diagonal and L are closed disjoint
surfaces, and the preceding computation covers all their points. Thus L
is exactly the full off-diagonal fibre square as a reduced affine scheme,
not just a dense rational graph. Its coordinate ring is C[x,x^-1,y].

This is the SAME L as ROOT's earlier closed Lagrangian control, not merely
a similar example. Its free swap is (x,y)->(-x,-y+2/x^2), and its old
primitive3/x=delta((3/2)xy) is unchanged.

## Exact match to the existing campaign object

The existing Danielewski/pseudo-plane chart is

    pi_plus(x,Y)=(x^2,x+x^3 Y,2Y+x^2 Y^2).

Set Y=-y and apply the target automorphism (A,U,Z)->(A,-U,Z). The result
is pi above. Equivalently the familiar chart in T has t=x^2 y-1 and
Z=x^2 y^2-2y, followed by (A,U,Z)=(x^2,xt,Z). The change interchanges
the two chart signs; it does not identify the distinct omitted divisors
of the separate T selfmap and A2 chart.

The retained report xmodel/danielewski-invariantization-root-20260911.md
28fb540a4bb834ad40d1aa0349b8a2458cf7665951484e4896638f18275e3189
already supplies S, its etale quotient/chart and the regular scalar-pair
construction endpoint. The earlier collision report
xmodel/collision-lagrangian-global-control-root-20260912.md
10d473b069d3805c553c66dcb7c0233bfec131a4d53b71c5cd5e22922eaf5cd6
did not make this exact identification. Its rational two-coordinate map
and genuine pole remain correct; pi is instead a polynomial map into S,
not into the target plane A2.

## Consequences and the exact remaining distinction

Full-plane polynomial SOURCE, smooth affine TARGET, etaleness, surjectivity
and the listed collision geometry together still admit this nontrivial
relation and its nonconstant unit x. Thus the actual target-plane condition
is essential in the arbitrary-unit question; full-plane source origin alone
does not exclude L. This is an explicit scope sharpening of the same control,
not a counterexample to the actual polynomial Keller A2->A2 statement.

If a regular scalar pair h,g on S existed for its natural volume form,
F=(h,g) composed pi would be an actual polynomial Keller map. The standard
volume form is dA wedge dU/(2A^2) on A!=0; its pi pullback is dx wedge dy,
and the global extension follows from the U,Z chart just used. L would
remain a closed irreducible component of the smooth off-diagonal square
of F: it has dimension2 and sits inside that square, whose components are
disjoint smooth surfaces. Hence an actual-source theorem that every such
component has constant units would exclude ALL S scalar pairs, not merely
a sparse degree family. That theorem remains GAP. No regular pair on S,
unit theorem, cocycle extension to the larger F square or JC2 closure is
obtained by this conditional pairing.

## Decision and custody

Record the fingerprint as KNOWN/DUPLICATE and merge it with the S/T route.
Do not launch a new control family, promote another geometry-only shortcut,
or claim a new collision representation. No independent FIRST is selected
merely to recheck this elementary coordinate identification. The actual
target-plane/cocycle compatibility gap remains untouched; the existing
S scalar-pair endpoint and unbounded hypotheses remain literal.

Only manual algebra, selected canonical history and the two retained reports;
no new external theorem or novelty audit, scientific execution, AWS action
or live peer payload. Astra's bootstrap implementation is independent and
not a mathematical input. Existing finalizer transaction, own apply_patch
writes, complete readback and unchanged postpins. No shared promotion,
provisional descendant, global rerank, broad sweep or cadence reset.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5277`.
- Body SHA-256:
  `f4fcf6e6b4671fb9b3946b9de435e2feb374951459ad92ef14d385a2a55a9113`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
