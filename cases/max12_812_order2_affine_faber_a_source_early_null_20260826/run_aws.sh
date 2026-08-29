#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6; singular_bin=$7
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"; printf 'characteristic=%s\n' "$characteristic"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"; printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_source_early_null_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
compiled="$aws_job/compiled"
python3 cases/max12_812_order2_affine_faber_a_source_early_null_20260826/compile_source_early_null.py "$compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input=$(find "$compiled" -maxdepth 1 -name '*.sing' -type f -print -quit)
set +e
/usr/bin/time -v timeout "$timeout_seconds" "$singular_bin" -q "$input" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En '\?|// \*\*|error occurred' "$aws_job/compiler.stdout" "$aws_job/compiler.stderr" "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1
then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_SOURCE_TCOEFF_CONTROL=1' 'A_SOURCE_CORRECTED_LOWER_ZERO=1' 'A_SOURCE_CORRECTED_R1_CONTROL=1' 'A_SOURCE_CORRECTED_T7_CANCEL=1' 'A_SOURCE_MONOMIAL_SLICE_CONTROL=1' 'A_SOURCE_NATURAL_CONTROL=1' 'A_SOURCE_REPEATED_CUBIC_CONTROL=1' 'A_SOURCE_ENDPOINT=PASS_CORRECTION_COMPLETE_T7_CANCELLATION_AND_CUBIC_IDENTITIES' 'A_SOURCE_DONE=1' 'A_SOURCE_SCOPE=DELAYED_LOAD_A_FACE_SOURCE_TRIAGE_NO_TOTAL_REES_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT'; do
  if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_SOURCE_EARLY_NULL\n' >> "$aws_job/run/$tag.validation"
