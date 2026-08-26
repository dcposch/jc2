#!/usr/bin/env bash
set -uo pipefail

if [[ $# -ne 7 ]]; then
  echo "usage: run_with_rc.sh JOB_ROOT TAG SOURCE_ROOT OUT_DIR ARCHIVE_SHA SOLUTION_SHA COMMIT" >&2
  exit 64
fi

job_root=$1
tag=$2
source_root=$3
out_dir=$4
archive_sha=$5
solution_sha=$6
commit=$7

echo "wrapper_started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
ulimit -v 16777216
set +e
env \
  JC2_AWS_JOB_TAG="$tag" \
  JC2_SOURCE_ARCHIVE="$job_root/source.tar.gz" \
  timeout --signal=TERM --kill-after=60 3600 \
  "$job_root/verify_remote.sh" \
    "$source_root" "$out_dir" "$archive_sha" "$solution_sha" "$commit"
rc=$?
set -e
printf '%s\n' "$rc" > "$job_root/rc"
echo "wrapper_finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "wrapper_rc=$rc"
exit "$rc"
