#!/usr/bin/env bash
set -euo pipefail

run_dir=${1:?run dir}
label=${2:?label}
job=${3:?Singular job}
mem_gib=${4:?address-space GiB}
file_gib=${5:?output-file GiB}
wall_seconds=${6:?wall seconds}

[[ "$run_dir" == /* && "$job" == "$run_dir/"* && "$label" =~ ^[A-Za-z0-9._-]+$ ]]
set +e
/usr/bin/time -v \
  timeout --foreground --signal=TERM --kill-after=60s "$wall_seconds" \
    prlimit --as=$((mem_gib * 1024 * 1024 * 1024)) \
            --fsize=$((file_gib * 1024 * 1024 * 1024)) \
            --cpu=$((wall_seconds * 2)) \
            -- Singular -q "$job" \
  > "$run_dir/$label.log" 2>&1
rc=$?
printf '%s\n' "$rc" > "$run_dir/$label.rc"
(cd "$run_dir"; sha256sum "$label.log" > "$label.output.sha256")
exit "$rc"
