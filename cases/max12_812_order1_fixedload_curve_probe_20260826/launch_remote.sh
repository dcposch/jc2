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
config=$5
compile_timeout=$6
engine_timeout=$7
case "$config" in
  A) characteristic=32003 ;;
  B) characteristic=65521 ;;
  *) exit 125 ;;
esac
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'compile_timeout_seconds=%s\n' "$compile_timeout"
  printf 'engine_timeout_seconds=%s\n' "$engine_timeout"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'config=%s\n' "$config"
  printf 'characteristic=%s\n' "$characteristic"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order1_fixedload_curve_probe_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 \
  cases/max12_812_order1_fixedload_curve_probe_20260826/compile_order1_probe.py \
  "$aws_job/compiled" --config "$config" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
input="$aws_job/compiled/order1_fixedload_${config}_p${characteristic}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
exec bash cases/max12_812_order1_fixedload_curve_probe_20260826/run_probe_aws.sh \
  "$aws_root" "$aws_job/run" "$tag" "$input" "$cap_kib" "$engine_timeout"
