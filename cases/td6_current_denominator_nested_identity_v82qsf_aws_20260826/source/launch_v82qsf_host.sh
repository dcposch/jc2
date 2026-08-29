#!/usr/bin/env bash
set -euo pipefail

root=${1:?run root required}
label=${2:?host label required}
archive=${3:?source archive required}
expected=${4:?archive SHA256 required}
stamp=${5:?UTC stamp required}

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82QSF fleet requires Linux" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V82QSF fleet requires Amazon EC2" >&2
  exit 96
fi
actual=$(sha256sum "$archive" | cut -d' ' -f1)
[[ "$actual" == "$expected" ]] || { echo "REFUSED: archive SHA mismatch" >&2; exit 95; }
available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
(( available_kib >= 8388608 )) || { echo "REFUSED: less than 8 GiB available" >&2; exit 94; }

mkdir -p "$root"
cp "$archive" "$root/source.tar.gz"
tar -xzf "$root/source.tar.gz" -C "$root"
printf 'hostname=%s\nlabel=%s\nstart_utc=%s\narchive_sha256=%s\ncap_kib=1048576\ntimeout_seconds=600\n' \
  "$(hostname)" "$label" "$(date -u +%FT%TZ)" "$actual" > "$root/registration.meta"

(
  set +e
  ulimit -v 1048576
  cd "$root/source" || exit 120
  export AWS_RUN_TAG="td6_v82qsf_nested_${label}_${stamp}"
  /usr/bin/time -v timeout 600 bash run_v82qsf.sh > "$root/stdout" 2> "$root/stderr"
  rc=$?
  printf '%s\n' "$rc" > "$root/rc"
  printf '%s\n' "$(date -u +%FT%TZ)" > "$root/finished_utc"
  sha256sum "$root/stdout" "$root/stderr" "$root/rc" > "$root/RESULTS.sha256"
  exit "$rc"
) > "$root/wrapper.log" 2>&1 < /dev/null &
printf '%s\n' "$!" > "$root/pid"
printf 'pid=%s\n' "$!"
