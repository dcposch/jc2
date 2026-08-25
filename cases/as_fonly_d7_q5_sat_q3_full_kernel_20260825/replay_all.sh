#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?set to the repository root}"
: "${OUTPUT_ROOT:?set to a fresh output directory}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825"
mkdir -p "$OUTPUT_ROOT"

for spec in 0000_0000000 0270_0101000 0513_0201000; do
  model="$case_dir/aws_run/base_${spec}/model.stdout"
  job="$OUTPUT_ROOT/base_${spec}"
  env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$model" JOB_DIR="$job" \
    bash "$case_dir/run_remote.sh"
done

for spec in 0000_0000000 0270_0101000 0513_0201000; do
  grep -F 'PASS-AS-Q5-Q3-FULL-KERNEL-SAT' \
    "$OUTPUT_ROOT/base_${spec}/replay.stdout"
done

echo PASS-AS-Q5-Q3-FULL-KERNEL-ALL-THREE
