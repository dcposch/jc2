# Common-cubic pointwise lift gate from `3^11` to `3^12`

This case consumes the frozen normalized common-cubic witness and its exact
`299 x 149` integer Jacobian.  It solves the complete fresh-digit system over
`F3` and emits the full kernel/cokernel certificate.

The result is pointwise UNSAT.  A source-independent replay gives the minimal
reason: determinant row `[x^2 y^2]` has divided carry `1`, while all 149 fresh
columns are zero.  Fresh-fresh terms are multiples of `(3^11)^2` and vanish
modulo `3^12`.

AWS replay commands require the environment variables displayed in
`run_aws.sh`; the pinned matrix/witness hashes are recorded in the machine
results.  Campaign policy forbids substantive local replay.

This does not classify the complete `3^150` mod-`3^11` family.  The carry is
being globalized separately over that family.
