# Generic curves from translated source lines

Producer: swarmHQ ROOT (gpt-6-astra), September 15, 2026.
Basis: `6f2a845a39d6490fdc69fde4a75119fc722a2924`.
MANUAL/BOOK-relative, PRODUCER-CHECKED, UNPROMOTED. Novelty UNKNOWN.
This is a Bertini corollary of the reviewed generic difference-surface
result, not a new Bertini theorem or a JC2 proof.

## Exact statement

Let F:A2_C -> A2_C be a polynomial Keller map, of generic degree d.
There is a nonempty Zariski-open set of affine source lines L such that,
for an affine-linear parametrization l:A1 -> L, the map

    Psi_L:A1_z x A2_q -> A2_t,   Psi_L(z,q)=F(q)-F(l(z))

has geometrically integral generic fiber. In fact Psi_L is smooth and
surjective for EVERY source line. No generic fiber is asserted to be A1.

We may further choose this open set so that L is not contained in the
inverse image of the nonproper-value set of F. For every such L, the
zero fiber is connected if and only if d=1. If d>1, it has the graph
q=l(z), isomorphic to A1, as a nonempty open-and-closed component, and
has a nonempty off-graph part. Thus the unresolved special-fiber problem
can also be expressed using this relative-curve family.

The quantifier is a GENERAL FIXED COMPLEX LINE (direction and offset),
followed by a generic translation. It is not every line, every member of
a fixed pencil, every translation, or finiteness of bad translations.

## Proof

Put k=C(t1,t2). The generic surface

    S={F(q)-F(p)=t}

is geometrically integral and smooth over k. This is the accepted
generic-geometric consequence used in
[KELLER-TENSOR-CONSTANTS-1](tensor-constants-swarmHQ-root-20260915T111600Z.md),
with [independent review](tensor-constants-review-swarmHQ-sol-20260915T112400Z.md).
It uses only the reviewed branch-disjointness core and geometric-generic
passage, not Chau's no-line theorem or the finite-exception bound.

The first-source projection pi:S -> A2_k is a base change of F and hence
etale. Its nonempty open image has dimension two. Apply
[Stacks, Lemma 37.32.3](https://stacks.math.columbia.edu/tag/0G4C)
to the trivial line bundle and the space of sections spanned by
1,p1-a,p2-b. Here (a,b) is a k-rational point in the image, which exists
because k is infinite. The common zero set of p1-a,p2-b is nonempty and
zero-dimensional, hence has codimension two in S; it misses the divisor
of the section 1. The base locus of the whole system is empty. These
are the lemma's exact hypotheses; no projectivity or embedding of S is
assumed. Consequently a general inverse image of an affine line is
geometrically irreducible. It is also smooth, being etale over that line,
so it is geometrically integral.

For clarity, a general line over the parameter field can be replaced by
a nonempty open set of FIXED complex lines. Work in the line chart
p2=A p1+B and set kbar=overline{k}. The Bertini-good kbar-open contains
D(h) for some nonzero h in kbar[A,B]. Express its finitely many
coefficients in a C-linearly independent basis beta_1,...,beta_r:

    h=sum_j beta_j h_j(A,B),   h_j in C[A,B].

Choose a nonzero h_j. For every (A,B) in D(h_j)(C), linear independence
implies h(A,B) != 0. Hence the inverse image of that fixed line in
S_kbar is integral. This is precisely geometric integrality of the
generic t-fiber of Psi_L. The line chart is open in the space of affine
lines, so the asserted nonempty C-open set follows.

For any fixed line, the q-Jacobian of Psi_L is the invertible Jacobian
of F. Thus Psi_L is smooth of relative dimension one. It is surjective:
the image U=F(A2) is open with finite complement. Indeed a missing curve
h=0 would make h(F) a unit in C[x,y], hence a nonzero constant, contrary
to the injectivity of F*:C[u,v] -> C[x,y]. The nonconstant curve
F(l(A1))+t cannot be contained in that finite complement. A point in
its intersection with U gives a point of the required fiber.

For t=0, projection to z is an etale separated morphism, the base change
of F along F composed with l. Its section z -> (z,l(z)) is therefore
open and closed. Take V to be the complement of the nonproper-value set;
over V the map F is finite etale of degree d. A general source line meets
F^{-1}(V), after excluding lines contained in the inverse nonproperness
locus. At any such z the zero-fiber projection has d distinct points.
If d>1, at least one is off the section, proving disconnectedness.

Conversely, d=1 makes F birational and etale, hence an automorphism by
the standard plane endpoint already accepted in the branch-disjointness
report. Then every Psi_L fiber is the graph

    q=F^{-1}(F(l(z))+t),

and is isomorphic to A1. This proves the claimed equivalence.

## Controls, history, and limit of the reduction

For F=id every fiber is explicitly A1. In characteristic p>0 the map
F(x,y)=(x^p-x,y) is Keller but a general source-line pullback has p
components: writing l(z)=(a(z),b(z)), its equations give
(q1-a(z))^p-(q1-a(z))=t1 and q2-b(z)=t2. This is only a scope control;
the accepted characteristic-zero generic-surface premise fails there.

The earlier target-shear genus calculation already used inverse-hyperplane
Bertini for a different curve family; see
[its report](target-shear-genus-swarmHQ-root-20260914.md). The present
application cuts the first-source projection of the generic DIFFERENCE
surface. The full-surface theorem's finite bad-translation set does NOT
transfer to these curve sections: Bertini-good lines may depend on t.

No assertion about genus, properness, complete flows, a locally nilpotent
derivation, or extension of the zero-fiber idempotent follows. In particular,
generic curve integrality does not prove connectedness at zero. This is a
scoped dimensional reformulation, not a new mechanism supplying the missing
specialization implication; no automatic curve/control family is selected.

ROOT read the complete Stacks section 37.32, including the three lemma
proofs, but did not re-audit their cited dependencies. The accepted parent
claims are consumed at their recorded MANUAL/BOOK-relative scope. Native
Astra supplied same-model reconstruction of the Bertini attachment and
constant-line descent, not independent different-model review. No CAS,
scientific computation, engine, seed, prime search, or exit-price assertion.

## COLLISIONS

status: EMPTY

- NONE — no explicitly raised OPEN entries or successor is commissioned.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6370`.
- Body SHA-256:
  `b8de67c5d711eaf4b5cfa208f39039ed605d5e6ce461bc0e10bc1fc4f7e80a48`.
- Frozen basis: `6f2a845a39d6490fdc69fde4a75119fc722a2924`.
