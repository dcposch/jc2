#!/bin/sh
set -eu

if [ "$#" -ne 8 ]; then
  echo "usage: $0 REPO OUTROOT TAG LOWER LOWER_ORDER UPPER UPPER_ORDER PARENT" >&2
  exit 64
fi

repo=$1
outroot=$2
tag=$3
lower=$4
lower_order=$5
upper=$6
upper_order=$7
parent=$8
case_rel=cases/max12_912_order3_nu_q8_p127_hensel_common_pade_high_aws_20260825
case_dir="$repo/$case_rel"
out="$outroot/$tag"
mkdir -p "$out"
: > "$out/result.out"
: > "$out/stderr.log"

start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  echo "start_utc=$start"
  echo "method=simultaneous-common-denominator-two-order-exact"
  echo "virtual_memory_limit_kib=16777216"
  echo "timeout_seconds=7200"
  sha256sum "$0" "$case_dir/common_pade_high.py" "$parent" "$lower" "$upper" | sed 's/^/source_sha256=/'
} > "$out/run.meta"

set +e
(
  ulimit -v 16777216
  timeout --signal=TERM --kill-after=120 7200 /usr/bin/time -v \
    python3 "$case_dir/common_pade_high.py" \
      --parent "$parent" \
      --lower "$lower" --lower-order "$lower_order" \
      --upper "$upper" --upper-order "$upper_order" \
      --output "$out/reconstruction.json"
) > "$out/result.out" 2> "$out/stderr.log"
rc=$?
set -e

end=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  echo "end_utc=$end"
  echo "rc=$rc"
} >> "$out/run.meta"

if [ "$rc" -ne 0 ]; then
  echo "endpoint=FAIL" >> "$out/run.meta"
  exit "$rc"
fi
for marker in \
  Q8-P127-HENSEL-SIMULTANEOUS-COMMON-PADE-HIGH \
  status=PASS \
  prefix_match=1
do
  count=$(grep -Fxc "$marker" "$out/result.out" || true)
  if [ "$count" -ne 1 ]; then
    echo "endpoint=FAIL marker=$marker count=$count" >> "$out/run.meta"
    exit 65
  fi
done
test -s "$out/reconstruction.json"
{
  echo "endpoint=PASS"
  sha256sum "$out/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$out/stderr.log" | sed 's/^/stderr_sha256=/'
  sha256sum "$out/reconstruction.json" | sed 's/^/reconstruction_sha256=/'
} >> "$out/run.meta"

