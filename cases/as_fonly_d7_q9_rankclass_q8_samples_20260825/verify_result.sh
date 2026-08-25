#!/bin/sh
set -eu
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
tag=as_q9_rankclass_q8_samples_20260825T022400Z
result_dir="$case_dir/results_$tag"
test "$(sha256sum "$result_dir/aggregate.json" | awk '{print $1}')" = \
  492a70d7145578bf35730b0a48dc54687f8de3c7168dc1a23b7f0f4c0404b967
grep -q '^PASS-Q9-RANKCLASS-Q8-SAMPLE-AGGREGATE$' "$result_dir/aggregate.out"
test "$(find "$result_dir" -name 'shard_*.json' | wc -l | tr -d ' ')" = 27
test "$(grep -l '^PASS-Q9-RANKCLASS-Q8-SAMPLE-SHARD$' \
  "$result_dir"/shard_*.out | wc -l | tr -d ' ')" = 27
test -z "$(find "$result_dir" -name '*.err' -type f -size +0c -print)"
(
  cd "$result_dir"
  sed 's#  .*/results_as_q9_rankclass_q8_samples_20260825T022400Z/#  #' \
    OUTPUTS.sha256 | sha256sum -c - >/dev/null
)
printf '%s\n' PASS-Q9-RANKCLASS-Q8-SAMPLES-FROZEN-HASH-AND-CUSTODY-CHECK
