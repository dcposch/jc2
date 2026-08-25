#!/bin/sh
set -eu

tag=${1:?usage: run_remote.sh UNIQUE_UTC_TAG}
case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$case_dir/../.." && pwd)
parent="$root/cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824"
successor="$root/cases/as_fonly_d7_vertical_next_cartier_20260824"
result_dir="$case_dir/results_$tag"
mkdir -p "$result_dir"
printf 'tag=%s\nhost=%s\nstart_utc=%s\npython=%s\nvm_limit_kib=16777216\ntimeout_seconds=43200\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$(python3 --version 2>&1)" > "$result_dir/run.meta"

run_one() {
  label=$1
  shift
  set +e
  (
    ulimit -v 16777216
    /usr/bin/time -v -o "$result_dir/$label.time" \
      timeout --signal=TERM --kill-after=60s 43200 "$@"
  ) > "$result_dir/$label.stdout" 2> "$result_dir/$label.stderr"
  rc=$?
  set -e
  printf 'label=%s\nrc=%s\nend_utc=%s\n' \
    "$label" "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    > "$result_dir/$label.rc"
  return "$rc"
}

overall=0
run_one full_c5_replay sh "$parent/replay_all.sh" || overall=1
run_one full_c5_manifest sh -c \
  'cd "$1" && shasum -a 256 -c MANIFEST.sha256' sh "$parent" || overall=1
run_one next_cartier_replay sh "$successor/replay_all.sh" || overall=1
run_one next_cartier_manifest sh -c \
  'cd "$1" && shasum -a 256 -c MANIFEST.sha256' sh "$successor" || overall=1

(cd "$result_dir" && sha256sum \
  full_c5_replay.stdout full_c5_replay.stderr full_c5_replay.time full_c5_replay.rc \
  full_c5_manifest.stdout full_c5_manifest.stderr full_c5_manifest.time full_c5_manifest.rc \
  next_cartier_replay.stdout next_cartier_replay.stderr next_cartier_replay.time next_cartier_replay.rc \
  next_cartier_manifest.stdout next_cartier_manifest.stderr next_cartier_manifest.time next_cartier_manifest.rc) \
  > "$result_dir/OUTPUTS.sha256"
printf 'overall_rc=%s\nend_utc=%s\n' \
  "$overall" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$result_dir/run.meta"
exit "$overall"

