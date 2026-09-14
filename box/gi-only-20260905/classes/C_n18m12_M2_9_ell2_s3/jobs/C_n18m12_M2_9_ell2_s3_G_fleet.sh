#!/bin/bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
GI_ROOT="$(cd "$HERE/../.." && pwd)"
python3 "$GI_ROOT/solve_class.py" --class-id "C_n18m12_M2_9_ell2_s3" --timeout 600 --output-dir "$HERE/solve" \
  --modular-screen --screen-timeout 600 --msolve-threads 8
