#!/bin/sh
# One D25PF lane: solve a single per-fiber D25 race system (called by
# d25pf_run.sh via xargs -P 4).  Marker + rc + size self-recorded to
# pilot.log; 0-byte .out is NEVER a verdict (rc decides).
P=$1
lab=$2
ROOT=${D25_ROOT:-$HOME/jc72108}
D=$ROOT/d25pf
f=$D/d25pf_p${P}_${lab}.ms
o=$D/out/d25pf_p${P}_${lab}.out
if [ -s "$o" ] && grep -q "^D25PF $lab: rc=0 .*p$P\$" "$ROOT/pilot.log"; then
  exit 0
fi
t0=$(date +%s)
timeout 3600 msolve -v 2 -g 2 -t 4 -f "$f" -o "$o" \
  > "$D/out/d25pf_p${P}_${lab}.v2log" 2>&1
rc=$?
echo "D25PF $lab: rc=$rc size=$(wc -c < "$o" | tr -d ' ') secs=$(( $(date +%s) - t0 )) p$P" >> "$ROOT/pilot.log"
