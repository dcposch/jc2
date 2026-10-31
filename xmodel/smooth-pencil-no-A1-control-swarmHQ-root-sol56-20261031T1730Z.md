# A smooth surjective affine-plane pencil with no affine-line fibre

Evidence: MANUAL with one fixed symbolic identity check. Lifecycle: PROVISIONAL.
Independent review: PASS, configured gpt-5.6-sol/ultra; hosted identity unverified.
Producer: swarmHQ ROOT. Novelty unassessed. JC2 remains unresolved.

The [independent review](smooth-pencil-no-A1-review-sol56-20261031T1720Z.md) checks every fibre and the inverse regular maps. The mathematical core below is byte-identical to the reviewed candidate; [originals, checks and provenance](../box/smooth-pencil-no-A1-control-swarmHQ-20261031T1730Z/README.md) preserve its exact scope.

## Claim

Over C put f=xy-1 and g=x+y(xy-1), and define h=[f:g]:A2->P1.
The morphism h is smooth and surjective. Every fibre is connected and isomorphic either to C* or to A1 minus two distinct points. Thus no fibre has an A1 component, despite all fibres being rational and smooth.

## Base-point freeness and smoothness

The exact identity (1+y^2)f-yg=-1 proves that f and g have no common zero.
Direct differentiation gives

    g df - f dg = dx + (x^2-f^2) dy.

This one-form never vanishes. On g!=0 the differential of f/g is this form divided by g^2; on f!=0 the differential of g/f is its negative divided by f^2. Both source and target are smooth over C, so this differential criterion proves h is a smooth morphism.

## Every finite fibre

For lambda in C write D_lambda(y)=y-lambda-lambda*y^2. Then

    f-lambda*g = x*D_lambda(y)+(lambda*y-1),
    D_lambda(y)*g-1 = (1+y^2)*(f-lambda*g).

Consequently D_lambda is invertible on the fibre h=[lambda:1], with inverse g. Its coordinate ring is exactly C[y,D_lambda(y)^(-1)], with

    x=(1-lambda*y)/D_lambda(y),  g=1/D_lambda(y),  f=lambda/D_lambda(y).

These formulas give inverse regular maps, not merely a birational parametrization. No base point has to be deleted from V(f-lambda*g), because (f,g) is the unit ideal.
For lambda=0, D_0=y, so the fibre is C*.
For lambda!=0, D_lambda is quadratic with discriminant 1-4*lambda^2. For lambda=1/2 or -1/2 it has one distinct double root, so localization again gives C*. For every other nonzero lambda it has two distinct roots, giving A1 minus two points.
Each such open subset is nonempty and connected; its scheme is reduced even when the denominator has a repeated root.

## The fibre at infinity

On g=0 the identity (1+y^2)f=-1 holds, so 1+y^2 is invertible. Conversely

    x=y/(1+y^2),  f=-1/(1+y^2),  g=0

gives an isomorphism of h^(-1)([1:0]) with Spec C[y,(1+y^2)^(-1)], which is A1 minus {i,-i}.
This accounts for every point of P1 and proves surjectivity. Each fibre is irreducible and has a nonconstant unit; A1 has only constant units. In particular none is A1 and none contains a separate A1 component.
As a consistency check only, the generic Euler characteristic is -1 and the three exceptional fibres at 0,1/2,-1/2 have Euler characteristic 0; Euler integration gives 2*(-1)+3*(0-(-1))=1.

## Why this is not a Keller counterexample

The Jacobian of (f,g) is xy^2-x-y, not a nonzero constant; it vanishes at (0,0).
For finite lambda!=0,1/2,-1/2, the radial coordinate g=1/D_lambda has derivative (2*lambda*y-1)/D_lambda^2, vanishing at y=1/(2*lambda). That point is in the fibre because D_lambda there equals (1-4*lambda^2)/(4*lambda), which is nonzero. The radial map to C* therefore fails to be etale on these fibres.
For a missing-value Keller pair (p,q), smoothness of [p:q] is accompanied by etaleness of the radial coordinate on every fibre component. The example satisfies the first property but not the second. It refutes the universal special-A1-fibre assertion; it does not settle the stronger actual-Keller problem or even Keller surjectivity.

## Scope and verification

This refutes the universal assertion that a smooth surjective algebraic morphism A2_C->P1 must have an A1 fibre component, even after adding rationality and irreducibility of all fibres. It does not refute a statement requiring constant Jacobian or radial etaleness on every fibre component. No Keller surjectivity, properness, or JC2 conclusion follows.

The proof uses explicit coordinate-ring isomorphisms and the standard smooth-morphism differential criterion over C. The independent reviewer also checked the relative hypersurface Jacobian criterion directly. The symbolic receipt supports polynomial identities; it does not replace the proof. The original prospective Bezout prediction had a sign typo, exposed by the check and corrected before candidate sealing; the reviewed proof uses (1+y^2)f-yg=-1.

## OPEN(S) RAISED

None. The actual-Keller radial-etaleness and surjectivity gaps are preexisting and remain unresolved. No novelty or exhaustive historical-collision claim.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `c2d8ede89f709b2c9da2851ba00f34e5b6b703e3` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4928`.
- Body SHA-256:
  `f84db70bda33b0099b62c0b0c3a4ce891a2961326835735c9caea377aa5b5c1b`.
- Frozen basis: `c2d8ede89f709b2c9da2851ba00f34e5b6b703e3`.
