#!/usr/bin/env bash
# Collect the two completed jobs, terminate the one authorized worker, then hash.
set -euo pipefail

ROOT=/home/ubuntu/jc2
LANE="$ROOT/box/k8-b11-q1-20260905"
FLEET="$ROOT/ops/fleet/fleet.sh"
IP=172.30.0.97
INSTANCE_ID=i-06d4a0da61650ede5
REMOTE="$ROOT/box/k8-b11-q1-20260905"
DEST="$LANE/fleet/$INSTANCE_ID"
Q_SHA=66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb
P_SHA=bdcde96858f3a16c32f8bf9af405c64fbadcb743a1a67ee8f1f568e17fce7c23

mkdir -p "$DEST/results" "$DEST/dispatch" "$LANE/input"

# Do not destroy the worker unless both sequential jobs have sealed their rc.
bash "$FLEET" run "$IP" '
  set -eu
  R=/home/ubuntu/jc2/box/k8-b11-q1-20260905/results
  test -s "$R/exact_q.rc" && test -s "$R/mod32003.rc"
  m=$(pgrep -c -u ubuntu -x msolve || true)
  s=$(pgrep -c -u ubuntu -x Singular || true)
  date -u +final_idle_utc=%Y-%m-%dT%H:%M:%SZ
  printf "exact_rc=%s\nmod32003_rc=%s\nCAS_PROCESSES=%s\n" \
    "$(cat "$R/exact_q.rc")" "$(cat "$R/mod32003.rc")" "$((m+s))"
  test "$((m+s))" -eq 0
' | tee "$LANE/custody/final-worker-idle.txt"

bash "$FLEET" pull "$IP" "$REMOTE/results/" "$DEST/results/"
bash "$FLEET" pull "$IP" "$REMOTE/run-input/K8_B11_Q1_p32003.ms" \
  "$LANE/input/K8_B11_Q1_p32003.ms"
bash "$FLEET" pull "$IP" "$REMOTE/run-input/mod32003.watchdog_seconds" \
  "$DEST/mod32003.watchdog_seconds"
bash "$FLEET" pull "$IP" /home/ubuntu/exact_q.log "$DEST/dispatch/exact_q.log"
bash "$FLEET" pull "$IP" /home/ubuntu/mod32003.log "$DEST/dispatch/mod32003.log"

test "$(sha256sum "$LANE/input/K8_B11_Q1_p0.ms" | awk '{print $1}')" = "$Q_SHA"
test "$(sha256sum "$LANE/input/K8_B11_Q1_p32003.ms" | awk '{print $1}')" = "$P_SHA"
cmp -s "$LANE/input/mod32003.watchdog_seconds" "$DEST/mod32003.watchdog_seconds"
test -s "$DEST/results/exact_q.rc"
test -s "$DEST/results/mod32003.rc"
for stem in exact_q mod32003; do
  for suffix in custody time v2.log start_ns start_utc end_ns end_utc rc stdout; do
    test -f "$DEST/results/$stem.$suffix"
  done
done
exact_end_ns=$(<"$DEST/results/exact_q.end_ns")
mod_start_ns=$(<"$DEST/results/mod32003.start_ns")
test "$exact_end_ns" -lt "$mod_start_ns"
printf 'exact_end_ns=%s\nmod_start_ns=%s\nstrictly_sequential=1\n' \
  "$exact_end_ns" "$mod_start_ns" > "$LANE/custody/sequential-jobs.txt"

{
  for stem in exact_q mod32003; do
    sum="$DEST/results/$stem.output.sha256"
    out="$DEST/results/$stem.msout"
    if [ -s "$sum" ]; then
      expected=$(awk 'NR==1 {print $1}' "$sum")
      actual=$(sha256sum "$out" | awk '{print $1}')
      expected_bytes=$(<"$DEST/results/$stem.output.bytes")
      actual_bytes=$(stat -c %s "$out")
      test "$actual" = "$expected"
      test "$actual_bytes" = "$expected_bytes"
      printf '%s output_present=1 expected=%s actual=%s bytes=%s match=1\n' \
        "$stem" "$expected" "$actual" "$actual_bytes"
    else
      test ! -e "$out"
      printf '%s output_present=0 checksum_present=0\n' "$stem"
    fi
  done
} > "$LANE/custody/pulled-output-verification.txt"

{
  date -u +termination_request_utc=%Y-%m-%dT%H:%M:%SZ
  bash "$FLEET" term "$INSTANCE_ID"
  aws ec2 wait instance-terminated --region us-east-1 --instance-ids "$INSTANCE_ID"
  date -u +termination_confirmed_utc=%Y-%m-%dT%H:%M:%SZ
  aws ec2 describe-instances --region us-east-1 --instance-ids "$INSTANCE_ID" \
    --query 'Reservations[0].Instances[0].{ID:InstanceId,State:State.Name,IP:PrivateIpAddress,Type:InstanceType,Owner:Tags[?Key==`Owner`]|[0].Value}' \
    --output json
} | tee "$LANE/custody/worker-termination.log"
grep -q '"State": "terminated"' "$LANE/custody/worker-termination.log"

PYTHONDONTWRITEBYTECODE=1 python3 "$LANE/summarize_results.py" \
  "$DEST/results" "$LANE/custody/results-summary.json" exact_q mod32003 \
  > "$LANE/custody/results-summary.stdout"
PYTHONDONTWRITEBYTECODE=1 python3 "$LANE/source/lane_eta.py" \
  --status "$DEST/results/exact_q.v2.log" \
  > "$LANE/custody/exact-final-eta.txt" || true
PYTHONDONTWRITEBYTECODE=1 python3 "$LANE/source/lane_eta.py" \
  --status "$DEST/results/mod32003.v2.log" \
  > "$LANE/custody/mod32003-final-eta.txt" || true

bash "$LANE/make_artifact_manifest.sh"
