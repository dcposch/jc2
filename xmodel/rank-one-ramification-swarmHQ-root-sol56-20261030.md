# Local rank-one ramification lemma: reviewed integration

Producer: swarmHQ (ROOT; main configured gpt-6-astra, hosted identity unverified).
Independent hostile reviewer: swarmHQ (configured gpt-5.6-sol, hosted identity unverified).
Date: 2026-10-30T17:22:15.721169+00:00
Basis: 5ed1dba19564865a10dee632055fca07110f969f
Evidence tier: MANUAL, relative to the named standard analytic foundations below.
Lifecycle: PROVISIONAL. Independent verdict PASS at the exact local scope; no novelty claim.

## Evidence and exact scope

The mathematical excerpt below is byte-identical to lines7–53 of the [sealed author candidate](../box/rank-one-ramification-swarmHQ-20261030/author-candidate.md). The [sealed independent review](rank-one-ramification-review-sol56-20261030T1710Z.md) checks each step and the finite rank-zero scope control. The candidate's original UNREVIEWED label records its earlier status and remains unchanged. This integration introduces no new mathematical claim or stronger application.

## Statement

Let f:(S,p)->(T,q) be a finite holomorphic map of smooth complex surface germs.
Suppose the reduced ramification divisor near p is a single smooth curve E, and rank(df_p)=1.
Then E maps unramifiedly to the normalization of the image branch f(E) at the point over q.
Here unramified means local parameter order one; it does not assert that f(E) is smooth or immersed in T.
The standard existence and local-parameter description of finite normalization of a complex curve germ are used.

## Proof

Choose a target coordinate P whose pullback has nonzero differential at p, and use p=P as a source coordinate with a second coordinate v.
Write the other target coordinate as Q(p,v). If P restricted to E has nonzero differential, its order one already proves the claim.
Otherwise, smoothness of E makes E a graph p=h(v) with h(0)=h'(0)=0.
If h were identically zero, the ramification identity Q_v=p^k U(p,v), k>=1 and U a unit, would make Q(0,v) constant.
Then f would contract E, contradicting finiteness. Thus ord(h)=m is a finite integer at least two.
A change of the source coordinate v by an invertible holomorphic germ puts h(v)=v^m.
Because the ramification support is exactly E, in these coordinates

    Q_v(p,v) = (p-v^m)^k U(p,v),   k>=1,   U(0,0)=c != 0.

Subtract the target function B(P), where B(p)=Q(p,0). This is an invertible local change of the second target coordinate.
Consequently, on E,

    (Q-B(P))|E = integral from 0 to v of (v^m-s^m)^k U(v^m,s) ds.

Give p weight m and v weight one. The constant term c of U contributes

    c * v^(mk+1) * integral from 0 to 1 of (1-s^m)^k ds.

The displayed integral is a nonzero rational number (it is positive for these positive integers m,k).
Every remaining monomial of U has positive weight and contributes strictly higher order in v after integration and substitution p=v^m.
Thus the restrictions of P and Q-B(P) to E have respective orders m and mk+1.
If the map E->normalization(f(E)) had local parameter order delta, the orders of all pulled-back target functions would be multiples of delta.
Therefore delta divides both m and mk+1. Their greatest common divisor is one, proving delta=1.

## Rank zero is not automatically excluded

The finite polynomial map

    P(u,v)=v^2+u^3,   Q(u,v)=2v^3+3u^3*v

has determinant 9u^5, hence smooth reduced ramification curve E={u=0}, but its differential has rank zero at the origin.
Finiteness follows directly from v^3-3Pv+Q=0 and u^3=P-v^2: both source coordinates are integral over C[P,Q].
The restriction E->f(E) is v->(v^2,2v^3), whose normalization parameter is v; this example does NOT refute the proposed unramified conclusion at rank-zero points.
It refutes only the shortcut that smooth ramification support forces rank one.
It is not an actual Keller normalization with a whole omitted-boundary complement A2: its complement S\E is Gm x A1.
No family search or CAS was performed.

## Dependencies and prior work

The proof uses standard complex-analytic facts: the holomorphic coordinate/implicit-function theorems; factorization by the reduced equation of a smooth divisor in a regular analytic local ring; analytic roots of units; finiteness implying zero-dimensional fibres; existence and universal property of normalization of a reduced curve germ; and the DVR order formula under a finite map of smooth curve germs. These are identified foundations, not a new literature audit.

The earlier campaign results on smooth omitted curves do not supply smoothness of the ambient normalization or rank one at every point. The historical DC2-REVIEW body remains unread after its seal failure; priority is unassessed. No paper theorem is newly adopted here.

## Reviewed limitations

- The smoothness of both surface germs, the single smooth reduced ramification component, and rank one at the point are essential premises of this proof.
- It does not treat a singular normalization surface, a singular reduced ramification support, or a rank-zero point.
- Parameter order one over the normalized image does not say that the image is smooth or immersed in the target.
- A pointwise rank-one lemma is not a theorem that an entire omitted curve has degree one. No global attachment, properness, boundary-degree, corank-zero, Keller, N=1, or JC2 conclusion follows.
- The polynomial example is not a Keller map and its complement is `G_m x A^1`; it is only a finite local/global scope control.
- Review was manual and packet-confined. No CAS, scientific computation, source query, or new control search was performed.

## Collisions and novelty

Outside-packet search was not authorized. The stopped historical DC2-REVIEW body was not supplied or read, so novelty and historical priority remain unassessed.

## Replay and negative controls

Desk-only. The proof uses the orders m and mk+1. The finite polynomial control and its monic integrality relations are included verbatim above and were independently recomputed manually. There was no CAS or family search. See the [artifact README](../box/rank-one-ramification-swarmHQ-20261030/README.md) and SHA256SUMS for exact report custody. The positive rational quantity is the real integral; multiplying it by a nonzero complex constant gives a nonzero coefficient.

## Limitations and next test

Rank-zero smooth-source points and singular normalization points remain untreated. A subsequent investigation must state a separate bounded local implication and check compatibility with the whole Keller source before making a global deduction. No new research lane is authorized by this publication.

## OPENS RAISED

None. The existing local and global gaps are retained without a new named OPEN entry.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `5ed1dba19564865a10dee632055fca07110f969f` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6883`.
- Body SHA-256:
  `7be35e0897dff1e455be4116dceec01daedfa778947865ff7cab0b48d03c2013`.
- Frozen basis: `5ed1dba19564865a10dee632055fca07110f969f`.
