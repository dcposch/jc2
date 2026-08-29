#!/usr/bin/env bash
set -euo pipefail

[[ "$(uname -s)" == Linux ]] || { echo "REFUSED: Linux required" >&2; exit 97; }
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
[[ -n "${AWS_RUN_TAG:-}" && "$AWS_RUN_TAG" == td6_v82qst1c_current_* ]] || exit 95
: "${TD6_Q_EXPONENT:?TD6_Q_EXPONENT required}"
: "${TD6_PIVOT_POLICY:?TD6_PIVOT_POLICY required}"
: "${TD6_PIVOT_SCOPE:?TD6_PIVOT_SCOPE required}"
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
[[ "$TD6_Q_EXPONENT" == 2 || "$TD6_Q_EXPONENT" == 10 ]] || exit 94
[[ "$TD6_PIVOT_POLICY" == reverse ]] || exit 93
[[ "$TD6_PIVOT_SCOPE" == current-only ]] || exit 91
PYTHON=/home/ubuntu/venvs/td6/bin/python3
[[ -x "$PYTHON" ]] || exit 92
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE.sha256
sha256sum -c V82QST1C_SOURCE.sha256
sha256sum -c NESTED_IDENTITY_REVIEW_PINS.sha256
"$PYTHON" replay_v82qst1s_current.py
