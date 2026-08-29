#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3; cap=$4
case "$host" in Box02) target=ubuntu@34.203.207.55 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_p0_total_rees_j2_a1_rho0_unit_screen_g16_v29_20260827
v23=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827
v28=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/aws_q/compiled
tag="max12_812_order2_p0_total_rees_j2_a1_rho0_unit_g16_v29_r1_${stamp}_${suffix}"
root="/home/ubuntu/jobs/$tag/source"; job="$root/$package/aws_${suffix}_r1"
tarball=$(mktemp -t j2-a1-rho0-unit-g16-v29r1.XXXXXX.tar.gz); trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" "$package" "$v23/census_j2_typed_v23.py" "$v23/output_r1" "$v28" ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball"|awk '{print $1}'); opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"; scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" "cd '$root' && test \"\$(sha256sum source.tar.gz|awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws_r1.sh' '$root' '$job' '$tag' 0 '$cap' 600 7200 '$sha' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$host" "$job" "$tag" "$sha"
