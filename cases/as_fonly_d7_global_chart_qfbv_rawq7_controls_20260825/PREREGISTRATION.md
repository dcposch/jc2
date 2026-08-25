# Preregistration — raw-Q7 global-chart controls and proof

Generate the predecessor formula by omitting only the terminal high loop from
the hash-pinned raw-Q7 producer.  Obtain a Boolector SAT model and replay its
13 Q9, 32 Q8, and 18 Q7 digits through the independent integer source; require
recursive/literal determinant agreement and a nonzero terminal row.

For the full formula, deterministically apply Z3 4.16
`simplify -> bit-blast -> tseitin-cnf`, emit DIMACS, run CaDiCaL with a textual
DRAT trace, and require an independent `drat-trim` verification.  All input,
output, source, solver, proof, and checker hashes are load-bearing.

