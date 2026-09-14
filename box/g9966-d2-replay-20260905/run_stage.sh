#!/usr/bin/env bash
# Exact-Q D2-floor replay of one (branch, stage) on the pinned qstar_reduce.
# usage: run_stage.sh <delta2|delta52> <stage> [timeout_seconds]
set -euo pipefail
branch=${1:?branch}
stage=${2:?stage}
TO=${3:-12000}
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"
case "$branch" in
  delta2) outdir="$HERE/runs/delta2" ;;
  delta52) outdir="$HERE/runs/delta52" ;;
  *) echo "branch must be delta2 or delta52" >&2; exit 2 ;;
esac
mkdir -p "$outdir"
json="$outdir/stage${stage}.json"
sing="$outdir/stage${stage}.sing"
err="$outdir/stage${stage}.err"
tm="$outdir/stage${stage}.time"
if [[ -e $json || -e $sing ]]; then
  echo "refusing to overwrite $json" >&2
  exit 4
fi
export PYTHONHASHSEED=0 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1 FLINT_NUM_THREADS=1
echo "LAUNCHED branch=$branch stage=$stage timeout=$TO pwd=$HERE"
set +e
/usr/bin/time -v -o "$tm" \
  timeout --signal=TERM --kill-after=30s "$TO" \
  python3 -u "$HERE/replay_engine.py" --branch "$branch" --stage "$stage" \
    --emit-singular "$sing" \
    >"$json" 2>"$err"
status=$?
set -e
echo "STATUS=$status branch=$branch stage=$stage"
if [[ -s $json ]]; then
  python3 - "$json" <<'PY'
import json,sys
p=sys.argv[1]
d=json.load(open(p))
je=d.get("joint_elimination",{})
sg=je.get("singular",{})
print("VERDICT:", d.get("verdict"))
print("dimension =", d.get("counts",{}).get("exact_Krull_dimension_localized"))
print("unit_ideal =", sg.get("unit_ideal"))
print("Qstar_pivots =", je.get("Qstar_pivots"))
print("residual_count =", je.get("residual_count"))
if je.get("residual_rows"):
    r=je["residual_rows"][0]
    print("first_residual", r.get("label"), "=", r.get("expression"))
print("GG_UNIT" if sg.get("unit_ideal") else "GG_NONUNIT")
PY
fi
exit "$status"
