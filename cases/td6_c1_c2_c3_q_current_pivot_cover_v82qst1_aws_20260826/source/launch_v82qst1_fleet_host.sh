#!/usr/bin/env bash
set -euo pipefail

root=${1:?run root required}
label=${2:?host label required}
archive=${3:?source archive required}
expected=${4:?archive SHA256 required}
stamp=${5:?UTC stamp required}
shift 5
(( $# > 0 )) || { echo "REFUSED: no policy:q specifications" >&2; exit 91; }

if [[ "$(uname -s)" != Linux ]]; then
  echo "REFUSED: V82QST1 fleet requires Linux" >&2
  exit 97
fi
if ! grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor; then
  echo "REFUSED: V82QST1 fleet requires Amazon EC2" >&2
  exit 96
fi
actual=$(sha256sum "$archive" | cut -d' ' -f1)
[[ "$actual" == "$expected" ]] || { echo "REFUSED: archive SHA mismatch" >&2; exit 95; }

mkdir -p "$root"
cp "$archive" "$root/source.tar.gz"
tar -xzf "$root/source.tar.gz" -C "$root"
source_dir="$root/source"
printf 'hostname=%s\nlabel=%s\nstart_utc=%s\narchive_sha256=%s\ncap_per_lane_kib=2097152\ntimeout_seconds=7200\nspecifications=%s\n' \
  "$(hostname)" "$label" "$(date -u +%FT%TZ)" "$actual" "$*" \
  > "$root/registration.meta"

(
  set +e
  for specification in "$@"; do
    policy=${specification%%:*}
    exponent=${specification##*:}
    [[ "$policy" == reverse || "$policy" == sparse ]] || exit 94
    [[ "$exponent" == 2 || "$exponent" == 10 ]] || exit 93
    lane="$root/${policy}_q${exponent}"
    mkdir -p "$lane/output"
    tag="td6_v82qst1_current_${label}_${policy}_q${exponent}_${stamp}"
    printf 'hostname=%s\nlabel=%s\ntag=%s\nq_exponent=%s\npivot_policy=%s\nstart_utc=%s\narchive_sha256=%s\ncap_kib=2097152\ntimeout_seconds=7200\n' \
      "$(hostname)" "$label" "$tag" "$exponent" "$policy" \
      "$(date -u +%FT%TZ)" "$actual" > "$lane/launch.meta"
    (
      set +e
      ulimit -v 2097152
      cd "$source_dir" || exit 120
      export AWS_RUN_TAG="$tag"
      export TD6_Q_EXPONENT="$exponent"
      export TD6_PIVOT_POLICY="$policy"
      export TD6_OUTPUT_DIR="$lane/output"
      /usr/bin/time -v timeout 7200 bash run_v82qst1_current.sh \
        > "$lane/stdout" 2> "$lane/stderr"
      rc=$?
      printf '%s\n' "$rc" > "$lane/rc"
      printf '%s\n' "$(date -u +%FT%TZ)" > "$lane/finished_utc"
      exit "$rc"
    ) > "$lane/wrapper.log" 2>&1 < /dev/null &
    printf '%s\n' "$!" > "$lane/pid"
  done
  wait
  printf '%s\n' "$(date -u +%FT%TZ)" > "$root/fleet_finished_utc"
) > "$root/fleet_supervisor.log" 2>&1 < /dev/null &
printf '%s\n' "$!" > "$root/fleet_supervisor.pid"
printf 'fleet_supervisor_pid=%s\n' "$!"

