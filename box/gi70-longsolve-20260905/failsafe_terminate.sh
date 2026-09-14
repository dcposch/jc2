#!/usr/bin/env bash
# Exact-instance safety net: collect and terminate after all 170-minute inner
# guards have had their 60-second kill grace.  A prior manual termination is a
# clean no-op.  This never addresses any other fleet instance.
set -u
ROOT=/home/ubuntu/jc2
OUT=$ROOT/box/gi70-longsolve-20260905
ID=i-0b29f3356aaf6ef81
TARGET_EPOCH=$(date -u -d '2026-09-05T19:54:30Z' +%s)
NOW_EPOCH=$(date -u +%s)
DELAY=$((TARGET_EPOCH-NOW_EPOCH))
if (( DELAY > 0 )); then sleep "$DELAY"; fi
STATE=$(aws ec2 describe-instances --region us-east-1 --instance-ids "$ID" \
  --query 'Reservations[0].Instances[0].State.Name' --output text 2>/dev/null || true)
echo "FAILSAFE_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ) state=$STATE"
if [[ $STATE == running ]]; then
  bash "$OUT/collect_worker.sh" || echo "FAILSAFE_COLLECT_FAILED rc=$?"
  bash "$OUT/terminate_worker.sh"
elif [[ $STATE == pending || $STATE == stopping || $STATE == stopped ]]; then
  bash "$OUT/terminate_worker.sh"
else
  echo "FAILSAFE_NOOP state=$STATE"
fi
