#!/usr/bin/env bash
# Bounded no-CAS regression for the worker process-group safety contract.

set -euo pipefail

target_dir=$(cd "$(dirname "$0")" && pwd -P)
# shellcheck source=process_group_guard.sh
source "$target_dir/process_group_guard.sh"

if [[ "${1:-}" == --dummy-worker ]]; then
  [[ "$#" == 3 && "$2" == /tmp/tail3-pgid-regression.* \
      && "$3" == "$2/"* ]]
  probe_dir=$2
  probe_token=$3
  exec /usr/bin/time -v \
    timeout --foreground --signal=TERM --kill-after=2s 10s \
      prlimit --as=134217728 --cpu=10 -- \
        python3 -c \
          'import time; payload=bytearray(32*1024*1024); time.sleep(10)' \
          "$probe_token"
fi
[[ "$#" == 0 ]]

probe_dir=$(mktemp -d /tmp/tail3-pgid-regression.XXXXXX)
probe_token=$probe_dir/dummy.token
worker_pid=""
worker_sid=""
worker_pgid=""

session_non_zombie_count() {
  [[ "$worker_sid" =~ ^[0-9]+$ ]] || { echo 0; return; }
  ps -eo sid=,state= | awk -v wanted="$worker_sid" \
    '$1==wanted && $2 !~ /^Z/ {count++} END {print count+0}'
}

session_pgids() {
  [[ "$worker_sid" =~ ^[0-9]+$ ]] || return
  ps -eo pgid=,sid=,state= | awk -v wanted="$worker_sid" \
    '$2==wanted && $3 !~ /^Z/ {print $1}' | sort -nu
}

cleanup() {
  local pgid second
  for pgid in $(session_pgids); do
    if tail3_validate_group "$probe_dir" "$pgid"; then
      tail3_signal_group "$probe_dir" "$pgid" TERM || true
    fi
  done
  for second in $(seq 1 30); do
    (( $(session_non_zombie_count) == 0 )) && break
    sleep 0.1
  done
  for pgid in $(session_pgids); do
    if tail3_validate_group "$probe_dir" "$pgid"; then
      tail3_signal_group "$probe_dir" "$pgid" KILL || true
    fi
  done
  if [[ "$worker_pid" =~ ^[0-9]+$ ]]; then
    wait "$worker_pid" 2>/dev/null || true
  fi
  rmdir "$probe_dir" 2>/dev/null || true
}
trap cleanup EXIT
trap 'exit 130' INT TERM

setsid bash "$0" --dummy-worker "$probe_dir" "$probe_token" \
  >/dev/null 2>&1 &
worker_pid=$!
worker_sid=$worker_pid

for _ in $(seq 1 40); do
  worker_pgid=$(ps -o pgid= -p "$worker_pid" 2>/dev/null | tr -d ' ' || true)
  [[ "$worker_pgid" == "$worker_pid" ]] && break
  kill -0 "$worker_pid" 2>/dev/null || break
  sleep 0.05
done
[[ "$worker_pgid" == "$worker_pid" ]]

dummy_pid=""
dummy_rss=0
for _ in $(seq 1 100); do
  dummy_pid=$(ps -eo pid=,pgid=,comm= | awk -v wanted="$worker_pgid" \
    '$2==wanted && $3 ~ /^python/ {print $1; exit}')
  if [[ "$dummy_pid" =~ ^[0-9]+$ ]]; then
    dummy_rss=$(ps -o rss= -p "$dummy_pid" | tr -d ' ' || true)
    [[ "$dummy_rss" =~ ^[0-9]+$ ]] || dummy_rss=0
    (( dummy_rss >= 20000 )) && break
  fi
  sleep 0.05
done
[[ "$dummy_pid" =~ ^[0-9]+$ ]]
(( dummy_rss >= 20000 ))

tail3_validate_group "$probe_dir" "$worker_pgid"
group_rss=$(ps -eo pgid=,rss= | awk -v wanted="$worker_pgid" \
  '$1==wanted {sum+=$2} END {print sum+0}')
(( group_rss >= dummy_rss ))

echo "PROCESS_GROUP_REGRESSION_PGID=$worker_pgid"
echo "PROCESS_GROUP_REGRESSION_DUMMY_PID=$dummy_pid"
echo "PROCESS_GROUP_REGRESSION_DUMMY_RSS_KIB=$dummy_rss"
echo "PROCESS_GROUP_REGRESSION_GROUP_RSS_KIB=$group_rss"
echo "PROCESS_GROUP_REGRESSION_RSS_INCLUDED=PASS"

tail3_signal_group "$probe_dir" "$worker_pgid" TERM
for _ in $(seq 1 50); do
  (( $(session_non_zombie_count) == 0 )) && break
  sleep 0.1
done
if (( $(session_non_zombie_count) != 0 )); then
  echo "STOP: validated TERM left a live regression descendant" >&2
  exit 30
fi
wait "$worker_pid" 2>/dev/null || true
worker_pid=""
if ps -eo sid= | awk -v wanted="$worker_sid" \
    '$1==wanted {found=1} END {exit !found}'; then
  echo "STOP: regression session survived validated TERM" >&2
  exit 31
fi
rmdir "$probe_dir"
trap - EXIT INT TERM
echo "PROCESS_GROUP_REGRESSION_TERM_CLEARED=PASS"
echo "PROCESS_GROUP_REGRESSION=PASS"
