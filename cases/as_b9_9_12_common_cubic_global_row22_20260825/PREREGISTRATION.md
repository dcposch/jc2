# Preregistration — global `[x^2 y^2]` carry on the full family

Regenerate, from the independent common-cubic source, the complete
mod-`3^11` family above the one fixed B9 mod-243 parent.  Use its exact
17 active, 116 spectator, and 149 fresh coordinates, then choose canonical
RREF sections to expose a bijective

```text
17 active + 78 spectator-kernel + 55 fresh-kernel = 150 trits
```

parameterization.

First certify source-theoretically that the next fresh Jacobian row for the
determinant coefficient `[x^2 y^2]` is universally zero: every family member
has the same mod-3 reduction.  Evaluate its divided `3^11` carry on canonical
origin, signed basis, and deterministic mixed controls.  Any reported point
must replay all 299 parent rows literally modulo `3^11`.

If a carry-zero point is found, immediately solve all 299 next-digit rows and
literal-replay any mod-`3^12` lift.  Sampling proves only displayed witness
existence/nonconstancy, never the full zero locus or emptiness.  The exact
symbolic zero locus is a successor if the carry is nonconstant.

Execution is AWS-only with Linux/job-tag fail-closed guards.
