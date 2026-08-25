#!/bin/sh
set -eu
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
tag=${1:?usage: run_remote.sh UNIQUE_UTC_TAG}
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
printf 'tag=%s\nhost=%s\nstart_utc=%s\npython=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$(python3 --version 2>&1)" > "$result_dir/run.meta"
set +e
env JC2_ROOT="$root" OUTPUT_JSON="$result_dir/particulars.json" \
  python3 "$case_dir/audit_particulars.py" \
  > "$result_dir/audit.stdout" 2> "$result_dir/audit.stderr"
rc=$?
set -e
printf 'rc=%s\nend_utc=%s\n' "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> "$result_dir/run.meta"
(cd "$result_dir" && find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 \
  -exec sha256sum {} + | sort -k2 > OUTPUTS.sha256)
exit "$rc"
