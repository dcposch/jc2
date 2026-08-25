# TD6 V55 complete previous/pole source-row audit — AWS

This immutable package records a proof-carrying disjoint audit of all 54
arbitrary-degree previous/pole original rows for the fixed source-typed center
family

```text
(c1,c2,c3)=(C,V,U),
q_beta=t+beta*t^2+t^25.
```

Nine AWS shards used the exact same source archive and partitioned row indices
by `index mod 9`.  Every shard retained the 3,602-column transport source,
the staged first and previous/pole systems, direct arbitrary-degree polynomial
division, original-row replay, and the genuine quadratic positive control.
Each shard ended at `rc=0` with
`TD6-A3-Q2-SOURCE-ROW-SHARD-V55 PASS`.

The separately executed fail-closed checker then verified:

```text
mode=previous
shard_count=9
total_original_row_count=54
disjoint=true
exhaustive=true
archive_sha256=afb1bbab4572893eb1c5b96faa82832fbfd55508142e9085711952c964cdcc2a
stdout_union_sha256=e0c73f462671fd57e38c10a2c4b13c5612e96d0367721f1dee3ebe74ebfe2ba4
TD6-SOURCE-ROW-SHARD-UNION PASS
```

Thus every one of the 54 registered previous/pole original rows has an exact
replayed reduction through the staged first system at this source scope.  Of
these rows, 36 are genuinely quadratic; the frozen positive control
`('X-1',0)` confirms that the arbitrary-degree path is exercised.

## AWS custody

- Host: r6d, `100.26.198.153`.
- Shard run tags:
  `td6_v55_prev_shards_r6d_20260825T094434Z_s00` through `s08`.
- Union run tag: `td6_v55_prev_union_r6d_20260825T1022Z`.
- Source archive SHA-256:
  `afb1bbab4572893eb1c5b96faa82832fbfd55508142e9085711952c964cdcc2a`.
- Union checker SHA-256:
  `4c4ef3f0178f0e9af16b293aab2435581de32aabbdf72dfca3cfe3cae9760c9b`.
- Union stdout SHA-256:
  `0a4ff0ecf052b71f914031e25a2705988312770293183c73745ce47c6a9e9855`.
- Union stderr is empty, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Per-shard wall times were 23:06--31:53 and peak RSS was at most
  535,820 KB.

Every per-shard stdout, stderr, return code, UTC interval, source check, and
archive hash is retained under `evidence/s00` through `evidence/s08`.
The checker custody is under `evidence/union`.

## Deterministic replay

On an AWS host with the pinned campaign Python environment:

```sh
tar -xzf source/td6-aws-handoff-20260825-v55v56.tar.gz
cd td6-aws-handoff-20260825-v55v56
sha256sum -c SOURCE.sha256
sha256sum -c V55_V56_SOURCE.sha256

for i in 0 1 2 3 4 5 6 7 8; do
  run="../v55-s${i}"
  mkdir -p "$run/artifacts"
  TD6_SHARD_COUNT=9 TD6_SHARD_INDEX="$i" \
    TD6_OUTPUT_DIR="$run/artifacts" \
    ./run_v55.sh > "$run/shard.stdout" 2> "$run/shard.stderr"
  printf '0\n' > "$run/rc"
  cp ../archive.sha256 "$run/archive.sha256"
done

python verify_shard_union.py previous \
  ../v55-s0 ../v55-s1 ../v55-s2 ../v55-s3 ../v55-s4 \
  ../v55-s5 ../v55-s6 ../v55-s7 ../v55-s8
```

Each shard requires up to about 0.55 GiB and should be run on AWS under the
campaign memory/time policy.  The checker itself is a short exact text audit.

## Scope firewall

This package proves only exhaustive exact reduction of the 54 registered
previous/pole original rows at the fixed `(C,V,U), q_beta` source scope.  Each
shard deliberately prints `full_source_identity_replayed=false` because the
N13/P12 identity is a separate dependency-closed calculation.  Full source
composition still requires a passing V53 identity and an exhaustive V56 audit
of all 40 current rows.  No generic-open cover, fixed-A3 family kill, TD6,
SP-2, landing, ceiling, or JC2 conclusion follows from V55 alone.
