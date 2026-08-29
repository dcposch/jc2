#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V26 exact worker runner refused host" >&2
  exit 125
fi
if [[ $# -ne 9 ]]; then
  echo "usage: $0 AWS_ROOT AWS_JOB TAG CAP_KIB OUTER_TIMEOUT INNER_TIMEOUT FREEZE COMPILED_DIR JOB_ID" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
outer_timeout=$5
inner_timeout=$6
freeze=$7
compiled=$8
job_id=$9
rel=cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827

if [[ "$compiled" != /* ]]; then
  compiled="$aws_root/$compiled"
fi
if [[ ! -f "$compiled/RELEASE_V24R2_EXACT.json" ]]; then
  echo "V26 worker dependency hold: RELEASE_V24R2_EXACT.json missing" >&2
  exit 126
fi
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'outer_timeout_seconds=%s\n' "$outer_timeout"
  printf 'inner_timeout_seconds=%s\n' "$inner_timeout"
  printf 'job_id=%s\n' "$job_id"
  printf 'design=v26_one_exact_prepass_agreement_or_rank_minor_chart\n'
  printf 'scope=no_aggregation_no_later_grade_no_jet_no_arc_no_closure_no_JC2\n'
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$outer_timeout" \
  python3 "$rel/run_v26_exact_worker.py" "$compiled" "$job_id" "$aws_job/output" --timeout "$inner_timeout" \
  > "$aws_job/run/worker.stdout" 2> "$aws_job/run/worker.stderr"
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
} >> "$aws_job/launch_registration.txt"
printf 'engine_rc=%s\n' "$rc" > "$aws_job/run/FINAL.validation"
if [[ "$rc" -ne 0 ]]; then
  exit "$rc"
fi
grep -q '^K00_V26_WORKER=' "$aws_job/run/worker.stdout"
status=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["status"])' "$aws_job/output/RESULT.json")
printf 'validator=%s\n' "$status" >> "$aws_job/run/FINAL.validation"
find "$aws_job/output" "$aws_job/run" "$aws_job/freeze_check.stdout" \
  "$aws_job/launch_registration.txt" -type f -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/EVIDENCE.sha256.tmp"
mv "$aws_job/EVIDENCE.sha256.tmp" "$aws_job/EVIDENCE.sha256"
