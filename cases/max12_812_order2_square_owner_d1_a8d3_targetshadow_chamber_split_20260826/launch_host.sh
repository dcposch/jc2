#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 5 ]]; then exit 125; fi
archive=$1; tag=$2; characteristic=$3; source_sha=$4; cap_kib=$5
case "$tag" in max12_812_order2_square_d1_a8d3_targetshadow_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65519|65521) ;; *) exit 125 ;; esac
base="/home/ubuntu/jobs/$tag"; source_root="$base/source"; evidence="$base/evidence"
if [[ -e "$base" ]]; then exit 125; fi
[[ "$(sha256sum "$archive" | cut -d ' ' -f 1)" == "$source_sha" ]] || exit 125
mkdir -p "$source_root"; tar -xzf "$archive" -C "$source_root"; cd "$source_root"
printf '%s  %s\n' "$source_sha" "$archive" > "$base/archive.sha256"
sha256sum -c cases/max12_812_order2_square_owner_d1_a8d3_targetshadow_chamber_split_20260826/FREEZE.sha256 > "$base/prelaunch_freeze.stdout"
nohup bash cases/max12_812_order2_square_owner_d1_a8d3_targetshadow_chamber_split_20260826/run_aws.sh \
  "$source_root" "$evidence" "$tag" "$characteristic" 7200 "$cap_kib" "$source_sha" \
  > "$base/outer.stdout" 2> "$base/outer.stderr" < /dev/null &
launcher_pid=$!; printf '%s\n' "$launcher_pid" > "$base/host_launcher.pid"
printf 'tag=%s host=%s pid=%s base=%s characteristic=%s cap_kib=%s\n' \
  "$tag" "$(hostname)" "$launcher_pid" "$base" "$characteristic" "$cap_kib"
