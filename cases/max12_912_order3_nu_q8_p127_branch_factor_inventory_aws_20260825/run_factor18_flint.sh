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
case_rel=cases/max12_912_order3_nu_q8_p127_branch_factor_inventory_aws_20260825
outdir=$outroot/$tag
python_bin=${PYTHON_BIN:-/home/ubuntu/venvs/td6/bin/python}
test ! -e "$outdir"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=independent python-flint branch-factor gcd\n'
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_limit_kib=%s\n' "$vmem_kib"
  "$python_bin" -c 'import flint; print("python_flint="+flint.__version__)'
  sha256sum "$repo/$case_rel/run_factor18_flint.sh" \
    "$repo/$case_rel/factor18_flint.py" \
    "$repo/$case_rel/aws_r6d_v1/result.out" \
    "$repo/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json"
} >"$outdir/run.meta"
set +e
(ulimit -v "$vmem_kib"; /usr/bin/time -v timeout "$timeout_seconds" \
  "$python_bin" "$repo/$case_rel/factor18_flint.py" \
  >"$outdir/result.out" 2>"$outdir/stderr.log")
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
  sha256sum "$outdir/result.out" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
grep -qx 'factor_irreducible=1' "$outdir/result.out" || exit 89
grep -qx 'factor_degree=1243' "$outdir/result.out" || exit 90
grep -qx 'singular_gcd_degree=0' "$outdir/result.out" || exit 91
grep -qx 'factor18_flint_end' "$outdir/result.out" || exit 93
