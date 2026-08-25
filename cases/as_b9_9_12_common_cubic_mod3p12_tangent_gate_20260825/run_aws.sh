#!/usr/bin/env bash
set -euo pipefail
test "$(uname -s)" = Linux || {
  echo "AWS-only runner refuses non-Linux host" >&2
  exit 97
}
: "${AWS_JOB_TAG:?}"
case "$AWS_JOB_TAG" in
  as_b9_common_cubic_mod3p12_*) ;;
  *) echo "unregistered AWS job tag: $AWS_JOB_TAG" >&2; exit 98 ;;
esac
: "${PYTHON:?}"
: "${MATRIX_GZIP:?}"
: "${WITNESS_JSON:?}"
: "${EXPECTED_MATRIX_GZIP_SHA256:?}"
: "${EXPECTED_WITNESS_SHA256:?}"
: "${OUTPUT_JSON:?}"
: "${CERTIFICATE_GZIP:?}"
"$PYTHON" "$(dirname "$0")/mod3p12_gate.py"
