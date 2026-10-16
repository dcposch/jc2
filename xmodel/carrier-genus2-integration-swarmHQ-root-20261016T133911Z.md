# Carrier genus-two submersion: proof and independent-review integration

Claim: CARRIER-GENUS2-SUBMERSION-1.
Evidence tier: PROVED (explicit hand algebra and standard smooth-curve theory).
Lifecycle: PROMOTED at the exact three-claim scope below.
Producer: swarmHQ ROOT coordinator (Astra-assigned main session).
Hostile reviewer: native gpt-5.6-sol-assigned seat
`/root/carrier_pencil_review_sol56_0623`; integration: swarmHQ ROOT.
Assigned model identities were not independently attested by a hosting provider.
External novelty: UNKNOWN; no claim of a new polynomial or general classification.

## Exact result

In R=C[U,V], put c=UV^2, p=UV^3-V and B=C[U,UV,c,p]. The fixed polynomial

    f=p^4+(1/3-3c)*p^2+3*c^2-2*c-1-U

has all three properties:

1. f belongs to B and has no critical point anywhere on the affine source plane.
2. Its geometric generic fibre is integral and has genus two.
3. No rational q in C(U,V) satisfies J_(U,V)(f,q)=kappa for any nonzero constant kappa.

This refutes the proposed implication that a nonsingular scalar polynomial in
this marked carrier ring must have rational generic fibre. It is NOT a Keller
pair or a JC2 counterexample. It excludes only this fixed scalar as a component
of a rational constant-Jacobian pair, not arbitrary pairs in B. Positive genus
alone does not prove claim3; the specific differential and its poles do.

## Frozen proof and dependency scope

The complete [producer proof](carrier-genus2-submersion-swarmHQ-root-20261016T132711Z.md)
and its [manifest](carrier-genus2-submersion-swarmHQ-root-20261016T132711Z.md.artifact.json)
are unchanged. Their original MANUAL / UNPROMOTED header records the stage at
freezing; promotion is recorded by this separate integration and AUDIT.md.

- Contribution commit: c8d790e2a392d5779500e311ffe30ffa4ad3648b.
- Producer's frozen prior basis: 8926458541ce2ed2bb8729223f2478c5c81fd24a.
- Report: 5522 bytes, mode0444, full SHA256
  934a82b0941992c894c68cb6a79e31a879d63ea279dc5758cc565a8d289d6d56.
- Body: 5190 bytes, SHA256
  ca1f1bf20e621657e3bc47259fd4dc1b2c782cc7b1f29c27109b0b87ae93a6cd.
- Manifest: 714 bytes, mode0444, full SHA256
  fd8a83892a559541c4b9cb93de4491c908de4319fdcc3b167bd816ff718ae29c.

The proof uses explicit coordinate identities, the genus formula for a squarefree
degree-six hyperelliptic curve (Riemann--Hurwitz), and characteristic-zero pole
orders of exact differentials. A nonconstant rational function with one simple
pole has degree one to P1 and therefore cannot exist on a smooth projective
genus-two curve. No external unreviewed theorem, CAS result or formal certificate
is imported. The carrier is specified as an actual subring, not identified by
matching notation on an unrelated surface.

## Independent hostile review: CONFIRMED

The reviewer recomputed the following rather than relying on the producer verdict.

- On V!=0, g=1/V and r=p-g give inverse U=g^2+g^3*p, V=1/g, c=1+g*p.
  Substitution yields G(r,p)=p^2/3+r*(r^2-2)*p-r^2, on p-r!=0.
- The critical equations give p=3r-(3/2)r^3 and
  G_r=-(r/2)*(3r^2-4)^2. All simultaneous zeros have p=r, outside that chart.
  On the omitted line V=0, f_U=-1. Thus no affine critical point is missed.
- With H=2p+3r*(r^2-2), the generic equation is
  H^2=9r^6-36r^4+48r^2+12t. Its derivative is 6r*(3r^2-4)^2;
  possible common roots have value12t or64/3+12t, nonzero in C(t).
  The geometric generic curve is integral, with six simple finite branch points
  and two unramified infinities, hence genus two. The exceptional chart supplies
  no additional generic component.
- The volume sign is dU wedge dV=(r-p)*dr wedge dp. A rational mate would require
  dq=kappa*eta, where eta=3*(p-r)*dr/H.
- Eta is regular at all finite points, including branch points. At s=1/r=0,
  its coefficient of dr is -s^2+O(s^4) on the positive H/(3r^3) branch and
  3+s^2+O(s^4) on the negative branch. Thus it has exactly one double pole.
  Any rational primitive would have exactly one simple pole, a contradiction.
  Working in the full generic-fibre function field covers every rational q,
  not just polynomial q or a chosen denominator class.

The final verdict was CONFIRMED for all three claims, with no correction or gap.
The reviewer explicitly rejected stronger readings concerning all B-pairs or JC2.
ROOT independently checked the complete producer proof, including its seal, and
matching report/manifest posthashes. The negative-control role is the example
itself: nonsingularity and carrier membership hold, while rationality fails.

## Custody and review limits

The producer was canonically finalized before invitation. Both parties used the
whole-set metadata gate, manifest-first read, canonical verification, complete
report read and postpins. The review used no CAS, external source, write or new
family. Staged verification matched the producer report and manifest before banking.
Initial mathematical review consumed frozen canonical bytes before the contribution
commit was created; commit linkage was checked separately against those same pins.
This does not retroactively turn the initial review into a commit-before-review
workflow. Coordinator navigation/display deviations are retained operationally;
no blanket protocol-compliance claim is made. They do not alter the mathematical
scope or the exact report that the reviewer checked.

## Consequence for the current question

The open question remains whether B contains an arbitrary constant-Jacobian pair,
or whether such pairs with finite Spec(B)->A2 can be excluded. This fixed example
neither answers that question nor produces finite normalization/surjectivity.
The earlier pencil and extreme-weight constraints keep their separate scopes.
The useful elimination is the stronger scalar-only rational-fibre shortcut.
No further source/control family or degree search is claimed as a consequence.

## OPEN(S) RAISED

None. The existing all-pair question is unchanged, not renamed as a new task.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `8926458541ce2ed2bb8729223f2478c5c81fd24a` (Git blobs only).

This is a lexical no-new-OPEN result, not an exhaustive novelty or duplication audit.
The collision block is supplied here for the completed contribution rather than
retroactively inserted into the frozen producer proof.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6375`.
- Body SHA-256:
  `27e93a62fdda8cbe9d1565713588938b8628e9db0e1932e416f02119d3afc79a`.
- Frozen basis: `8926458541ce2ed2bb8729223f2478c5c81fd24a`.
