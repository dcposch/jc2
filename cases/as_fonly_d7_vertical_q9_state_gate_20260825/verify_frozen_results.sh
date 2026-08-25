#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
result_dir="$case_dir/results_as_d7_q9_state_20260825T011049Z"
check_tmp=$(mktemp -d "${TMPDIR:-/tmp}/jc2-q9-check.XXXXXX")
trap 'rm -rf "$check_tmp"' EXIT HUP INT TERM

(cd "$repo_root" && sha256sum -c "$case_dir/SOURCE_CLOSURE.sha256")
(cd "$case_dir" && sha256sum -c RUNNER_MANIFEST.sha256)
(cd "$case_dir" && sha256sum -c REMOTE_RESULTS_MANIFEST.sha256)

index=0
while [ "$index" -lt 27 ]; do
  label=$(printf '%02d' "$index")
  test ! -s "$result_dir/shard_$label.err"
  grep -qx 'rc=0' "$result_dir/shard_$label.rc"
  grep -q 'Exit status: 0' "$result_dir/shard_$label.time"
  index=$((index + 1))
done
test ! -s "$result_dir/aggregate.err"
grep -qx 'overall_rc=0' "$result_dir/launch.meta"
grep -qx 'aggregate_rc=0' "$result_dir/launch.meta"
python3 "$case_dir/aggregate_shards.py" "$result_dir" 27 \
  > "$check_tmp/aggregate.out" 2> "$check_tmp/aggregate.err"
test ! -s "$check_tmp/aggregate.err"
diff -u "$result_dir/aggregate.out" "$check_tmp/aggregate.out"
printf '%s\n' PASS-Q9-FROZEN-HASH-AND-AGGREGATE-CHECK

