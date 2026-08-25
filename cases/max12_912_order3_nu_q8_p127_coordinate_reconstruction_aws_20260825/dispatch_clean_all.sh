#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: $0 <repo> <out-root> <tag-prefix> <parallelism>" >&2
  exit 2
fi

repo_root=$1
out_root=$2
tag_prefix=$3
parallelism=$4
case "$tag_prefix" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$parallelism" in ''|*[!0-9]*) exit 2 ;; esac
if (( parallelism < 1 || parallelism > 96 )); then exit 2; fi

case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825
runner=$case_dir/run_clean_control.sh
dispatch_dir=$out_root/${tag_prefix}_dispatch
if [[ -e $dispatch_dir ]]; then
  echo "duplicate dispatch refused" >&2
  exit 3
fi
mkdir -p "$dispatch_dir"
{
  echo "tag_prefix=$tag_prefix"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "w_values=1..126"
  echo "parallelism=$parallelism"
  echo "route=corrected pure-Singular fixed-fibre stdfglm shape fanout"
  sha256sum "$0" "$runner" "$case_dir/generate_clean.py" "$case_dir/generate.py"
} > "$dispatch_dir/run.meta"

active=0
failure=0
declare -a pids=()
for w_value in $(seq 1 126); do
  tag=${tag_prefix}_w${w_value}
  (
    "$runner" "$repo_root" "$out_root" "$tag" "$w_value"
  ) > "$dispatch_dir/w${w_value}.supervisor.stdout" \
    2> "$dispatch_dir/w${w_value}.supervisor.stderr" &
  pids+=("$!")
  ((active += 1))
  if (( active >= parallelism )); then
    if ! wait -n; then failure=1; fi
    ((active -= 1))
  fi
done
for pid in "${pids[@]}"; do
  if kill -0 "$pid" 2>/dev/null; then
    if ! wait "$pid"; then failure=1; fi
  fi
done

pass_count=0
fail_count=0
unfinished_count=0
for w_value in $(seq 1 126); do
  lane=$out_root/${tag_prefix}_w${w_value}
  if [[ ! -f $lane/run.meta ]]; then
    ((unfinished_count += 1))
  elif grep -qx 'rc=0' "$lane/run.meta"; then
    ((pass_count += 1))
  else
    ((fail_count += 1))
  fi
done
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "pass_count=$pass_count"
  echo "fail_count=$fail_count"
  echo "unfinished_count=$unfinished_count"
  echo "failure_flag=$failure"
} >> "$dispatch_dir/run.meta"

if (( failure != 0 || fail_count != 0 || unfinished_count != 0 || pass_count != 126 )); then
  exit 1
fi
