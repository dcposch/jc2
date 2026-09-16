# The quintic 2+3 partition chart has no polynomial target invariants

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra co-research.
Date: September16,2026 UTC.
Basis: 4069f525c6a7475d8ae2d815949ea17777ec9380.
Evidence: MANUAL with the named classical GIT import below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; different-model review required.

## Statement and construction scope

Let Y be the projective coarse moduli space of complex binary quintics
whose roots have multiplicity at most two, modulo projective changes of
variable and scalar. Consider a quintic together with a marked unordered
pair of distinct SIMPLE roots. Equivalently, factor it as a quadratic
with distinct roots times a cubic, with nonzero resultant, and retain
the partition rather than an ordering within either factor.

Its coarse parameter space is

    U = A2_(r,s) minus {(9,54)}.

Forgetting the partition gives a dominant quasi-finite morphism
q:U->Y of generic degree10. Its image is Y minus the single orbit y_* of
quintics with multiplicity pattern (2,2,1). For the literal field inclusion

    q*: K=C(Y) -> L=C(r,s),

one has

    q*(K) intersect C[r,s] = C.                         (1)

Consequently NO nonconstant rational target function becomes a polynomial
on this full source chart. In particular, no rational target
postcomposition produces a dominant polynomial plane map, let alone a
Keller counterexample. This covers all rational target functions, not
just a selected invariant pair. Polynomial coordinate automorphisms of
the fixed source do not change (1).

This is a construction filter for this one literal partition chart.
It does not cover arbitrary rational or finite source substitutions,
different markings, other root counts, or other affine models of L.
No etaleness assertion about the coarse quotient is made. JC2 remains open.

## Dependency and prior scope

The classical target identification used here is
Y=P(1,2,3), a normal projective integral surface, with geometric points
the indicated stable quintic orbits. Stable equals semistable and means
multiplicity at most two. See Hassett--Kresch--Tschinkel,
[On the moduli of degree 4 Del Pezzo surfaces](https://www.math.brown.edu/bhassett/papers/modulidP4/noheighttwo16.pdf),
Section5, printed9--11; author PDF dated September7,2014. Those selected
pages were read as extracted text, not the whole paper or its arithmetic
results. Only the coarse-space and orbit statements are imported;
stack etaleness is not being transferred to coarse spaces.

The campaign's [fixed-high-coefficient marked-root slices](marked-root-fixed-coefficient-slices-swarmHQ-root-20260915T124800Z.md)
do not cover this projective 2+3 partition quotient. The divisorial-pole
mechanism is standard and overlaps the earlier fixed torus-quotient
target-rigidity test; the different client here has a projective target,
forcing constants rather than merely target regularity. No literature
novelty is claimed. Targeted history found no identical client, not an
exhaustive priority result. No low-degree Keller theorem is needed.

## 1. Exact source quotient

Move the two marked simple roots to 0 and infinity. Write the remaining
cubic as

    H(X,Y)=a X^3+b X^2 Y+c X Y^2+d Y^3,       ad!=0.

The quintic is XYH. The remaining equivalences are scalar multiplication
of H, the diagonal torus, and the interchange X<->Y. Torus weights on
(a,b,c,d) are (3,1,-1,-3). Put

    A=ad, B=bc, C0=ac^3, D0=b^3d, E=C0+D0.

The torus invariant ring is

    C[A,B,C0,D0]/(C0*D0-A*B^3).

For completeness, strip factors ad and bc from any weight-zero monomial.
The remaining nonconstant monomial uses either a,c or b,d, and the weight
equation makes it a power of ac^3 or b^3d. The only relation is the
displayed binomial. Interchange fixes A,B and swaps C0,D0, so its invariant
ring is C[A,B,E]. The ordinary degrees are 2,2,4. On A!=0, quotienting
the scalar grading gives the polynomial ring

    C[r,s],       r=B/A,       s=E/A^2.                  (2)

There is also a direct orbit check. Scale and apply the diagonal torus
to normalize a=d=1. The effective remaining diagonal action is
(b,c)->(zeta b,zeta^(-1)c), zeta^3=1, together with b<->c. Its invariant
ring is C[bc,b^3+c^3]. These are precisely r,s, and a finite-group
quotient separates its orbits. Every pair r,s occurs: b^3,c^3 have sum s
and product r^3, with cube roots chosen so bc=r; the r=0 cases are
included. Thus (2) is the whole coarse chart, not only a function-field
parametrization.

Since a,d are nonzero, neither marked root is a root of H. The product
XYH is stable unless H has a triple root. For H=(alpha X+beta Y)^3,
alpha beta!=0, substitution gives r=9,s=54. Conversely, these two values
give b^3=c^3=27 after a=d=1, and bc=9, hence a triple root. All such
cubics form one residual-group orbit. Therefore the stable source is
exactly the punctured plane U stated above.

## 2. The forgetful map and its exact image

Multiplication of the two factors, followed by the stable quintic
quotient, is invariant under the residual group and descends to q:U->Y.
Equivalently, the homogeneous quintic invariants restrict to invariant
functions in the coefficient chart; the stable condition ensures they
define a morphism to the projective quotient. No choice of roots or
rational section is being declared regular globally.

A stable quintic has one of the multiplicity patterns

    (1,1,1,1,1),       (2,1,1,1),       (2,2,1).

The first two admit two marked simple roots; the last does not. All
quintics of the last pattern are projectively equivalent, because their
three distinct support points can be moved to any prescribed triple.
This proves the exact cofinite image Y minus {y_*}.

Each fiber consists of a finite set of choices of two simple roots,
modulo the automorphism group of that quintic. Thus q is quasi-finite.
A general configuration of five points has no nonidentity projective
automorphism: each of the finitely many nonidentity root permutations
imposes a proper cross-ratio condition. Over this open locus its fiber
has binomial(5,2)=10 points. Characteristic zero makes the corresponding
function-field extension separable, giving generic degree10. Special
stabilizers may identify choices; they do not create positive-dimensional
fibers, and no unramified claim is inferred from this count.

## 3. Divisorial poles prove (1)

Take h in C(Y) such that q*h belongs to C[r,s]. In particular, q*h is
regular on U. For each prime divisor D0 on Y, the image calculation and
quasi-finiteness supply a prime divisor E0 of U dominating D0. Normality
provides discrete valuation rings at their generic points. The morphism
gives

    ord_(E0)(q*h)=e*ord_(D0)(h),       e>0.

Indeed a local uniformizer at D0 has positive order at E0, while a unit
and its inverse remain units there. Regularity upstairs therefore forces
ord_(D0)(h)>=0 for EVERY target prime divisor. Normality extends h over
the finitely many codimension-two points as well. A global regular
function on the integral projective surface Y is constant. This proves
(1). Conversely constants plainly pull back to constants.

Only cofinite coverage, quasi-finiteness, normality and projectivity are
used here; neither a uniform pole-order bound nor properness of q is
assumed. The missing source point cannot conceal a target polar divisor.
Rationality of both fields consequently does not provide polynomial
coordinates for this literal field inclusion.

## Controls and limits

- With normalized cubic H=X^3+Y^3, (r,s)=(0,0) is a valid stable source
  point. With H=(X+Y)^3, (9,54) is the excluded unstable point. Thus a
  genuine codimension-two deletion is retained, not declared absent.
- A quintic with two distinct double roots and one simple root is stable
  but has no eligible marked pair. This checks the target omission.
- The open immersion A2->P2 avoids a DIVISOR, not just a point. Its
  rational coordinates pull back to polynomials; it does not satisfy
  the cofinite-image hypothesis of the pole argument.
- With target A2 rather than a projective surface, the identity map
  admits nonconstant regular target functions. Projectivity is essential
  for the final constant conclusion.
- Arbitrary source substitution is not covered. For example y/x becomes
  the polynomial v under (u,v)->(u,uv), although y/x is not polynomial
  on the original plane. No denominator-cancellation exclusion for
  general source changes follows from (1).

Desk-only: hand invariant-ring, orbit, root-multiplicity and valuation
arguments. No CAS, polynomial search, scientific subprocess, cloud job,
or independently verified numerical experiment. Same-model co-research
is not different-model FIRST. This closes the proposed construction on
its literal chart, not an all-degree proof route or all moduli constructions.
No larger marking/root-count family is selected.

ROOT's proposal and independent native Astra reconstruction agree on
all displayed rings, the exact stable puncture, the cofinite image and
the pole argument. Astra completed its mathematical check at03:22:09UTC;
its full final response and authoritative completion were collected before
ROOT closed this report. This is corroboration, not a second-model review.
The nearest report's whole-read SHA256 was
a56a1de74b34a283e1c4f32bc4e316f0da372f4c75a18c60afd1fd96589333e5;
FALLACY-v2 was
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
Both remained unchanged before closure.

## OPENS RAISED

None. Independent hostile review is required before promotion.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Canonical scan completed exit0; its lexical result is not a novelty
certificate or an exhaustive mathematical scope comparison.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9788`.
- Body SHA-256:
  `b2753ce061c01614fd09955968d3f9aad8bb009a2ec6807a9e8e616267f33337`.
- Frozen basis: `4069f525c6a7475d8ae2d815949ea17777ec9380`.
