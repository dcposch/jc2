#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only D8 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: run_D8_aws.sh AWS_ROOT AWS_JOB TAG FIELD CAP_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
field=$4
cap_kib=$5
timeout_seconds=$6
freeze=$7
rel=cases/max12_812_order2_u2_62_k00_filtered_macaulay_d8_v10_20260827
v9rel=cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827
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
python3 "$rel/emit_D8.py" "$aws_job/output/emitted" \
  > "$aws_job/run/emitter.stdout" 2> "$aws_job/run/emitter.stderr"
g++ -O3 -std=c++17 "$v9rel/macaulay_rref.cpp" -o "$aws_job/output/macaulay_rref" -lflint -lgmp \
  > "$aws_job/run/compiler.stdout" 2> "$aws_job/run/compiler.stderr"
sha256sum "$aws_job/output/macaulay_rref" > "$aws_job/run/BINARY.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_job/run" "$lane_tag" timeout "$timeout_seconds" \
  "$aws_job/output/macaulay_rref" --field "$field" \
  "$aws_job/output/emitted/macaulay_D8.tsv" "$aws_job/output/solution_D8.tsv"
rc=$?
set -e
printf 'engine_rc=%s\n' "$rc" > "$aws_job/run/FINAL.validation"
if [[ "$rc" -ne 0 ]]; then
  exit "$rc"
fi
python3 "$rel/validate_D8.py" "$aws_job/run/RESULT.json" \
  "$aws_job/output/emitted/SOURCE_AUDIT.json" "$aws_job/output/emitted/macaulay_D8.tsv" \
  "$aws_job/output/solution_D8.tsv" --field "$field" \
  > "$aws_job/run/validator.stdout" 2> "$aws_job/run/validator.stderr"
printf 'validator=PASS_FILTERED_D8\n' >> "$aws_job/run/FINAL.validation"
sha256sum "$aws_job/run/RESULT.json" "$aws_job/output/emitted/SOURCE_AUDIT.json" \
  "$aws_job/output/emitted/macaulay_D8.tsv" "$aws_job/output/solution_D8.tsv" \
  > "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
