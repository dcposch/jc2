# Geometrically integral quotients of small-degree ambient towers

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra same-model check.
Date: September 16, 2026. Basis: 3be38d75eb885c9fde1fd1229c18f7be06d36f7c.
Evidence: MANUAL, conditional on the accepted Keller/block premises below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model FIRST.
Claim: CONNECTED-QUOTIENT-TOWER-1. JC2 remains unresolved.

## Statement and changed construction test

Let X_m --> ... --> X_0 be a finite tower of dominant generically finite
rational maps of integral complex varieties of the same dimension. Suppose
each induced function-field extension has degree at most three. Let

    q_m:X_m --> A2_s,       q_0:X_0 --> A2_t

be dominant rational maps with GEOMETRICALLY INTEGRAL generic fibers.
Suppose h:A2_s->A2_t is a polynomial map with nonzero constant Jacobian and

    q_0 composed (X_m --> X_0) = h composed q_m

as rational maps. Then h is a polynomial automorphism, conditional on the
three accepted plane Keller premises listed below.

There is no bound on tower length, ambient dimension, polynomial degrees,
generic fiber genera or the total degree of the ambient composition. The
ambient maps need not themselves be Keller, polynomial, finite or everywhere
defined. No group action or quotient at an intermediate stage is required.
The descended h, however, MUST be a whole-plane polynomial Keller map.

The new first test for this construction route is field-theoretic: check
relative algebraic closure at the two endpoint quotients. When both tests
pass, small-degree ambient iteration followed by such a compatible quotient
cannot create a plane counterexample. Searching for nonlinear compatible
actions is unnecessary in this stated setting. Arbitrary projected plane
sections do not furnish this commuting endpoint-fibration square.

## Accepted dependencies, not new degree theorems

Consume the three premises at exactly the scopes already used by the
[low-fiber tower FIRST](low-fiber-tower-transfer-gate-sol-20260913.md):

1. A polynomial plane Keller map cannot have mapping degree two or three.
2. For its actual extension K=C(h_1,h_2) inside L=C(s_1,s_2), there is no
   STRICT proper intermediate K<M<L with [M:K] equal to two or three.
3. A birational polynomial plane Keller map is an automorphism.

The second-leg degree [M:K] is not the first-leg degree [L:M]. The
[binding cubic addendum](block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-addendum-sol56-20260830.md)
and [priority/scope recovery](cubic-block-priority-recovery-root-20260912.md)
retain singular normalizations and arbitrary strict first-leg degree.
Their named internal/external premises keep their existing evidence tiers.
This report does not reprove or independently upgrade any of those results.

## 1. All fields in one ambient field

Pullback through the dominant rational maps embeds the ambient fields as

    E_0 subset E_1 subset ... subset E_m.

Pull back both surface fields into E_m. Write L=q_m^*C(s_1,s_2), and
K=q_0^*C(t_1,t_2), transported through the ambient tower. The commuting
identity identifies K subset L with the ACTUAL extension of h. Since h
is Keller, it is dominant and generically finite, so [L:K] is finite.

Geometric integrality of the endpoint generic fibers implies that K is
relatively algebraically closed in E_0 and L is relatively algebraically
closed in E_m. This is a statement about those particular embeddings, not
an identification of fields merely because their variables have similar names.

One elementary explanation of this implication is as follows. A nontrivial
finite subextension of a function field over its base is separable in
characteristic zero. Tensoring it with an algebraic closure of the base
splits it into a product of more than one field. Its injection into the
tensor of the full function field would put nontrivial idempotents in a
domain, contrary to geometric integrality. No properness or connectedness
of all special fibers is used.

Set C_i=E_i intersect L inside E_m. Then C_0=K and C_m=L. Also C_i is
relatively algebraically closed in E_i: an element of E_i algebraic over
C_i is algebraic over K, since C_i/K is finite; it is thus algebraic over
L and belongs to L by the top endpoint hypothesis. Hence it lies in C_i.
In particular these C_i are the full relative algebraic closures of K in E_i.

## 2. The constant-field steps inherit the small degree

For i>=1, choose a primitive element of the finite characteristic-zero
extension C_i/C_(i-1), with irreducible polynomial P over C_(i-1).
It remains irreducible over E_(i-1). Indeed, the coefficients of any monic
factor over E_(i-1) are algebraic over C_(i-1), as symmetric expressions
in roots of P. Relative algebraic closure forces those coefficients into
C_(i-1), contradicting the irreducibility of P there.

Consequently

    [C_i:C_(i-1)] = [E_(i-1) C_i:E_(i-1)]
                  <= [E_i:E_(i-1)] <= 3.

The compositum is contained in E_i. In this particular situation the
left-hand degree also DIVIDES the ambient step degree, by the tower law.
Only the inequality is needed. This is not the false divisibility claim
for arbitrary composita: relative algebraic closure is load-bearing here.
The primitive-polynomial argument is the classical field argument in
[Stacks, Lemma 10.47.8](https://stacks.math.columbia.edu/tag/037P);
the geometric-integrality convention is
[Stacks, Section 10.49](https://stacks.math.columbia.edu/tag/05DW).
ROOT read both primary passages on September 16; no new classification
theorem or source applicability premise is imported from them.

## 3. First strict step, not a bound on the total degree

Suppose L differs from K. Choose the first strict step of the finite
constant-field tower. Its lower field is K and its upper field M has
[M:K] equal to two or three. If M is strictly smaller than L, accepted
premise 2 excludes that actual proper target block. If M=L, accepted
premise 1 excludes the whole Keller mapping degree. Thus L=K, and
premise 3 makes h an automorphism. Equal steps cause no problem. An empty
ambient tower gives C_0=K=L directly.

This argument does NOT assert that the entire descended degree is at most
three before using the Keller exclusions. It finds one forbidden initial
block. The argument never attempts to descend a polynomial map to each C_i;
the accepted block premise is a theorem about intermediate fields of the
actual whole-plane Keller inclusion.

## 4. Controls and limits

Ambient degree need not survive a quotient. The map
(x,y,z)->(x,y,z^3), with q_m=q_0=(x,y), descends to the identity. Both
generic fibers are geometrically integral, and all ambient degree is
vertical. Thus no additive-action-style equality of total degrees is used.

Conversely, two successive maps (x,y,z)->(x^3,y,z), with the same coordinate
projections, descend to (s,t)->(s^9,t). This map is NOT Keller. It verifies
that the field argument permits total quotient degree nine while producing
an initial cubic block; the Keller premises are essential to the conclusion.

Geometric CONNECTEDNESS alone is insufficient for the endpoint field
argument on arbitrary nonnormal varieties. The integral threefold

    X: u^2=t v^2 in A4_(t,w,u,v),       q=(t,w)

has a geometrically connected generic fiber consisting of two lines meeting
after base change. But u/v in C(X) has square t and is not in C(t,w).
Thus the base field is not relatively algebraically closed. This control
refutes a weakened hypothesis-to-field inference, not the Keller conclusion
under the actual hypotheses.

Dropping the bottom hypothesis also hides the whole original problem:
take an identity ambient tower on A2_s times A1, q_m the projection, and
q_0=h composed q_m for any prospective plane Keller map h. The square is
automatic, but if the mapping degree of h is d>1 the bottom geometric generic
fiber is a disjoint union of d lines. This is a conditional scope warning, NOT a known
noninvertible Keller example. Without the top hypothesis, C_m need not
equal L; no conclusion for that enlarged scope is asserted either.

The theorem covers any tower of the accepted cubic core, its identity
stabilizations and independent polynomial coordinate changes, WHEN the
two actual endpoint quotient hypotheses and commuting identity hold.
Only the previously accepted ambient generic degree bound is needed here;
unlike restriction-to-a-plane theorems, exceptional ambient fibers are not
being used to infer a degree on a lower-dimensional image.

Geometrically nonintegral generic fibers, an ambient step of degree at least four,
arbitrary projected plane sections and noncompatible output projections
remain outside scope. No such alternative construction is supplied.
Nothing here establishes a quotient, a block in every Keller map, or JC2.

## 5. History, evidence and review boundary

The [right-factor theorem](low-fiber-keller-factor-invariance-root-20260913.md)
uses image fields of dimension two contained in the plane source field,
with a full factorization in the opposite direction. The
[additive bridge](additive-quotient-descent-swarmHQ-root-20260915T232000Z.md)
requires a compatible primitive locally nilpotent action and identifies
degrees using a slice. Neither supplies the arbitrary endpoint-fibration
argument above. The present proof is a classical field-theoretic composition
with existing small-block exclusions, not a new small-degree closure or a
claim of literature novelty. Targeted archive/report searches found no exact
statement in that scope; no exhaustive priority determination is claimed.

ROOT and native Astra independently reconstructed the constant-field proof,
then compared it and the controls. The native task was independently observed
COMPLETED before this report was finalized. Same-model agreement is not FIRST.
All reasoning and examples were checked manually; no scientific interpreter,
CAS, numerical experiment or worker was used. No new exit-price assertion.

Whole local reads and full SHA256 pins:

- Low-fiber FIRST: 63e69b73ced5f3b5026632f4c6e70c70a83daaa90ae39d6e1da3f4688b6418d5.
- Cubic binding addendum: b3bdd87cb27b614ca4bac476fd7f4c676b9551026397f3a895dbf84f4f195419.
- Cubic scope recovery: 18d41c9b42de44625b9dda6090b4b252f0c31edff641adf3d47e92f16f67679e.
- Right-factor producer: 940942db7942e0588677e5f10b17c1dbddf7961bb02a3a84e58c1ce3f3f853ca.
- Additive producer: a6919a3e38f1e0c9d78b88262435164e7905284d465e4fb94bc37a690642e96e.
- FALLACY-v2: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- COORDINATION: 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.

The low-fiber FIRST passes current artifact verification. The old cubic
addendum matches its historical full hash and passes its body/basis seal,
but artifact verification still fails the already documented mode mismatch:
0664 now versus recorded 0444. No old bytes or modes were changed. Historical
acceptance plus matching contents, not a falsely claimed successful current
publication transaction, are the basis for consuming that scoped premise.

QUANTITY: existence of a nonautomorphic descended polynomial Keller map in
the exact endpoint-fibration setting. CHEAPEST TEST: the relative-constant
field tower and first strict block, performed manually. One different-model
hostile review remains required before promotion. No automatic quotient,
action, control-family or higher-degree successor is selected.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11572`.
- Body SHA-256:
  `1ec1a8b76731c2ecb9aeab99e992eb381e5fa5e78b7fa1857eac5d7b0901633b`.
- Frozen basis: `3be38d75eb885c9fde1fd1229c18f7be06d36f7c`.
