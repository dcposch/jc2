#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" || $# -ne 5 ]]; then exit 125; fi
aws_root=$1
aws_job=$2
tag=$3
cap_kib=$4
wall=$5
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\npid=%s\nstart_utc=%s\n' \
    "$tag" "$(hostname)" "$$" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'cap_kib=%s\nwall_seconds=%s\njob_dir=%s\n' "$cap_kib" "$wall" "$aws_job"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" \
  timeout "$wall" python3 \
  cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/replay_p0_cusp_grade12_unit.py \
  "$aws_job/compiled"
rc=$?
set -e
stdout="$aws_job/run/$tag.stdout"
validation="$aws_job/run/$tag.validation"
printf 'rc=%s\n' "$rc" > "$validation"
if [[ "$rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit "$rc"; fi
for required in \
  P0_CUSP_G12_SOURCE_HASHES=PASS \
  P0_CUSP_G12_ALL_SEVEN_ROWS=PASS \
  P0_CUSP_G12_G11_PIVOTS=PASS \
  P0_CUSP_G12_RAW_ROW6_UNIT=PASS \
  P0_CUSP_G12_FOCUSED_FOUR_TAILS=PASS \
  P0_CUSP_G12_STATUS=PASS_INDEPENDENT_EXACT_REPLAY
do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"
    exit 90
  fi
done
sha256sum "$aws_job"/compiled/* > "$aws_job/compiled.sha256"
printf 'validator=PASS_P0_CUSP_GRADE12_UNIT_REPLAY\n' >> "$validation"
