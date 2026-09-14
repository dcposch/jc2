#!/bin/bash
# Poll full-order jobs. Print ACTION_REQUIRED on new terminals; DONE when
# both already-full class unbounded solves have a verdict (or all jobs dead
# after start). FAILED on control-fail or timeout-wrapper death without verdict
# for BOTH already-full classes.
set -euo pipefail
ROOT=/home/ubuntu/jc2/box/moh14-charts-20260905
KEY=~/.ssh/jc2-fleet
SSH="ssh -i $KEY -o StrictHostKeyChecking=no -o ConnectTimeout=6"
STAMP=/tmp/fo_watch.prev
: > /tmp/fo_watch.now

add() { echo "$1" >> /tmp/fo_watch.now; }

# local logs
for f in "$ROOT"/logs/*.log; do
  [ -f "$f" ] || continue
  b=$(basename "$f")
  if grep -qE 'MS_VERDICT|ZS_VERDICT|PP_VERDICT|RP_VERDICT|NATIVE_DONE|POINT_PASS' "$f"; then
    add "LOCAL $b $(grep -E 'MS_VERDICT|ZS_VERDICT|PP_VERDICT|RP_VERDICT|NATIVE_DONE|POINT_PASS|MS_DIM|MS_FULL|ZS_DIM|RP_DIM' "$f" | tail -3 | tr '\n' ';')"
  fi
done
# only live extract logs (ignore stale builders/*.out from the envelope generation)
for f in "$ROOT"/logs/ex_*.log; do
  [ -f "$f" ] || continue
  if grep -q NATIVE_DONE "$f"; then
    add "EXTRACT $(basename "$f") $(grep NATIVE_ "$f" | tr '\n' ';')"
  fi
done

for ip in 172.30.0.7 172.30.0.18 172.30.0.28 172.30.0.166 172.30.0.254; do
  $SSH ubuntu@$ip 'for f in /home/ubuntu/jc2/box/moh14-charts-20260905/logs/*.log; do
      [ -f "$f" ] || continue
      if grep -qE "MS_VERDICT|ZS_VERDICT|PP_VERDICT|NATIVE_DONE|POINT_PASS" "$f" 2>/dev/null; then
        echo "FLEET '"$ip"' $(basename $f) $(grep -E "MS_VERDICT|ZS_VERDICT|PP_VERDICT|NATIVE_DONE|POINT_PASS|MS_DIM|MS_FULL" "$f" | tail -3 | tr "\n" ";")"
      fi
    done
  ' 2>/dev/null >> /tmp/fo_watch.now || add "SSH_FAIL $ip"
done

sort -u /tmp/fo_watch.now -o /tmp/fo_watch.now
new=0
if [ -f "$STAMP" ]; then
  if ! cmp -s /tmp/fo_watch.now "$STAMP"; then
    new=1
  fi
else
  new=1
fi
cp /tmp/fo_watch.now "$STAMP"

has15=$(grep -c 'mm15_u32003.*MS_VERDICT\|mm15_u32051.*MS_VERDICT' /tmp/fo_watch.now || true)
has12=$(grep -c 'mm12_u32003.*MS_VERDICT\|mm12_u32051.*MS_VERDICT' /tmp/fo_watch.now || true)
# also match LOCAL mm15_u32003.log MS_VERDICT
grep -q 'mm15_u32003' /tmp/fo_watch.now && grep -q 'MS_VERDICT' /tmp/fo_watch.now && has15=1 || true
grep -q 'mm12_u32003' /tmp/fo_watch.now && grep -q 'MS_VERDICT' /tmp/fo_watch.now && has12=1 || true

if grep -q CONTROL_EMPTY_FAIL /tmp/fo_watch.now; then
  echo "FAILED: control empty fail"
  cat /tmp/fo_watch.now
  exit 1
fi

if [ "$new" -eq 1 ]; then
  echo "ACTION_REQUIRED: job terminals updated"
  cat /tmp/fo_watch.now
fi

# DONE once both already-full unbounded have some MS_VERDICT somewhere
if grep -q 'mm15_u' /tmp/fo_watch.now && grep -q 'MS_VERDICT' /tmp/fo_watch.now \
   && grep -q 'mm12_u' /tmp/fo_watch.now; then
  # require explicit both
  if grep 'mm15_u' /tmp/fo_watch.now | grep -q MS_VERDICT \
     && grep 'mm12_u' /tmp/fo_watch.now | grep -q MS_VERDICT; then
    echo "DONE: unbounded verdicts for both already-full classes"
    cat /tmp/fo_watch.now
    exit 0
  fi
fi
exit 0
