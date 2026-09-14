#!/bin/bash
mkdir -p /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 8 7 --pin-index 0 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K8_B7_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K8_B7_Q0 P
sleep 0.3
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 8 7 --pin-index 1 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K8_B7_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K8_B7_Q1 P
sleep 0.3
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 8 10 --pin-index 0 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K8_B10_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K8_B10_Q0 P
sleep 0.3
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 8 10 --pin-index 1 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K8_B10_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K8_B10_Q1 P
sleep 0.3
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 9 --pin-index 0 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B9_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B9_Q0 P
sleep 0.3
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 9 --pin-index 1 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B9_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B9_Q1 P
sleep 0.3
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 7 6 --pin-index 0 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K7_B6_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K7_B6_Q0 P
sleep 0.3
( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 7 6 --pin-index 1 --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K7_B6_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K7_B6_Q1 P
sleep 0.3
echo BATCH_DONE
