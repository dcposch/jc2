# Rational cusp-avoidance: independent FIRST review and integration

Verdict: CONFIRMED / PROMOTED / MANUAL at the exact scope below.
Producer: native Astra plus swarmHQ ROOT.
Independent reviewer: native gpt-5.6-sol, message-only FIRST.
Review terminal: 2026-10-17 01:58:30 UTC. Integration: swarmHQ ROOT.
Public basis: fa6f3c67b85a2248f5645679bbd993e6032dcb30.
Operational admission: swarmHQ 5f5e6886db2c4e0c0976a6070c11a04c0a9ae615.

## Frozen producer and exact result

[Producer proof](cusp-avoidance-swarmHQ-astra-root-20261017T015255Z.md),
6161 bytes, mode444, full SHA256
344bd60956c8859fd06402d44211e0caf4229627d28ff82747f29b996c06c17b.
Its actual manifest is the same path with `.artifact.json` appended,
704 bytes, mode444, SHA256
b6376194e846d1cbc7d7897520e1ca80b83660dee99099568b65f716e7c7a4a9.
The original UNPROMOTED producer and seal remain unchanged. This independently
reviewed integration promotes only the following assertion:

Every closed irreducible rational dimension-one curve in A2 over C meets
the cusp q^2=p^3. There is no bound on the number of punctures of its affine
normalization. No novelty claim is made.

## Independent attacks and resolution

The reviewer checked that closedness handles all omitted normalization points:
on the projective normalization P1, if both p and q are regular, every defining
polynomial of D still vanishes after evaluation. Hence that point maps into D,
even if it was absent from a chosen rational parametrization.

With nonzero p,q and nonconstant R=q^2/p^3, put w=p^2/q. Then p=Rw^2 and
q=R^2w^3. Writing a=ord(w), the review independently checked all four cases:

- At an R-zero of order k, a<=-ceil(k/2); the next integer makes both
  k+2a and 2k+3a positive.
- At an R-pole of order l, a<=floor(2l/3)=l-ceil(l/3); the next integer
  makes both -l+2a and -2l+3a positive.
- At R=1, a<=-1, since otherwise both coordinates are regular and
  q^2-p^3=R^3*w^6*(R-1) vanishes.
- At all other unit values, a<=0 or both coordinates vanish.

These cases cover every point, with no implicit numerator-coprimality premise.
The sum of orders of w is zero and the sum of pole orders of R is d=deg(R).
Consequently 0<=d-sum ceil(k/2)-sum ceil(l/3)-n1<=d-n0-ninf-n1.
Here the n values count distinct points in the three specified fibres, not
ramification multiplicities. Separability and Riemann--Hurwitz give
2d-2 >= (d-n0)+(d-ninf)+(d-n1), so the divisor upper bound is <=-2.
Both the sign and the count were independently checked.

The reviewer also checked all degeneracies. For constant R=c not 0 or 1,
w must be nonconstant, and one of its zeros gives the origin. R=1 puts D
on the cusp. If one coordinate vanishes identically, the other is nonconstant
and one of its zeros gives the origin. Both coordinates constant cannot
parametrize a curve.

Counterexample controls: the locally closed rational curve q=0,p!=0 really
does avoid the cusp, demonstrating the necessity of closedness. The closed
rational curve pq=1 meets it at p^5=1. The disjoint nonzero fibres
q^2-p^3=c have smooth genus-one projective models, not rational ones.
No numerical or bounded-degree search substitutes for the proof.

## Consequence boundary

This is not an exclusion of all birational constant-Jacobian target repairs
of the cubic-cusp donor. It does not establish the needed geometry of pole
components, control a target change at the cusp's infinity, or handle all
branch components. It gives no general Keller-map normal form, finite-
normalization emptiness, or JC2 conclusion. The earlier affine-radial theorem
retains its unchanged-target-only scope. Positive characteristic is not covered.

## Review custody

Reviewer ACK/start01:57:39, terminal postpins01:58:30. The admission's original
partial02:06:20 and HARD02:16:20 were met early; no cap was renewed.
Whole-set pre-gate passed for ten governing files and the proof/actual manifest,
including regular-file, nonsymlink-ancestry, exact-hash and charged-mode checks.
Eight prior whole governing reads were reused after matching hashes. The changed
RESTRICTIONS186 and APPROACHES887 were read whole. The frozen Git blob
5f5e688:STATE.md was read whole, 410 lines/29855 bytes, SHA256
b517876a76a4d3c168127b5a63f54ca9e6f607ca46c2f49ca02e1487876ea483.
The producer was read whole, 126 lines including seal, and its actual manifest
was read whole. artifact_finalize verify returned VERIFIED. All ten governing
files, frozen STATE, proof, and manifest postpins matched.

The reviewer reports no deviations, writes, children, history/source expansion,
network, CAS/scientific subprocesses, cloud/paid CLI, adapter or protected-tree
access. ROOT's earlier oversized instruction displays are recorded in the
producer and operational journal; this review did not repeat them. No exit-price
declaration is appropriate: no exit price or Keller compatibility is asserted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4882`.
- Body SHA-256:
  `90631f57697b15daad6ae13c38f7a31acbc50fe93abf4e17da07339633599014`.
- Frozen basis: `fa6f3c67b85a2248f5645679bbd993e6032dcb30`.
