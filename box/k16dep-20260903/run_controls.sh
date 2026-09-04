#!/bin/bash
# controls for the formula J(Q,P) = c*gamma + pi*E(h): t=2 both fibres, generic points, gauge change; t=3,4,5 mod p
set -u
J=/tmp/jc2-lane.9Mpgn1/inputs/terminal_laurent_t2.json
run() { echo "----- $*"; timeout 600 python3 rebuild_pair.py "$@" 2>&1 | grep -v "^PIVOT"; }
run 2 --fibre 1/5 --point 3,0 --json $J --label "AXIS b3=3"
run 2 --fibre 1/5 --point -2/7,0 --json $J --label "AXIS b3=-2/7"
run 2 --fibre 1/5 --point 1,0 --B0 5/3 --json $J --label "AXIS b3=1 gauge B0=5/3"
run 2 --fibre 1/5 --point 2,3 --json $J --label "generic"
run 2 --fibre 1/5 --point -5/2,1/3 --json $J --label "generic"
run 2 --fibre 1/5 --point 0,1 --json $J --label "b4-axis"
run 2 --fibre 2/5 --point 1,0 --json $J --label "AXIS on y=2/5 (not a cone point)"
run 2 --fibre 2/5 --point 2,3 --json $J --label "generic y=2/5"
run 2 --fibre 2/5 --point 0,0 --json $J --label "ORIGIN y=2/5"
run 2 --fibre 1/5 --point 0,0 --json $J --label "ORIGIN y=1/5"
python3 - <<'PY' > roots.txt
for t,p in ((3,32003),(4,32029),(5,32009),(6,32003)):
    q=2*t+1
    r=[y for y in range(p) if (12*q*q*y*y-12*q*(t+1)*y+(t+1)*(3*t+2))%p==0]
    print(t,p,r)
PY
cat roots.txt
while read t p r; do
  r1=$(echo "$r" | tr -d '[],' | awk '{print $1}')
  run $t --modp $p --fibre $r1 --seed 7 --label "mod $p root $r1 random point"
  run $t --modp $p --fibre $r1 --point $(python3 -c "print(','.join(['0']*$t))") --label "ORIGIN mod $p"
done < <(sed 's/\[//; s/\]//; s/,/ /g' roots.txt | awk '{print $1, $2, $3}')
