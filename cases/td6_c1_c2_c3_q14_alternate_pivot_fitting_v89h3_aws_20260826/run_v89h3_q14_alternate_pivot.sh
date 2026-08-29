#!/usr/bin/env bash
set -euo pipefail

[[ "$(uname -s)" == Linux ]] || { echo "REFUSED: Linux required" >&2; exit 97; }
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
[[ -n "${AWS_RUN_TAG:-}" && "$AWS_RUN_TAG" == td6_v89h3_q14_pivot_* ]] || exit 95
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
[[ "${TD6_Q_SCOPE:-}" == tail-q14-q16-q24 ]] || exit 94
[[ "${TD6_PIVOT_POLICY:-}" == ascending ]] || exit 93
[[ "${TD6_V89H3_PIVOT_POLICY:-}" == registered-single-exchange ]] || exit 90
[[ "${TD6_PIVOT_SCOPE:-}" == all-staged ]] || exit 92
[[ "${TD6_V89H3_PIVOT_SCOPE:-}" == all-132-section-columns ]] || exit 89
PYTHON=/home/ubuntu/venvs/td6/bin/python3
[[ -x "$PYTHON" ]] || exit 91
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE.sha256
"$PYTHON" replay_v89h3_q14_alternate_pivot.py
