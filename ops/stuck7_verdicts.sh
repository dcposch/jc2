#!/bin/bash
# stuck7_verdicts.sh -- run msolve locally on the SMALL stuck-closure systems
# (< $MAXMB MB, default 25), timeout 900 s each, verdict-authenticated output.
# p>0 jobs use the .RED.ms twin (msolve 0.10.1 64-bit-clamp hazard rule).
set -u
cd "$(dirname "$0")/.."
MAXMB=${MAXMB:-25}
OUT=runs/stuck7_verdicts
mkdir -p "$OUT"
FAMS="12_36mn23d144_r0 12_36mn23d144_r1 12_36mn23d144_r2 12_36mn23d144_r3 \
      6_15mn27d147 10_40mn32d150_r0 10_40mn32d150_r1 12_33mn23d135 8_28mn34d144"
for fam in $FAMS; do
  for f in systems/farm/$fam/*.ms; do
    [ -e "$f" ] || continue
    case "$f" in
      *.RED.ms) ;;                                # reduced twin: runnable
      *.p65521.ms) [ -e "${f%.ms}.RED.ms" ] && continue ;;  # prefer twin
    esac
    szmb=$(( $(stat -f%z "$f") / 1048576 ))
    [ "$szmb" -ge "$MAXMB" ] && continue
    base=$(basename "$f" .ms)
    o="$OUT/$base.out"
    [ -s "$o" ] && continue
    echo "== msolve $f (${szmb}MB)"
    /usr/bin/time timeout 900 msolve -g 2 -t 4 -f "$f" -o "$o" 2>> "$OUT/timings.log"
    rc=$?
    if [ $rc -ne 0 ]; then echo "   rc=$rc (timeout/fail)"; continue; fi
    head -c 200 "$o" | tr -d '\n' | head -c 120; echo
    if [ "$(head -c 4 "$o")" = "[1]:" ] || grep -qx '\[1\]' "$o"; then
      echo "   VERDICT candidate: EMPTY (GB=[1]) -- authenticate before banking"
    fi
  done
done
