#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$HERE/run_stage.sh" delta2 3 12000
