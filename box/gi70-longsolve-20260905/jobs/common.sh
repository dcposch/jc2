#!/usr/bin/env bash
set -u

GI70_ROOT=/home/ubuntu/jc2/box/gi70-longsolve-20260905

start_rss_monitor() {
  local result_dir=$1
  mkdir -p "$result_dir"
  (
    while true; do
      {
        echo "POLL_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        free -b
        ps -eo pid,ppid,pgid,etimes,rss,vsz,%mem,comm,args | awk 'NR==1 || /Singular|msolve|run_guided.py|guided_gb.py/'
      } >> "$result_dir/rss-15min.log"
      sleep 900
    done
  ) &
  RSS_MONITOR_PID=$!
}

stop_rss_monitor() {
  kill "${RSS_MONITOR_PID:-}" 2>/dev/null || true
  wait "${RSS_MONITOR_PID:-}" 2>/dev/null || true
}

run_logged() {
  local result_dir=$1
  shift
  mkdir -p "$result_dir"
  set +e
  timeout --signal=TERM --kill-after=60s 10200s \
    /usr/bin/time -v -o "$result_dir/time-v.txt" \
    "$@" > >(tee "$result_dir/stdout.log") 2> >(tee "$result_dir/stderr.log" >&2)
  RUN_RC=$?
  set -e
  echo "$RUN_RC" > "$result_dir/returncode.txt"
  return "$RUN_RC"
}
