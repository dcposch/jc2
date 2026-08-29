#!/usr/bin/env bash
set -euo pipefail

root=${1:?run root required}
label=${2:?host label required}
archive=${3:?source archive required}
expected=${4:?archive SHA256 required}
stamp=${5:?UTC stamp required}

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V84R2 block 0,1 requires Linux" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V84R2 block 0,1 requires Amazon EC2" >&2
  exit 96
fi
actual=$(sha256sum "$archive" | cut -d' ' -f1)
[[ "$actual" == "$expected" ]] || {
  echo "REFUSED: archive SHA mismatch" >&2
  exit 95
}

mkdir -p "$root/evidence"
cp "$archive" "$root/source.tar.gz"
tar -xzf "$root/source.tar.gz" -C "$root"
source_dir="$root/source"
tag="td6_v84r2_k2_${label}_block_0_1_${stamp}"
printf 'hostname=%s\nlabel=%s\ntag=%s\nstart_utc=%s\narchive_sha256=%s\nblock_a=0\nblock_b=1\ncap_kib=8388608\n' \
  "$(hostname)" "$label" "$tag" "$(date -u +%FT%TZ)" "$actual" \
  > "$root/registration.meta"
(
  set +e
  ulimit -v 8388608
  cd "$source_dir" || exit 120
  export AWS_RUN_TAG="$tag"
  export TD6_K2_BLOCK_A=0
  export TD6_K2_BLOCK_B=1
  export TD6_OUTPUT_DIR="$root/evidence"
  /usr/bin/time -v timeout 21600 bash run_v84r2.sh \
    > "$root/stdout" 2> "$root/stderr"
  rc=$?
  printf '%s\n' "$rc" > "$root/rc"
  printf '%s\n' "$(date -u +%FT%TZ)" > "$root/finished_utc"
  exit "$rc"
) > "$root/wrapper.log" 2>&1 < /dev/null &
printf '%s\n' "$!" > "$root/pid"
printf 'wrapper_pid=%s\n' "$!"
