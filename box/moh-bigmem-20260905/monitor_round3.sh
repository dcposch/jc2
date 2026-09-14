#!/usr/bin/env bash
# Round-3 local polling supervisor.  It only pulls artifacts from the eight
# explicitly charged workers; stopping and termination remain a manual hard-stop
# action after inspection of the 16:50Z state.
set -u

ROOT=/home/ubuntu/jc2/box/moh-bigmem-20260905
LOG="$ROOT/harvest/monitor-round3.log"
IPS=(
  172.30.0.108 172.30.0.183 172.30.0.190 172.30.0.202
  172.30.0.121 172.30.0.125 172.30.0.45 172.30.0.55
)
NEXT=$(date -u -d '2026-09-05T15:02:47Z' +%s)
LAST=$(date -u -d '2026-09-05T16:42:47Z' +%s)

printf 'MONITOR_START utc=%s next=%s last=%s\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$NEXT" "$LAST" | tee -a "$LOG"

while (( NEXT <= LAST )); do
  now=$(date -u +%s)
  while (( now < NEXT )); do
    remain=$((NEXT-now))
    (( remain > 30 )) && remain=30
    sleep "$remain"
    now=$(date -u +%s)
  done

  stamp=$(date -u +%H%M)
  printf 'POLL_START stamp=t%s utc=%s\n' "$stamp" \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG"
  failures=0
  pids=()
  for ip in "${IPS[@]}"; do
    bash "$ROOT/harvest_one.sh" "$ip" "$stamp" \
      >"/tmp/moh-round3-${stamp}-${ip##*.}.out" 2>&1 &
    pids+=("$!")
  done
  for pid in "${pids[@]}"; do
    wait "$pid" || failures=$((failures+1))
  done
  files=$(find "$ROOT/harvest/t$stamp" -type f 2>/dev/null | wc -l)
  printf 'POLL_END stamp=t%s utc=%s failures=%s files=%s\n' "$stamp" \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$failures" "$files" | tee -a "$LOG"
  NEXT=$((NEXT+600))
done

printf 'MONITOR_REGULAR_POLLS_DONE utc=%s\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG"
