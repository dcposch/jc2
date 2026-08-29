#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3; characteristic=$4
case "$host" in
 Box02) ssh_target=ubuntu@34.203.207.55 ;;
 Box03) ssh_target=ubuntu@98.80.65.144 ;;
 r6d) ssh_target=ubuntu@100.26.198.153 ;;
 *) exit 65 ;;
esac
package=cases/max12_812_order2_affine_faber_a_h18_q7_a4_through_g54_sparse_v1_20260826
v5=cases/max12_812_order2_affine_faber_a_h17_q7_a3_through_g51_sparse_v5_20260826/compute_h17_q7_through_g51_v5.py
v2=cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v2_20260826/compute_h17_q7_g48_sparse.py
base=cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/compute_sparse_dag_v4.py
tails=cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
tag="max12_812_order2_affine_faber_a_h18_q7_a4_through_g54_v1_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"
remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t affine-faber-a-h18-q7-g54-v1.XXXXXX.tar.gz)
tar -czf "$tarball" "$package" "$v5" "$v2" "$base" "$tails"
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" "cd '$remote_root' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' '$characteristic' 16777216 1800 > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\n' "$host" "$remote_job" "$tag"
