# Affine radial rational Jacobian pairs cannot be repaired in fixed targets

Producer: swarmHQ coordinator, gpt-6-astra; native gpt-6-astra hostile co-check
Date: 2026-10-16 UTC
Basis: 20924a378586de8d42fcdb71e0b7f685be898893
Evidence tier: MANUAL, conditional on the two accepted classical-import results below
Lifecycle: PRODUCER-CHECKED; UNPROMOTED pending different-model hostile review

## Statement and scope

Let \(t=X/Y\), let \(A,B,C,D\in\mathbb C(t)\), and set
\[
 P=A(t)Y+B(t),\qquad Q=C(t)Y+D(t).
\]
Suppose \(J_{X,Y}(P,Q)=1\). If \((P,Q)\) is genuinely rational, meaning that
at least one of \(P,Q\) is not in \(\mathbb C[X,Y]\), there is no finite field
embedding
\[
 \mathbb C(X,Y)\hookrightarrow\mathbb C(u,v)
\]
under which these same \(P,Q\) become whole-plane polynomials with nonzero
constant \(J_{u,v}(P,Q)\).

Thus finite rational source substitutions cannot repair any genuinely rational
pair affine in the radial variable, in these fixed target coordinates.
Polynomial members of the displayed class are affine automorphisms. The theorem
does not assert that arbitrary Keller pairs reduce to this class, does not allow
arbitrary birational target changes, and does not assert invertibility of an
arbitrary subsequent Keller source substitution in the polynomial-member case.

## Dependencies and prior work

Two previously accepted campaign results are used with their existing scope and
classical-import tiers; their source proofs are not re-established here.

1. The branch-attachment step of
   [SYMPLECTIC-TARGET-SMOOTH-BRANCH-1](../AUDIT.md#symplectic-target-smooth-branch-1--2026-09-16)
   (basis above, AUDIT lines23953–24005): ramification over an affine target
   curve persists under finite source-field extension. If the target functions
   become a polynomial Keller pair, such a curve is a component of its actual
   nonproperness set, via the full finite normalization. Jelonek polynomial
   coverage then makes the curve's normalization \(\mathbb A^1\).
   Only this necessary condition is used: neither the smooth-projective-branch
   hypothesis nor the further smoothness/Chau contradiction is asserted here.
2. The [integral-back-coordinate criterion](integral-back-coordinate-donor-swarmHQ-root-20260917T161200Z.md),
   with its [independent Sol review](integral-back-coordinate-review-swarmHQ-sol-20260917T161900Z.md),
   is recorded as PROMOTED/MANUAL in APPROACHES lines413–424 at the same basis.
   A genuinely rational constant-J donor whose two original source coordinates
   are integral over its output ring admits no such finite rational source repair
   in fixed targets. Its proof makes the source substitution polynomial etale;
   donor poles then cannot disappear.

The new argument combines the first necessary condition with a monic equation
for the normalization parameter of the branch curve and a homogeneous-part
integrality lemma. The rational generating family
\(P=Y-f'(t),\ Q=-tP-f(t)\) is a special case, not the whole class.
The cubic member was already used as a rational donor in September17 campaign
work. Prior carrier Wronskian and extreme-weight tests did not establish this
affine-radial statement. No literature-priority claim is made.

## Argument or computation

### The two Jacobian identities

Since \(dX\wedge dY=Y\,dt\wedge dY\), expanding \(dP\wedge dQ\) gives
\[
 A'C-AC'=1,\qquad B'C-AD'=0. \tag{1}
\]
Primes denote differentiation in \(t\). In particular neither \(A\) nor \(C\)
is identically zero. The nonzero Jacobian makes \(P,Q\) algebraically independent,
and \(\mathbb C(X,Y)/\mathbb C(P,Q)\) is finite.

### A nonconstant translation gives a branch curve

Assume \((B,D)\) is nonconstant and let \(\Delta\) be the closure of its image
in the affine target plane. At the generic point of \(Y=0\) in the smooth
\((t,Y)\) chart, all four coefficients are regular and the map to the target is
a morphism. The divisor has curve image \(\Delta\), and the differential has
rank one there. Its two-form Jacobian is exactly \(Y\), by (1).

The map is generically quasi-finite along this divisor, since its residue map
to the image curve is nonconstant. In characteristic zero the residue extension
is separable, so the Jacobian order is the transverse ramification index minus
one. That index is therefore two. The valuation remains a genuine ramified
valuation of the field extension even though \((t,Y)\mapsto(tY,Y)\) contracts
the divisor to the origin of the original source plane.

If a polynomial Keller landing as in the statement existed, dependency1 would
force the normalization of \(\Delta\) to be \(\mathbb A^1\). Consequently there
is an element \(h\in\mathbb C(B,D)\subseteq\mathbb C(t)\) such that
\[
 B=b(h),\qquad D=d(h),\qquad b,d\in\mathbb C[h]. \tag{2}
\]
There is no assumption that \(t\mapsto h\) has degree one.

### The normalization parameter is integral

The curve \(\Delta\) cannot be a line. Indeed, if \(B\) is constant and \(D\)
nonconstant, the second identity in (1) forces \(A=0\), contradicting the first.
If \(B\) is nonconstant and \(D=\alpha B+\beta\), the same identity gives
\(C=\alpha A\), again contradicting the first. This also covers constant \(D\).

A constant determinant-one linear target change therefore arranges
\[
 0<m=\deg b<n=\deg d.
\]
To see this, unequal degrees can be interchanged by a determinant-one change;
if the degrees are equal, subtract the leading-coefficient multiple of one
coordinate from the other. The resulting lower-degree coordinate is nonconstant,
because otherwise \(\Delta\) would be a line. This change preserves the output
ring, both Jacobian identities, and the radial form of the pair.

The second identity in (1), after cancelling the nonzero \(h'(t)\), yields
\(b'(h)C=A d'(h)\), where these primes denote differentiation in \(h\).
Eliminating \(Y\) gives
\[
 b(h)d'(h)-d(h)b'(h)-P d'(h)+Q b'(h)=0. \tag{3}
\]
As a polynomial in \(h\), its degree is \(m+n-1\) and its leading coefficient is
the nonzero constant
\[
 (n-m)\operatorname{lc}(b)\operatorname{lc}(d).
\]
Indeed, the \(P,Q\) terms have degrees at most \(n-1,m-1\). Dividing (3) by
that constant proves that \(h\), and hence \(B,D\), are integral over
\(R=\mathbb C[P,Q]\).

### Homogeneous part integrality

We prove separately that the first identity in (1) implies
\[
 X=tY,\ Y\quad\hbox{are integral over }\quad
 R_0=\mathbb C[A(t)Y,C(t)Y]. \tag{4}
\]
Let \(V\) be any valuation ring of \(\mathbb C(t,Y)\) containing \(R_0\).
It contains \(\mathbb C\), so its valuation is trivial on \(\mathbb C^*\).
Its restriction to \(\mathbb C(t)\) is either trivial or centered at a point
of \(\mathbb P^1\); no rank-one assumption on \(V\) is needed.

If this restriction is trivial, \(A,C,t\) are units and \(A Y\in V\) implies
\(Y,X\in V\). If the center is a finite point \(t=a\in\mathbb C\), then
\(t\in V\). Were \(Y\notin V\), nonnegativity of both products would force
\(A,C\) both to have strictly positive valuation, hence both to vanish at \(a\).
But two rational functions regular and vanishing at the same finite point make
\(A'C-AC'\) vanish there, contradicting (1). Thus \(Y,X\in V\).

At infinity put \(s=1/t\) and
\[
 a(s)=sA(1/s),\qquad c(s)=sC(1/s).
\]
Then \(A(t)Y=a(s)X\), \(C(t)Y=c(s)X\), and direct differentiation gives
\[
 a'c-ac'=-1.
\]
A pole of \(X\) would force both \(a,c\) to vanish at zero, which is impossible
by this identity. Hence \(X\in V\), and \(Y=sX\in V\) too. Since all valuation
rings containing \(R_0\) contain \(X,Y\), the valuative criterion for integral
closure proves (4).

### Completion and polynomial members

If \(B,D\) are constant, (4) immediately makes \(X,Y\) integral over \(R\).
If they are nonconstant, a hypothetical landing forces (2), and (3) makes
\(B,D\) integral over \(R\). Therefore \(A Y=P-B\) and \(C Y=Q-D\) are integral
over \(R\). Equation (4) and transitivity of integrality give \(X,Y\) integral
over \(R\) again. Dependency2 excludes the genuinely rational donor in either
case. If the normalization of \(\Delta\) is not \(\mathbb A^1\), dependency1
already excludes the hypothetical landing.

Finally, under \((X,Y)\mapsto(\lambda X,\lambda Y)\), each displayed output has
only homogeneous degrees zero and one. If it is a polynomial, its degree-zero
part is constant and its degree-one part is linear. Thus a polynomial pair in
this class is affine, and its Jacobian one makes it an affine automorphism.
This completes exactly the stated dichotomy.

## Replay and negative controls

Desk-only. No CAS, parameter search or external source-body fetch is used.
The producer argument and the native Astra hostile co-check agree. The latter
completed at2026-10-16 21:43:46 UTC against the same displayed proof; it checked
the branch valuation, possibly non-birational normalization parameter, degree
reduction, all-valuation lemma and quantifiers. It is not a different-model FIRST.

Three controls delimit the result:

- \(P=Y, Q=-X\) satisfies (1) and is polynomial. The genuine-rationality hypothesis
  is necessary; the theorem must not reject this affine automorphism.
- \(P=X^2/Y, Q=Y^2/(3X)\) is homogeneous rational with Jacobian one. Here
  \(A=t^2,C=1/(3t),B=D=0\), and explicitly
  \(X^3=3P^2Q\), \(Y^3=9PQ^2\). It tests the constant-translation case and
  shows why both finite and infinite directions must be included in (4).
- \(P=Y-3t^2, Q=-tY+2t^3\) has translation curve
  \((B,D)=(-3t^2,2t^3)\), a cusp with normalization \(\mathbb A^1\), not a smooth
  affine line. Its relation \(t^3+Pt+Q=0\) illustrates the integrality step.
  The proof uses normalization, not an unsupported smoothness assumption.

The canonical adjacent artifact manifest pins these frozen proof bytes. Verify
with `python3 ops/artifact_finalize.py verify --final xmodel/affine-radial-obstruction-swarmHQ-root-20261016T214900Z.md`.

## Limitations and next test

This filters an all-degree family of rational construction candidates; it does
not supply a general normal form for Keller maps or decide the campaign's actual
finite-normalization boundary problem. Polynomial target automorphisms preserve
the output ring, but arbitrary birational target repairs are not covered.
The next test is an independent different-model hostile review of this frozen
statement, the new proof, and applicability of the two accepted imports.

## OPENS RAISED

None. No speculative extension or new computational farm is admitted here.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10533`.
- Body SHA-256:
  `00b0346f9e9b32257a0641465df0e32ba4392b5f7221dd12911917bc8e0a836d`.
- Frozen basis: `20924a378586de8d42fcdb71e0b7f685be898893`.
