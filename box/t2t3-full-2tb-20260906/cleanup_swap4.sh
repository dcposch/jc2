#!/usr/bin/env bash
# Retire the final build-only swap extent after preparation, before solvers.
set -Eeuo pipefail
readonly BASE=/home/ubuntu/t2t3-full
while [[ ! -f $BASE/logs/after-build-prepare.controller.rc ]]; do sleep 5; done
[[ $(< "$BASE/logs/after-build-prepare.controller.rc") == 0 ]]
sudo swapoff "$BASE/.build-swap4"
sudo rm -- "$BASE/.build-swap4"
swapon --show --bytes > "$BASE/logs/postbuild-all-swapon.txt"
[[ ! -s $BASE/logs/postbuild-all-swapon.txt ]]
grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo \
  > "$BASE/logs/postbuild-all-memory.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$BASE/logs/all-build-swap-removed.utc"
