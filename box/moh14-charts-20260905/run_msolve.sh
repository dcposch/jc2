#!/usr/bin/env bash
# Durable msolve -g 2 launcher.
# Usage: run_msolve.sh INPUT.ms TIMEOUT_S THREADS [extra msolve flags...]
set -u
if [[ $# -lt 3 ]]; then
  echo "usage: $0 INPUT.ms TIMEOUT_S THREADS [extra msolve flags...]" >&2
  exit 2
fi
input=$1
limit=$2
threads=$3
shift 3
base=${input%.ms}
out=${base}.g2.out
err=${base}.g2.stderr
rcfile=${base}.g2.rc
metafile=${base}.g2.meta
{
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "host=$(hostname)"
  echo "input=$input"
  echo "input_sha256=$(sha256sum "$input" | awk '{print $1}')"
  echo "timeout_seconds=$limit"
  echo "threads=$threads"
  printf 'extra_args='
  printf '%q ' "$@"
  printf '\n'
  echo "msolve=$(command -v msolve)"
  echo "msolve_sha256=$(sha256sum "$(command -v msolve)" | awk '{print $1}')"
} > "$metafile"
timeout --signal=TERM --kill-after=30s "${limit}s" \
  /usr/bin/time -v msolve -g 2 -t "$threads" -v 2 "$@" -f "$input" -o "$out" \
  > "${base}.g2.stdout" 2> "$err"
rc=$?
echo "$rc" > "$rcfile"
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "returncode=$rc"
  if [[ -f "$out" ]]; then
    echo "output_bytes=$(stat -c %s "$out")"
    echo "output_sha256=$(sha256sum "$out" | awk '{print $1}')"
  fi
} >> "$metafile"
exit "$rc"
