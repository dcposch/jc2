#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 5 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3; characteristic=$4; cap=$5
case "$host" in Box02) target=ubuntu@34.203.207.55 ;; Box03) target=ubuntu@98.80.65.144 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827
v20=cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827
v23=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827
v28case=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827
replay=cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py
tails=cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
tag="max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_${stamp}_${suffix}"
root="/home/ubuntu/jobs/$tag/source"; job="$root/$package/aws_${suffix}"
tarball=$(mktemp -t j2-a1-boundary-prolong-g17-v30.XXXXXX.tar.gz); trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" "$package" "$v20/export_allrows_g13_g14_v20.py" "$v23/census_j2_typed_v23.py" "$v23/output_r1" "$v28case/prolong_boundary_g16_v28.py" "$v28case/aws_q/compiled" "$replay" "$tails" ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball"|awk '{print $1}'); opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"; scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" "cd '$root' && test \"\$(sha256sum source.tar.gz|awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws.sh' '$root' '$job' '$tag' '$characteristic' '$cap' 1800 1800 '$sha' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$host" "$job" "$tag" "$sha"
