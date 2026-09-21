# Integration: actual additive quotient and the one-point scheme criterion

Producer/integrator: swarmHQ ROOT (Codex/gpt-6-astra; hosted identity unattested)
Independent reviewer: requested Fable5.1/max, different-model hostile FIRST
Date: 2026-09-21 UTC
Basis: a450b715198107cfdc219256985756e4e5acffb9
Evidence tier: MANUAL with named classical imports
Lifecycle: integration decision PROMOTED at exactly the scope below

## Decision and frozen evidence

Accept KELLER-ADDITIVE-QUOTIENT-1. The
[producer](keller-additive-quotient-swarmHQ-root-20260921T012300Z.md)
and [hostile FIRST](keller-additive-quotient-first-swarmHQ-fable-20260921T013000Z.md)
support the actual-source construction and its conditional equivalences.
No positive scheme-neighborhood, separatedness or properness premise
has been proved. JC2 remains unresolved. The original reports are kept
byte-identical; this integration corrects reviewer wording and source
attribution, not the producer's mathematical statement.

Frozen evidence identities:

- Producer full SHA256
  `19d4f01376692efcd87b839dbbd088625b66c26e1bf5db94ecf98d8421b4ad3e`,
  manifest `634e2e29dc229c07da5fe41e52ee56c7bf44df00109902a5732c01b45a424b8c`.
  Producer basis ee7e771e; reviewed contribution a450b715.
- Raw FIRST full SHA256
  `cdd5f8087ff18715797944a148ffd1d31a0023a0042a5f81a69e6674546c762d`.
  Its legacy BODY_SEALED/CLEAN receipt records the completion-marker
  boundary, not a canonical seal. No canonical seal is retrofitted.

The producer's frozen UNPROMOTED label records its pre-review lifecycle;
this integration and the accepted ledger record the later promotion.
No literature-priority claim is made: internal calculations preceded this
initial independent audit, and their old evidence tiers remain historical.

## Accepted scope

For every polynomial F=(P,Q):A2_C->A2_C with detDF=c!=0, put
Y=F(w)+ta on V=A5_(t,w,a). Then

    Phi_b(t,w,a)=(t,w+tb,a-(F(w+tb)-F(w))/t)

is a scheme-theoretically free Ga2-action with invariant ring C[t,Y].
Its fppf quotient p:V->X is a Ga2-torsor. X is a smooth irreducible
finite-type algebraic space of dimension3 with affine diagonal. The
invariant map is q=h p, with h:X->A3_(t,Y) etale and an isomorphism over
t!=0. The special fiber X0 of pi:X->A1 is A2_w and h0=F. Every geometric
fiber of pi is A2; these are NOT the fibers of q or h over (t,Y).

The following are equivalent within this exact construction:

- F is an automorphism;
- some point of X0 has a Zariski-open scheme neighborhood in X;
- X is a scheme;
- X is separated over C;
- X is affine;
- the action is proper;
- the displayed action has the report's polynomial translation coordinates.

Thus hypothetical noninvertibility makes every point of X0 nonschematic
in the stated neighborhood sense. An explicit etale scheme chart still
exists. Neither that chart nor the affine invariant ring supplies a
Zariski-open scheme neighborhood.

## Independent reconciliation and binding precision

FIRST reconstructed all nine requested interfaces and found no unsupported
mathematical implication. ROOT independently checked the local ZMT chain
against the frozen proof before collecting FIRST, then read all225lines
of the terminal review. The following precision is binding.

1. **Use the correct source for quotient existence.**
   [Stacks tag06PH, Lemma80.11.7](https://stacks.math.columbia.edu/tag/06PH)
   applies to free actions of flat locally finitely presented group
   algebraic spaces and supplies an algebraic-space quotient and torsor.
   Here the group is Ga2 over C; no finite-group quotient theorem is used.

2. **The producer's ZMT citation was correct.** The directly read
   [tag05K0, Lemma37.43.3](https://stacks.math.columbia.edu/tag/05K0)
   states the finite factorization used by the producer: quasi-finite
   separated source morphism, qcqs target, open immersion followed by a
   finite map. FIRST's recollection that this tag was instead only the
   integral-normalization statement is not accepted. No neighboring
   theorem or fresh source retrieval is needed to repair the attribution.

3. **Quasi-finiteness uses etaleness, not affineness alone.** On the
   chosen affine neighborhood V0, etaleness gives local quasi-finiteness;
   finite type/quasi-compactness gives quasi-finiteness. The fact that both
   V0 and A3 are affine supplies separatedness. FIRST's compressed phrase
   must not be read as a claim that arbitrary maps between affines are
   quasi-finite. The producer uses the correct conjunction.

4. **The diagonal square has X, not V, in its first factor.** The precise
   base change is X x_(X x X) (V x V) = V x_X V = Ga2 x V. This is the
   square used in the producer. A mistyped first factor in FIRST item3
   does not change the correctly identified action morphism or its proof.

5. **The finite-etale locus is genuinely generic, not global.** One may
   justify the standard fact directly: w1,w2 are algebraic over C(P,Q).
   After inverting one nonzero target polynomial clearing the coefficients
   of their monic minimal polynomials, the localized source ring becomes
   finite over the localized target ring.
   The already etale map is finite etale on that nonempty target open,
   with rank equal to the field degree. It therefore supplies a collision
   if the degree exceeds1, but does not assert global finiteness of F.

6. **Birationality is invoked locally on schemes where needed.** The
   global description of h means it is an isomorphism over a dense open.
   Irreducibility of X follows from the surjective torsor, and any affine
   neighborhood V0 of a special point meets that dense open. ZMT is applied
   to V0->A3, not to an unproved separated X. Finite integral closure inside
   C(t,Y) is C[t,Y] by normality. Restricting the resulting open immersion
   to the nonempty open V0 intersect X0 makes F birational. The report's
   unit/codimension-two argument then gives automorphy.

These are citation corrections, type corrections and unpacked classical
steps. They introduce no new positive premise, extension theorem or
source family. The opposite implication uses the original explicit
s=(w-F^-1(Y))/t coordinates; collision arcs test the original action.

## Source-read limits and custody

ROOT read both relevant primary theorem statements and their immediate
page proofs during producer preparation. Linked dependency proofs were
not re-audited; these remain named classical imports. The birational-
definition page tag01RN was navigation/definition verification, not a
stronger open-immersion theorem. No new source was acquired at integration.

FIRST attempted each authorized endpoint once, both returning HTTP200,
but its in-call extraction filter dropped the statements and proofs.
It therefore checked the mathematical import from prior knowledge, NOT
from an independently verified primary-text read. The review's page-title
and comment capture, shell-captured hashes and newline-normalized hashes
do not repair that limitation or certify raw source-byte identity.
The no-refetch rule was respected; no mirror, retry or dependency page
was used. ROOT's earlier direct read supports the precise attribution
above, without pretending it was FIRST's read.

The same external review terminated with exit0/DONE. Exact supervisor,
descendants and cgroup were confirmed absent BEFORE receipt-first
collection. The report, log and receipt were then frozen read-only and
whole-read; their pre/post hashes matched, as did all seven charged inputs
and the current governance/prompt/launcher pins. The canonical producer
was reverified. None of this integrity evidence substitutes for the
manual mathematical audit.

Delivery limitations remain separate: the startup acknowledgment was
captured108seconds after launch, a48second miss, and abbreviated three
executable paths. The raw report says readback01:45 but gives measured
completion01:44:22; its terminal log explicitly corrects the rounded
readback wording to shortly before that completion. Raw bytes are not
rewritten. Full side effects, early-draft/partial timing, hosted identity
and disabled-memory behavior are not certified by the final-only log.
Independent author/service/integration caps were not extended.

## Consequence for research, and exclusions

This banks a checked ACTUAL-source reduction, not a hypothetical surrogate
or another bounded-degree exclusion. The missing global step is now
stated without an etale-versus-Zariski ambiguity: closing this route needs
a scheme neighborhood (or another equivalent positive condition) for this quotient.
No such step is supplied by the reviewed reduction.

The earlier Picard/resolution-property, affine-fibration and Luna source
fits keep their original scope and missing hypotheses. No new theorem
about arbitrary additive actions, quotient spaces, affine-plane fibrations,
cohomology vanishing or actual counterexamples is promoted. No automatic
classification, source-fit, control family or new strategic echo follows.

## Replay and negative controls

Desk-only. FIRST independently recomputed the chart determinant c both
at t!=0 and t=0, arbitrary-base freeness and translation inverses, and
checked the collision-image nonclosedness separately from the DVR argument.
The producer's identity-map check and non-Keller stabilizer control remain
at their stated scope. No scientific code, CAS, numerical sample, modular
test or formal certificate is claimed.

## OPENS RAISED

None. The retained positive quotient premise is still the global JC2 gap,
not a newly commissioned test or a proof of impossibility.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Whole-author readback completed 2026-09-21 01:49:18 UTC; two wording
clarifications, the collision output and this footer were then added.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9837`.
- Body SHA-256:
  `8a6199534a6db41db261b69d2b4f1bb79658db62c6a395ce4e9d88b31fcae443`.
- Frozen basis: `a450b715198107cfdc219256985756e4e5acffb9`.
