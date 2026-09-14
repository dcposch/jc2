#!/bin/bash
set -eu
cd /home/ubuntu/jc2/box/char-degree-20260905/d108
# Exactly Q, complete characteristic coefficients, each stage independent.
# Cap each child address space at 12 GiB; at most three jobs are live.
printf '%s\n' 0 1 2 3 4 5 6 7 8 | xargs -P 3 -I STAGE bash -c '
  ulimit -v 12582912
  exec python3 char_degree_driver.py --stage STAGE --run --timeout 1200 > stageSTAGE.driver.log 2>&1
'
