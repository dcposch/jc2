#!/usr/bin/env bash
# Run one isolated exact-Q stage with authoritative GNU-time custody.
set -euo pipefail
ENGINE=${1:?engine path}
BRANCH=${2:?delta2 or delta52}
STAGE=${3:?stage}
OUTDIR=${4:?output directory}
INNER_TIMEOUT=${5:-9000}
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

mkdir -p "$OUTDIR"
STEM="$OUTDIR/stage${STAGE}"
for suffix in json err sing time rc started-utc finished-utc; do
  test ! -e "${STEM}.${suffix}" || {
    echo "refusing to overwrite ${STEM}.${suffix}" >&2
    exit 4
  }
done

date -u +%Y-%m-%dT%H:%M:%SZ > "${STEM}.started-utc"
export PYTHONHASHSEED=0
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1 FLINT_NUM_THREADS=1
set +e
/usr/bin/time -v -o "${STEM}.time" \
  timeout --signal=TERM --kill-after=30s "${INNER_TIMEOUT}" \
  python3 -u "$ENGINE" --branch "$BRANCH" --stage "$STAGE" \
    --emit-singular "${STEM}.sing" \
    > "${STEM}.json" 2> "${STEM}.err"
STATUS=$?
set -e
printf '%s\n' "$STATUS" > "${STEM}.rc"
date -u +%Y-%m-%dT%H:%M:%SZ > "${STEM}.finished-utc"

if [[ $STATUS -eq 0 ]]; then
  python3 - "$STEM.json" <<'PY'
import json
import sys

path = sys.argv[1]
data = json.load(open(path, encoding="utf-8"))
joint = data["joint_elimination"]
singular = joint["singular"]
constants = [
    (row["label"], row["expression"])
    for row in joint["residual_rows"]
    if not __import__("sympy").sympify(row["expression"]).free_symbols
]
print(
    "COMPLETED",
    data["branch"],
    "stage", data["stage_spec"]["stage"],
    "verdict", data["verdict"],
    "pivots", joint["Qstar_pivots"],
    "residual", joint["residual_count"],
    "unit", singular["unit_ideal"],
    "dimension", data["counts"]["exact_Krull_dimension_localized"],
    "first_constant", constants[:1],
    flush=True,
)
PY
else
  echo "FAILED branch=$BRANCH stage=$STAGE rc=$STATUS" >&2
fi
exit "$STATUS"
