#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82QST0 requires Linux" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V82QST0 requires Amazon EC2" >&2
  exit 96
fi
if [[ -z "${AWS_RUN_TAG:-}" || "${AWS_RUN_TAG}" != td6_v82qst0_current_* ]]; then
  echo "REFUSED: registered V82QST0 tag required" >&2
  exit 95
fi
: "${TD6_Q_EXPONENT:?TD6_Q_EXPONENT required}"
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
case ",2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24," in
  *",${TD6_Q_EXPONENT},"*) ;;
  *) echo "REFUSED: unlicensed q exponent ${TD6_Q_EXPONENT}" >&2; exit 94 ;;
esac
PYTHON=/home/ubuntu/venvs/td6/bin/python3
[[ -x "$PYTHON" ]] || { echo "REFUSED: TD6 venv missing" >&2; exit 93; }
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE.sha256
sha256sum -c V82QST0_SOURCE.sha256
"$PYTHON" replay_v82qsd_current.py
