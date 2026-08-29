#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then
  echo "usage: $0 HOST MODE CHARACTERISTIC UTC_STAMP" >&2
  exit 64
fi
host=$1
mode=$2
characteristic=$3
stamp=$4
case "$host" in
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
case "$mode:$characteristic" in
  terminal:0|taylor0:0|taylor1:65521) ;;
  *) exit 66 ;;
esac
package=cases/max12_812_order2_p0_odd_sheet_receivers_20260826
tag="max12_812_order2_p0_odd_${mode}_p${characteristic}_${stamp}_${host}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${host}_${mode}_p${characteristic}"
archive=$(mktemp /tmp/jc2-p0-odd-receivers.XXXXXX.tar.gz)
trap 'rm -f "$archive"' EXIT
tar -czf "$archive" \
  ops/aws_exact_lane.sh \
  "$package" \
  cases/max12_812_order2_p0_odd_face_g11_g12_20260826/compile_p0_odd_g11_g12.py \
  cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees.py \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  cases/max12_high_row_probe_20260824/shared_faber_probe.py \
  xmodel/max12-812-order2-p0-odd-sheet-terminal-taylor-pullback-design-20260826.md \
  xmodel/max12-812-order2-p0-odd-face-g11-g12-design-20260826.md \
  xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md \
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md \
  xmodel/max12-812-order2-square-third-tail-sharp-v2-promotion-20260826.md \
  xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md
ssh_options=(-i "${HOME}/.ssh/claude-cli.pem" -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$archive" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' 33554432 '$mode' '$characteristic' 5400 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nmode=%s\ncharacteristic=%s\ntag=%s\nremote_root=%s\nremote_job=%s\n' \
  "$host" "$mode" "$characteristic" "$tag" "$remote_root" "$remote_job"
