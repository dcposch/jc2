#!/usr/bin/env bash
set -eu
cd /home/ubuntu/jc2/box/char-degree-20260905/d108
run_stage() {
  stage="$1"
  python3 remainder_stage.py --stage "$stage" --translated --strong-front --emit-only > "circuit-stage${stage}-input.driver.log" 2>&1
  (ulimit -v 16777216; python3 coefficient_circuit_backend.py --input "d108_remainder_stage${stage}_translated_strongfront.input.json" --out "d108_circuit_stage${stage}_translated_strongfront.sing" --timeout 900; code=$?; echo "CIRCUIT_EXIT_CODE=$code") > "circuit-stage${stage}-translated-strongfront.driver.log" 2>&1
}
export -f run_stage
seq 0 7 | xargs -P 2 -I STAGE bash -c 'run_stage "$1"' _ STAGE
