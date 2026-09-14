#!/bin/bash
# Wake on terminal markers in full-order logs. Silent until DONE/FAILED/ACTION.
# Args: none. Polls local + fleet logs.
set -euo pipefail
ROOT=/home/ubuntu/jc2/box/moh14-charts-20260905
KEY=~/.ssh/jc2-fleet
SSH="ssh -i $KEY -o StrictHostKeyChecking=no -o ConnectTimeout=8"
hosts=(172.30.0.7 172.30.0.18 172.30.0.28 172.30.0.166 172.30.0.254)

collect() {
  echo "===== LOCAL $(date -u +%H:%M:%S) ====="
  for f in "$ROOT"/logs/*.log; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    if grep -qE 'MS_VERDICT|ZS_VERDICT|PP_VERDICT|NATIVE_DONE|POINT_PASS' "$f" 2>/dev/null; then
      echo "TERM $base: $(grep -E 'MS_VERDICT|ZS_VERDICT|PP_VERDICT|NATIVE_DONE|POINT_PASS|MS_DIM|ZS_DIM|MS_FULL' "$f" | tail -5 | tr '\n' ' | ')"
    fi
  done
  # local singular still running?
  nloc=$(pgrep -c Singular || true)
  echo "local_singular=$nloc"
  for ip in "${hosts[@]}"; do
    echo "===== $ip ====="
    $SSH ubuntu@$ip 'n=$(pgrep -c Singular || echo 0); echo singular=$n;
      ps -o pid,etime,rss,cmd -C Singular --no-headers 2>/dev/null | awk "{printf \"  %s rss_kb=%s %s\n\", \$2,\$3,\$4}";
      for f in /home/ubuntu/jc2/box/moh14-charts-20260905/logs/*.log; do
        [ -f "$f" ] || continue
        if grep -qE "MS_VERDICT|ZS_VERDICT|PP_VERDICT|NATIVE_DONE|POINT_PASS" "$f" 2>/dev/null; then
          echo "TERM $(basename $f): $(grep -E "MS_VERDICT|ZS_VERDICT|PP_VERDICT|NATIVE_DONE|POINT_PASS|MS_DIM|MS_FULL" "$f" | tail -4 | tr "\n" " | ")"
        fi
      done
      for f in /home/ubuntu/jc2/box/moh14-charts-20260905/classes/*/builders/*.out; do
        [ -f "$f" ] || continue
        if grep -q NATIVE_DONE "$f" 2>/dev/null; then
          echo "EXTRACT $(basename $f): $(grep NATIVE_ "$f" | tr "\n" " | ")"
        fi
      done
    ' 2>/dev/null || echo "ssh_fail $ip"
  done
}

# One-shot status to stdout of this script (used by the first call).
# The monitor loop only prints DONE/FAILED/ACTION.
collect > /tmp/fo_watch_status.txt
# Terminal if ALL of: mm15 unbounded verdict AND mm12 unbounded verdict
# OR any FAILED (timeout kill without verdict after timeout wrapper exit)
mm15u=$(grep -l 'MS_VERDICT' "$ROOT"/logs/mm15_u32003.log 2>/dev/null || true)
# keep looping in monitor mode:
prev=""
while :; do
  collect > /tmp/fo_watch_status.txt
  # local mm15/mm12 unbounded
  v15=""; v12=""; fail=""
  grep -q 'MS_VERDICT' "$ROOT"/logs/mm15_u32003.log 2>/dev/null && v15=$(grep MS_VERDICT "$ROOT"/logs/mm15_u32003.log | tail -1)
  # fleet mm12
  :
  # count TERM lines
  nterm=$(grep -c '^TERM ' /tmp/fo_watch_status.txt || true)
  nsing=$(grep -c singular= /tmp/fo_watch_status.txt || true)
  sig=$(md5sum /tmp/fo_watch_status.txt | awk '{print $1}')
  # wake if a NEW terminal marker appeared
  if grep -qE 'MS_VERDICT UNIT|POINT_PASS|NATIVE_DONE equations=' /tmp/fo_watch_status.txt; then
    if [ "$sig" != "$prev" ]; then
      echo "ACTION_REQUIRED: new terminal marker"
      grep -E '^TERM |^EXTRACT |MS_VERDICT|POINT_PASS|NATIVE_DONE' /tmp/fo_watch_status.txt | head -40
      prev=$sig
    fi
  fi
  # all local timeout wrappers dead AND no verdict on mm15 u -> failed
  if ! pgrep -f 'fo_u32003.sing' >/dev/null 2>&1; then
    if [ -f "$ROOT"/logs/mm15_u32003.log ] && ! grep -q MS_VERDICT "$ROOT"/logs/mm15_u32003.log; then
      # still running on fleet maybe; only fail local mm15 if log has no start
      :
    fi
  fi
  sleep 30
done
