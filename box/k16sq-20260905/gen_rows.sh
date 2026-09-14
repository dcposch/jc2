#!/bin/bash
# Regenerate exact terminal rows with Astra's frozen emitter (box/k16astra-20260905/emit_arrays.py).
# usage: gen_rows.sh <tag> <t> [--d +-1]
tag=$1; t=$2; shift 2
D=/home/ubuntu/jc2/box/k16sq-20260905
python3 /home/ubuntu/jc2/box/k16astra-20260905/emit_arrays.py $t "$@" --out $D/${tag}_rows.sing > $D/${tag}_generate.sing
/usr/bin/time -f "WALL %e s  MAXRSS %M KB" -o $D/${tag}_generate.time timeout 3600 stdbuf -oL Singular -q $D/${tag}_generate.sing > $D/${tag}_generate.log 2>&1
echo "exit=$?" >> $D/${tag}_generate.log
tail -3 $D/${tag}_generate.log; cat $D/${tag}_generate.time
