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
sha256sum -c cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
compiled="$aws_job/compiled"
set +e
python3 cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/compile_generic_j_exclusion.py \
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
  'GENERIC_J_COORDINATE_ISOMORPHISM=1' \
  'GENERIC_J_PARITY_ALL=1' \
  'GENERIC_J_AFFINE_GRAPH_ROWS=1' \
  'GENERIC_J_JACOBIAN_FORMULAS=1' \
  'GENERIC_J_DETERMINANT_OK=1' \
  'GENERIC_J_A_FACE_RANK2_AND_R7_KERNEL_NULL=1' \
  'GENERIC_J_K_FACE_RANK1_AND_R7_KERNEL_NULL=1' \
  'GENERIC_J_RAW_CUBIC=1' \
  'GENERIC_J_RAW_QUINTIC=1' \
  'GENERIC_J_ENDPOINT=PASS_GENERIC_PARITY_IFT_DATA_AND_EXCEPTIONAL_FIRST_ORDER_NULLITY' \
  'GENERIC_J_DONE=1' \
  'GENERIC_J_SCOPE=NORMALIZED_ORDINARY_FABER_FACE_ONLY_GATE_A_TOTAL_REES_EXCEPTIONAL_FANS_TERMINAL_TAYLOR_ORDER2_AND_JC2_OPEN'
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
printf 'validator=PASS_GENERIC_J_EXCLUSION_DATA\n' >> "$aws_job/run/$tag.validation"

