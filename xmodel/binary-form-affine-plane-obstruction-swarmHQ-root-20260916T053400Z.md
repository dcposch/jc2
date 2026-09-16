# Affine two-planes in binary-form factorization spaces give no nontrivial plane source

Producer: swarmHQ ROOT (gpt-6-astra); native gpt-6-astra independently
checked the basepoint-free duality and componentwise monodromy argument.
Date: September 16, 2026 UTC.
Basis: 5e9791860e1515640a494cd271f0c1bc3f454f45.
Evidence: MANUAL, with the named nonproperness theorem below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; different-model review required.

## Statement and exact scope

Work over C. Let j,k>0, j!=k, N=j+k. Fix degree-N homogeneous binary
forms F0,U,V, with U,V linearly independent. Set H(p,q)=F0+pU+qV and

    X = {(p,q,L,Q): L in Sym^j(C^2), Q in Sym^k(C^2),
                    LQ=H(p,q), Res(L,Q)=1}.

Use the usual homogeneous resultant, and let pi:X->A2 be (p,q,L,Q)->(p,q).
Then every irreducible component Z of X which is isomorphic to the
ENTIRE affine plane maps isomorphically to A2 under pi. In particular
no such component yields a polynomial Keller map of generic degree>1.

All degrees j!=k and all affine two-planes of coefficients are covered.
This is not an assertion about nonlinear target surfaces, arbitrary
polynomial maps from A2 into X which are not component isomorphisms,
other resultant constructions, equal degrees, or arbitrary Keller maps.
It is NOT a proof of JC2. There really can be degree-one A2 components;
see the control below. No dimension-three source is ruled out.

## Dependencies, priority and nearest history

The only non-elementary plane-map input used here is the known theorem
that each irreducible nonproperness curve of a generically finite
polynomial map A2->A2 admits a nonconstant polynomial parametrization.
It is recorded as Theorem 1.2, with Definitions 2.1 and 2.3, in
[Jelonek--Lason, arXiv:1411.5011v2](https://arxiv.org/pdf/1411.5011v2).
The selected primary statements were read September 16. The source
uses C-uniruledness, not merely rational parametrizability; that
distinction is essential here. We also use standard finite-cover
monodromy, existence of affine finite-group quotients, Euler-characteristic
multiplicativity for finite unramified covers, and simple connectedness
of C^2. The needed characteristic-zero plane duality is recalled below.

Prior construction-level results must not be confused with this claim:

- [Fixed high-coefficient marked-root slices](marked-root-fixed-coefficient-slices-swarmHQ-root-20260915T124800Z.md)
  fix all high coefficients and use their specified source presentation.
- [Literal cubic affine target sections](affine-target-plane-sections-swarmHQ-root-20260915T235600Z.md)
  treat one specified cubic triple, not arbitrary binary-form degrees.
- [Quintic partition target-field obstruction](quintic-partition-target-field-swarmHQ-root-20260916T032000Z.md)
  is about its marked projective moduli chart. An affine coefficient
  plane is not that chart.
- [nasqret's plane-descent obstruction](https://github.com/nasqret/jacobian-counterexample/blob/main/knowledge/plane-descent-obstructions.md)
  treats arbitrary affine binary-form planes in the fixed source-root
  chart w=y+1/x, using a Wronskian and rational-square obstruction.
  It does not assert the componentwise statement in arbitrary source
  coordinates or for arbitrary positive factor degrees.
- [Pitchford's degree-difference manuscript](https://github.com/ipitchford/degree-difference-affine-slices/blob/main/paper.tex)
  already records the residual scaling torsor and whole-slice Euler
  obstructions. Its selected statements were read, not its whole proof
  audited. It labels itself an unrefereed candidate. The scaling count
  below is known, not claimed as new. A whole-union Euler count alone
  would not exclude an A2 COMPONENT.
- [Ross's uniqueness analysis](https://michaelmross.github.io/jacobian/uniqueness.html)
  covers its higher-dimensional linear-factor construction. Its stated
  dimension range does not supply the present plane argument.

The changed mechanism is the dual discriminant together with off-block
ordered-root incidence. No earlier unpromoted campaign report is a
proof premise. These comparisons are a targeted priority check, not a
claim of exhaustive novelty or a broad literature sweep.

## 1. The actual source is etale

At any point with Res(L,Q)=1 the factors are coprime. The differential
of multiplication is

    (dL,dQ) |-> Q*dL+L*dQ.

Its kernel consists exactly of (cL,-cQ): divisibility by L and Q,
and their fixed degrees, prove this. Its domain has dimension N+2,
so the map is onto the N+1 dimensional space of product coefficients.
Along this kernel the resultant derivative is (k-j)c, by its separate
homogeneities k and j. It is nonzero for c!=0.

Thus the multiplication-plus-resultant differential is an isomorphism.
Its inverse image of the affine plane H(p,q), with resultant fixed to1,
is etale over that plane. X is a smooth affine surface, its irreducible
components are disjoint, and each nonempty component dominates A2
(etale maps are open). We never substitute a normalization of another
source for X.

## 2. Product planes through zero

If F0 lies in the span of U,V, translate (p,q) so that H=pU+qV.
The action

    t.(L,Q,p,q) = (t^j L, t^(-k) Q, t^(j-k) p, t^(j-k) q)

preserves X. A connected algebraic group preserves each of its finitely
many irreducible components. Choose a prime ell>j+k. The subgroup mu_ell
acts freely: a nontrivial element cannot fix the nonzero vector L,
since its multiplier t^j is not1.

For any component Z, the affine quotient Z/mu_ell exists and the
quotient map is a finite etale cover of degree ell. Hence

    chi_c(Z)=ell*chi_c(Z/mu_ell).

Complex algebraic varieties have integral compactly-supported Euler
characteristic; multiplicativity here follows from a finite compatible
triangulation of a finite covering. This is incompatible with Z=A2,
whose Euler characteristic is1. This elementary finite-subgroup argument
does not require a theorem linearizing a Gm action or a projectivity
assumption on Z.

We can therefore assume F0,U,V are linearly independent.

## 3. Remove fixed roots, without changing the source ring

Let G=gcd(F0,U,V), chosen as a fixed binary form, and write
F0=G*f0, U=G*u, V=G*v. The reduced forms have the same degree n,
have no common projective zero, and remain linearly independent.
In particular n>=2. This reduction is on the PRODUCT, not an assertion
that the original resultant constraint becomes a new normalized one.

At a fixed root of G, all its multiplicity must belong to L or all
to Q, since these are coprime. On an irreducible component that allocation
is constant: the alternatives L(a)=0 and Q(a)=0 are disjoint closed
sets covering the component. Generic fixed multiplicities therefore
give constant forms G_L,G_Q with G_L*G_Q=G and

    L=G_L*A, Q=G_Q*B, A*B=f0+p*u+q*v.

Divisibility by these constant forms, first valid on a dense open set,
holds identically by the coefficient equations. Division by a fixed
form is linear on its coefficient subspace. Thus the coefficients of
A,B generate the SAME component coordinate ring as those of L,Q,
together with p,q; and p,q themselves are linear functions of the
coefficients of A*B minus f0 because u,v are independent.

Let a=deg A, b=deg B, so a+b=n. We retain the ORIGINAL j!=k and
the ORIGINAL resultant equation throughout. Reduced degrees a,b may
be equal, and one may be zero.

Suppose now that Z is isomorphic to A2. If a=0, then A is an everywhere
nonzero regular function on Z, since L never vanishes. It is a constant
unit. All coefficients of B=(f0+p*u+q*v)/A are affine-linear in p,q.
Consequently O(Z)=C[p,q], and pi is an isomorphism. The case b=0 is
identical. The remaining argument assumes a,b>0.

## 4. Common-zero directions imply finiteness

Suppose u,v have a common projective zero xi. Then f0(xi)!=0, because
the reduced triple has no common zero. Evaluation gives on Z

    A(xi)*B(xi)=f0(xi)!=0.

If Z=A2, both factors are units in its polynomial ring, hence nonzero
constants. Choose xi as the point at infinity on the root line. The
dehomogenized A,B then have constant nonzero leading coefficients.
Divide by them to make both polynomials monic. Their product is monic
and has coefficients in C[p,q]. Every root is integral over C[p,q];
therefore the elementary symmetric functions giving all factor
coefficients are integral as well. The ring-generation observation in
section3 now makes O(Z) finite over C[p,q].

Thus pi|Z is finite and etale. Its image is closed and open, hence all
of A2. A connected finite etale cover of complex A2 has degree1 by
simple connectedness of C^2, and is an isomorphism. There is no
assumption here that reduced degrees a,b are unequal.

## 5. The basepoint-free directions and their dual curve

It remains to suppose u,v have NO common projective zero. Define

    phi:P1 -> C subset P2, t |-> [u(t):v(t):f0(t)].

Its image is a projective irreducible nonlinear curve: a line containing
it would give a linear relation among the three forms. It avoids
O=[0:0:1]. Write d=deg C>=2 and e=deg(P1->normalization(C)); then n=ed.
For generic (p,q), the line pX+qY+Z=0 cuts C in d distinct smooth
points, each with e distinct preimages. These define d BLOCKS of roots.

Let D be the affine part (dual coordinates [p:q:1]) of C's dual curve.
It is a nonempty irreducible nonlinear curve. Generic points of D
correspond to a line simply tangent at one smooth point of C and
transverse elsewhere. The tangent point and the other intersection
points can avoid the finite branch/singular images and fixed roots.

For clarity, the characteristic-zero duality facts used here can be
seen on a local lift r of a smooth curve. Its tangent line is h=r cross r'.
Differentiating h.r=h.r'=0 shows that r is the tangent-line point of
the dual whenever h and h' are independent. They are generically
independent unless h is constant, which would make C a line.
Thus biduality recovers r from the tangent to the dual. The Gauss map
is generically one-to-one: at a smooth dual point this recovered r is
unique. In characteristic zero the nonconstant Gauss map has nonzero
generic differential, excluding generic flexes. These give ordinary
generic contact and exclude generic bitangency. Finite exceptional
sets can be removed. The cover P1->normalization(C) is generically
unramified. Therefore inertia about generic D is a product tau of e
disjoint transpositions, pairing the two colliding root blocks.

Additional discriminant components from branch points of phi may
exist; they are not identified with or silently discarded from D.

### 5a. D is not polynomially parametrizable

If (p(s),q(s)) were a nonconstant polynomial map into D, its image
would be dense. By an affine target-coordinate change, cancel common
top degree terms until deg p=m>deg q=r>=1. If this ended with q
constant, the image would be a line, which D is not.

The tangent-line map of D has projective coordinates

    [q'(s) : -p'(s) : p'(s)q(s)-q'(s)p(s)].

The last coordinate has degree m+r-1 with nonzero leading coefficient
(m-r)*lead(p)*lead(q), strictly greater than the other two degrees.
At s=infinity this map therefore takes the value O=[0:0:1]. Removing
any common polynomial factor does not alter that limit. By biduality
the image closure is C, contradicting O not in C. Affine changes of
(p,q) preserve the dual point O. Birationality of the polynomial
parametrization was not assumed.

### 5b. Every component, not merely the union, escapes over D

Remove from the parameter plane all singular or non-squarefree reduced
fibers and all fibers where a reduced root meets a fixed root of G.
Call the resulting dense open set T. Over T, roots form a finite
unramified cover. For any fixed allocation of G, factorizations choose
an a-element subset of the n moving roots. For each such partition,
all original factors differ by (L,Q)->(cL,c^(-1)Q), and their resultant
changes by c^(k-j). Thus there are |k-j| choices making it1.
This defines a finite etale cover over T: locally trivialize the
projective factor lines, then the scaling satisfies a nonzero-unit
power equation. Root partitions and the possible residual scalings
are both retained. Components correspond to monodromy orbits of these
enhanced choices. Projecting an orbit gives a root-partition orbit.

Let M be root monodromy over T. Ordered root pairs with different
images on C satisfy the equations

    f0(t_i)+p*u(t_i)+q*v(t_i)=0, i=1,2.

Put Delta=u(t1)v(t2)-u(t2)v(t1). If Delta!=0 they determine p,q
uniquely. If Delta=0 and phi(t1)!=phi(t2), there is NO solution:
the nonzero pairs (u,v) are proportional, but the full triples are not.
So off-block ordered-pair incidence is precisely an open graph over
P1 x P1. Restricting to T leaves a nonempty irreducible open set;
it dominates T because a general line meets nonlinear C in d>=2
distinct points. Hence M is transitive on ordered off-block pairs.

Let K be the normal subgroup of M generated by the conjugates of tau.
Choose one swapped pair of tau. Conjugation and off-block transitivity
show that K contains an element sending any root r to any root s in
a different block. With at least two blocks this makes K transitive
on all roots, including those in the same block via an intermediate
root in another block. Every nonempty proper root subset therefore
fails to be invariant under some conjugate of tau.

In particular, every component's partition orbit contains a partition
which is moved by tau at a generic main-D collision. Such a partition
splits at least one colliding pair between A and B. Every lift to the
enhanced scaling cover then escapes as the parameter tends to that
point of D. Indeed, if L,Q stayed bounded along a subsequence, their
limits would be nonzero (their product tends to the nonzero H at this
generic point). The limiting projective factors would share the split
root, giving Res(L,Q)=0 by continuity, contrary to Res=1.
The collision was chosen away from the fixed roots; their allocations
and extra excluded target lines do not change this argument.

Thus the nonproperness set of pi on EACH individual component contains
a dense open part of D, hence D. The finite cover over T also ensures
that this nonproperness set is contained in the curve complement of T.
So D is an irreducible component of the nonproperness set, not just
a curve in an uncontrolled higher-dimensional bad locus.

If Z=A2, the polynomial nonproperness theorem gives a nonconstant
polynomial parametrization of D. Section5a contradicts it. Therefore
the basepoint-free case with a,b>0 has no component isomorphic to A2.
Together with sections2--4 this proves the stated degree-one conclusion.

## Replay, controls and failure modes

Desk-only; no CAS, numerical evidence, degree scan or scientific Python.
The proof treats arbitrary fixed degrees, including composite phi and
unequal original degrees whose reduced degrees become equal. Manual
ROOT synthesis and native same-model audit are not different-model FIRST.
FALLACY-v2 SHA256:
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
No new exit-price assertion; charge_basis is inapplicable.

1. Degree-one positive control: j=1,k=2 and
   H=T*S^2+p*T^2*S+q*T^3. The factorization L=T,
   Q=S^2+p*T*S+q*T^2 has resultant1. It is an entire A2
   component by etaleness and its closed graph, mapping identically to
   (p,q). Removing fixed G=T leaves a=0; an assertion excluding ALL
   A2 components would be false.
2. Distinct discriminant components: H=p*T^3+T^2*S+q*S^3 has
   basepoint-free directions T^3,S^3. Its discriminant is
   -q*(4+27*p^2*q). The main dual component is 4+27*p^2*q=0;
   q=0 is an extra branch-image line. The main curve has no
   nonconstant polynomial parametrization, since p^2*q is a nonzero
   constant in C[s], making both p and q constant. This checks the
   need to distinguish the main component from an extra line.
3. Residual scaling alone does NOT exclude an individual component;
   neither does a whole-union Euler count. Section5b supplies the
   missing quantifier rather than assuming transitive partition action.
4. For j=k the resultant derivative on the multiplication kernel
   vanishes and the residual scaling is not finite. That case is
   deliberately outside the statement.
5. A rational parametrization of D would not suffice for contradiction.
   The polynomial conclusion of the named source theorem is essential.

## Limitations and next test

This closes a specified complete-source construction architecture only
if the proof survives hostile review. The next test is one different-model
manual review of this frozen report, emphasizing gcd allocation, monic
integrality, generic tangency with composite phi, componentwise inertia,
and the polynomial/nonpolynomial distinction. Estimated 20 minutes;
no paid computation or descendants are justified before that gate.
No claim is made that arbitrary prospective Keller maps admit this
factorization presentation or an affine coefficient-plane target.

## OPENS RAISED

None. The exact statement awaits independent review; this report introduces
no successor family or unbounded program based on its provisional proof.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

This administrative output does not certify novelty. The mathematical
comparison with the nearest prior mechanisms is above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17400`.
- Body SHA-256:
  `f5f7b9413aa62ce5fe74d1e11ed0a9b9f0df32fec93effe1382fd65717978613`.
- Frozen basis: `5e9791860e1515640a494cd271f0c1bc3f454f45`.
