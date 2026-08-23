#!/bin/bash
# stuck7_verdicts.sh -- run msolve locally on the SMALL stuck-closure systems
# (< $MAXMB MB, default 25), timeout 900 s each, verdict-authenticated output.
# p>0 jobs use the .RED.ms twin (msolve 0.10.1 64-bit-clamp hazard rule).
set -u
cd "$(dirname "$0")/.."
MAXMB=${MAXMB:-25}
MSOLVE_SEED=${MSOLVE_SEED:-0}
OUT=runs/stuck7_verdicts
mkdir -p "$OUT"
MSOLVE_BIN=$(command -v msolve)
MSOLVE_VERSION=$(msolve --version 2>&1 | head -n 1)
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
    timefile="$OUT/$base.time"
    meta="$OUT/$base.meta"
    [ -s "$o" ] && continue
    echo "== msolve $f (${szmb}MB)"
    char=$(sed -n '2p' "$f" | tr -d '[:space:]')
    {
      echo "utc_start=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
      echo "host=$(hostname)"
      echo "msolve_bin=$MSOLVE_BIN"
      echo "msolve_version=$MSOLVE_VERSION"
      echo "input=$f"
      echo "input_characteristic=$char"
      echo "input_sha256=$(shasum -a 256 "$f" | awk '{print $1}')"
      echo "random_seed=$MSOLVE_SEED"
      echo "command=msolve -v 2 -g 2 --random-seed $MSOLVE_SEED -t 4 -f $f -o $o"
    } > "$meta"
    /usr/bin/time timeout 900 msolve -v 2 -g 2 --random-seed "$MSOLVE_SEED" -t 4 -f "$f" -o "$o" 2> "$timefile"
    rc=$?
    cat "$timefile" >> "$OUT/timings.log"
    grep -i 'initial prime' "$timefile" >> "$meta" || true
    echo "utc_end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$meta"
    echo "exit_status=$rc" >> "$meta"
    [ -s "$o" ] && echo "output_sha256=$(shasum -a 256 "$o" | awk '{print $1}')" >> "$meta"
    if [ $rc -ne 0 ]; then echo "   rc=$rc (timeout/fail)"; continue; fi
    head -c 200 "$o" | tr -d '\n' | head -c 120; echo
    if grep -qx '\[1\]:' "$o" || grep -qx '\[1\]' "$o"; then
      if [ "$char" = 0 ]; then
        echo "   TRACE: FIRST-PRIME-EMPTY (NOT Q-EMPTY)"
      else
        echo "   VERDICT candidate: EMPTY over F_$char (GB=[1]) -- authenticate before banking"
      fi
    elif [ "$char" = 0 ]; then
      if grep -q '^#length of basis:' "$o" && grep -q '^\[' "$o" && grep -q '\]:$' "$o"; then
        echo "   VERDICT: NONEMPTY over Qbar (reconstructed Q basis; engine-trusted)"
      else
        echo "   NO-VERDICT (no complete basis body emitted)"
      fi
    fi
  done
done
