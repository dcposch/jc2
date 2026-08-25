#!/usr/bin/env bash
set -euo pipefail
: "${MATRIX_JSON:?}"
: "${OUTPUT_JSON:?}"
: "${PYTHON:?}"
/usr/bin/time -v timeout 3600 "${PYTHON}" \
  "$(dirname "$0")/compute_snf_flint.py"
