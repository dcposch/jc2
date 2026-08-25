#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then
  echo "usage: $0 REPO OUTROOT SHAPE_SAMPLES VALUES_FILE" >&2
  exit 64
fi
repo=$1
outroot=$2
samples=$3
values=$4
case_dir=$repo/cases/max12_912_order3_nu_q8_p127_breadth_order8_aws_20260825
runner=$case_dir/run_one.sh
mkdir -p "$outroot"
if [ -e "$outroot/dispatch.meta" ]; then echo "duplicate dispatch refused" >&2; exit 65; fi
sha256sum "$0" "$runner" "$case_dir/generate_breadth.py" "$values" "$samples" > "$outroot/dispatch.sources.sha256"
: > "$outroot/dispatch.pids"
: > "$outroot/dispatch.meta"
seen=' '
count=0
while IFS= read -r w; do
  [ -n "$w" ] || continue
  case "$w" in *[!0-9]*) echo "bad w=$w" >&2; exit 66 ;; esac
  case "$seen" in *" $w "*) echo "duplicate w=$w" >&2; exit 66 ;; esac
  seen="$seen$w "
  tag=$(printf 'q8_p127_breadth_w%03d_order8_v1' "$w")
  nohup "$runner" "$repo" "$outroot" "$samples" "$w" \
    > "$outroot/$tag.dispatch.out" 2> "$outroot/$tag.dispatch.err" &
  pid=$!
  echo "$w $pid" >> "$outroot/dispatch.pids"
  count=$((count+1))
done < "$values"
{
  echo "host=$(hostname)"
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "lane_count=$count"
  echo "order=8"
} > "$outroot/dispatch.meta"
echo "launched=$count"
