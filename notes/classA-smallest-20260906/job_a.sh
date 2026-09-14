#!/bin/bash
set -u
S=/home/ubuntu/classA-smallest-20260906.xpXroy
mkdir -p "$S/results/a_guided"
echo "JOB_A_START $(date -u +%Y-%m-%dT%H:%M:%SZ)"
/usr/bin/python3 "$S/jobs/monitor_cgroup_rss.py" "$S/results/a_guided/rss.json" "$S/results/a_guided/rss.stop" &
monitor=$!
/usr/bin/time -v -o "$S/results/a_guided/time.txt" \
  /usr/bin/timeout --signal=TERM --kill-after=30s 8940s \
  /usr/bin/python3 "$S/jobs/run_guided_r005.py"
rc=$?
/usr/bin/touch "$S/results/a_guided/rss.stop"
wait "$monitor"
cgpath=$(awk -F: '$1=="0" {print $3}' /proc/self/cgroup)
echo "JOB_A_CGROUP_MEMORY_PEAK_BYTES $(cat /sys/fs/cgroup${cgpath}/memory.peak)"
echo "JOB_A_END $(date -u +%Y-%m-%dT%H:%M:%SZ) RC=$rc"
exit "$rc"
