#!/usr/bin/env bash
set -euo pipefail

k00_tag=max12_812_order2_u2_62_k00_v27_alt_full_p6_rank2_20260827T201000Z_r6a
k00_jobs=/home/ubuntu/jobs
k00_archive="$k00_jobs/${k00_tag}_source.tar.gz"
k00_source="$k00_jobs/${k00_tag}_source"
k00_job="$k00_jobs/$k00_tag"
k00_pidfile="$k00_jobs/${k00_tag}.launcher.pid"
k00_outer_stdout="$k00_jobs/${k00_tag}.outer.stdout"
k00_outer_stderr="$k00_jobs/${k00_tag}.outer.stderr"
k00_freeze_rel=cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/SOURCE_FREEZE_FULL_P6_RANK2_CHART_ALTERNATIVE.sha256
k00_freeze_sha=ffd2e4da109e2701499152eb5561f97005b06f536077abc6fd7242b87fc9f7f7
k00_archive_sha=d7d21850913496da618cf8b15ad09b7d225a3de6f002fd73edaba081746a8ee9
k00_wrapper=cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/run_v27_full_p6_rank2_chart_alt_aws.sh

[[ "$(hostname)" == ip-172-30-0-34 ]]
[[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" == "Amazon EC2" ]]
[[ -z "$(swapon --show --noheadings 2>/dev/null)" ]]
(( $(awk '/MemAvailable:/ {print $2}' /proc/meminfo) >= 450000000 ))
[[ -f "$k00_archive" ]]
[[ "$(sha256sum "$k00_archive" | awk '{print $1}')" == "$k00_archive_sha" ]]
for k00_path in "$k00_source" "$k00_job" "$k00_pidfile" "$k00_outer_stdout" "$k00_outer_stderr"; do
  [[ ! -e "$k00_path" ]]
done

mkdir "$k00_source"
tar -xzf "$k00_archive" -C "$k00_source"
cd "$k00_source"
[[ "$(sha256sum "$k00_freeze_rel" | awk '{print $1}')" == "$k00_freeze_sha" ]]
sha256sum -c "$k00_freeze_rel" >/dev/null
chmod -R a-w "$k00_source"
[[ -z "$(find "$k00_source" -type f -perm /222 -print -quit)" ]]

nohup bash "$k00_source/$k00_wrapper" \
  "$k00_source" "$k00_job" "$k00_tag" \
  402653184 21600 21000 "$k00_freeze_rel" "$k00_freeze_sha" \
  "$k00_archive" "$k00_archive_sha" \
  >"$k00_outer_stdout" 2>"$k00_outer_stderr" </dev/null &
k00_pid=$!
printf '%s\n' "$k00_pid" > "$k00_pidfile"
printf 'tag=%s\npid=%s\nsource_freeze_sha256=%s\nsource_archive_sha256=%s\n' \
  "$k00_tag" "$k00_pid" "$k00_freeze_sha" "$k00_archive_sha"
