#!/bin/bash
mkdir -p /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 13 --pin-index 0 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B13_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B13_Q0 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 13 --pin-index 1 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B13_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B13_Q1 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 14 --pin-index 0 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B14_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B14_Q0 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 14 --pin-index 1 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B14_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B14_Q1 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 15 --pin-index 0 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B15_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B15_Q0 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 15 --pin-index 1 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B15_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B15_Q1 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 16 --pin-index 0 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B16_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B16_Q0 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 16 --pin-index 1 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B16_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B16_Q1 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 17 --pin-index 0 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B17_Q0.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B17_Q0 S
sleep 0.3
( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/r2_solve.py 9 17 --pin-index 1 --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve > /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/logs/K9_B17_Q1.log 2>&1 ) </dev/null >/dev/null 2>&1 &
echo LAUNCHED K9_B17_Q1 S
sleep 0.3
echo BATCH_DONE
