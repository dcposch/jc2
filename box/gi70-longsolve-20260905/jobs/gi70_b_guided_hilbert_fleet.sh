#!/usr/bin/env bash
set -euo pipefail
source /home/ubuntu/jc2/box/gi70-longsolve-20260905/jobs/common.sh
R="$GI70_ROOT/results/b_guided_hilbert"
echo "GI70_JOB_START b utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) host=$(hostname)"
start_rss_monitor "$R"
trap stop_rss_monitor EXIT
run_logged "$R" stdbuf -oL python3 "$GI70_ROOT/run_guided.py" || true
echo "GI70_JOB_END b rc=$RUN_RC utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit "$RUN_RC"
