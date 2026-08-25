#!/bin/sh
# Evidence-aware AWS runner for the immutable active Q8 support matrix.
# Usage: aws_q8_invariant_support_run.sh TAG TIMEOUT_SECONDS
set -eu

if [ "$#" -ne 2 ]; then
  echo "usage: $0 TAG TIMEOUT_SECONDS" >&2
  exit 2
fi
tag=$1
cap=$2
case "$tag" in
  ''|*[!A-Za-z0-9._-]*) echo "invalid tag" >&2; exit 2 ;;
esac
case "$cap" in
  ''|*[!0-9]*) echo "invalid timeout" >&2; exit 2 ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)
case_dir=$repo_root/cases/max12_912_order3_nu_q8_invariant_support_20260824
parent=$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824
out_root=${JC2_Q8_SUPPORT_OUT:-$repo_root/aws-q8-support-out}
lane=$out_root/$tag
if [ -e "$lane" ]; then
  echo "duplicate lane refused: $lane" >&2
  exit 3
fi
mkdir -p "$lane/results"

meta=$lane/metadata.txt
summary=$lane/summary.json
stderr=$lane/stderr.log
{
  echo "tag=$tag"
  echo "backend=python-exact-modular-q8-support"
  echo "workers=8"
  echo "order=128"
  echo "max_left=24"
  echo "max_right=24"
  echo "max_columns=108"
  echo "holdout=16"
  echo "timeout_seconds=$cap"
  echo "host=$(hostname)"
  echo "nproc=$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo UNKNOWN)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "python=$(python3 --version 2>&1)"
  sha256sum "$0" | sed 's/^/runner_sha256=/'
  for source in "$case_dir/modular_support.py" "$case_dir/run_matrix.py" \
    "$case_dir/replay.py" "$parent/MANIFEST.sha256" "$parent/FREEZE.txt"
  do
    sha256sum "$source" | sed 's/^/source_sha256=/'
  done
  free -b | sed 's/^/start_free=/'
} > "$meta"

set +e
timeout --signal=TERM --kill-after=60 "$cap" nice -n 5 python3 \
  "$case_dir/run_matrix.py" \
  --output-directory "$lane/results" \
  --workers 8 --order 128 --max-left 24 --max-right 24 \
  --max-columns 108 --holdout 16 --timeout 3600 \
  > "$summary" 2> "$stderr"
rc=$?
set -e

{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "exit_code=$rc"
  echo "summary_bytes=$(wc -c < "$summary" | tr -d ' ')"
  echo "stderr_bytes=$(wc -c < "$stderr" | tr -d ' ')"
  echo "summary_sha256=$(sha256sum "$summary" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$stderr" | awk '{print $1}')"
  echo "result_count=$(find "$lane/results" -type f -name 'support-*.json' | wc -l | tr -d ' ')"
  free -b | sed 's/^/end_free=/'
  if [ "$rc" -eq 0 ]; then echo "final_status=DONE"; else echo "final_status=FAILED"; fi
} >> "$meta"
exit "$rc"
