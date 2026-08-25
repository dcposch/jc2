#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then
  echo "usage: $0 <repo> <out-root> <tag>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_rational_etale_point_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  sha256sum "$0" "$case_dir/audit.py" | sed 's/^/source_sha256=/'
} > "$meta"
set +e
python3 "$case_dir/audit.py" > "$lane/audit.json" 2> "$lane/stderr.log"
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/audit.json" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
