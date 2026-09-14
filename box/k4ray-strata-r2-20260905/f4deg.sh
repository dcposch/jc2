#!/bin/bash
# per msolve verbose log: max F4 degree reached, and the largest F4 matrix (rows x cols)
D=/home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve
for f in $D/*.log; do
  [ -e "$f" ] || continue
  grep -aoE '^ *[0-9]+ +[0-9]+ +[0-9]+ +[0-9]+ x [0-9]+' "$f" | \
   awk -v n="$(basename $f .log)" '{if($1>d)d=$1; if($4>r){r=$4;c=$6}} END{printf "%s\t%d\t%d\t%d\n", n, d+0, r+0, c+0}'
done
