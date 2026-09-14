#!/usr/bin/env bash
set -euo pipefail
source /home/ubuntu/jc2/box/gi70-longsolve-20260905/jobs/common.sh
R="$GI70_ROOT/results/c_c1_msolve"
mkdir -p "$R"
echo "GI70_JOB_START c utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) host=$(hostname)"
test "$(msolve -V 2>&1 | head -1)" = "0.10.1"
python3 "$GI70_ROOT/guard_msolve.py" \
  "$GI70_ROOT/inputs/c_c1_p1073741827.ms" \
  "$GI70_ROOT/inputs/c_guard_expected.json" | tee "$R/guard.json"
grep -q '"all_checks_pass": true' "$R/guard.json"
echo "GI70_C_GUARD_PASS slots=4553310 limit=2147483647"
start_rss_monitor "$R"
trap stop_rss_monitor EXIT
run_logged "$R" stdbuf -oL msolve -g 2 -t 32 -v 2 -l 44 -m 2000 \
  -f "$GI70_ROOT/inputs/c_c1_p1073741827.ms" -o "$R/msolve.out" || true
echo "GI70_JOB_END c rc=$RUN_RC utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit "$RUN_RC"
