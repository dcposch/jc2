#!/bin/bash
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
for i in $(seq 2 20); do
  sleep 600
  n=$(printf "%02d" $i)
  bash $D/collect.sh 2>/dev/null | sort > $D/status-$n.tsv
  date -u +"POLL $n %H:%M:%SZ" >> $D/poll.log
  awk -F'\t' '{m[$3]++; q[$9]++} END{printf "  MOD:"; for(k in m) printf " %s=%d",k,m[k]; printf "  |  Q:"; for(k in q) printf " %s=%d",k,q[k]; print ""}' $D/status-$n.tsv >> $D/poll.log
done
echo POLL_LOOP_DONE >> $D/poll.log
