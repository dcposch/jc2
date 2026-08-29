#!/usr/bin/env bash
set -euo pipefail

: "${AWS_RUN_TAG:?AWS_RUN_TAG is required}"
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"
: "${TD6_Q_EXPONENT:?TD6_Q_EXPONENT is required}"
: "${TD6_PIVOT_POLICY:?TD6_PIVOT_POLICY is required}"
: "${TD6_PIVOT_SCOPE:?TD6_PIVOT_SCOPE is required}"
: "${TD6_Q_SCOPE:?TD6_Q_SCOPE is required}"
: "${TD6_F_SPECIALIZATION:?TD6_F_SPECIALIZATION is required}"

case "$AWS_RUN_TAG" in
  td6_v89h15_allq_p13_*) ;;
  *) echo "refusing non-AWS or misregistered tag" >&2; exit 97 ;;
esac

exec python3 replay_v89h15_allq_p13_full_normal_form.py
