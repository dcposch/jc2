#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${OUTPUT_ROOT:?}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_q3_full_output_cone_z9_20260825"
model_dir="$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/aws_run"
mkdir -p "$OUTPUT_ROOT"
for spec in 0000_0000000 0270_0101000 0513_0201000; do
  env JC2_ROOT="$JC2_ROOT" \
      MODEL_OUTPUT="$model_dir/base_${spec}/model.stdout" \
      JOB_DIR="$OUTPUT_ROOT/base_${spec}" \
    bash "$case_dir/run_remote.sh"
done
echo PASS-AS-Q3-FULL-OUTPUT-CONE-Z9-REPLAY-ALL
