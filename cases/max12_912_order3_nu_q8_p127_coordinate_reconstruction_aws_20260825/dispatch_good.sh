#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then
  echo "usage: $0 <repo> <out-root> <concurrency>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
concurrency=$3
case "$concurrency" in ''|*[!0-9]*) exit 2 ;; esac
if [ "$concurrency" -lt 1 ] || [ "$concurrency" -gt 64 ]; then
  echo "concurrency must lie in 1..64" >&2
  exit 2
fi
if [ -e "$out_root" ]; then echo "duplicate output root refused" >&2; exit 3; fi
mkdir -p "$out_root"
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825
values=$out_root/values.txt
for w_value in $(seq 1 126); do
  case "$w_value" in 25|39|56|125) continue ;; esac
  echo "$w_value"
done > "$values"
meta=$out_root/dispatch.meta
{
  echo "tag=q8_p127_coordinate_shape_123_good_fibres_v1"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=127"
  echo "excluded_existing_w=25"
  echo "excluded_nonshape_w=39,56,125"
  echo "expected_lane_count=$(wc -l < "$values" | tr -d ' ')"
  echo "concurrency=$concurrency"
  sha256sum "$0" "$case_dir/run_one.sh" "$case_dir/generate.py" | sed 's/^/source_sha256=/'
  echo "values_sha256=$(sha256sum "$values" | awk '{print $1}')"
} > "$meta"
set +e
xargs -P "$concurrency" -n 1 sh -c \
  '"$1/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825/run_one.sh" "$1" "$2" "q8_p127_coordinate_shape_w${3}_v1" "$3"' \
  worker "$repo_root" "$out_root" < "$values"
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
} >> "$meta"
exit "$rc"
