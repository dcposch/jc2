#!/bin/bash
# exact-Q (characteristic 0) msolve Groebner run for one chart.
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
K=$1; B=$2; PIN=$3; WD=${4:-7200}; TH=${5:-2}
STEM="K${K}_B${B}_Q${PIN}"
mkdir -p $D/logs
( ulimit -v 62914560 2>/dev/null
  timeout -s KILL "$WD" /usr/bin/time -v python3 -u "$D/msolve_export.py" "$K" "$B" --pin-index "$PIN" \
    --char 0 --run --dump-timeout $((WD-300)) --msolve-timeout $((WD-600)) --threads "$TH" \
    > "$D/logs/${STEM}.exactq_ms.log" 2>&1
  echo "EXACTQMS_RC=$?" >> "$D/logs/${STEM}.exactq_ms.log" )
echo "EXACTQMS_DONE ${STEM}"
