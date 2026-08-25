#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 1 ]; then
  echo "usage: $0 OUTDIR" >&2
  exit 64
fi
outdir=$1
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
tag=$(basename -- "$outdir")
mkdir -p "$outdir"
exec >"$outdir/runner.stdout" 2>"$outdir/runner.stderr"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'route=degree122 polynomial interpolation then exact all-row modulo-H substitution\n'
  printf 'timeout_seconds=14400\n'
  printf 'virtual_memory_limit_kib=268435456\n'
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate_polynomial_graph.py"
} >"$outdir/run.meta"
python3 "$case_dir/generate_polynomial_graph.py" --stats "$outdir/generator_stats.json" >"$outdir/input.sing"
sha256sum "$outdir/input.sing" "$outdir/generator_stats.json" >>"$outdir/run.meta"
set +e
(ulimit -v 268435456; /usr/bin/time -v timeout 14400 Singular -q <"$outdir/input.sing" >"$outdir/result.out" 2>"$outdir/stderr.log")
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
  sha256sum "$outdir/result.out" "$outdir/stderr.log"
} >>"$outdir/run.meta"
if [ "$rc" -ne 0 ]; then
  exit "$rc"
fi
if grep -q '^   ? ' "$outdir/result.out"; then
  exit 89
fi
grep -qx 'Q8-P127-POLYNOMIAL-GRAPH-SUBSTITUTION-END' "$outdir/result.out" || exit 90
for label in e1 e3 e5 e7 e2 e4 einv ev; do
  grep -qx "${label}_zero=1" "$outdir/result.out" || exit 91
done
