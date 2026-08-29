#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3
case "$host" in Box02) ssh_target=ubuntu@34.203.207.55 ;; Box03) ssh_target=ubuntu@98.80.65.144 ;; r6d) ssh_target=ubuntu@100.26.198.153 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826
v4=cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/evidence
v6=cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/evidence
tag="max12_812_order2_affine_faber_a_h17_upper_graph_v10_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"; remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t affine-faber-a-h17-upper-v10.XXXXXX.tar.gz); trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" "$package" "$v4/Box02/aws_qdag/output/abstract_functional_support.json" "$v4/r6d/aws_pdag/output/abstract_functional_support.json" "$v6/Box02/aws_qsecondary/output/abstract_secondary_support.json" "$v6/r6d/aws_psecondary/output/abstract_secondary_support.json"
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' 8388608 600 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"
