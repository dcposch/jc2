#!/bin/bash
# usage: run_batch.sh TIMEOUT job1.sing job2.sing ...  (runs <=3 concurrently, foreground, each under timeout)
T=$1; shift
printf "%s\n" "$@" | xargs -P 3 -I{} bash -c 'j={}; b=${j%.sing}; s=$(date +%s); timeout '"$T"' Singular -q "$j" > "$b.out" 2> "$b.err"; rc=$?; e=$(date +%s); echo "$b rc=$rc wall=$((e-s))s" >> batch.log; echo "$b rc=$rc wall=$((e-s))s"'
