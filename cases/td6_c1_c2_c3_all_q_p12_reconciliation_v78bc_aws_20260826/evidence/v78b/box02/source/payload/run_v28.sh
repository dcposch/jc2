#!/usr/bin/env bash
set -euo pipefail
sha256sum -c SOURCE.sha256
/usr/bin/time -v timeout 28800 python3 \
  jc2/cases/td6_c1_c2_c3_q2_beta_dual_20260825/replay.py \
  > beta-dual.stdout 2> beta-dual.stderr
