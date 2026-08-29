#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 ]]; then exit 64; fi
stamp=$1
ssh_target=ubuntu@98.80.65.144
package=cases/max12_812_order2_p0_odd_sheet_receivers_20260826
tag="max12_812_order2_p0_odd_g14_exact_q_${stamp}_Box03"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_Box03_g14_exact_q"
archive=$(mktemp /tmp/jc2-p0-odd-g14-exact.XXXXXX)
trap 'rm -f "$archive"' EXIT
tar -czf "$archive" \
  ops/aws_exact_lane.sh \
  "$package/reduce_grade14_exact.py" \
  "$package/REGISTRATION_G14_EXACT.md" \
  "$package/extract_grade13_exact.py" \
  "$package/compile_receivers.py" \
  "$package/FREEZE.sha256" \
  "$package/FREEZE_G14_EXACT.sha256" \
  "$package/RESULT.md" \
  "$package/launch_grade14_exact.sh" \
  "$package/run_grade14_exact_aws.sh" \
  cases/max12_812_order2_p0_odd_face_g11_g12_20260826/compile_p0_odd_g11_g12.py \
  cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees.py \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  cases/max12_high_row_probe_20260824/shared_faber_probe.py \
  xmodel/max12-812-order2-p0-odd-sheet-terminal-taylor-pullback-design-20260826.md \
  xmodel/max12-812-order2-p0-odd-face-g11-g12-design-20260826.md \
  xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md \
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md \
  xmodel/max12-812-order2-square-third-tail-sharp-v2-promotion-20260826.md \
  xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md \
  xmodel/max12-812-order2-p0-odd-grade13-triangular-prolongation-20260826.md
ssh_options=(-i "${HOME}/.ssh/claude-cli.pem" -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$archive" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_grade14_exact_aws.sh' '$remote_root' '$remote_job' '$tag' 33554432 1800 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'tag=%s\nremote_job=%s\n' "$tag" "$remote_job"

