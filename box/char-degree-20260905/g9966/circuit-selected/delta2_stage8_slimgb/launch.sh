#!/bin/bash
set -eu
cd /home/ubuntu/jc2
python3 -u box/char-degree-20260905/d108/coefficient_circuit_backend_v2.py \
  --input box/char-degree-20260905/g9966/circuit-inputs/delta2_stage8.input.json \
  --out box/char-degree-20260905/g9966/circuit-selected/delta2_stage8_slimgb/base.sing \
  --timeout 0
python3 box/char-degree-20260905/slimgb_variant.py \
  --source box/char-degree-20260905/g9966/circuit-selected/delta2_stage8_slimgb/base.sing \
  --out box/char-degree-20260905/g9966/circuit-selected/delta2_stage8_slimgb/augmented.sing
exec python3 -u box/char-degree-20260905/run_singular_case.py \
  --script box/char-degree-20260905/g9966/circuit-selected/delta2_stage8_slimgb/augmented.sing \
  --out box/char-degree-20260905/g9966/circuit-selected/delta2_stage8_slimgb \
  --input box/char-degree-20260905/g9966/circuit-inputs/delta2_stage8.input.json \
  --seconds 1200 --memory-gib 32
