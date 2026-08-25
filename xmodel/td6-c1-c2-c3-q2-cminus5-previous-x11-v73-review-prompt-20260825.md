# Hostile-review charge: TD6 V73K `C=-5U^2,V=0,D(U)`

Act as an adversarial algebraic referee.  Inspect, but do not modify or
execute, these frozen surfaces:

- `cases/td6_c1_c2_c3_q2_cminus5_previous_x11_v73_aws_20260825/`
- `xmodel/td6-c1-c2-c3-q2-cminus5-previous-x11-v73-aws-20260825.md`

The claimed theorem is narrow: in the fixed source-typed normalized A3
section with `q_beta=t+beta*t^2+t^25`, the original TD6 source-row system is
incompatible on `V=0,C=-5U^2,D(U)` for every beta.  No endpoint, whole-B3,
whole-A3, TD6, SP-2, landing, or JC2 conclusion is claimed.

Audit these load-bearing points independently from the readable source and
evidence, treating stored PASS strings as non-authoritative:

1. Source typing and provenance: fixed p-boundary/dead-stretch/F1/pole data,
   raw line `V=0,C=-5U^2`, and no illicit weighted scaling.
2. The hash-pinned parent-compiler interception: exactly one intended outer
   range is changed; inner ranges are delegated unchanged; all twelve
   original previous rows `('X-1',0..11)` are reconstructed.
3. Direct `q_beta'=1+2 beta t+25 t^24` is retained in the theorem run and its
   degree-11 contribution is the full `4*beta*f2[10]`.  Distinguish the
   separate omit-q-prime control from the theorem run.
4. The dependent `('X-1',11)` residual is beta-independent, with numerator
   support only `U`, no residual denominator, inverse denominator only `U`,
   and normalized target `-1` on `D(U)`.
5. Source ancestry: previous left-null combination, exact first-stage
   division, lift to thirteen original first rows, one complete original
   previous-plus-first convolution, and scalar normalization.  Check signs
   and that no reduced/echelon row is silently treated as original.
6. The omission, plus-one, and wrong-row controls.  In particular, decide
   whether the lexicographic exponent-vector leading-monomial argument is a
   valid integral-domain certificate that the omitted full convolutions
   would have nonzero deltas.
7. Completeness of the numerator/denominator and leaf-denominator ledgers;
   confirm that only `U` is localized.
8. Dual-host custody: after excluding only host/run/path provenance lines,
   all theorem output lines agree and the four theorem artifacts are
   byte-identical.  Verify the manifest/freeze design by reading it; do not
   run shell or producer code.

Return numbered findings with severity, the strongest exact claim you can
confirm, every required repair, and one final standalone verdict line chosen
from:

`CONFIRMED`

`CONFIRMED_WITH_REPAIRS`

`NOT_CONFIRMED`
