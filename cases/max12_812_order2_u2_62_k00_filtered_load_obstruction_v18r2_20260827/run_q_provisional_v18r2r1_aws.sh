#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V18R2 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 10 ]]; then
  echo "usage: run_q_provisional_v18r2_aws.sh AWS_ROOT AWS_JOB TAG CAP_KIB EXTRACT_TIMEOUT MATRIX_TIMEOUT FREEZE COMPILED_V17_Q P_RESULT ROW_PRELUDE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
extract_timeout=$5
matrix_timeout=$6
freeze=$7
compiled_v17_q=$8
p_result=$9
row_prelude=${10}
rel=cases/max12_812_order2_u2_62_k00_filtered_load_obstruction_v18r2_20260827

mkdir -p "$aws_job/run/artifacts" "$aws_job/compiled" "$aws_job/output"
exact_input_script="$aws_job/compiled/extracted/exact_input.sing"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q\n'
  printf 'dependency=V17-p65521 provisional; no promotion before V17-Q\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'extract_timeout_seconds=%s\n' "$extract_timeout"
  printf 'matrix_timeout_seconds=%s\n' "$matrix_timeout"
  printf 'expected_pattern=K10:D4,K6:D3,K2:D2\n'
} > "$aws_job/launch_registration.txt"

cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"

python3 "$rel/extract_v17_exact_inputs_v18r2.py" \
  "$compiled_v17_q" "$p_result" "$exact_input_script" \
  > "$aws_job/run/extractor.stdout" 2> "$aws_job/run/extractor.stderr"

/usr/bin/time -v timeout "$extract_timeout" bash -c \
  'cd "$1" && exec Singular -q "$2"' _ \
  "$aws_job/run/artifacts" "$exact_input_script" \
  > "$aws_job/run/exact_input.stdout" 2> "$aws_job/run/exact_input.stderr"

python3 "$rel/build_exact_input_manifest_v18r2.py" \
  "$aws_job/run/artifacts" "$aws_job/run/exact_input.stdout" \
  "$compiled_v17_q" "$p_result" "$aws_job/run/PROVISIONAL_EXACT_INPUT.json" \
  > "$aws_job/run/input_validator.stdout" 2> "$aws_job/run/input_validator.stderr"

python3 "$rel/emit_filtered_load_v18r2.py" "$aws_job/output/emitted" \
  "$aws_job" "$p_result" "$row_prelude" --field Q --max-cutoff 4 \
  > "$aws_job/run/emitter.stdout" 2> "$aws_job/run/emitter.stderr"

g++ -O3 -std=c++17 "$rel/macaulay_rref_v18r2.cpp" \
  -o "$aws_job/output/macaulay_rref" -lflint -lgmp \
  > "$aws_job/run/compiler.stdout" 2> "$aws_job/run/compiler.stderr"
sha256sum "$aws_job/output/macaulay_rref" > "$aws_job/run/BINARY.sha256"

validator_args=()
: > "$aws_job/run/RUN_INDEX.tsv"
for spec in K10:4 K6:3 K2:2; do
  direction=${spec%%:*}
  last=${spec##*:}
  for ((cutoff=2; cutoff<=last; cutoff++)); do
    matrix="$aws_job/output/emitted/matrix_${direction}_D${cutoff}.tsv"
    solution="$aws_job/output/solution_${direction}_D${cutoff}.tsv"
    /usr/bin/time -v timeout "$matrix_timeout" "$aws_job/output/macaulay_rref" \
      --field Q "$matrix" "$solution" \
      > "$aws_job/run/${direction}_D${cutoff}.stdout" \
      2> "$aws_job/run/${direction}_D${cutoff}.stderr"
    consistent=$(awk '$1=="consistent" {print $2}' "$solution")
    if [[ "$consistent" != "0" && "$consistent" != "1" ]]; then
      echo "malformed exact consistency marker" >&2
      exit 70
    fi
    printf '%s\t%s\t%s\n' "$direction" "$cutoff" "$consistent" >> "$aws_job/run/RUN_INDEX.tsv"
    validator_args+=(--entry "$direction" "$matrix" "$solution")
    if [[ "$consistent" == "0" ]]; then
      break
    fi
  done
done

python3 "$rel/validate_filtered_load_v18r2.py" \
  "$aws_job/run/RESULT.json" "$aws_job/output/emitted/SOURCE_AUDIT.json" \
  --field Q "${validator_args[@]}" \
  > "$aws_job/run/validator.stdout" 2> "$aws_job/run/validator.stderr"
python3 "$rel/check_expected_q_v18r2.py" "$aws_job/run/RESULT.json" \
  > "$aws_job/run/target_gate.stdout" 2> "$aws_job/run/target_gate.stderr"
printf 'validator=PASS_K00_FILTERED_LOAD_V18R2_PROVISIONAL_Q\n' > "$aws_job/run/FINAL.validation"
find "$aws_job/output" "$aws_job/run" -type f -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/run/ENDPOINT_EVIDENCE.sha256.tmp"
mv "$aws_job/run/ENDPOINT_EVIDENCE.sha256.tmp" "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
