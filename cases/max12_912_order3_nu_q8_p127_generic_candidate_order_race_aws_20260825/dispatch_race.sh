#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then
  echo "usage: $0 <repo> <out-root> <memory-GiB-per-lane>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
memory_gib=$3
case "$memory_gib" in ''|*[!0-9]*) exit 2 ;; esac
if [ "$memory_gib" -lt 8 ] || [ "$memory_gib" -gt 32 ]; then exit 2; fi
if [ -e "$out_root" ]; then echo "duplicate output root refused" >&2; exit 3; fi
mkdir -p "$out_root"
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_generic_candidate_order_race_aws_20260825
matrix=$out_root/matrix.tsv
for engine in std slimgb; do
  for order in dp block; do
    for permutation in reverse inv-first interleave; do
      printf '%s\t%s\t%s\n' "$engine" "$order" "$permutation"
    done
  done
done > "$matrix"
for permutation in reverse inv-first interleave; do
  printf 'slimgb\tlp\t%s\n' "$permutation"
done >> "$matrix"
meta=$out_root/dispatch.meta
{
  echo "tag=q8_p127_generic_candidate_order_race_v2"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "lane_count=$(wc -l < "$matrix" | tr -d ' ')"
  echo "memory_gib_per_lane=$memory_gib"
  sha256sum "$0" "$case_dir/run_remote.sh" "$case_dir/generate.py" | sed 's/^/source_sha256=/'
  echo "matrix_sha256=$(sha256sum "$matrix" | awk '{print $1}')"
} > "$meta"
set +e
python3 "$case_dir/generate.py" --engine std --order dp --permutation reverse \
  > "$out_root/preflight.sing" 2> "$out_root/preflight.stderr"
preflight_rc=$?
set -e
{
  echo "preflight_rc=$preflight_rc"
  echo "preflight_bytes=$(wc -c < "$out_root/preflight.sing" | tr -d ' ')"
  echo "preflight_sha256=$(sha256sum "$out_root/preflight.sing" | awk '{print $1}')"
  echo "preflight_stderr_sha256=$(sha256sum "$out_root/preflight.stderr" | awk '{print $1}')"
} >> "$meta"
if [ "$preflight_rc" -ne 0 ] || [ ! -s "$out_root/preflight.sing" ]; then
  {
    echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    echo "rc=97"
    echo "failure=generator_preflight"
  } >> "$meta"
  exit 97
fi
set +e
pids=""
while IFS="$(printf '\t')" read -r engine order permutation; do
  tag=q8_candidate_${engine}_${order}_${permutation}_r6a_v2
  "$case_dir/run_remote.sh" "$repo_root" "$out_root" "$tag" \
    "$engine" "$order" "$permutation" "$memory_gib" &
  pids="$pids $!"
done < "$matrix"
rc=0
for pid in $pids; do
  if ! wait "$pid"; then rc=1; fi
done
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
} >> "$meta"
exit "$rc"
