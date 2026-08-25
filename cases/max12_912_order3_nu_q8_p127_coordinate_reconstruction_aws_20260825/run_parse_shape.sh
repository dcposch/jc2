#!/bin/sh
set -eu
if [ "$#" -ne 6 ]; then
  echo "usage: $0 <repo> <sweep-root> <w25-lane> <candidate> <out-root> <tag>" >&2
  exit 2
fi
repo_root=$1
sweep_root=$2
w25_lane=$3
candidate=$4
out_root=$5
tag=$6
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "route=exact shape parser and candidate-specialization audit"
  sha256sum "$0" "$case_dir/parse_shape.py" "$candidate" | sed 's/^/source_sha256=/'
} > "$meta"
set +e
/usr/bin/time -v python3 "$case_dir/parse_shape.py" \
  --sweep-root "$sweep_root" --w25-lane "$w25_lane" --candidate "$candidate" \
  --output "$lane/shape_samples.json" > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
  if [ -f "$lane/shape_samples.json" ]; then
    echo "shape_samples_sha256=$(sha256sum "$lane/shape_samples.json" | awk '{print $1}')"
  fi
} >> "$meta"
exit "$rc"
