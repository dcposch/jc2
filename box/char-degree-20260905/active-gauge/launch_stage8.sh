#!/bin/bash
set -eu
case "$1" in delta2|delta52) branch="$1";; *) exit 64;; esac
cd /home/ubuntu/jc2
export CHAR_MEMORY_KIB=50331648
ulimit -v "$CHAR_MEMORY_KIB"
exec python3 -u box/char-degree-20260905/active-gauge/active_ring_run.py \
  --input "box/char-degree-20260905/active-gauge/inputs/${branch}_stage8.json" \
  --out "box/char-degree-20260905/active-gauge/${branch}_stage8" \
  --timeout 1800
