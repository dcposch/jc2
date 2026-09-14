#!/usr/bin/env bash
# Custody-preserving msolve 0.10.1 -g 2 job with 3h watchdog and RSS log.
# Usage: run_msolve_job.sh WORKDIR META ROWS CHAR TIMEOUT_S THREADS [extra msolve flags]
# Official 0.10.1 binary via $MSOLVE (default ~/moh-bigmem-20260905/bin/msolve).
# No tight ulimit -v: prior gate alloc-failures used 8–48 GiB caps.
set -u
if [[ $# -lt 6 ]]; then
  echo "usage: $0 WORKDIR META ROWS CHAR TIMEOUT_S THREADS [extra msolve flags...]" >&2
  exit 2
fi
WORKDIR=$1; META=$2; ROWS=$3; CHAR=$4; LIMIT=$5; THREADS=$6
shift 6
mkdir -p "$WORKDIR"
STEM=$(basename "$WORKDIR")
ROOT=${ROOT:-$HOME/moh-bigmem-20260905}
MSOLVE=${MSOLVE:-"$ROOT/bin/msolve"}
CHART=${CHART:-"$ROOT/msolve_chart.py"}
PYTHON=${PYTHON:-python3}
INPUT="$WORKDIR/${STEM}_p${CHAR}.ms"
MANIFEST="$WORKDIR/${STEM}_p${CHAR}.manifest.json"
EMITJSON="$WORKDIR/${STEM}_p${CHAR}.emit.json"
OUT="$WORKDIR/${STEM}_p${CHAR}.g2.out"
STDOUT="$WORKDIR/${STEM}_p${CHAR}.g2.stdout"
STDERR="$WORKDIR/${STEM}_p${CHAR}.g2.stderr"
RCFILE="$WORKDIR/${STEM}_p${CHAR}.g2.rc"
METAFILE="$WORKDIR/${STEM}_p${CHAR}.g2.meta"
RSS="$WORKDIR/${STEM}_p${CHAR}.rss.log"
STATUS="$WORKDIR/${STEM}_p${CHAR}.status.json"
SAMPLER_PIDFILE="$WORKDIR/${STEM}_p${CHAR}.sampler.pid"

echo "JOB_START stem=$STEM char=$CHAR timeout=$LIMIT threads=$THREADS utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname) nproc=$(nproc) mem=$(awk '/MemTotal/{print $2}' /proc/meminfo)kB"
echo "rows=$(sha256sum "$ROWS")"
echo "meta=$(sha256sum "$META")"
echo "msolve_bin=$(sha256sum "$MSOLVE")"
"$MSOLVE" -V || true

if [[ ! -s "$INPUT" ]]; then
  echo "EMIT_START utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  "$PYTHON" "$CHART" emit \
    --meta "$META" --rows "$ROWS" \
    --characteristic "$CHAR" --source-characteristic 0 \
    --order-mode source \
    --output "$INPUT" --manifest "$MANIFEST" --json-output "$EMITJSON"
  erc=$?
  echo "EMIT_RC=$erc utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  if [[ $erc -ne 0 ]]; then
    echo "EMIT_FAIL"
    echo "$erc" > "$RCFILE"
    exit $erc
  fi
fi
echo "input=$(sha256sum "$INPUT") bytes=$(stat -c %s "$INPUT")"

{
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "host=$(hostname)"
  echo "input=$INPUT"
  echo "input_sha256=$(sha256sum "$INPUT" | awk '{print $1}')"
  echo "timeout_seconds=$LIMIT"
  echo "threads=$THREADS"
  echo "characteristic=$CHAR"
  printf 'extra_args='
  printf '%q ' "$@"
  printf '\n'
  echo "msolve=$MSOLVE"
  echo "msolve_sha256=$(sha256sum "$MSOLVE" | awk '{print $1}')"
} > "$METAFILE"

: > "$RSS"
(
  while true; do
    pid=$(pgrep -n -x msolve 2>/dev/null || true)
    echo "utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) msolve_pid=${pid:-none}" >> "$RSS"
    if [[ -n "${pid:-}" && -r /proc/$pid/status ]]; then
      awk '/VmPeak|VmSize|VmHWM|VmRSS/' /proc/$pid/status >> "$RSS"
    fi
    sleep 20
  done
) &
SPID=$!
echo "$SPID" > "$SAMPLER_PIDFILE"

# Soft ceiling leaves OS headroom; NOT the 8–48 GiB gate that caused rc139.
ulimit -v 700000000 2>/dev/null || true

timeout --signal=TERM --kill-after=60s "${LIMIT}s" \
  /usr/bin/time -v "$MSOLVE" -g 2 -t "$THREADS" -v 2 "$@" -f "$INPUT" -o "$OUT" \
  > "$STDOUT" 2> "$STDERR"
rc=$?
kill "$SPID" 2>/dev/null || true
wait "$SPID" 2>/dev/null || true
echo "$rc" > "$RCFILE"
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "returncode=$rc"
  if [[ -f "$OUT" ]]; then
    echo "output_bytes=$(stat -c %s "$OUT")"
    echo "output_sha256=$(sha256sum "$OUT" | awk '{print $1}')"
  fi
  echo "rss_samples=$(grep -c '^utc=' "$RSS" || true)"
  echo "max_sampled_VmHWM_KiB=$(awk '/VmHWM:/{print $2}' "$RSS" | sort -n | tail -1)"
} >> "$METAFILE"

echo "SOLVE_RC=$rc utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"$PYTHON" "$CHART" status \
  --output "$OUT" --stderr "$STDERR" --rc-file "$RCFILE" \
  --manifest "$MANIFEST" --json-output "$STATUS" || true
if [[ -f "$STATUS" ]]; then
  echo -n "PARSED_STATUS "
  "$PYTHON" -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("status"), "unit=", d.get("unit_ideal"), "certainty=", d.get("certainty"), "rc=", d.get("returncode"))' "$STATUS"
fi
echo "JOB_END stem=$STEM rc=$rc"
exit $rc
