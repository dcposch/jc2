#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82QSF requires Linux" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V82QSF requires Amazon EC2" >&2
  exit 96
fi
if [[ -z "${AWS_RUN_TAG:-}" || "${AWS_RUN_TAG}" != td6_v82qsf_nested_* ]]; then
  echo "REFUSED: registered V82QSF tag required" >&2
  exit 95
fi
sha256sum -c SOURCE.sha256
/home/ubuntu/venvs/td6/bin/python3 replay_v82qsf.py
