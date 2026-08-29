#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true); if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 3 ]]; then exit 125; fi
archive=$1; tag=$2; characteristic=$3
case "$tag" in max12_812_order2_square_lowcontact_c1c2_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65521) ;; *) exit 125 ;; esac
base="/home/ubuntu/jobs/$tag"; source_root="$base/source"; evidence="$base/evidence"; if [[ -e "$base" ]]; then exit 125; fi
mkdir -p "$source_root"; tar -xzf "$archive" -C "$source_root"; cd "$source_root"
sha256sum -c cases/max12_812_order2_square_owner_lowcontact_c1_c2_20260826/FREEZE.sha256 > "$base/prelaunch_freeze.stdout"
nohup bash cases/max12_812_order2_square_owner_lowcontact_c1_c2_20260826/run_aws.sh "$source_root" "$evidence" "$tag" 33554432 "$characteristic" 600 7200 > "$base/outer.stdout" 2> "$base/outer.stderr" < /dev/null &
launcher_pid=$!; printf '%s\n' "$launcher_pid" > "$base/host_launcher.pid"; printf 'tag=%s host=%s pid=%s base=%s characteristic=%s\n' "$tag" "$(hostname)" "$launcher_pid" "$base" "$characteristic"
