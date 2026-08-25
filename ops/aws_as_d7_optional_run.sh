#!/bin/sh
# Evidence-aware runner for one optional full-ring AS D7 decomposition.
# Usage: aws_as_d7_optional_run.sh TAG VARIANT TIMEOUT_SECONDS
set -eu

if [ "$#" -ne 3 ]; then
  echo "usage: $0 TAG {subsystem|char-dp|char-xfirst} TIMEOUT_SECONDS" >&2
  exit 2
fi
tag=$1
variant=$2
cap=$3
case "$tag" in
  ''|*[!A-Za-z0-9._-]*) echo "invalid tag" >&2; exit 2 ;;
esac
case "$variant" in
  subsystem|char-dp|char-xfirst) ;;
  *) echo "invalid variant" >&2; exit 2 ;;
esac
case "$cap" in
  ''|*[!0-9]*) echo "invalid timeout" >&2; exit 2 ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)
case_dir=$repo_root/cases/as_fonly_d7_vertical_d7_cap_boundary_20260824
out_root=${JC2_AS_D7_OUT:-$repo_root/aws-as-d7-out}
lane=$out_root/$tag
if [ -e "$lane" ]; then
  echo "duplicate lane refused: $lane" >&2
  exit 3
fi
mkdir -p "$lane"

meta=$lane/metadata.txt
result=$lane/result.out
stdout=$lane/stdout.log
timing=$lane/time.log
{
  echo "tag=$tag"
  echo "variant=$variant"
  echo "characteristic=3"
  echo "timeout_seconds=$cap"
  echo "host=$(hostname)"
  echo "nproc=$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo UNKNOWN)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "singular=$(Singular --version 2>/dev/null | head -n 1 || echo MISSING)"
  sha256sum "$0" | sed 's/^/runner_sha256=/'
  sha256sum "$case_dir/MANIFEST.sha256" | sed 's/^/manifest_sha256=/'
  sha256sum "$case_dir/FREEZE.txt" | sed 's/^/freeze_sha256=/'
  free -b | sed 's/^/start_free=/'
} > "$meta"

set +e
timeout --signal=TERM --kill-after=300 "$cap" /usr/bin/time -v \
  "$case_dir/run_optional_full_minass.sh" "$variant" "$result" \
  > "$stdout" 2> "$timing"
rc=$?
set -e

{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "exit_code=$rc"
  echo "result_bytes=$(wc -c < "$result" 2>/dev/null | tr -d ' ' || echo 0)"
  echo "stdout_sha256=$(sha256sum "$stdout" | awk '{print $1}')"
  echo "time_sha256=$(sha256sum "$timing" | awk '{print $1}')"
  if [ -f "$result" ]; then
    echo "result_sha256=$(sha256sum "$result" | awk '{print $1}')"
  else
    echo "result_sha256=MISSING"
  fi
  free -b | sed 's/^/end_free=/'
  if [ "$rc" -eq 0 ]; then echo "final_status=DONE"; else echo "final_status=FAILED"; fi
} >> "$meta"
exit "$rc"
