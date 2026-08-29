#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: stop_aws.sh RUN_DIR" >&2
  exit 64
fi

run_dir=$(realpath "$1")
registry="$run_dir/groups.tsv"
[[ -f "$registry" ]]
exec python3 "$(dirname "$0")/process_group_guard.py" stop \
  --registry "$registry" --grace-seconds 30
