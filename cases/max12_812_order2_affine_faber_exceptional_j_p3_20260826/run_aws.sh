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
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"

cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_exceptional_j_p3_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
compiled="$aws_job/compiled"
set +e
python3 cases/max12_812_order2_affine_faber_exceptional_j_p3_20260826/compile_exceptional_p3.py \
  "$compiled" --characteristic "$characteristic" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi

for input in "$compiled"/*.sing; do
  name=$(basename "$input" .sing)
  set +e
  /usr/bin/time -v timeout "$timeout_seconds" "$singular_bin" -q "$input" \
    > "$aws_job/run/$name.stdout" 2> "$aws_job/run/$name.stderr"
  engine_rc=$?
  set -e
  printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$name.validation"
  if [[ "$engine_rc" -ne 0 ]]; then
    printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$name.validation"
    exit "$engine_rc"
  fi
  if grep -En '\?|// \*\*|error occurred' \
    "$aws_job/run/$name.stdout" "$aws_job/run/$name.stderr" >/dev/null 2>&1
  then
    printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$name.validation"
    exit 91
  fi
  case "$name" in
    exceptional_controls_*) required='EXCEPTIONAL_P3_CONTROLS_DONE=1' ;;
    exceptional_A_*) required='EXCEPTIONAL_P3_A_DONE=1' ;;
    exceptional_K_*) required='EXCEPTIONAL_P3_K_DONE=1' ;;
    *) exit 92 ;;
  esac
  if [[ "$(grep -Fxc "$required" "$aws_job/run/$name.stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$name.validation"
    exit 93
  fi
  printf 'validator=PASS_EXCEPTIONAL_P3_SHARD\n' >> "$aws_job/run/$name.validation"
done
printf 'validator=PASS_EXCEPTIONAL_P3_ALL\n' > "$aws_job/run/$tag.validation"
