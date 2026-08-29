#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
base_archive=$1; diag_archive=$2; tag=$3; characteristic=$4; base_sha=$5; diag_sha=$6; cap_kib=$7
case "$tag" in max12_812_order2_square_d1_a8d3_j38_bridge_diag_*) ;; *) exit 125 ;; esac
base="/home/ubuntu/jobs/$tag"; source_root="$base/source"; evidence="$base/evidence"
if [[ -e "$base" ]]; then exit 125; fi
[[ "$(sha256sum "$base_archive" | cut -d ' ' -f 1)" == "$base_sha" ]] || exit 125
[[ "$(sha256sum "$diag_archive" | cut -d ' ' -f 1)" == "$diag_sha" ]] || exit 125
mkdir -p "$source_root"; tar -xzf "$base_archive" -C "$source_root"; tar -xzf "$diag_archive" -C "$source_root"; cd "$source_root"
printf '%s  %s\n%s  %s\n' "$base_sha" "$base_archive" "$diag_sha" "$diag_archive" > "$base/archives.sha256"
sha256sum -c cases/max12_812_order2_square_owner_d1_a8d3_j38_bridge_diagnostic_20260826/FREEZE.sha256 > "$base/prelaunch_freeze.stdout"
nohup bash cases/max12_812_order2_square_owner_d1_a8d3_j38_bridge_diagnostic_20260826/run_aws.sh \
  "$source_root" "$evidence" "$tag" "$characteristic" 10800 "$cap_kib" "$base_sha" "$diag_sha" \
  > "$base/outer.stdout" 2> "$base/outer.stderr" < /dev/null &
launcher_pid=$!; printf '%s\n' "$launcher_pid" > "$base/host_launcher.pid"
printf 'tag=%s host=%s pid=%s base=%s characteristic=%s\n' "$tag" "$(hostname)" "$launcher_pid" "$base" "$characteristic"
