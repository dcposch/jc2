#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing non-Linux execution" >&2
  exit 97
fi
: "${AWS_JOB_TAG:?AWS_JOB_TAG is required}"
case "$AWS_JOB_TAG" in
  as_b9_common_cubic_kuranishi_span_*) ;;
  *) echo "unregistered AWS job tag: $AWS_JOB_TAG" >&2; exit 98 ;;
esac
: "${JOB_ROOT:?JOB_ROOT is required}"

check_sha() {
  local file="$1"
  local expected="$2"
  [[ "$(sha256sum "$file" | awk '{print $1}')" == "$expected" ]]
}

check_sha "$JOB_ROOT/analyze_structural_span.py" \
  "0cbfd304c5a214b2120b024ba322986543d42d4bd09192319b71329d924eb9c3"
check_sha "$JOB_ROOT/emit_kuranishi_map.py" \
  "1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf"
check_sha "$JOB_ROOT/global_row22_v1.py" \
  "b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f"
check_sha "$JOB_ROOT/independent_common_core.py" \
  "460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8"
check_sha "$JOB_ROOT/fresh_block.json.gz" \
  "f7f473c5781f610dd0f96112981e8f3b3c7757467d42b7c465a3dfde5c80e8af"

export EMITTER_SOURCE="$JOB_ROOT/emit_kuranishi_map.py"
export GLOBAL_V1_SOURCE="$JOB_ROOT/global_row22_v1.py"
export FRESH_BLOCK_GZIP="$JOB_ROOT/fresh_block.json.gz"
export INDEPENDENT_PARENT_SOURCE="$JOB_ROOT/independent_common_core.py"
export JC2_ROOT="$JOB_ROOT/parent_source"
export PARENT_AUDIT_RESULT="$JOB_ROOT/parent_audit_result.json"
export LINEAR_REPLAY_JSON="$JOB_ROOT/linear_replay.json"
export PARENT_REPLAY_JSON="$JOB_ROOT/parent_replay.json"
export ANF_OUTPUT="$JOB_ROOT/parent.anf.json"
export PARENT_WITNESS_OUTPUT="$JOB_ROOT/parent_witness.json"
export GLOBAL_V1_RESULT="$JOB_ROOT/v1_result.json"
export GLOBAL_V1_WITNESS="$JOB_ROOT/v1_witness.json"
export POINTS_GZIP="$JOB_ROOT/v1_points.json.gz"
export WITNESS_OUTPUT="$JOB_ROOT/span_witness.json"
export SMT_OUTPUT="$JOB_ROOT/span_parent.smt2"
export PARENT_EMIT_RESULT="$JOB_ROOT/parent_emit_result.json"
export CERTIFICATE_GZIP="$JOB_ROOT/structural_span_certificate.json.gz"
export OUTPUT_JSON="$JOB_ROOT/result.json"

exec /usr/bin/time -v python3 "$JOB_ROOT/analyze_structural_span.py"
