#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then exit 64; fi
host=$1
stamp=$2
suffix=$3
characteristic=$4
case "$host" in
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
case "$characteristic" in 0|65521) ;; *) exit 65 ;; esac

package=cases/max12_812_order2_p0_a_cech_g14_g15_20260826
tag="max12_812_order2_p0_a_cech_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${suffix}"
archive=$(mktemp -t p0-a-cech.XXXXXX.tar.gz)
trap 'rm -f "$archive"' EXIT
tar -czf "$archive" \
  "$package" \
  cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/compile_square_a_prolongation.py \
  cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/FREEZE.sha256 \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py \
  cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md \
  xmodel/max12-812-order2-square-a-prolongation-design-20260826.md \
  xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md \
  xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md \
  xmodel/max12-812-order2-square-third-tail-divisibility-theorem-20260826.md \
  xmodel/max12-812-order2-p0-dk0-support-exhaustion-ramified-closure-design-20260826.md \
  ops/aws_exact_lane.sh
ssh_options=(-i "${HOME}/.ssh/claude-cli.pem" -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$archive" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' 16777216 '$characteristic' 600 3600 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"

