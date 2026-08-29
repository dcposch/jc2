#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then exit 64; fi
host=$1; stamp=$2; suffix=$3
case "$host" in Box02) target=ubuntu@34.203.207.55 ;; Box03) target=ubuntu@98.80.65.144 ;; *) exit 65 ;; esac
package=cases/max12_812_order2_p0_total_rees_j2_a1_rho0_linear_dual_v27_20260827
v23=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827
tag="max12_812_order2_p0_total_rees_j2_a1_rho0_linear_dual_v27_${stamp}_${suffix}"
root="/home/ubuntu/jobs/$tag/source"; job="$root/$package/aws_${suffix}"
tarball=$(mktemp -t j2-a1-rho0-linear-dual-v27.XXXXXX.tar.gz); trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" "$package" "$v23/census_j2_typed_v23.py" "$v23/output_r1" ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball"|awk '{print $1}'); opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"; scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" "cd '$root' && test \"\$(sha256sum source.tar.gz|awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws.sh' '$root' '$job' '$tag' 419430400 1800 '$sha' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'remote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$job" "$tag" "$sha"
