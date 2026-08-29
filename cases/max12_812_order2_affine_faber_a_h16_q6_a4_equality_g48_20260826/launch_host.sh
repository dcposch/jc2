#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3; characteristic=$4
case "$host" in Box03) ssh_target=ubuntu@98.80.65.144 ;; r6d) ssh_target=ubuntu@100.26.198.153 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_affine_faber_a_h16_q6_a4_equality_g48_20260826
base=cases/max12_812_order2_affine_faber_a_mixed_sigma45_20260826
tails=cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
tag="max12_812_order2_affine_faber_a_h16_q6_a4_g48_${stamp}_${suffix}"
remote_root="/home/ubuntu/jobs/$tag/source"; remote_job="$remote_root/$package/aws_${suffix}"
tarball=$(mktemp -t affine-faber-a-h16-q6-a4-g48.XXXXXX.tar.gz); trap 'rm -f "$tarball"' EXIT
tar -czf "$tarball" "$package" "$base/compile_sigma45.py" "$tails"
archive_sha=$(sha256sum "$tarball" | awk '{print $1}')
ssh_options=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${ssh_options[@]}" "$ssh_target" "mkdir -p '$remote_root'"
scp "${ssh_options[@]}" "$tarball" "$ssh_target:$remote_root/source.tar.gz"
ssh "${ssh_options[@]}" "$ssh_target" "cd '$remote_root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$archive_sha' && tar -xzf source.tar.gz && mkdir -p '$remote_job' && nohup bash '$package/run_aws.sh' '$remote_root' '$remote_job' '$tag' '$characteristic' 33554432 1800 '$archive_sha' > '$remote_job.outer.stdout' 2> '$remote_job.outer.stderr' & echo \$!"
printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$host" "$remote_job" "$tag" "$archive_sha"
