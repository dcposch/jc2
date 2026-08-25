#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$case_dir"

python3 check_matrix_identity.py
python3 check_vertical_state.py
shasum -a 256 -c MANIFEST.sha256
printf '%s\n' 'PASS-AS-D7-VERTICAL-STATE-SUFFICIENCY-ALL'
