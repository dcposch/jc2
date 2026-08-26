#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82P is AWS/Linux only" >&2
  exit 97
fi
if [[ -z "${AWS_RUN_TAG:-}" || "${AWS_RUN_TAG}" != td6_v82p_* ]]; then
  echo "REFUSED: registered td6_v82p_ tag required" >&2
  exit 98
fi
: "${TD6_OUTPUT_DIR:?missing TD6_OUTPUT_DIR}"
: "${TD6_DEAD_LEVEL:?missing TD6_DEAD_LEVEL}"
case "$TD6_DEAD_LEVEL" in
  10|15) ;;
  *) echo "REFUSED: level must be 10 or 15" >&2; exit 99 ;;
esac
PYTHON=/home/ubuntu/venvs/td6/bin/python3
[[ -x "$PYTHON" ]] || exit 100
printf 'aws_hostname=%s\naws_run_tag=%s\n' "$(hostname)" "$AWS_RUN_TAG"
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE.sha256
"$PYTHON" payload/jc2/cases/td6_c1_c2_c3_kernel_dead_staged_shard_v82p_20260826/replay.py
