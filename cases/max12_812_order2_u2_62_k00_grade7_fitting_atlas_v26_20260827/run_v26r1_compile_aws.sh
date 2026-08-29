#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V26R1 compiler runner refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: $0 AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS FREEZE MODE" >&2
  exit 125
fi
k00_aws_root=$1
k00_aws_job=$2
k00_lane_tag=$3
k00_cap_kib=$4
k00_timeout_seconds=$5
k00_freeze=$6
k00_mode=$7
k00_rel=cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827

if [[ "$k00_mode" != "held" ]]; then
  echo "V26R1 streaming repair is held-compile only" >&2
  exit 125
fi
mkdir -p "$k00_aws_job/run"
{
  printf 'tag=%s\n' "$k00_lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact_source_compilation\n'
  printf 'virtual_memory_cap_kib=%s\n' "$k00_cap_kib"
  printf 'timeout_seconds=%s\n' "$k00_timeout_seconds"
  printf 'mode=held_streaming_parser_repair\n'
  printf 'design=v26_unchanged_compiler_plus_streaming_flat_sum_adapter\n'
  printf 'scope=compiler_only_no_stratum_no_jet_no_arc_no_closure_no_JC2\n'
} > "$k00_aws_job/launch_registration.txt"
cd "$k00_aws_root"
sha256sum -c "$k00_freeze" > "$k00_aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$k00_lane_tag"
export OMP_NUM_THREADS=1
ulimit -v "$k00_cap_kib"
set +e
/usr/bin/time -v timeout "$k00_timeout_seconds" \
  python3 "$k00_rel/compile_fitting_atlas_v26r1_streaming.py" \
  "$k00_aws_job/output" --compile-held \
  > "$k00_aws_job/run/compiler.stdout" 2> "$k00_aws_job/run/compiler.stderr"
k00_rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$k00_rc"
} >> "$k00_aws_job/launch_registration.txt"
printf 'engine_rc=%s\n' "$k00_rc" > "$k00_aws_job/run/FINAL.validation"
if [[ "$k00_rc" -ne 0 ]]; then
  exit "$k00_rc"
fi
grep -q '^K00_V26_COMPILER=PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION$' \
  "$k00_aws_job/run/compiler.stdout"
k00_status=$(python3 -c \
  'import json,sys; print(json.load(open(sys.argv[1]))["status"])' \
  "$k00_aws_job/output/RESULT.json")
printf 'validator=%s\n' "$k00_status" >> "$k00_aws_job/run/FINAL.validation"
find "$k00_aws_job/output" "$k00_aws_job/run" \
  "$k00_aws_job/freeze_check.stdout" "$k00_aws_job/launch_registration.txt" \
  -type f ! -name EVIDENCE.sha256 -print0 | sort -z | \
  xargs -0 sha256sum > "$k00_aws_job/EVIDENCE.sha256"
