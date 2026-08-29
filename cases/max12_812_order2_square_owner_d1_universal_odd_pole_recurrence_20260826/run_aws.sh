#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6; max_terminal=$7
case "$tag" in max12_812_order2_square_d1_odd_pole_recurrence_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65521) ;; *) exit 125 ;; esac
mkdir -p "$aws_job"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
inventory=cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/aws_q_box03/compiled/source_inventory.json
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'pid=%s\n' "$$"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"; printf 'max_terminal=%s\n' "$max_terminal"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"; printf 'timeout_seconds=%s\n' "$timeout_seconds"
} > "$aws_job/launch_registration.txt"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 \
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/odd_pole_recurrence_miner.py \
  "$aws_job/compiled" --characteristic "$characteristic" --max-terminal "$max_terminal" \
  --inventory "$inventory" --inventory-max-grade 38 --inventory-max-pole 3 \
  > "$aws_job/stdout" 2> "$aws_job/stderr"
rc=$?
set -e
printf 'rc=%s\n' "$rc" > "$aws_job/rc"
if [[ "$rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' > "$aws_job/validation"; exit 124; fi
if [[ "$rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' > "$aws_job/validation"; exit 90; fi
for required in \
  'ODDREC_LAURENT_TO_FABER_TRANSFORM=PASS' \
  'ODDREC_ALL_POLES_Q_LE_R=PASS' \
  'ODDREC_FIRST_OUTSIDE_POLE_NEGATIVE_CONTROLS=PASS' \
  'ODDREC_TERMINAL_POLE_NEGATIVE_CONTROLS=PASS' \
  'ODDREC_ROW7_R2_S_SCALARS=1,-1/2,-1/8,-1/16' \
  'ODDREC_ROW7_R3_S_SCALARS=1,1/2,3/8,5/16' \
  'ODDREC_COMPLETE_INVENTORY_POLE_CEILING=PASS' \
  'ODDREC_ENDPOINT=PASS_UNIVERSAL_ODD_POLE_RECURRENCE_MINER'; do
  if [[ "$(grep -Fxc "$required" "$aws_job/stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" > "$aws_job/validation"; exit 90
  fi
done
if grep -Fq 'FAIL:' "$aws_job/stdout" || grep -Fq 'FAIL:' "$aws_job/stderr" \
   || grep -Fq 'Traceback' "$aws_job/stderr"; then
  printf 'validator=FAIL_DIAGNOSTIC\n' > "$aws_job/validation"; exit 90
fi
printf 'validator=PASS_UNIVERSAL_ODD_POLE_RECURRENCE_MINER\n' > "$aws_job/validation"
sha256sum "$aws_job/compiled/result.json" "$aws_job/stdout" "$aws_job/stderr" > "$aws_job/results.sha256"
printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$aws_job/launch_registration.txt"
