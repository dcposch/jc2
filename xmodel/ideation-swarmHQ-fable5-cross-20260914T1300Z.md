# swarmHQ FULL1300 adversarial cross: Fable5.1

Producer swarmHQ Fable 5.1 (claude-fable-5-1), cross participant, 2026-09-14.
Basis bf1e1ffe30af1bfa123449596fd96064e87d655d. Manual reasoning, inert
reads, apply_patch only. Strategy analysis, not a promotion gate: nothing
below is promoted, no OPEN is raised, no exit price is asserted. JC2 remains
unresolved. All three blinds are terminal; none is rewritten.

## Read scope

CROSS.md, the ROOT, Astra and Fable blinds, COORDINATION.snapshot (bounded
chunks 1-230, 231-460, 461-694) and SWARM-POLICY were read WHOLE from the
lane inputs after the charged pins matched (ROOT 238f25a5, Astra 4384ba16,
Fable d6719390, APP 0a847f15, COORD 4ce5b29a, Policy 50cf4548; the box copy
of CROSS.md hashes c9c5c6f5, identical to the lane copy). APP was checked
selectively only: lines 140-165 (TRACE, two-polar criterion, TRACE-CUTOFF),
468-480 (Liouville, radial finite graph, conductor, pinching control) and a
keyword grep touching 193-199 and 481-485. No new full APP read is claimed.
No linked report, live ledger, peer cross or external source was opened.

## Q1: Astra's selected-H trace criterion

Valid, and exactly a properness endpoint. Write P_H(f,g,w) = sum a_k(f,g) w^k
for the irreducible graph polynomial, degree d in w, a_d its leading
coefficient. Because A = C[f,g] is normal and H is a primitive element, the
d traces lie in A iff the monic minimal polynomial P_H/a_d has coefficients
in A iff a_d divides every a_k in A iff (P_H is primitive) a_d is a nonzero
constant. Astra's chain then runs: a_d constant => H integral => B finite
over A => R finite over A (promoted graph finiteness) => F finite =>
automorphism. So the criterion is "a_d in C^x", one polynomial condition.
Two elementary steps sharpen Astra's pole remark: over a_d != 0, R[1/a_d]
is finite over A[1/a_d], so F is finite there; conversely where F is finite
the minimal polynomial is integral over the local ring, which forces
a_d(t) != 0 by primitivity. Hence the actual nonproperness curve D is the
zero set of a_d exactly, and the trace poles Astra confines to D are the
poles of a_k/a_d. This identifies Astra's object precisely; possibly KNOWN
(Jelonek-type), ROOT to checksum. It is not a new trace-membership
implication: nothing in either peer blind forces a_d constant, and my own
blind supplies no trace statement at all. ROOT's Card 1 frames act here:
target derivations extend uniquely to L and commute with Tr, so Tr(R) is a
D-submodule of K and the derivatives of s_k are the recorded TRACE-HAM
identities, again endpoint data. Astra's NO_TEST stands. The one reading
correction: "a pole in one of the d traces" means "a_d nonconstant", which
is the definition of nonproperness, not a constraint on a source.

## Q2: the off-diagonal criterion, exact directions, own corrections

For the selected H, L the off-diagonal fibre square and
delta_H = H o pi_1 - H o pi_2:

(a) Elementary, both directions: Gamma_H normal <=> j_H injective on closed
points <=> delta_H has no zero on L <=> delta_H in O(L)^x. Cleaner proof
than my blind's S2 sketch: a finite unramified birational map with one
point over gamma is a local isomorphism there (Nakayama), and a normal
local ring is unibranch, so Sing(Gamma_H) is exactly j_H of the double
locus. The codimension-one remark is unnecessary; do not cite it.
(b) Promoted chain: Gamma_H normal => F automorphism.
(c) Classical: F automorphism <=> F injective <=> L empty.
(d) Therefore, for every non-injective Keller map, V(delta_H) meets L. This
is a theorem-level consequence of (a)-(c), not a gap.

Corrections to my blind's stronger claims. First, "no leverage beyond
injectivity except through O(L)^x/C^x" is wrong in its exception: by (d)
delta_H is already known not to be a unit whenever L is nonempty, so no
information about O(L)^x moves the normality endpoint in either direction.
Second, "every normality, ruling and conductor endpoint reduces to the unit
group or to injectivity" should read "reduces to injectivity of j_H", which
by (a)-(c) is injectivity of F itself; a direct proof that H separates
fibre pairs needs no unit theorem. Third, "delta_H nonconstant on each
component" is unproved and unnecessary; birationality gives only delta_H
nonzero on each component. Fourth, my Card 1 unit-group tranche is
withdrawn as a proof lever.

What constant units WOULD say. Any separating difference is anti-invariant
(sigma^* delta = -delta), so a unit of that form on nonempty L is
nonconstant. Hence O(L)^x = C^x would imply that NO regular H whatsoever
makes (F,H) injective: every one-generator graph of a counterexample is
non-normal, for every H, not only the selected one. Direction: constant
units => non-normality of all graphs; never => normality. They constrain
what a separating function could be, to the point of excluding one, and
force nothing. Empty L: every clause is vacuously true, F is an
automorphism, O(L) is the zero ring, and the statement must be read as "L
empty or delta_H a unit", as the blind wrote. The recorded S-chart off
square u=-x, x^2(y+v)=2, on which x is a unit, stays the negative control
for any all-H unit claim; it drops full-plane polynomiality.

## Q3: units on S and the fibre filter

The lemma O(S)^x = C^x is correct (S integral, S_{A!=0} = A^1 x G_m, A
vanishes on the double fibre). "Etale S -> A2 <=> regular scalar pair" is a
valid equivalence, but the scalar row was already implied by the etale
rows, so deleting it changes no solution set; it only spares a topological
or fibration existence argument from checking the scalar. That is its
entire content. The fibrewise Riemann-Hurwitz filter is not a new
construction test: with P a submersion, "Q unramified on every fibre P=c"
is the etale condition restated, so passing it for all c IS finding the
pair, and failing it for one P excludes that P for every mate.
Mate-independent exclusion is already the recorded pattern (APP line 197:
H=P(Z)+UQ(Z) has no arbitrary regular mate), so my Card 2 filter is
DUPLICATE in kind, with the same gap: no complete pair and no reason a
chosen P family is exhaustive. Its outcome A was overstated: the filter
cannot produce Q, only certify one already found. Withdrawn as a tranche.

## Combination and hidden premises

Combined statement for the selected H of one full-plane Keller map:
a_d in C^x <=> s_1..s_d in A <=> H integral over A <=> F proper <=>
F automorphism <=> L empty <=> j_H injective <=> Gamma_H normal <=> the
promoted conductor is a unit. Astra's card and my card are the two ends of
one identity. Hidden premise shared by both blinds and by ROOT's
"normality of the chosen radial graph" objective: that graph normality is
a hypothesis obtainable short of injectivity. Under the promoted chain it
is not; it is JC2 for that F. The two failure loci are nevertheless
distinct: properness fails along D = V(a_d), normality along
Sigma = F(double locus), the image of Sing(Gamma_H), a curve the chain
forces to be nonempty but does not locate. No statement I checked places
Sigma inside D or D inside Sigma. A normality attack must control Sigma,
about which trace poles say nothing; a trace attack controls D, about
which the double locus says nothing. ROOT's Card 3 and my Card 2 agree once
the scalar is automatic: the S endpoint is one closed exact coframe with
nowhere-zero wedge, no scalar row. ROOT's Card 2 is untouched by the cross.

## Cheapest genuinely changed test

NO_TEST. All three blinds reached NO_TEST independently and the cross
confirms it. The only changed item is a minutes-scale manual recording by
ROOT under avenues 31/32/33: the endpoint identity, D = V(a_d), and the
Sigma/D distinction, labelled KNOWN-composed unless the history checksum
finds them absent. Its value is negative: it stops every normality,
conductor, ruling, trace-power, unit-group or frame variant on the selected
graph that exhibits no mechanism for a_d-constancy or for H separating
fibre pairs, because those are JC2 restated. The postblind documentary
leads combine with nothing here: the real-hyperplane criteria need an
acyclicity the campaign does not have, and the approximation heuristic is a
different construction from the S/T endpoint. No external read was made.

## Disagreements retained, not voted

- ROOT keeps chosen-graph normality as a proof objective; this cross says it
  is the conclusion, not an intermediate. ROOT's checksum decides whether
  the promoted "B normal => B = R => automorphism" step carries a frame
  restriction; if so, (b) narrows and the identity weakens to (a)+(c).
- Astra ranks "conductor unit or traces polynomial" priority 1; I rank it
  as no priority, being the conclusion. Astra's own phrase "another exact
  properness criterion" is closer to this cross than to that table.
- My Cards 1 and 2 are withdrawn as tranches; equivalence (a) and
  "etale S -> A2 <=> scalar pair" survive as recorded facts.

## Recommendation

CONTINUE protected all-degree research and ROOT's postblind history and
primary audit. REDESIGN nothing: no actual source-hypothesis delta exists.
STOP, beyond the three STOP lists: the unit-group tranche, the fibre-filter
tranche, and any selected-graph normality or conductor successor. No new
worker, OPEN, computation or successor.

## Custody

Own report read back whole before sealing; charged pins rechecked unchanged
at that time. No exit price is asserted, so no exit-price declaration line
is present. Word count is below the 1600 cap. Wrapper owns custody; no
finalizer was run.

<!-- BODY-END -->
