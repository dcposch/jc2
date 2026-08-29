#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 ]]; then exit 64; fi
host=$1
stamp=$2
case "$host" in
  Box03) ssh_target=ubuntu@98.80.65.144 ;;
  r6d) ssh_target=ubuntu@100.26.198.153 ;;
  *) exit 65 ;;
esac
package=cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826
tag="max12_812_order2_p0_odd_row5_g14_replay_${stamp}_${host}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${host}"
archive=$(mktemp /tmp/jc2-p0-odd-row5-g14.XXXXXX)
trap 'rm -f "$archive"' EXIT
tar -czf "$archive" \
  ops/aws_exact_lane.sh \
  "$package/replay_row5_grade14.py" \
  "$package/REGISTRATION.md" \
  "$package/FREEZE.sha256" \
  "$package/launch_host.sh" \
  "$package/run_aws.sh" \
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json \
  cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees.py \
  cases/max12_high_row_probe_20260824/shared_faber_probe.py \
  xmodel/max12-812-order2-p0-odd-sheet-terminal-taylor-pullback-design-20260826.md \
  xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md
ssh_options=(-i "${HOME}/.ssh/claude-cli.pem" -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$archive" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" \
  "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' 8388608 900 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'tag=%s\nremote_job=%s\n' "$tag" "$remote_job"

