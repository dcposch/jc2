#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
source_root="$job_dir/source/jc2"
case_dir="$source_root/cases/d43_exact_sparse_rows_v2_20260828"
manifest="$case_dir/PIPELINE_MANIFEST.json"
records_dir="$job_dir/records"
output_dir="$job_dir/output"
sides_dir="$output_dir/sides"

[[ "$(uname -s)" == Linux ]] || exit 90
[[ -n "${AWS_RUN_TAG:-}" ]] || exit 91
[[ -n "${AWS_EXPECTED_HOSTNAME:-}" ]] || exit 92
[[ "$AWS_RUN_TAG" == "$(basename "$job_dir")" ]] || exit 93

atomic_marker() {
  local path=$1 value=$2 temporary
  temporary="${path}.tmp.$$"
  printf '%s\n' "$value" >"$temporary"
  mv "$temporary" "$path"
}

zero_swap() {
  local total free
  total=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo)
  free=$(awk '/^SwapFree:/{print $2}' /proc/meminfo)
  [[ "$total" == 0 && "$free" == 0 ]]
}

fail_terminal() {
  atomic_marker "$output_dir/TERMINAL" "$1"
  exit "$2"
}

run_capped() {
  local name=$1 cpu=$2 address_space=$3 timeout_seconds=$4
  shift 4
  zero_swap || return 95
  set +e
  /usr/bin/time -v -o "$output_dir/${name}.time" \
    timeout --foreground --signal=TERM --kill-after=60s "$timeout_seconds" \
    prlimit --as="$address_space" --fsize=137438953472 \
    taskset --cpu-list "$cpu" nice -n 10 env PYTHONDONTWRITEBYTECODE=1 \
    "$@" >"$output_dir/${name}.stdout" 2>"$output_dir/${name}.stderr"
  local rc=$?
  set -e
  atomic_marker "$output_dir/${name}.rc" "$rc"
  zero_swap || return 96
  return "$rc"
}

mkdir -p "$records_dir" "$output_dir" "$sides_dir"
[[ -s "$records_dir/REGISTERED.json" ]] || fail_terminal NO_VERDICT_NO_REGISTRATION 39
atomic_marker "$output_dir/CURRENT_STAGE" PREFLIGHT
python3 -B "$case_dir/aws_preflight_v2.py" \
  --manifest "$manifest" --run-dir "$job_dir" \
  --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || \
  fail_terminal NO_VERDICT_PREFLIGHT 40

cd "$source_root"
sha256sum -c cases/d43_exact_sparse_rows_v2_20260828/OPERATIONAL_SOURCE.sha256 \
  >"$records_dir/source_check.stdout" 2>"$records_dir/source_check.stderr" || \
  fail_terminal NO_VERDICT_SOURCE_DRIFT 41

atomic_marker "$output_dir/CURRENT_STAGE" BUILD_INDEPENDENT_F_G_CONCURRENT
run_capped BUILD_F 2 412316860416 86400 \
  python3 -B "$case_dir/selected_rows_v2.py" build-side \
  --manifest "$manifest" --preflight-receipt "$records_dir/PREFLIGHT.json" \
  --side f --output "$sides_dir/f.pkl" &
pid_f=$!
run_capped BUILD_G 3 412316860416 86400 \
  python3 -B "$case_dir/selected_rows_v2.py" build-side \
  --manifest "$manifest" --preflight-receipt "$records_dir/PREFLIGHT.json" \
  --side g --output "$sides_dir/g.pkl" &
pid_g=$!
set +e
wait "$pid_f"; rc_f=$?
wait "$pid_g"; rc_g=$?
set -e
[[ "$rc_f" == 0 && "$rc_g" == 0 ]] || \
  fail_terminal NO_VERDICT_INDEPENDENT_SIDE_BUILD 42
zero_swap || fail_terminal NO_VERDICT_SWAP_DRIFT 96

atomic_marker "$output_dir/CURRENT_STAGE" ASSEMBLE_MATCHED_PAIR
run_capped ASSEMBLE_PAIR 2 274877906944 7200 \
  python3 -B "$case_dir/selected_rows_v2.py" assemble-pair \
  --manifest "$manifest" --preflight-receipt "$records_dir/PREFLIGHT.json" \
  --f-receipt "$sides_dir/f.pkl.receipt.json" \
  --g-receipt "$sides_dir/g.pkl.receipt.json" \
  --output "$sides_dir/PAIR.json" || \
  fail_terminal NO_VERDICT_PAIR_CUSTODY 43

atomic_marker "$output_dir/CURRENT_STAGE" CONDITIONAL_BAND20_THEN_ALL184
run_capped CONDITIONAL_EMIT_ALL 2 549755813888 86400 \
  python3 -B "$case_dir/selected_rows_v2.py" conditional-emit-all \
  --manifest "$manifest" --preflight-receipt "$records_dir/PREFLIGHT.json" \
  --pair "$sides_dir/PAIR.json" --output-dir "$output_dir" || \
  fail_terminal NO_VERDICT_COLLAPSED_D21_OR_ALL184 44

atomic_marker "$output_dir/CURRENT_STAGE" FINALIZE_ATOMIC_CUSTODY
zero_swap || fail_terminal NO_VERDICT_SWAP_DRIFT 96
set +e
/usr/bin/time -v -o "$records_dir/finalize.time" \
  timeout --foreground --signal=TERM --kill-after=60s 3600 \
  prlimit --as=68719476736 --fsize=137438953472 \
  taskset --cpu-list 2 nice -n 10 env PYTHONDONTWRITEBYTECODE=1 \
  python3 -B "$case_dir/selected_rows_v2.py" finalize \
  --manifest "$manifest" --preflight-receipt "$records_dir/PREFLIGHT.json" \
  --output-dir "$output_dir" \
  >"$records_dir/finalize.stdout" 2>"$records_dir/finalize.stderr"
finalize_rc=$?
set -e
atomic_marker "$records_dir/finalize.rc" "$finalize_rc"
[[ "$finalize_rc" == 0 ]] || fail_terminal NO_VERDICT_FINAL_CUSTODY 45
zero_swap || fail_terminal NO_VERDICT_SWAP_DRIFT 96
