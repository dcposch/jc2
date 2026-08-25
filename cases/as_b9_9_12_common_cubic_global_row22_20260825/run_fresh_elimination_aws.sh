#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing non-Linux execution" >&2
  exit 97
fi
: "${AWS_JOB_TAG:?AWS_JOB_TAG is required}"
case "$AWS_JOB_TAG" in
  as_b9_common_cubic_fresh_elim_*) ;;
  *) echo "unregistered AWS job tag: $AWS_JOB_TAG" >&2; exit 98 ;;
esac
: "${SHARD_COUNT:?SHARD_COUNT is required}"
: "${SHARD_INDEX:?SHARD_INDEX is required}"
: "${JOB_ROOT:?JOB_ROOT is required}"

python_source="$JOB_ROOT/fresh_elimination.py"
global_source="$JOB_ROOT/global_row22_v1.py"
parent_source="$JOB_ROOT/independent_common_core.py"

[[ "$(sha256sum "$python_source" | awk '{print $1}')" == \
  "8951a907473f7195398e0f3c7f915e0867a4784a97a317d54be924544cbea713" ]]
[[ "$(sha256sum "$global_source" | awk '{print $1}')" == \
  "b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f" ]]
[[ "$(sha256sum "$parent_source" | awk '{print $1}')" == \
  "460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8" ]]

export GLOBAL_V1_SOURCE="$global_source"
export INDEPENDENT_PARENT_SOURCE="$parent_source"
export JC2_ROOT="$JOB_ROOT/parent_source"
export PARENT_AUDIT_RESULT="$JOB_ROOT/parent_audit_result.json"
export LINEAR_REPLAY_JSON="$JOB_ROOT/linear_replay.json"
export PARENT_REPLAY_JSON="$JOB_ROOT/parent_replay.json"
export ANF_OUTPUT="$JOB_ROOT/parent.anf.json"
export PARENT_WITNESS_OUTPUT="$JOB_ROOT/parent_witness.json"
export GLOBAL_V1_RESULT="$JOB_ROOT/v1_result.json"
export GLOBAL_V1_WITNESS="$JOB_ROOT/v1_witness.json"
export POINTS_GZIP="$JOB_ROOT/v1_points.json.gz"
export OUTPUT_JSON="$JOB_ROOT/result_${SHARD_INDEX}.json"
export WITNESS_OUTPUT="$JOB_ROOT/witness_${SHARD_INDEX}.json"
export RECORDS_GZIP="$JOB_ROOT/records_${SHARD_INDEX}.json.gz"

exec /usr/bin/time -v python3 "$python_source"
