You are the hostile different-model reviewer for the producer-checked bounded
claim `AS3-MIN-W2 / W2-SURVIVOR`. Work in
`/Users/dc/code/math/jc2`. The producer is an OpenAI Codex session; you are the
required independent Claude/Fable reviewer. Write only
`xmodel/review-witt-oddprime-claude.md`. Do not edit source/data/shared ledgers,
use the network, launch W3, or broaden the support.

Read in full:

- `cases/round2_witt_oddprime/PREREGISTRATION.md`
- `xmodel/round2-witt-oddprime-20260824.md`
- every file in `cases/round2_witt_oddprime/`
- the exact pre-existing source claims cited in `provenance.json`, only as
  needed to audit that this is a new odd-prime/W2 test of an already typed
  Artin--Schreier control rather than an invented family.

Attack these clauses separately:

1. The cap was frozen before its computation and contains exactly `p=3`,
   `P_a=x+a*x^3`, `Q=y`, `a=1,2`, exact supports, and the fixed marked
   collision `(0,0),(1,0)->(0,0)`. `a=1` fails the collision; `a=2` enters.
2. At `a=2`, the special-fibre map has Jacobian exactly one, generic degree
   exactly three with basis `1,x,x^2`, separable derivative one, and the two
   distinct marked points collide. Do not infer degree from finite-point
   counting.
3. The Teichmueller lift of `2 in F_3` to `Z/9` is `8`. For
   `P~=x+8*x^3`, `Q~=y`, the divided error is `E=2*x^2 mod 3`; its top
   two-variable de Rham/Cartier class vanishes. Independently derive the
   correction equation and verify `A=0`, `B=x^2*y`.
4. The explicit lift
   `P2=x+8*x^3`, `Q2=y+3*x^2*y` has determinant
   `1+27*x^2+72*x^4`, hence exactly one modulo 9, and retains the same marked
   collision modulo 9.
5. Producer and independent replay implementations are genuinely separate
   enough for their stated checks, their canonical hashes/manifests are
   current, and `verify.py` passes from a fresh scratch replay.
6. The only conclusion is one explicit polynomial Keller-collision lift over
   `Z/9` for this fixed characteristic-three support. It is not a W3 or
   compatible all-Witt lift, not bounded-support persistence, not a Z_3 or
   characteristic-zero polynomial map, not a germ, and not a JC2
   counterexample. The new fact only refutes a blanket extrapolation of the
   characteristic-two Mondello-stratum first-Witt obstruction to all odd
   primes/supports.

Audit the preregistration timestamp correction and file hashes. Run all three
documented commands into a fresh `mktemp -d` where output paths permit; do not
overwrite frozen artifacts. Independently recompute the two-value census,
generic algebra, Teichmueller representative, error class, correction,
determinant, and collision without trusting producer verdict strings. Try to
find a sign/bracket-convention error, a restricted-correction-space mistake,
a misuse of the two-variable de Rham quotient, a marked-point lift failure, or
a hidden support/cap change.

Return exactly `CONFIRMED`, `CONFIRMED WITH GAPS`, `GAPS`, or `REFUTED`, with
the smallest failing identity if applicable. Put verdict and promotion guidance
near the top; record model/CLI/version, UTC, basis/dirty perimeter, exact
commands, artifact hashes, independent derivations, gaps, and scope.
