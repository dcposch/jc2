#!/usr/bin/env bash
set -euo pipefail
: "${WITNESS_JSON:?}"
: "${EXPECTED_WITNESS_SHA256:?}"
: "${OUTPUT_JSON:?}"
: "${MATRIX_GZIP:?}"
python3 "$(dirname "$0")/jacobian_snf.py"
