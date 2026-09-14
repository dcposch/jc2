#!/usr/bin/env bash
set -eu
cd /home/ubuntu/jc2/box/char-degree-20260905/d108
run_stage() {
  stage="$1"
  python3 meanfree_stage.py --stage "$stage" > "meanfree-stage${stage}-input.driver.log" 2>&1
  (ulimit -v 16777216; python3 coefficient_circuit_backend_v2.py --input "d108_meanfree_stage${stage}_strongfront.input.json" --out "d108_meanfree_circuit_stage${stage}_strongfront.sing" --timeout 600; code=$?; echo "CIRCUIT_EXIT_CODE=$code") > "meanfree-circuit-stage${stage}.driver.log" 2>&1
}
export -f run_stage
seq 0 8 | xargs -P 2 -I STAGE bash -c 'run_stage "$1"' _ STAGE
