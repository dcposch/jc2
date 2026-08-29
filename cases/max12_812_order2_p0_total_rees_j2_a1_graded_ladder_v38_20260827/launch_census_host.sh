#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then exit 64; fi
host=$1
stamp=$2
cap=$3
case "$host" in
  r6d) target=ubuntu@3.91.104.135; host_label=r6d ;;
  Box01) target=ubuntu@54.175.21.169; host_label=box01 ;;
  *) exit 65 ;;
esac
package=cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_20260827
v37=cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827
v23=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827
v28=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827
v30=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827
v33=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827
v35=cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827
tag="max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_${stamp}_census_${host_label}"
root="/home/ubuntu/jobs/$tag/source"
job="$root/$package/aws_census_${host_label}"
tarball=$(mktemp -t j2-a1-graded-v38-census.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" \
  "$package/PREREGISTRATION_CENSUS.md" "$package/census_graded_ladder_v38.py" \
  "$package/validate_census_v38.py" "$package/run_aws_census.sh" "$package/FREEZE_CENSUS.sha256" \
  "$v37/solve_graded_ladder_v37.py" "$v23/census_j2_typed_v23.py" "$v23/output_r1" \
  "$v28/aws_q/compiled" "$v30/aws_q/compiled" "$v33/aws_q/compiled" "$v35/aws_q/compiled" \
  ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball" | awk '{print $1}')
opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"
scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" "cd '$root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws_census.sh' '$root' '$job' '$tag' '$cap' 3600 '$sha' '$host_label' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$host" "$job" "$tag" "$sha"
