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
printf 'hostname=%s\nlabel=%s\narchive_sha256=%s\nstart_utc=%s\ncap_kib=268435456\ntimeout_seconds=21600\nscope=q14-mod-F-splitting-independent-cokernel\n' \
  "$(hostname)" "$label" "$expected" "$(date -u +%FT%TZ)" > "$root/registration.meta"
(
  set +e
  lane="$root/modfcokernel"
  mkdir -p "$lane/output"
  tag="td6_v89h6_q14_mod_f_cokernel_${label}_${stamp}"
  printf 'hostname=%s\nlabel=%s\ntag=%s\nstart_utc=%s\narchive_sha256=%s\ncap_kib=268435456\ntimeout_seconds=21600\nscope=q14-mod-F-splitting-independent-cokernel\n' \
    "$(hostname)" "$label" "$tag" "$(date -u +%FT%TZ)" "$expected" > "$lane/launch.meta"
  (
    set +e
    ulimit -v 268435456
    cd "$source_dir" || exit 120
    export AWS_RUN_TAG="$tag"
    export TD6_Q_EXPONENT=2
    export TD6_PIVOT_POLICY=ascending
    export TD6_PIVOT_SCOPE=all-staged
    export TD6_Q_SCOPE=tail-q14-q16-q24
    export TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U
    export TD6_PRIME_SENTINEL=p1000003-C8-V3-U1
    export TD6_OUTPUT_DIR="$lane/output"
    /usr/bin/time -v timeout 21600 bash run_v89h6_q14_mod_f_cokernel.sh \
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
