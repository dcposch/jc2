#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V84 is AWS/Linux only" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V84 requires Amazon EC2" >&2
  exit 96
fi
if [[ -z "${AWS_RUN_TAG:-}" || "${AWS_RUN_TAG}" != td6_v84_k2_* ]]; then
  echo "REFUSED: registered td6_v84_k2_ tag required" >&2
  exit 95
fi
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
: "${TD6_K2_BLOCK_A:?TD6_K2_BLOCK_A required}"
: "${TD6_K2_BLOCK_B:?TD6_K2_BLOCK_B required}"

PYTHON=/home/ubuntu/venvs/td6/bin/python3
if [[ ! -x "$PYTHON" ]]; then
  echo "REFUSED: registered TD6 Python environment missing" >&2
  exit 94
fi
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c V84_SOURCE.sha256
"$PYTHON" \
  payload/jc2/cases/td6_c1_c2_c3_qdead_previous_pole_k2_shard_v84_20260826/replay.py

