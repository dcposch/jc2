#!/usr/bin/env bash
set -euo pipefail

: "${AWS_RUN_TAG:?AWS_RUN_TAG is required}"
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"
: "${TD6_PRIME:?TD6_PRIME is required}"
: "${TD6_U:?TD6_U is required}"
: "${TD6_V:?TD6_V is required}"

case "$AWS_RUN_TAG" in
  td6_v89h13_p12_maxminor_*) ;;
  *) echo "refusing non-AWS or misregistered tag" >&2; exit 97 ;;
esac

exec python3 replay_v89h13_p12_maximal_minor_pilot.py
