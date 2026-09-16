# Different-model review: quintic partition target-field obstruction

Reviewer: swarmHQ gpt-5.6-sol, native task torus_quotient_sol_review.
Recorder: ROOT, faithfully recording the terminal mathematical review and
final verdict; this is not a verbatim log or a Sol-authored file.
Evidence: MANUAL hostile proof review. Verdict: CONFIRMED, A-E.
Mathematical completion: 2026-09-16T03:29:41Z.
Reviewed contribution: f38acc8a1c268b1a47f7befe2dd1aae91d322ef1.

## Frozen scope and custody

The [producer report](quintic-partition-target-field-swarmHQ-root-20260916T032000Z.md)
was complete and sealed before review. Sol read the whole report and
manifest and verified finalizer custody, all expected pins, 0444 modes,
and unchanged HEAD. ROOT collected the entire mathematical message and
final verdict and observed authoritative COMPLETED before this record.

- Producer body: b2753ce061c01614fd09955968d3f9aad8bb009a2ec6807a9e8e616267f33337.
- Producer full: de842da606627616e8a8c1670240721e16247c33e3b88f764e817f2a2b01a651.
- Producer manifest: e55fe588038d29e43dd6a1efdde1c422b35ead0034e09eb6ad4244046627a74d.
- Embedded basis: 4069f525c6a7475d8ae2d815949ea17777ec9380.
- Nearest marked-root fixed-coefficient comparison:
  a56a1de74b34a283e1c4f32bc4e316f0da372f4c75a18c60afd1fd96589333e5.
- FALLACY-v2: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

The source marks an unordered pair of DISTINCT SIMPLE roots of a stable
binary quintic. It is not the space of every boundary 2+3 partition.
The map forgets that marking into the projective coarse quintic quotient.

## A. Whole source invariant ring — CONFIRMED

For H=aX^3+bX^2Y+cXY^2+dY^3, ad!=0, the remaining torus weights are
(3,1,-1,-3). Stripping ad and bc from a weight-zero monomial leaves
powers of ac^3 or b^3d. Thus the invariant ring is

    C[A,B,C,D]/(CD-AB^3),
    A=ad, B=bc, C=ac^3, D=b^3d.

The root swap interchanges C,D and fixes A,B, giving C[A,B,C+D].
Localizing A and taking scalar degree zero gives exactly C[r,s], with
r=B/A and s=(C+D)/A^2. Normalizing a=d=1 leaves a finite mu3 action
and b,c interchange, whose invariants bc,b^3+c^3 separate finite orbits.
They realize every pair r,s. This proves a coarse orbit chart, not only
a birational parametrization or a globally regular gauge choice.

## B. Exact stable puncture — CONFIRMED

The two marked roots cannot meet H because ad!=0. Instability is exactly
a triple root in H. A cube gives r=9,s=54. Conversely those values imply
bc=9 and b^3+c^3=54, b^3*c^3=729 in the normalized chart, so b^3=c^3=27.
This is one residual triple-root orbit. Therefore

    U=A2_(r,s) minus {(9,54)}.

The cubic X^3+Y^3 gives the stable point(0,0), a contrasting control.

## C. Target, morphism, image and degree — CONFIRMED

Sol independently read the permitted primary Section5 of Hassett--Kresch--
Tschinkel, [On the moduli of degree 4 Del Pezzo surfaces](https://www.math.brown.edu/bhassett/papers/modulidP4/noheighttwo16.pdf),
printed9--11. It supports the characteristic-zero coarse target
Y=P(1,2,3), normal and projective, and the stable locus of quintics with
at most double roots. This is a selected-source check, not a whole-paper
audit or a coarse-etaleness import.

The invariant multiplication morphism descends to q:U->Y. Stable root
patterns are 1+1+1+1+1, 2+1+1+1, and 2+2+1. Exactly the last lacks two
simple roots. Its three support points give one PGL2 orbit y_*, so
q(U)=Y minus {y_*}. Each fiber is a finite set of eligible marked pairs
modulo the finite quintic stabilizer. Hence q is quasi-finite. A generic
five-point configuration has trivial stabilizer, giving binomial(5,2)=10
choices and, in characteristic zero, generic field degree10. Special
stabilizers can identify choices; constant cardinality and etaleness
are not asserted.

## D. Divisorial-pole intersection — CONFIRMED

For every target prime divisor D, cofinite image and quasi-finiteness
supply a source prime divisor E dominating D. The generic normal local
rings are DVRs, and their local inclusion gives

    ord_E(q*h)=e*ord_D(h), e>0.

A target uniformizer has positive source order; target units and their
inverses remain units. If q*h is polynomial in r,s, it is regular on U,
so h has no negative divisorial order anywhere on Y. Normality extends
h across codimension two; projective integrality gives H0(Y,O_Y)=C.
Thus, inside C(r,s),

    q*C(Y) intersect C[r,s] = C.

No properness of q or bound on pole order is needed. The open immersion
A2->P2 omits a divisor and fails the coverage premise. An affine target
can have nonconstant global regular functions and fails the last step.

## E. Construction conclusion and excluded readings — CONFIRMED

Every rational target component whose pullback is polynomial is constant.
Hence there is no dominant polynomial target postcomposition, let alone
a Keller pair, on this fixed source chart. Polynomial source coordinate
automorphisms preserve the intersection. Arbitrary rational or finite
source changes are NOT covered: y/x becomes v under (u,v)->(u,uv),
illustrating why denominator cancellation requires a separate argument.
Other markings, charts, root counts and general JC2 remain outside scope.

No correction or GAP was found. The proof uses a standard pole mechanism;
the review does not establish literature novelty. No reviewer files,
scientific subprocess, CAS, cloud jobs or dependent research were used.
Integrity checks are custody evidence, not a substitute for the arguments.

## OPENS RAISED

None. No larger marking or root-count family is proposed.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The canonical lexical scan is not a mathematical novelty certificate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5761`.
- Body SHA-256:
  `d36fed78654aaa746bcb8cda069f7bbc0fd3a9423bc1ac5fe15d85d9ac7b565c`.
- Frozen basis: `f38acc8a1c268b1a47f7befe2dd1aae91d322ef1`.
