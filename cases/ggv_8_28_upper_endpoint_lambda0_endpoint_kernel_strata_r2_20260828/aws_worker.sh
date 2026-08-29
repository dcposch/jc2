#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
lane=$2
source_root="$job_dir/source/jc2/cases"
case_dir="$source_root/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r2_20260828"
input_case="$source_root/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_components_r1_20260828"
matrix="$input_case/input/symbolic_quadratic_q_rankdrop.sing"
fitting="$input_case/input/FITTING_STRATA_RAW.sing"
content="$input_case/input/COFACTOR_CONTENT.txt"
output_dir="$job_dir/output"
records_dir="$job_dir/records"
compiled_base="$output_dir/compiled/base"
compiled_branches="$output_dir/compiled/branches"
census_dir="$output_dir/census"
run_dir="$output_dir/run"

[[ "$lane" == p || "$lane" == c8q1 || "$lane" == c8p || "$lane" == q1p_triple ]]
deadline=$((SECONDS + 30))
while [[ ! -f "$records_dir/REGISTERED" ]]; do
  if (( SECONDS >= deadline )); then
    printf '%s\n' NO_VERDICT_REGISTRATION_TIMEOUT >"$output_dir/TERMINAL"
    exit 30
  fi
  sleep 0.05
done

zero_swap() {
  local total free
  total=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo)
  free=$(awk '/^SwapFree:/{print $2}' /proc/meminfo)
  [[ "$total" == 0 && "$free" == 0 ]]
}

stage() {
  local name=$1 cap=$2 time_file=$3 stdout_file=$4 stderr_file=$5
  shift 5
  mkdir -p "$output_dir/stages"
  printf '%s\n' "$name" >"$output_dir/CURRENT_STAGE"
  if ! zero_swap; then
    printf '%s\n' 90 >"$output_dir/stages/${name}.rc"
    return 90
  fi
  set +e
  /usr/bin/time -v -o "$time_file" \
    timeout --foreground --signal=TERM --kill-after=30s "$cap" \
    prlimit --as=103079215104 --fsize=34359738368 \
    taskset --cpu-list 1 env PYTHONDONTWRITEBYTECODE=1 "$@" \
    >"$stdout_file" 2>"$stderr_file"
  local rc=$?
  set -e
  printf '%s\n' "$rc" >"$output_dir/stages/${name}.rc"
  if ! zero_swap; then
    printf '%s\n' 91 >"$output_dir/stages/${name}.rc"
    return 91
  fi
  return "$rc"
}

mkdir -p "$compiled_base" "$compiled_branches" "$census_dir" "$run_dir"
printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 -B "$case_dir/aws_preflight.py" --run-dir "$job_dir" \
  --job-tag "$(basename "$job_dir")" --lane "$lane" \
  --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || {
    printf '%s\n' NO_VERDICT_PREFLIGHT_OR_ACTIVE_CONFLICT >"$output_dir/TERMINAL"
    exit 31
  }
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$case_dir"
sha256sum -c SOURCE.sha256 >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"
  exit 32
}
sha256sum -c PREREGISTRATION.sha256 >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || {
  printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"
  exit 33
}

stage ADAPTER_SELFCHECK 180 "$output_dir/selfcheck.time" "$output_dir/selfcheck.stdout" "$output_dir/selfcheck.stderr" \
  python3 -B "$case_dir/selfcheck_strata.py" --case-dir "$case_dir" \
    --matrix "$matrix" --fitting "$fitting" --content "$content" || {
      printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK >"$output_dir/TERMINAL"
      exit 34
    }
grep -q '^STRATA_ADAPTER_SELFCHECK_PASS$' "$output_dir/selfcheck.stdout" || {
  printf '%s\n' NO_VERDICT_ADAPTER_SELFCHECK_MARKER >"$output_dir/TERMINAL"
  exit 35
}

stage BUILD_BASE 90 "$output_dir/build_base.time" "$output_dir/build_base.stdout" "$output_dir/build_base.stderr" \
  python3 -B "$case_dir/build_strata_scripts.py" --phase base \
    --matrix "$matrix" --fitting "$fitting" --content "$content" \
    --output-dir "$compiled_base" || {
      printf '%s\n' NO_VERDICT_BUILD_BASE >"$output_dir/TERMINAL"
      exit 36
    }

cd "$census_dir"
stage FACTOR_CENSUS 300 "$output_dir/factor_census.time" "$output_dir/factor_census.stdout" "$output_dir/factor_census.stderr" \
  Singular -q "$compiled_base/factor_census.sing" || {
    printf '%s\n' NO_VERDICT_FACTOR_CENSUS >"$output_dir/TERMINAL"
    exit 37
  }
for marker in \
  'RAW_CONTENT_DISTINCT_FACTOR_COUNT=3' \
  'P_IRREDUCIBLE_FACTOR_COUNT=1' \
  'P_LINEAR_C8_IDENTITY=1' \
  'RAW_CONTENT_DIVISIBLE_P_C8_Q1=1' \
  'FACTOR_CENSUS_PASS=1'; do
  grep -q "^${marker}$" "$output_dir/factor_census.stdout" || {
    printf '%s\n' NO_VERDICT_FACTOR_OR_IRREDUCIBILITY_DISAGREEMENT >"$output_dir/TERMINAL"
    exit 38
  }
done

stage BUILD_BRANCHES 90 "$output_dir/build_branches.time" "$output_dir/build_branches.stdout" "$output_dir/build_branches.stderr" \
  python3 -B "$case_dir/build_strata_scripts.py" --phase branches \
    --matrix "$matrix" --census-dir "$census_dir" --output-dir "$compiled_branches" || {
      printf '%s\n' NO_VERDICT_BUILD_BRANCHES >"$output_dir/TERMINAL"
      exit 39
    }

printf 'stratum|status|method|script\n' >"$output_dir/STRATUM_VERDICTS.tsv"
survivors=0
dead=0
failed=0

run_one() {
  local label=$1 method=$2 script=$3 cap=$4
  local stem
  stem=$(basename "$script" .sing)
  local parse_script="${script%.sing}_parse.sing"
  if [[ -f "$parse_script" ]]; then
    stage "PARSE_${label}" 90 "$run_dir/${stem}.parse.time" "$run_dir/${stem}.parse.stdout" "$run_dir/${stem}.parse.stderr" \
      Singular -q "$parse_script" || {
        printf '%s|NO_VERDICT_PARSE|%s|%s\n' "$label" "$method" "$stem" >>"$output_dir/STRATUM_VERDICTS.tsv"
        failed=$((failed + 1))
        return
      }
    grep -q "^BRANCH_FULL_MATRIX_PARSE_PASS=${label}$" "$run_dir/${stem}.parse.stdout" || {
      printf '%s|NO_VERDICT_PARSE_MARKER|%s|%s\n' "$label" "$method" "$stem" >>"$output_dir/STRATUM_VERDICTS.tsv"
      failed=$((failed + 1))
      return
    }
  fi
  cd "$run_dir"
  stage "KERNEL_${label}" "$cap" "$run_dir/${stem}.time" "$run_dir/${stem}.stdout" "$run_dir/${stem}.stderr" \
    Singular -q "$script" || true
  if grep -q '^KERNEL_REPLAY_ZERO=1$' "$run_dir/${stem}.stdout" && \
     grep -q '^EXACT_GENERIC_ENDPOINT_SURVIVOR=1$' "$run_dir/${stem}.stdout"; then
    printf '%s|PASS_EXACT_GENERIC_ENDPOINT_SURVIVOR|%s|%s\n' "$label" "$method" "$stem" >>"$output_dir/STRATUM_VERDICTS.tsv"
    survivors=$((survivors + 1))
  elif grep -q '^KERNEL_REPLAY_ZERO=1$' "$run_dir/${stem}.stdout" && \
       grep -q '^GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING=1$' "$run_dir/${stem}.stdout"; then
    printf '%s|GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING|%s|%s\n' "$label" "$method" "$stem" >>"$output_dir/STRATUM_VERDICTS.tsv"
    dead=$((dead + 1))
  else
    printf '%s|NO_VERDICT_ADAPTER_CAP_OR_REPLAY|%s|%s\n' "$label" "$method" "$stem" >>"$output_dir/STRATUM_VERDICTS.tsv"
    failed=$((failed + 1))
  fi
}

if [[ "$lane" == p ]]; then
  stage PARSE_P_GENERIC 90 "$run_dir/p_generic.parse.time" "$run_dir/p_generic.parse.stdout" "$run_dir/p_generic.parse.stderr" \
    Singular -q "$compiled_base/parse_p_generic.sing" || {
      printf '%s\n' NO_VERDICT_P_GENERIC_PARSE >"$output_dir/TERMINAL"
      exit 40
    }
  grep -q '^FULL_MATRIX_PARSE_PASS=P_GENERIC$' "$run_dir/p_generic.parse.stdout" || {
    printf '%s\n' NO_VERDICT_P_GENERIC_PARSE_MARKER >"$output_dir/TERMINAL"
    exit 41
  }
  run_one P_GENERIC exact_function_field_linear_c8_chart "$compiled_base/p_generic.sing" 3600
elif [[ "$lane" == c8q1 ]]; then
  stage PARSE_C8_Q1 90 "$run_dir/c8_q1.parse.time" "$run_dir/c8_q1.parse.stdout" "$run_dir/c8_q1.parse.stderr" \
    Singular -q "$compiled_base/parse_c8_q1.sing" || {
      printf '%s\n' NO_VERDICT_C8_Q1_PARSE >"$output_dir/TERMINAL"
      exit 42
    }
  grep -q '^FULL_MATRIX_PARSE_PASS=C8_Q1$' "$run_dir/c8_q1.parse.stdout" || {
    printf '%s\n' NO_VERDICT_C8_Q1_PARSE_MARKER >"$output_dir/TERMINAL"
    exit 43
  }
  run_one C8_Q1_GENERIC exact_function_field "$compiled_base/c8_q1.sing" 3600
else
  while IFS='|' read -r family branch multiplicity factor_sha method solved script_name; do
    [[ "$family" == family ]] && continue
    if [[ "$lane" == c8p && "$family" != C8P ]]; then
      continue
    fi
    if [[ "$lane" == q1p_triple && "$family" != Q1P && "$family" != TRIPLE ]]; then
      continue
    fi
    cap=2400
    [[ "$lane" == q1p_triple ]] && cap=1500
    run_one "${family}_BRANCH_${branch}" "$method" "$compiled_branches/$script_name" "$cap"
  done <"$compiled_branches/BRANCH_MANIFEST.tsv"
fi

printf 'SURVIVORS=%s\nGENERIC_DEAD=%s\nFAILED=%s\n' "$survivors" "$dead" "$failed" >"$output_dir/LANE_COUNTS.txt"
if (( survivors > 0 )); then
  printf '%s\n' PASS_EXACT_GENERIC_ENDPOINT_SURVIVOR >"$output_dir/LANE_VERDICT"
  printf '%s\n' EXACT_GENERIC_ENDPOINT_SURVIVOR_FOUND >"$output_dir/VERDICT"
elif (( failed == 0 && dead > 0 )); then
  printf '%s\n' GENERIC_STRATA_ENDPOINT_DEAD_RANK_JUMPS_PENDING >"$output_dir/LANE_VERDICT"
  printf '%s\n' NO_VERDICT_RANK_JUMP_SUBSTRATA_PENDING >"$output_dir/VERDICT"
else
  printf '%s\n' NO_VERDICT_ADAPTER_CAP_OR_REPLAY >"$output_dir/LANE_VERDICT"
  printf '%s\n' NO_VERDICT_INCOMPLETE_STRATA >"$output_dir/VERDICT"
fi
find "$census_dir" "$compiled_base" "$compiled_branches" "$run_dir" -type f -print0 | \
  sort -z | xargs -0 sha256sum >"$output_dir/EXACT_ARTIFACTS.sha256"
zero_swap || {
  printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"
  exit 91
}
printf '%s\n' ENDPOINT_STRATA_JOB_COMPLETE >"$output_dir/TERMINAL"
printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"
