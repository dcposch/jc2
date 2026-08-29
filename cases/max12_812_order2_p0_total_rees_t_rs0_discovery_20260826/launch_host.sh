#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then exit 64; fi
host=$1
stamp=$2
suffix=$3
characteristic=$4
case "$host" in
  Box02) ssh_target=ubuntu@34.203.207.55 ;;
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6a) ssh_target=ubuntu@3.91.104.135 ;;
  r6b) ssh_target=ubuntu@34.204.74.226 ;;
  r6c) ssh_target=ubuntu@54.167.205.167 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
case "$characteristic" in 0|32003|65521) ;; *) exit 66 ;; esac
package=cases/max12_812_order2_p0_total_rees_t_rs0_discovery_20260826
tag="max12_812_order2_p0_total_rees_t_rs0_discovery_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t p0-total-rees-t-rs0-discovery.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" \
  "$package" \
  cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py \
  cases/max12_812_order2_p0_cusp_g10_g11_20260826/compile_p0_cusp_g10_g11.py \
  cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/compile_raw_cusp_g12_cech_v2.py \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  xmodel/max12-812-order2-p0-total-rees-t-rs-implementation-audit-codex-20260826.md \
  xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md \
  ops/aws_exact_lane.sh
archive_sha=$(sha256sum "$tarball" | awk '{print $1}')
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$archive_sha' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' '$characteristic' 134217728 900 7200 '$archive_sha' > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' \
  "$host" "$remote_job" "$tag" "$archive_sha"
