#!/bin/bash
# One k=4-ray beta-stratum chart (K,b,pin): guided_gb exact-Q AND msolve modular,
# in parallel, each under its own watchdog.  Detached-safe.
#   solve_stratum.sh K b PIN [WATCHDOG_SECONDS] [CORES] [PRIME]
set -uo pipefail
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
K=$1; B=$2; PIN=$3; WD=${4:-9000}; CORES=${5:-2}; P=${6:-32003}
STEM="K${K}_B${B}_Q${PIN}"
mkdir -p "$D/logs"
export PYTHONUNBUFFERED=1

( ulimit -v 25165824 2>/dev/null
  timeout -s KILL "$WD" /usr/bin/time -v python3 -u "$D/strata_chart.py" run \
    "${STEM}_EXACTQ" "$K" "$B" --pin-index "$PIN" --chars 0 \
    --timeout $((WD-300)) --count-timeout $((WD-300)) --cores "$CORES" \
    > "$D/logs/${STEM}.exactq.log" 2>&1
  echo "EXACTQ_RC=$?" >> "$D/logs/${STEM}.exactq.log" ) &
PQ=$!

( ulimit -v 25165824 2>/dev/null
  timeout -s KILL "$WD" /usr/bin/time -v python3 -u "$D/msolve_export.py" \
    "$K" "$B" --pin-index "$PIN" --char "$P" --run \
    --dump-timeout $((WD-300)) --msolve-timeout $((WD-600)) --threads "$CORES" \
    > "$D/logs/${STEM}.mod.log" 2>&1
  echo "MOD_RC=$?" >> "$D/logs/${STEM}.mod.log" ) &
PM=$!

wait $PQ; wait $PM
echo "STRATUM_DONE ${STEM}"
