#!/bin/bash
set -eu
cd /home/ubuntu/jc2/box/char-degree-20260905/d108
printf '%s\n' 0 1 2 3 4 5 6 7 8 | xargs -P 2 -I STAGE bash -c '
  ulimit -v 25165824
  export CHAR_RUN_SUFFIX=_m24 CHAR_MEMORY_KIB=25165824
  exec python3 normalized_backend.py --stage STAGE --run --timeout 1200 > totalface-stageSTAGE-m24.driver.log 2>&1
'
