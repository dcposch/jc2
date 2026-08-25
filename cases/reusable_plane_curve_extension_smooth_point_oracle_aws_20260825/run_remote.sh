#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 11 ]; then
  echo "usage: $0 REPO OUTROOT TAG CURVE_REL CURVE_SHA256 MODULUS START STOP TIMEOUT_SECONDS VMEM_KIB CASE_REL" >&2
  exit 64
fi

repo=$1
outroot=$2
tag=$3
curve_rel=$4
curve_sha256=$5
modulus=$6
start=$7
stop=$8
timeout_seconds=$9
vmem_kib=${10}
case_rel=${11}
outdir=$outroot/$tag

test ! -e "$outdir"
test -f "$repo/$curve_rel"
test -f "$repo/$case_rel/generate_singular.py"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"

python3 "$repo/$case_rel/generate_singular.py" \
  --curve "$repo/$curve_rel" \
  --curve-sha256 "$curve_sha256" \
  --modulus "$modulus" \
  --start "$start" --stop "$stop" >"$outdir/input.sing"

{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=reusable extension-field smooth-point oracle\n'
  printf 'curve_rel=%s\ncurve_sha256=%s\nmodulus=%s\n' "$curve_rel" "$curve_sha256" "$modulus"
  printf 'start=%s\nstop=%s\n' "$start" "$stop"
  printf 'timeout_seconds=%s\nvirtual_memory_limit_kib=%s\n' "$timeout_seconds" "$vmem_kib"
  Singular --version | head -1
  sha256sum "$repo/$case_rel/generate_singular.py" \
    "$repo/$case_rel/run_remote.sh" "$repo/$curve_rel" "$outdir/input.sing"
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
if grep -Eiq 'error occurred|not defined|wrong type|parse error|FAILURE' \
  "$outdir/singular.stdout" "$outdir/singular.stderr"; then
  exit 88
fi
grep -qx 'EXTENSION_SMOOTH_POINT_ORACLE_SHARD_PASS' "$outdir/singular.stdout" || exit 89

