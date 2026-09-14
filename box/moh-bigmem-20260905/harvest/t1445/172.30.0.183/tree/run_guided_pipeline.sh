#!/usr/bin/env bash
# Singular guided std: modular high-prime then exact-Q, control battery.
# Usage: run_guided_pipeline.sh TARGET_NAME
set -u
ROOT=${ROOT:-$HOME/moh-bigmem-20260905}
TARGET=$1
TDIR="$ROOT/targets/$TARGET"
. "$TDIR/env.sh"
WATCHDOG=${WATCHDOG:-10800}
if [[ -n "${NATIVE_ROWS:-}" && -f "${NATIVE_ROWS}" ]]; then
  ROWS="$NATIVE_ROWS"
  META="$NATIVE_META"
else
  ROWS="${GRAPH_ROWS:-}"
  META="${GRAPH_META:-}"
fi
if [[ ! -f "${ROWS:-}" ]]; then
  echo "GUIDED_NO_ROWS target=$TARGET native=${NATIVE_ROWS:-} graph=${GRAPH_ROWS:-}"
  exit 2
fi
echo "GUIDED_PIPELINE_START target=$TARGET rows=$ROWS utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python3 "$ROOT/run_guided_job.py" \
  --workdir "$TDIR/guided" \
  --meta "$META" --rows "$ROWS" \
  --name "$TARGET" \
  --primes 1073741827 \
  --timeout "$WATCHDOG" \
  --cpus 32
echo "GUIDED_PIPELINE_END utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
