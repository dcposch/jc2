#!/bin/bash
# mkbatch.sh <outfile> <tier:P|S> <K b pin> ...   -> per-worker detached batch launcher
OUT=$1; TIER=$2; shift 2
D=/home/ubuntu/jc2/box/k4ray-strata-r2-20260905
{
echo '#!/bin/bash'
echo "mkdir -p $D/msolve $D/logs"
while [ $# -ge 3 ]; do
  K=$1; B=$2; P=$3; shift 3
  ST="K${K}_B${B}_Q${P}"
  if [ "$TIER" = P ]; then
    # 400 GB address space, 32 msolve threads, 85-min formation cap, 45-min msolve cap
    echo "( ulimit -v 419430400; setsid nohup timeout 9600 python3 -u $D/r2_solve.py $K $B --pin-index $P --threads 32 --form-timeout 5100 --msolve-timeout 2700 --outdir $D/msolve > $D/logs/${ST}.log 2>&1 ) </dev/null >/dev/null 2>&1 &"
  else
    # known formation-bound in round 1: re-confirmation only, niced, 40 GB cap
    echo "( ulimit -v 41943040; setsid nohup nice -n 19 timeout 9600 python3 -u $D/r2_solve.py $K $B --pin-index $P --threads 8 --form-timeout 8000 --msolve-timeout 1200 --outdir $D/msolve > $D/logs/${ST}.log 2>&1 ) </dev/null >/dev/null 2>&1 &"
  fi
  echo "echo LAUNCHED ${ST} ${TIER}"
  echo "sleep 0.3"
done
echo 'echo BATCH_DONE'
} > "$OUT"
chmod +x "$OUT"
