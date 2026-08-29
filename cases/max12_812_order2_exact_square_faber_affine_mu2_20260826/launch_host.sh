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

package=cases/max12_812_order2_exact_square_faber_affine_mu2_20260826
tag="max12_812_order2_faber_affine_mu2_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t faber-affine-mu2.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" \
  "$package" \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  cases/max12_812_order2_exact_square_pell_20260826/compile_exact_square_pell.py \
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md \
  xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md \
  xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md

ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' '$characteristic' 33554432 1800 /usr/bin/Singular > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"
