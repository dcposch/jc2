#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then
  echo "usage: $0 <repo-root> <output-root> <tag>" >&2
  exit 2
fi
repo_root=$1
output_root=$2
tag=$3
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
lane=$output_root/$tag
if [ -e "$lane" ]; then
  echo "duplicate lane refused" >&2
  exit 3
fi
mkdir -p "$lane"
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_candidate_q8_boundary_aws_20260825
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "route=exact F_127 candidate boundary division"
  sha256sum "$0" "$case_dir/replay.py" | sed 's/^/source_sha256=/'
} > "$meta"
set +e
python3 "$case_dir/replay.py" > "$lane/result.json" 2> "$lane/stderr.log"
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "result_sha256=$(sha256sum "$lane/result.json" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
