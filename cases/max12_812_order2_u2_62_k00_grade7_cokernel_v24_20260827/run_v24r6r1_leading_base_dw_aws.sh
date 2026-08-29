#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V24R6R1 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: $0 SOURCE_ROOT OUTPUT_ROOT TAG VMEM_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 64
fi

k00_source_root=$1
k00_output_root=$2
k00_tag=$3
k00_vmem_kib=$4
k00_timeout_seconds=$5
k00_freeze=$6
k00_case_rel=cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827

mkdir -p "$k00_output_root/run"
{
  printf 'tag=%s\n' "$k00_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'design=v24r6r1_exact_Q_seven_actual_eight_logical_leading_base_DW\n'
  printf 'workers=1\n'
  printf 'virtual_memory_cap_kib=%s\n' "$k00_vmem_kib"
  printf 'outer_timeout_seconds=%s\n' "$k00_timeout_seconds"
  printf 'scope=exact_Q_D_k10_0_W_leading_base_F10_only_no_arc_no_closure_no_JC2\n'
} > "$k00_output_root/launch_registration.txt"
cd "$k00_source_root"
sha256sum -c "$k00_freeze" > "$k00_output_root/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$k00_tag"
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
ulimit -v "$k00_vmem_kib"

set +e
/usr/bin/time -v timeout "$k00_timeout_seconds" \
  python3 "$k00_case_rel/compile_v24r6r1_leading_base_dw.py" \
  "$k00_output_root/output" \
  >"$k00_output_root/run/compiler.stdout" \
  2>"$k00_output_root/run/compiler.stderr"
k00_rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$k00_rc"
} >> "$k00_output_root/launch_registration.txt"

if [[ $k00_rc -eq 0 ]] && grep -q '^K00_V24R6R1=' "$k00_output_root/run/compiler.stdout"; then
  k00_result_status=$(python3 -c \
    'import json,sys; print(json.load(open(sys.argv[1]))["status"])' \
    "$k00_output_root/output/RESULT.json")
  printf 'engine_rc=0\nvalidator=%s\n' "$k00_result_status" \
    > "$k00_output_root/run/FINAL.validation"
else
  printf 'engine_rc=%s\nvalidator=FAIL\n' "$k00_rc" \
    > "$k00_output_root/run/FINAL.validation"
  exit "$k00_rc"
fi

find "$k00_output_root/output" "$k00_output_root/run" \
  "$k00_output_root/freeze_check.stdout" \
  "$k00_output_root/launch_registration.txt" \
  -type f ! -name EVIDENCE.sha256 -print0 \
  | sort -z | xargs -0 sha256sum > "$k00_output_root/EVIDENCE.sha256"
