#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 6 ]; then
  echo "usage: $0 REPO OUTROOT PREFIX SHARD_COUNT TAG PYTHON_BIN" >&2
  exit 64
fi
repo=$1
outroot=$2
prefix=$3
shard_count=$4
tag=$5
python_bin=$6
case_rel=cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825
outdir=$outroot/$tag
test ! -e "$outdir"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"
results=()
{
  printf 'tag=%s\nhost=%s\nstart_utc=%s\n' \
    "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=fail-closed exact F_127^2 point-count aggregate\n'
  printf 'prefix=%s\nshard_count=%s\n' "$prefix" "$shard_count"
  "$python_bin" -c 'import flint; print("python_flint="+flint.__version__)'
  sha256sum "$repo/$case_rel/run_aggregate.sh" "$repo/$case_rel/aggregate.py" \
    "$repo/$case_rel/run_shard.sh" "$repo/$case_rel/count_shard.py"
  for ((index=0; index<shard_count; index++)); do
    shard=$(printf '%s_i%02d' "$prefix" "$index")
    dir=$outroot/$shard
    grep -qx 'rc=0' "$dir/run.meta"
    grep -Eq '^[[:space:]]*"status": "PASS",$' "$dir/result.json"
    results+=("$dir/result.json")
    sha256sum "$dir/result.json" "$dir/run.meta" "$dir/stderr.log"
  done
} >"$outdir/run.meta"
set +e
/usr/bin/time -v "$python_bin" "$repo/$case_rel/aggregate.py" "${results[@]}" \
  >"$outdir/result.json" 2>"$outdir/stderr.log"
rc=$?
set -e
{
  printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc"
  sha256sum "$outdir/result.json" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
grep -qx '  "genus_positive_if_geometrically_integral": true,' "$outdir/result.json" || exit 89
grep -qx '  "smooth_rational_affine_point_count": 16168,' "$outdir/result.json" || exit 90
