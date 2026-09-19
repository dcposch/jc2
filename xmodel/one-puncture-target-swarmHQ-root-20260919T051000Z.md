# One source puncture excludes polynomial target repairs of elliptic multiplication

Producer: swarmHQ ROOT (Astra assigned context; hosted identity not exposed).
Date: September 19, 2026 UTC.
Frozen basis: 2f8bb48d64d431f96cad7c842ddfe38e61ad7452.
Evidence: MANUAL, with named classical curve imports.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; same-model co-check is not FIRST.
No literature-novelty or JC2-resolution claim.

## 1. Exact different-pencil lemma

Let H:A2_s -> A2_t be a DOMINANT polynomial map over C. Let r_s and r_t
be nonconstant rational functions on the respective planes, with
r_t composed H=r_s. Assume their geometric generic curves are integral
and have genus ONE. If the normalization of the FULL affine source
generic curve has exactly ONE geometric puncture in its smooth projective
completion, then the generic degree of H is ONE.

The two pencils need NOT be the same. Neither a constant Jacobian nor
properness of the affine map is assumed. The source puncture hypothesis
is about its actual affine model, not just its function field.

## 2. Full affine curves, including pencil base points

Use distinct coordinates x,y on the source and u,v on the target. Write
r_s=a_s/b_s and r_t=a_t/b_t in reduced form, and put K=C(t). Define

    q_s=a_s-t*b_s,                 R_s=K[x,y]/(q_s),
    q_t=a_t-t*b_t,                 R_t=K[u,v]/(q_t).

These are the FULL affine generic plane curves, not the opens D(b_s)
and D(b_t). Their fraction fields are L_s=C(x,y) and L_t=C(u,v), with
their separate K-structures t -> r_s and t -> r_t. To identify the kernel,
clear denominators in t and use the primitive irreducible polynomial
a_i-t*b_i; r_i is transcendental over C. Coprimality is essential here.
Geometric integrality stated first on D(b_i) also passes to the full
curve: R_i injects into (R_i)_(b_i), and scalar extension is flat.

Write H=(P,Q). The pencil identity gives in K[x,y]

    b_s*(a_t(H)-t*b_t(H)) = b_t(H)*(a_s-t*b_s).

Since gcd(b_s,q_s)=1, q_s divides a_t(H)-t*b_t(H). Thus substitution
induces a regular map R_t -> R_s, INCLUDING target pencil base points.
On fraction fields it is exactly the injective H*:L_t -> L_s. It fixes
K via the displayed two K-structures, and its degree is

    N=[L_s:H*(L_t)]=degree_gen(H).

Let B_s and B_t be the respective finite normalizations in L_s and L_t.
For z in B_t, applying H* to a monic equation for z over R_t produces
a monic equation for H*(z) over R_s. Hence H*(B_t) is contained in B_s.
This proves a regular dominant map C_s=Spec(B_s) -> C_t=Spec(B_t).
It does not assume that H, or this affine curve map, is finite.

## 3. Completion and the puncture count

Normal curves in characteristic zero are smooth. Over Kbar the curves
remain integral and admit smooth projective completions Cbar_s,Cbar_t.
The map extends to a nonconstant finite morphism f:Cbar_s -> Cbar_t.
Its degree is N: the finite map before scalar extension is flat of rank
N, and that rank survives base change. The classical imports are
[Stacks, section 53.2](https://stacks.math.columbia.edu/tag/0BXX),
particularly Lemmas 53.2.2--53.2.4 and Theorem 53.2.6, with the
characteristic-zero smoothness and scalar-extension facts in 53.2.8--53.2.9.

Both genera are one. The characteristic-zero
[Riemann--Hurwitz formula](https://stacks.math.columbia.edu/tag/0C1B)
gives deg(Ram)=0, so f is unramified. Every geometric target point has
exactly N distinct preimages. Let S_s=Cbar_s minus C_s and
S_t=Cbar_t minus C_t, after scalar extension. These sets are finite,
and S_t is nonempty: a positive-dimensional integral affine curve
cannot also be projective. Affine regularity gives

    f^(-1)(S_t) subset S_s,
    N*|S_t| = |f^(-1)(S_t)| <= |S_s| = 1.

Thus N=1. Only the source puncture count is prescribed; no equality
between the source and target puncture sets or affine models was used.
The linked classical statement groups were checked at this scope,
not as a whole-book proof audit.

## 4. Fixed original Weierstrass source, arbitrary birational target

The [integral-back donor report, section 3](integral-back-coordinate-donor-swarmHQ-root-20260917T161200Z.md)
records the dominant rational plane map

    r=y^2-x^3-a*x,                 Phi_m=(U_m,V_m)=[m](x,y),

for fixed a in C and |m|>=2, using the generic elliptic curve
E_t: y^2=x^3+a*x+t. Multiplication preserves r and has degree m^2;
these are the inherited classical elliptic multiplication facts.

The full source generic affine curve is smooth: its cubic discriminant
-16*(4*a^3+27*t^2) is nonzero in K. Its smooth projective cubic

    Y^2*Z = X^3+a*X*Z^2+t*Z^3

has just one point with Z=0, namely O=[0:1:0]. Thus its affine
normalization has exactly one geometric puncture.

Let tau be ANY birational target change and suppose H=tau composed Phi_m
were polynomial. Set r_s=r and r_t=r composed tau^(-1). The target
pencil has the same geometrically integral genus-one function field,
and r_t composed H=r_s. Dominance and degree m^2 are unchanged by tau.
The lemma forces m^2=1, a contradiction. Therefore NO such H is polynomial,
even before asking whether its Jacobian is constant.

In particular, the one-sided scaling (U_m,V_m/m) is covered: it is one
allowed birational target change. The different target pencil causes
no problem. This statement keeps the ORIGINAL source plane fixed.
Arbitrary rational source changes may change its punctures and are
NOT covered; no arbitrary two-ended repair exclusion is established.

## 5. Controls and exact campaign comparison

The identity map on the source with both pencils r has degree one and
satisfies the assumptions. Genus zero cannot replace genus one: the
polynomial map (x,y)->(x,y^2) preserves r=x, has a one-punctured generic
source A1, and has degree two. The one-puncture input also matters in
the underlying curve argument: for an elliptic curve E, multiplication
restricts to a regular map E minus E[m] -> E minus {O}, of degree m^2.
There are m^2 source punctures. This is a curve-level scope control,
not a polynomial plane map or a Keller counterexample.

The [positive-genus invariant theorem](positive-genus-invariant-swarmHQ-root-20260919T035200Z.md)
uses the SAME pencil and allows arbitrary nonempty affine puncture sets.
It excludes MATCHED birational conjugacy, but explicitly does not cover
one-sided normalization breaking that invariant. The present different-
pencil lemma closes that one-sided gap for the fixed original elliptic
source by using its additional one-puncture geometry.

The integral-back donor test instead fixes the target coordinate ring
and allows finite rational source substitutions. Neither old test by
itself gives this arbitrary-target, fixed-source statement, and their
combination with this result still supplies no theorem for arbitrary
simultaneous source and target changes. Scoped comparisons with frozen
public and HQ histories are bounded history coverage, not a novelty claim.

ROOT checked the proof and a native Astra co-check agreed on the full
curve map, degree, normalization, puncture count and fixed-source
application. This is same-model scrutiny, not different-model FIRST.
No CAS, scientific code, cloud computation or proof assistant was used.
No rational invariant or one-puncture pencil is produced for arbitrary
Keller maps; no new donor, parameter family or descendant is proposed.
JC2 remains unresolved.

## OPEN(S) RAISED

None. No new bounded experiment or provisional descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7579`.
- Body SHA-256:
  `84f6ab718eca50d001336aa5d5491b3714e4c48bdd43427983da144f234daa35`.
- Frozen basis: `2f8bb48d64d431f96cad7c842ddfe38e61ad7452`.
