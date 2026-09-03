#!/bin/bash
# Usage: run_singular.sh NAME TIMEOUT_SEC SINGULAR_FILE
set -euo pipefail
BOX=/home/ubuntu/jc2/box/k16t6-20260903
cd "$BOX"
name="$1"
timeout_sec="$2"
src="$3"
export OMP_NUM_THREADS=1
echo "START $name $(date -u +%FT%TZ)" | tee "$name.stamp"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=15 "${timeout_sec}" \
  Singular -q "$src" > "$name.out" 2> "$name.err"
rc=$?
set -e
echo "$rc" > "$name.exit"
echo "END $name rc=$rc $(date -u +%FT%TZ)" | tee -a "$name.stamp"
if grep -q 'MAIN_EXACT_UNIT\|MAIN_SATURATED_EMPTY' "$name.out" 2>/dev/null; then
  echo UNIT >> "$name.stamp"
elif grep -q 'MAIN_NONUNIT\|MAIN_NONTRIVIAL' "$name.out" 2>/dev/null; then
  echo NONUNIT >> "$name.stamp"
fi
exit 0
