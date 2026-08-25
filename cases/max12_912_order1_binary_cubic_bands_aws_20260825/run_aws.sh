#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 OUTDIR STRATUM" >&2
  exit 64
fi

outdir=$1
stratum=$2
case "$stratum" in
  triple|double|squarefree) ;;
  *) echo "invalid stratum: $stratum" >&2; exit 65 ;;
esac

mkdir -p "$outdir"
case_dir=$(cd "$(dirname "$0")" && pwd)
sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/compile_bands.py" \
  "$case_dir/compose_sat_interface.py" "$case_dir/run_aws.sh" \
  > "$outdir/SOURCE.sha256"
python3 --version > "$outdir/python.version" 2>&1
Singular --version > "$outdir/singular.version" 2>&1
date -u +%Y-%m-%dT%H:%M:%SZ > "$outdir/start_utc"

/usr/bin/time -v timeout 3600 python3 "$case_dir/compile_bands.py" \
  --stratum "$stratum" --outdir "$outdir" \
  > "$outdir/compiler.stdout" 2> "$outdir/compiler.stderr"
grep -q '"PASS": true' "$outdir/compiler.stdout"

/usr/bin/time -v timeout 3600 Singular "$outdir/obstruction.sing" \
  > "$outdir/singular.stdout" 2> "$outdir/singular.stderr"
grep -qx 'PASS' "$outdir/singular.stdout"

if [[ "$stratum" == "squarefree" ]]; then
  /usr/bin/time -v timeout 60 python3 "$case_dir/compose_sat_interface.py" \
    > "$outdir/sat_interface.stdout" 2> "$outdir/sat_interface.stderr"
  grep -q '"PASS": true' "$outdir/sat_interface.stdout"
  cp "$case_dir/sat_interface_result.json" "$outdir/sat_interface_result.json"
fi

date -u +%Y-%m-%dT%H:%M:%SZ > "$outdir/end_utc"
sha256sum "$outdir"/* > "$outdir/OUTPUT.sha256.tmp"
mv "$outdir/OUTPUT.sha256.tmp" "$outdir/OUTPUT.sha256"
echo "PASS $stratum"

