#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 STAGE" >&2
  exit 2
fi

stage="$1"
case "$stage" in
  ''|*[!0-9]*)
    echo "stage must be a nonnegative integer" >&2
    exit 2
    ;;
esac

cd "$(dirname "$0")/../.."

outdir="box/g9966Bgate-20260903/runs/delta2"
mkdir -p "$outdir"

env \
  OPENBLAS_NUM_THREADS=1 \
  OMP_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 \
  NUMEXPR_NUM_THREADS=1 \
  timeout 2400 \
  /usr/bin/time -v \
    -o "$outdir/stage${stage}.time" \
  python3 box/g9966band-20260903/band_engine.py \
    --branch delta2 \
    --stage "$stage" \
    --emit-singular "$outdir/stage${stage}.sing" \
    > "$outdir/stage${stage}.json" \
    2> "$outdir/stage${stage}.err"
