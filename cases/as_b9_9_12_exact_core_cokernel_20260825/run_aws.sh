#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${OUTPUT_JSON:?}"
: "${PARENT_REPLAY_JSON:?}"
: "${BASES_JSON:?}"
: "${PROJECTED_GZIP:?}"
python3 "$JC2_ROOT/cases/as_b9_9_12_exact_core_cokernel_20260825/exact_core_cokernel.py"
