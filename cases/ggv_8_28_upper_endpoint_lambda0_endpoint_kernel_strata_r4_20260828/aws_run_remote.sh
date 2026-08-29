#!/usr/bin/env bash
set -Eeuo pipefail
job_dir=$1
case_dir="$job_dir/source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r4_20260828"
r3_run="$job_dir/source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r3_20260828/aws_run_remote.sh"
mkdir -p "$job_dir/runtime" "$job_dir/records"
materialized="$job_dir/runtime/aws_run_remote_r4_materialized.sh"
python3 -B "$case_dir/build_run_r4.py" --r3-run "$r3_run" --output "$materialized" \
  >"$job_dir/records/RUN_BUILD.stdout" 2>"$job_dir/records/RUN_BUILD.stderr"
grep -q '^R4_RUN_NARROW_TRANSFORM_PASS$' "$job_dir/records/RUN_BUILD.stdout"
exec bash "$materialized" "$@"
