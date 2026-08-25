# V55/V56 proof-carrying source-row shards

V55 partitions all 54 arbitrary-degree previous/pole source rows by
`index mod shard_count`.  V56 partitions all 40 arbitrary-degree current
source rows by the same rule and lazily reconstructs every previous-row
ancestor used by each selected current row.  Both retain the V50/V53 source,
the genuine quadratic positive control, exact sparse polynomial division,
and direct original-row replay.

Suggested launch:

```sh
# V55: 9 shards, six rows each
TD6_SHARD_COUNT=9 TD6_SHARD_INDEX=0 TD6_OUTPUT_DIR="$PWD/artifacts" \
  ./run_v55.sh > shard.stdout 2> shard.stderr

# V56: 10 shards, four rows each
TD6_SHARD_COUNT=10 TD6_SHARD_INDEX=0 TD6_OUTPUT_DIR="$PWD/artifacts" \
  ./run_v56.sh > shard.stdout 2> shard.stderr
```

Every shard must end rc zero at its mode-specific PASS marker.  Promotion is
forbidden until an exact union checker parses immutable outputs, verifies
identical source/archive hashes, proves disjoint coverage of exactly
`0..53` and `0..39`, and pairs the audit with a completed V53 source identity.
No individual shard proves a full identity, generic open, fixed-A3 family,
TD6, SP-2, or JC2 claim.
