#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
component=$2
source_cases="$job_dir/source/jc2/cases"
case_dir="$source_cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_descent_r6_20260828"
r5_case="$source_cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828"
r1_case="$source_cases/ggv_8_28_upper_endpoint_lambda0_rank_jump_fitting_census_r1_20260828"
input_case="$source_cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_components_r1_20260828"
r6_input_case="$source_cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r6_20260828"
r5_compiler="$r5_case/build_nf_rank.py"
r1_compiler="$r1_case/build_fitting_census.py"
matrix="$input_case/input/symbolic_quadratic_q_rankdrop.sing"
factor_archive="$r6_input_case/custody/ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a.tar.gz"
output_dir="$job_dir/output"
records_dir="$job_dir/records"
compiled_dir="$output_dir/compiled"
run_dir="$output_dir/run"

case "$component" in p|c8p02) ;; *) exit 29 ;; esac
deadline=$((SECONDS+30))
while [[ ! -f "$records_dir/REGISTERED" ]]; do
  if (( SECONDS >= deadline )); then printf '%s\n' NO_VERDICT_REGISTRATION_TIMEOUT >"$output_dir/TERMINAL"; exit 30; fi
  sleep .05
done

zero_swap() {
  local total free
  total=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo)
  free=$(awk '/^SwapFree:/{print $2}' /proc/meminfo)
  [[ "$total" == 0 && "$free" == 0 ]]
}

stage() {
  local name=$1 cap=$2 timing=$3 stdout=$4 stderr=$5
  shift 5
  mkdir -p "$output_dir/stages"
  printf '%s\n' "$name" >"$output_dir/CURRENT_STAGE"
  if ! zero_swap; then printf '%s\n' 90 >"$output_dir/stages/${name}.rc"; return 90; fi
  set +e
  /usr/bin/time -v -o "$timing" timeout --foreground --signal=TERM --kill-after=30s "$cap" \
    prlimit --as=103079215104 --fsize=34359738368 taskset --cpu-list 1 \
    env PYTHONDONTWRITEBYTECODE=1 "$@" >"$stdout" 2>"$stderr"
  local rc=$?
  set -e
  printf '%s\n' "$rc" >"$output_dir/stages/${name}.rc"
  if ! zero_swap; then printf '%s\n' 91 >"$output_dir/stages/${name}.rc"; return 91; fi
  return "$rc"
}

finish_failure() {
  printf '%s\n' "$1" >"$output_dir/VERDICT"
  printf '%s\n' QUOTIENT_NF_RANK_DESCENT_JOB_COMPLETE >"$output_dir/TERMINAL"
  printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"
  exit 0
}

mkdir -p "$compiled_dir" "$run_dir" "$output_dir/stages"
printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 -B "$case_dir/aws_preflight.py" --run-dir "$job_dir" --job-tag "$(basename "$job_dir")" \
  --component "$component" --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || {
    printf '%s\n' NO_VERDICT_PREFLIGHT_OR_CONFLICT >"$output_dir/TERMINAL"; exit 31;
  }
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$case_dir"
sha256sum -c SOURCE.sha256 >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"; exit 32;
}
sha256sum -c PREREGISTRATION.sha256 >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"; exit 33;
}

stage PYTHON_SELFCHECK 180 "$output_dir/selfcheck.time" "$output_dir/selfcheck.stdout" "$output_dir/selfcheck.stderr" \
  python3 -B "$case_dir/selfcheck_rank_descent.py" --case-dir "$case_dir" \
  --r5-compiler "$r5_compiler" --r1-compiler "$r1_compiler" --matrix "$matrix" \
  --factor-archive "$factor_archive" || finish_failure NO_VERDICT_PYTHON_SELFCHECK
grep -q '^RANK_DESCENT_SELFCHECK_PASS$' "$output_dir/selfcheck.stdout" || finish_failure NO_VERDICT_PYTHON_SELFCHECK_MARKER

stage BACKEND_SELFCHECK 60 "$output_dir/backend_selfcheck.time" "$output_dir/backend_selfcheck.stdout" "$output_dir/backend_selfcheck.stderr" \
  Singular -q "$case_dir/adapter_selfcheck.sing" || finish_failure NO_VERDICT_BACKEND_SELFCHECK
grep -q '^ADVERSARIAL_Q2_REDUCER_SELFCHECK_PASS$' "$output_dir/backend_selfcheck.stdout" || finish_failure NO_VERDICT_BACKEND_SELFCHECK_MARKER

stage BUILD_REDUCE 300 "$output_dir/build_reduce.time" "$output_dir/build_reduce.stdout" "$output_dir/build_reduce.stderr" \
  python3 -B "$r5_compiler" --phase reduce --r1-compiler "$r1_compiler" --matrix "$matrix" \
  --factor-archive "$factor_archive" --component "$component" --output-dir "$compiled_dir" || finish_failure NO_VERDICT_BUILD_REDUCE
grep -q '^NF_RANK_BUILD_PASS$' "$output_dir/build_reduce.stdout" || finish_failure NO_VERDICT_BUILD_REDUCE_MARKER

cd "$run_dir"
stage RUN_REDUCE 3300 "$run_dir/reduce.time" "$run_dir/reduce.stdout" "$run_dir/reduce.stderr" \
  Singular -q "$compiled_dir/${component}_nf_reduce.sing" || finish_failure NO_VERDICT_RUN_REDUCE
for marker in '^PINNED_STANDARD_BASIS_REDUCER_PASS=1$' '^ADVERSARIAL_IDEAL_FACTOR_NF_ZERO=1$' '^ADVERSARIAL_MUTATION_NF_NONZERO=1$' '^NF_RATIONAL_UNIT_PIVOT_COUNT=95$' '^NF_RESIDUAL_ROWS=11$' '^NF_RESIDUAL_COLS=10$' '^NF_DRIFT_COUNT=0$' '^NF_PIVOT_INVARIANT_FAILURES=0$' '^EXPLICIT_NF_AFTER_EVERY_ENTRY_OPERATION=1$' '^NF_RESIDUAL_REDUCTION_COMPLETE=1$'; do
  grep -q "$marker" "$run_dir/reduce.stdout" || finish_failure NO_VERDICT_RUN_REDUCE_MARKER
done
label=$(awk -F= '/^STRATUM_LABEL=/{print $2}' "$run_dir/reduce.stdout" | tail -n 1)
case "$component:$label" in p:P|c8p02:C8P02) ;; *) finish_failure NO_VERDICT_LABEL_DISAGREEMENT ;; esac
residual="$run_dir/${label}_NF_RESIDUAL_MATRIX.tsv"
[[ -s "$residual" ]] || finish_failure NO_VERDICT_RESIDUAL_MISSING

stage BUILD_DESCENT 600 "$output_dir/build_descent.time" "$output_dir/build_descent.stdout" "$output_dir/build_descent.stderr" \
  python3 -B "$case_dir/build_rank_descent.py" --r5-compiler "$r5_compiler" \
  --r1-compiler "$r1_compiler" --matrix "$matrix" --factor-archive "$factor_archive" \
  --component "$component" --residual "$residual" --output-dir "$compiled_dir" || finish_failure NO_VERDICT_BUILD_DESCENT
for marker in '^SUPPORT_ENTRY_COUNT=75$' '^SIZE10_FORMAL_SLOT_COUNT=11$' '^SIZE10_MATCHABLE_SLOT_COUNT=2$' '^SIZE9_FORMAL_SLOT_COUNT=550$' '^SIZE9_MATCHABLE_SLOT_COUNT=172$' '^RANK_DESCENT_BUILD_PASS$'; do
  grep -q "$marker" "$output_dir/build_descent.stdout" || finish_failure NO_VERDICT_BUILD_DESCENT_MARKER
done

stage RUN_DESCENT 3300 "$run_dir/descent.time" "$run_dir/descent.stdout" "$run_dir/descent.stderr" \
  Singular -q "$compiled_dir/${component}_rank_descent.sing" || finish_failure NO_VERDICT_RUN_DESCENT
for marker in '^PINNED_STANDARD_BASIS_REDUCER_PASS=1$' '^SIZE10_FORMAL_SLOT_COUNT=11$' '^SIZE10_STRUCTURAL_ZERO_SLOT_COUNT=9$' '^SIZE10_MATCHABLE_CANDIDATE_COUNT=2$' '^SIZE10_MATCHABLE_NF_ZERO_COUNT=2$' '^SIZE10_MATCHABLE_NF_NONZERO_COUNT=0$' '^SIZE9_FORMAL_SLOT_COUNT=550$' '^SIZE9_STRUCTURAL_ZERO_SLOT_COUNT=378$' '^SIZE9_MATCHABLE_CANDIDATE_COUNT=172$' '^SIZE9_WITNESS_NF_NONZERO=1$' '^SUPPORT_REPLAY_FAILURES=0$' '^EVERY_SIZE10_MINOR_NF_ZERO=1$' '^EXACT_SIZE9_NF_WITNESS=1$' '^EXACT_QUOTIENT_RANK9_CERTIFICATE_COMPLETE=1$'; do
  grep -q "$marker" "$run_dir/descent.stdout" || finish_failure NO_VERDICT_RUN_DESCENT_MARKER
done
if grep -q '^FATAL_' "$run_dir/reduce.stdout" "$run_dir/descent.stdout"; then finish_failure NO_VERDICT_FATAL_MARKER; fi

printf 'component|nf_unit_pivots|nf_residual_rank|total_rank|status\n%s|95|9|104|EXACT_QUOTIENT_NF_RANK_CERTIFICATE\n' "$component" >"$output_dir/COMPONENT_RESULT.tsv"
printf '%s\n' NO_VERDICT_QUOTIENT_NF_RANK_CERTIFICATE_ONLY >"$output_dir/VERDICT"
find "$compiled_dir" "$run_dir" -type f -print0 | sort -z | xargs -0 sha256sum >"$output_dir/EXACT_ARTIFACTS.sha256"
zero_swap || { printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"; exit 91; }
printf '%s\n' QUOTIENT_NF_RANK_DESCENT_JOB_COMPLETE >"$output_dir/TERMINAL"
printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"

