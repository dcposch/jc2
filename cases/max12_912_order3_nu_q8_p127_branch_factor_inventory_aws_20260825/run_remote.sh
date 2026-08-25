#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 5 ]; then
  echo "usage: $0 REPO OUTROOT TAG CANDIDATE TIMEOUT_SECONDS" >&2
  exit 64
fi
repo=$1
outroot=$2
tag=$3
candidate_rel=$4
timeout_seconds=$5
case_rel=cases/max12_912_order3_nu_q8_p127_branch_factor_inventory_aws_20260825
outdir=$outroot/$tag
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=exact squarefree discriminant factor inventory\n'
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_limit_kib=33554432\n'
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$repo/$case_rel/run_remote.sh" "$repo/$case_rel/generate.py" \
    "$repo/cases/max12_912_order3_nu_q8_p127_candidate_genus_aws_20260825/generate_v2.py" \
    "$repo/$candidate_rel"
} >"$outdir/run.meta"
python3 "$repo/$case_rel/generate.py" --candidate "$repo/$candidate_rel" >"$outdir/input.sing"
sha256sum "$outdir/input.sing" >>"$outdir/run.meta"
set +e
(ulimit -v 33554432; /usr/bin/time -v timeout "$timeout_seconds" Singular -q <"$outdir/input.sing" >"$outdir/result.out" 2>"$outdir/stderr.log")
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
  sha256sum "$outdir/result.out" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
if grep -q '^   ? ' "$outdir/result.out"; then exit 89; fi
grep -qx 'radical_degree=1746' "$outdir/result.out" || exit 90
grep -qx 'factor_degree_sum=1746' "$outdir/result.out" || exit 91
grep -qx 'factor_inventory_end' "$outdir/result.out" || exit 92
