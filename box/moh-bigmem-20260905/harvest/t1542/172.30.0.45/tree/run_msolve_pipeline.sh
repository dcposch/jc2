#!/usr/bin/env bash
# Native msolve (char p=1073741827, Tc-1 via msolve_chart) then graph if native
# is not a finished UNIT/NONUNIT verdict. 3h watchdog per invocation.
# Usage: run_msolve_pipeline.sh TARGET_NAME
set -u
ROOT=${ROOT:-$HOME/moh-bigmem-20260905}
TARGET=$1
TDIR="$ROOT/targets/$TARGET"
. "$TDIR/env.sh"
WATCHDOG=${WATCHDOG:-10800}
THREADS=${THREADS:-32}
# Native first.
if [[ -n "${NATIVE_ROWS:-}" && -f "$NATIVE_ROWS" ]]; then
  echo "PIPELINE_NATIVE_START target=$TARGET utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  bash "$ROOT/run_msolve_job.sh" \
    "$TDIR/msolve_native" "$NATIVE_META" "$NATIVE_ROWS" \
    1073741827 "$WATCHDOG" "$THREADS" -l 44
  nrc=$?
  echo "PIPELINE_NATIVE_RC=$nrc"
  STATUS=$(ls "$TDIR/msolve_native/"*.status.json 2>/dev/null | head -1 || true)
  parsed=""
  if [[ -n "$STATUS" ]]; then
    parsed=$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("status"), d.get("unit_ideal"))' "$STATUS" 2>/dev/null || true)
  fi
  echo "PIPELINE_NATIVE_PARSED=$parsed"
  case "$parsed" in
    "UNIT True"|"NONUNIT False")
      echo "PIPELINE_NATIVE_HAS_VERDICT; skip graph unless UNIT needs exact-Q"
      if [[ "$parsed" == "UNIT True" ]]; then
        echo "PIPELINE_MODULAR_UNIT_SIGNAL exact-Q confirmation on identical generators"
        python3 "$ROOT/run_guided_job.py" \
          --workdir "$TDIR/exactq_after_msolve_unit" \
          --meta "$NATIVE_META" --rows "$NATIVE_ROWS" \
          --name "${TARGET}_native_exactq" \
          --primes "" --timeout "$WATCHDOG" --cpus 32 || true
      fi
      echo "PIPELINE_DONE native-verdict utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
      exit 0
      ;;
  esac
else
  echo "PIPELINE_NO_NATIVE_ROWS"
  nrc=2
fi

# Graph presentation if present and native did not yield a basis verdict.
if [[ -n "${GRAPH_ROWS:-}" && -f "$GRAPH_ROWS" ]]; then
  echo "PIPELINE_GRAPH_START target=$TARGET utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  bash "$ROOT/run_msolve_job.sh" \
    "$TDIR/msolve_graph" "$GRAPH_META" "$GRAPH_ROWS" \
    1073741827 "$WATCHDOG" "$THREADS" -l 44
  grc=$?
  echo "PIPELINE_GRAPH_RC=$grc"
  GSTATUS=$(ls "$TDIR/msolve_graph/"*.status.json 2>/dev/null | head -1 || true)
  if [[ -n "$GSTATUS" ]]; then
    gparsed=$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("status"), d.get("unit_ideal"))' "$GSTATUS" 2>/dev/null || true)
    echo "PIPELINE_GRAPH_PARSED=$gparsed"
    if [[ "$gparsed" == "UNIT True" ]]; then
      echo "PIPELINE_GRAPH_MODULAR_UNIT_SIGNAL exact-Q confirmation"
      python3 "$ROOT/run_guided_job.py" \
        --workdir "$TDIR/exactq_after_graph_unit" \
        --meta "$GRAPH_META" --rows "$GRAPH_ROWS" \
        --name "${TARGET}_graph_exactq" \
        --primes "" --timeout "$WATCHDOG" --cpus 32 || true
    fi
  fi
else
  echo "PIPELINE_NO_GRAPH_ROWS"
fi
echo "PIPELINE_END utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
