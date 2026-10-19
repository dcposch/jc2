# Independent FIRST: positive-zero multibranch obstruction

VERDICT: CONFIRMED / PROMOTED-MANUAL at the exact scope below.
REVIEWER: retained Sol5.6-assigned native seat affine_radial_first_sol56_2157.
Hosted model identity is unverified; no paid-adapter receipt is claimed.
AUTHORSHIP: ROOT transcribes the terminal independent review; ROOT produced the proof.
Reviewer terminal verdict: 2026-10-19T10:17:35Z; ROOT registry closure by10:18:12 UTC.
Frozen public basis: 3832aae6d2da9d1564416bad66db9c1d3bfdf7dc.

## Charged artifact

[Producer](positive-zero-cycle-swarmHQ-root-20261019T101200Z.md):128lines,
7068bytes,mode0444,fullSHA256
115f551e6b14f7f9715801a23024c43f5d604d14da49e580f6146d9f02ee03e1.
Body6736bytes,SHA d65fbc37cb3a10ee063dffb335143c69ac04d9a0d3a0f0e4ce4ba57160392176.
Manifest698bytes,mode0444,SHA
217e1bd89bb8db8639d002ac92bcb9ed5ac954fd5eded64c81cad12464a54e16.
The producer's sealed UNPROMOTED label is not rewritten; this review and ROOT's
ledger integration supply promotion only at the following precise scope.

## Exact confirmed result

Let S be a smooth projective complex surface, omega a nonzero rational two-form,
and E an irreducible curve with ord_E(omega)>0. If E has at least two geometric
branches at a point z where omega is regular on a neighborhood, there are no
rational coordinates u,v generating C(S) with omega=c du wedge dv, c in C*.

For a finite dominant map pi:X->Y of normal projective complex surfaces,
assume an irreducible ramification curve E is multibranch at a smooth point x,
its image y is smooth, and a rational target form eta is regular and nowhere
zero near y. Then pi*eta has no such rational Darboux coordinates on C(X).
If eta=dp wedge dq for target field coordinates, the exclusion survives every
birational target change with nonzero scalar constant Jacobian relative to
that fixed form. Only birational source coordinates, not finite source-field
extensions, are covered. Even rational constant-Jacobian representatives are
excluded at this area-form scope; polynomiality is not needed for the lemma.

## Independent proof audit

1. Resolve the multibranch point. Strict E attaches at least twice to the
connected exceptional tree over z. The path between attachments together with
E is a cycle; two contacts on one component give parallel edges. Global
irreducibility is essential. Strict E keeps its positive differential order.

2. For a blowup of a regular local form f dx wedge dy, the new exceptional
order is 1+mult_center(f), hence positive. Subsequent pullbacks remain regular
over z. All cycle components are positive. On a dominating common resolution,
additional blowups at cycle intersections insert positive-order components;
other blowups do not erase the cycle. The argument does not assume that a
positive exceptional curve has center outside the eventual affine source.

3. If omega=c du wedge dv and C(S)=C(u,v), resolve the birational identification
with P2_(u,v). Its standard form has divisor -3L_infinity. A positive curve on
the common resolution cannot dominate a P2 curve, since noncontracted prime
valuations preserve differential order, while target orders are0 or-3.
Every cycle component is therefore exceptional. Intersecting contracted
curves have the same image, so the connected cycle lies in one point-fiber.
Factorization into point blowups makes that exceptional dual graph a tree.
This gives the required contradiction, including after arbitrary further
common-resolution blowups. The proof uses the whole cycle, not a componentwise
boundary claim.

4. Resolve normal X away from the smooth neighborhood of x. Pullback of eta
is regular near x. At the generic ramification valuation, characteristic-zero
ramification gives ord_E(pi*eta)=e_E ord_D(eta)+(e_E-1)=e_E-1>0. The neighborhood
of y meets the generic point of its image curve D, so ord_D(eta)=0. The
multibranch germ persists. The surface result applies. A constant-Jacobian
representative after a scalar-constant target change would give exactly the
forbidden constant multiple of du wedge dv.

The standard imports are characteristic-zero surface/embedded resolution,
common resolution, point-blowup factorization, and the tame differential-order
formula. No new external source or source-proof audit is claimed.

## A5 application and comparison

The accepted [A5 FIRST](a5-pentagon-chart-review-swarmHQ-sol56-root-20261018T222155Z.md)
supplies the single irreducible two-branch ramification curve and smooth source
and target pentagon points. The new consequence applies only IF the chosen
target area form is regular and nonzero there. No global target coordinate pair
with that property is supplied. Completed local parameters are not silently
identified with global field generators. Arbitrary target Jacobian, finite
source enlargement, other covers and actual Keller normalization are not
excluded by this A5 application. JC2 and B=R remain unresolved.

The [older zero-free-model criterion](zero-free-branch-model-review-swarmHQ-sol-20260917T044800Z.md)
does not already establish this exact implication. It assumes a globally
zero-free target model with smooth branch components and then permits finite
source embeddings for polynomial landings. The new lemma uses a multibranch
positive-zero source curve at a pole-free point and requires a birational
source identification. Neither supplies the other's hypotheses. Novelty is
unknown; bounded historical discovery is not an absence certificate.

## Review custody and scope

ACK10:16:18 verified actual executable paths; partial10:17:22 and terminal
10:17:35 met original caps. Packet1--83 and all charged scientific bodies were
read whole:producer1--128 plus manifest,A5 producer1--127,A5 FIRST1--112,
zero-free FIRST1--67. Whole-set metadata matched before scientific body reads;
artifact_finalize verify passed. Fresh governing reads were frozen STATE1--254,
RUNBOOK1--434 and public APPROACHES1--941; other required governing whole-reads
were reused only at the reviewer's own complete matching pins. Postpins and
specified modes all matched. No reviewer deviations or unread charged scope.
ROOT's earlier display deviations are retained in the operational journal.
No reviewer writes,queries,network,CAS,Git mutation,model CLI,descendants or
protected-tree access. This is independent manual FIRST, not formalization.

OPEN(S) RAISED: None.

## COLLISIONS

status: EMPTY

- NONE -- no explicitly tagged OPEN entries are raised.

Corpus basis: 3832aae6d2da9d1564416bad66db9c1d3bfdf7dc (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6552`.
- Body SHA-256:
  `59c496f2db9693f8452032b827b6cbb1dd21ca8c8f3832dd876630a0e0af25e5`.
- Frozen basis: `3832aae6d2da9d1564416bad66db9c1d3bfdf7dc`.
