#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 8 ]]; then exit 64; fi
host=$1
stamp=$2
suffix=$3
characteristic=$4
grade=$5
algorithm=$6
cap_kib=$7
engine_timeout=$8
case "$host" in
  Box02) ssh_target=ubuntu@34.203.207.55 ;;
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
case "$characteristic" in 0|65521) ;; *) exit 66 ;; esac
case "$grade" in 10|11|12) ;; *) exit 67 ;; esac
case "$algorithm" in sat|elim) ;; *) exit 68 ;; esac
package=cases/max12_812_order2_p0_total_rees_t_rs_chart_discovery_v11_20260826
v10=cases/max12_812_order2_p0_total_rees_t_rs_chart_discovery_v10_20260826
v9=cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826
tag="max12_812_order2_p0_total_rees_t_rs_chart_discovery_v11_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t p0-total-rees-t-rs-chart-v11.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" "$package" "$v10" "$v9" \
  xmodel/max12-812-order2-p0-total-rees-t-rs-implementation-audit-codex-20260826.md \
  xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md \
  ops/aws_exact_lane.sh
archive_sha=$(sha256sum "$tarball" | awk '{print $1}')
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$archive_sha' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && setsid -f bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' '$characteristic' '$grade' '$algorithm' '$cap_kib' 300 '$engine_timeout' '$archive_sha' </dev/null > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr'"
printf 'host=%s\n' "$host"
printf 'remote_job=%s\n' "$remote_job"
printf 'tag=%s\n' "$tag"
printf 'source_archive_sha256=%s\n' "$archive_sha"
