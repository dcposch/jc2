# AWS-only 27-way N12/N11 structural-base shards

This package partitions the `3^7=2187` structural bases into 27 contiguous
lexicographic intervals of 81 bases.  It is a discovery accelerator and an
independent aggregate-count check.  The existing monolithic r6d runner
remains the canonical ordered state-stream hash.

Each shard has a 12-hour timeout and an 8 GiB virtual-memory ceiling.  Run
only on an AWS host with at least 27 idle CPUs.  Launch orphan-safe with a
unique tag:

```sh
nohup setsid ./launch_all.sh UNIQUE_UTC_TAG > launch_UNIQUE_UTC_TAG.log 2>&1 < /dev/null &
```

The aggregate fails closed unless all 27 outputs finish, cover contiguous
ranges exactly once, sum to the frozen parent total `1,085,103`, and satisfy
the exact `729` spectator-fibre identity.  It emits every shard-output hash
and an ordered binary Merkle root.

Timeout/OOM/partial aggregation is no mathematical evidence.  A successful
aggregate supplies counts and a Merkle certificate, not the monolithic
stream digest and not a lower-row/all-depth conclusion.
