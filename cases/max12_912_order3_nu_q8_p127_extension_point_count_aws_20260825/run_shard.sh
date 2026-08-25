#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 7 ]; then
  echo "usage: $0 REPO OUTROOT TAG START STOP TIMEOUT_SECONDS VMEM_KIB" >&2
  exit 64
fi
repo=$1
outroot=$2
tag=$3
start=$4
stop=$5
timeout_seconds=$6
vmem_kib=$7
case_rel=cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825
candidate_rel=cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json
python_bin=${PYTHON_BIN:-/home/ubuntu/venvs/td6/bin/python}
outdir=$outroot/$tag
test ! -e "$outdir"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=exact F_127^2 smooth-affine point-count shard\n'
  printf 'start=%s\nstop=%s\n' "$start" "$stop"
  printf 'timeout_seconds=%s\nvirtual_memory_limit_kib=%s\n' "$timeout_seconds" "$vmem_kib"
  "$python_bin" -c 'import flint; print("python_flint="+flint.__version__)'
  sha256sum "$repo/$case_rel/run_shard.sh" "$repo/$case_rel/count_shard.py" \
    "$repo/$candidate_rel"
} >"$outdir/run.meta"
set +e
(ulimit -v "$vmem_kib"; /usr/bin/time -v timeout "$timeout_seconds" \
  "$python_bin" "$repo/$case_rel/count_shard.py" \
  --candidate "$repo/$candidate_rel" --start "$start" --stop "$stop" \
  >"$outdir/result.json" 2>"$outdir/stderr.log")
rc=$?
set -e
{
  printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc"
  sha256sum "$outdir/result.json" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
grep -q '"status": "PASS"' "$outdir/result.json" || exit 89

