#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then exit 64; fi
target=$1
stamp=$2
cap=$3
package=cases/max12_812_order2_gate_t_drho_a2d3_composition_v45_20260827
v44=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44_20260827
v44r1=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r1_20260827
v44r3=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r3_20260827
v20=cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827
v28=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827
parser=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py
replay=cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py
tails=cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
d1=cases/max12_812_order2_square_owner_d1_unique_ac_d23_lowa6_local_row_20260826
tag="max12_812_order2_gate_t_drho_a2d3_composition_v45_${stamp}_q"
root="/home/ubuntu/jobs/$tag/source"
job="$root/$package/aws_q"
tarball=$(mktemp -t drho-a2d3-v45.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" \
  "$package" "$v44/compile_actual_total_g20_v44.py" \
  "$v44r1/compile_actual_total_g20_v44r1.py" \
  "$v44r1/compiler_pass_validator_failed_v1_aws_q_r6a/compiled" \
  "$v44r3/FREEZE.sha256" "$v44r3/validate_frozen_v44r1_v44r3.py" \
  "$v44r3/validate_crosslane_v44r3.py" \
  "$v44r3/aws_qcross_r6a/RESULT_q.json" "$v44r3/aws_qcross_r6a/RESULT_CROSS.json" \
  "$v44r3/aws_p65521_r6b/RESULT_p65521.json" \
  "$v20/export_allrows_g13_g14_v20.py" "$v28/prolong_boundary_g16_v28.py" \
  "$parser" "$replay" "$tails" \
  "$d1/compile_local_row.py" "$d1/aws_v7_q/compiled/source_inventory.json" \
  "$d1/aws_v7_q/run/max12_812_order2_square_d1_unique_ac_d23_lowa6_localrow_v7_q_20260826.stdout" \
  xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-promotion-20260826.md \
  xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-hostile-review-grok-20260826.md \
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md \
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-hostile-review-opus5-20260827.md \
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-erratum-sol-20260827.md \
  ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball" | awk '{print $1}')
opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"
scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" \
  "cd '$root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws.sh' '$root' '$job' '$tag' '$cap' 3600 '$sha' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'target=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' "$target" "$job" "$tag" "$sha"
