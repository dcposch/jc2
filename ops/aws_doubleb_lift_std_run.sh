#!/bin/sh
# Evidence-aware exact Singular default-std membership runner.
# Usage: aws_doubleb_lift_std_run.sh TAG TIMEOUT_SECONDS
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
out_root=${JC2_DOUBLEB_OUT:-$repo_root/aws-doubleb-out}
lane=$out_root/$tag
if [ -e "$lane" ]; then
  echo "duplicate lane refused: $lane" >&2
  exit 3
fi
mkdir -p "$lane"

meta=$lane/metadata.txt
input=$lane/input.sing
result=$lane/result.out
stderr=$lane/stderr.log
generator=$repo_root/cases/max12_912_order3_double_b_p_membership_20260824/generate_lift_std.py
base_generator=$repo_root/cases/max12_912_order3_double_b_p_membership_20260824/generate_lift.py

python3 "$generator" > "$input"
{
  echo "tag=$tag"
  echo "backend=Singular-lift-default-std"
  echo "characteristic=0"
  echo "timeout_seconds=$cap"
  echo "host=$(hostname)"
  echo "nproc=$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo UNKNOWN)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "python=$(python3 --version 2>&1)"
  echo "singular=$(Singular --version 2>/dev/null | head -n 1 || echo MISSING)"
  sha256sum "$0" | sed 's/^/runner_sha256=/'
  sha256sum "$generator" | sed 's/^/generator_sha256=/'
  sha256sum "$base_generator" | sed 's/^/base_generator_sha256=/'
  sha256sum "$repo_root/cases/max12_912_order3_double_b_p_elimination_20260824/input.ms" | sed 's/^/source_sha256=/'
  sha256sum "$repo_root/cases/max12_912_order3_double_b_p_elimination_20260824/result.out" | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$input" | awk '{print $1}')"
  echo "input_bytes=$(wc -c < "$input" | tr -d ' ')"
  free -b | sed 's/^/start_free=/'
} > "$meta"

set +e
timeout --signal=TERM --kill-after=300 "$cap" nice -n 5 Singular -q \
  < "$input" > "$result" 2> "$stderr"
rc=$?
set -e

{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "exit_code=$rc"
  echo "result_bytes=$(wc -c < "$result" | tr -d ' ')"
  echo "stderr_bytes=$(wc -c < "$stderr" | tr -d ' ')"
  echo "result_sha256=$(sha256sum "$result" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$stderr" | awk '{print $1}')"
  free -b | sed 's/^/end_free=/'
  if [ "$rc" -eq 0 ]; then echo "final_status=DONE"; else echo "final_status=FAILED"; fi
} >> "$meta"
exit "$rc"
