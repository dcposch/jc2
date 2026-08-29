#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V18 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 9 ]]; then
  echo "usage: run_filtered_load_v18_aws.sh AWS_ROOT AWS_JOB TAG FIELD CAP_KIB TIMEOUT_SECONDS FREEZE V17_LANE ROW_PRELUDE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
field=$4
cap_kib=$5
timeout_seconds=$6
freeze=$7
v17_lane=$8
row_prelude=$9
rel=cases/max12_812_order2_u2_62_k00_filtered_load_obstruction_v18_20260827
engine_source=cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827/macaulay_rref.cpp
mkdir -p "$aws_job/run" "$aws_job/output"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=%s\n' "$field"
  printf 'timeout_seconds_per_matrix=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'v17_lane=%s\n' "$v17_lane"
  printf 'row_prelude=%s\n' "$row_prelude"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"
python3 "$rel/emit_filtered_load_v18.py" "$aws_job/output/emitted" \
  "$v17_lane" "$row_prelude" --field "$field" --max-cutoff 6 \
  > "$aws_job/run/emitter.stdout" 2> "$aws_job/run/emitter.stderr"
g++ -O3 -std=c++17 "$engine_source" -o "$aws_job/output/macaulay_rref" -lflint -lgmp \
  > "$aws_job/run/compiler.stdout" 2> "$aws_job/run/compiler.stderr"
sha256sum "$aws_job/output/macaulay_rref" > "$aws_job/run/BINARY.sha256"
validator_args=()
: > "$aws_job/run/RUN_INDEX.tsv"
for direction in K10 K6 K2; do
  for cutoff in 2 3 4 5 6; do
    matrix="$aws_job/output/emitted/matrix_${direction}_D${cutoff}.tsv"
    solution="$aws_job/output/solution_${direction}_D${cutoff}.tsv"
    /usr/bin/time -v timeout "$timeout_seconds" "$aws_job/output/macaulay_rref" \
      --field "$field" "$matrix" "$solution" \
      > "$aws_job/run/${direction}_D${cutoff}.stdout" \
      2> "$aws_job/run/${direction}_D${cutoff}.stderr"
    consistent=$(awk '$1=="consistent" {print $2}' "$solution")
    if [[ "$consistent" != "0" && "$consistent" != "1" ]]; then
      echo "malformed consistency marker" >&2
      exit 70
    fi
    printf '%s\t%s\t%s\n' "$direction" "$cutoff" "$consistent" >> "$aws_job/run/RUN_INDEX.tsv"
    validator_args+=(--entry "$direction" "$matrix" "$solution")
    if [[ "$consistent" == "0" ]]; then
      break
    fi
  done
done
python3 "$rel/validate_filtered_load_v18.py" \
  "$aws_job/run/RESULT.json" "$aws_job/output/emitted/SOURCE_AUDIT.json" \
  --field "$field" "${validator_args[@]}" \
  > "$aws_job/run/validator.stdout" 2> "$aws_job/run/validator.stderr"
printf 'validator=PASS_K00_FILTERED_LOAD_V18\n' > "$aws_job/run/FINAL.validation"
find "$aws_job/output" "$aws_job/run" -type f -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/run/ENDPOINT_EVIDENCE.sha256.tmp"
mv "$aws_job/run/ENDPOINT_EVIDENCE.sha256.tmp" "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
