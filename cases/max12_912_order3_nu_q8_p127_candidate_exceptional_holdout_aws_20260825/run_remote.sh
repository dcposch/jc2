#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 5 ]]; then
  echo "usage: $0 REPO OUT_ROOT TAG FIBRE_ROOT [FIBRE_ROOT ...]" >&2
  exit 2
fi
repo=$1
out_root=$2
tag=$3
shift 3
case_dir="$repo/cases/max12_912_order3_nu_q8_p127_candidate_exceptional_holdout_aws_20260825"
out="$out_root/$tag"
if [[ -e "$out" ]]; then
  echo "refusing to overlap existing output: $out" >&2
  exit 3
fi
mkdir -p "$out"
start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
set +e
/usr/bin/time -v timeout 600 python3 "$case_dir/exceptional_holdout.py" "$@" \
  > "$out/result.json" 2> "$out/stderr.log"
rc=$?
set -e
end=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$start"
  printf 'end_utc=%s\n' "$end"
  printf 'rc=%s\n' "$rc"
} > "$out/run.meta"
sha256sum "$case_dir/exceptional_holdout.py" "$case_dir/run_remote.sh" \
  "$out/result.json" "$out/stderr.log" "$out/run.meta" > "$out/RESULT_MANIFEST.sha256"
exit "$rc"
