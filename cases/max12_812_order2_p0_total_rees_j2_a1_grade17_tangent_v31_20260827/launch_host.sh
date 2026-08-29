#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 5 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3; characteristic=$4; cap=$5
case "$host" in Box02) target=ubuntu@34.203.207.55 ;; Box03) target=ubuntu@98.80.65.144 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_p0_total_rees_j2_a1_grade17_tangent_v31_20260827
v23=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827
v28=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827
v30=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827
tag="max12_812_order2_p0_total_rees_j2_a1_grade17_tangent_v31_${stamp}_${suffix}"
root="/home/ubuntu/jobs/$tag/source"; job="$root/$package/aws_${suffix}"
tarball=$(mktemp -t j2-a1-grade17-tangent-v31.XXXXXX.tar.gz); trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" "$package" "$v23/census_j2_typed_v23.py" "$v23/output_r1" "$v28/aws_q/compiled" "$v30/aws_q/compiled" ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball" | awk '{print $1}'); opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"; scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" "cd '$root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws.sh' '$root' '$job' '$tag' '$characteristic' '$cap' 900 '$sha' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$host" "$job" "$tag" "$sha"
