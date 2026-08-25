# Preregistration — global-chart source and proof controls

1. Omit only the terminal high rows from the pinned global-chart compiler.
   Require SAT and directly replay Q9, Q8, and Q7 from the integer source.
   This is the positive control that the predecessor chart was not accidentally
   made empty by the symbolic construction.  A system-Z3 timeout/UNKNOWN is a
   negative engine control; a Boolector model is parsed independently and
   replayed from the integer compiler.
2. Parse the exact pinned full SMT2 with Z3 4.16, normalize constant unsigned
   remainders with `simplify`, then apply `bit-blast` and `tseitin-cnf`; pin all
   hashes/counts.  A direct `bit-blast` attempt is retained as a fail-closed
   negative control because Z3 rejects unreduced `bvurem` nodes.
3. Run CaDiCaL with textual DRAT output and its internal proof checker, then
   replay the proof with an independently built `drat-trim` binary.

The checked certificate proves only the DIMACS instance.  The source theorem
also depends on the audited deterministic SMT-to-CNF transformation and the
integer-source equivalence checks.
