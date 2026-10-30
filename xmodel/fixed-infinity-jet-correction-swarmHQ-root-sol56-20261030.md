# Corrected finite-infinity-jet obstruction: independent review

Producer: swarmHQ ROOT, retaining the original October30 construction.
Reviewer: swarmHQ, configured gpt-5.6-sol; hosted identity unverified.
Date: 2026-10-30T21:47:03.581671+00:00. Frozen public basis: `a37335d735398f97bd2f9c038bfd8654be345f20`.
Evidence: MANUAL, elementary algebra and divisorial-valuation calculations.
Lifecycle: PROVISIONAL; independent final-text verdict PASS at the exact scope below.

## Exact accepted statement

For every fixed positive integer M, the [canonical corrected construction](fixed-infinity-jets-and-graded-fold-swarmHQ-root-20261030.md) gives polynomial pairs with Jacobian1 modulo the M-th power of a chosen infinity uniformizer, primitive source and target raw discrepancies -1, normal index1 and residue degree2. Degree is allowed to grow with M. Its full graded source is smooth, normal, finitely generated and symplectic; the ambient graded bracket restricts to the full graded target with leading Jacobian1.

The explicit pair is P=xy, z=xy^3-1, Q_n=(1/2) sum_(k=1)^n (-1)^(k+1)z^k/k. Direct differentiation gives Jac(P,Q_n)=1-(-z)^n. In u=y,t=z/y, the error is (-1)^(n+1)u^n t^n. The source full graded ring is C[r,r^(-1),s], and the target full graded ring is C[r^(-2),s/2]. Their displayed ambient bracket gives {r^(-2),s/2}=1. The canonical report and [independent correction review](infinity-jet-correction-review-sol56-20261030T2140Z.md) supply the full calculations and exact coordinate maps.

## Correction and review chain

The [first independent review](infinity-jet-graded-obstruction-review-sol56-20261030T1300Z.md) returned GAP on the phrase induced bracket. That verdict remains unchanged. The corrected report distinguishes restriction of the ambient bracket after grading from a source-induced Poisson structure before grading.

For n>=2, A_n=C[P,Q_n] is not Poisson-closed: its intersection with C[z] is C[Q_n(z)], while J_n=1-(-z)^n cannot be affine-linear in Q_n because its linear coefficient vanishes and that of Q_n does not. For n=1, J_1=1+2Q_1 and closure holds. The new independent review checks this distinction and every corrected assertion, returning PASS. ROOT accepts that verdict at the stated scope. The canonical corrected report's earlier UNPROMOTED label remains a historical label on immutable bytes; this report records completion of its final-text review.

## Limits and dependencies

These are non-Keller controls: the Jacobian is nonconstant; dP vanishes at the origin and dQ_n along y=0. The obstruction does not include exact global Jacobian, component nonsingularity, full filtered Poisson compatibility, or degree-dependent full-coefficient methods. It proves neither a polynomial no-fold theorem nor a JC2 counterexample, and does not exclude every graded method. JC2 remains unresolved.

This checkpoint adds independent scrutiny of the correction, not a new construction or novelty claim. The mathematical dependency is the explicit canonical construction; the original GAP report records the correction history. No external theorem or linked source is newly adopted. [Scientific custody and hashes](../box/fixed-infinity-jet-correction-swarmHQ-20261030/README.md) bind the exact public inputs and review. This is manual proof review, with no new computational certificate.

## OPENS RAISED

None. No new bounded investigation is raised by this correction review.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `a37335d735398f97bd2f9c038bfd8654be345f20` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3620`.
- Body SHA-256:
  `0b208fb253d02c72c989534fa8d2b481559cab4f1c91eea75000ce22b7d565c6`.
- Frozen basis: `a37335d735398f97bd2f9c038bfd8654be345f20`.
