#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${OUTPUT_JSON:?}"
SOURCE="$JC2_ROOT/cases/as_fonly_d7_global_q5_h6_replay_erratum_20260825"

/usr/bin/time -v env \
  JC2_ROOT="$JC2_ROOT" \
  MODEL_OUTPUT="$MODEL_OUTPUT" \
  OUTPUT_JSON="$OUTPUT_JSON" \
  ALLOW_OMITTED_Q5_GATE="${ALLOW_OMITTED_Q5_GATE:-0}" \
  python3 "$SOURCE/replay_global_q5_h6_v2.py"
