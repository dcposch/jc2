#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 5 ]]; then exit 64; fi
host=$1
stamp=$2
suffix=$3
characteristic=$4
cap=$5
case "$host" in
  r6a) target=ubuntu@3.91.104.135 ;;
  r6b) target=ubuntu@34.204.74.226 ;;
  *) exit 65 ;;
esac
package=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r1_20260827
base=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44_20260827/compile_actual_total_g20_v44.py
v20=cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827
v28=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827
v33=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827
v35=cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827
parser=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py
replay=cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py
tails=cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
tag="max12_812_order2_gate_t_actual_total_g20_custody_v44r1_${stamp}_${suffix}"
root="/home/ubuntu/jobs/$tag/source"
job="$root/$package/aws_${suffix}"
tarball=$(mktemp -t actual-total-g20-v44r1.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" \
  "$package" "$base" \
  "$v20/export_allrows_g13_g14_v20.py" \
  "$v28/prolong_boundary_g16_v28.py" \
  "$v33/prolong_boundary_g18_v33.py" "$v33/aws_q/compiled" \
  "$v35/evaluate_grade19_orbit_v35.py" "$v35/aws_q/compiled" \
  "$parser" "$replay" "$tails" ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball" | awk '{print $1}')
opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"
scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" \
  "cd '$root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws.sh' '$root' '$job' '$tag' '$characteristic' '$cap' 3600 '$sha' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'host=%s\ntarget=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' \
  "$host" "$target" "$job" "$tag" "$sha"

