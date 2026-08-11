#!/bin/bash
# stuck7_post.sh -- post-emission steps for the stuck-family closure
# (SECTION4-AUTOMATION.md "Stuck-family closure"):
#   1. produce round-trip-guarded .RED.ms twins for every new p>0 emission
#      (AUDIT.md 2026-08-10 standing rule: all p>0 shipments reduced into [0,p))
#   2. write the farm queue fragment systems/farm/queue/stuck7/queue.txt
#      (same format as dispatch(); box01/box02 queue.txt untouched: box01 live)
set -e
cd "$(dirname "$0")/.."
FAMS="12_36mn23d144_r0 12_36mn23d144_r1 12_36mn23d144_r2 12_36mn23d144_r3 \
      6_15mn27d147 10_40mn32d150_r0 10_40mn32d150_r1 12_33mn23d135 8_28mn34d144"
for fam in $FAMS; do
  for f in systems/farm/$fam/*.p65521.ms; do
    [ -e "$f" ] || continue
    case "$f" in *.RED.ms) continue;; esac
    red="${f%.ms}.RED.ms"
    if [ ! -e "$red" ]; then
      python3 ops/reduce_msp.py "$f" "$red" && echo "RED twin: $red"
    fi
  done
done
mkdir -p systems/farm/queue/stuck7
python3 - <<'EOF'
import json, os
fams = ("12_36mn23d144_r0 12_36mn23d144_r1 12_36mn23d144_r2 12_36mn23d144_r3 "
        "6_15mn27d147 10_40mn32d150_r0 10_40mn32d150_r1 12_33mn23d135 "
        "8_28mn34d144").split()
import hashlib
jobs, seen = [], {}
for fam in fams:
    man = json.load(open(f"systems/farm/{fam}/manifest.json"))
    for e in man.get("cases", []):
        for rec in e.get("systems", []):
            if "path" not in rec:
                continue
            p = rec["path"]
            if rec["char"]:                     # p>0: ship the RED twin
                red = p[:-3] + "RED.ms"
                if os.path.exists(red):
                    p = red
            h = hashlib.md5(open(p, "rb").read()).hexdigest()
            if h in seen:                       # 12_36 r1/r2 twin systems:
                print(f"dedup: {p} == {seen[h]} (verdict transfers)")
                continue
            seen[h] = p
            jobs.append((rec["bytes"], p))
jobs.sort(key=lambda j: (-j[0], j[1]))
with open("systems/farm/queue/stuck7/queue.txt", "w") as f:
    f.write(f"# farm queue stuck7 (stuck-family closure): {len(jobs)} jobs, "
            f"{sum(b for b, _ in jobs)} bytes est\n")
    for _, p in jobs:
        f.write(p + "\n")
print(f"queue fragment: {len(jobs)} jobs")
EOF
