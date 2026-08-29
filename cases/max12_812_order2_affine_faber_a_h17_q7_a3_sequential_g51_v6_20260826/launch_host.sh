#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3; characteristic=$4
case "$host" in Box02) ssh_target=ubuntu@34.203.207.55 ;; Box03) ssh_target=ubuntu@98.80.65.144 ;; r6d) ssh_target=ubuntu@100.26.198.153 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826
v5=cases/max12_812_order2_affine_faber_a_h17_q7_a3_through_g51_sparse_v5_20260826
qrows="$v5/evidence/Box03/aws_qg51/output/rows_g48_g51.json"
qfunctions="$v5/evidence/Box03/aws_qg51/output/functionals_g51.json"
prows="$v5/evidence/Box02/aws_pg51/output/rows_g48_g51.json"
pfunctions="$v5/evidence/Box02/aws_pg51/output/functionals_g51.json"
tag="max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"; remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t affine-faber-a-h17-q7-sequential-g51-v6.XXXXXX.tar.gz)
tar -czf "$tarball" "$package" "$qrows" "$qfunctions" "$prows" "$pfunctions"
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' '$characteristic' 8388608 900 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"
