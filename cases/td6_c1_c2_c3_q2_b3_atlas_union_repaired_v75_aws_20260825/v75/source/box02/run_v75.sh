#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

case "$(uname -s)" in
  Linux) ;;
  *) echo "REFUSE: V75 is AWS/Linux only" >&2; exit 90 ;;
esac

: "${JC2_AWS_RUN_TAG:?registered AWS run tag required}"
: "${JC2_AWS_EXPECTED_HOSTNAME:?exact AWS hostname required}"
test "$(hostname)" = "$JC2_AWS_EXPECTED_HOSTNAME"
case "$JC2_AWS_RUN_TAG" in td6_v75_*) ;; *) exit 91 ;; esac

sha256sum -c SOURCE.sha256
timeout --signal=TERM --kill-after=15s 300 /usr/bin/python3 replay_v75.py
