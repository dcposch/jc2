#!/usr/bin/env bash
set -u
if [ "$#" -ne 11 ]; then
  echo "usage: $0 <repo> <out-root> <tag-prefix> <prime> <start-w> <stop-w> <drl|fglm> <parallel> <threads> <seed> <timeout-per-lane>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag_prefix=$3
prime=$4
start_w=$5
stop_w=$6
mode=$7
parallel=$8
threads=$9
seed=${10}
timeout_lane=${11}
case "$tag_prefix" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$prime:$start_w:$stop_w:$parallel:$threads:$seed:$timeout_lane" in *[!0-9:]*) exit 2 ;; esac
case "$mode" in drl|fglm) ;; *) exit 2 ;; esac
if [ "$start_w" -lt 1 ] || [ "$stop_w" -lt "$start_w" ] || [ "$stop_w" -ge "$prime" ]; then exit 2; fi
case_dir=$repo_root/cases/max12_912_order3_nu_q8_box02_broad_scan_dispatch_20260825
runner=$repo_root/cases/max12_912_order3_nu_q8_box02_drl_fglm_controls_20260825/run_msolve.sh
dispatch=$out_root/$tag_prefix
lanes=$dispatch/lanes
if [ -e "$dispatch" ]; then echo "duplicate dispatch refused" >&2; exit 3; fi
mkdir -p "$lanes"
meta=$dispatch/dispatch.meta
{
  echo "tag_prefix=$tag_prefix"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=$prime"
  echo "w_range=$start_w:$stop_w"
  echo "mode=$mode"
  echo "parallel=$parallel"
  echo "threads_per_lane=$threads"
  echo "random_seed=$seed"
  echo "timeout_per_lane=$timeout_lane"
  sha256sum "$0" "$case_dir/summarize.py" "$runner" | sed 's/^/source_sha256=/'
} > "$meta"
failures=0
pids=()
for w_value in $(seq "$start_w" "$stop_w"); do
  printf -v w_padded '%03d' "$w_value"
  tag=${tag_prefix}_w${w_padded}
  "$runner" "$repo_root" "$lanes" "$tag" "$prime" "$w_value" "$mode" \
    "$threads" "$seed" "$timeout_lane" \
    > "$dispatch/$tag.supervisor.out" 2> "$dispatch/$tag.supervisor.err" &
  pids+=("$!")
  if [ "${#pids[@]}" -ge "$parallel" ]; then
    for pid in "${pids[@]}"; do wait "$pid" || failures=$((failures+1)); done
    pids=()
  fi
done
for pid in "${pids[@]}"; do wait "$pid" || failures=$((failures+1)); done
python3 "$case_dir/summarize.py" --lanes "$lanes" --prime "$prime" \
  --start "$start_w" --stop "$stop_w" --mode "$mode" > "$dispatch/summary.json"
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "lane_failures=$failures"
  echo "summary_sha256=$(sha256sum "$dispatch/summary.json" | awk '{print $1}')"
} >> "$meta"
exit "$failures"

