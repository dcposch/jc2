#!/bin/bash
set -u
S=/home/ubuntu/classA-smallest-20260906.xpXroy
mkdir -p "$S/results/b_msolve"
echo "JOB_B_START $(date -u +%Y-%m-%dT%H:%M:%SZ)"
/usr/bin/python3 "$S/jobs/monitor_cgroup_rss.py" "$S/results/b_msolve/rss.json" "$S/results/b_msolve/rss.stop" &
monitor=$!
/usr/bin/time -v -o "$S/results/b_msolve/time.txt" \
  /usr/bin/timeout --signal=TERM --kill-after=30s 8940s \
  /usr/local/bin/msolve -g 2 -t 16 -v 2 -l 44 -m 1000 \
  -f "$S/data/R005_c1_p1073741827.ms" -o "$S/results/b_msolve/basis.out"
rc=$?
/usr/bin/touch "$S/results/b_msolve/rss.stop"
wait "$monitor"
cgpath=$(awk -F: '$1=="0" {print $3}' /proc/self/cgroup)
echo "JOB_B_CGROUP_MEMORY_PEAK_BYTES $(cat /sys/fs/cgroup${cgpath}/memory.peak)"
echo "JOB_B_END $(date -u +%Y-%m-%dT%H:%M:%SZ) RC=$rc"
exit "$rc"
