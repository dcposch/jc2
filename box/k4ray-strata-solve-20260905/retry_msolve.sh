#!/bin/bash
# Re-run msolve on an already-emitted .ms file with a high memory ceiling.
#   retry_msolve.sh <STEM_p CHAR> <timeout> <threads> <vmem_kb>
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
MS=$1; TO=${2:-3000}; TH=${3:-4}; VM=${4:-157286400}
base=$(basename "$MS" .ms)
( ulimit -v $VM 2>/dev/null
  /usr/bin/time -v timeout -s KILL "$TO" msolve -g 2 -t "$TH" -f "$MS" -o "$D/msolve/${base}.retry.msout" \
    > "$D/logs/${base}.retry.log" 2>&1
  echo "RETRY_RC=$?" >> "$D/logs/${base}.retry.log" )
echo -n "RETRY $base "
if [ -s "$D/msolve/${base}.retry.msout" ]; then
  L=$(grep -o 'length of basis:[^,]*' "$D/msolve/${base}.retry.msout" | head -1)
  B=$(grep -v '^#' "$D/msolve/${base}.retry.msout" | tr -d ' \n')
  if [ "$B" = "[1]:" ]; then echo "UNIT ($L)"; else echo "NONUNIT ($L) head=$(echo $B|cut -c1-120)"; fi
else echo "NO_OUTPUT rc=$(grep -o 'RETRY_RC=.*' $D/logs/${base}.retry.log|tail -1)"; fi
