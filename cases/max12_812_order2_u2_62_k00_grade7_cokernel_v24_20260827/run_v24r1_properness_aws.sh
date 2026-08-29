#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V24R1 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: $0 SOURCE_ROOT OUTPUT_ROOT TAG VMEM_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 64
fi

source_root=$1
output_root=$2
tag=$3
vmem_kib=$4
timeout_seconds=$5
freeze=$6
case_rel=cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827

mkdir -p "$output_root/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=F_65521\n'
  printf 'virtual_memory_cap_kib=%s\n' "$vmem_kib"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'design=v24r1_modular_localized_prior_ideal_properness\n'
  printf 'scope=no_exact_Q_no_Wzero_no_grade8_no_arc_no_closure_no_JC2\n'
} > "$output_root/launch_registration.txt"
cd "$source_root"
sha256sum -c "$freeze" > "$output_root/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$vmem_kib"

set +e
/usr/bin/time -v timeout "$timeout_seconds" \
  python3 "$case_rel/compile_v24r1_properness.py" "$output_root/output" \
  >"$output_root/run/compiler.stdout" \
  2>"$output_root/run/compiler.stderr"
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
} >> "$output_root/launch_registration.txt"

if [[ $rc -eq 0 ]] && grep -q '^K00_V24R1=' "$output_root/run/compiler.stdout"; then
  result_status=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["status"])' "$output_root/output/RESULT.json")
  printf 'engine_rc=0\nvalidator=%s\n' "$result_status" > "$output_root/run/FINAL.validation"
else
  printf 'engine_rc=%s\nvalidator=FAIL\n' "$rc" > "$output_root/run/FINAL.validation"
  exit "$rc"
fi

find "$output_root/output" "$output_root/run" "$output_root/freeze_check.stdout" \
  "$output_root/launch_registration.txt" -type f ! -name EVIDENCE.sha256 -print0 \
  | sort -z | xargs -0 sha256sum > "$output_root/EVIDENCE.sha256"
