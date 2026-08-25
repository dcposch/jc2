#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <candidate-relative-path>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
candidate_relative=$4
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$candidate_relative" in /*|*..*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_candidate_point_count_aws_20260825
candidate=$repo_root/$candidate_relative
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "route=stdlib exact F127 affine point and gradient count"
  echo "timeout_seconds=600"
  echo "virtual_memory_limit_kib=2097152"
  python3 --version
  sha256sum "$0" "$case_dir/count_points.py" "$candidate"
} > "$meta"
set +e
(ulimit -v 2097152; timeout --signal=TERM --kill-after=30 600 \
  /usr/bin/time -v python3 "$case_dir/count_points.py" --candidate "$candidate" \
  > "$lane/result.json" 2> "$lane/stderr.log")
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/result.json" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
