#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82 is AWS/Linux only" >&2
  exit 97
fi
if [[ -z "${AWS_RUN_TAG:-}" || "${AWS_RUN_TAG}" != td6_v82_* ]]; then
  echo "REFUSED: missing registered td6_v82_ AWS_RUN_TAG" >&2
  exit 98
fi
: "${TD6_OUTPUT_DIR:?missing TD6_OUTPUT_DIR}"

PYTHON=/home/ubuntu/venvs/td6/bin/python3
if [[ ! -x "$PYTHON" ]]; then
  echo "REFUSED: registered TD6 AWS Python is absent: $PYTHON" >&2
  exit 99
fi
printf 'aws_hostname=%s\n' "$(hostname)"
printf 'aws_run_tag=%s\n' "$AWS_RUN_TAG"
"$PYTHON" -c 'import flint; print("python_flint_version=" + flint.__version__)'
sha256sum -c SOURCE.sha256
"$PYTHON" payload/jc2/cases/td6_c1_c2_c3_q_dead_joint_first_fitting_v82_20260826/replay.py
