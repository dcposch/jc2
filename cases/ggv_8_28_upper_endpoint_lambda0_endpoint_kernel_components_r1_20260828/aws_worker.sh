#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
lane=$2
source_dir="$job_dir/source"
case_dir="$source_dir/jc2/cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_components_r1_20260828"
output_dir="$job_dir/output"
records_dir="$job_dir/records"
run_dir="$output_dir/run"
compiled_dir="$output_dir/compiled"

[[ "$lane" == c8 || "$lane" == q1 || "$lane" == p ]]
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

mkdir -p "$compiled_dir" "$run_dir"
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

stage ADAPTER_SELFCHECK 60 "$output_dir/selfcheck.time" "$output_dir/selfcheck.stdout" "$output_dir/selfcheck.stderr" \
  python3 -B "$case_dir/selfcheck_components.py" --case-dir "$case_dir" || {
    printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK >"$output_dir/TERMINAL"
    exit 34
  }
grep -q '^COMPONENT_ADAPTER_SELFCHECK_PASS$' "$output_dir/selfcheck.stdout" || {
  printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK_MARKER >"$output_dir/TERMINAL"
  exit 35
}

stage BUILD_COMPONENT_SCRIPTS 60 "$output_dir/build.time" "$output_dir/build.stdout" "$output_dir/build.stderr" \
  python3 -B "$case_dir/build_component_scripts.py" \
    --source "$case_dir/input/symbolic_quadratic_q_rankdrop.sing" \
    --fitting "$case_dir/input/FITTING_STRATA_RAW.sing" \
    --output-dir "$compiled_dir" || {
      printf '%s\n' NO_VERDICT_BUILD_FAILURE >"$output_dir/TERMINAL"
      exit 36
    }

upper=$(printf '%s' "$lane" | tr '[:lower:]' '[:upper:]')
stage "PARSE_${upper}" 60 "$output_dir/parse.time" "$output_dir/parse.stdout" "$output_dir/parse.stderr" \
  Singular -q "$compiled_dir/parse_${lane}.sing" || {
    printf '%s\n' NO_VERDICT_MATRIX_PARSE >"$output_dir/TERMINAL"
    exit 37
  }
grep -q "^FULL_MATRIX_PARSE_PASS COMPONENT=${upper}$" "$output_dir/parse.stdout" || {
  printf '%s\n' NO_VERDICT_MATRIX_PARSE_MARKER >"$output_dir/TERMINAL"
  exit 38
}

cd "$run_dir"
if [[ "$lane" == c8 || "$lane" == q1 ]]; then
  stage "COMPONENT_${upper}_GENERIC" 1800 "$run_dir/component.time" "$run_dir/component.stdout" "$run_dir/component.stderr" \
    Singular -q "$compiled_dir/component_${lane}.sing" || true
  if grep -q '^COMPONENT_EXACT_KERNEL_PASS=1$' "$run_dir/component.stdout"; then
    if grep -q '^COMPONENT_GENERIC_ENDPOINT_SURVIVOR=1$' "$run_dir/component.stdout"; then
      component_verdict=PASS_GENERIC_ENDPOINT_SURVIVOR
    elif grep -q '^COMPONENT_GENERIC_ENDPOINT_DEAD=1$' "$run_dir/component.stdout"; then
      component_verdict=GENERIC_ENDPOINT_DEAD_INTERSECTIONS_PENDING
    else
      component_verdict=NO_VERDICT_PULLBACK_MARKER
    fi
  else
    component_verdict=NO_VERDICT_ADAPTER_OR_CAP
  fi
else
  component_verdict=NO_VERDICT_FIXED_SAMPLE_SCREEN
  for sample_id in 01 02 03 04 05 06; do
    stage "COMPONENT_P_SAMPLE_${sample_id}" 300 "$run_dir/p_${sample_id}.time" "$run_dir/p_${sample_id}.stdout" "$run_dir/p_${sample_id}.stderr" \
      Singular -q "$compiled_dir/p_sample_${sample_id}.sing" || true
    if grep -q '^P_SAMPLE_ENDPOINT_SURVIVOR=1$' "$run_dir/p_${sample_id}.stdout"; then
      component_verdict="PASS_EXACT_ENDPOINT_SURVIVOR_SAMPLE_${sample_id}"
      break
    fi
  done
fi

printf 'LANE=%s\nCOMPONENT_VERDICT=%s\n' "$lane" "$component_verdict" >"$output_dir/COMPONENT_VERDICT.txt"
if [[ "$component_verdict" == PASS_* ]]; then
  printf '%s\n' EXACT_ENDPOINT_SURVIVOR_COMPONENT_FOUND >"$output_dir/VERDICT"
else
  printf '%s\n' NO_VERDICT_COMPONENT_INTERSECTIONS_PENDING >"$output_dir/VERDICT"
fi
find "$run_dir" -maxdepth 1 -type f \( -name '*KERNEL*' -o -name '*PULLBACK*' -o -name '*.stdout' -o -name '*.time' \) -print0 | \
  sort -z | xargs -0 sha256sum >"$run_dir/COMPONENT_CERTIFICATES.sha256"
zero_swap || {
  printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"
  exit 91
}
printf '%s\n' ENDPOINT_COMPONENT_JOB_COMPLETE >"$output_dir/TERMINAL"
printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"

