#!/usr/bin/env bash
set -euo pipefail

root=${1:?run root required}
label=${2:?host label required}
archive=${3:?source archive required}
expected=${4:?archive SHA256 required}
stamp=${5:?UTC stamp required}
[[ "$(uname -s)" == Linux ]] || exit 97
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96
actual=$(sha256sum "$archive" | cut -d' ' -f1)
[[ "$actual" == "$expected" ]] || exit 95

mkdir -p "$root"
cp "$archive" "$root/source.tar.gz"
tar -xzf "$root/source.tar.gz" -C "$root"
source_dir="$root/source"
printf 'hostname=%s\nlabel=%s\nstart_utc=%s\narchive_sha256=%s\ncap_kib=68719476736\ntimeout_seconds=21600\nq15_scope=exact-target-shear\n' \
  "$(hostname)" "$label" "$(date -u +%FT%TZ)" "$actual" \
  > "$root/registration.meta"
(
  set +e
  lane="$root/q15"
  mkdir -p "$lane/output"
  tag="td6_v88q15_total_shear_${label}_${stamp}"
  printf 'hostname=%s\nlabel=%s\ntag=%s\nstart_utc=%s\narchive_sha256=%s\ncap_kib=68719476736\ntimeout_seconds=21600\nq15_scope=exact-target-shear\n' \
    "$(hostname)" "$label" "$tag" "$(date -u +%FT%TZ)" "$actual" \
    > "$lane/launch.meta"
  (
    set +e
    ulimit -v 68719476736
    cd "$source_dir" || exit 120
    export AWS_RUN_TAG="$tag"
    export TD6_Q_EXPONENT=2
    export TD6_PIVOT_POLICY=ascending
    export TD6_PIVOT_SCOPE=all-staged
    export TD6_OUTPUT_DIR="$lane/output"
    /usr/bin/time -v timeout 21600 bash run_v88q15_total_shear.sh \
      > "$lane/stdout" 2> "$lane/stderr"
    rc=$?
    printf '%s\n' "$rc" > "$lane/rc"
    printf '%s\n' "$(date -u +%FT%TZ)" > "$lane/finished_utc"
    exit "$rc"
  ) > "$lane/wrapper.log" 2>&1 < /dev/null &
  printf '%s\n' "$!" > "$lane/pid"
  wait
  printf '%s\n' "$(date -u +%FT%TZ)" > "$root/fleet_finished_utc"
) > "$root/fleet_supervisor.log" 2>&1 < /dev/null &
printf '%s\n' "$!" > "$root/fleet_supervisor.pid"
printf 'fleet_supervisor_pid=%s\n' "$!"
