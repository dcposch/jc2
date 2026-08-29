#!/usr/bin/env bash
set -euo pipefail

: "${AWS_RUN_TAG:?AWS_RUN_TAG is required}"
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"
case "$AWS_RUN_TAG" in
  td6_v89h14_p12_two_row_*) ;;
  *) echo "refusing non-AWS or misregistered tag" >&2; exit 97 ;;
esac
exec python3 replay_v89h14_p12_two_row_scalar_split.py
