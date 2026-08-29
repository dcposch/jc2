#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi

aws_root=$1
aws_job=$2
tag=$3
characteristic=$4
cap_kib=$5
timeout_seconds=$6
singular_bin=$7
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'singular=%s\n' "$singular_bin"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"

cd "$aws_root"
sha256sum -c cases/max12_812_order2_exact_square_affine_mu2_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
compiled="$aws_job/compiled"
set +e
python3 cases/max12_812_order2_exact_square_affine_mu2_20260826/compile_affine_mu2.py \
  "$compiled" --characteristic "$characteristic" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/run/$tag.validation"
if [[ "$compiler_rc" -ne 0 ]]; then
  printf 'validator=FAIL_COMPILER\n' >> "$aws_job/run/$tag.validation"
  exit "$compiler_rc"
fi

input=$(find "$compiled" -maxdepth 1 -name '*.sing' -type f -print -quit)
if [[ -z "$input" ]]; then
  printf 'validator=FAIL_NO_INPUT\n' >> "$aws_job/run/$tag.validation"
  exit 89
fi
set +e
/usr/bin/time -v timeout "$timeout_seconds" "$singular_bin" -q "$input" \
  > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" >> "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"
  exit "$engine_rc"
fi

for required in \
  'AFFINE_MU2_PROBE_DONE=1' \
  'AFFINE_MU2_SCOPE=EXACT_SQUARE_AFFINE_TARGET_SUPPORT_ONLY_NO_REES_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT'
do
  if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"
    exit 90
  fi
done
if grep -En '\?|// \*\*|error occurred' \
  "$aws_job/compiler.stdout" "$aws_job/compiler.stderr" \
  "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1
then
  printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"
  exit 91
fi
printf 'validator=PASS_AFFINE_MU2_PROBE\n' >> "$aws_job/run/$tag.validation"

