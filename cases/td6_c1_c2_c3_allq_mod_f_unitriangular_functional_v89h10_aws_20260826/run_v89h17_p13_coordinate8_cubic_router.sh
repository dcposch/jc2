#!/usr/bin/env bash
set -euo pipefail

case "${AWS_RUN_TAG:-}" in
  td6_v89h17_p13_cubic_*) ;;
  *) echo "missing/invalid AWS_RUN_TAG" >&2; exit 2 ;;
esac
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"

python3 replay_v89h17_p13_coordinate8_cubic_router.py
