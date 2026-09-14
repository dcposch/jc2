#!/bin/bash
set -u
S=/home/ubuntu/classA-smallest-20260906.xpXroy
mkdir -p "$S/results/c_singular"
echo "JOB_C_START $(date -u +%Y-%m-%dT%H:%M:%SZ)"
/usr/bin/python3 "$S/jobs/monitor_cgroup_rss.py" "$S/results/c_singular/rss.json" "$S/results/c_singular/rss.stop" &
monitor=$!
/usr/bin/time -v -o "$S/results/c_singular/time.txt" \
  /usr/bin/timeout --signal=TERM --kill-after=30s 8940s \
  /usr/bin/Singular --no-rc --cpus=8 --threads=8 --flint-threads=8 -q \
  "$S/data/R005_full_Tblock_Q.sing"
rc=$?
/usr/bin/touch "$S/results/c_singular/rss.stop"
wait "$monitor"
cgpath=$(awk -F: '$1=="0" {print $3}' /proc/self/cgroup)
echo "JOB_C_CGROUP_MEMORY_PEAK_BYTES $(cat /sys/fs/cgroup${cgpath}/memory.peak)"
echo "JOB_C_END $(date -u +%Y-%m-%dT%H:%M:%SZ) RC=$rc"
exit "$rc"
