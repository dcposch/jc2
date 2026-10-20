# Pole-free zero support of a field-generating rational Darboux form

STATUS: UNPROMOTED / manual ROOT producer; independent FIRST required.
OWNER: swarmHQ-root. Frozen basis: 782c5584145043d4f37991571cabd4af00bbe5a0.
Scope: birational two-forms on complex surfaces, not a JC2 proof.

## 1. Statement

Let S be a smooth projective complex surface, omega a nonzero rational
two-form, and U the open locus where omega is regular (zeros are allowed).
Suppose C(S)=C(u,v) and omega=c du wedge dv, with c in C*.
Then the reduced positive zero divisor of omega restricted to U is a
simple-normal-crossings divisor: its irreducible components are smooth,
at most two pass through any point, and any two meet transversely.
In particular, cusps, self-nodes, tangencies and triple points of the reduced
positive zero support cannot occur at a pole-free point.

Multiplicities are not asserted to be one. This is an obstruction on the
SAME function field. Exactness or a generically finite Darboux pair without
field generation does not suffice. Nothing is asserted at points on poles.

## 2. Zero-free-model descent with zeros permitted on the source

We use the following lemma. Let Y be another smooth projective complex
surface, eta a nonzero rational two-form with div_Y(eta)<=0, and
r:S--->Y a birational map. If omega=r*eta is regular on U, then r is a
morphism U->Y, though not necessarily a morphism into an affine chart.

Proof. Resolve r by point blowups pi:W->S, with h:W->Y a birational
morphism. Fix p in U. Every pi-exceptional curve above p has strictly
positive order in pi*omega. For the first blowup this is
1+mult_p(a), where omega=a ds wedge dt in regular local coordinates.
The coefficient a is regular, including when a(p)=0. Further pullbacks
remain regular above p and every new exceptional order is again at least1.

If such an exceptional curve were not h-contracted, its generic valuation
would coincide with a prime-divisor valuation on Y. Its differential order
would be at most0, because div_Y(eta)<=0. This contradicts
pi*omega=h*eta. Hence all curves in pi^-1(p) are h-contracted.
The fiber is connected; consequently its image under h is a single point.

Let Gamma be the reduced closure of the graph of r in S x Y.
The proper map W->Gamma is surjective. Thus the fiber of Gamma->S at p is
a singleton. This proper birational projection is quasi-finite over a
neighborhood of p, hence finite there; finite birationality over the
normal surface S makes it an isomorphism there. This proves the lemma.
If pi is already an isomorphism above p, no descent step is needed.

This is the same descent argument used in the accepted
[zero-free-model FIRST](zero-free-branch-model-review-swarmHQ-sol-20260917T044800Z.md),
lines17--19, with the explicit observation that source nonvanishing is
unnecessary for positivity of exceptional orders. It is not a new
independent mechanism or a re-audit of that accepted obstruction.

## 3. Normal crossings of the positive zero support

Apply the lemma to Y=P2_(u,v), eta=c du wedge dv, whose divisor is
-3L_infinity. Field generation makes r birational. Therefore r is regular
on U. Resolve its remaining indeterminacy with centers outside U; this
gives pi:W->S an isomorphism over U and h:W->P2 a birational morphism.

A positive-order prime of pi*omega cannot dominate a P2 curve: the standard
form has only orders0 and-3 there, and a noncontracted prime preserves the
generic DVR and differential order. Every positive zero component on U
therefore lies in the reduced exceptional divisor of h on W.

A birational morphism between smooth projective surfaces factors into
point blowups. Its reduced exceptional divisor is SNC: start with the
empty exceptional divisor and note that a point blowup preserves SNC
after adding its new exceptional curve. Its components are smooth.
A reduced subdivisor of an SNC divisor is SNC. Restricting to pi^-1(U),
which is identified with U, proves section1.

Imports: characteristic-zero surface resolution, resolution of a rational
map away from its domain of definition, connected fibers for a sequence
of point blowups, point-blowup factorization of smooth-surface birational
morphisms, and proper-quasi-finite/finite-birational descent over a normal
base. These are the same classical surface/descent imports used in the
accepted zero-free-model and CYCLE arguments; no new external source is used.

## 4. Conditional finite-cover consequence

Let pi:X->Y be a finite dominant map of normal projective complex surfaces.
Let x and y=pi(x) be smooth points, and let eta be a rational two-form on Y
regular and nowhere zero near y. If the reduced ramification divisor on
the smooth source is NOT SNC at x, there cannot be u,v generating C(X)
with pi*eta=c du wedge dv for a nonzero constant c.

Indeed pi*eta is regular near x and its positive zero divisor there is the
ramification divisor, with generic coefficient e_E-1 along a ramified
prime E. Resolve X away from this neighborhood and apply section1.
The conclusion survives scalar-constant-Jacobian birational target changes
relative to eta, but NOT arbitrary target area changes or finite source-field
enlargements. No eligible target area form is manufactured by this argument.

## 5. Controls and exact reach

The need for field generation is concrete. Put
F=x and G=y^3/3-x^3*y. Then dF wedge dG=(y^2-x^3) dx wedge dy, whose
positive zero support has a cusp at the origin, although the form is
regular and exact. The extension C(x,y)/C(F,G) has degree3, not1.
This is a NON-KELLER control, not a counterexample candidate.

The conclusion strengthens the accepted
[CYCLE statement](positive-zero-cycle-review-swarmHQ-sol56-root-20261019T101735Z.md)
at pole-free points, including singularities that do not create its
multibranch dual-graph cycle. It does not supply the hypotheses missing
from an actual-normalization proof. In particular, the retained disjoint-A1
boundary picture can already have SNC support. No omitted boundary is
forced to have a cusp, tangency, triple point, or any other violation.
No B=R theorem, JC2 proof/counterexample, arbitrary donor exclusion,
finite-source-extension exclusion, automatic successor or degree bound follows.
External novelty is unknown; the new statement is extracted from an
existing campaign descent argument, not a claim of a novel general method.

OPEN(S) RAISED: None.

## COLLISIONS

status: EMPTY

- NONE -- no explicitly tagged OPEN entries are raised.

Corpus basis: 782c5584145043d4f37991571cabd4af00bbe5a0 (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6556`.
- Body SHA-256:
  `b283c94d9d1737bb4d3a2c09ed39280b44b880d75edabfa960dc7d879dedfd95`.
- Frozen basis: `782c5584145043d4f37991571cabd4af00bbe5a0`.
