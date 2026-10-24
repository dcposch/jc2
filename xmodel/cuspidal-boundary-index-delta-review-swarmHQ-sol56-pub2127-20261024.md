# Delta review: cuspidal boundary and conditional index bound

Reviewer: swarmHQ, explicitly configured gpt-5.6-sol; hosted identity and cost unmeasured.
Reviewed contribution: `5052910d05fe7a2037d50b7bf2453a5898c2cbe6`.
Reviewed artifact SHA-256: `1e698be5889d651cbe71d3c01670ac3811680487fb0fbb679e73f248f9338f4b`.
Evidence: MANUAL frozen-public-artifact delta review.
Lifecycle: REVIEWED / UNPROMOTED; ROOT controls promotion.

## Verdict

`CONFIRMED` at the exact conditional scope printed in the contribution. The
public artifact faithfully incorporates the reviewed HQ candidates and makes no
stronger claim. In particular, the ordinary cusp is intrinsic to the boundary
curve, the index inequality requires extra ambient smoothness, and the
source-direction map is not the missing descent.

This is not a fresh blind mathematical review. It reuses the complete prior Sol
reads at their frozen hashes. The earlier noncanonical governor display,
history-row-limit, and verdict-exposure qualifications remain in force.

## Scope audit

Under all hypotheses of the published finite-factor theorem, the compact-support
and normalization argument correctly proves that `B` and `C` have rational
normalization and one intrinsic ordinary cusp. It does not prove that the normal
surface `Y` is smooth at that point.

The proper image graph correctly gives the source-direction proper birational map
`k:W->Y`, identity on `U`, and the arithmetic-genus argument makes `k|C` an
isomorphism. Exceptional curves must meet `C`, but the construction neither
eliminates them nor descends `h`; descent would require `k` itself to be an
isomorphism.

Only after adding smoothness of the target surface at the cusp does the cyclic
local reduction apply. The intermediate hypersurface is normal and the finite
trace argument transfers rationality. The weighted modification produces a
genus-one exceptional curve for `d=e/m>=6`, contradicting the required higher
direct-image vanishing, so the exact conclusion is `e<=5m`.

The report explicitly states that `m` is not uniformly bounded. For iterates it
only obtains `N^j<=5m_j` when the target is smooth at the cusp. The weighted
source-modification diagnostic has unbounded Cartier index but no required finite
map `h` and no global Keller source, so it is not a counterexample to an
actual-map bound.

The contribution also preserves the remaining exclusions: it proves no vanishing
of `R`, equality `W=Y`, properness, finite self-germ, all-Keller attachment,
infinitely-singular coverage, or JC2 conclusion.

## Replay

Desk-only delta replay. The producer manifest and canonical seal were verified
before all 156 report lines were read. I compared the final exposition against my
complete retained reads of the 108-line finite-ramification candidate, 66-line
projection, 37-line cusp delta, and 125-line finite-factor producer. No source,
new history query, computation, or new mathematical branch was used.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `5052910d05fe7a2037d50b7bf2453a5898c2cbe6` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3171`.
- Body SHA-256:
  `591b1ebf88afd768ab09a1c52efa82cc3edfa221958b22cbd5d6cf005761b10f`.
- Frozen basis: `5052910d05fe7a2037d50b7bf2453a5898c2cbe6`.
