#!/bin/sh
# D25PF lane runner (box01; atlas 8.S8 lane pattern): the 36 per-fiber
# D25 race systems, 4 parallel lanes x (msolve -g 2 -t 4), timeout 3600
# per fiber; completion markers "D25PF <fiber>: rc=.. size=.. secs=.."
# appended to ~/jc72108/pilot.log.  Orphan-safe: launch as
#   setsid nohup sh d25pf_run.sh 105337 > d25pf/run_p105337.log 2>&1 &
# Resume-safe: fibers with a banked rc=0 marker + nonempty .out are
# skipped (see d25pf_lane.sh).  DOES NOT touch the running union lanes
# (msolve ... d25fam_*): no pkill anywhere in this chain.
P=${1:-105337}
ROOT=${D25_ROOT:-$HOME/jc72108}
D=$ROOT/d25pf
mkdir -p "$D/out"
echo $$ > "$D/run_p$P.pid"
LABS=$(ls "$D" | sed -n "s/^d25pf_p${P}_\(a[0-9][0-9][pm][pm]\)\.ms$/\1/p" | sort)
N=$(echo "$LABS" | wc -w | tr -d ' ')
echo "LAUNCH D25PF x$N p$P 4lanes t4 cap3600 $(date -u +%FT%TZ)" >> "$ROOT/pilot.log"
echo "$LABS" | tr ' ' '\n' | xargs -P 4 -I{} sh "$ROOT/d25/d25pf_lane.sh" "$P" "{}"
echo "D25PF-RUN p$P DONE $(date -u +%FT%TZ)" >> "$ROOT/pilot.log"
rm -f "$D/run_p$P.pid"
