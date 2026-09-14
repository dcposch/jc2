#!/usr/bin/env bash
# Wait for the detached build, retire its temporary swap, then validate/derive inputs.
set -Eeuo pipefail
readonly BASE=/home/ubuntu/t2t3-full
while [[ ! -f $BASE/logs/full-build.rc ]]; do sleep 5; done
[[ $(< "$BASE/logs/full-build.rc") == 0 ]]
date -u +%Y-%m-%dT%H:%M:%SZ > "$BASE/logs/after-build-observed.utc"
sudo swapoff "$BASE/.build-swap3"
sudo swapoff "$BASE/.build-swap2"
sudo swapoff "$BASE/.build-swap"
sudo sysctl -w vm.swappiness="$(< "$BASE/logs/prebuild-swap.swappiness")"
sudo rm -- "$BASE/.build-swap3" "$BASE/.build-swap2" "$BASE/.build-swap"
swapon --show --bytes > "$BASE/logs/postbuild-swapon.txt"
grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo \
  > "$BASE/logs/postbuild-memory.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$BASE/logs/build-swap-removed.utc"
"$BASE/drivers/prepare_full.sh" > "$BASE/logs/prepare-full.stdout" \
  2> "$BASE/logs/prepare-full.stderr"
printf '0\n' > "$BASE/logs/prepare-full.rc"
