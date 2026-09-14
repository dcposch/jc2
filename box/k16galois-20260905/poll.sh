#!/bin/bash
SSH="ssh -n -o BatchMode=yes -o ConnectTimeout=8 -i /home/ubuntu/.ssh/jc2-fleet"; B=/home/ubuntu/jc2/box/k16galois-20260905
sleep ${1:-240}
echo "== $(date -u +%H:%M:%SZ)"
echo "== W28 msolve t8"; timeout 20 $SSH ubuntu@172.30.0.28 "tail -1 $B/msolve_t8.log | cut -c1-100; ps -o etime=,rss= -C msolve | tail -1"
echo "== W7"; timeout 20 $SSH ubuntu@172.30.0.7 "cd $B; cat w7m.log; ls -la msolve_t8_mod_p32003_b0_minors.ms 2>/dev/null | awk '{print \$5}'; tail -1 msolve_t8_minors.log 2>/dev/null | cut -c1-100; grep -h EXACT exactchart_t5_exact.out | tail -1; ps -o etime=,rss=,cmd= -C msolve,Singular | grep -v moh14 | cut -c1-70"
echo "== W18"; timeout 20 $SSH ubuntu@172.30.0.18 "cd $B; grep -h 'MAIN\|COLON' pattern_t8_mod_p32003_b0_dimonly.out colon_t4_exact.out pattern_t7_mod_p32059_b0_dimonly.out 2>/dev/null; grep -h BOUNDARY boundary_t7_mod_p32059_b0.out 2>/dev/null; ps -o etime=,rss=,cmd= -C Singular | grep -v moh14 | cut -c1-70"
echo "== desk t4: $(grep EXACT $B/exactchart_t4_exact.out | tail -1 | cut -c1-40) $(ps -o etime= -p $(pgrep -f '^Singular -q exactchart_t4' | head -1) 2>/dev/null)"
