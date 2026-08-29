# V82QS preregistration — single-q current-adjoint shards

The dual 22-axis V82Q monoliths are exact and CPU-active but have spent more
than three hours in the current stage.  This bounded latency repair partitions
the same licensed q inventory into 22 one-axis staged replays, split 11/11
between Box03 and r6d.  It does not replace the monoliths: their eventual
dual-host table remains the aggregate authority, while the shards give early
per-axis current coordinates and an exact union control.

Each shard independently rebuilds transport, FIRST, previous/pole, and
current from the original source, retains the q-boundary singleton and direct
q-prime omission controls, and emits the complete one-column current
conormal table.  The source is the reviewed V78C single-q compiler, now run in
`staged` rather than `p12` mode.  Its inherited V78C banner is historical;
the wrapper prints a V82QS current-shard banner and pins the compiler SHA-256
`792f42de85a935a7a09b799caefe6f5a0aeccec104f303dd21cfd43050116493`.

The exact union must contain each exponent
`2..14,16..24` once, exclude q15, and agree expression-by-expression with the
eventual simultaneous table.  Any failed source hash, nonzero exit, missing
table, duplicated/missing exponent, or disagreement is no combined verdict.

Execution is AWS/Linux only.  Each shard has a 4 GiB virtual-memory cap and a
six-hour timeout.  Scope is the fixed source-typed A3 section on the declared
generic principal open, square-zero current adjoint scheduling only.  The
base current system is inconsistent; no column/kernel is a tangent vector,
family, TD6, SP-2, landing, or JC2 result.
