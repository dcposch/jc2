#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 9 ]]; then
  echo "usage: $0 REPO OUT_ROOT TAG --engine ENGINE --order ORDER --permutation PERM --placement PLACE" >&2
  exit 2
fi

repo=$1
out_root=$2
tag=$3
shift 3
case_dir="$repo/cases/max12_912_order3_nu_q8_p127_candidate_seeded_quotient_aws_20260825"
out="$out_root/$tag"

if [[ -e "$out" ]]; then
  echo "refusing to overlap existing output: $out" >&2
  exit 3
fi
mkdir -p "$out"

python3 "$case_dir/generate.py" "$@" > "$out/input.sing" 2> "$out/generator.stderr"
sha256sum "$case_dir/generate.py" "$case_dir/run_remote.sh" "$out/input.sing" > "$out/input.sha256"

start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
set +e
(
  ulimit -v 67108864
  /usr/bin/time -v timeout --signal=TERM --kill-after=300 43200 nice -n 8 Singular -q < "$out/input.sing"
) > "$out/result.out" 2> "$out/stderr.log"
rc=$?
set -e
end=$(date -u +%Y-%m-%dT%H:%M:%SZ)

{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$start"
  printf 'end_utc=%s\n' "$end"
  printf 'rc=%s\n' "$rc"
  printf 'argv='
  printf '%q ' "$@"
  printf '\n'
} > "$out/run.meta"
sha256sum "$out/input.sing" "$out/generator.stderr" "$out/result.out" "$out/stderr.log" "$out/run.meta" > "$out/RESULT_MANIFEST.sha256"
exit "$rc"
