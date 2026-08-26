#!/usr/bin/env bash
set -euo pipefail

root=${1:?run root required}
tag=${2:?run tag required}
archive=${3:?source archive required}
if [[ "$(uname -s)" != Linux || "$tag" != td6_v82_* ]]; then
  echo "REFUSED: registered AWS/Linux V82 tag required" >&2
  exit 97
fi
mkdir -p "$root"
cp "$archive" "$root/source.tar.gz"
printf 'hostname=%s\ntag=%s\nstart_utc=%s\narchive_sha256=%s\n' \
  "$(hostname)" "$tag" "$(date -u +%FT%TZ)" \
  "$(sha256sum "$archive" | cut -d' ' -f1)" > "$root/launch.meta"
tar -xzf "$root/source.tar.gz" -C "$root"
source_dir="$root/td6-v82-joint-first-fitting-source-20260826"
mkdir -p "$root/evidence"
(
  set +e
  ulimit -v 16777216
  cd "$source_dir" || exit 120
  export AWS_RUN_TAG="$tag"
  export TD6_OUTPUT_DIR="$root/evidence"
  /usr/bin/time -v timeout 21600 bash run_v82.sh \
    > "$root/stdout" 2> "$root/stderr"
  rc=$?
  printf '%s\n' "$rc" > "$root/rc"
  printf '%s\n' "$(date -u +%FT%TZ)" > "$root/finished_utc"
  exit "$rc"
) &
printf '%s\n' "$!" > "$root/pid"
printf 'wrapper_pid=%s\n' "$!"
