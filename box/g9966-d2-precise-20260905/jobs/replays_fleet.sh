#!/usr/bin/env bash
# All requested cumulative stages are independent and use separate exact-Q processes.
set -euo pipefail
HERE=/home/ubuntu/jc2/box/g9966-d2-precise-20260905
cd "$HERE"
test "$(python3 -c 'import json; print(json.load(open("certificates/control-validation.json"))["status"])')" = PASS
bash verify_inputs.sh

PIDS=()
NAMES=()
for stage in 0 1 2 3 4; do
  name="precise-delta2-stage${stage}"
  bash run_one.sh "$HERE/band_engine.py" delta2 "$stage" runs/delta2 9000 \
    > "logs/${name}.log" 2>&1 &
  PIDS+=("$!"); NAMES+=("$name")
  printf '%s\n' "$!" > "logs/${name}.pid"
done
for stage in 0 1 2 3 4 5 6 7 8; do
  name="precise-delta52-stage${stage}"
  bash run_one.sh "$HERE/band_engine.py" delta52 "$stage" runs/delta52 9000 \
    > "logs/${name}.log" 2>&1 &
  PIDS+=("$!"); NAMES+=("$name")
  printf '%s\n' "$!" > "logs/${name}.pid"
done

STATUS=0
set +e
for index in "${!PIDS[@]}"; do
  wait "${PIDS[$index]}"; rc=$?
  printf '%s\t%s\n' "${NAMES[$index]}" "$rc" | tee -a logs/replay-child-statuses.tsv
  [[ $rc -eq 0 ]] || STATUS=1
done
set -e
if [[ $STATUS -eq 0 ]]; then
  printf 'ALL_REPLAYS_COMPLETE\n'
else
  printf 'REPLAY_FAILURE_OR_TIMEOUT\n' >&2
fi
exit "$STATUS"
