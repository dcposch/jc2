#!/bin/sh
set -eu
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
tag=as_q7kernel_next_high_20260825T030036Z
result_dir="$case_dir/results_$tag"
test "$(sha256sum "$result_dir/aggregate.json" | awk '{print $1}')" = \
  87f63bdd0a9408ac1b2a019b4de9e17645625293fc75b3460a334b70e8f0a96f
test "$(sha256sum "$result_dir/aggregate.stdout" | awk '{print $1}')" = \
  c9b36bd72a1a0c052028263208ed2dd2a8951e5e63347bf28252f7eba20caba9
grep -q '^PASS-Q7KERNEL-NEXT-HIGH-AGGREGATE$' "$result_dir/aggregate.stdout"
test "$(find "$result_dir" -name 'shard_*.json' | wc -l | tr -d ' ')" = 27
test "$(grep -l '^PASS-Q7KERNEL-NEXT-HIGH-SHARD$' \
  "$result_dir"/shard_*.stdout | wc -l | tr -d ' ')" = 27
test -z "$(find "$result_dir" -name '*.stderr' -type f -size +0c -print)"
(
  cd "$result_dir"
  sed 's#  .*/results_as_q7kernel_next_high_20260825T030036Z/#  #' \
    OUTPUTS.sha256 | sha256sum -c - >/dev/null
)
printf '%s\n' PASS-Q7KERNEL-NEXT-HIGH-FROZEN-HASH-AND-CUSTODY-CHECK
