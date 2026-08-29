#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
source_root="$job_dir/source/jc2"
case_dir="$source_root/cases/d43_exact_sparse_rows_20260828"
manifest="$case_dir/PILOT_MANIFEST.json"
records_dir="$job_dir/records"
output_dir="$job_dir/output"
checkpoint_dir="$output_dir/sparse_checkpoints"
row_dir="$output_dir/rows"

[[ "$(uname -s)" == Linux ]] || exit 90
[[ -s "$records_dir/REGISTERED.json" ]] || exit 91
[[ -n "${AWS_RUN_TAG:-}" ]] || exit 92
[[ -n "${AWS_EXPECTED_HOSTNAME:-}" ]] || exit 93
[[ "$AWS_RUN_TAG" == "$(basename "$job_dir")" ]] || exit 94

zero_swap() {
  local total free
  total=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo)
  free=$(awk '/^SwapFree:/{print $2}' /proc/meminfo)
  [[ "$total" == 0 && "$free" == 0 ]]
}

stage() {
  local name=$1 timeout_seconds=$2
  shift 2
  printf '%s\n' "$name" >"$output_dir/CURRENT_STAGE"
  zero_swap || return 95
  set +e
  /usr/bin/time -v -o "$output_dir/${name}.time" \
    timeout --foreground --signal=TERM --kill-after=60s "$timeout_seconds" \
    prlimit --as=549755813888 --fsize=137438953472 \
    taskset --cpu-list 2 nice -n 10 env PYTHONDONTWRITEBYTECODE=1 \
    "$@" >"$output_dir/${name}.stdout" 2>"$output_dir/${name}.stderr"
  local rc=$?
  set -e
  printf '%s\n' "$rc" >"$output_dir/${name}.rc"
  zero_swap || return 96
  return "$rc"
}

mkdir -p "$records_dir" "$output_dir" "$checkpoint_dir" "$row_dir"
printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 -B "$case_dir/aws_preflight.py" \
  --manifest "$manifest" --run-dir "$job_dir" \
  --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || {
    printf '%s\n' NO_VERDICT_PREFLIGHT >"$output_dir/TERMINAL"
    exit 40
  }

cd "$source_root"
sha256sum -c cases/d43_exact_sparse_rows_20260828/SOURCE.sha256 \
  >"$records_dir/source_check.stdout" 2>"$records_dir/source_check.stderr" || {
    printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"
    exit 41
  }

stage BUILD_SPARSE_CHECKPOINTS 86400 \
  python3 -B "$case_dir/selected_rows.py" build-sparse \
  --manifest "$manifest" --output-dir "$checkpoint_dir" || {
    printf '%s\n' NO_VERDICT_SPARSE_BUILD >"$output_dir/TERMINAL"
    exit 42
  }
grep -q 'EXACT_SPARSE_CHECKPOINTS_COMPLETE' \
  "$checkpoint_dir/SPARSE_CHECKPOINTS.json" || {
    printf '%s\n' NO_VERDICT_SPARSE_BUILD_MARKER >"$output_dir/TERMINAL"
    exit 43
  }

stage EMIT_BAND20 21600 \
  python3 -B "$case_dir/selected_rows.py" emit-shard \
  --manifest "$manifest" --sparse-receipt \
  "$checkpoint_dir/SPARSE_CHECKPOINTS.json" --bands 20 \
  --output "$row_dir/d43_exact_band20.pkl" || {
    printf '%s\n' NO_VERDICT_BAND20_EMISSION >"$output_dir/TERMINAL"
    exit 44
  }
grep -q 'PASS_EXACT_D21_BAND20_EQUALITY' \
  "$row_dir/d43_exact_band20.pkl.receipt.json" || {
    printf '%s\n' NO_VERDICT_D21_REGRESSION >"$output_dir/TERMINAL"
    exit 45
  }

find "$output_dir" -type f -print0 | sort -z | xargs -0 sha256sum \
  >"$output_dir/ARTIFACTS.sha256"
zero_swap || {
  printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"
  exit 96
}
printf '%s\n' BAND20_EXACT_SOURCE_EMISSION_COMPLETE_PENDING_REVIEW \
  >"$output_dir/VERDICT"
printf '%s\n' D43_EXACT_BAND20_PILOT_COMPLETE >"$output_dir/TERMINAL"
printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"
