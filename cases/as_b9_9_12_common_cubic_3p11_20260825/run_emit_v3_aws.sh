#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${PATCHED_SOURCE_OUTPUT:?}"
python3 "$JC2_ROOT/cases/as_b9_9_12_common_cubic_3p11_20260825/emit_common_cubic_v3.py"
