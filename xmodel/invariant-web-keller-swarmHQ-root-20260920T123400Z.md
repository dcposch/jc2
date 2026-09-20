# A preserved finite algebraic web forces a plane Keller map to be invertible

Producer: swarmHQ ROOT, Astra-assigned seat; hosted identity not independently
attested. September 20, 2026. Evidence: MANUAL with named accepted and classical
imports. Lifecycle: PRODUCER-CHECKED / UNPROMOTED; different-model hostile FIRST
is required before promotion or descendants.
Frozen public basis: 2db51ba4dae686f7bc8c60a9521ff3b8f9ec8306.

## 1. Exact conditional statement

**INVARIANT-WEB-KELLER-1 (proposed).** A polynomial map
F:A2_C -> A2_C with nonzero constant Jacobian determinant which preserves
a finite algebraic web is a polynomial automorphism. The same conclusion
holds if a positive iterate preserves such a web.

Here a reduced k-web, k>=1, means a generically unordered set of k DISTINCT
algebraic tangent-line directions. On the affine plane it can be represented
by a homogeneous binary polynomial

    W(x,y;u,v) = sum_{i=0}^k a_i(x,y) u^(k-i) v^i,
    a_i in R=C[x,y], gcd(a_0,...,a_k)=1,

whose projective roots are distinct over an algebraic closure of K=C(x,y).
The variables u,v represent a tangent vector; equivalently W is a primitive
polynomial symmetric k-differential. Clear rational coefficient denominators
and divide their gcd to get this representation for any algebraic web.
Isolated common zeros of the coefficients and special-fiber collisions are
initially allowed. No generic factorization over K or global splitting is
assumed. Preservation means preservation of THIS SAME generic set of
directions under pullback by F, not simply having a web on each endpoint.

This theorem does NOT supply an invariant web for a hypothetical
noninvertible Keller map, bounded direction-orbit growth, or an algebraic
invariant line on a finite cover. It is not a JC2 proof or a novelty claim.

## 2. Dependencies and comparison

Use the accepted campaign statements at their binding scopes:

- **INVARIANT-FOLIATION-KELLER-1**: a polynomial plane Keller map with ANY
  nonzero constant Jacobian preserving an algebraic foliation, or having a
  positive iterate that does so, is an automorphism. See the
  [producer](invariant-foliation-keller-swarmHQ-root-20260920T100525Z.md)
  and [binding FIRST integration](invariant-foliation-first-integration-swarmHQ-root-20260920T103300Z.md).
- **RATIONAL-PENCIL-UNIFICATION-1**: a polynomial plane Keller map preserving
  any nonconstant rational pencil is an automorphism. In particular it
  applies to h(F)=a*h with nonconstant polynomial h and a nonzero constant.
  See the [binding FIRST integration](rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md).

These retain their own classical and primary-source dependencies, including
the foliation theorem's Favre--Pereira import; they are not independently
re-audited here. Their full input hashes are recorded in Section 8.

Additional classical facts: a Keller morphism is etale and quasifinite;
projective quasifinite morphisms are finite; finite etale covers of A2_C
are disjoint unions of copies of A2_C. For the latter, analytification is
a finite topological covering of simply connected C2; each connected
component has degree one and its finite birational map to normal A2 is an
isomorphism. Thus no simply-connected assertion about a punctured plane or
arbitrary finite cover is being substituted. The elementary discriminant
identities used below are explained explicitly.

The earlier [Bass/web source-fit](bass-specialization-web-scope-swarmHQ-root-20260914.md)
tested web-extension and completeness theorems without obtaining a global
inverse. Here the changed hypothesis is a web preserved by the SAME map,
and the mechanism is its discriminant on the original affine plane.
The earlier failed projective-tangency import is not used. Both frozen
public evidence and the HQ journal were searched before admission;
bounded comparison is not an exhaustive literature search.

## 3. Primitive pullback has a constant multiplier

Write F=(P,Q), det(DF)=c in C*. For a binary form, define

    (F*W)(x,y;u,v) = W(P,Q; P_x*u+P_y*v, Q_x*u+Q_y*v).

The coefficient vector is obtained from (a_i(F)) by an invertible
R-linear matrix, namely the appropriate symmetric-power representation
of DF. Its inverse has polynomial entries because DF^{-1} does. Hence
these two coefficient vectors generate the same ideal in R.

Primitivity of (a_i) implies their common-zero set in A2 is finite or
empty: any curve component would give a common irreducible factor in R.
If an irreducible q divided every a_i(F), F would map the entire curve
V(q) into that finite set, contradicting quasifiniteness. Therefore F*W
is primitive. This does not assume the coefficient ideal is the unit
ideal, nor that F is proper or surjective.

Preservation and generic reducedness give F*W=lambda*W for lambda in K*:
two binary forms of equal degree with the same distinct projective roots
are proportional. Write lambda as a reduced polynomial fraction. Its
denominator divides all a_i, so is constant; primitivity of F*W makes
its numerator constant as well. Thus

    F*W = lambda W,                 lambda in C*.                (1)

For k=1 this is an invariant algebraic foliation and the accepted theorem
already proves the result. Henceforth k>=2.

## 4. The discriminant dichotomy

Let Delta=Disc(W) in R be the binary-form discriminant. It is nonzero
because the generic projective roots are distinct. The identities are

    Disc(a W) = a^(2k-2) Disc(W),
    Disc(W composed M) = det(M)^(k(k-1)) Disc(W).                 (2)

To see the determinant exponent, factor W into k linear forms over a
splitting field. Up to a fixed sign its discriminant is the product of
the squared pairwise 2-by-2 determinants of their coefficient rows.
Changing tangent variables by M multiplies each determinant by det(M);
there are k(k-1)/2 pairs. Scaling the binary form gives its standard
homogeneous discriminant degree 2k-2. These are polynomial identities,
so the factorization need not exist over R or K.

Applying (2) to (1), with the coefficients first substituted by F, gives

    c^(k(k-1)) Delta(F) = lambda^(2k-2) Delta.                   (3)

If Delta is NONCONSTANT, (3) is a preserved polynomial pencil and the
accepted rational-pencil theorem proves that F is an automorphism.
We need not assume Delta irreducible or that its zero set is smooth.

Only the case Delta in C* remains. Importantly, Delta=0 identically is
not a third branch: it was excluded by the definition of a reduced web.

## 5. Constant discriminant splits the direction cover on A2

Consider the CLOSED algebraic incidence variety

    H = {((x,y),[u:v]) in A2 x P1 : W(x,y;u,v)=0}.

Nonzero constant Delta implies that at EVERY base point the specialized
binary form is nonzero and has exactly k distinct projective roots. Thus
H->A2 is projective with finite fibers, hence finite. It is etale: in a
slope chart containing a chosen root, the derivative of the root equation
with respect to the slope is nonzero, so the algebraic etale criterion
applies. Using both P1 charts retains directions with infinite slope.
There are no omitted coefficient-base points: a zero binary form would
have zero discriminant when k>=2.

Consequently H->A2 is a finite etale degree-k cover of the WHOLE affine
plane. By the classical fact in Section 2,

    H = H_1 disjoint-union ... disjoint-union H_k,
    H_i -> A2 an algebraic isomorphism.                         (4)

Each H_i therefore defines an algebraic section of the projectivized
tangent bundle, hence a line distribution and an algebraic foliation
on A2. Rank-one distributions on a surface are integrable. For use of
the accepted criterion one can also represent its generic direction by
a rational one-form and clear denominators to a primitive polynomial
one-form. No finite branched cover is identified with A2 in this step.

## 6. The map permutes the sheets, so an iterate preserves a foliation

The polynomial inverse of DF ensures that

    ((x,y),[u:v]) -> (F(x,y),[DF(x,y)*(u,v)])

is a regular map on A2 x P1. Equation (1) restricts it to H->H.
Since each H_i is connected and the target components in (4) are open
and closed, H_i maps into one H_{sigma(i)}. The index does not vary
with (x,y). At any base point DF is invertible and maps the k distinct
directions bijectively onto the k directions over its image; therefore
sigma is a PERMUTATION, not merely a map of a finite set.

A positive power, for example k!, fixes every sheet. F^(k!) thus
preserves an algebraic foliation on the ORIGINAL A2. The accepted
invariant-foliation theorem implies that F is an automorphism. Combined
with Section 4 and the k=1 case, this proves the proposed statement.

If F^m instead preserves the web initially, its Jacobian is c^m, so
the argument applies to F^m. An invertible iterate gives a polynomial
inverse of F by composing (F^m)^{-1} with F^(m-1). No degree-one
assumption on F, its restriction to a leaf, or the direction cover
was used in advance.

## 7. Checks and excluded stronger readings

- For W=u*v and F=(a*x,b*y), lambda=c=a*b and (3) reads c^2=lambda^2,
  checking the k=2 exponents. F=(y,x) permutes the two directions, so
  passing to an iterate genuinely belongs in the argument.
- W=v^2-x*u^2 is primitive and generically reduced but has discriminant
  4x. Its root cover is branched, not a trivial finite-etale cover.
  The identity map preserves it; our NONCONSTANT discriminant branch
  uses the pencil instead of asserting that this web splits.
- The non-Keller F=(x^2,y) preserves W=u*v but F*W=2x*W. This checks why
  etaleness/invertibility of the polynomial Jacobian matrix is essential
  to the constant-multiplier step.
- An actual Keller coframe does not provide the required invariant web.
  For example F=(x+y^2,y) pulls W=u*v*(u+v) back to
  (u+2y*v)*v*(u+(2y+1)*v), not a rational scalar multiple of W.
  Thus F*(the standard web) is not automatically the SAME standard web.

The statement is sufficient, not asserted necessary for automorphy. It
does not prove finite-orbit stabilization of directions, preservation
of an algebraic tensor, local-to-global algebraization, or any global
existence premise. No descendants or new web/control family are proposed.
There is no CAS experiment or formal certificate; same-model checking
would not count as independent FIRST.

## 8. Frozen dependency pins

Foliation producer full SHA256:
1ccc0fc8d9f70ca9d9743efee2d63aa5d390219f0f87fb045be88d543e7a9054.
Foliation binding integration full SHA256:
5bf434b3d273ffaf5cecbae754556553e0f27f8b5c3058edea84dd0b1e335a16.
Pencil binding integration full SHA256:
433840900e0edd661cce65557e1f05b8fbf8acc4dd00f90ece863c9d82896926.
All three were read whole and matched their retained pins before drafting.
No new external classification theorem or paper body is imported here.

## OPEN(S) RAISED

None. This report does not commission invariant-web existence or a family.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised open entries.

Trusted `ops/open_collision.py` check of this partial returned EMPTY;
this checks recorded identifiers, not novelty or mathematical correctness.

Author completion: 2026-09-20 12:37:25 UTC, after whole-body readback,
manual checks, unchanged dependency pins and the trusted collision check.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11336`.
- Body SHA-256:
  `ce95a1b0455d3eeeb3ad0f9d28c58ff563109c6952ab23c9d06ae09eb396f4af`.
- Frozen basis: `2db51ba4dae686f7bc8c60a9521ff3b8f9ec8306`.
