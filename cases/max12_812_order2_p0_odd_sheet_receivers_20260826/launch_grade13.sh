#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then exit 64; fi
host=$1
prime=$2
stamp=$3
case "$host:$prime" in
  Box03:32003) ssh_target=ubuntu@98.80.65.144 ;;
  r6d:65521) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
package=cases/max12_812_order2_p0_odd_sheet_receivers_20260826
tag="max12_812_order2_p0_odd_g13_p${prime}_${stamp}_${host}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${host}_g13_p${prime}"
archive=$(mktemp /tmp/jc2-p0-odd-g13.XXXXXX)
trap 'rm -f "$archive"' EXIT
tar -czf "$archive" \
  ops/aws_exact_lane.sh \
  "$package/analyze_grade13.py" \
  "$package/REGISTRATION_G13.md" \
  "$package/compile_receivers.py" \
  "$package/FREEZE.sha256" \
  "$package/FREEZE_G13.sha256" \
  "$package/RESULT.md" \
  "$package/launch_grade13.sh" \
  "$package/run_grade13_aws.sh" \
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
  "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_grade13_aws.sh' '$remote_root' '$remote_job' '$tag' '$prime' 8388608 1800 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'tag=%s\nremote_job=%s\n' "$tag" "$remote_job"
