#!/bin/bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
GI_ROOT="$(cd "$HERE/../.." && pwd)"
python3 "$GI_ROOT/solve_class.py" --class-id "C_n24m16_M12_17_ell1_s3" --timeout 600 --build-timeout 3600 --output-dir "$HERE/solve" \
  --modular-screen --screen-timeout 600 --msolve-threads 8
