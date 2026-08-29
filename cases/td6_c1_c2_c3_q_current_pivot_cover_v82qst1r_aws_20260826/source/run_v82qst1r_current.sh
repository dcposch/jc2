#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82QST1R requires Linux" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V82QST1R requires Amazon EC2" >&2
  exit 96
fi
if [[ -z "${AWS_RUN_TAG:-}" || "${AWS_RUN_TAG}" != td6_v82qst1r_current_* ]]; then
  echo "REFUSED: registered V82QST1R tag required" >&2
  exit 95
fi
: "${TD6_Q_EXPONENT:?TD6_Q_EXPONENT required}"
: "${TD6_PIVOT_POLICY:?TD6_PIVOT_POLICY required}"
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
[[ "$TD6_Q_EXPONENT" == 2 || "$TD6_Q_EXPONENT" == 10 ]] || exit 94
[[ "$TD6_PIVOT_POLICY" == reverse || "$TD6_PIVOT_POLICY" == sparse ]] || exit 93
PYTHON=/home/ubuntu/venvs/td6/bin/python3
[[ -x "$PYTHON" ]] || { echo "REFUSED: TD6 venv missing" >&2; exit 92; }
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE.sha256
sha256sum -c V82QST1R_SOURCE.sha256
"$PYTHON" replay_v82qst1r_current.py

