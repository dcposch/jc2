#!/bin/sh
set -eu
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
tag=as_q8state_next_high_samples_20260825T031215Z
result_dir="$case_dir/results_$tag"
test "$(sha256sum "$result_dir/aggregate.json" | awk '{print $1}')" = \
  3d42d327476b0fdaba635588b332af2ab2ed415a17cd758a2a38cbdf2495ee8f
test "$(sha256sum "$result_dir/aggregate.stdout" | awk '{print $1}')" = \
  de3aa4e57a69d99eae4905a5add4f15a0fb6f865fa1fa884c591370928b17b62
grep -q '^PASS-Q8STATE-NEXT-HIGH-AGGREGATE$' "$result_dir/aggregate.stdout"
test "$(find "$result_dir" -name 'state_*.json' | wc -l | tr -d ' ')" = 66
test "$(grep -l '^PASS-Q8STATE-NEXT-HIGH-SAMPLE$' \
  "$result_dir"/state_*.stdout | wc -l | tr -d ' ')" = 66
test -z "$(find "$result_dir" -name '*.stderr' -type f -size +0c -print)"
(cd "$result_dir" && sha256sum -c OUTPUTS.sha256 >/dev/null)
printf '%s\n' PASS-Q8STATE-NEXT-HIGH-FROZEN-HASH-AND-CUSTODY-CHECK
