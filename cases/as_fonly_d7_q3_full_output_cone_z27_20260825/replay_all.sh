#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)"
case_dir="${root}/cases/as_fonly_d7_q3_full_output_cone_z27_20260825"
parent_dir="${root}/cases/as_fonly_d7_q3_full_output_cone_z9_20260825/aws_run"
model_dir="${root}/cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/aws_run"
out="$(mktemp -d /tmp/as-z27-replay.XXXXXX)"

for base in base_0000_0000000 base_0270_0101000 base_0513_0201000; do
  mkdir -p "${out}/${base}"
  JC2_ROOT="${root}" \
  MODEL_OUTPUT="${model_dir}/${base}/model.stdout" \
  PARENT_OUTPUT_JSON="${parent_dir}/${base}/q3_parent.json" \
  PREVIOUS_Z9_RESULT_JSON="${parent_dir}/${base}/result.json" \
  OUTPUT_JSON="${out}/${base}/result.json" \
  python3 "${case_dir}/solve_full_output_cone_z27.py" \
    > "${out}/${base}/stdout" 2> "${out}/${base}/stderr"
  cmp "${out}/${base}/result.json" \
      "${case_dir}/aws_box02/${base}/result.json"
done

python3 "${case_dir}/verify_frozen.py"
printf 'replay_dir=%s\n' "${out}"
printf '%s\n' PASS-AS-Q3-FULL-OUTPUT-CONE-Z27-REPLAY
