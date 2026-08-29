#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then exit 64; fi
host=$1
stamp=$2
characteristic=$3
suffix=$4
case "$host" in
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
case "$characteristic" in 0|65521) ;; *) exit 66 ;; esac
package=cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_20260826
tag="max12_812_order2_p0_cusp_raw_g12_cech_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t p0-cusp-raw-g12-cech.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" \
  "$package" \
  cases/max12_812_order2_p0_cusp_g10_g11_20260826 \
  cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  xmodel/max12-812-order2-p0-cusp-successor-design-20260826.md \
  xmodel/max12-812-order2-zero-load-p0-successor-design-20260826.md \
  xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md \
  xmodel/max12-812-order2-square-third-tail-sharp-v2-promotion-20260826.md \
  xmodel/max12-812-order2-p0-odd-grade14-unit-elimination-promotion-20260826.md \
  xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md \
  ops/aws_exact_lane.sh
ssh_options=(-i "${HOME}/.ssh/claude-cli.pem" -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' 16777216 '$characteristic' 600 1800 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"
