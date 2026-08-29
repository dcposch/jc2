#!/usr/bin/env bash
set -euo pipefail

root=${1:?root required}
label=${2:?label required}
archive=${3:?archive required}
expected=${4:?archive SHA256 required}
stamp=${5:?stamp required}
[[ "$(uname -s)" == Linux ]] || exit 97
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
[[ "$(sha256sum "$archive" | cut -d' ' -f1)" == "$expected" ]] || exit 95
mkdir -p "$root"
cp "$archive" "$root/source.tar.gz"
tar -xzf "$root/source.tar.gz" -C "$root"
source_dir="$root/source"
printf 'hostname=%s\nlabel=%s\narchive_sha256=%s\nstart_utc=%s\n' \
  "$(hostname)" "$label" "$expected" "$(date -u +%FT%TZ)" > "$root/registration.meta"
(
  set +e
  lane="$root/kmodf"
  mkdir -p "$lane/output"
  tag="td6_v89k1_k_b3_mod_f_${label}_${stamp}"
  printf 'hostname=%s\nlabel=%s\ntag=%s\nstart_utc=%s\narchive_sha256=%s\n' \
    "$(hostname)" "$label" "$tag" "$(date -u +%FT%TZ)" "$expected" > "$lane/launch.meta"
  (
    set +e
    ulimit -v 4194304
    cd "$source_dir" || exit 120
    export AWS_RUN_TAG="$tag"
    export TD6_OUTPUT_DIR="$lane/output"
    /usr/bin/time -v timeout 600 bash run_v89k1_k_b3_mod_f.sh \
      > "$lane/stdout" 2> "$lane/stderr"
    rc=$?
    printf '%s\n' "$rc" > "$lane/rc"
    date -u +%FT%TZ > "$lane/finished_utc"
    exit "$rc"
  ) > "$lane/wrapper.log" 2>&1 < /dev/null &
  printf '%s\n' "$!" > "$lane/pid"
  wait
  date -u +%FT%TZ > "$root/fleet_finished_utc"
) > "$root/fleet_supervisor.log" 2>&1 < /dev/null &
printf '%s\n' "$!" > "$root/fleet_supervisor.pid"
printf 'fleet_supervisor_pid=%s\n' "$!"
