# Rational-pencil preservation forces polynomial Keller invertibility

Evidence tier: MANUAL, relative to the explicitly named classical and accepted
campaign imports below. Lifecycle: PRODUCER-CHECKED / PROVISIONAL pending
different-model FIRST. Producer: swarmHQ ROOT (Astra-assigned campaign seat);
same-model independent co-check: native0346 (Astra), not FIRST. Hosted model
identity is not independently attested. Date: September 20, 2026.
Basis: a91c8ad9829fb9417e9650787a185126274e058e.

## 1. Exact statement and scope

**RATIONAL-PENCIL-UNIFICATION-1.** Let F:A2_C -> A2_C be polynomial with
det DF=c in C*, with NO restriction on |c|. Suppose a nonconstant rational
function r in C(x,y) and a rational self-map phi of P1 satisfy
r composed with F = phi composed with r. Then F is an automorphism.

Dominance makes phi nonconstant. Neither primitivity, a polynomial pencil,
absence of affine base points, a prescribed generic genus, nor degree one
on the base is assumed. The conclusion applies also if a positive iterate
of F has such a pencil: an invertible iterate makes F invertible.

This supplies NO pencil for an arbitrary hypothetical counterexample,
NO global JC2 proof and NO counterexample. It does not assert that every
polynomial automorphism preserves a pencil. The genuinely new interfaces
are elimination of periodic affine base points, extension of the accepted
genus-zero argument to base-point-free rational morphisms, and elementary
polynomialization of a primitive dependent numerator-denominator pair.

The combination removes DNT's dynamical-degree/modulus dependency, the
earlier closed-polynomial-generator import, and the exact-area rational-map
theorem from this conditional conclusion. It retains the accepted general
hyperbolic moving-pencil theorem and the stated geometric imports.
No literature-novelty claim is made.

## 2. Inputs, dependencies and comparison

Frozen terminal inputs, paths relative to this repository:

- `xmodel/homogeneous-pencil-composition-swarmHQ-root-20260919T175300Z.md`,
  SHA256 45c5c50e94a73272b5b5ad6c387035d1defc9553c7dcb825ead2b85e8db9a854;
  binding integration
  `xmodel/homogeneous-pencil-first-integration-swarmHQ-root-20260919T181000Z.md`,
  SHA256 16060675d9b95f2a1cc106bc4bf376140f4b1b859e1e5c96571a12210d6fca01.
  Use only its elementary lift and field-degree cancellation, valid for all c.
- `xmodel/rational-polynomial-pencil-swarmHQ-root-20260920T011100Z.md`,
  SHA256 f06a1d0c931f1e7270f6b63132dbfd5b01588928e0f9e5e2ee8f115665367e88;
  binding integration
  `xmodel/rational-pencil-first-integration-swarmHQ-root-20260920T013400Z.md`,
  SHA256 4fc8f4f6a2d978a2335bcd75e8a21297f78ac089c17e055bd31f81fd03dda382.
  Genus-zero primitive POLYNOMIAL pencils, all nonzero constant c.
- `xmodel/hyperbolic-moving-pencil-swarmHQ-root-20260919T203700Z.md`,
  SHA256 bcb4e3c3851f50db05654c9acfcba11131d55df4f29302a28cf89dceeb42370a;
  binding integration
  `xmodel/hyperbolic-pencil-first-integration-swarmHQ-root-20260919T205600Z.md`,
  SHA256 6c1be9fd3a3f81baa73cbfae5a6e426e25434f55d09cb04815440130e3c790a5.
  Use ONLY its conclusion for general dominant polynomial maps: a primitive
  polynomial pencil of positive affine Euler defect, with base degree d>=2,
  gives N=d and a nonconstant rational invariant for F ITSELF. Its exact-J=1
  corollary is NOT used. The pointed-moduli/finite-automorphism descent in
  that theorem remains an inherited dependency, not reproved here.

Classical imports: resolution of surface pencils; Stein factorization;
H1(O)=0 for a smooth projective rational surface; generic smoothness and
geometric integrality for a relatively closed base field in characteristic
zero; Riemann--Hurwitz for smooth complete curves; descent of finiteness;
Serre duality, adjunction, and dimension-one coherent cohomology;
birational Keller implies automorphism, and finite etale A2 covers are trivial.

Nonproper-value imports retain the previous statement-level source scope:
Nguyen Van Chau, arXiv:0905.3939v3, March 17, 2010,
<https://arxiv.org/pdf/0905.3939v3>, Section 2(i) and Theorem 4 (printed p.3):
nonproper components of a generically finite polynomial plane map admit
nonconstant polynomial parametrizations, and for a constant-nonzero-Jacobian
map none is abstractly A1. The prior report checked these statements;
this report makes no new proof audit of the imported theorems.

Both frozen public history and the pre-admission HQ journal were searched
for the periodic-base-point/order mechanism before admission. The nearest
accepted homogeneous proof allowed affine base points but did not eliminate
them. Earlier all-pencil synthesis applied only to exact J=1 with additional
imports. Bounded history search is not an exhaustive novelty certificate.

## 3. Primitive replacement

Put L=C(x,y). Resolve r on P2 to obtain a morphism from a smooth projective
rational surface X to P1 and take Stein factorization X -> C -> P1.
The intermediate curve C is smooth projective and its function field K is
the relative algebraic closure of C(r) in L. Since pi_*O_X=O_C, the low-degree
Leray sequence injects H1(C,O_C) into H1(X,O_X)=0. Thus C has genus zero and
is P1 over C. Write K=C(h), r=R(h), with R a nonconstant rational function.

Apply the injective F* to an algebraic equation for h over C(r).
Because F*r=phi(r), F*h is algebraic over C(phi(r)), hence over C(r).
Relative closure gives hF=psi(h) for a rational psi. From
R psi=phi R and degrees of nonconstant P1 maps, deg psi=deg phi=:d.

The resolved geometric generic h-fiber is smooth and integral. We do NOT
assert this for the full affine equation a-tb before affine base points
are removed. Every use of full smooth affine fibers below follows either
base-freeness or polynomialization. Write h=a/b in reduced form in C[x,y].

## 4. Independent pair: lift, degree and removal of base points

Assume a,b algebraically independent. Write psi=[A:B], where A,B are
coprime homogeneous binary forms of common degree d. Their common zero
in A2 is only the origin; G=(A,B) is finite of generic degree d^2.

The pair (aF,bF) is coprime: a common divisor would map under the etale,
quasifinite F into the finite set V(a,b). The pair (A(a,b),B(a,b)) is also
coprime: its common-zero set is contained in V(a,b). Equality of rational
functions therefore gives a COMMON constant unit u with

    (a,b) composed with F = u (A(a,b),B(a,b)) =: G0 composed with (a,b).

Both components must use the same unit. With H=(a,b) dominant generically
finite, cancellation of generic degrees in HF=G0H gives

    N(F)=d^2.                                             (4.1)

This requires quasifiniteness in the coprimality step, not mere dominance,
and it holds for every c in C*. If d=1, N=1 and F is an automorphism.

If d>1, let Z=V(a,b), a finite set. Since G0(0)=0, F(Z) is contained in Z.
If Z is nonempty, some z in it is periodic, say F^k(z)=z. In the regular
local ring at z let ell=min(ord_z a,ord_z b)>0. The etale local iterate
F^k has invertible linear term and preserves order (equivalently it gives
an automorphism of the completed local ring). Consequently

    min(ord_z(a composed with F^k),ord_z(b composed with F^k)) = ell.

But G0^k is homogeneous of degree d^k, so HF^k=G0^kH has both components
in m_z^(d^k ell). This says ell>=d^k ell, impossible. Hence Z is EMPTY,
and h=[a:b]:A2 -> P1 is a morphism on the unchanged affine plane.

## 5. Dependent pair: polynomialization without a generator theorem

Assume a,b algebraically dependent. Their field C(a,b) has transcendence
degree one and is algebraic over C(h). Relative closure therefore implies
a,b in C(h).

Let Gamma be the irreducible affine curve closure of the image of
H=(a,b). Any nonempty fiber of A2 -> Gamma has dimension at least one.
The fiber H^-1(0,0)=V(a,b), however, is finite or empty by coprimality.
It must be empty. Thus h is again a morphism to P1.
Equivalently, normality lifts H to the normalization of Gamma; a local
parameter at an attained point of that smooth curve cuts a divisor in
A2. This also verifies the assertion when Gamma itself is singular.

At least one of a,b is a nonconstant rational function q(h). It has a pole
at some v in P1. If h^-1(v) were nonempty, that fiber would contain a
divisor: a nonempty fiber of a dominant morphism from a smooth surface
to a smooth curve is locally a nonzero nonunit principal equation.
The pullback of q's pole has negative valuation there, contradicting
regularity of q(h). Hence h omits v.

A Mobius transformation taking v to infinity gives a globally regular
function p on A2, so p is polynomial and C(p)=C(h). The identity for h
becomes pF=chi(p) with chi rational and deg chi=d. In fact chi is polynomial:

    C(p) intersect C[x,y] = C[p].                         (5.1)

To see this, write chi=U/V in reduced univariate form. Bezout makes
U(p),V(p) comaximal. If their quotient is polynomial, V(p) is a unit in
C[x,y], hence constant. Nonconstant p then forces V constant. The same
argument proves (5.1). The polynomial p is primitive because C(p)=K is
relatively algebraically closed in L.

## 6. Full-fiber degree comparison

Let h now be ANY primitive morphism A2 -> P1 preserved with base degree d,
and let g,n be the genus and number of punctures of its full smooth
geometric generic fiber. In particular n>=1, since that positive-dimensional
curve is closed in an affine surface and cannot be complete.

After algebraic closure of the target generic base field, the source
splits into the d distinct full fibers over psi(s)=t. Each has the same
g,n as the target; these are embeddings of the generic pencil, not an
assumption that arbitrary fibers are pointed-isomorphic. F restricts to
dominant etale maps of smooth affine curves. The degrees are equal, say k,
and function-field towers give

    N=d k.                                               (6.1)

More explicitly, put K=C(h), K0=C(psi(h)) and sigma=F*. The extension
sigma(L)/K0 is regular, so it is linearly disjoint from K/K0. Thus
[sigma(L)K:sigma(L)]=d and k=[L:sigma(L)K]=N/d. Equality of the component
degrees also follows from conjugacy of the d base embeddings. Complete
each curve smoothly. For an extended map of degree k,
Riemann--Hurwitz and the fact that every inverse image of a target puncture
is a source puncture give

    2g-2+n >= k(2g-2+n).                                 (6.2)

One can see the inequality by writing total ramification as the contribution
over target punctures plus remaining nonnegative ramification. It allows
source punctures over interior points; it does not assume properness.
If delta=2g-2+n>0, k=1; equal puncture counts then imply the map of full
affine fibers is an isomorphism, not a proper open subset inclusion.

If g=0,n=1, the curves are A1 and a nonconstant morphism is a finite
polynomial map. If g=0,n=2, the curves are Gm and such a morphism is
z -> alpha z^m with m a nonzero integer, also finite. For g=0,n>=3,
(6.2) gives k=1 and the preceding full-fiber isomorphism. Thus in ALL
genus-zero cases F is finite over the geometric generic BASE, a stronger
statement than merely having a finite extension of function fields.

## 7. Genus-zero morphism lemma: chart spreading and properness

**Lemma.** If a polynomial Keller F preserves a primitive morphism
h:A2 -> P1 whose generic genus is zero, then F is an automorphism.

Write h=[a:b] with no common zero, and use target base chart t=a/b.
Its inverse image is V=D(b), with coordinate ring C[x,y,1/b]. The actual
source over V is F^-1(V)=D(b composed with F), NOT D(b). The generic-base
restriction is finite by Section 6 and descent of finiteness from an
algebraic closure of C(t). Because h is globally a morphism, each source
component here is the FULL fiber h=s, psi(s)=t: its points cannot disappear
by a hidden affine base point or by incorrectly inverting b on the source.

This map of affine coordinate rings is finitely generated. Over C(t),
choose monic equations for a finite generating set of the source algebra
over the target algebra. Clear their finitely many BASE denominators in
C[t]. The identities themselves can also be cleared of their finitely
many base denominators; equivalently use the domain embeddings into the
generic localizations. After inverting a single nonzero q(t), those
generators are integral. Thus F is finite over h^-1(U) for a nonempty
open U contained in P1. This is not a deduction from field degree alone.

The nonproper-value set A_F is therefore contained in finitely many
fibers of h. If nonempty it is a curve, and every irreducible component
is an entire irreducible component of one of these fibers.

Resolve h:P2 --> P1 ONLY at infinity, obtaining a smooth projective
rational surface X with a morphism f:X -> P1 that retains the original
A2 unchanged. A general fiber G is a smooth P1. It is nef, G^2=0, and
K_X.G=-2. For any scheme fiber D, D is linearly equivalent to G. If
K_X+D had a nonzero section, its effective divisor would have negative
intersection -2 with the nef G, impossible. Serre duality gives
H2(X,O_X(-D))=0. The exact sequence for D and H1(X,O_X)=0 give
H1(D,O_D)=0.

For each reduced irreducible component C of D, O_D surjects onto O_C;
the kernel has dimension-one support, so its H2 vanishes. Hence
H1(C,O_C)=0. An integral projective curve of arithmetic genus zero is
smooth P1. This argument ALLOWS reducible and nonreduced fibers; it does
not claim every whole special fiber is smooth.

It follows that each component of A_F is a smooth affine rational curve.
By the stated nonproper-value import it has a nonconstant polynomial
parametrization A1 -> C. A smooth affine rational curve is P1 with a
nonempty finite set removed; such a parametrization forces exactly one
puncture (extend to a finite map of P1 and use surjectivity). Thus it is
abstractly A1, contradicting the Keller no-A1-component theorem. Therefore
A_F is empty, F is finite etale and consequently an automorphism. QED.

## 8. Degree-one-base lemma, proved before using new invariants

Suppose an arbitrary rational pencil is preserved with d=1. Replace it
primitively as in Section 3; the new base degree is still one. If its
reduced numerator and denominator are independent, (4.1) gives N=1.
If dependent, Section 5 produces a primitive polynomial pencil p.
For genus zero use the accepted polynomial theorem (or Section 7);
for positive genus delta=2g-2+n>0, so (6.1)--(6.2) with d=1 give N=k=1.
In every case F is an automorphism. This holds for every c in C*.

In particular ANY nonconstant fixed rational invariant implies automorphy.
Primitive replacement of a fixed invariant need not give identity on the
new base, but its degree remains one, which is all this lemma requires.
This proof uses neither the hyperbolic invariant-production theorem nor
the exact-area rational-map theorem, so Section 9 is not circular.

## 9. Finish the theorem

Normalize r as in Section 3 and split by dependence of its reduced a,b.

If independent, d=1 is already done. For d>1 Section 4 removes all affine
base points. If g=0, Section 7 gives automorphy. If g>=1, delta>0 and
(6.1)--(6.2) give N=d. This contradicts N=d^2 for d>1.

If dependent, Section 5 gives a primitive polynomial p with pF=chi(p),
deg chi=d. Genus zero is covered by the accepted polynomial theorem.
For positive genus, d=1 is Section 8. For d>=2, invoke ONLY the accepted
general-dominant-map conclusion of HYPERBOLIC-MOVING-PENCIL-1: F has a
nonconstant fixed rational invariant. Apply Section 8 to it. No exact-J=1
corollary, modulus estimate, or closed-generator theorem enters. QED.

## 10. Checks, limitations and review targets

Manual positive check: F=(alpha x,beta y), alpha,beta nonzero, preserves
h=x/y with d=1 and satisfies the conclusion for arbitrary c=alpha beta.
Polynomial triangular automorphisms preserving x satisfy the dependent case.

Negative checks from existing evidence, no new control family:

- F=(x^2,y^2), h=x/y has N=4,d=2 and the periodic base point (0,0).
  Its local iterate is NOT etale, so ideal order is not preserved. This
  exhibits exactly the missing hypothesis of Section 4, not a contradiction.
- T=(x^2 y,x y^2), h=x/y has d=1,N=3. T is not quasifinite: the axes
  contract, and the common factor in the pulled-back numerator/denominator
  defeats the lift step. Mere dominance cannot replace the Keller condition.
- F=(x,xy), h=x gives finite generic full-fiber maps and vertical nonproper
  set, but its nonconstant Jacobian permits an A1 nonproper component.
  The Keller endpoint in Section 7 is indispensable.

No CAS, prime search, worker computation, or new source acquisition was
used. All ring maps/localizations are explicit in Sections 4--7. This is
not a new exit-price claim and makes no charge_basis declaration.

Highest-priority FIRST interfaces: primitive replacement; homogeneous
degree cancellation at arbitrary c; periodic ideal-order contradiction;
dependent-pair omitted-value argument; full source fibers in D(bF);
generic-base rather than field-level finiteness; cohomology of scheme
fibers; degree-one lemma before consuming the general hyperbolic theorem.

The global missing premise is STILL existence of a preserved rational
pencil for an arbitrary hypothetical noninvertible Keller map, or some
different global closing argument. No bounded experiment in this report
establishes that premise, and no automatic classification successor follows.

ROOT's full draft was completed at03:37:52 before collection of the peer's
full composition. The peer's earlier partial supplied the smoothness and
D(bF) cautions now incorporated above. Native0346 completed at03:39:11;
its whole final and authoritative completed status were collected before
this report's author completion. All six interfaces were confirmed at the
stated imported scope. The peer's normalization argument is additionally
included in Section 5. This same-model co-check is NOT different-model
FIRST; it performed no new primary-source or imported-proof audit.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author completion: 2026-09-20 03:41:46 UTC; whole-body readback and changed
passages checked, collision check EMPTY, terminal native co-check collected.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18269`.
- Body SHA-256:
  `b98f59860386d58a1adeff9b6ca8aea14adc170d748b831a665c2a860c3e3393`.
- Frozen basis: `a91c8ad9829fb9417e9650787a185126274e058e`.
