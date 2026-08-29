# V26R1E ideal-zero validator erratum

Status: `REPLAY_VALIDATOR_FAILURE_PRESERVED_NO_THEOREM`.

R1E correctly reconstructed `G=std(Graw)` and computed the reverse-inclusion
normal forms `JNF=reduce(J,G)`.  It then compared the multi-entry ideal `JNF`
directly with scalar `0`.  Singular treats a zero ideal with several stored
slots as non-equal to scalar zero, just as it treats a multi-column zero
matrix.  The run failed closed at `SERIALIZED_REVERSE_INCLUSION`.

An additive diagnostic iterated over every stored entry of `JNF`: all were
exactly zero (`JBAD=0`), after which both the recomputed-standard-basis marker
and final replay marker fired without a standard-basis warning.  This
diagnostic is not itself consumed as the theorem run.

R1F replaces the reverse-inclusion scalar comparison with an entrywise loop.
For completeness it also makes the `I6(A)=0` and `I5(A) nonzero` preconditions
entrywise, eliminating all remaining ideal-to-scalar zero tests.  No source
polynomial, ideal, matrix, minor, field, algorithm, resource cap, rollback
tag, or endpoint changed.

R1E supplies no grade-seven stratum, jet, arc, closure, or JC2 theorem.
