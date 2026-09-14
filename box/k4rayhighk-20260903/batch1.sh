#!/bin/bash
cd /home/ubuntu/jc2
R=box/k4rayhighk-20260903/runs
for spec in "CAL_K5_B4 5 4" "CAL_K5_B9 5 9" "CAL_K6_B5 6 5" "CAL_K6_B11 6 11" "MAIN_K7_B6 7 6" "MAIN_K8_B7 8 7" "MAIN_K9_B8 9 8"; do
  set -- $spec
  echo "=== $1 start $(date +%T)"
  timeout 1300 python3 box/k4rayhighk-20260903/drive.py $1 direct $2 $3 --timeout 1200 2>&1 | tail -2
  echo "=== $1 exit=$? $(date +%T)"
done
