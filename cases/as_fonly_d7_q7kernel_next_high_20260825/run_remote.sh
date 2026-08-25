#!/bin/sh
set -eu
tag=${1:?usage: run_remote.sh UNIQUE_UTC_TAG}
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
printf 'tag=%s\nhost=%s\nstart_utc=%s\npython=%s\nvm_limit_kib=2097152_per_shard\ntimeout_seconds=43200\nshards=27\nparallel=27\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$(python3 --version 2>&1)" > "$result_dir/run.meta"
set +e
(
  index=0
  while [ "$index" -lt 27 ]; do
    (
      ulimit -v 2097152
      env JC2_ROOT="$root" SHARD_COUNT=27 SHARD_INDEX="$index" \
        OUTPUT_JSON="$result_dir/shard_$(printf '%02d' "$index").json" \
        python3 "$case_dir/compile_shard.py" \
        > "$result_dir/shard_$(printf '%02d' "$index").stdout" \
        2> "$result_dir/shard_$(printf '%02d' "$index").stderr"
    ) &
    index=$((index + 1))
  done
  wait
  env RESULT_DIR="$result_dir" python3 "$case_dir/aggregate.py" \
    > "$result_dir/aggregate.stdout" 2> "$result_dir/aggregate.stderr"
) 2> "$result_dir/launcher.stderr"
rc=$?
set -e
printf 'rc=%s\nend_utc=%s\n' "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> "$result_dir/run.meta"
find "$result_dir" -maxdepth 1 -type f ! -name OUTPUTS.sha256 \
  -exec sha256sum {} + | sort -k2 > "$result_dir/OUTPUTS.sha256"
exit "$rc"
