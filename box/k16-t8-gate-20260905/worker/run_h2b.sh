#!/bin/bash
set -uo pipefail
cd /home/ubuntu/k16-t8-gate-20260905
start=$(date -u +%FT%TZ)
printf '%s\n' "$start" > h2b.started
sha256sum affinew_p32027.ms /usr/local/bin/msolve > h2b.remote.sha256
/usr/bin/time -v -o h2b.time timeout --signal=TERM --kill-after=30s 10200s /usr/local/bin/msolve -f affinew_p32027.ms -g 2 -t 32 -v 2 -o h2b.gb > h2b.log 2>&1
rc=$?
printf 'exit=%s\nstarted=%s\nfinished=%s\nwatchdog_seconds=10200\nthreads=32\n' "$rc" "$start" "$(date -u +%FT%TZ)" > h2b.status
sha256sum h2b.log h2b.time h2b.status h2b.gb > h2b.outputs.sha256 2>/dev/null
exit "$rc"
