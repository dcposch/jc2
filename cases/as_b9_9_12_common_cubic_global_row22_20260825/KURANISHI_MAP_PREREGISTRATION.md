# Preregistration — exact 176-coordinate predecessor Kuranishi map

Use the frozen constant `205 x 55` fresh block (rank 29, kernel 26) and
its canonical `176 x 205` left quotient.  Parameterize the complete
predecessor family by the reviewed canonical coordinates
`17 active + 78 spectator-kernel = 95` and set the final fresh-kernel
particular to zero, which is licensed after applying the left quotient.

Compile every one of the 176 quotient coordinates directly from the literal
299-row integer source circuit, using arithmetic modulo `3^12` and explicit
division by `3^10` and `3^11` only after the corresponding divisibility rows.
The modular circuit, not an interpolated polynomial, is the arbiter.

Construct deterministic overlapping row blocks on Box02, Box03, and r6d.
All blocks consume one pinned family source and one pinned quotient payload;
overlap-coordinate structural hashes must agree byte for byte.  The aggregate
formula includes all 176 coordinates.  A SAT model must be decoded through
the original integer evaluator, solve both remaining affine fibres, and
literal-replay all 299 equations modulo `3^12`.

Degree firewall: the source residual has determinant degree two and common
core degree four, but canonical ternary lift/carry gates may increase the
ordinary reduced F3 ANF degree.  No quadratic/quartic ANF bound is assumed.
Any later expanded ANF must carry an exact source proof or exhaustive
functional equality certificate.  The 447 sampled predecessor controls are
validation and elimination-order evidence only.
