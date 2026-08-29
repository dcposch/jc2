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
characteristic=$5
compile_timeout=$6
engine_timeout=$7
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"
  printf 'compile_timeout_seconds=%s\n' "$compile_timeout"
  printf 'engine_timeout_seconds=%s\n' "$engine_timeout"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_disc_halfweight_kuranishi_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 \
  cases/max12_812_order2_disc_halfweight_kuranishi_20260826/compile_disc_halfweight.py \
  "$aws_job/compiled" --characteristic "$characteristic" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
input="$aws_job/compiled/disc_halfweight_p${characteristic}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" \
  timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/$tag.stdout"
validation="$aws_job/run/$tag.validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi
for required in \
  'DISC_HALF_SOURCE_HASHES=PASS' \
  'DISC_HALF_RHO6_DIVISIBLE=1' \
  'DISC_HALF_DIVISION_IDENTITY=1' \
  'DISC_HALF_FORBIDDEN_INDEPENDENCE=1' \
  'DISC_HALF_REC13_ZERO=1' \
  'DISC_HALF_REC14_ZERO=1' \
  'DISC_HALF_RANK_BOUND=3' \
  'DISC_HALF_ANALYTIC_IN_SOURCE=1' \
  'DISC_HALF_SOURCE_IN_ANALYTIC=1' \
  'DISC_HALF_MATCHED_ENDPOINT_UNIT=1' \
  'DISC_HALF_ENDPOINT=PASS_SOURCE_ANALYTIC_IDEAL_EQUALITY'
do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"
    exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Eq '^\? ' "$stdout"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"
  exit 90
fi
printf 'validator=PASS_DISC_HALFWEIGHT_SOURCE_CERTIFICATE\n' >> "$validation"
