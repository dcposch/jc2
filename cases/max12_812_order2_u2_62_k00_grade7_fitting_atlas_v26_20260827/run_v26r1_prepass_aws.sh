#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V26R1 exact prepass runner refused host" >&2
  exit 125
fi
if [[ $# -ne 9 ]]; then
  echo "usage: $0 AWS_ROOT AWS_JOB TAG CAP_KIB OUTER_TIMEOUT INNER_TIMEOUT FREEZE COMPILED_DIR RELEASE_DIR" >&2
  exit 125
fi
k00_aws_root=$1
k00_aws_job=$2
k00_lane_tag=$3
k00_cap_kib=$4
k00_outer_timeout=$5
k00_inner_timeout=$6
k00_freeze=$7
k00_compiled=$8
k00_release=$9
k00_rel=cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827

if [[ "$k00_compiled" != /* ]]; then
  k00_compiled="$k00_aws_root/$k00_compiled"
fi
if [[ "$k00_release" != /* ]]; then
  k00_release="$k00_aws_root/$k00_release"
fi
if [[ ! -f "$k00_compiled/RESULT.json" ]] || \
   [[ ! -f "$k00_release/RELEASE_V26R1_W0.json" ]]; then
  echo "V26R1 compiled/release gate missing" >&2
  exit 126
fi
mkdir -p "$k00_aws_job/run"
{
  printf 'tag=%s\n' "$k00_lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact\n'
  printf 'workers=1\n'
  printf 'virtual_memory_cap_kib=%s\n' "$k00_cap_kib"
  printf 'outer_timeout_seconds=%s\n' "$k00_outer_timeout"
  printf 'inner_timeout_seconds=%s\n' "$k00_inner_timeout"
  printf 'design=v26r1_exact_six_variable_B_plus_I5A_rank_prepass\n'
  printf 'dependency=V24R6R1_internal_Sol_audit_PASS_Opus5_cross_audit_PENDING\n'
  printf 'rollback_tag=PROVISIONAL_ROLLBACK_TAG_OPUS5_PENDING\n'
  printf 'promotion=FORBIDDEN_UNTIL_OPUS5_CROSS_AUDIT_PASS_AND_ADJUDICATION\n'
  printf 'scope=prepass_only_no_grade7_atlas_no_jet_no_arc_no_closure_no_JC2\n'
} > "$k00_aws_job/launch_registration.txt"
cd "$k00_aws_root"
sha256sum -c "$k00_freeze" > "$k00_aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$k00_lane_tag"
export OMP_NUM_THREADS=1
ulimit -v "$k00_cap_kib"
set +e
/usr/bin/time -v timeout "$k00_outer_timeout" \
  python3 "$k00_rel/run_v26r1_exact_prepass.py" \
  "$k00_compiled" "$k00_release" "$k00_aws_job/output" \
  --timeout "$k00_inner_timeout" \
  > "$k00_aws_job/run/prepass.stdout" \
  2> "$k00_aws_job/run/prepass.stderr"
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
grep -q '^K00_V26R1_PREPASS=' "$k00_aws_job/run/prepass.stdout"
k00_status=$(python3 -c \
  'import json,sys; print(json.load(open(sys.argv[1]))["status"])' \
  "$k00_aws_job/output/RESULT.json")
printf 'validator=%s\n' "$k00_status" >> "$k00_aws_job/run/FINAL.validation"
find "$k00_aws_job/output" "$k00_aws_job/run" \
  "$k00_aws_job/freeze_check.stdout" "$k00_aws_job/launch_registration.txt" \
  -type f ! -name EVIDENCE.sha256 -print0 | sort -z | \
  xargs -0 sha256sum > "$k00_aws_job/EVIDENCE.sha256"
