#!/bin/sh
set -eu
tag=${1:?usage: run_remote.sh UNIQUE_UTC_TAG}
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
printf 'tag=%s\nhost=%s\nstart_utc=%s\npython=%s\nvm_limit_kib=2097152_per_lane\ntimeout_seconds=43200\nlanes=66\nparallel=66\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$(python3 --version 2>&1)" > "$result_dir/run.meta"
set +e
(
  for family_count in q8_kernel:39 q9_locus:27; do
    family=${family_count%:*}
    count=${family_count#*:}
    index=0
    while [ "$index" -lt "$count" ]; do
      (
        ulimit -v 2097152
        stem="state_${family}_$(printf '%02d' "$index")"
        env JC2_ROOT="$root" STATE_FAMILY="$family" SAMPLE_INDEX="$index" \
          OUTPUT_JSON="$result_dir/$stem.json" \
          python3 "$case_dir/compile_state.py" \
          > "$result_dir/$stem.stdout" 2> "$result_dir/$stem.stderr"
      ) &
      index=$((index + 1))
    done
  done
  wait
  env RESULT_DIR="$result_dir" python3 "$case_dir/aggregate.py" \
    > "$result_dir/aggregate.stdout" 2> "$result_dir/aggregate.stderr"
) 2> "$result_dir/launcher.stderr"
rc=$?
set -e
printf 'rc=%s\nend_utc=%s\n' "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> "$result_dir/run.meta"
(
  cd "$result_dir"
  find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 \
    -exec sha256sum {} + | sort -k2 > OUTPUTS.sha256
)
exit "$rc"
