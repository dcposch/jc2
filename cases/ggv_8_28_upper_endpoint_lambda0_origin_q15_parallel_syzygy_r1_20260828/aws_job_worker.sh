#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
job_type=$2
host_alias=$3
source_dir="$job_dir/source"
case_dir="$source_dir/jc2/cases/ggv_8_28_upper_endpoint_lambda0_origin_q15_parallel_syzygy_r1_20260828"
output_dir="$job_dir/output"
records_dir="$job_dir/records"

case "$job_type" in
  syzygy_g15_target_d7_p65521|syzygy_full_active_d7_p65519|\
  singular_g15_core_block_std_p65497|singular_full_core_block_slimgb_p65521|\
  singular_full_reverse_dp_slimgb_p65519|msolve_full_endpoint_p65497) ;;
  *) printf '%s\n' NO_VERDICT_INVALID_JOB_TYPE >"$output_dir/TERMINAL"; exit 29 ;;
esac

deadline=$((SECONDS + 30))
while [[ ! -f "$records_dir/REGISTERED" ]]; do
  if (( SECONDS >= deadline )); then
    printf '%s\n' NO_VERDICT_REGISTRATION_TIMEOUT >"$output_dir/TERMINAL"; exit 30
  fi
  sleep 0.05
done

zero_swap() {
  local total free
  total=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo)
  free=$(awk '/^SwapFree:/{print $2}' /proc/meminfo)
  [[ "$total" == 0 && "$free" == 0 ]]
}

stage() {
  local name=$1 cap=$2 time_file=$3 stdout_file=$4 stderr_file=$5
  shift 5
  mkdir -p "$output_dir/stages"
  printf '%s\n' "$name" >"$output_dir/CURRENT_STAGE"
  if ! zero_swap; then
    printf '%s\n' 90 >"$output_dir/stages/${name}.rc"
    return 90
  fi
  set +e
  /usr/bin/time -v -o "$time_file" \
    timeout --foreground --signal=TERM --kill-after=30s "$cap" \
    prlimit --as=68719476736 --fsize=17179869184 \
    taskset --cpu-list 1 env PYTHONDONTWRITEBYTECODE=1 "$@" \
    >"$stdout_file" 2>"$stderr_file"
  local rc=$?
  set -e
  printf '%s\n' "$rc" >"$output_dir/stages/${name}.rc"
  if ! zero_swap; then
    printf '%s\n' 91 >"$output_dir/stages/${name}.rc"
    return 91
  fi
  return "$rc"
}

printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 "$case_dir/aws_preflight.py" --run-dir "$job_dir" \
  --job-tag "$(basename "$job_dir")" --host-alias "$host_alias" \
  --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || {
    printf '%s\n' NO_VERDICT_PREFLIGHT_OR_ACTIVE_CONFLICT >"$output_dir/TERMINAL"; exit 31; }
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$case_dir"
sha256sum -c SOURCE.sha256 >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"; exit 32; }
sha256sum -c PREREGISTRATION.sha256 >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"; exit 33; }

mkdir -p "$output_dir/compiled" "$output_dir/run"
stage SOLVER_SELFCHECK 30 "$output_dir/selfcheck.time" "$output_dir/selfcheck.stdout" "$output_dir/selfcheck.stderr" \
  python3 -B selfcheck_sparse_syzygy.py || {
    printf '%s\n' NO_VERDICT_SOLVER_SELFCHECK >"$output_dir/TERMINAL"; exit 34; }
stage COMPILE_EXACT_DEDUP 300 "$output_dir/compile.time" "$output_dir/compile.stdout" "$output_dir/compile.stderr" \
  python3 -B compile_dedup_portfolio.py --output-dir "$output_dir/compiled" || {
    printf '%s\n' NO_VERDICT_DEDUP_COMPILE >"$output_dir/TERMINAL"; exit 35; }
dedup_sha=$(sha256sum "$output_dir/compiled/DEDUP.json" | awk '{print $1}')
printf '%s\n' "$dedup_sha" >"$output_dir/compiled/DEDUP.sha256"

verdict=NO_VERDICT_MODULAR_SIGNAL_ABSENT_OR_CAP
case "$job_type" in
  syzygy_g15_target_d7_p65521)
    stage SPARSE_SYZYGY_G15_D7_P65521 1200 \
      "$output_dir/run/time.txt" "$output_dir/run/stdout.txt" "$output_dir/run/stderr.txt" \
      python3 -B search_sparse_syzygy.py --dedup "$output_dir/compiled/DEDUP.json" \
        --dedup-sha256 "$dedup_sha" --subset g15 --multiplier-vars target \
        --total-degree 7 --saturation-power 0 --prime 65521 --max-columns 5000 \
        --output "$output_dir/run/CERTIFICATE.json" || true
    if grep -q 'MODULAR_SYZYGY_FOUND_WITH_REPLAY' "$output_dir/run/stdout.txt"; then
      verdict=MODULAR_SYZYGY_FOUND_WITH_REPLAY
    fi
    ;;
  syzygy_full_active_d7_p65519)
    stage SPARSE_SYZYGY_FULL_D7_P65519 2400 \
      "$output_dir/run/time.txt" "$output_dir/run/stdout.txt" "$output_dir/run/stderr.txt" \
      python3 -B search_sparse_syzygy.py --dedup "$output_dir/compiled/DEDUP.json" \
        --dedup-sha256 "$dedup_sha" --subset full --multiplier-vars active \
        --total-degree 7 --saturation-power 0 --prime 65519 --max-columns 20000 \
        --output "$output_dir/run/CERTIFICATE.json" || true
    if grep -q 'MODULAR_SYZYGY_FOUND_WITH_REPLAY' "$output_dir/run/stdout.txt"; then
      verdict=MODULAR_SYZYGY_FOUND_WITH_REPLAY
    fi
    ;;
  singular_g15_core_block_std_p65497)
    stem=g15_core_block_std_p65497
    stage PARSE_SELECTED_ORDER 60 "$output_dir/run/parse.time" "$output_dir/run/parse.stdout" "$output_dir/run/parse.stderr" \
      Singular -q "$output_dir/compiled/${stem}_parse.sing" || {
        printf '%s\n' NO_VERDICT_ORDER_PARSE >"$output_dir/TERMINAL"; exit 36; }
    stage G15_CORE_BLOCK_STD_P65497 1800 "$output_dir/run/time.txt" "$output_dir/run/stdout.txt" "$output_dir/run/stderr.txt" \
      Singular -q "$output_dir/compiled/${stem}.sing" || true
    grep -q 'TARGET_NF_ZERO=1' "$output_dir/run/stdout.txt" && verdict=MODULAR_TARGET_MEMBERSHIP_SIGNAL
    ;;
  singular_full_core_block_slimgb_p65521)
    stem=full_core_block_slimgb_p65521
    stage PARSE_SELECTED_ORDER 60 "$output_dir/run/parse.time" "$output_dir/run/parse.stdout" "$output_dir/run/parse.stderr" \
      Singular -q "$output_dir/compiled/${stem}_parse.sing" || {
        printf '%s\n' NO_VERDICT_ORDER_PARSE >"$output_dir/TERMINAL"; exit 36; }
    stage FULL_CORE_BLOCK_SLIMGB_P65521 1800 "$output_dir/run/time.txt" "$output_dir/run/stdout.txt" "$output_dir/run/stderr.txt" \
      Singular -q "$output_dir/compiled/${stem}.sing" || true
    grep -q 'TARGET_NF_ZERO=1' "$output_dir/run/stdout.txt" && verdict=MODULAR_TARGET_MEMBERSHIP_SIGNAL
    ;;
  singular_full_reverse_dp_slimgb_p65519)
    stem=full_reverse_dp_slimgb_p65519
    stage PARSE_SELECTED_ORDER 60 "$output_dir/run/parse.time" "$output_dir/run/parse.stdout" "$output_dir/run/parse.stderr" \
      Singular -q "$output_dir/compiled/${stem}_parse.sing" || {
        printf '%s\n' NO_VERDICT_ORDER_PARSE >"$output_dir/TERMINAL"; exit 36; }
    stage FULL_REVERSE_DP_SLIMGB_P65519 1800 "$output_dir/run/time.txt" "$output_dir/run/stdout.txt" "$output_dir/run/stderr.txt" \
      Singular -q "$output_dir/compiled/${stem}.sing" || true
    grep -q 'TARGET_NF_ZERO=1' "$output_dir/run/stdout.txt" && verdict=MODULAR_TARGET_MEMBERSHIP_SIGNAL
    ;;
  msolve_full_endpoint_p65497)
    stage MSOLVE_FULL_ENDPOINT_P65497 1800 "$output_dir/run/time.txt" "$output_dir/run/stdout.txt" "$output_dir/run/stderr.txt" \
      msolve -f "$output_dir/compiled/msolve_full_endpoint_p65497.in" \
        -o "$output_dir/run/msolve.out" -t 1 -v 1 -g 1 || true
    grep -q '^\[-1\]' "$output_dir/run/msolve.out" && verdict=MODULAR_ENDPOINT_IDEAL_EMPTY_SIGNAL
    ;;
esac

printf '%s\n' "$verdict" >"$output_dir/VERDICT"
zero_swap || { printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"; exit 91; }
printf '%s\n' PORTFOLIO_JOB_COMPLETE >"$output_dir/TERMINAL"
printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"
