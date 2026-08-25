#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
remote_name=REMOTE_RESULTS_as_d7_next_top_shards_20260825T001733Z
result_dir="$case_dir/$remote_name/jc2/cases/as_fonly_d7_vertical_next_top_shards_20260825/results_as_d7_next_top_shards_20260825T001733Z"
scratch=$(mktemp -d "${TMPDIR:-/tmp}/as-d7-top-shards-verify.XXXXXX")
trap 'rm -rf "$scratch"' EXIT HUP INT TERM

(
  cd "$case_dir/$remote_name"
  shasum -a 256 -c ../REMOTE_RESULTS_MANIFEST.sha256
)
python3 "$case_dir/aggregate_shards.py" "$result_dir" 27 \
  > "$scratch/aggregate.out"
cmp "$scratch/aggregate.out" "$result_dir/aggregate.out"
(
  cd "$case_dir"
  shasum -a 256 -c RESULT_MANIFEST.sha256
)
printf '%s\n' 'PASS-AS-FONLY-D7-NEXT-TOP-SHARDS-FROZEN-RESULT'
