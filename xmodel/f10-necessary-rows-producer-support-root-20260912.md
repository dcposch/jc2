# Necessary-row producer: retained-support feasibility bound

MANUAL / PRODUCER-CHECKED CANDIDATE, NOT PROMOTED. No execution or new
registration. The r3 source remains untested. ROOT began the current revisit
around03:00UTC September12; this report transaction began03:10:49UTC.
Original report reserve03:24 / HARD03:27; no runtime clock is changed.

## Exact scope and history

For the exact branch-deleted producer below, once its genuine-place/scalar
checks permit a node, every retained polynomial intermediate has fewer than
100000 monomials. The producer's mathematical graph contributes at most12360
serialized monomials and the complete output is less than4MiB. These are
structural bounds, not measurements, predictions of completion, or bounds
on total live Python objects, operation count, CPU, RSS or batch disk usage.
All anomaly, admissibility, authority and resource predicates remain active.

Direct finite-place evaluation and deleting the dead Laurent-q branch are
ALREADY accepted mechanisms. The previous block redesign bounded the REMOVED
inverse branch, not the retained SCALE/graph stages. Its FIRST explicitly
left retained term/wire sufficiency unknown. This attachment addresses that
narrow feasibility question with no implementation change. It does not
repair the stopped runtime/descendant-cleanup or holder-release workflow.

The checker is independently assigned to Astra; this report charges none of
its new live work. It proves only the producer claim. A different-model FIRST
is needed before this bound is used to justify an expensive commitment.

## Frozen inputs

Fresh pins, followed by complete text reads, for the executable math sources:

- box/f10-necessary-rows-producer-astra-20260911/produce.py:
  5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a.
- box/f10-direct-rows-powerfix-astra-20260911/arithmetic.py:
  acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73.
- box/f10-necessary-rows-producer-astra-20260911/authority.py:
  804c7aff56538fc332bf68638b03b7167eccdb49f73337f1a5f1823348b522a4.

Fresh pin/WHOLE source-interface and history context:

- box/f10-necessary-rows-root-20260911/ROOT-ADOPTED-NECESSARY-ROWS.md:
  176363939a8aa6861995cd72a99c61f7d04bfeab5a9634f6d3143dcd3d3bd098.
- box/f10-source-cone-direct-circuit-astra-20260911/ROOT-ADOPTED-CORRECTIONS.md:
  39ed9b3910efee02dd2f17ced7951a8b83557e612d100d4ae34f76e0895b4002.
- xmodel/f10-direct-rows-inverse-redesign-astra-20260911.md:
  19f1a4229cacb14c7744230707a9a822d63658cbd9ef7f727d5f164bdb8c1874.

The old necessary-row FIRST was searched at selected passages, not freshly
WHOLE-read here. Its recorded SHA8e07e419d321b09ecd13c61a1c5fdc3dbaf9a099c1a1ebedf9b9fe6ef280073b
was rechecked after that search. No new independent review is attributed to
it. The complete executable sources above own the new support argument.

## Elementary support count

For variables of weights (1,w1,...,wm), the number N(d) of monomials of
exact weight d is the number of nonnegative integer tuples satisfying
sum wi*ei<=d. The disjoint unit boxes based at these tuples lie inside
the positive simplex sum wi*ui<d+sum wi. Therefore

N(d) <= (d+sum wi)^m / (m! product wi).

This bounds supports over ANY coefficient ring. Partial products/sums at a
fixed weight obey the same bound before cancellation, not only after it.
Weight-one multiplication also makes N(d) nondecreasing with d.

RAW variables (X1,X2,X3,X4,z,S,theta) have weights (1,2,3,4,7,1,3).
Eliminate X1. The other weights sum20 and product504. For d<=23,

Nraw(d) <= 43^6/(720*504) < 18000.

Indeed43^6=6321363049 <18000*362880=6531840000. FORMAL parameter
variables (X1,X2,X3,X4,z) have weights (1,2,3,4,7). For h<=10 their
number is <=26^4/(24*168)<114. The auxiliary theta has weight0 and
degree at most14 in the circuit, so at most1710 formal monomials suffice.

GRAPH variables X1..X4 have weights (1,2,3,4). For d<=30,

Ngraph(d) <=39^3/(6*24)=59319/144 <412.

We use the intentionally loose integer ceiling412 below. No enumeration,
CAS, sampled place, or import of the scientific code was used for these
inequalities. They count dictionary KEYS, not coefficient bit complexity.

## Retained producer walk: pre-SCALE

The mathematical code's add/mul build a fresh dictionary and check its
current size. Hence a support set containing every pairwise product also
bounds the inner multiplication loop before exact cancellation. All scalar
field lists have degree<=7 after reduction and are not Poly dictionaries.

1. LEADING and FORMAL. Every gap-h parameter polynomial has weight h,
   by induction: forcing multiplies bands i and h-i; theta differentiation
   preserves parameter weight; upper elimination, scalar matrix inversion,
   scalar functionals and coefficient extraction preserve it. The only
   introduced parameters are Xh of weight h, z of weight7, U of weight4,
   U*d0 of weight7 and U^2 of weight8. Basis/variation columns have parameter
   weight0. Thus h<=10 for every formal partial sum/product. Theta degree
   is<=7 in ordinary band/operator work. The largest exceptional theta
   expression is C^2*integral(R*invC2): degrees6+(1+6+1)=14. The series
   routine multiplies its already truncated term by c-1 of degree3 before
   truncating; degree<=10 there, also below14. Binary polynomial power
   computes no unused terminal square. All these supports are<=1710.
   Matrix inverse products and denominator registries are scalar, not
   parameter polynomial inverses. A bad scalar place still stops.

2. INSTALL and LAURENT-S. Each admitted A term has total weight10 by the
   fixed S exponent10-h-3j. Every partial Ahat sum has the same weight.
   Ahat is polynomial; the two excluded negative-exponent positions are
   inspected separately. Write a_j=[theta^j]Ahat. Their weights are10-3j.
   Dformal=(a2+U)/S has weight3 and S exponent>=-1. Vformal=
   (a1-z+U*Dformal)/S has weight6 and S exponent>=-2, including BEFORE
   a negative-S anomaly might cancel. Multiplication by S or S^2 injects
   these supports into nonnegative raw degrees4 and8. All intermediate
   numerators obey the same bounds. No vanishing anomaly is assumed.

3. EULER and JACOBIAN. Pi has raw weight10 and Delta weight23. Descending
   induction gives bb[j] weight17-3j: each summand of q has that weight,
   and coefficient extraction at S^i followed by reinsertion S^i preserves
   it. Fixed gauges contribute zero, not a new parameter. Bhat and every
   partial installed sum have weight17. Each Jacobian product has weight
   10+17-1-3=23; its accumulated terms and J-Delta lie in Hraw(23).
   Every extracted low/upper coefficient has the corresponding smaller
   weight. Euler-band reindexing gives parameter weight h<=10 with its
   original theta degree<=5. Thus all retained raw/auxiliary/diagnostic
   dictionaries through this stage have fewer than18000 keys.

4. GRAPH INPUT and GRAPH. All pre-substitution polynomials are independent
   of S,theta; T=z*P1[0]-U*P0[0] has parameter weight27. This T is NOT
   incorrectly put in raw degree<=23. For five parameter variables up to
   degree27 the preceding simplex estimate is43^4/(24*168)<850, so its
   partial products/sums remain small. Hq and zeta have X-weight7; scalar
   critical-c inversion changes no support. Substitute_z forms each
   coefficient monomial times zeta^r, weight equal to its input weight,
   and adds terms of that same weight. Its power routine has no unused
   final square: all powers used have weight<=21 for r<=3. All graph
   intermediates, including g=Hq*ell and zeta*ell, have weight<=30 and
   therefore<=412 keys. Zero and duplicate slots are still retained.

These are structural statements about the actual fixed loops, independent
of the final envelope checks. They do not infer generic identities from
modular zeros or omit any expression whose diagnostic might be nonzero.

## SCALE: Laurent reindexing, not aggregate inverse expansion

Define Phi_k(P)=s^k P(X,z=s^2,S,theta=s*t), allowing Laurent S.
For a fixed k this is injective on monomials: the t exponent remembers the
old theta exponent, and then the s exponent recovers the old z exponent.
Hence it does not increase term counts. Products obey
Phi_k(P)*Phi_l(Q)=Phi_(k+l)(PQ); partial accumulators have supports in the
same reindexed raw product envelope. Coefficient extraction in t shifts k
by the extracted exponent, and differentiation in t shifts k by1.

The code's origA/B are Phi_-3(Ahat),Phi_-5(Bhat). Its origd/v/k/u/ell
are the displayed Phi_-1(D),Phi_-2(V),Phi_-3(K),Phi_-1(U),Phi_-3(E).
OrigPi=Phi_-3(Pi), origUpper=Phi_-7(Delta), origJ=Phi_-7(J).
These identities follow term-by-term BEFORE any comparison is tested.
Both separate Jacobian products and their accumulation inherit Hraw(23).

Reconstruction similarly consists of Phi_-3 images of
S*theta^3, (S*D-U)*theta^2, (z-U*D+S*V)*theta and K.
Every summand has weight10 and S exponent>=-1; multiplying this common
Laurent envelope by S embeds it into Hraw(11). Thus its partial products
and sums, including an as-yet uncancelled Laurent part, stay<18000.
The A_inverse comparison shares the same common Laurent envelope.

OrigResidual is Phi_-7(J-Delta) minus1 and Phi_-2(U*theta).
Its intermediate additions involve at most three fixed reindexed envelopes,
each with fewer than18000 possible keys. Low1 compares
Phi_-6(P1[i])-(origu if i=0) with the identical two-envelope extraction;
low0 compares Phi_-7(P0[i])-(1 if i=0) with its two-envelope extraction.
Partial construction/comparison adds no new envelope: both operands use
the same fixed shifts. Bracket_scale and target_inverse are each within
one Hraw(23) image. Guard multiplication and its comparison are scalar
monomials. The loose common bound FOUR envelopes, each<18000 keys,
plus two isolated constants gives fewer than72002 keys for every SCALE
dictionary. In particular it is below100000 without assuming the final
six comparison groups vanish. This addresses transients, not only outputs.

No hidden truncation or early required-zero assumption is used. The old
alternative map S=P*q^3-z*q^2+U*q,theta=q^-1 is absent from the new source;
its much larger aggregate support is NOT bounded by the SCALE argument.

## Wire term and byte bounds

There are exactly30 polynomial positions: Hq,zeta,25 slots,ell,g,U, plus
two field scalars c,c_inverse. Each polynomial has weight<=30 and<=412
terms, so the producer's accumulated wire counter is<=30*412=12360.
This is below both20000 per polynomial and400000 total. In particular
retaining empty and repeated slots does not invalidate the count.

The initialized field has degree<=7 and p<=2147483647. Thus each coefficient
coordinate has at most10 decimal digits, and every graph exponent has at
most2 (its weight is<=30). A compact JSON monomial record, including a
separator, is less than128 bytes: its four exponent strings need<=21,
its seven field strings<=92, and the pair brackets/comma<=3. The graph
terms therefore use less than12360*128=1582080 bytes. All fixed labels,
brackets, polynomial dictionaries and scalar records fit a conservative
65536-byte overhead allowance.

Authority.load_pinned reads at most65537 bytes and rejects a registration
larger than65536. The copied place/source_pins/contract data are contained
in that registration. Reencoding strings using ensure_ascii=True expands
their original JSON byte representation by at most a factor6 (including
non-ASCII and escape cases), so less than393216 additional bytes suffices.
The whole producer payload is consequently below4MiB, far below its
134217728-byte wire predicate. This does NOT bound runtime logs, native
metadata, a malformed checker input, total resident graph copies or a
complete batch's aggregate disk use. The byte proof uses the exact current
source limits and metadata parser; changing them would need a new analysis.

## Scope controls, interface and disposition

Manual negative control: if a variable q has negative weight-3, the sums
sum_(i=0..N) X1^(3i)*q^i all have weight0 with N+1 terms. Positive weighted
degree alone then gives NO finite support bound. This is why the removed
inverse type cannot be smuggled into the proof. SCALE instead has a fixed
injective reindexing for each small, explicitly enumerated input envelope.

A second control distinguishes memory/time from support. Multiplying two
polynomials with m and n terms can still visit m*n pairs even when every
partial accumulator fits a much smaller homogeneous envelope. Keeping many
such dictionaries can also consume large aggregate memory. Thus this proof
does not eliminate CPU/RSS/wall or implementation-cleanup failures, prove
a useful speedup, select a good place, or guarantee production completes.

Theorem-interface pass: this bound consumes the accepted necessary-row
circuit's literal fixed degrees. It does NOT alter the accepted23z/19z
source implication, nor discharge its missing actual place,25-row agreement,
297-rank witness, or T+X1^27 negative-control observation. It creates no
new source family or closure and authorizes no retry of terminal batches.

History disposition: SAME weighted-support method as the old inverse-block
proposal, NEW APPLICATION to the already retained producer stages that
its own FIRST explicitly left unbounded. No general algorithmic novelty is
claimed. The cheapest next discriminator is one focused different-model
STATIC gate on this source walk together with Astra's independent checker
analysis if terminally available; planning12-15minutes, UNMEASURED. The
separate operational release/cleanup question remains a launch hold.

No new canonical OPEN ID or scientific artifact is introduced. Manual
source reasoning only; no Python scientific import, AST/syntax/test, local
dummy, CAS, AWS allocation, process-control change or protected-tree read.
Only this owned report transaction and current canonical live notes may be
edited. Own complete readback and postpins precede the final marker.

Closeout03:14UTC: own full untruncated readback completed, and all six
charged input pins were rechecked unchanged03:14:27. Own target was absent
at begin; targeted history search found the earlier inverse-block bounds,
which are disclosed above, and no earlier retained-stage proof was located
in that bounded search. No whole-corpus novelty claim or canonical OPEN ID.
COLLISIONS: no new identifier or duplicate live ownership. Astra's separate
checker status message arrived only after this proof body was written; its
live report is uninspected and not a premise. This closeout and marker are
the last body write; transaction sealing/verification follow before03:24.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14650`.
- Body SHA-256:
  `cbc67dc817632f07e5a6b5ddadc79ab91c8460674771afbca16163ed095c55a5`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
