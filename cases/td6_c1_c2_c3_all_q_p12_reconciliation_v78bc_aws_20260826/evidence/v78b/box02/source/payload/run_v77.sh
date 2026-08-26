#!/usr/bin/env bash
set -euo pipefail

test "$(uname -s)" = Linux || { echo "REFUSE_NON_LINUX" >&2; exit 90; }
test -n "${TD6_V77_EXPECT_HOST:-}" || { echo "MISSING_EXPECT_HOST" >&2; exit 91; }
test "$(hostname)" = "$TD6_V77_EXPECT_HOST" || { echo "HOST_MISMATCH" >&2; exit 92; }
case "${TD6_V77_RUN_TAG:-}" in
  td6_v77_*) ;;
  *) echo "UNREGISTERED_RUN_TAG" >&2; exit 93 ;;
esac

cd "$(dirname "$0")"
sha256sum -c SOURCE.sha256
echo "aws_platform=$(uname -s)"
echo "aws_hostname=$(hostname)"
echo "aws_run_tag=$TD6_V77_RUN_TAG"
exec python3 jc2/cases/td6_c1_c2_c3_q3_gamma_dual_20260825/replay.py
