#!/bin/sh
# D25PF1: single-representative per-fiber D25 probe (redirect 2026-08-20).
# Rationale: batch-1 of the 36-fiber race (d25pf_run.sh) returned 4/4
# UNIFORM rc=124 at the 3600 s caps (a00mm/a00mp/a00pm/a00pp); by the
# 8.S8 support-identity structure the 36 fibers are expected uniformly
# difficult, so 36 one-hour timeouts carry no more information than 4.
# The batch was cancelled (literal inspected PIDs, no pattern kills) and
# replaced by ONE representative fiber -- a00pp, the historically banked
# one -- at a 24 h cap, -t 8.  Marker "D25PF1 a00pp: rc=.. size=.." to
# pilot.log.  The union + l44 lanes continue untouched as the primary
# verdict routes.
# Launch: setsid nohup sh d25pf1_run.sh > ~/jc72108/d25pf/pf1.console.log 2>&1 &
P=105337
ROOT=${D25_ROOT:-$HOME/jc72108}
D=$ROOT/d25pf
mkdir -p "$D/out"
echo $$ > "$D/pf1.pid"
echo "LAUNCH D25PF1 a00pp p$P 24h t8 $(date -u +%FT%TZ)" >> "$ROOT/pilot.log"
t0=$(date +%s)
timeout 86400 msolve -v 2 -g 2 -t 8 -f "$D/d25pf_p${P}_a00pp.ms" \
  -o "$D/out/d25pf1_a00pp.out" > "$D/out/d25pf1_a00pp.v2log" 2>&1
rc=$?
echo "D25PF1 a00pp: rc=$rc size=$(wc -c < "$D/out/d25pf1_a00pp.out" | tr -d ' ') secs=$(( $(date +%s) - t0 )) p$P" >> "$ROOT/pilot.log"
rm -f "$D/pf1.pid"
