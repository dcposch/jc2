#!/bin/bash
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
K=$1; B=$2; PIN=$3; WD=${4:-4200}; TH=${5:-4}; VM=${6:-209715200}
STEM="K${K}_B${B}_Q${PIN}"
( ulimit -v $VM 2>/dev/null
  timeout -s KILL "$WD" /usr/bin/time -v python3 -u "$D/msolve_export.py" "$K" "$B" --pin-index "$PIN" \
    --char 0 --run --dump-timeout $((WD-200)) --msolve-timeout $((WD-400)) --threads "$TH" \
    > "$D/logs/${STEM}.exactq_ms2.log" 2>&1
  echo "EQ2_RC=$?" >> "$D/logs/${STEM}.exactq_ms2.log" )
echo "EQ2_DONE ${STEM}"
