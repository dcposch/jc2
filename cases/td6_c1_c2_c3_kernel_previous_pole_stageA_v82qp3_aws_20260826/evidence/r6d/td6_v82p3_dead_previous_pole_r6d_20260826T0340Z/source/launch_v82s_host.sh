#!/usr/bin/env bash
set -euo pipefail
root=${1:?run root required}
host_label=${2:?host label required}
archive=${3:?archive required}
if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: AWS/Linux required" >&2
  exit 97
fi
mkdir -p "$root/lanes"
cp "$archive" "$root/source.tar.gz"
printf 'hostname=%s\nhost_label=%s\nstart_utc=%s\narchive_sha256=%s\n' \
  "$(hostname)" "$host_label" "$(date -u +%FT%TZ)" \
  "$(sha256sum "$archive" | cut -d' ' -f1)" > "$root/registration.meta"
tar -xzf "$root/source.tar.gz" -C "$root"
source_dir="$root/td6-v82s-kernel-dead-first-shards-source-20260826"
for level in 10 15; do
  lane="$root/lanes/d$level"
  tag="td6_v82s_${host_label}_d${level}_20260826T0253Z"
  mkdir -p "$lane/evidence"
  printf 'hostname=%s\ntag=%s\nlevel=%s\n' \
    "$(hostname)" "$tag" "$level" > "$lane/launch.meta"
  (
    set +e
    ulimit -v 8388608
    cd "$source_dir" || exit 120
    export AWS_RUN_TAG="$tag"
    export TD6_DEAD_LEVEL="$level"
    export TD6_OUTPUT_DIR="$lane/evidence"
    /usr/bin/time -v timeout 14400 bash run_v82s.sh \
      > "$lane/stdout" 2> "$lane/stderr"
    rc=$?
    printf '%s\n' "$rc" > "$lane/rc"
    printf '%s\n' "$(date -u +%FT%TZ)" > "$lane/finished_utc"
    exit "$rc"
  ) > "$lane/wrapper.log" 2>&1 < /dev/null &
  printf '%s\n' "$!" > "$lane/pid"
  printf 'd%s_pid=%s\n' "$level" "$!"
done
