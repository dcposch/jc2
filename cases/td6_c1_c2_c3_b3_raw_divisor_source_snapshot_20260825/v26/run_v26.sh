#!/usr/bin/env bash
set -u

if [ "$#" -ne 6 ]; then
  echo "usage: run_v26.sh ARCHIVE RUN_DIR PYTHON LANE COMPONENT EXPECTED_ARCHIVE_SHA256" >&2
  exit 64
fi

archive=$1
run_dir=$2
python_bin=$3
lane=$4
component=$5
expected_archive_sha256=$6

case "$lane" in
  ascending) lane_args=("--component=$component") ;;
  reverse-first) lane_args=("--component=$component" --reverse-first) ;;
  *) echo "unknown lane: $lane" >&2; exit 64 ;;
esac
case "$component" in
  p3|b16|bneg2|bq|b3tq|b3half) ;;
  *) echo "unknown component: $component" >&2; exit 64 ;;
esac

mkdir -p "$run_dir"
meta="$run_dir/$lane.meta"
stdout="$run_dir/$lane.stdout"
stderr="$run_dir/$lane.stderr"
payload="$run_dir/td6-aws-handoff-20260824-v26"

actual_archive_sha256=$(sha256sum "$archive" | awk '{print $1}')
if [ "$actual_archive_sha256" != "$expected_archive_sha256" ]; then
  echo "archive hash mismatch" >&2
  exit 65
fi

tar -xzf "$archive" -C "$run_dir"
(
  cd "$payload"
  sha256sum -c SOURCE.sha256
) > "$run_dir/source-check.stdout" 2> "$run_dir/source-check.stderr"
if [ "$?" -ne 0 ]; then
  echo "source closure verification failed" >&2
  exit 66
fi

script="$payload/jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py"
start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  echo "lane=$lane"
  echo "component=$component"
  echo "host=$(hostname)"
  echo "supervisor_pid=$$"
  echo "start_utc=$start_utc"
  echo "archive=$archive"
  echo "archive_sha256=$actual_archive_sha256"
  echo "source_manifest_sha256=$(sha256sum "$payload/SOURCE.sha256" | awk '{print $1}')"
  echo "producer_sha256=$(sha256sum "$script" | awk '{print $1}')"
  echo "python=$python_bin"
  "$python_bin" --version 2>&1 | sed 's/^/python_version=/'
  "$python_bin" -c 'import flint; print("python_flint=" + flint.__version__)'
  echo "command=/usr/bin/time -v timeout 28800 $python_bin $script ${lane_args[*]}"
} > "$meta"

set +e
/usr/bin/time -v timeout 28800 "$python_bin" "$script" "${lane_args[@]}" \
  > "$stdout" 2> "$stderr"
rc=$?
set -e

{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$stdout" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$stderr" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
