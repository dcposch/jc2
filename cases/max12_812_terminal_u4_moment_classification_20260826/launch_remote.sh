#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "usage: launch_remote.sh JOB_ROOT TAG EXPECTED_SOURCE_SHA256" >&2
  exit 64
fi

job_root=$1
tag=$2
expected_source_sha=$3
out_dir="$job_root/output"
mkdir -p "$out_dir"

printf '%s\n' \
  "launcher_started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "host=$(hostname)" \
  "tag=$tag" \
  "virtual_memory_cap_kib=8388608" \
  "timeout_seconds=600" > "$job_root/launch.meta"

set +e
env \
  JC2_AWS_JOB_TAG="$tag" \
  EXPECTED_SOURCE_SHA256="$expected_source_sha" \
  /usr/bin/time -v \
  "$job_root/run_aws.sh" "$job_root/enumerate_u4.py" "$out_dir"
rc=$?
set -e

printf '%s\n' "$rc" > "$job_root/rc"
printf '%s\n' "launcher_finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$job_root/launch.meta"
printf '%s\n' "launcher_rc=$rc" >> "$job_root/launch.meta"
exit "$rc"
