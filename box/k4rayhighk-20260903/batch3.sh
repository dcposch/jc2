#!/bin/bash
cd /home/ubuntu/jc2
for K in 7 8 9; do
  BMAX=$((2*K-1))
  for ((b=1;b<=BMAX;b++)); do
    cut=$((3*b-2*K)); if [ $cut -lt 0 ]; then cut=0; fi
    echo "=== SCUT_K${K}_B${b} cut=$cut start $(date +%T)"
    timeout 460 python3 box/k4rayhighk-20260903/drive.py SCUT_K${K}_B${b} direct $K $b --rhocut $cut --timeout 420 --cores 1 2>&1 | tail -1
    echo "=== SCUT_K${K}_B${b} rc=$? $(date +%T)"
  done
done
echo BATCH3_DONE
