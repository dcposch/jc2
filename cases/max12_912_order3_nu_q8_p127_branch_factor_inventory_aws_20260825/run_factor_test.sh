#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 6 ]; then
  echo "usage: $0 REPO OUTROOT TAG INDEX TIMEOUT_SECONDS VMEM_KIB" >&2
  exit 64
fi
repo=$1
outroot=$2
tag=$3
index=$4
timeout_seconds=$5
vmem_kib=$6
case_rel=cases/max12_912_order3_nu_q8_p127_branch_factor_inventory_aws_20260825
outdir=$outroot/$tag
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=exact branch-factor common-gcd over finite extension\n'
  printf 'factor_index=%s\n' "$index"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_limit_kib=%s\n' "$vmem_kib"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$repo/$case_rel/run_factor_test.sh" "$repo/$case_rel/generate_factor_test.py" \
    "$repo/$case_rel/aws_r6d_v1/result.out" \
    "$repo/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json"
} >"$outdir/run.meta"
python3 "$repo/$case_rel/generate_factor_test.py" --index "$index" >"$outdir/input.sing"
sha256sum "$outdir/input.sing" >>"$outdir/run.meta"
set +e
(ulimit -v "$vmem_kib"; /usr/bin/time -v timeout "$timeout_seconds" Singular -q <"$outdir/input.sing" >"$outdir/result.out" 2>"$outdir/stderr.log")
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
  sha256sum "$outdir/result.out" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
if grep -q '^   ? ' "$outdir/result.out"; then exit 89; fi
grep -qx "factor_index=$index" "$outdir/result.out" || exit 90
grep -qx 'factor_test_end' "$outdir/result.out" || exit 91
