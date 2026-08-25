#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 10 ]; then
  echo "usage: $0 REPO OUTROOT TAG PRIME MODE ENGINE ORDER PRINT_BASIS TIMEOUT_SECONDS VMEM_KIB" >&2
  exit 64
fi

repo=$1
outroot=$2
tag=$3
prime=$4
mode=$5
engine=$6
order=$7
print_basis=$8
timeout_seconds=$9
vmem_kib=${10}
case_rel=cases/max12_912_order3_nu_q8_w0_fibre_stratification_aws_20260825
parent_rel=cases/max12_912_order3_nu_q8_global_quotient_probe_20260824
outdir=$outroot/$tag

test ! -e "$outdir"
test "$print_basis" = yes || test "$print_basis" = no
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"

generator_args=(--prime "$prime" --mode "$mode" --engine "$engine" --order "$order")
if [ "$print_basis" = yes ]; then generator_args+=(--print-basis); fi
python3 "$repo/$case_rel/generate.py" "${generator_args[@]}" >"$outdir/input.sing"

{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=localized six-row w=0 fibre stratification\n'
  printf 'prime=%s\nmode=%s\nengine=%s\norder=%s\nprint_basis=%s\n' \
    "$prime" "$mode" "$engine" "$order" "$print_basis"
  printf 'timeout_seconds=%s\nvirtual_memory_limit_kib=%s\n' "$timeout_seconds" "$vmem_kib"
  Singular --version | head -1
  sha256sum "$repo/$case_rel/generate.py" "$repo/$case_rel/run_remote.sh" \
    "$repo/$case_rel/PREREGISTRATION.md" "$repo/$case_rel/PREREGISTRATION.manifest.sha256" \
    "$repo/$parent_rel/quotient_compiler.py" "$repo/$parent_rel/MANIFEST.sha256" \
    "$outdir/input.sing"
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
grep -qx 'Q8_W0_FIBRE_STRATUM_PASS' "$outdir/singular.stdout" || exit 89
grep -qx 'original_remainder_zero=1' "$outdir/singular.stdout" || exit 90

