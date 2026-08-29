#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V19 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: run_v19_aws.sh ROOT JOB TAG FREEZE RESULT EMITTER ONEPARAM" >&2
  exit 125
fi
root=$1
job=$2
tag=$3
freeze=$4
result=$5
emitter=$6
oneparam=$7
rel=cases/max12_812_order2_u2_62_k00_honest_reachability_type_v19_20260827
v18=cases/max12_812_order2_u2_62_k00_filtered_load_obstruction_v18r1_20260827/aws_p65521_box01_pass
review=xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md
mkdir -p "$job/run"
cd "$root"
sha256sum -c "$freeze" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
python3 "$rel/audit_reachability_types_v19.py" \
  "$result" "$emitter" "$oneparam" "$review" "$job/run/RESULT.json" \
  --entry K10 "$v18/output/solution_K10_D4.tsv" "$v18/output/emitted/rows_K10_D4.json" \
  --entry K6  "$v18/output/solution_K6_D3.tsv"  "$v18/output/emitted/rows_K6_D3.json" \
  --entry K2  "$v18/output/solution_K2_D2.tsv"  "$v18/output/emitted/rows_K2_D2.json" \
  > "$job/run/audit.stdout" 2> "$job/run/audit.stderr"
printf 'validator=PASS_K00_V19_REACHABILITY_TYPE_AUDIT\n' > "$job/run/FINAL.validation"
find "$job/run" -type f -print0 | sort -z | xargs -0 sha256sum > "$job/run/EVIDENCE.sha256"
