#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3
case "$host" in Box03) ssh_target=ubuntu@98.80.65.144 ;; r6d) ssh_target=ubuntu@100.26.198.153 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_affine_faber_a_graph_relative_h15_h18_cone_20260826
support=cases/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826
tag="max12_812_order2_affine_faber_a_graph_relative_h15_h18_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"; remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t affine-faber-a-graph-relative-h15-h18.XXXXXX.tar.gz); trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" "$package" "$support/evidence/Box03/aws_q/run/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826T164514Z_q.stdout" "$support/evidence/r6d/aws_p65521/run/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826T164514Z_p65521.stdout"
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' 8388608 300 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"
