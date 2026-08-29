#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
mode=$2
source_dir="$job_dir/source"
jc2_dir="$source_dir/jc2"
case_dir="$jc2_dir/cases/ggv_8_28_upper_endpoint_q1_fixed_a_full_raw_split_r2_20260828"
output_dir="$job_dir/output"
records_dir="$job_dir/records"

case "$mode" in
  resume_lambda0)
    system_id=lambda_0_full_qgates
    system_dir="$case_dir/input/lambda_0_full_qgates"
    groebner_cap=600
    exact_cap=1500
    ;;
  compile_lambda1)
    system_id=lambda_1_full_qgates
    system_dir="$output_dir/compiled/lambda_1_full_qgates"
    groebner_cap=300
    exact_cap=900
    ;;
  *)
    printf '%s\n' NO_VERDICT_INVALID_MODE >"$output_dir/TERMINAL"
    exit 29
    ;;
esac

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

fail_terminal() {
  local marker=$1 rc=$2
  printf '%s\n' "$rc" >"$output_dir/LAST_STAGE_RC"
  printf '%s\n' "$marker" >"$output_dir/TERMINAL"
  exit "$rc"
}

printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 "$case_dir/preflight.py" \
  --run-dir "$job_dir" --job-tag "$(basename "$job_dir")" --mode "$mode" \
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
sha256sum -c PREREGISTRATION.sha256 \
  >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || {
    printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"
    exit 33
  }

mkdir -p "$output_dir/validation" "$output_dir/triangular" "$output_dir/groebner"
if [[ "$mode" == compile_lambda1 ]]; then
  mkdir -p "$system_dir"
  if stage_command DESK_LAMBDA1_SPLIT 180 \
    "$output_dir/desk.time" "$output_dir/desk.stdout" "$output_dir/desk.stderr" \
    python3 -B compile_lambda1_slice.py --desk-check; then
    desk_rc=0
  else
    desk_rc=$?
  fi
  [[ "$desk_rc" -eq 0 ]] || fail_terminal NO_VERDICT_LAMBDA1_DESK "$desk_rc"

  if stage_command COMPILE_LAMBDA1_ONLY 2700 \
    "$output_dir/compile.time" "$output_dir/compile.stdout" "$output_dir/compile.stderr" \
    python3 -B compile_lambda1_slice.py --output-dir "$system_dir"; then
    compile_rc=0
  else
    compile_rc=$?
  fi
  [[ "$compile_rc" -eq 0 ]] || fail_terminal NO_VERDICT_LAMBDA1_COMPILE "$compile_rc"

  if stage_command VALIDATE_LAMBDA1_EMISSION 600 \
    "$output_dir/validation/time.txt" "$output_dir/validation/stdout.txt" "$output_dir/validation/stderr.txt" \
    python3 -B validate_emitted_qgate.py \
      --system-dir "$system_dir" --system-id "$system_id" \
      --exact-output "$output_dir/validation/VALIDATION.json"; then
    validate_rc=0
  else
    validate_rc=$?
  fi
else
  if stage_command VALIDATE_FROZEN_LAMBDA0_EMISSION 600 \
    "$output_dir/validation/time.txt" "$output_dir/validation/stdout.txt" "$output_dir/validation/stderr.txt" \
    python3 -B validate_emitted_qgate.py \
      --system-dir "$system_dir" --system-id "$system_id" --frozen-lambda0 \
      --exact-output "$output_dir/validation/VALIDATION.json"; then
    validate_rc=0
  else
    validate_rc=$?
  fi
fi
printf '%s\n' "$validate_rc" >"$output_dir/validation/RC"
[[ "$validate_rc" -eq 0 ]] || fail_terminal NO_VERDICT_EMISSION_VALIDATION "$validate_rc"

if stage_command REDUCE_EMITTED_SYSTEM 1800 \
  "$output_dir/triangular/time.txt" "$output_dir/triangular/stdout.txt" "$output_dir/triangular/stderr.txt" \
  python3 -B reduce_q_gates.py \
    --system "$system_dir/Q_GATE_SYSTEM.json" \
    --output-dir "$output_dir/triangular"; then
  reduce_rc=0
else
  reduce_rc=$?
fi
printf '%s\n' "$reduce_rc" >"$output_dir/triangular/RC"
[[ "$reduce_rc" -eq 0 ]] || fail_terminal NO_VERDICT_REDUCTION "$reduce_rc"

if python3 - "$output_dir/triangular/TRIANGULAR_REDUCTION.json" <<'PY'
import json, sys
item = json.load(open(sys.argv[1]))
raise SystemExit(0 if item["terminal_constant_obstruction"] is not None else 1)
PY
then
  printf '%s\n' EXACT_Q_TRIANGULAR_CONSTANT_OBSTRUCTION >"$output_dir/VERDICT"
  printf '%s\n' EXACT_Q_TRIANGULAR_CONSTANT_OBSTRUCTION >"$output_dir/TERMINAL"
else
  for prime in 65521 65519 65497; do
    if stage_command "GROEBNER_REDUCED_P${prime}" "$groebner_cap" \
      "$output_dir/groebner/p${prime}.time" \
      "$output_dir/groebner/p${prime}.stdout" \
      "$output_dir/groebner/p${prime}.stderr" \
      Singular -q "$output_dir/triangular/reduced_p${prime}.sing"; then
      groebner_rc=0
    else
      groebner_rc=$?
    fi
    printf '%s\n' "$groebner_rc" >"$output_dir/groebner/p${prime}.rc"
  done

  if grep -q 'UNIT=1' "$output_dir/groebner/p65521.stdout" \
    && grep -q 'UNIT=1' "$output_dir/groebner/p65519.stdout" \
    && grep -q 'UNIT=1' "$output_dir/groebner/p65497.stdout"; then
    if stage_command GROEBNER_REDUCED_EXACT_Q_TRACKED "$exact_cap" \
      "$output_dir/groebner/q_tracked.time" \
      "$output_dir/groebner/q_tracked.stdout" \
      "$output_dir/groebner/q_tracked.stderr" \
      bash -c 'cd "$1" && exec Singular -q reduced_q_tracked.sing' _ "$output_dir/triangular"; then
      q_rc=0
    else
      q_rc=$?
    fi
    printf '%s\n' "$q_rc" >"$output_dir/groebner/q_tracked.rc"
    if [[ "$q_rc" -eq 0 ]] \
      && grep -q 'UNIT=1' "$output_dir/groebner/q_tracked.stdout" \
      && grep -q 'BASIS_REPLAY_ZERO=1' "$output_dir/groebner/q_tracked.stdout" \
      && grep -q 'UNIT_REPLAY_ZERO=1' "$output_dir/groebner/q_tracked.stdout"; then
      printf '%s\n' EXACT_Q_UNIT_REDUCED_WITH_REPLAY >"$output_dir/VERDICT"
      printf '%s\n' EXACT_Q_UNIT_REDUCED_WITH_REPLAY >"$output_dir/TERMINAL"
    else
      printf '%s\n' NO_VERDICT_MODULAR_UNIT_EXACT_Q_INCOMPLETE >"$output_dir/VERDICT"
      printf '%s\n' NO_VERDICT_MODULAR_UNIT_EXACT_Q_INCOMPLETE >"$output_dir/TERMINAL"
    fi
  else
    printf '%s\n' NO_VERDICT_MODULAR_SCREEN_NONUNIT_OR_INCOMPLETE >"$output_dir/VERDICT"
    printf '%s\n' NO_VERDICT_MODULAR_SCREEN_NONUNIT_OR_INCOMPLETE >"$output_dir/TERMINAL"
  fi
fi

zero_swap || { printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"; exit 91; }
python3 - "$mode" "$system_id" "$output_dir" <<'PY'
import hashlib, json, sys
from pathlib import Path
mode, system_id, output = sys.argv[1], sys.argv[2], Path(sys.argv[3])
reduction = json.loads((output / "triangular/TRIANGULAR_REDUCTION.json").read_text())
validation = json.loads((output / "validation/VALIDATION.json").read_text())
verdict = (output / "VERDICT").read_text().strip()
result = {
    "schema": "GGV-8_28-QGATE-SPLIT-RESULT-v1",
    "mode": mode,
    "system_id": system_id,
    "verdict": verdict,
    "source_system_sha256": reduction["source_system_sha256"],
    "validation_sha256": hashlib.sha256((output / "validation/VALIDATION.json").read_bytes()).hexdigest(),
    "reduction_sha256": hashlib.sha256((output / "triangular/TRIANGULAR_REDUCTION.json").read_bytes()).hexdigest(),
    "pivot_count": reduction["pivot_count"],
    "free_variable_count": reduction["free_variable_count"],
    "active_free_variable_count": reduction["active_free_variable_count"],
    "compatibility_count": reduction["compatibility_count"],
    "terminal_constant_obstruction": reduction["terminal_constant_obstruction"],
    "scope": {
        "necessary_qgate_screen_only": True,
        "nonunit_or_timeout_is_not_a_survivor": True,
        "lambda1_normalization_claimed": False,
        "raw_endpoint_witness_produced": False,
        "classification_requires_exact_Q_replay_or_exact_triangular_constant": True,
    },
    "validation_status": validation["status"],
}
(output / "RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
PY
printf '%s\n' RESULT_FROZEN >"$output_dir/CURRENT_STAGE"
