#!/bin/bash
cd /home/ubuntu/jc2
for spec in "MAIN_K7_B6 7 6" "MAIN_K8_B7 8 7" "MAIN_K9_B8 9 8" "MAIN_K7_B7 7 7" "MAIN_K7_B8 7 8" "MAIN_K8_B8 8 8" "MAIN_K9_B9 9 9" "MAIN_K7_B9 7 9" "MAIN_K8_B9 8 9" "MAIN_K9_B10 9 10" "MAIN_K7_B10 7 10" "MAIN_K9_B11 9 11"; do
  set -- $spec
  echo "=== $1 start $(date +%T)"
  timeout 1000 python3 box/k4rayhighk-20260903/drive.py $1 direct $2 $3 --timeout 900 --cores 2 2>&1 | tail -2
  echo "=== $1 rc=$? $(date +%T)"
done
echo ALLDONE
