#!/bin/sh
set -eu
tag=${1:?usage: run_remote.sh UNIQUE_UTC_TAG}
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
printf 'tag=%s\nhost=%s\nstart_utc=%s\npython=%s\nshard_count=27\nper_class=4\nvm_limit_kib_per_shard=4194304\ntimeout_seconds=43200\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$(python3 --version 2>&1)" > "$result_dir/run.meta"
pids=""
for index in $(seq 0 26); do
  label=$(printf '%02d' "$index")
  (
    ulimit -v 4194304
    set +e
    /usr/bin/time -v -o "$result_dir/shard_${label}.time" \
      timeout --signal=TERM --kill-after=60s 43200 \
      env JC2_ROOT="$root" SHARD_COUNT=27 SHARD_INDEX="$index" PER_CLASS=4 \
      OUTPUT_JSON="$result_dir/shard_${label}.json" \
      python3 "$case_dir/compile_shard.py" \
      > "$result_dir/shard_${label}.out" \
      2> "$result_dir/shard_${label}.err"
    rc=$?
    printf '%s\n' "$rc" > "$result_dir/shard_${label}.rc"
    exit "$rc"
  ) &
  pids="$pids $!"
done
overall=0
for pid in $pids; do
  if ! wait "$pid"; then overall=1; fi
done
if [ "$overall" -eq 0 ]; then
  set +e
  /usr/bin/time -v -o "$result_dir/aggregate.time" \
    env RESULT_DIR="$result_dir" SHARD_COUNT=27 \
    python3 "$case_dir/aggregate.py" \
    > "$result_dir/aggregate.out" 2> "$result_dir/aggregate.err"
  aggregate_rc=$?
  set -e
else
  aggregate_rc=99
fi
printf 'overall_rc=%s\naggregate_rc=%s\nend_utc=%s\n' \
  "$overall" "$aggregate_rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> "$result_dir/run.meta"
find "$result_dir" -maxdepth 1 -type f ! -name OUTPUTS.sha256 \
  -print0 | sort -z | xargs -0 sha256sum > "$result_dir/OUTPUTS.sha256"
if [ "$overall" -ne 0 ]; then exit "$overall"; fi
exit "$aggregate_rc"
