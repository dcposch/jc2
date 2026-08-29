#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V26 compiler runner refused host" >&2
  exit 125
fi
if [[ $# -ne 8 ]]; then
  echo "usage: $0 AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS FREEZE MODE V24R2_RESULT_OR_DASH" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
freeze=$6
mode=$7
v24r2=$8
rel=cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827

case "$mode" in
  held)
    compiler_args=(--compile-held)
    if [[ "$v24r2" != "-" ]]; then
      echo "held mode requires V24R2_RESULT_OR_DASH=-" >&2
      exit 125
    fi
    ;;
  released)
    if [[ "$v24r2" != /* ]]; then
      v24r2="$aws_root/$v24r2"
    fi
    if [[ "$v24r2" == "-" ]] || [[ ! -f "$v24r2" ]]; then
      echo "released mode requires an exact-Q V24R2 result path" >&2
      exit 125
    fi
    compiler_args=(--v24r2-endpoint "$v24r2")
    ;;
  *)
    echo "MODE must be held or released" >&2
    exit 125
    ;;
esac

mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact_source_compilation\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'mode=%s\n' "$mode"
  printf 'design=v26_direct_V20R2_DAG_representation_independent_Fitting_atlas\n'
  printf 'scope=compiler_only_no_stratum_no_jet_no_arc_no_closure_no_JC2\n'
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" \
  python3 "$rel/compile_fitting_atlas_v26.py" "$aws_job/output" "${compiler_args[@]}" \
  > "$aws_job/run/compiler.stdout" 2> "$aws_job/run/compiler.stderr"
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
grep -q '^K00_V26_COMPILER=PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION$' "$aws_job/run/compiler.stdout"
status=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["status"])' "$aws_job/output/RESULT.json")
printf 'validator=%s\n' "$status" >> "$aws_job/run/FINAL.validation"
find "$aws_job/output" "$aws_job/run" "$aws_job/freeze_check.stdout" \
  "$aws_job/launch_registration.txt" -type f -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/EVIDENCE.sha256.tmp"
mv "$aws_job/EVIDENCE.sha256.tmp" "$aws_job/EVIDENCE.sha256"
