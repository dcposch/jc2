#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
source_dir="$job_dir/source"
jc2_dir="$source_dir/jc2"
case_dir="$jc2_dir/cases/ggv_8_28_upper_endpoint_q1_fixed_a_full_raw_20260828"
output_dir="$job_dir/output"
records_dir="$job_dir/records"

registration_deadline=$((SECONDS + 30))
while [[ ! -f "$records_dir/REGISTERED" ]]; do
  if (( SECONDS >= registration_deadline )); then
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

stage_command() {
  local stage=$1 cap=$2 time_file=$3 stdout_file=$4 stderr_file=$5
  shift 5
  printf '%s\n' "$stage" >"$output_dir/CURRENT_STAGE"
  zero_swap || return 90
  set +e
  /usr/bin/time -v -o "$time_file" \
    timeout --foreground --signal=TERM --kill-after=30s "$cap" \
    prlimit --as=68719476736 --fsize=17179869184 \
    taskset --cpu-list 1 env PYTHONDONTWRITEBYTECODE=1 "$@" \
    >"$stdout_file" 2>"$stderr_file"
  local rc=$?
  set -e
  zero_swap || return 91
  return "$rc"
}

printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 "$source_dir/runner/preflight.py" \
  --run-dir "$job_dir" --job-tag "$(basename "$job_dir")" \
  --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || {
    printf '%s\n' NO_VERDICT_PREFLIGHT_OR_ACTIVE_CONFLICT >"$output_dir/TERMINAL"
    exit 31
  }
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$case_dir"
sha256sum -c SOURCE.sha256 \
  >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || {
    printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"
    exit 32
  }
printf '%s  %s\n' \
  0bf429c75a33efa31abedb98c5e16848f0f2385f873776f1a3161d2572c12b2f \
  PREREGISTRATION.md | sha256sum -c - \
  >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || {
    printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"
    exit 33
  }

mkdir -p "$output_dir/prep/q_gates" "$output_dir/prep/raw" \
  "$output_dir/branches/lambda_0" "$output_dir/branches/lambda_1"

stage_command DESK_Q_GATES 120 \
  "$output_dir/prep/q_desk.time" "$output_dir/prep/q_desk.stdout" "$output_dir/prep/q_desk.stderr" \
  python3 -B compile_q_gates.py --desk-check || {
    printf '%s\n' NO_VERDICT_Q_DESK >"$output_dir/TERMINAL"; exit 34; }
stage_command DESK_RAW 120 \
  "$output_dir/prep/raw_desk.time" "$output_dir/prep/raw_desk.stdout" "$output_dir/prep/raw_desk.stderr" \
  python3 -B compile_fixed_q1_raw.py --desk-check || {
    printf '%s\n' NO_VERDICT_RAW_DESK >"$output_dir/TERMINAL"; exit 35; }

stage_command COMPILE_Q_GATES 1800 \
  "$output_dir/prep/q_compile.time" "$output_dir/prep/q_compile.stdout" "$output_dir/prep/q_compile.stderr" \
  python3 -B compile_q_gates.py --output-dir "$output_dir/prep/q_gates" || {
    printf '%s\n' NO_VERDICT_Q_COMPILE >"$output_dir/TERMINAL"; exit 36; }
stage_command COMPILE_FULL_RAW_D35 1800 \
  "$output_dir/prep/raw_compile.time" "$output_dir/prep/raw_compile.stdout" "$output_dir/prep/raw_compile.stderr" \
  python3 -B compile_fixed_q1_raw.py --output-dir "$output_dir/prep/raw" || {
    printf '%s\n' NO_VERDICT_RAW_COMPILE >"$output_dir/TERMINAL"; exit 37; }

declare -a systems=(
  lambda_0_c2_nonzero_exact_D0_reduced_qgates
  lambda_0_full_qgates
  lambda_1_full_qgates
)

for system in "${systems[@]}"; do
  if [[ "$system" == lambda_1* ]]; then
    branch=lambda_1
  else
    branch=lambda_0
  fi
  system_out="$output_dir/branches/$branch/$system"
  mkdir -p "$system_out/triangular" "$system_out/groebner"
  if stage_command "REDUCE_$system" 1800 \
    "$system_out/reduce.time" "$system_out/reduce.stdout" "$system_out/reduce.stderr" \
    python3 -B reduce_q_gates.py \
      --system "$output_dir/prep/q_gates/$system/Q_GATE_SYSTEM.json" \
      --output-dir "$system_out/triangular"; then
    reduce_rc=0
  else
    reduce_rc=$?
  fi
  printf '%s\n' "$reduce_rc" >"$system_out/REDUCE_RC"
  if [[ "$reduce_rc" -ne 0 ]]; then
    printf '%s\n' NO_VERDICT_REDUCTION >"$system_out/VERDICT"
    continue
  fi

  for prime in 65521 65519 65497; do
    if stage_command "GROEBNER_${system}_P${prime}" 600 \
      "$system_out/groebner/p${prime}.time" \
      "$system_out/groebner/p${prime}.stdout" \
      "$system_out/groebner/p${prime}.stderr" \
      Singular -q "$system_out/triangular/reduced_p${prime}.sing"; then
      groebner_rc=0
    else
      groebner_rc=$?
    fi
    printf '%s\n' "$groebner_rc" >"$system_out/groebner/p${prime}.rc"
  done

  if grep -q 'UNIT=1' "$system_out/groebner/p65521.stdout" \
    && grep -q 'UNIT=1' "$system_out/groebner/p65519.stdout" \
    && grep -q 'UNIT=1' "$system_out/groebner/p65497.stdout"; then
    if stage_command "GROEBNER_${system}_EXACT_Q_TRACKED" 1800 \
      "$system_out/groebner/q_tracked.time" \
      "$system_out/groebner/q_tracked.stdout" \
      "$system_out/groebner/q_tracked.stderr" \
      Singular -q "$system_out/triangular/reduced_q_tracked.sing"; then
      q_rc=0
    else
      q_rc=$?
    fi
    printf '%s\n' "$q_rc" >"$system_out/groebner/q_tracked.rc"
    if [[ "$q_rc" -eq 0 ]] \
      && grep -q 'UNIT=1' "$system_out/groebner/q_tracked.stdout" \
      && grep -q 'BASIS_REPLAY_ZERO=1' "$system_out/groebner/q_tracked.stdout" \
      && grep -q 'UNIT_REPLAY_ZERO=1' "$system_out/groebner/q_tracked.stdout"; then
      printf '%s\n' EXACT_Q_UNIT_REDUCED_WITH_REPLAY >"$system_out/VERDICT"
    else
      printf '%s\n' MODULAR_UNIT_EXACT_Q_NO_VERDICT >"$system_out/VERDICT"
    fi
  else
    printf '%s\n' MODULAR_SCREEN_NONUNIT_OR_INCOMPLETE >"$system_out/VERDICT"
  fi
done

zero_swap || { printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"; exit 91; }
printf '%s\n' STAGE1_FULLTAIL_QGATES_COMPLETE >"$output_dir/TERMINAL"
