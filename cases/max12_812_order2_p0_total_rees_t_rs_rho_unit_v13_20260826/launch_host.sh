#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 7 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3; characteristic=$4; algorithm=$5; cap_kib=$6; engine_timeout=$7
case "$host" in
  Box02) ssh_target=ubuntu@34.203.207.55 ;;
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
package=cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v13_20260826
v12=cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v12_20260826
v9=cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826
tag="max12_812_order2_p0_total_rees_t_rs_rho_unit_v13_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"; remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t p0-total-rees-t-rs-rho-unit-v13.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" "$package" "$v12" "$v9" ops/aws_exact_lane.sh
archive_sha=$(sha256sum "$tarball" | awk '{print $1}')
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$archive_sha' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && setsid -f bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' '$characteristic' '$algorithm' '$cap_kib' '$engine_timeout' '$archive_sha' </dev/null > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr'"
printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$host" "$remote_job" "$tag" "$archive_sha"
