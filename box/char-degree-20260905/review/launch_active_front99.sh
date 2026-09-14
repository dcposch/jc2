#!/bin/bash
set -eu
cd /home/ubuntu/jc2
export CHAR_MEMORY_KIB=50331648
ulimit -v "$CHAR_MEMORY_KIB"
mkdir -p box/char-degree-20260905/review/front99-delta2-stage0-active
exec python3 -u box/char-degree-20260905/review/active_ring_run.py \
  --input box/char-degree-20260905/g9966/front-inputs/delta2_stage0.json \
  --out box/char-degree-20260905/review/front99-delta2-stage0-active \
  --timeout 1200
