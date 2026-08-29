#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
source_dir="$job_dir/source"
case_dir="$source_dir/jc2/cases/ggv_8_28_upper_endpoint_lambda0_left_kernel_cofactor_r1_20260828"
output_dir="$job_dir/output"
records_dir="$job_dir/records"
run_dir="$output_dir/run"
compiled_dir="$output_dir/compiled"

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
    prlimit --as=206158430208 --fsize=34359738368 \
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
  --job-tag "$(basename "$job_dir")" --output "$records_dir/PREFLIGHT.json" \
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
  python3 -B "$case_dir/selfcheck_adapter.py" --case-dir "$case_dir" || {
    printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK >"$output_dir/TERMINAL"
    exit 34
  }
grep -q '^ADAPTER_SELFCHECK_PASS$' "$output_dir/selfcheck.stdout" || {
  printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK_MARKER >"$output_dir/TERMINAL"
  exit 35
}

stage BUILD_EXACT_SCRIPT 60 "$output_dir/build.time" "$output_dir/build.stdout" "$output_dir/build.stderr" \
  python3 -B "$case_dir/build_left_kernel_script.py" \
    --source "$case_dir/input/symbolic_quadratic_q_rankdrop.sing" \
    --output "$compiled_dir/left_kernel_cofactor.sing" \
    --parse-output "$compiled_dir/left_kernel_cofactor_parse.sing" || {
      printf '%s\n' NO_VERDICT_BUILD_FAILURE >"$output_dir/TERMINAL"
      exit 36
    }

stage PARSE_FULL_MATRIX 60 "$output_dir/parse.time" "$output_dir/parse.stdout" "$output_dir/parse.stderr" \
  Singular -q "$compiled_dir/left_kernel_cofactor_parse.sing" || {
    printf '%s\n' NO_VERDICT_MATRIX_PARSE >"$output_dir/TERMINAL"
    exit 37
  }
grep -q '^FULL_MATRIX_PARSE_PASS ROWS=106 COLS=105$' "$output_dir/parse.stdout" || {
  printf '%s\n' NO_VERDICT_MATRIX_PARSE_MARKER >"$output_dir/TERMINAL"
  exit 38
}

cd "$run_dir"
stage EXACT_LEFT_KERNEL_COFACTOR 5400 "$run_dir/left.time" "$run_dir/left.stdout" "$run_dir/left.stderr" \
  Singular -q "$compiled_dir/left_kernel_cofactor.sing" || true
if ! grep -q '^LEFT_KERNEL_CERTIFICATE_PASS=1$' "$run_dir/left.stdout"; then
  printf '%s\n' NO_VERDICT_LEFT_KERNEL_OR_CAP >"$output_dir/TERMINAL"
  exit 39
fi
for marker in LEFT_KERNEL_REPLAY_ZERO=1 RAW_DENOMINATORS_ONE=1 OMITTED_CALIBRATION=1 ENDPOINT_DUAL_REPLAY_ZERO=1; do
  grep -q "^${marker}$" "$run_dir/left.stdout" || {
    printf '%s\n' NO_VERDICT_EXACT_REPLAY_DISAGREEMENT >"$output_dir/TERMINAL"
    exit 40
  }
done
[[ -s LEFT_KERNEL_RAW.sing && -s LEFT_KERNEL_RAW.tsv && -s ENDPOINT_DUALS_RAW.tsv ]] || {
  printf '%s\n' NO_VERDICT_MISSING_RAW_CERTIFICATE >"$output_dir/TERMINAL"
  exit 41
}

cp LEFT_KERNEL_RAW.sing STRATA_GCD_RUN.sing
cat "$case_dir/strata_tail.sing" >>STRATA_GCD_RUN.sing
stage EXACT_CONTENT_STRATA 1200 "$run_dir/strata.time" "$run_dir/strata.stdout" "$run_dir/strata.stderr" \
  Singular -q STRATA_GCD_RUN.sing || true
grep -q '^STRATA_GCD_PASS=1$' "$run_dir/strata.stdout" || {
  printf '%s\n' NO_VERDICT_STRATA_OR_CAP >"$output_dir/TERMINAL"
  exit 42
}

sha256sum LEFT_KERNEL_RAW.sing LEFT_KERNEL_RAW.tsv ENDPOINT_DUALS_RAW.tsv \
  COFACTOR_CONTENT.txt STRATA_GCD_RUN.sing >CERTIFICATE_FILES.sha256
printf '%s\n' EXACT_LEFT_KERNEL_CERTIFICATE_PASS_RESIDUAL_STRATA_PENDING >"$output_dir/VERDICT"
zero_swap || {
  printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"
  exit 91
}
printf '%s\n' LEFT_KERNEL_JOB_COMPLETE >"$output_dir/TERMINAL"
printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"

