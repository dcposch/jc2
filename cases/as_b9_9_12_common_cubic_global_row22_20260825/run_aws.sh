#!/usr/bin/env bash
set -euo pipefail
test "$(uname -s)" = Linux || {
  echo "AWS-only runner refuses non-Linux host" >&2
  exit 97
}
: "${AWS_JOB_TAG:?}"
case "$AWS_JOB_TAG" in
  as_b9_common_cubic_global_row22_*) ;;
  *) echo "unregistered AWS job tag: $AWS_JOB_TAG" >&2; exit 98 ;;
esac
: "${INDEPENDENT_PARENT_SOURCE:?}"
: "${PARENT_AUDIT_RESULT:?}"
: "${LINEAR_REPLAY_JSON:?}"
: "${PARENT_REPLAY_JSON:?}"
: "${ANF_OUTPUT:?}"
: "${PARENT_WITNESS_OUTPUT:?}"
: "${OUTPUT_JSON:?}"
: "${WITNESS_OUTPUT:?}"
: "${POINTS_GZIP:?}"
python3 "$(dirname "$0")/global_row22.py"
