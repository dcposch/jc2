#!/bin/bash
# assemble report from sections (append-only cat), verify inputs, size, collision scan, artifact hashes
set -u
B=/home/ubuntu/jc2/box/k16-universal-20260905; R=/home/ubuntu/jc2/xmodel/k16-universal-series-fable5-20260905.md
cd /home/ubuntu/jc2 || exit 1
sha256sum -c $B/manifest.sha256 > $B/input-verification-final.log 2>&1; echo "inputs: $(grep -c ': OK' $B/input-verification-final.log)/4 OK"
if [ -e "$R" ]; then echo "REPORT EXISTS — not overwriting"; exit 2; fi
cat $B/sections/00_header.md $B/sections/01_custody.md $B/sections/02_task1.md $B/sections/03_task2.md $B/sections/04_task3.md $B/sections/05_verify.md $B/sections/06_verdict.md $B/sections/07_fallacy.md $B/sections/08_opens.md $B/sections/09_record.md > $R
printf '\n<!-- BODY-END -->\n' >> $R
echo "report bytes: $(wc -c < $R)"; grep -c "BODY-END" $R
python3 ops/open_collision.py --root . $R > $B/collision_scan.txt 2>&1; echo "collision rc=$?"
grep -v "k16-universal-series\|k16-universal-20260905" $B/collision_scan.txt > $B/collision_scan.filtered.txt; head -8 $B/collision_scan.filtered.txt
