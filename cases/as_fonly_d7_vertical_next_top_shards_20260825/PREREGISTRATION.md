# Preregistered 27-way N12/N11 shard accelerator

The test and mathematical interpretation are identical to the frozen
monolithic runner `as_fonly_d7_vertical_next_top_carry_20260824`.  Only the
execution partition changes: structural bases are ordered lexicographically
and split into 27 contiguous intervals by integer endpoints
`floor(2187*i/27)`.

The runner executes the definition prefix of the source-hashed monolithic
compiler, ending immediately before its enumeration marker.  Every shard
then enumerates its assigned bases with the same row reduction, state order,
and exact F3 expression evaluator.  `N11` is tested directly because the
separately frozen source theorem proves that its six advertised degree-six
directions are Frobenius and hence absent.

Discovery outcomes:

- aggregate `N12=0`: obstruction at degree twelve for this finite branch;
- aggregate `N12>0,N11=0`: obstruction at degree eleven;
- aggregate `N11>0`: proceed to the separately preregistered degree-ten gate;
- any failed shard, range mismatch, source mismatch, timeout, or OOM: no
  verdict.

No recurrence, all-depth, characteristic-zero, no-lift, counterexample, or
JC2 inference is licensed.
