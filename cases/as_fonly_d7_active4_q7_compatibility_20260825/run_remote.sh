#!/bin/sh
set -eu
tag=${1:?usage: run_remote.sh UNIQUE_UTC_TAG}
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
printf 'tag=%s\nhost=%s\nstart_utc=%s\npython=%s\nvm_limit_kib=4194304\ntimeout_seconds=43200\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$(python3 --version 2>&1)" > "$result_dir/run.meta"
set +e
(
  ulimit -v 4194304
  timeout --signal=TERM --kill-after=60s 43200 \
    env JC2_ROOT="$root" BOOTSTRAP_JSON="$result_dir/bootstrap.json" \
      OUTPUT_JSON="$result_dir/active_cube.json" \
      python3 "$case_dir/active_cube.py"
) > "$result_dir/replay.stdout" 2> "$result_dir/replay.stderr"
rc=$?
set -e
printf 'rc=%s\nend_utc=%s\n' "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> "$result_dir/run.meta"
(cd "$result_dir" && find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 \
  -exec sha256sum {} + | sort -k2 > OUTPUTS.sha256)
exit "$rc"
