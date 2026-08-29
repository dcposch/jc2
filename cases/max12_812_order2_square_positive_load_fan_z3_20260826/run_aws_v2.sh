#!/usr/bin/env bash
set -euo pipefail

[[ "$(uname -s)" == Linux ]] || exit 97
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
[[ "${AWS_RUN_TAG:-}" == max12_812_order2_square_positive_load_fan_z3_v2_* ]] || exit 95
: "${FAN_OUTPUT_DIR:?FAN_OUTPUT_DIR required}"
: "${FAN_VENV:?FAN_VENV required}"
mkdir -p "$FAN_OUTPUT_DIR/wheel"
python3 -m pip download --disable-pip-version-check --no-input --only-binary=:all: \
  --no-deps --dest "$FAN_OUTPUT_DIR/wheel" 'z3-solver==4.13.3.0'
wheel_count=$(find "$FAN_OUTPUT_DIR/wheel" -maxdepth 1 -type f -name '*.whl' | wc -l | tr -d ' ')
[[ "$wheel_count" == 1 ]] || exit 94
sha256sum "$FAN_OUTPUT_DIR"/wheel/*.whl > "$FAN_OUTPUT_DIR/wheel.sha256"
python3 -m venv "$FAN_VENV"
"$FAN_VENV/bin/python" -m pip install --disable-pip-version-check --no-input \
  --no-index --find-links "$FAN_OUTPUT_DIR/wheel" 'z3-solver==4.13.3.0'
"$FAN_VENV/bin/python" -m pip freeze | sort > "$FAN_OUTPUT_DIR/pip-freeze.txt"
"$FAN_VENV/bin/python" enumerate_positive_load_fan.py
python3 verify_positive_load_fan.py "$FAN_OUTPUT_DIR/positive_load_fan_cells.json"
sha256sum "$FAN_OUTPUT_DIR/positive_load_fan_cells.json" \
  "$FAN_OUTPUT_DIR/pip-freeze.txt" "$FAN_OUTPUT_DIR/wheel.sha256"

