#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 1 ]; then
  echo "usage: $0 OUTDIR" >&2
  exit 64
fi
outdir=$1
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo=$(CDPATH= cd -- "$case_dir/../.." && pwd)
mkdir -p "$outdir"
exec >"$outdir/result.out" 2>"$outdir/stderr.log"
start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  printf 'tag=q8_p127_clean_graph_shape_audit_v1\n'
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$start"
  printf 'route=fail-closed clean fixed-fibre graph extraction\n'
  sha256sum "$0" "$case_dir/parse_clean.py" \
    "$repo/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825/parse_shape.py" \
    "$repo/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json"
} >"$outdir/run.meta"
set +e
/usr/bin/time -v timeout 1800 python3 "$case_dir/parse_clean.py" \
  --clean-root "$case_dir/clean_fibres" \
  --candidate "$repo/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json" \
  --helpers "$repo/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825/parse_shape.py" \
  --output "$outdir/clean_samples.json"
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
  if [ -f "$outdir/clean_samples.json" ]; then
    sha256sum "$outdir/clean_samples.json"
  fi
  sha256sum "$outdir/result.out" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then
  exit "$rc"
fi
grep -qx 'status=PASS' "$outdir/result.out" || exit 90
grep -qx 'fibre_count=126' "$outdir/result.out" || exit 91
grep -qx 'good_fibre_count=123' "$outdir/result.out" || exit 92
grep -qx 'singular_diagnostic_count=0' "$outdir/result.out" || exit 93
