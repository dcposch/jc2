#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
lane=$2
source_root="$job_dir/source/jc2/cases"
case_dir="$source_root/ggv_8_28_upper_endpoint_lambda0_rank_jump_fitting_census_r1_20260828"
input_case="$source_root/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_components_r1_20260828"
r6_case="$source_root/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r6_20260828"
matrix="$input_case/input/symbolic_quadratic_q_rankdrop.sing"
r6_archive="$r6_case/custody/ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a.tar.gz"
output_dir="$job_dir/output"
records_dir="$job_dir/records"
compiled_dir="$output_dir/compiled"
run_dir="$output_dir/run"

[[ "$lane" == base_a || "$lane" == base_b || "$lane" == pair || "$lane" == triple ]]
deadline=$((SECONDS + 30))
while [[ ! -f "$records_dir/REGISTERED" ]]; do
  if (( SECONDS >= deadline )); then
    printf '%s\n' NO_VERDICT_REGISTRATION_TIMEOUT >"$output_dir/TERMINAL"
    exit 30
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
    prlimit --as=103079215104 --fsize=34359738368 \
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

mkdir -p "$compiled_dir" "$run_dir" "$output_dir/stages"
printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 -B "$case_dir/aws_preflight.py" --run-dir "$job_dir" \
  --job-tag "$(basename "$job_dir")" --lane "$lane" \
  --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || {
    printf '%s\n' NO_VERDICT_PREFLIGHT_OR_ACTIVE_CONFLICT >"$output_dir/TERMINAL"
    exit 31
  }
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$case_dir"
sha256sum -c SOURCE.sha256 >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"
  exit 32
}
sha256sum -c PREREGISTRATION.sha256 >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"
  exit 33
}

stage ADAPTER_SELFCHECK 180 "$output_dir/selfcheck.time" "$output_dir/selfcheck.stdout" "$output_dir/selfcheck.stderr" \
  python3 -B "$case_dir/selfcheck_fitting_census.py" --case-dir "$case_dir" \
    --matrix "$matrix" --r6-archive "$r6_archive" || {
      printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK >"$output_dir/TERMINAL"
      exit 34
    }
grep -q '^FITTING_CENSUS_SELFCHECK_PASS$' "$output_dir/selfcheck.stdout" || {
  printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK_MARKER >"$output_dir/TERMINAL"
  exit 35
}

stage BUILD_SCRIPTS 180 "$output_dir/build.time" "$output_dir/build.stdout" "$output_dir/build.stderr" \
  python3 -B "$case_dir/build_fitting_census.py" --matrix "$matrix" \
    --r6-archive "$r6_archive" --lane "$lane" --output-dir "$compiled_dir" || {
      printf '%s\n' NO_VERDICT_BUILD >"$output_dir/TERMINAL"
      exit 36
    }
grep -q '^FITTING_CENSUS_BUILD_PASS$' "$output_dir/build.stdout" || {
  printf '%s\n' NO_VERDICT_BUILD_MARKER >"$output_dir/TERMINAL"
  exit 37
}

printf 'label|status|unit_pivots|residual_rows|residual_cols|residual_rank|total_rank|script\n' >"$output_dir/COMPONENT_RESULTS.tsv"
success=0
failed=0
while IFS='|' read -r label zero_variables factor_sha factor script_name; do
  [[ "$label" == label ]] && continue
  stem=${script_name%.sing}
  parse="$compiled_dir/${stem}_parse.sing"
  script="$compiled_dir/$script_name"
  stage "PARSE_${label}" 120 "$run_dir/${stem}.parse.time" "$run_dir/${stem}.parse.stdout" "$run_dir/${stem}.parse.stderr" \
    Singular -q "$parse" || {
      printf '%s|NO_VERDICT_PARSE|NA|NA|NA|NA|NA|%s\n' "$label" "$script_name" >>"$output_dir/COMPONENT_RESULTS.tsv"
      failed=$((failed + 1))
      continue
    }
  grep -q "^FULL_MATRIX_PARSE_PASS=${label}$" "$run_dir/${stem}.parse.stdout" || {
    printf '%s|NO_VERDICT_PARSE_MARKER|NA|NA|NA|NA|NA|%s\n' "$label" "$script_name" >>"$output_dir/COMPONENT_RESULTS.tsv"
    failed=$((failed + 1))
    continue
  }
  cd "$run_dir"
  stage "CENSUS_${label}" 1500 "$run_dir/${stem}.time" "$run_dir/${stem}.stdout" "$run_dir/${stem}.stderr" \
    Singular -q "$script" || true
  if grep -q '^UNIT_PIVOT_INVARIANTS_PASS=1$' "$run_dir/${stem}.stdout" && \
     grep -q '^UNIT_PIVOT_CENSUS_COMPLETE=1$' "$run_dir/${stem}.stdout"; then
    pivots=$(sed -n 's/^RATIONAL_UNIT_PIVOT_COUNT=//p' "$run_dir/${stem}.stdout")
    rows=$(sed -n 's/^RESIDUAL_ROWS=//p' "$run_dir/${stem}.stdout")
    cols=$(sed -n 's/^RESIDUAL_COLS=//p' "$run_dir/${stem}.stdout")
    rrank=$(sed -n 's/^RESIDUAL_GENERIC_RANK=//p' "$run_dir/${stem}.stdout")
    trank=$(sed -n 's/^TOTAL_GENERIC_RANK=//p' "$run_dir/${stem}.stdout")
    if [[ "$pivots" =~ ^[0-9]+$ && "$rows" =~ ^[0-9]+$ && "$cols" =~ ^[0-9]+$ && \
          "$rrank" =~ ^[0-9]+$ && "$trank" =~ ^[0-9]+$ && "$trank" -le 104 ]]; then
      printf '%s|EXACT_RESIDUAL_CENSUS|%s|%s|%s|%s|%s|%s\n' \
        "$label" "$pivots" "$rows" "$cols" "$rrank" "$trank" "$script_name" \
        >>"$output_dir/COMPONENT_RESULTS.tsv"
      success=$((success + 1))
    else
      printf '%s|NO_VERDICT_RANKDROP_OR_MARKER_DISAGREEMENT|%s|%s|%s|%s|%s|%s\n' \
        "$label" "${pivots:-NA}" "${rows:-NA}" "${cols:-NA}" "${rrank:-NA}" "${trank:-NA}" "$script_name" \
        >>"$output_dir/COMPONENT_RESULTS.tsv"
      failed=$((failed + 1))
    fi
  else
    printf '%s|NO_VERDICT_ADAPTER_CAP_OR_INVARIANT|NA|NA|NA|NA|NA|%s\n' "$label" "$script_name" \
      >>"$output_dir/COMPONENT_RESULTS.tsv"
    failed=$((failed + 1))
  fi
done <"$compiled_dir/COMPONENT_MANIFEST.tsv"

printf 'SUCCESS=%s\nFAILED=%s\n' "$success" "$failed" >"$output_dir/LANE_COUNTS.txt"
if (( failed == 0 && success > 0 )); then
  printf '%s\n' NO_VERDICT_FITTING_CENSUS_ONLY >"$output_dir/VERDICT"
else
  printf '%s\n' NO_VERDICT_INCOMPLETE_FITTING_CENSUS >"$output_dir/VERDICT"
fi
find "$compiled_dir" "$run_dir" -type f -print0 | sort -z | xargs -0 sha256sum \
  >"$output_dir/EXACT_ARTIFACTS.sha256"
zero_swap || {
  printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"
  exit 91
}
printf '%s\n' FITTING_CENSUS_JOB_COMPLETE >"$output_dir/TERMINAL"
printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"

