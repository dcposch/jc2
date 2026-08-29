#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only filtered Macaulay runner refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: run_filtered_macaulay_aws.sh AWS_ROOT AWS_JOB TAG FIELD CAP_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
field=$4
cap_kib=$5
timeout_seconds=$6
freeze=$7
rel=cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827
mkdir -p "$aws_job/run" "$aws_job/output"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=%s\n' "$field"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"
python3 "$rel/emit_filtered_macaulay.py" "$aws_job/output/emitted" --max-cutoff 7 \
  > "$aws_job/run/emitter.stdout" 2> "$aws_job/run/emitter.stderr"
g++ -O3 -std=c++17 "$rel/macaulay_rref.cpp" -o "$aws_job/output/macaulay_rref" -lflint -lgmp \
  > "$aws_job/run/compiler.stdout" 2> "$aws_job/run/compiler.stderr"
sha256sum "$aws_job/output/macaulay_rref" > "$aws_job/run/BINARY.sha256"
set +e
for cutoff in 2 3 4 5 6 7; do
  "$aws_root/ops/aws_exact_lane.sh" \
    "$aws_root" "$aws_job/run" "${lane_tag}_D${cutoff}" timeout "$timeout_seconds" \
    "$aws_job/output/macaulay_rref" --field "$field" \
    "$aws_job/output/emitted/macaulay_D${cutoff}.tsv" \
    "$aws_job/output/solution_D${cutoff}.tsv"
  rc=$?
  if [[ "$rc" -ne 0 ]]; then
    printf 'cutoff=%s rc=%s\n' "$cutoff" "$rc" > "$aws_job/run/FAIL.validation"
    exit "$rc"
  fi
done
set -e
validator_args=()
for cutoff in 2 3 4 5 6 7; do
  validator_args+=(--matrix-solution \
    "$aws_job/output/emitted/macaulay_D${cutoff}.tsv" \
    "$aws_job/output/solution_D${cutoff}.tsv")
done
python3 "$rel/validate_filtered_macaulay.py" \
  "$aws_job/run/RESULT.json" "$aws_job/output/emitted/SOURCE_AUDIT.json" \
  "$aws_job/output/emitted/load_normal_stencil.json" --field "$field" \
  "${validator_args[@]}" \
  > "$aws_job/run/validator.stdout" 2> "$aws_job/run/validator.stderr"
printf 'validator=PASS_FILTERED_D7\n' > "$aws_job/run/FINAL.validation"
sha256sum "$aws_job/run/RESULT.json" "$aws_job/output/emitted/SOURCE_AUDIT.json" \
  "$aws_job/output/emitted/load_normal_stencil.json" "$aws_job/output/solution_D7.tsv" \
  > "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
