#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 6 ]]; then exit 64; fi
host=$1
stamp=$2
suffix=$3
prime=$4
cap=$5
labels_csv=$6
case "$host" in
  r6d) target=ubuntu@3.91.104.135; host_label=r6d ;;
  Box01) target=ubuntu@54.175.21.169; host_label=box01 ;;
  *) exit 65 ;;
esac
if [[ "$suffix" != "q$prime" ]]; then exit 66; fi
case "$prime" in 65521|65519|65497|65479) ;; *) exit 67 ;; esac
package=cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_20260827
v37=cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827
v23=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827
v28=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827
v30=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827
v33=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827
v35=cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827
bundle="max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_${stamp}_${suffix}_bundle"
root="/home/ubuntu/jobs/$bundle/source"
tarball=$(mktemp -t j2-a1-graded-v38-v2.XXXXXX.tar.gz)
COPYFILE_DISABLE=1 tar -czf "$tarball" \
  "$package/PREREGISTRATION.md" "$package/solve_graded_ladder_v38.py" \
  "$package/validate_graded_ladder_v38.py" "$package/run_aws.sh" "$package/launch_host.sh" \
  "$package/launch_host_v2.sh" "$package/FREEZE.sha256" "$package/FREEZE_LAUNCH_V2.sha256" \
  "$package/aws_census_r6d/compiled/census.json" "$package/aws_census_r6d/RESULT.json" \
  "$package/aws_control_census_box01/compiled/census.json" "$package/aws_control_census_box01/RESULT.json" \
  "$v37/solve_graded_ladder_v37.py" "$v23/census_j2_typed_v23.py" "$v23/output_r1" \
  "$v28/aws_q/compiled" "$v30/aws_q/compiled" "$v33/aws_q/compiled" "$v35/aws_q/compiled" \
  ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball" | awk '{print $1}')
opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"
scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" "cd '$root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && sha256sum -c '$package/FREEZE_LAUNCH_V2.sha256'"
IFS=',' read -ra labels <<< "$labels_csv"
for target_label in "${labels[@]}"; do
  case "$target_label" in
    i1_j0|i1_j1|i1_j2|i1_j3|i1_j4|i1_j5|i2_j0|i2_j1|i2_j2|i2_j3|i3_j0|i3_j1|i3_j2|i4_j0|i4_j1|i5_j0) ;;
    *) exit 68 ;;
  esac
  tag="max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_${stamp}_${suffix}_${target_label}"
  job="$root/$package/aws_${suffix}_${target_label}"
  ssh "${opt[@]}" "$target" "cd '$root' && mkdir -p '$job' && setsid -f bash '$package/run_aws.sh' '$root' '$job' '$tag' '$prime' '$cap' 21600 '$sha' '$host_label' '$target_label' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
  printf 'host=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$host" "$job" "$tag" "$sha"
done
