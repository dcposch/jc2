#!/bin/bash
# usage: run_job.sh <timeout_s> <tag> <t> <kind> [label rows]
D=/home/ubuntu/jc2/box/k16sq-20260905
to=$1; tag=$2; t=$3; kind=$4; label=$5; rows=$6
name=${tag}_${kind}${label:+_$label}
python3 $D/emit_analysis.py $kind $tag $t $label $rows > $D/$name.sing
/usr/bin/time -f "WALL %e s MAXRSS %M KB" -o $D/$name.time timeout $to stdbuf -oL Singular -q $D/$name.sing > $D/$name.out 2>&1
echo "exit=$?" >> $D/$name.out
