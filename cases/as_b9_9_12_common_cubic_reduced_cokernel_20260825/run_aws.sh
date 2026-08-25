#!/usr/bin/env bash
set -euo pipefail
: "${PYTHON:?}"
: "${MATRIX_GZIP:?}"
: "${WITNESS_JSON:?}"
: "${EXPECTED_MATRIX_GZIP_SHA256:?}"
: "${EXPECTED_WITNESS_SHA256:?}"
: "${OUTPUT_JSON:?}"
: "${BASIS_GZIP:?}"
"$PYTHON" "$(dirname "$0")/reduced_cokernel.py"
