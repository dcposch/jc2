#!/bin/bash
set -euo pipefail

ROOT=/home/ubuntu/jc2
LANE="$ROOT/box/k8-b11-q1-20260905"
RES="$LANE/results"
IN="$LANE/run-input/K8_B11_Q1_p0.ms"
OUT="$RES/exact_q.msout"
EXPECTED_SHA=66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb

mkdir -p "$RES"
if pgrep -u ubuntu -x msolve >/dev/null || pgrep -u ubuntu -x Singular >/dev/null; then
  echo "REFUSE_NONEXCLUSIVE_EXACT_RUN"
  ps -fu ubuntu
  exit 70
fi

sha=$(sha256sum "$IN" | awk '{print $1}')
nvars=$(awk 'NR==1 {print split($0,a,","); exit}' "$IN")
ngens=$(awk 'END {print NR-2}' "$IN")
char=$(sed -n '2p' "$IN")
bytes=$(stat -c %s "$IN")
if [ "$sha" != "$EXPECTED_SHA" ] || [ "$nvars" != 97 ] || [ "$ngens" != 330 ] || \
   [ "$char" != 0 ] || [ "$bytes" != 65003245 ]; then
  echo "INPUT_CUSTODY_MISMATCH sha=$sha variables=$nvars generators=$ngens char=$char bytes=$bytes"
  exit 86
fi

date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$RES/exact_q.start_utc"
date +%s%N > "$RES/exact_q.start_ns"
{
  printf 'host=%s\n' "$(hostname)"
  printf 'nproc=%s\n' "$(nproc)"
  printf 'input=%s\n' "$IN"
  printf 'input_sha256=%s\n' "$sha"
  printf 'input_bytes=%s\n' "$bytes"
  printf 'variables=%s\n' "$nvars"
  printf 'generators=%s\n' "$ngens"
  printf 'characteristic=%s\n' "$char"
  printf 'msolve_path=/usr/local/bin/msolve\n'
  printf 'msolve_sha256=%s\n' "$(sha256sum /usr/local/bin/msolve | awk '{print $1}')"
  printf 'msolve_version=%s\n' "$(msolve -h 2>&1 | grep -oE '0\.[0-9]+\.[0-9]+' | head -1)"
  printf 'command=/usr/local/bin/msolve -g 2 -t 64 -v 2 --random-seed 0 -f %s -o %s\n' "$IN" "$OUT"
  printf 'watchdog_seconds=9000\n'
} > "$RES/exact_q.custody"

set +e
/usr/bin/time -v -o "$RES/exact_q.time" \
  timeout --signal=TERM --kill-after=30s 9000s \
  stdbuf -oL -eL /usr/local/bin/msolve -g 2 -t 64 -v 2 --random-seed 0 -f "$IN" -o "$OUT" \
    > "$RES/exact_q.stdout" 2> "$RES/exact_q.v2.log"
rc=$?
set -e
date +%s%N > "$RES/exact_q.end_ns"
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$RES/exact_q.end_utc"
if [ -f "$OUT" ]; then
  sha256sum "$OUT" > "$RES/exact_q.output.sha256"
  stat -c '%s' "$OUT" > "$RES/exact_q.output.bytes"
fi
printf '%s\n' "$rc" > "$RES/exact_q.rc.tmp"
mv "$RES/exact_q.rc.tmp" "$RES/exact_q.rc"
echo "EXACT_Q_DONE rc=$rc"
exit "$rc"
