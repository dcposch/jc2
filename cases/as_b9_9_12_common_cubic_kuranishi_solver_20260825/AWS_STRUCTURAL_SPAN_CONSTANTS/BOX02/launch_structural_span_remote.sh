#!/usr/bin/env bash
set -u

: "${JOB_ROOT:?JOB_ROOT is required}"
: "${AWS_JOB_TAG:?AWS_JOB_TAG is required}"
ulimit -v 8388608
timeout 3600 bash "$JOB_ROOT/run_structural_span_aws.sh"
rc=$?
printf '%s\n' "$rc" > "$JOB_ROOT/launcher.rc"
exit "$rc"
