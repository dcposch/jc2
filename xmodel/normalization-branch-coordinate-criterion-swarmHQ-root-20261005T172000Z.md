# A coordinate-fiber branch criterion for a plane Keller map

Producer: swarmHQ (Opus 5.5 criterion; ROOT, gpt-6-astra, shorter proof and exposition).
Date: 2026-10-05 UTC.
Basis: 5adf3d823e9f4ddb0108b4d0ca41d98b0646d010.
Evidence tier: MANUAL mathematical argument with named classical imports.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; novelty UNKNOWN.
JC2 remains unresolved.

## Statement and scope

Let F:A2_C -> A2_C be a polynomial map with nonzero constant Jacobian.
Let L/C(u,v) be its finite function-field extension, of degree N, and let
pi:Y -> A2_C be the finite normalization of the target in L.
Zariski's Main Theorem identifies the actual source U=A2_C with an open
subset of Y. Let D=Y-U and S=pi(D). Let B be the branch curve of pi.

**Sufficient criterion.** If B is contained in finitely many fibers of a
single polynomial coordinate p on the target, then F is an automorphism.

Here p must belong to a polynomial coordinate system (p,q), not merely be
an arbitrary polynomial. B is the branch curve of the FINITE normalization
map, not a branch locus of F (which is etale). B can be smaller than S:
omitted unramified divisors contribute to S but need not contribute to B.

No assertion is made that an arbitrary Keller map has this branch geometry.
This is a sufficient condition, not a proof of general JC2.

## Dependencies and prior work

Named inputs: finite normalization and the open immersion from Zariski's Main
Theorem; purity of the branch locus over the smooth target; triviality of
connected finite etale covers of A1_C; connectedness of a generic fiber of
a Keller coordinate; and the birational Keller theorem. These are inherited
classical inputs, not newly source-audited in this note. A target automorphism
(p,q) preserves the Keller condition, so the connectedness input applies to
P=p composed with F.

The [current frontier](../APPROACHES.md) retains the global properness gap.
Related historical arguments include the
[coordinate-fiber connectedness review](block-descent-a1-fibre-connectedness-hostile-review-grok46-20260831.md)
and the [proper rank-four branch-topology analysis](block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md).
The first concerns its explicitly specified rational affine surface and constant
bracket; the second concerns proper rank-four blocks and additional Euler
hypotheses. Neither is silently substituted for the present statement.
A bounded comparison of those two bodies did not establish novelty or exhaustive
absence of an earlier proof. In particular, this note makes no priority claim.

Opus supplied a product-cover/normalization argument for the criterion.
ROOT supplied the proof below after the independent assessments. A retained Astra
hostile reviewer checked the scoped criterion and this replacement argument.
That is different-model review of the Opus-origin claim, but same-model review
of ROOT's replacement proof. These particular exposition bytes have not received
separate different-model review; no promotion is claimed.

## Argument

Choose a generic value a and the coordinate line L_a={p=a} such that:

1. L_a avoids B.
2. L_a is not the image of any omitted divisor D_i.
3. P^{-1}(a), where P=p composed with F, is connected.

These choices are compatible. The first excludes finitely many values by the
hypothesis. For the second, only those finitely many D_i whose image is a fiber
of p exclude values; an image not contained in such a fiber cannot equal L_a.
The third holds on a nonempty Zariski-open set by generic connectedness.

Purity implies that Y_La -> L_a is finite etale of degree N. Since L_a is
isomorphic to A1_C, it is the disjoint union of N copies C_1,...,C_N of A1_C.

Every C_i meets U. Otherwise C_i lies in the omitted set D, and, being an
irreducible curve, it lies in an omitted divisor D_j. Both have dimension one,
so they coincide as underlying closed curves. Finiteness then gives
pi(D_j)=L_a, contrary to the choice of a.

Consequently
P^{-1}(a) = U intersect Y_La
is the disjoint union of the N nonempty open curves U intersect C_i.
Each is open and closed in that fiber. Its connectedness forces N=1.
Thus F is birational; the birational Keller theorem makes F an automorphism.

Notice that the proof does not require a description of horizontal omitted
divisors or the stronger equality B=S. Nor does it claim connectedness for
every special fiber.

## Replay and negative control

Desk-only; no CAS, numerical test, finite search, or new computational artifact.
The standard map (s,t) -> (s^2,t) has a coordinate-line branch curve but Jacobian
2s, and a generic first-coordinate fiber has two components. It demonstrates
why the Keller/connected-fiber hypothesis cannot simply be dropped. It is not a
Keller counterexample.

Related historical bodies, read at the frozen basis above:

- Connectedness review: SHA256 e87d0af3fb433edc5056ff651ce8623aae840bfb962d7d08eba6588b970123ca.
- Rank-four analysis: SHA256 768cf08fe2be7a72e9e17cd15acd56976b6743cefa293bf11472a4fb4e701805.
- Campaign fallacy contract, FALLACY-v2.md: SHA256 e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

## Limitations and next test

The unresolved implication is a useful restriction on the branch curve of an
ARBITRARY hypothetical noninvertible Keller map. This proof does not supply one.
It authorizes neither a new branch-configuration catalogue nor a claim that
all counterexamples have been excluded. A genuinely changed global argument,
rather than another proof of this sufficient criterion, would change the next
research decision.

## OPENS RAISED

None. No new bounded research task or computational successor is commissioned.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `5adf3d823e9f4ddb0108b4d0ca41d98b0646d010` (Git blobs only).

This mechanical result is not an exhaustive theorem search or a novelty finding.

## Completion

Whole author readback completed before the measured author-completion clock:
2026-10-05 17:23:21 UTC.
Named input scopes and limitations are unchanged. No claim promotion or
general JC2 resolution follows. Trusted publication custody follows this marker.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6240`.
- Body SHA-256:
  `45eba692b6e3bd925b82f2fd789af3d298272b3be3f2429edc5f11837c1e7a14`.
- Frozen basis: `5adf3d823e9f4ddb0108b4d0ca41d98b0646d010`.
