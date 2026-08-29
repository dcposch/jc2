#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 5 ]]; then
  printf 'usage: %s host remote_root config characteristic tag\n' "$0" >&2
  exit 64
fi
host=$1
remote_root=$2
config=$3
characteristic=$4
tag=$5
case "$host" in
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
case "$config" in generic|p0moving) ;; *) exit 66 ;; esac
case "$characteristic" in 0|65521) ;; *) exit 67 ;; esac

case_dir=cases/max12_812_order2_square_third_tail_sharp_20260826
remote_job="$remote_root/$case_dir/aws_${host}_${config}_${characteristic}"
tarball=$(mktemp -t square-third-sharp.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" \
  "$case_dir" \
  cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  xmodel/max12-812-order2-square-third-tail-divisibility-theorem-20260826.md \
  xmodel/max12-812-order2-zero-load-p0-successor-design-20260826.md \
  ops/aws_exact_lane.sh
ssh_options=(-i "${HOME}/.ssh/claude-cli.pem" -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$case_dir/run_aws.sh' '$remote_root' '$remote_job' '$tag' 16777216 '$config' '$characteristic' 600 3600 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"
