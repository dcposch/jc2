#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 8 ] || [ "$#" -gt 9 ]; then
  echo "usage: $0 REPO OUTROOT TAG MODE START STOP TIMEOUT_SECONDS VMEM_KIB [REFERENCE]" >&2
  exit 64
fi

repo=$1
outroot=$2
tag=$3
mode=$4
start=$5
stop=$6
timeout_seconds=$7
vmem_kib=$8
reference=${9:-}
case_rel=cases/max12_912_order3_nu_q8_p127_extension_point_count_singular_aws_20260825
candidate_rel=cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json
outdir=$outroot/$tag

test "$mode" = controls || test "$mode" = shard
test ! -e "$outdir"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"

generator_args=(
  --candidate "$repo/$candidate_rel"
  --mode "$mode"
  --start "$start"
  --stop "$stop"
)
if [ "$mode" = shard ]; then
  test -n "$reference"
  generator_args+=(--reference "$reference")
fi

python3 "$repo/$case_rel/generate_singular.py" "${generator_args[@]}" >"$outdir/input.sing"

{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=independent Singular F_127^2 fibre gcd count\n'
  printf 'mode=%s\nstart=%s\nstop=%s\n' "$mode" "$start" "$stop"
  printf 'timeout_seconds=%s\nvirtual_memory_limit_kib=%s\n' "$timeout_seconds" "$vmem_kib"
  Singular --version | head -1
  sha256sum "$repo/$case_rel/generate_singular.py" \
    "$repo/$case_rel/run_remote.sh" "$repo/$candidate_rel" "$outdir/input.sing"
  if [ -n "$reference" ]; then sha256sum "$reference"; fi
} >"$outdir/run.meta"

set +e
(ulimit -v "$vmem_kib"; /usr/bin/time -v timeout "$timeout_seconds" \
  Singular -q "$outdir/input.sing" >"$outdir/singular.stdout" 2>"$outdir/singular.stderr")
rc=$?
set -e

{
  printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc"
  sha256sum "$outdir/singular.stdout" "$outdir/singular.stderr"
} >>"$outdir/run.meta"

if [ "$rc" -ne 0 ]; then exit "$rc"; fi
if grep -Eiq 'error occurred|not defined|wrong type|parse error|SINGULAR_COUNT_MISMATCH|FAILURE' \
  "$outdir/singular.stdout" "$outdir/singular.stderr"; then
  exit 88
fi
if [ "$mode" = controls ]; then
  grep -qx 'SINGULAR_FQ2_CONTROLS_PASS' "$outdir/singular.stdout" || exit 89
else
  grep -qx 'SINGULAR_FQ2_SHARD_PASS' "$outdir/singular.stdout" || exit 89
fi

