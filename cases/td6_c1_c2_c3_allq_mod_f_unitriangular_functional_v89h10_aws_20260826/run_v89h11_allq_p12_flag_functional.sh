#!/usr/bin/env bash
set -euo pipefail

[[ "$(uname -s)" == Linux ]] || exit 97
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
[[ -n "${AWS_RUN_TAG:-}" && "$AWS_RUN_TAG" == td6_v89h11_allq_p12_flag_functional_* ]] || exit 95
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
[[ "${TD6_Q_EXPONENT:-}" == 2 ]] || exit 94
[[ "${TD6_PIVOT_POLICY:-}" == ascending ]] || exit 93
[[ "${TD6_PIVOT_SCOPE:-}" == all-staged ]] || exit 92
[[ "${TD6_Q_SCOPE:-}" == q2-q14-q16-q24 ]] || exit 91
[[ "${TD6_F_SPECIALIZATION:-}" == exact-C-equals-V2-minus-U3-over-U ]] || exit 89
[[ "${TD6_FUNCTIONAL_SCOPE:-}" == empty-parameter-allq ]] || exit 88
PYTHON=/home/ubuntu/venvs/td6/bin/python3
[[ -x "$PYTHON" ]] || exit 90
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE_P12_FLAG.sha256
sha256sum -c PAYLOAD_CLOSURE.sha256
"$PYTHON" replay_v89h11_allq_p12_flag_functional.py
