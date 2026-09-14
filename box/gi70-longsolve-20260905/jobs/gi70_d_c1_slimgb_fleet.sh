#!/usr/bin/env bash
set -euo pipefail
source /home/ubuntu/jc2/box/gi70-longsolve-20260905/jobs/common.sh
R="$GI70_ROOT/results/d_c1_slimgb"
echo "GI70_JOB_START d utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) host=$(hostname)"
start_rss_monitor "$R"
trap stop_rss_monitor EXIT
run_logged "$R" stdbuf -oL Singular --no-rc -q "$GI70_ROOT/inputs/d_c1_slimgb.sing" || true
echo "GI70_JOB_END d rc=$RUN_RC utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit "$RUN_RC"
