#!/bin/zsh
# E1 probe matrix: all nonorigin systems at p=65521, smallest first.
# Usage: ./run_probes.sh [threads]
set -u
T=${1:-10}
cd "$(dirname "$0")"
for sys in reg_9_24_c3 open_8_28_c2 reg_9_24_c2 reg_7_21 open_8_28_c1 reg_9_24_c1 reg_9_27; do
  f="systems/${sys}.p65521.ms"
  o="runs/${sys}.p65521.out"
  [ -f "$o" ] && { echo "SKIP $sys (output exists)"; continue; }
  echo "=== $sys start $(date +%H:%M:%S)"
  /usr/bin/time msolve -g 2 -t "$T" -f "$f" -o "$o" 2>> runs/timings.log
  status=$?
  if [ $status -ne 0 ]; then echo "!!! $sys FAILED status=$status"; continue; fi
  if grep -qx '\[1\]:' "$o"; then verdict="EMPTY (GB=[1])"; else
    verdict="NONEMPTY-OR-UNDECIDED (basis $(grep -c ',' "$o" || true) lines)"
  fi
  echo "=== $sys done $(date +%H:%M:%S): $verdict"
done
echo "ALL PROBES DONE"
