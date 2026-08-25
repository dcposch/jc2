#!/usr/bin/env bash
set -euo pipefail

# This is intentionally a portable source replay, not a local-compute
# recommendation.  Campaign policy currently requires substantive runs on AWS.
: "${MODEL_OUTPUT:?path to the pinned Q5 Boolector model is required}"
: "${OUTPUT_DIR:?output directory is required}"

case_dir=$(cd "$(dirname "$0")" && pwd)
jc2_root=$(cd "$case_dir/../.." && pwd)
mkdir -p "$OUTPUT_DIR"
env \
  JC2_ROOT="$jc2_root" \
  MODEL_OUTPUT="$MODEL_OUTPUT" \
  PARENT_OUTPUT_JSON="$OUTPUT_DIR/parent_q5_replay.json" \
  OUTPUT_JSON="$OUTPUT_DIR/q4_affine_certificate.json" \
  python3 "$case_dir/analyze_pinned_q4_affine.py" \
  > "$OUTPUT_DIR/replay.stdout" \
  2> "$OUTPUT_DIR/replay.stderr"
sha256sum "$OUTPUT_DIR"/* > "$OUTPUT_DIR/OUTPUT.sha256"

