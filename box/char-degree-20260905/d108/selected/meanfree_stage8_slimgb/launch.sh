#!/bin/bash
set -eu
cd /home/ubuntu/jc2/box/char-degree-20260905/d108
python3 -u coefficient_circuit_backend_v2.py --input selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json --out selected/meanfree_stage8_slimgb/base.sing --timeout 0
python3 selected/meanfree_stage8_slimgb/slimgb_variant_snapshot.py --source selected/meanfree_stage8_slimgb/base.sing --out selected/meanfree_stage8_slimgb/augmented.sing
exec python3 -u selected/meanfree_stage8_slimgb/run_singular_case_snapshot.py --script selected/meanfree_stage8_slimgb/augmented.sing --out selected/meanfree_stage8_slimgb --input selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json --seconds 1200 --memory-gib 32
