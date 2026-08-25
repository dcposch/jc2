#!/bin/sh
set -eu
if [ "$#" -ne 6 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <candidate-relative> <timeout-sec> <vm-kib>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
candidate_relative=$4
timeout_seconds=$5
vm_kib=$6
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$candidate_relative" in /*|*..*) exit 2 ;; esac
case "$timeout_seconds:$vm_kib" in *[!0-9:]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_candidate_genus_aws_20260825
candidate=$repo_root/$candidate_relative
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
python3 "$case_dir/generate_branch_bound.py" --candidate "$candidate" \
  > "$lane/input.sing" 2> "$lane/generator.stderr"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "route=fail-closed resultant radical branch lower bound"
  echo "timeout_seconds=$timeout_seconds"
  echo "virtual_memory_limit_kib=$vm_kib"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate_branch_bound.py" "$case_dir/generate_v2.py" "$candidate"
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
} > "$meta"
set +e
(ulimit -v "$vm_kib"; timeout --signal=TERM --kill-after=120 "$timeout_seconds" \
  /usr/bin/time -v Singular -q < "$lane/input.sing" \
  > "$lane/result.out" 2> "$lane/stderr.log")
rc=$?
set -e
if [ "$rc" -eq 0 ] && grep -q '^   ? ' "$lane/result.out"; then rc=91; fi
if [ "$rc" -eq 0 ] && [ -s "$lane/generator.stderr" ]; then rc=92; fi
if [ "$rc" -eq 0 ] && ! grep -qx 'branch_bound_end' "$lane/result.out"; then rc=93; fi
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
