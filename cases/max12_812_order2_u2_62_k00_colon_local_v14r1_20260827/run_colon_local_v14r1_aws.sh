#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V14R1 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: run_colon_local_v14r1_aws.sh AWS_ROOT AWS_JOB TAG FIELD CAP_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
field=$4
cap_kib=$5
timeout_seconds=$6
freeze=$7
if [[ "$field" != "Q" && "$field" != "65521" ]]; then
  echo "unsupported V14R1 field" >&2
  exit 125
fi
rel=cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827
v14rel=cases/max12_812_order2_u2_62_k00_colon_local_v14_20260827
v1rel=cases/max12_812_order2_u2_62_k00_closure_incidence_v1_20260827
mkdir -p "$aws_job/run/artifacts" "$aws_job/run/serialized_replay/artifacts"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=%s\n' "$field"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
python3 "$rel/compile_colon_local_v14r1.py" "$aws_job/compiled" --field "$field" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input="$aws_job/compiled/k00_colon_local_v14r1_${field}.sing"
prelude="$aws_job/compiled/serialized_replay_prelude_${field}.sing"
sha256sum "$input" "$prelude" "$aws_job/compiled/compiler_result.json" > "$aws_job/compiled.sha256"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_job/run" "$lane_tag" timeout "$timeout_seconds" \
  bash "$aws_root/$v1rel/run_singular_in_dir.sh" "$aws_job/run/artifacts" "$input"
rc=$?
set -e
printf 'engine_rc=%s\n' "$rc" > "$aws_job/run/FINAL.validation"
if [[ "$rc" -ne 0 ]]; then
  exit "$rc"
fi
python3 "$v14rel/validate_colon_local.py" \
  "$aws_job/run/$lane_tag.stdout" "$aws_job/run/artifacts" \
  "$aws_job/compiled/compiler_result.json" "$aws_job/run/BASE_RESULT.json" \
  > "$aws_job/run/base_validator.stdout" 2> "$aws_job/run/base_validator.stderr"
python3 "$rel/build_serialized_replay.py" "$prelude" "$aws_job/run/artifacts" \
  "$aws_job/run/serialized_replay/replay.sing" "$aws_job/run/serialized_replay/BUILD_RESULT.json" \
  --field "$field" > "$aws_job/run/serialized_replay/builder.stdout" \
  2> "$aws_job/run/serialized_replay/builder.stderr"
set +e
timeout 300 bash "$aws_root/$v1rel/run_singular_in_dir.sh" \
  "$aws_job/run/serialized_replay/artifacts" "$aws_job/run/serialized_replay/replay.sing" \
  > "$aws_job/run/serialized_replay/replay.stdout" \
  2> "$aws_job/run/serialized_replay/replay.stderr"
replay_rc=$?
set -e
printf 'replay_rc=%s\n' "$replay_rc" > "$aws_job/run/serialized_replay/FINAL.validation"
if [[ "$replay_rc" -ne 0 ]]; then
  exit "$replay_rc"
fi
python3 "$rel/validate_colon_local_v14r1.py" \
  "$aws_job/run/$lane_tag.stdout" "$aws_job/run/artifacts" \
  "$aws_job/compiled/compiler_result.json" "$aws_job/run/BASE_RESULT.json" \
  "$aws_job/run/serialized_replay/replay.stdout" "$aws_job/run/serialized_replay/artifacts" \
  "$aws_job/run/serialized_replay/BUILD_RESULT.json" "$aws_job/run/RESULT.json" \
  > "$aws_job/run/validator.stdout" 2> "$aws_job/run/validator.stderr"
printf 'validator=PASS_K00_COLON_LOCAL_V14R1\n' >> "$aws_job/run/FINAL.validation"
sha256sum "$aws_job/run/RESULT.json" "$aws_job/run/BASE_RESULT.json" \
  "$aws_job/run/artifacts/LOCAL_UNIT_WITNESS_R1.txt" \
  "$aws_job/run/artifacts"/COLON_LIFT_*.txt "$aws_job/run/artifacts"/UNIT_MULTIPLIER_*.txt \
  "$aws_job/run/serialized_replay/replay.sing" "$aws_job/run/serialized_replay/replay.stdout" \
  "$aws_job/run/serialized_replay/artifacts/SERIALIZED_IDENTITY_RESIDUAL.txt" \
  "$aws_job/run/serialized_replay/artifacts/SERIALIZED_UNIT_WITNESS.txt" \
  > "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
