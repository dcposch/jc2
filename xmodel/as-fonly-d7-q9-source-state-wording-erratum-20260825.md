# AS F-only D7 Q9 source-state wording erratum

Date: 2026-08-25.  This note does not modify the frozen producer package.
It records the two non-mathematical attribution corrections found by hostile
review
`xmodel/as-fonly-d7-q9-source-state-review-claude-20260825.md`
(SHA-256
`ab0c98be9a5793213d2273695162b29f7391837f83d445d38ac016ffe21cee0c`).

1. The producer report says the compiler “proves” that the six current
   degree-six Frobenius coefficients are spectators in the four new Q9 bands.
   The claim is true, but the new-band compiler does not assert it at runtime.
   Its proof is the typed-support argument: those coefficients occupy
   Frobenius positions, their derivatives are multiples of three, and their
   only possible new-row occurrence dies modulo three after the relevant
   division.  Promotion must cite that argument, not a nonexistent runtime
   check.
2. `RESULT_README.md` attributes integrality of `M_9/3` to the corrected-Q10
   predecessor.  More precisely, it is enforced by the inherited D98
   degree-nine rows, for which `KFdiv_9=0`; the corrected-Q10 row adds no
   degree-nine condition.  The per-state exact-division assertion remains a
   valid execution check.

Neither correction changes a source row, division, state coordinate, rank,
census, witness, manifest, or theorem scope.  Frozen bytes remain immutable.
