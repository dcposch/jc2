#!/bin/bash
set -euo pipefail

ROOT=/home/ubuntu/jc2
LANE="$ROOT/box/k8-b11-q1-20260905"
RES="$LANE/results"
QIN="$LANE/run-input/K8_B11_Q1_p0.ms"
IN="$LANE/run-input/K8_B11_Q1_p32003.ms"
OUT="$RES/mod32003.msout"
EXPECTED_Q_SHA=66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb
EXPECTED_SHA=bdcde96858f3a16c32f8bf9af405c64fbadcb743a1a67ee8f1f568e17fce7c23
WATCHDOG_FILE="$LANE/run-input/mod32003.watchdog_seconds"
WATCHDOG_SECONDS=2400

if [ -s "$WATCHDOG_FILE" ]; then
  IFS= read -r WATCHDOG_SECONDS < "$WATCHDOG_FILE"
fi
case "$WATCHDOG_SECONDS" in
  ''|*[!0-9]*) echo "INVALID_MOD_WATCHDOG seconds=$WATCHDOG_SECONDS"; exit 64 ;;
esac
if [ "$WATCHDOG_SECONDS" -lt 1 ] || [ "$WATCHDOG_SECONDS" -gt 2400 ]; then
  echo "INVALID_MOD_WATCHDOG seconds=$WATCHDOG_SECONDS"
  exit 64
fi

mkdir -p "$RES" "$(dirname "$IN")"
test -s "$RES/exact_q.rc"
if pgrep -u ubuntu -x msolve >/dev/null || pgrep -u ubuntu -x Singular >/dev/null; then
  echo "REFUSE_NONEXCLUSIVE_MODULAR_RUN"
  ps -fu ubuntu
  exit 70
fi
qsha=$(sha256sum "$QIN" | awk '{print $1}')
if [ "$qsha" != "$EXPECTED_Q_SHA" ]; then
  echo "Q_INPUT_CUSTODY_MISMATCH sha=$qsha"
  exit 86
fi
awk 'NR==2 {$0="32003"} {print}' "$QIN" > "$IN.tmp"
mv "$IN.tmp" "$IN"
sha=$(sha256sum "$IN" | awk '{print $1}')
nvars=$(awk 'NR==1 {print split($0,a,","); exit}' "$IN")
ngens=$(awk 'END {print NR-2}' "$IN")
char=$(sed -n '2p' "$IN")
bytes=$(stat -c %s "$IN")
if [ "$sha" != "$EXPECTED_SHA" ] || [ "$nvars" != 97 ] || [ "$ngens" != 330 ] || \
   [ "$char" != 32003 ] || [ "$bytes" != 65003249 ]; then
  echo "MOD_INPUT_CUSTODY_MISMATCH sha=$sha variables=$nvars generators=$ngens char=$char bytes=$bytes"
  exit 86
fi

date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$RES/mod32003.start_utc"
date +%s%N > "$RES/mod32003.start_ns"
{
  printf 'host=%s\n' "$(hostname)"
  printf 'nproc=%s\n' "$(nproc)"
  printf 'source_q_sha256=%s\n' "$qsha"
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
  printf 'watchdog_seconds=%s\n' "$WATCHDOG_SECONDS"
} > "$RES/mod32003.custody"

set +e
/usr/bin/time -v -o "$RES/mod32003.time" \
  timeout --signal=TERM --kill-after=30s "${WATCHDOG_SECONDS}s" \
  stdbuf -oL -eL /usr/local/bin/msolve -g 2 -t 64 -v 2 --random-seed 0 -f "$IN" -o "$OUT" \
    > "$RES/mod32003.stdout" 2> "$RES/mod32003.v2.log"
rc=$?
set -e
date +%s%N > "$RES/mod32003.end_ns"
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$RES/mod32003.end_utc"
if [ -f "$OUT" ]; then
  sha256sum "$OUT" > "$RES/mod32003.output.sha256"
  stat -c '%s' "$OUT" > "$RES/mod32003.output.bytes"
fi
printf '%s\n' "$rc" > "$RES/mod32003.rc.tmp"
mv "$RES/mod32003.rc.tmp" "$RES/mod32003.rc"
echo "MOD32003_DONE rc=$rc"
exit "$rc"
