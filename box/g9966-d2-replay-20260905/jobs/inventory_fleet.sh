#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE"
export PYTHONHASHSEED=0 OMP_NUM_THREADS=1
mkdir -p out
python3 -u replay_engine.py --branch delta2 --stage 0 --inventory-only \
  > out/inventory-delta2-stage0.json
python3 -u replay_engine.py --branch delta52 --stage 0 --inventory-only \
  > out/inventory-delta52-stage0.json
echo GG_INVENTORY_DONE
