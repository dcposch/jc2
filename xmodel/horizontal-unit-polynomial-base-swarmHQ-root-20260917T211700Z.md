# Geometric generic units can be detected over a horizontal polynomial base

Producer: swarmHQ, ROOT (gpt-6-astra); independent same-model manual co-check by Astra.
Date: 2026-09-17 UTC; native co-check finished 21:15:15, independently terminal at 21:18 UTC.
Basis: edee3f0a80b8e5ecd4c4cea149788664e7e7db2d.
Evidence tier: MANUAL, self-contained geometric and algebraic argument.
Lifecycle: PROVISIONAL; different-model hostile review pending. Same-model agreement is not that review.
Claim: HORIZONTAL-UNIT-POLYNOMIAL-BASE-1.

## Statement and scope

Let P be a nonconstant polynomial in C[x,y] whose generic fiber is
geometrically integral. Put K=C(t), with t mapped to P, and
R_K=C[x,y] tensor_{C[t]} K. Write a non-base unit for an element of
(R_K tensor_K E)^* outside E^*, where E/K is a field extension.

**A. Polynomial-base detection.** If R_K tensor_K Kbar has a non-base
unit, there is a nonconstant h in C[s] such that R_K tensor_K C(s)
has a non-base unit, where the base map is t=h(s). More precisely,
one may choose C(s)/K from the function field of one horizontal boundary
component of any smooth SNC resolution of the P-pencil obtained by
point blowups over the line at infinity. There are finitely many such
components for a fixed resolution.

**B. Globalization with extra hypotheses.** Suppose additionally that P
has no critical points and every closed fiber P^{-1}(a) is irreducible.
For one of the h in A, the smooth integral affine surface

    X_h = Spec C[x,y,s]/(P(x,y)-h(s))

has a nonconstant global unit whose restriction to its generic s-fiber
is non-base. No power of the unit obtained in the proof of A is needed:
multiplication by a rational function of s suffices. The selected h then
has degree at least two.

Equivalently, under the extra hypotheses, geometric-generic unit
vanishing follows if global units are constant on X_h for each of the
finite list of horizontal-component covers. This is a REDUCTION to
those unit-vanishing problems, not a solution of them.

There is no assertion that the selected polynomial field lies in a
previously fixed field of definition of the original unit. We enlarge
that field and replace the unit by a product of conjugates. This
qualification is essential to comparison with the D4 counterexample.

## Dependencies and prior work

The proof uses resolution of a pencil on a smooth surface by point
blowups, Stein factorization for a proper map to a normal curve,
characteristic-zero generic smoothness, Galois descent for coordinate
rings, and the codimension-one criterion for regular functions on a
normal affine variety. Each application is specified below. No Hodge
splitting or generic-to-special topological comparison is assumed.

The geometric observation that a horizontal boundary component meets
a connected infinity fiber at only one point is known. A scoped primary
source check found it in the proof of Theorem 3.9(a), printed pages 9–10,
of A. J. Parameswaran and M. Tibar, *On the Geometry of Regular Maps From
a Quasi-Projective Surface to a Curve*, OWP2013-03 (January 25, 2013):
[primary preprint](https://publications.mfo.de/bitstream/handle/mfo/1053/OWP2013_03.pdf?isAllowed=y&sequence=1).
We use only that tree argument, reproved here for the resolved A2 pencil;
we do not import its broader monodromy or purity conclusions. The source
was read in selected relevant passages, not audited in its entirety.

Nearest campaign results, both read in full:

- [Generic-unit globalization](geometric-unit-globalization-swarmHQ-root-20260916T232700Z.md),
  SHA256 87dc47e2ff7ae6caab9e5b0d434b1cdc596b5b958ce83ccbf6ad60aded89cf21:
  on an arbitrary finite base curve, an appropriate power and base
  rescaling globalize a generic unit under nonsingularity and all-fiber
  irreducibility. The new step here selects a polynomial base from actual
  boundary geometry, after which its Picard obstruction is trivial.
- [D4 rational-base counterexample](d4-rational-base-counterexample-swarmHQ-root-20260917T191600Z.md),
  SHA256 65906bbadc41f8107df0a2d76f7c8966b77b07e52289c689a2a5867f86d4a29a:
  abstract representation and cohomology conditions do not force a
  suitable intermediate A1 quotient in a fixed cover. That accepted
  counterexample is not retracted, repaired, or contradicted here.

The campaign's earlier separated-variable topology screen leaves a gap:
a theorem about a generic fiber of P(x,y)-h(s) does not establish the
needed topology of its particular zero fiber. This report does not fill
that gap. Scoped history searches found no exact prior campaign statement
of the stabilizer-norm reduction; this is not an exhaustive novelty claim.

## Argument

### 1. The actual polynomial pencil supplies polynomial puncture fields

Resolve P:P2 -->> P1 by point blowups supported over the line at infinity.
Further point blowups there can make the reduced boundary SNC. Obtain a
smooth projective surface X, a morphism f:X->P1, and an unchanged open A2
on which f=P. Its reduced boundary D=X\A2 is a tree of smooth rational
curves. Initially it is the line at infinity; blowing up a smooth point
of the boundary adds a leaf and blowing up an intersection subdivides an
edge. These operations preserve the tree and rationality assertions.

Geometric integrality of the generic fiber makes the finite part of the
Stein factorization trivial. Indeed, the function field of that finite
part is the algebraic closure of K in C(X), which is K; the finite
birational map to normal P1 is an isomorphism. Consequently all fibers
of f are connected. Its fiber over infinity is entirely contained in D,
since P is regular and finite-valued on A2. Its reduced support D_infty
is therefore a connected subtree of D. Multiplicities are irrelevant to
connectedness and are not asserted to be one.

Let B be a horizontal boundary component. The nonconstant morphism
B=P1 -> P1 is finite and surjective. Its inverse image of infinity is
exactly B intersect D_infty, so it is nonempty. It contains at most one
point: two intersections would attach the vertex B to the connected
subtree D_infty twice and create a cycle. Two intersections with the
same component likewise give two edges and a cycle. SNC excludes triple
points and tangencies that could obscure this graph description.

Thus B has a unique point over infinity. Choose a coordinate s on B
whose only pole is that point. The rational function f|B has no other
pole, hence equals a polynomial h(s). Therefore

    E_B = C(B) = C(s),    K -> E_B given by t -> h(s).

The generic intersection of B with X_K is a closed boundary point with
residue field E_B. Distinct horizontal components meet only in finitely
many special fibers, so this describes the closed points of the generic
boundary without an identification at crossings.

### 2. A puncture stabilizer preserves one nonzero unit valuation

The generic fiber X_K is a smooth projective geometrically integral
curve: generic smoothness applies in characteristic zero, and its open
affine part is Spec R_K. Let u be the assumed geometric-generic unit.
On X_Kbar its principal divisor is supported on the boundary. It is not
zero, since a rational function with no poles on a projective integral
curve is constant. Choose a geometric boundary point xi such that

    n = ord_xi(u) != 0.

Choose a finite Galois extension L/K inside Kbar that defines both u and
u^{-1} and splits all generic boundary points. Put G=Gal(L/K) and
H=Stab_G(xi). If the underlying closed point belongs to B, its residue
field, with the embedding selected by xi, is E_B. The action on the
geometric points of this closed point is the action on embeddings of
E_B into L. Therefore H=Gal(L/E_B) and L^H=E_B.

Use the semilinear action on R_K tensor_K L and set

    v = product_{sigma in H} sigma(u).

Both v and v^{-1} are H-invariant elements of that coordinate ring.
Galois descent gives v in (R_K tensor_K E_B)^*. Every sigma in H fixes
xi, so the induced local-ring isomorphism preserves its discrete
valuation. Hence

    ord_xi(v) = sum_{sigma in H} ord_xi(sigma(u))
              = |H| n != 0.

Elements of E_B^* are constants on this curve and have valuation zero.
Thus v is non-base. This proves A. Using H instead of all of G is the
essential noncancellation step; a full G-norm may lose the information.

If u was initially defined over E0, E_B need not be contained in E0.
The extension L was enlarged to split the punctures as well as to
define u. The construction is not literal descent of u, nor a theorem
about intermediate quotients of an arbitrarily prescribed cover E0/K.
In particular it makes no claim excluding actual units on the specific
D4 cover in the cited report.

### 3. Globalization on the selected A1 base

Assume now that P is nonsingular and every closed fiber is irreducible.
The morphism P:A2->A1 is smooth. Its base change X_h->A1_s is smooth
and flat; its closed fibers are reduced irreducible curves. Its generic
fiber is geometrically integral, so its total space is integral: smooth
flatness gives no vertical irreducible components, and the generic
fiber has one component. In particular X_h is a smooth normal affine
surface, and its generic-fiber function field is its function field.

View v from step 2 as a rational function on X_h. Since v and v^{-1}
are regular on its generic s-fiber, its divisor has only vertical prime
components. Irreducibility and reducedness identify those primes with
the entire closed fibers F_a, and flat smoothness gives multiplicity one:

    div_Xh(v) = sum_a n_a F_a,    F_a = div_Xh(s-a),

with finitely many n_a nonzero. Set q(s)=product_a(s-a)^{n_a} in C(s)^*.
Then w=v/q(s) has divisor zero on X_h. Normality implies that w and
w^{-1}, having no codimension-one poles, are regular everywhere. Thus w
is a global unit. Its generic restriction is still non-base, because
division by q(s) cannot turn a non-base element into a base element.

If deg h=1, eliminating s identifies X_h with A2, whose only global
units are C^*. This contradicts the non-base restriction of w. Hence
deg h>=2. This proves B.

## Replay and negative controls

Desk-only; no scientific computation, parameter search, or new external
execution is evidence for the proof. ROOT reconstructed all three steps;
a separate same-model Astra task attacked the tree, residue-field,
stabilizer, normality and degree-one implications and returned agreement.
It did not audit the primary source. Different-model review is still due.

- Coordinate control P=x has geometric generic fiber A1 and no non-base
  units. A horizontal cover alone therefore does not manufacture units.
- Reducible-fiber control P=xy has the generic unit x, with a degree-one
  polynomial base already sufficient for A. There is no global non-base
  unit on A2. In particular no power x^e, e>0, can be made a global unit
  by base rescaling: the two valuations at x=0 and y=0 differ by e,
  whereas a function of xy contributes equally. This illustrates why B
  needs the extra fiber assumptions and why its degree bound is not A's.
- The subgroup norm cannot be silently replaced by the full norm. Under
  a larger group, conjugation may move xi to punctures with opposite
  valuations. Only the displayed stabilizer computation proves the
  nonzero valuation of v.
- The D4 fixed-cover module counterexample is a scope control, not an
  example of units realized on an actual polynomial generic fiber.

No new exit-price assertion; FALLACY-v2's charge declaration is inapplicable.
Basis/source maps, geometric punctures and closed boundary points are kept
distinct. No unit-vanishing assertion is inferred from genericity or a cap.

## Limitations and next test

The immediate bounded test is different-model hostile review of the three
proof steps, the E0 versus E_B qualification, and the globalization
hypotheses. No dependent research or promotion should precede that gate.

Even if confirmed, the remaining mathematical task is unit vanishing on
the selected smooth polynomial-cover surfaces under the stated extra
hypotheses. This report provides no such theorem, no H1 vanishing, no
generic-to-special comparison and no splitting of a mixed period sequence.
It does not establish every-fiber irreducibility for arbitrary Keller
coordinates, global properness, or the Plane Jacobian Conjecture.

## OPENS RAISED

None new. Existing polynomial-cover unit-vanishing and source-hypothesis
gaps remain; the report changes the reduction feeding them, not their status.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12592`.
- Body SHA-256:
  `f6e7f3e4a5172573a55a177e0fcea188a70c55bd2637c8f821b831e4c7d9d1ad`.
- Frozen basis: `edee3f0a80b8e5ecd4c4cea149788664e7e7db2d`.
