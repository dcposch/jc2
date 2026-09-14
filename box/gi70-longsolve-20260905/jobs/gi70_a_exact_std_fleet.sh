#!/usr/bin/env bash
set -euo pipefail
source /home/ubuntu/jc2/box/gi70-longsolve-20260905/jobs/common.sh
R="$GI70_ROOT/results/a_exact_std"
echo "GI70_JOB_START a utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) host=$(hostname)"
start_rss_monitor "$R"
trap stop_rss_monitor EXIT
run_logged "$R" stdbuf -oL Singular --no-rc -q "$GI70_ROOT/inputs/a_exact_std.sing" || true
echo "GI70_JOB_END a rc=$RUN_RC utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit "$RUN_RC"
