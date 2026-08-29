#!/usr/bin/env bash
set -euo pipefail

root=${1:?run root required}
host_label=${2:?host label required}
archive=${3:?archive required}
expected=${4:?archive SHA256 required}
stamp=${5:?UTC stamp required}

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82P4E requires Linux" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V82P4E requires Amazon EC2" >&2
  exit 96
fi
actual=$(sha256sum "$archive" | cut -d' ' -f1)
[[ "$actual" == "$expected" ]] || { echo "REFUSED: archive SHA mismatch" >&2; exit 95; }
available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
(( available_kib >= 33554432 )) || { echo "REFUSED: less than 32 GiB available" >&2; exit 94; }

mkdir -p "$root/lanes" "$root/source"
cp "$archive" "$root/source.tar.gz"
tar -xzf "$root/source.tar.gz" -C "$root/source"
printf 'hostname=%s\nhost_label=%s\nstart_utc=%s\narchive_sha256=%s\ncap_per_lane_kib=8388608\ntimeout_seconds=43200\nlevels=10,15\n' \
  "$(hostname)" "$host_label" "$(date -u +%FT%TZ)" "$actual" \
  > "$root/registration.meta"

for level in 10 15; do
  lane="$root/lanes/d$level"
  tag="td6_v82p4_extended_${host_label}_d${level}_${stamp}"
  mkdir -p "$lane/evidence"
  printf 'hostname=%s\ntag=%s\nlevel=%s\ncap_kib=8388608\ntimeout_s=43200\narchive_sha256=%s\n' \
    "$(hostname)" "$tag" "$level" "$actual" > "$lane/launch.meta"
  (
    set +e
    ulimit -v 8388608
    cd "$root/source" || exit 120
    export AWS_RUN_TAG="$tag"
    export TD6_DEAD_LEVEL="$level"
    export TD6_OUTPUT_DIR="$lane/evidence"
    /usr/bin/time -v timeout 43200 bash run_v82p4.sh \
      > "$lane/stdout" 2> "$lane/stderr"
    rc=$?
    printf '%s\n' "$rc" > "$lane/rc"
    printf '%s\n' "$(date -u +%FT%TZ)" > "$lane/finished_utc"
    sha256sum "$lane/stdout" "$lane/stderr" "$lane/rc" > "$lane/RESULTS.sha256"
    exit "$rc"
  ) > "$lane/wrapper.log" 2>&1 < /dev/null &
  printf '%s\n' "$!" > "$lane/pid"
  printf 'd%s_pid=%s\n' "$level" "$!"
done
