#!/bin/bash
# Usage: run_capped.sh NAME TIMEOUT_SEC COMMAND...
set -euo pipefail
BOX=/home/ubuntu/jc2/box/k16t6-20260903
cd "$BOX"
name="$1"
timeout_sec="$2"
shift 2
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-1}"
export SINGULAR_NUM_THREADS="${SINGULAR_NUM_THREADS:-1}"
echo "START $name $(date -u +%FT%TZ) timeout=${timeout_sec}s cmd=$*" | tee "$name.stamp"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=20 "${timeout_sec}" \
  "$@" > "$name.out" 2> "$name.err"
rc=$?
set -e
echo "$rc" > "$name.exit"
echo "END $name rc=$rc $(date -u +%FT%TZ)" | tee -a "$name.stamp"
if grep -qE 'MAIN_EXACT_UNIT|MAIN_SATURATED_EMPTY|STOP_AFTER_UNITS|LAURENT_T6|terminal_rows' "$name.out" 2>/dev/null; then
  echo HIT >> "$name.stamp"
fi
exit 0
