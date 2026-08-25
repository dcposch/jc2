#!/bin/sh
set -eu
if [ "$#" -ne 5 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <order16-result> <order32-result>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
order16=$4
order32=$5
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_hensel_common_pade_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "method=simultaneous-common-denominator-order16-train-order32-holdout"
  echo "virtual_memory_limit_kib=8388608"
  echo "timeout_seconds=1800"
  sha256sum "$0" "$case_dir/common_pade.py" "$order16" "$order32" | sed 's/^/source_sha256=/'
} > "$meta"
set +e
(ulimit -v 8388608; timeout --signal=TERM --kill-after=120 1800 \
  /usr/bin/time -v python3 "$case_dir/common_pade.py" \
    --order16 "$order16" --order32 "$order32" --output "$lane/reconstruction.json" \
    > "$lane/result.out" 2> "$lane/stderr.log")
rc=$?
set -e
endpoint=FAIL
if [ "$rc" -eq 0 ] \
  && grep -qx 'status=PASS' "$lane/result.out" \
  && grep -qx 'sequence_count=1330' "$lane/result.out" \
  && grep -qx 'prefix_match=1' "$lane/result.out" \
  && [ -s "$lane/reconstruction.json" ]; then
  endpoint=PASS
else
  [ "$rc" -ne 0 ] || rc=91
fi
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "endpoint=$endpoint"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
  if [ -f "$lane/reconstruction.json" ]; then
    echo "reconstruction_sha256=$(sha256sum "$lane/reconstruction.json" | awk '{print $1}')"
  fi
} >> "$meta"
exit "$rc"
