#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?set to the repository root}"
: "${OUTPUT_ROOT:?set to a fresh output directory}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825"
model_dir="$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/aws_run"
mkdir -p "$OUTPUT_ROOT"

for spec in 0000_0000000 0270_0101000 0513_0201000; do
  model="$model_dir/base_${spec}/model.stdout"
  job="$OUTPUT_ROOT/base_${spec}"
  env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$model" JOB_DIR="$job" \
    bash "$case_dir/run_remote_v2.sh"
done

env RESULT_ROOT="$OUTPUT_ROOT" python3 "$case_dir/verify_outputs_v2.py"
echo PASS-AS-Q3-Q2Q1-DEGREE1-INFLUENCE-REPLAY-ALL-V2
