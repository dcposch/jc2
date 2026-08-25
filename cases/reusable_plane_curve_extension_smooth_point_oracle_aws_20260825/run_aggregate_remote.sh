#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 11 ]; then
  echo "usage: $0 REPO OUTROOT TAG PREFIX CURVE_REL CURVE_SHA256 MODULUS LANES TIMEOUT_SECONDS VMEM_KIB CASE_REL" >&2
  exit 64
fi

repo=$1
outroot=$2
tag=$3
prefix=$4
curve_rel=$5
curve_sha256=$6
modulus=$7
lanes=$8
timeout_seconds=$9
vmem_kib=${10}
case_rel=${11}
outdir=$outroot/$tag

test ! -e "$outdir"
test -f "$repo/$curve_rel"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"

generator_sha256=$(sha256sum "$repo/$case_rel/generate_singular.py" | cut -d' ' -f1)
runner_sha256=$(sha256sum "$repo/$case_rel/run_remote.sh" | cut -d' ' -f1)

{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=reusable extension-field smooth-point aggregate\n'
  printf 'prefix=%s\ncurve_rel=%s\ncurve_sha256=%s\nmodulus=%s\nlanes=%s\n' \
    "$prefix" "$curve_rel" "$curve_sha256" "$modulus" "$lanes"
  printf 'timeout_seconds=%s\nvirtual_memory_limit_kib=%s\n' "$timeout_seconds" "$vmem_kib"
  sha256sum "$repo/$case_rel/generate_singular.py" \
    "$repo/$case_rel/run_remote.sh" "$repo/$case_rel/aggregate.py" \
    "$repo/$case_rel/run_aggregate_remote.sh" "$repo/$curve_rel"
} >"$outdir/run.meta"

set +e
(ulimit -v "$vmem_kib"; /usr/bin/time -v timeout "$timeout_seconds" \
  python3 "$repo/$case_rel/aggregate.py" \
    --repo "$repo" --root "$outroot" --prefix "$prefix" \
    --curve "$repo/$curve_rel" --curve-sha256 "$curve_sha256" \
    --modulus "$modulus" --lanes "$lanes" \
    --generator-sha256 "$generator_sha256" --runner-sha256 "$runner_sha256" \
    >"$outdir/result.json" 2>"$outdir/stderr.log")
rc=$?
set -e

{
  printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc"
  sha256sum "$outdir/result.json" "$outdir/stderr.log"
} >>"$outdir/run.meta"

if [ "$rc" -ne 0 ]; then exit "$rc"; fi
if grep -Eiq 'traceback|error|mismatch|failure' "$outdir/result.json" "$outdir/stderr.log"; then
  exit 88
fi
grep -q '"status": "PASS"' "$outdir/result.json" || exit 89

