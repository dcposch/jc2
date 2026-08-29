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
sha256sum -c cases/max12_812_order2_p0_odd_sheet_receivers_20260826/FREEZE_G14_EXACT.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "${tag}_python" \
  timeout "$wall" python3 \
  cases/max12_812_order2_p0_odd_sheet_receivers_20260826/reduce_grade14_exact.py \
  "$aws_job/compiled"
python_rc=$?
set -e
python_stdout="$aws_job/run/${tag}_python.stdout"
validation="$aws_job/run/$tag.validation"
printf 'python_rc=%s\n' "$python_rc" > "$validation"
if [[ "$python_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_PYTHON_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$python_rc" -ne 0 ]]; then printf 'validator=FAIL_PYTHON_ENGINE\n' >> "$validation"; exit "$python_rc"; fi
for required in \
  P0_ODD_G14_EXACT_SOURCE_HASHES=PASS \
  P0_ODD_G14_GRADE13_REDUCTION=PASS \
  P0_ODD_G14_EXACT_STATUS=PASS_LAURENT_REDUCTION
do
  if [[ "$(grep -Fxc "$required" "$python_stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"
    exit 90
  fi
done
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "${tag}_singular" \
  timeout "$wall" Singular -q "$aws_job/compiled/grade14_factor.sing"
singular_rc=$?
set -e
singular_stdout="$aws_job/run/${tag}_singular.stdout"
printf 'singular_rc=%s\n' "$singular_rc" >> "$validation"
if [[ "$singular_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_SINGULAR_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$singular_rc" -ne 0 ]]; then printf 'validator=FAIL_SINGULAR_ENGINE\n' >> "$validation"; exit "$singular_rc"; fi
for required in P0_ODD_G14_EXACT_SINGULAR_SOURCE=PASS P0_ODD_G14_EXACT_SINGULAR_DONE=PASS
do
  if [[ "$(grep -Fxc "$required" "$singular_stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"
    exit 91
  fi
done
sha256sum "$aws_job"/compiled/* > "$aws_job/compiled.sha256"
printf 'validator=PASS_G14_EXACT_NAVIGATION\n' >> "$validation"

