#!/usr/bin/env bash
set -euo pipefail
ROOT=/home/ubuntu/jc2
OUT=$ROOT/box/gi70-longsolve-20260905
ID=i-0b29f3356aaf6ef81

bash "$ROOT/ops/fleet/fleet.sh" term "$ID" | tee "$OUT/custody/termination-request.log"
aws ec2 wait instance-terminated --region us-east-1 --instance-ids "$ID"
aws ec2 describe-instances --region us-east-1 --instance-ids "$ID" \
  --query 'Reservations[0].Instances[0].{ID:InstanceId,State:State.Name,Type:InstanceType,Launch:LaunchTime,PrivateIp:PrivateIpAddress,Owner:Tags[?Key==`Owner`]|[0].Value}' \
  --output json | tee "$OUT/custody/instance-final.json"
test "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["State"])' "$OUT/custody/instance-final.json")" = terminated
