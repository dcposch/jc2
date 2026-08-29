#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1
aws_job=$2
tag=$3
cap_kib=$4
mode=$5
characteristic=$6
compile_timeout=$7
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\nlauncher_pid=%s\njob_dir=%s\nstart_utc=%s\n' \
    "$tag" "$(hostname)" "$$" "$aws_job" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'mode=%s\ncharacteristic=%s\ncompile_timeout_seconds=%s\nvirtual_memory_cap_kib=%s\n' \
    "$mode" "$characteristic" "$compile_timeout" "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_p0_odd_sheet_receivers_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" \
  timeout "$compile_timeout" python3 \
  cases/max12_812_order2_p0_odd_sheet_receivers_20260826/compile_receivers.py \
  "$aws_job/compiled" --mode "$mode" --characteristic "$characteristic"
compiler_rc=$?
set -e
stdout="$aws_job/run/$tag.stdout"
validation="$aws_job/run/$tag.validation"
printf 'compiler_rc=%s\n' "$compiler_rc" > "$validation"
if [[ "$compiler_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"
  exit 124
fi
if [[ "$compiler_rc" -ne 0 ]]; then
  printf 'validator=FAIL_COMPILER\n' >> "$validation"
  exit "$compiler_rc"
fi
for required in \
  'P0_ODD_RECEIVER_SOURCE_HASHES=PASS' \
  "P0_ODD_RECEIVER_MODE=$mode"
do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"
    exit 90
  fi
done
case "$mode" in
  terminal)
    status='PASS-P0-ODD-TERMINAL-RAW-DAG-TYPED'
    endpoint='RAW_TYPED_NOT_SOLVED'
    ;;
  taylor0)
    status='PASS-P0-ODD-TAYLOR-X0-TYPED-WAITING-GATE-A'
    endpoint='TYPED_WAITING_GATE_A'
    ;;
  taylor1)
    status='PASS-P0-ODD-TAYLOR-X1-TYPED-WAITING-GATE-A'
    endpoint='TYPED_WAITING_GATE_A'
    ;;
  *) exit 125 ;;
esac
for required in \
  "P0_ODD_RECEIVER_STATUS=$status" \
  "P0_ODD_RECEIVER_MATHEMATICAL_ENDPOINT=$endpoint"
do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"
    exit 90
  fi
done
if [[ "$mode" == taylor* ]] && grep -Eq 'PASS_TAYLOR|(^|[^A-Z_])(UNIT|LIFT|EMPTY)([^A-Z_]|$)' "$stdout"; then
  printf 'validator=FAIL_FORBIDDEN_TAYLOR_PROMOTION\n' >> "$validation"
  exit 90
fi
sha256sum "$aws_job"/compiled/* > "$aws_job/compiled.sha256"
printf 'validator=PASS_%s\n' "$mode" >> "$validation"
