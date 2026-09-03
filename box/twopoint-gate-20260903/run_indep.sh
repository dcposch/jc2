#!/bin/bash
cd /home/ubuntu/jc2/box/twopoint-gate-20260903/indep
for s in R1b_21_14_15_6_k4_mod32003 R2_21_14_15_6_k4_mod32003 R1b_21_14_15_6_k4_Q R2_21_14_15_6_k4_Q R1b_24_16_18_7_k4_mod32003 R1b_27_18_21_8_k4_mod32003 R2_24_16_18_7_k4_mod32003 R2_27_18_21_8_k4_mod32003 R1b_24_16_18_7_k4_Q R1b_27_18_21_8_k4_Q R2_24_16_18_7_k4_Q R2_27_18_21_8_k4_Q; do
  /usr/bin/time -f "WALL=%e RSS=%MKB EXIT=%x" -o $s.time timeout 400 Singular -q --no-rc $s.sing > $s.out 2>&1
  echo "== $s :: $(grep -E 'CONTROL|MAIN|dim=|DIVISION|degx|^[0-9]+$' $s.out | tr '\n' ' ') :: $(cat $s.time)" >> ../indep_runs.log
done
echo ALLDONE >> ../indep_runs.log
