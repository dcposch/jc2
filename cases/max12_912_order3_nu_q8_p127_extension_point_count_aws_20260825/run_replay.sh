#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 3 ]; then
  echo "usage: $0 REPO OUTROOT TAG" >&2
  exit 64
fi
repo=$1
outroot=$2
tag=$3
case_rel=cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825
outdir=$outroot/$tag
test ! -e "$outdir"
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"
{
  printf 'tag=%s\nhost=%s\nstart_utc=%s\n' \
    "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=portable stdlib frozen-custody replay\n'
  python3 --version
  sha256sum "$repo/$case_rel/replay.py" "$repo/$case_rel/run_replay.sh"
} >"$outdir/run.meta"
set +e
/usr/bin/time -v python3 "$repo/$case_rel/replay.py" \
  >"$outdir/result.json" 2>"$outdir/stderr.log"
rc=$?
set -e
{
  printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc"
  sha256sum "$outdir/result.json" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
grep -Eq '^[[:space:]]*"status": "PASS"' "$outdir/result.json" || exit 89
