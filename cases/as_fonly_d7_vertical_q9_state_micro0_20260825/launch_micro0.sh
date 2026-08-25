#!/bin/sh
set -eu

tag=${1:?usage: launch_micro0.sh UNIQUE_TAG MACRO_RESULT_DIR}
macro_result=${2:?usage: launch_micro0.sh UNIQUE_TAG MACRO_RESULT_DIR}
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
compiler="$root/cases/as_fonly_d7_vertical_q9_state_gate_20260825/compile_shard.py"
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
: > "$result_dir/pids.tsv"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmacro_result=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$macro_result" \
  > "$result_dir/launch.meta"
pids=""
index=0
while [ "$index" -lt 81 ]; do
  label=$(printf '%04d' "$index")
  (
    set +e
    ulimit -v 8388608
    /usr/bin/time -v -o "$result_dir/micro_$label.time" \
      timeout --signal=TERM --kill-after=60s 43200 \
      env JC2_ROOT="$root" SHARD_COUNT=2187 SHARD_INDEX="$index" \
      python3 "$compiler" \
      > "$result_dir/micro_$label.out" 2> "$result_dir/micro_$label.err"
    rc=$?
    printf 'index=%s\nrc=%s\nend_utc=%s\n' \
      "$index" "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
      > "$result_dir/micro_$label.rc"
    exit "$rc"
  ) &
  pid=$!
  printf '%s\t%s\n' "$index" "$pid" >> "$result_dir/pids.tsv"
  pids="$pids $pid"
  index=$((index + 1))
done
overall=0
for pid in $pids; do
  if ! wait "$pid"; then overall=1; fi
done
if [ "$overall" -eq 0 ]; then
  python3 "$case_dir/aggregate_hybrid.py" "$result_dir" "$macro_result" \
    > "$result_dir/hybrid_aggregate.out" 2> "$result_dir/hybrid_aggregate.err"
  aggregate_rc=$?
else
  aggregate_rc=125
fi
printf 'overall_rc=%s\naggregate_rc=%s\nend_utc=%s\n' \
  "$overall" "$aggregate_rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> "$result_dir/launch.meta"
exit "$overall"

