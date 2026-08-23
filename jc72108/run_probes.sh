#!/bin/zsh
# E1 probe matrix: all nonorigin systems at p=65521, smallest first.
# Usage: ./run_probes.sh [threads]
set -u
T=${1:-10}
MSOLVE_SEED=${MSOLVE_SEED:-0}
cd "$(dirname "$0")"
MSOLVE_BIN=$(command -v msolve)
MSOLVE_VERSION=$(msolve --version 2>&1 | head -n 1)
for sys in reg_9_24_c3 open_8_28_c2 reg_9_24_c2 reg_7_21 open_8_28_c1 reg_9_24_c1 reg_9_27; do
  f="systems/${sys}.p65521.ms"
  o="runs/${sys}.p65521.out"
  timefile="runs/${sys}.p65521.time"
  meta="runs/${sys}.p65521.meta"
  [ -s "$o" ] && { echo "SKIP $sys (nonempty output exists)"; continue; }
  echo "=== $sys start $(date +%H:%M:%S)"
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
    echo "command=msolve -v 2 -g 2 --random-seed $MSOLVE_SEED -t $T -f $f -o $o"
  } > "$meta"
  /usr/bin/time msolve -v 2 -g 2 --random-seed "$MSOLVE_SEED" -t "$T" -f "$f" -o "$o" 2> "$timefile"
  status=$?
  cat "$timefile" >> runs/timings.log
  grep -i 'initial prime' "$timefile" >> "$meta" || true
  echo "utc_end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$meta"
  echo "exit_status=$status" >> "$meta"
  [ -s "$o" ] && echo "output_sha256=$(shasum -a 256 "$o" | awk '{print $1}')" >> "$meta"
  if [ $status -ne 0 ]; then echo "!!! $sys FAILED status=$status"; continue; fi
  if grep -qx '\[1\]:' "$o"; then
    if [ "$char" = 0 ]; then
      verdict="FIRST-PRIME-EMPTY (NOT Q-EMPTY)"
    else
      verdict="EMPTY over F_$char (GB=[1])"
    fi
  elif [ "$char" = 0 ]; then
    if grep -q '^#length of basis:' "$o" && grep -q '^\[' "$o" && grep -q '\]:$' "$o"; then
      verdict="NONEMPTY over Qbar (reconstructed Q basis; engine-trusted)"
    else
      verdict="NO-VERDICT (no complete basis body emitted)"
    fi
  else
    verdict="NONEMPTY-OR-UNDECIDED over F_$char (basis $(grep -c ',' "$o" || true) lines)"
  fi
  echo "=== $sys done $(date +%H:%M:%S): $verdict"
done
echo "ALL PROBES DONE"
