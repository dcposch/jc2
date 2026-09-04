#!/usr/bin/env bash
set -euo pipefail

driver_dir=/home/ubuntu/jc2/box/row2515gate-20260903
artifact_dir="$driver_dir/artifacts"

run_one() {
  local input_path="$1"
  local output_path="${input_path%.sing}.out"
  local error_path="${input_path%.sing}.err"
  timeout 1800 env \
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
    Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc \
    < "$input_path" > "$output_path" 2> "$error_path"
  printf '%s\n' "SYSTEM ${input_path#$driver_dir/}"
  rg 'CONTROL_|MAIN_|TAME_' "$output_path" || true
}

for input_path in \
  "$artifact_dir/open_25_15_part_3_sparse_Q.sing" \
  "$artifact_dir/open_25_15_part_3_sparse_p32051.sing" \
  "$artifact_dir/open_25_15_part_3_sparse_p32057.sing" \
  "$artifact_dir/open_25_15_part_2_1_sparse_Q.sing" \
  "$artifact_dir/open_25_15_part_2_1_sparse_p32051.sing" \
  "$artifact_dir/open_25_15_part_2_1_sparse_p32057.sing" \
  "$artifact_dir/open_25_15_part_1_1_1_sparse_Q.sing" \
  "$artifact_dir/open_25_15_part_1_1_1_sparse_p32051.sing" \
  "$artifact_dir/open_25_15_part_1_1_1_sparse_p32057.sing" \
  "$artifact_dir/k16_t1_part_1_sparse_Q.sing" \
  "$artifact_dir/k16_t2_part_1_sparse_Q.sing" \
  "$artifact_dir/banked_15_10_part_1_1_sparse_Q.sing" \
  "$artifact_dir/tame_automorphism_Q.sing" \
  "$artifact_dir/tame_automorphism_p32051.sing" \
  "$artifact_dir/tame_automorphism_p32057.sing"
do
  run_one "$input_path"
done
