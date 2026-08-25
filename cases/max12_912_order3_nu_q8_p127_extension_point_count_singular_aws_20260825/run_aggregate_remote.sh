#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 5 ]; then
  echo "usage: $0 REPO OUTROOT TAG TIMEOUT_SECONDS VMEM_KIB" >&2
  exit 64
fi

repo=$1
outroot=$2
tag=$3
timeout_seconds=$4
vmem_kib=$5
case_rel=cases/max12_912_order3_nu_q8_p127_extension_point_count_singular_aws_20260825
outdir=$outroot/$tag
test ! -e "$outdir"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"

{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=fail-closed aggregate of independent Singular census\n'
  printf 'timeout_seconds=%s\nvirtual_memory_limit_kib=%s\n' "$timeout_seconds" "$vmem_kib"
  sha256sum "$repo/$case_rel/aggregate_singular.py" "$repo/$case_rel/run_aggregate_remote.sh"
} >"$outdir/run.meta"

set +e
(ulimit -v "$vmem_kib"; /usr/bin/time -v timeout "$timeout_seconds" \
  python3 "$repo/$case_rel/aggregate_singular.py" --root "$outroot" \
  >"$outdir/result.json" 2>"$outdir/stderr.log")
rc=$?
set -e
{
  printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc"
  sha256sum "$outdir/result.json" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
grep -q '"status": "PASS"' "$outdir/result.json" || exit 89

