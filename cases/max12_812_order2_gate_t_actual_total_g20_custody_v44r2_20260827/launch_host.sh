#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 4 ]]; then exit 64; fi
host=$1
stamp=$2
mode=$3
cap=$4
case "$host:$mode" in
  r6a:qcross) target=ubuntu@3.91.104.135 ;;
  r6b:p65521) target=ubuntu@34.204.74.226 ;;
  *) exit 65 ;;
esac
package=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r2_20260827
r1=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r1_20260827
parser=cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py
tag="max12_812_order2_gate_t_actual_total_g20_custody_v44r2_${stamp}_${mode}"
root="/home/ubuntu/jobs/$tag/source"
job="$root/$package/aws_${mode}"
tarball=$(mktemp -t actual-total-g20-v44r2.XXXXXX.tar.gz)
trap 'rm -f "$tarball"' EXIT
COPYFILE_DISABLE=1 tar -czf "$tarball" \
  "$package" \
  "$r1/compiler_pass_validator_failed_v1_aws_q_r6a/compiled" \
  "$r1/compiler_pass_validator_failed_v1_aws_q_r6a/run/"*_compiler.stdout \
  "$r1/compiler_pass_validator_failed_v1_aws_q_r6a/run/"*_compiler.stderr \
  "$r1/compiler_pass_validator_failed_v1_aws_p65521_r6b/compiled" \
  "$r1/compiler_pass_validator_failed_v1_aws_p65521_r6b/run/"*_compiler.stdout \
  "$r1/compiler_pass_validator_failed_v1_aws_p65521_r6b/run/"*_compiler.stderr \
  "$parser" ops/aws_exact_lane.sh
sha=$(sha256sum "$tarball" | awk '{print $1}')
opt=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes)
ssh "${opt[@]}" "$target" "mkdir -p '$root'"
scp "${opt[@]}" "$tarball" "$target:$root/source.tar.gz"
ssh "${opt[@]}" "$target" \
  "cd '$root' && test \"\$(sha256sum source.tar.gz | awk '{print \$1}')\" = '$sha' && tar -xzf source.tar.gz && mkdir -p '$job' && setsid -f bash '$package/run_aws.sh' '$root' '$job' '$tag' '$mode' '$cap' 1800 '$sha' </dev/null > '$job.outer.stdout' 2> '$job.outer.stderr'"
printf 'host=%s\ntarget=%s\nremote_job=%s\ntag=%s\nsource_archive_sha256=%s\n' \
  "$host" "$target" "$job" "$tag" "$sha"

