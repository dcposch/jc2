#!/bin/sh
set -eu
if [ "$#" -ne 6 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <samples.json> <coordinate> <max-den-degree>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
samples=$4
coordinate=$5
maximum=$6
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$coordinate" in c|d2|d4|x1|x3|x5|inv) ;; *) exit 2 ;; esac
case "$maximum" in ''|*[!0-9]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_simultaneous_coordinate_reconstruction_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "characteristic=127"
  echo "coordinate=$coordinate"
  echo "maximum_denominator_degree=$maximum"
  sha256sum "$0" "$case_dir/reconstruct.py" "$samples" | sed 's/^/source_sha256=/'
} > "$meta"
set +e
(ulimit -v 16777216; timeout --signal=TERM --kill-after=60 3600 nice -n 5 \
  /usr/bin/time -v python3 "$case_dir/reconstruct.py" \
    --samples "$samples" --coordinate "$coordinate" \
    --maximum-denominator-degree "$maximum" \
    --output "$lane/reconstruction.json" \
  > "$lane/result.out" 2> "$lane/stderr.log")
rc=$?
set -e
endpoint=FAIL
if [ "$rc" -eq 0 ] && grep -qx 'status=PASS' "$lane/result.out"; then
  endpoint=PASS
elif [ "$rc" -eq 0 ] && grep -qx 'status=ALIAS_CEILING' "$lane/result.out"; then
  endpoint=ALIAS_CEILING
elif [ "$rc" -eq 0 ] && grep -qx 'status=NO_UNIQUE_RECONSTRUCTION' "$lane/result.out"; then
  endpoint=NO_UNIQUE_RECONSTRUCTION
else
  [ "$rc" -ne 0 ] || rc=91
fi
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "endpoint=$endpoint"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
  [ ! -f "$lane/reconstruction.json" ] || echo "reconstruction_sha256=$(sha256sum "$lane/reconstruction.json" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
