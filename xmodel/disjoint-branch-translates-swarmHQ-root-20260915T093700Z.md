# Disjoint branch divisors and translated Keller fiber products

Producer: swarmHQ ROOT (gpt-6-astra). Basis:
`18acf7b12245b8eaf2f419a031ea01e7d16f18c1`.
Evidence: MANUAL with named standard/primary imports.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED. Novelty UNKNOWN.
No computational certificate, exit-price assertion, degree bound, or JC2 proof.
Authoring lease opened September 15, 2026 at09:35:55 UTC.

## Statement

Let \(F:\mathbb A^2_{\mathbb C}\to\mathbb A^2_{\mathbb C}\) be a
polynomial map with nonzero constant Jacobian, and let
\[
X_t=\{(p,q):F(p)-F(q)=t\},\qquad t\in\mathbb C^2.
\]
Let \(K=\mathbb C(u,v)\), let \(L/K\) be the function-field extension
defined by \(F\), and let \(M/K\) be its finite Galois closure in a fixed
algebraic closure. Let \(D\) be the reduced branch divisor of the finite
normalization of the target in \(M\).

1. If \(D\) and \(D+t\) share no irreducible component, \(X_t\) is
   nonempty and irreducible (indeed a smooth affine surface).
2. There is a finite set \(T\subset\mathbb C^2\) outside which all
   \(X_t\) are irreducible. If \(D\) has \(r>0\) components, one can
   take \(T=\{t:D_i=D_j+t\text{ for some }i,j\}\), with
   \(|T|\le r(r-1)+1\). This is a containment for the exceptional locus,
   not a claim that every element of \(T\) is exceptional.
3. If \(D=\varnothing\), \(F\) is an automorphism. Otherwise the above
   argument says nothing about irreducibility of \(X_0\).

This restricts the parameter locus; it does not exclude an isolated
disconnected zero fiber. The number \(r\) is not bounded uniformly here.

## Proof of the branch-disjointness assertion

The Jacobian hypothesis makes \(F\) etale, hence dominant and quasi-finite.
Its generic coordinate algebra is the finite separable field extension
\(L/K\). Normalizations in finite field extensions are finite because
the polynomial target is excellent. Purity applies because the target is
regular and the normalizations are normal.

Write \(F_t(q)=F(q)+t\). Its function field over the same target \(K\)
is denoted \(L_t\), not identified with \(L\) as a \(K\)-extension by
matching variable names. Its Galois closure \(M_t\) has branch divisor
\(D+t\). The variety \(X_t\) is the fiber product of \(F\) and
\(F_t\), with common target coordinate \(z=F(p)=F(q)+t\).

Put \(E=M\cap M_t\) inside a common algebraic closure of \(K\).
For every prime divisor of the affine target, at least one of \(M/K\)
and \(M_t/K\) is unramified at all places over it: this is exactly where
the no-common-component hypothesis is used. Subextensions of such an
unramified extension remain unramified. One can check this after passing
to a strict henselization of the corresponding discrete valuation ring,
where its finite etale algebra splits. Thus \(E/K\) is unramified over
every target prime divisor.

The finite normalization \(Y_E\to\mathbb A^2\) is consequently etale
everywhere by Zariski--Nagata purity. In the local formulation, source
normality, target regularity, quasi-finiteness, equality of local dimensions,
and unramifiedness at codimension-one specializations all hold. See
[Stacks Project, Lemma58.21.4](https://stacks.math.columbia.edu/tag/0BMB).
Its analytification is a finite topological covering of the simply connected
space \(\mathbb C^2\). Since \(Y_E\) is connected, the covering has
one sheet. Hence \(E=K\).

For two finite Galois extensions, trivial intersection implies linear
disjointness. Therefore \(M\) and \(M_t\), and hence their subfields
\(L\) and \(L_t\), are linearly disjoint over \(K\). The generic
fiber algebra \(L\otimes_K L_t\) is a field. Using arbitrary non-Galois
fields directly in the intersection argument would not justify this step.

The projection \(X_t\to\mathbb A^2_z\) is etale, being a composition
of a base change of an etale map with another etale map. Thus \(X_t\)
is regular. Its finitely many irreducible components are disjoint open
and closed subsets; each nonempty component has nonempty open image in
the irreducible target, and therefore dominates it. The generic fiber is
integral, so there can be only one component. There is no vertical component
hidden by passage to function fields. Nonemptiness also follows directly:
the image of \(F\) is a dense open set \(U\), and \(U\cap(U+t)\)
is nonempty. No properness of \(F\) or its fiber product was assumed.

An equivalent algebraic check avoids component language entirely. With
\(A=\mathbb C[z_1,z_2]\), the actual fiber-product coordinate ring
\(C_t=\mathbb C[p_1,p_2]\otimes_A\mathbb C[q_1,q_2]\) is \(A\)-flat,
since both factors are etale \(A\)-algebras. It therefore injects into
\(C_t\otimes_AK=L\otimes_KL_t\), a field, and is a domain.

## Why the exceptional-translation set is finite in the plane

Let \(A_F\) be the nonproper-value set. Off \(A_F\), the original
map is finite etale, so its finite Galois closure is etale there as well.
Consequently \(D\subset A_F\). Only this inclusion is needed; equality
with the non-Galois branch locus or the entire nonproperness set is not
assumed. Each component of \(D\) is therefore a component of \(A_F\).

Chau's primary text explicitly states that a plane polynomial map whose
nonproper-value set has a component isomorphic to the affine line must
have a singularity. Applied to our nonsingular \(F\), no \(D_i\) can
be an affine line. The source is [Nguyen Van Chau,
arXiv0710.5212v1](https://arxiv.org/pdf/0710.5212), printedp3, discussion
following(1.4) and Theorem1.2. This is an imported theorem, not a new
audit of its Newton--Puiseux proof. Its hypothesis concerns the whole
component, not just its normalization or a polynomial parametrization.

An irreducible algebraic plane curve \(C\) invariant under a nonzero
translation \(v\) must itself be an affine line. Indeed for any \(p\in C\),
all \(p+nv\), \(n\in\mathbb Z\), lie in \(C\). Every defining
polynomial then vanishes identically on \(p+\mathbb C v\), since its
restriction has infinitely many roots. The line is contained in \(C\)
and equals it by irreducibility and dimension. Thus each \(D_i\) has
trivial translation stabilizer.

For fixed \(i,j\), there is at most one \(t\) with \(D_i=D_j+t\):
two would give a nonzero stabilizer. The self-pairs all give the same
translation0, while there are \(r(r-1)\) ordered distinct pairs.
This proves the stated finite bound. Intersections at finitely many target
points do not count as common components and do not obstruct purity.

If \(D\) is empty, the same finite-etale-cover argument gives \(M=K\),
so \(F\) is birational and etale. Zariski's Main Theorem makes it an
open immersion into the normal target. Its image cannot omit a divisor:
a polynomial cutting out such a divisor would pull back to a nonconstant
unit on \(\mathbb A^2\). If the complement has codimension at least2,
normality extends the inverse coordinate functions across it, giving a
polynomial inverse. Hence \(F\) is an automorphism.

## Controls, scope, and remaining gap

The field step genuinely uses characteristic zero through simple
connectedness of affine space for finite etale covers. Over an algebraically
closed field of characteristic \(p>0\), \(F(x,y)=(x^p-x,y)\) has constant
Jacobian \(-1\) and empty branch divisor, yet every \(X_t\) is the
disjoint union of \(p\) affine planes, from the distinct roots of
\(w^p-w=t_1\) and \(y_1-y_2=t_2\). This is an elementary scope check,
not a characteristic-zero Keller counterexample or a construction family.

If \(F\) has generic degree greater than1, \(X_0\) has its diagonal
as a nonempty open-and-closed component and a nonempty off-diagonal part.
The new containment permits this:0 belongs to \(T\) whenever \(D\ne\varnothing\).
Thus neither generic connectedness nor finiteness of the exceptional set
establishes JC2. No theorem excluding such an isolated disconnected fiber
of this actual smooth difference map is supplied. No generic fiber is
asserted isomorphic to \(\mathbb A^2\); no locally nilpotent derivations,
proper family, finite secant map, or boundary no-escape bound is inferred.

Nearest history: the earlier canonical collision/secant tests in the frozen
`notes.md` distinguish quasi-finiteness from properness; the current
Bonnet2003 source gate left generic connectedness unproved and did not
establish an additive-group action. The present common-Galois-subfield
argument supplies a different, limited implication. Scoped searches for
translated covers, disjoint branch divisors and linear disjointness found
no exact history entry. Chau's source had already been inspected for other
scope questions (historical journal around line22448). Neither a missing
literal hit nor this useful composition establishes novelty.

No new OPEN task is commissioned by this report. The existing zero-fiber
connectedness gap remains; a successor would require a separately admitted
actual-source implication and independent review before reliance on this
unpromoted result. The producer checked the algebra and source attachment
manually; computational engines, seeds and primes are inapplicable.

Independent native Astra task `frobenius_source_gate` completed its
message-only attack at09:37:45 UTC: CONFIRMED at precisely the manual,
unpromoted scope. It checked the sign, Galois common-field step and actual
flat coordinate ring; ROOT separately checked the primary no-line source.
This is same-model co-research, not different-model FIRST or promotion.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9528`.
- Body SHA-256:
  `72bfcf84759596ce708ea1c7927699f87df01453e48fa8581ae9aee4a1a5fc09`.
- Frozen basis: `18acf7b12245b8eaf2f419a031ea01e7d16f18c1`.
