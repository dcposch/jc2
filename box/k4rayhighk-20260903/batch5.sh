#!/bin/bash
cd /home/ubuntu/jc2
for spec in "7 6" "7 7" "7 8" "7 9" "8 7" "8 8" "8 9" "9 8" "9 9" "9 10" "7 10" "7 11" "8 10" "9 11" "7 12" "7 13" "8 11" "9 12"; do
  set -- $spec; K=$1; b=$2
  cut=$((3*b-2*K)); if [ $cut -lt 0 ]; then cut=0; fi
  echo "=== MOD_K${K}_B${b} cut=$cut start $(date +%T)"
  timeout 400 python3 box/k4rayhighk-20260903/drive.py MOD_K${K}_B${b} direct $K $b --rhocut $cut --chars 32003 --timeout 360 --cores 1 2>&1 | tail -1
  echo "=== MOD_K${K}_B${b} rc=$? $(date +%T)"
done
echo BATCH5_DONE
