#!/bin/sh
set -eu

tag=${1:?usage: launch_all.sh UNIQUE_TAG}
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
: > "$result_dir/pids.tsv"
printf 'tag=%s\nhost=%s\nstart_utc=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  > "$result_dir/launch.meta"
pids=""
index=0
while [ "$index" -lt 27 ]; do
  label=$(printf '%02d' "$index")
  (
    set +e
    ulimit -v 8388608
    /usr/bin/time -v -o "$result_dir/shard_$label.time" \
      timeout --signal=TERM --kill-after=60s 43200 \
      env JC2_ROOT="$root" SHARD_COUNT=27 SHARD_INDEX="$index" \
      python3 "$case_dir/compile_shard.py" \
      > "$result_dir/shard_$label.out" 2> "$result_dir/shard_$label.err"
    rc=$?
    printf 'index=%s\nrc=%s\nend_utc=%s\n' \
      "$index" "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
      > "$result_dir/shard_$label.rc"
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
  python3 "$case_dir/aggregate_shards.py" "$result_dir" 27 \
    > "$result_dir/aggregate.out" 2> "$result_dir/aggregate.err"
  aggregate_rc=$?
else
  aggregate_rc=125
fi
printf 'overall_rc=%s\naggregate_rc=%s\nend_utc=%s\n' \
  "$overall" "$aggregate_rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> "$result_dir/launch.meta"
exit "$overall"
