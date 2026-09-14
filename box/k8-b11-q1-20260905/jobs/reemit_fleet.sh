#!/bin/bash
set -euo pipefail

ROOT=/home/ubuntu/jc2
LANE="$ROOT/box/k8-b11-q1-20260905"
OUT="$LANE/reemit"
RES="$LANE/results"
EXPECTED_SHA=66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb
EXPECTED_MOD_SHA=bdcde96858f3a16c32f8bf9af405c64fbadcb743a1a67ee8f1f568e17fce7c23

mkdir -p "$OUT" "$RES"
if pgrep -u ubuntu -x msolve >/dev/null || pgrep -u ubuntu -x Singular >/dev/null; then
  echo "REFUSE_NONEXCLUSIVE_REEMIT"
  ps -fu ubuntu
  exit 70
fi

date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$RES/reemit.start_utc"
date +%s%N > "$RES/reemit.start_ns"
set +e
/usr/bin/time -v -o "$RES/reemit.time" \
  timeout --signal=TERM --kill-after=30s 5700s \
  python3 -u "$ROOT/box/k4ray-strata-r2-20260905/r2_solve.py" \
    8 11 --pin-index 1 --threads 64 --form-timeout 5400 --no-run --outdir "$OUT" \
    > "$RES/reemit.stdout" 2> "$RES/reemit.stderr"
rc=$?
set -e
date +%s%N > "$RES/reemit.end_ns"
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$RES/reemit.end_utc"

qfile="$OUT/K8_B11_Q1_p0.ms"
pfile="$OUT/K8_B11_Q1_p32003.ms"
if [ "$rc" -eq 0 ] && [ -s "$qfile" ] && [ -s "$pfile" ]; then
  qsha=$(sha256sum "$qfile" | awk '{print $1}')
  psha=$(sha256sum "$pfile" | awk '{print $1}')
  nvars=$(awk 'NR==1 {print split($0,a,","); exit}' "$qfile")
  ngens=$(awk 'END {print NR-2}' "$qfile")
  char=$(sed -n '2p' "$qfile")
  bytes=$(stat -c %s "$qfile")
  {
    printf 'input=%s\n' "$qfile"
    printf 'sha256=%s\n' "$qsha"
    printf 'expected_sha256=%s\n' "$EXPECTED_SHA"
    printf 'mod_sha256=%s\n' "$psha"
    printf 'expected_mod_sha256=%s\n' "$EXPECTED_MOD_SHA"
    printf 'bytes=%s\n' "$bytes"
    printf 'variables=%s\n' "$nvars"
    printf 'generators=%s\n' "$ngens"
    printf 'characteristic=%s\n' "$char"
  } > "$RES/reemit.custody"
  if [ "$qsha" != "$EXPECTED_SHA" ] || [ "$psha" != "$EXPECTED_MOD_SHA" ] || \
     [ "$bytes" != 65003245 ] || [ "$nvars" != 97 ] || [ "$ngens" != 330 ] || \
     [ "$char" != 0 ]; then
    echo "REEMIT_CUSTODY_MISMATCH"
    rc=86
  else
    echo "REEMIT_CUSTODY_OK sha256=$qsha variables=$nvars generators=$ngens bytes=$bytes"
  fi
fi

printf '%s\n' "$rc" > "$RES/reemit.rc.tmp"
mv "$RES/reemit.rc.tmp" "$RES/reemit.rc"
exit "$rc"
