#!/bin/sh
set -eu
if [ "$#" -ne 5 ]; then
  echo "usage: $0 <repo> <samples> <out-root> <tag> <memory-GiB>" >&2
  exit 2
fi
repo_root=$1
samples=$2
out_root=$3
tag=$4
memory_gib=$5
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$memory_gib" in ''|*[!0-9]*) exit 2 ;; esac
if [ "$memory_gib" -lt 4 ] || [ "$memory_gib" -gt 64 ]; then exit 2; fi
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825
memory_kib=$((memory_gib * 1024 * 1024))
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "route=common-denominator Pade reconstruction"
  echo "virtual_memory_limit_kib=$memory_kib"
  echo "timeout_seconds=7200"
  sha256sum "$0" "$case_dir/rational_reconstruct.py" "$samples" | sed 's/^/source_sha256=/'
} > "$meta"
set +e
(ulimit -v "$memory_kib"; timeout --signal=TERM --kill-after=120 7200 \
  /usr/bin/time -v python3 "$case_dir/rational_reconstruct.py" \
  --samples "$samples" --output "$lane/reconstruction.json" \
  > "$lane/result.out" 2> "$lane/stderr.log")
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
  if [ -f "$lane/reconstruction.json" ]; then
    echo "reconstruction_sha256=$(sha256sum "$lane/reconstruction.json" | awk '{print $1}')"
  fi
} >> "$meta"
exit "$rc"
