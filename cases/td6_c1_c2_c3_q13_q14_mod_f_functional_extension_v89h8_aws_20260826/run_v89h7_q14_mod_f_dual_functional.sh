#!/usr/bin/env bash
set -euo pipefail

[[ "$(uname -s)" == Linux ]] || exit 97
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
[[ -n "${AWS_RUN_TAG:-}" && "$AWS_RUN_TAG" == td6_v89h7_q14_mod_f_dual_functional_* ]] || exit 95
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR required}"
[[ "${TD6_Q_EXPONENT:-}" == 2 ]] || exit 94
[[ "${TD6_PIVOT_POLICY:-}" == ascending ]] || exit 93
[[ "${TD6_PIVOT_SCOPE:-}" == all-staged ]] || exit 92
[[ "${TD6_Q_SCOPE:-}" == tail-q14-q16-q24 ]] || exit 91
[[ "${TD6_F_SPECIALIZATION:-}" == exact-C-equals-V2-minus-U3-over-U ]] || exit 89
[[ "${TD6_PRIME_SENTINEL:-}" == p1000033-C15-V4-U1 ]] || exit 88
[[ "${TD6_FUNCTIONAL:-}" == q14-empty-parameter-e3-coordinate0 ]] || exit 87
PYTHON=/home/ubuntu/venvs/td6/bin/python3
[[ -x "$PYTHON" ]] || exit 90
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE.sha256
sha256sum -c PAYLOAD_CLOSURE.sha256
"$PYTHON" replay_v89h7_q14_mod_f_dual_functional.py
