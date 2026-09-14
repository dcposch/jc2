#!/bin/bash
# Fleet-side batch for k4ray beta-strata. Run from /home/ubuntu/jc2 on the worker.
set -euo pipefail
cd /home/ubuntu/jc2
export PYTHONUNBUFFERED=1
LOGDIR=box/k4ray-beta-strata-20260905/fleet-logs
mkdir -p "$LOGDIR"

run_one() {
  local tag="$1"; shift
  echo "==== START $tag $(date -u +%H:%M:%S) ====" | tee -a "$LOGDIR/batch.log"
  python3 -u box/k4ray-beta-strata-20260905/strata_chart.py run "$tag" "$@" \
    > "$LOGDIR/${tag}.log" 2>&1 || echo "FAIL $tag" | tee -a "$LOGDIR/batch.log"
  echo "==== END $tag $(date -u +%H:%M:%S) ====" | tee -a "$LOGDIR/batch.log"
}

# Priority: K=8 extra strata (D=108), then K=9, then leftover K=7.
# Modular screens first (300s), then exact Q (1800s) if the modular fibre dies as a unit.
for b in 7 8 9 10; do
  for pin in 0 1; do
    run_one "FLEET_K8_B${b}_Q${pin}_P32003" 8 "$b" --pin-index "$pin" --chars 32003 --timeout 300 --count-timeout 180 --cores 4
  done
done

for b in 8 9 10; do
  for pin in 0 1; do
    run_one "FLEET_K9_B${b}_Q${pin}_P32003" 9 "$b" --pin-index "$pin" --chars 32003 --timeout 300 --count-timeout 240 --cores 4
  done
done

# Exact Q on the smallest extra K=8 covers
for b in 7 8; do
  for pin in 0 1; do
    run_one "FLEET_K8_B${b}_Q${pin}_Q" 8 "$b" --pin-index "$pin" --chars 0 --timeout 1800 --count-timeout 180 --cores 4
  done
done

echo DONE | tee -a "$LOGDIR/batch.log"
