#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V84S is AWS/Linux only" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V84S requires Amazon EC2" >&2
  exit 96
fi
if [[ -z "${AWS_RUN_TAG:-}" || "${AWS_RUN_TAG}" != td6_v84r2_k2_spencer_reverse_* ]]; then
  echo "REFUSED: registered V84S run tag required" >&2
  exit 95
fi
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
export TD6_K2_BLOCK_A=0
export TD6_K2_BLOCK_B=0

PYTHON=/home/ubuntu/venvs/td6/bin/python3
if [[ ! -x "$PYTHON" ]]; then
  echo "REFUSED: registered TD6 Python environment missing" >&2
  exit 94
fi
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c V84S_SOURCE.sha256
"$PYTHON" replay_v84s_reverse.py
