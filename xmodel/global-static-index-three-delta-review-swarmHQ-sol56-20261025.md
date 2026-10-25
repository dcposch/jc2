# Final artifact review: global static index-three target

Reviewer: configured Sol5.6 role; actual hosted identity and cost unmeasured.
Date: 2026-10-25 UTC
Basis: `b5adaf24e054df24d360ad301ab34044ce5b9c45`
Verdict: **CONFIRM_EXACT_PUBLIC_PACKAGE**
Lifecycle: final publication review; ROOT alone records promotion.

## Artifact checked

I reviewed the complete canonical producer
[`global-static-index-three-swarmHQ-root-astra-20261025.md`](global-static-index-three-swarmHQ-root-astra-20261025.md),
full SHA-256 `2df3edcab7d261d8fb08e2223a87333bfb1215d69bd5c03c72f749492c0233b8`,
body SHA-256 `e6bbe260ffb898a63ce1ca80b1bdffd15924d2c9ff1627fb1e145e4673771409`,
at artifact basis `318c2eb42c209b13915527794d5f1fa8faf58721`. Its manifest verified before
the body was read. The six mathematical sections preserve the HQ-reviewed proof.

## Mathematical preservation

The weighted hypersurface is a normal projective surface and its `T != 0` chart is the
entire marked `A^2`. The only nontrivial stabilizer chart is the index-three quotient at
`q=[0:0:1:0]`. Taking invariants in the actual reduced boundary ring gives
`C{s^2,s^3}`, so `B` is scheme-theoretically an ordinary cusp.

The marked form has divisor `-B`; reflexive extension yields the genuine identity
`omega_S=I_B Omega`. The residue generator on the index cover has character one,
and the unit argument proves exact canonical and boundary Cartier index three without
assuming the cover rational. Rationality of `S` follows separately from projective duality,
rational-resolution cohomology, and Leray.

Localization and the local Cartier criterion give `Cl(S)=Z[B]` and `Pic(S)=Z[3B]`.
The weighted-Proj multiple proves `3B` ample, while the boundary-normalization transition
has degree one, giving `B^2=1/3`. Resolving the marked boundary birational map supplies
the common static boundary model and integral dual class of square three.

## Ledger and scope check

The complete proposed APPROACHES/PROGRESS/AUDIT patch passed `git apply --check` against
the unchanged public ledgers and was not applied by this reviewer. Its mathematical claims,
links, hashes, lifecycle language, and qualifications match the producer and prior gate.
It correctly says that the common static boundary resolution exists while no simultaneous
actual finite `h`/proper `k` pair is supplied.

This one target excludes only a static index-one/Gorenstein shortcut. It provides no
unbounded family, universal index bound, iterate, Keller eigenvaluation attachment,
polynomial Keller pair, properness or descent theorem, or JC2 solution. The producer's
metadata-display/partial-response recovery qualifications and the prior review's corrected
task/entry LF accounting remain disclosed; this gate does not erase them.

## OPENS RAISED

None. The existing actual-map and infinitely-singular gaps remain at their prior scopes.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `b5adaf24e054df24d360ad301ab34044ce5b9c45` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3065`.
- Body SHA-256:
  `b8bea5419f3a37e7b84bca75a9b801ce74052f4106ea75c922554c3a29245f57`.
- Frozen basis: `b5adaf24e054df24d360ad301ab34044ce5b9c45`.
