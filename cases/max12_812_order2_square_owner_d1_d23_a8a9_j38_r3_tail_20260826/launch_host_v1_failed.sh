#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
archive=$1; tag=$2; characteristic=$3; a=$4; d=$5; source_sha=$6
case "$tag" in max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65519|65521) ;; *) exit 125 ;; esac
case "$a:$d" in 8:3|9:2|9:3) ;; *) exit 125 ;; esac
base="/home/ubuntu/jobs/$tag"; source_root="$base/source"; evidence="$base/evidence"
if [[ -e "$base" ]]; then exit 125; fi
actual_sha=$(sha256sum "$archive" | cut -d ' ' -f 1)
if [[ "$actual_sha" != "$source_sha" ]]; then exit 125; fi
mkdir -p "$source_root"; tar -xzf "$archive" -C "$source_root"; cd "$source_root"
printf '%s  %s\n' "$source_sha" "$archive" > "$base/archive.sha256"
sha256sum -c cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/FREEZE.sha256 > "$base/prelaunch_freeze.stdout"
nohup bash cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/run_aws.sh \
  "$source_root" "$evidence" "$tag" 134217728 "$characteristic" "$a" "$d" 10800 "$source_sha" \
  > "$base/outer.stdout" 2> "$base/outer.stderr" < /dev/null &
launcher_pid=$!; printf '%s\n' "$launcher_pid" > "$base/host_launcher.pid"
printf 'tag=%s host=%s pid=%s base=%s characteristic=%s cell=a%s_d%s\n' \
  "$tag" "$(hostname)" "$launcher_pid" "$base" "$characteristic" "$a" "$d"
