#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?set to the repository root}"
: "${OUTPUT_ROOT:?set to a fresh output directory}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825"
mkdir -p "$OUTPUT_ROOT"

for spec in 0000_0000000 0270_0101000 0513_0201000; do
  model="$case_dir/aws_run/base_${spec}/model.stdout"
  job="$OUTPUT_ROOT/base_${spec}"
  env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$model" JOB_DIR="$job" \
    bash "$case_dir/run_remote.sh"
done

for spec in 0000_0000000 0270_0101000 0513_0201000; do
  case "$spec" in
    0000_0000000) expected=8e563b395d4181d90967c75c35242abc557a8979b4c3f6d89757ce3d234b3f1b ;;
    0270_0101000) expected=5659a16810515290ede2dc78f404330971103f8cbc14fa3116901327f5dee2e9 ;;
    0513_0201000) expected=5ebacfe12f4492607f69e9518bb6a1ef6102179725f5033550d0b8397bae8015 ;;
  esac
  observed=$(sha256sum "$OUTPUT_ROOT/base_${spec}/certificates.json" | cut -d' ' -f1)
  test "$observed" = "$expected"
  grep -F 'PASS-AS-Q3-Q2Q1-GAUSSIAN-EXCLUSION-V2' \
    "$OUTPUT_ROOT/base_${spec}/producer.stdout"
  grep -F 'PASS-AS-Q3-Q2Q1-INDEPENDENT-CERTIFICATE-VERIFY-V2' \
    "$OUTPUT_ROOT/base_${spec}/verifier.stdout"
done

echo PASS-AS-Q3-Q2Q1-GAUSSIAN-EXCLUSION-ALL-THREE-V2
