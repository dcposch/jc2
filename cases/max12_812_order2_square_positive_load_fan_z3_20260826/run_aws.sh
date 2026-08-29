#!/usr/bin/env bash
set -euo pipefail

[[ "$(uname -s)" == Linux ]] || exit 97
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
[[ "${AWS_RUN_TAG:-}" == max12_812_order2_square_positive_load_fan_z3_* ]] || exit 95
: "${FAN_OUTPUT_DIR:?FAN_OUTPUT_DIR required}"
: "${FAN_VENV:?FAN_VENV required}"
mkdir -p "$FAN_OUTPUT_DIR"
python3 -m venv "$FAN_VENV"
"$FAN_VENV/bin/python" -m pip install --disable-pip-version-check --no-input 'z3-solver==4.13.3.0'
"$FAN_VENV/bin/python" -m pip freeze | sort > "$FAN_OUTPUT_DIR/pip-freeze.txt"
"$FAN_VENV/bin/python" enumerate_positive_load_fan.py
python3 verify_positive_load_fan.py "$FAN_OUTPUT_DIR/positive_load_fan_cells.json"
sha256sum "$FAN_OUTPUT_DIR/positive_load_fan_cells.json" "$FAN_OUTPUT_DIR/pip-freeze.txt"

