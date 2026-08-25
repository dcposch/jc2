#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${FROZEN_RESULT_JSON:?}"
: "${PARENT_OUTPUT_JSON:?}"
: "${OUTPUT_JSON:?}"
: "${MATRIX_JSON:?}"
python3 "${JC2_ROOT}/cases/as_fonly_d7_q3_mod243_jacobian_kuranishi_20260825/analyze_jacobian_kuranishi.py"
