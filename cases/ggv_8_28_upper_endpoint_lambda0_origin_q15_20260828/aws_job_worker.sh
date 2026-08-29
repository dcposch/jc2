#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
system_mode=$2
host_alias=$3
source_dir="$job_dir/source"
jc2_dir="$source_dir/jc2"
case_dir="$jc2_dir/cases/ggv_8_28_upper_endpoint_lambda0_origin_q15_20260828"
output_dir="$job_dir/output"
records_dir="$job_dir/records"

[[ "$system_mode" == general || "$system_mode" == control_q_e_F8_r_zero ]]
[[ "$host_alias" == r6a || "$host_alias" == r6b ]]

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

stage_command() {
  local stage=$1 cap=$2 time_file=$3 stdout_file=$4 stderr_file=$5
  shift 5
  printf '%s\n' "$stage" >"$output_dir/CURRENT_STAGE"
  zero_swap || return 90
  set +e
  /usr/bin/time -v -o "$time_file" \
    timeout --foreground --signal=TERM --kill-after=30s "$cap" \
    prlimit --as=68719476736 --fsize=8589934592 \
    taskset --cpu-list 1 env PYTHONDONTWRITEBYTECODE=1 "$@" \
    >"$stdout_file" 2>"$stderr_file"
  local rc=$?
  set -e
  zero_swap || return 91
  return "$rc"
}

printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 "$source_dir/runner/aws_preflight.py" \
  --run-dir "$job_dir" --job-tag "$(basename "$job_dir")" \
  --host-alias "$host_alias" --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || {
    printf '%s\n' NO_VERDICT_PREFLIGHT_OR_ACTIVE_CONFLICT >"$output_dir/TERMINAL"
    exit 31
  }
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$case_dir"
sha256sum -c SOURCE.sha256 \
  >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || {
    printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"; exit 32; }
printf '%s  %s\n' \
  72325a3bf4fe4d66aa87463c13c393a078355cc5d6c2b5ff5698ecfaf0f06ede \
  PREREGISTRATION.md | sha256sum -c - \
  >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || {
    printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"; exit 33; }

mkdir -p "$output_dir/prep/system" "$output_dir/reduction" "$output_dir/runs"
stage_command DESK_CHECK 120 \
  "$output_dir/prep/desk.time" "$output_dir/prep/desk.stdout" "$output_dir/prep/desk.stderr" \
  python3 -B compile_origin_q15.py --desk-check || {
    printf '%s\n' NO_VERDICT_DESK_CHECK >"$output_dir/TERMINAL"; exit 34; }

stage_command "COMPILE_${system_mode}" 2700 \
  "$output_dir/prep/compile.time" "$output_dir/prep/compile.stdout" "$output_dir/prep/compile.stderr" \
  python3 -B compile_origin_q15.py --system "$system_mode" \
    --output-dir "$output_dir/prep/system" || {
    printf '%s\n' NO_VERDICT_COMPILE >"$output_dir/TERMINAL"; exit 35; }

stage_command "REDUCE_${system_mode}" 2700 \
  "$output_dir/reduction/reduce.time" "$output_dir/reduction/reduce.stdout" "$output_dir/reduction/reduce.stderr" \
  python3 -B reduce_origin_q15.py \
    --system "$output_dir/prep/system/ORIGIN_Q15_SYSTEM.json" \
    --output-dir "$output_dir/reduction" || {
    printf '%s\n' NO_VERDICT_REDUCTION_OR_RANK_DISAGREEMENT >"$output_dir/TERMINAL"; exit 36; }

run_singular() {
  local task=$1 prime=$2 cap=$3
  local stem="${task}_p${prime}"
  local script="$output_dir/reduction/${stem}.sing"
  mkdir -p "$output_dir/runs/$task"
  if stage_command "${task^^}_P${prime}" "$cap" \
    "$output_dir/runs/$task/p${prime}.time" \
    "$output_dir/runs/$task/p${prime}.stdout" \
    "$output_dir/runs/$task/p${prime}.stderr" \
    bash -c 'cd "$1" && exec Singular -q "$2"' _ \
      "$output_dir/reduction" "$script"; then
    rc=0
  else
    rc=$?
  fi
  printf '%s\n' "$rc" >"$output_dir/runs/$task/p${prime}.rc"
}

run_exact() {
  local task=$1 cap=$2
  local script="$output_dir/reduction/${task}_q_tracked.sing"
  mkdir -p "$output_dir/runs/$task"
  if stage_command "${task^^}_EXACT_Q_TRACKED" "$cap" \
    "$output_dir/runs/$task/q.time" \
    "$output_dir/runs/$task/q.stdout" \
    "$output_dir/runs/$task/q.stderr" \
    bash -c 'cd "$1" && exec Singular -q "$2"' _ \
      "$output_dir/reduction" "$script"; then
    rc=0
  else
    rc=$?
  fi
  printf '%s\n' "$rc" >"$output_dir/runs/$task/q.rc"
}

all_marker() {
  local task=$1 marker=$2
  grep -q "$marker" "$output_dir/runs/$task/p65521.stdout" \
    && grep -q "$marker" "$output_dir/runs/$task/p65519.stdout" \
    && grep -q "$marker" "$output_dir/runs/$task/p65497.stdout"
}

# G15-only membership is a diagnostic/control and never classifies general.
for prime in 65521 65519 65497; do run_singular membership_g15 "$prime" 300; done
if all_marker membership_g15 'TARGET_NF_ZERO=1'; then
  printf '%s\n' THREE_PRIME_G15_MEMBERSHIP >"$output_dir/runs/membership_g15/MODULAR_MARKER"
  if [[ "$system_mode" == control_q_e_F8_r_zero ]]; then
    run_exact membership_g15 900
    if grep -q 'TARGET_NF_ZERO=1' "$output_dir/runs/membership_g15/q.stdout" \
      && grep -q 'BASIS_REPLAY_ZERO=1' "$output_dir/runs/membership_g15/q.stdout" \
      && grep -q 'TARGET_REPLAY_ZERO=1' "$output_dir/runs/membership_g15/q.stdout"; then
      printf '%s\n' EXACT_Q_G15_CONTROL_MEMBERSHIP_REPLAY \
        >"$output_dir/runs/membership_g15/EXACT_MARKER"
    fi
  fi
fi

for prime in 65521 65519 65497; do run_singular membership_base "$prime" 300; done
verdict=""
if all_marker membership_base 'TARGET_NF_ZERO=1'; then
  printf '%s\n' THREE_PRIME_BASE_MEMBERSHIP >"$output_dir/runs/membership_base/MODULAR_MARKER"
  run_exact membership_base 900
  if grep -q 'TARGET_NF_ZERO=1' "$output_dir/runs/membership_base/q.stdout" \
    && grep -q 'BASIS_REPLAY_ZERO=1' "$output_dir/runs/membership_base/q.stdout" \
    && grep -q 'TARGET_REPLAY_ZERO=1' "$output_dir/runs/membership_base/q.stdout"; then
    verdict=EXACT_Q_BASE_MEMBERSHIP_ENDPOINT_IMPOSSIBLE
  fi
fi

if [[ -z "$verdict" ]]; then
  for prime in 65521 65519 65497; do run_singular full "$prime" 300; done
  if all_marker full 'UNIT=1'; then
    printf '%s\n' THREE_PRIME_FULL_UNIT >"$output_dir/runs/full/MODULAR_MARKER"
    run_exact full 900
    if grep -q 'UNIT=1' "$output_dir/runs/full/q.stdout" \
      && grep -q 'BASIS_REPLAY_ZERO=1' "$output_dir/runs/full/q.stdout" \
      && grep -q 'UNIT_REPLAY_ZERO=1' "$output_dir/runs/full/q.stdout"; then
      verdict=EXACT_Q_FULL_UNIT_ENDPOINT_IMPOSSIBLE
    fi
  fi
fi

if [[ -z "$verdict" ]]; then verdict=NO_VERDICT_MODULAR_SURVIVOR_OR_CAP; fi
printf '%s\n' "$verdict" >"$output_dir/VERDICT"
zero_swap || { printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"; exit 91; }
printf '%s\n' ORIGIN_Q15_SCREEN_COMPLETE >"$output_dir/TERMINAL"
