#!/usr/bin/env bash
set -euo pipefail

case "${AWS_RUN_TAG:-}" in
  td6_v89h19r1_raw_p13_c12_*) ;;
  *) echo "missing/invalid AWS_RUN_TAG" >&2; exit 2 ;;
esac
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"
: "${TD6_Q_EXPONENT:?TD6_Q_EXPONENT is required}"
: "${TD6_Q_SCOPE:?TD6_Q_SCOPE is required}"
: "${TD6_PIVOT_POLICY:?TD6_PIVOT_POLICY is required}"
: "${TD6_PIVOT_SCOPE:?TD6_PIVOT_SCOPE is required}"
: "${TD6_F_SPECIALIZATION:?TD6_F_SPECIALIZATION is required}"

[[ "$TD6_Q_EXPONENT" == 2 ]]
[[ "$TD6_Q_SCOPE" == q2-q14-q16-q24 ]]
[[ "$TD6_PIVOT_POLICY" == ascending ]]
[[ "$TD6_PIVOT_SCOPE" == all-staged ]]
[[ "$TD6_F_SPECIALIZATION" == exact-C-equals-V2-minus-U3-over-U ]]

python3 replay_v89h19r1_raw_p13_coordinate12_audit.py
