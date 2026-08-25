#!/bin/sh
set -eu

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TAG=as_active4_plus_one_v2_20260825T034300Z
RESULTS="$HERE/results_$TAG"

(cd "$RESULTS" && shasum -a 256 -c OUTPUTS.sha256)
grep -F 'PASS-ACTIVE4-PLUS-ONE-AGGREGATE' "$RESULTS/aggregate.stdout" >/dev/null
grep -F 'mixed_cancellation_shard_count 0' "$RESULTS/aggregate.stdout" >/dev/null
test ! -s "$RESULTS/aggregate.stderr"
i=0
while [ "$i" -lt 28 ]; do
  grep -F 'PASS-ACTIVE4-PLUS-ONE-SHARD' \
    "$RESULTS/shard_$(printf '%02d' "$i").stdout" >/dev/null
  test ! -s "$RESULTS/shard_$(printf '%02d' "$i").stderr"
  i=$((i + 1))
done
echo PASS-ACTIVE4-PLUS-ONE-V2-RESULT-VERIFY
