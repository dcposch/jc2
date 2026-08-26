#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
aws_root=$1
aws_job=$2
tag=$3
cap_kib=$4
config=$5
freeze=$6
case "$config" in
  A65521) characteristic=65521; loads=2,3,5,7,11,13 ;;
  B32003) characteristic=32003; loads=17,19,23,29,31,37 ;;
  C32003) characteristic=32003; loads=41,43,47,53,59,61 ;;
  C65521) characteristic=65521; loads=41,43,47,53,59,61 ;;
  *) exit 125 ;;
esac
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=3600\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'config=%s\n' "$config"
  printf 'characteristic=%s\n' "$characteristic"
  printf 'loads=%s\n' "$loads"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
python3 cases/max12_812_order2_invariant_quotient_probe_20260826/compile_probe_crosscontrols.py \
  "$aws_job/compiled" --config "$config" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input="$aws_job/compiled/order2_invariant_quotient_p${characteristic}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
exec bash cases/max12_812_order2_invariant_quotient_probe_20260826/run_probe_aws.sh \
  "$aws_root" "$aws_job/run" "$tag" "$input" "$cap_kib"
