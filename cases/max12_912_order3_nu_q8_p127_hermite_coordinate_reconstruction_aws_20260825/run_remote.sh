#!/bin/sh
set -eu

if [ "$#" -ne 10 ]; then
  echo "usage: $0 REPO OUTROOT TAG SHAPE PARENT HELPER LOWER LOWER_ORDER UPPER UPPER_ORDER" >&2
  exit 64
fi
repo=$1
outroot=$2
tag=$3
shape=$4
parent=$5
helper=$6
lower=$7
lower_order=$8
upper=$9
shift 9
upper_order=$1
case_rel=cases/max12_912_order3_nu_q8_p127_hermite_coordinate_reconstruction_aws_20260825
case_dir="$repo/$case_rel"
out="$outroot/$tag"
if [ -e "$out" ]; then
  echo "duplicate lane refused" >&2
  exit 65
fi
mkdir -p "$out"
: > "$out/result.out"
: > "$out/stderr.log"
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "method=exact-Hermite-Pade-fibres-plus-moving-v-jets"
  echo "virtual_memory_limit_kib=33554432"
  echo "timeout_seconds=7200"
  sha256sum "$0" "$case_dir/reconstruct_hermite.py" "$shape" "$parent" "$helper" "$lower" "$upper" | sed 's/^/source_sha256=/'
} > "$out/run.meta"

set +e
(
  ulimit -v 33554432
  timeout --signal=TERM --kill-after=120 7200 /usr/bin/time -v \
    python3 "$case_dir/reconstruct_hermite.py" \
      --shape "$shape" --parent "$parent" --poly-helper "$helper" \
      --lower "$lower" --lower-order "$lower_order" \
      --upper "$upper" --upper-order "$upper_order" \
      --output "$out/reconstruction.json"
) > "$out/result.out" 2> "$out/stderr.log"
rc=$?
set -e
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
  echo "rc=$rc"
} >> "$out/run.meta"
if [ "$rc" -ne 0 ]; then
  echo "endpoint=FAIL" >> "$out/run.meta"
  exit "$rc"
fi
for marker in \
  Q8-P127-HERMITE-COORDINATE-RECONSTRUCTION \
  status=PASS \
  jet_prefix_match=1 \
  base_fibre_match_all_1330=1
do
  count=$(grep -Fxc "$marker" "$out/result.out" || true)
  if [ "$count" -ne 1 ]; then
    echo "endpoint=FAIL marker=$marker count=$count" >> "$out/run.meta"
    exit 66
  fi
done
test -s "$out/reconstruction.json"
{
  echo "endpoint=PASS"
  sha256sum "$out/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$out/stderr.log" | sed 's/^/stderr_sha256=/'
  sha256sum "$out/reconstruction.json" | sed 's/^/reconstruction_sha256=/'
} >> "$out/run.meta"

