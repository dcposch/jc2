#!/usr/bin/env bash
# The precise jobs are not released until this detached control phase passes.
set -euo pipefail
HERE=/home/ubuntu/jc2/box/g9966-d2-precise-20260905
cd "$HERE"
bash verify_inputs.sh

set +e
bash run_one.sh "$HERE/original_band_engine.py" delta2 4 control/delta2 3000 \
  > logs/control-delta2-stage4.log 2>&1 &
P1=$!
bash run_one.sh "$HERE/original_band_engine.py" delta52 8 control/delta52 3000 \
  > logs/control-delta52-stage8.log 2>&1 &
P2=$!
printf '%s\n' "$P1" > logs/control-delta2-stage4.pid
printf '%s\n' "$P2" > logs/control-delta52-stage8.pid
wait "$P1"; R1=$?
wait "$P2"; R2=$?
set -e
printf '%s %s\n' "$R1" "$R2" > logs/control-child-statuses.txt
test "$R1" -eq 0 -a "$R2" -eq 0
python3 validate_controls.py > certificates/control-validation.json
printf 'CONTROL_PASS\n'
