# V78C proof-carrying P12 shard preregistration

V78C is a latency accelerator for V78B, not a new mathematical shortcut.
For each licensed q exponent `e` in `2..14,16..24`, it runs the same exact
transport, first-stage reduction, original-row P12 source replay, varying
multiplier/lambda-prime audit, denominator check, and omission controls over
one square-zero coordinate `eps_e`.  The q2 compiler coordinate `qd.B` is
active exactly for `e=2` and is exact zero for every other shard.

All 22 shards must return the standalone PASS marker.  Their one-row P12
tables must union without duplicate/missing exponents and must equal the
corresponding rows of the simultaneous V78B table.  Exponents 2 and 3 must
also match V32 and corrected V77R respectively.  Run every shard from the
same hash-pinned source on two independent AWS hosts.  A shard failure or
union mismatch fails closed.

This remains first-order/source-support evidence at the already-empty fixed
A3 base.  It does not prove a q neighborhood, polynomial q family, full TD6,
SP-2, or JC2 claim.

