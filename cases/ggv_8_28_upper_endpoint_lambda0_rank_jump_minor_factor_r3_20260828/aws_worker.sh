#!/usr/bin/env bash
set -Eeuo pipefail
job_dir=$1; component=$2; source_root="$job_dir/source/jc2/cases"; case_dir="$source_root/ggv_8_28_upper_endpoint_lambda0_rank_jump_minor_factor_r3_20260828"; r2_case="$source_root/ggv_8_28_upper_endpoint_lambda0_rank_jump_fitting_census_r2_20260828"; output_dir="$job_dir/output"; records_dir="$job_dir/records"; compiled_dir="$output_dir/compiled"; run_dir="$output_dir/run"
case "$component" in
c8) archive="$r2_case/custody/ggv_lambda0_fitting_census_c8_r2_20260828T152000Z_r6a.terminal.tar.gz";;
q1) archive="$r2_case/custody/ggv_lambda0_fitting_census_q1_r2_20260828T152000Z_r6b.terminal.tar.gz";;
p) archive="$r2_case/custody/ggv_lambda0_fitting_census_p_r2_20260828T152000Z_r6c.terminal.tar.gz";;
c8_q1) archive="$r2_case/custody/ggv_lambda0_fitting_census_c8_q1_r2_20260828T152000Z_r6d.terminal.tar.gz";;
c8p02) archive="$r2_case/custody/ggv_lambda0_fitting_census_c8p02_r2_20260828T152000Z_r6e.terminal.tar.gz";;
q1p02) archive="$r2_case/custody/ggv_lambda0_fitting_census_q1p02_r2_20260828T152000Z_r6f.terminal.tar.gz";;
q1p03) archive="$r2_case/custody/ggv_lambda0_fitting_census_q1p03_r2_20260828T152000Z_r6g.terminal.tar.gz";;
triple02) archive="$r2_case/custody/ggv_lambda0_fitting_census_triple02_r2_20260828T152000Z_r6h.terminal.tar.gz";;
triple03) archive="$r2_case/custody/ggv_lambda0_fitting_census_triple03_r2_20260828T152000Z_r6i.terminal.tar.gz";;
*) exit 29;; esac
deadline=$((SECONDS+30)); while [[ ! -f "$records_dir/REGISTERED" ]]; do if ((SECONDS>=deadline)); then printf '%s\n' NO_VERDICT_REGISTRATION_TIMEOUT >"$output_dir/TERMINAL"; exit 30; fi; sleep .05; done
zero_swap(){ local t f; t=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo); f=$(awk '/^SwapFree:/{print $2}' /proc/meminfo); [[ "$t" == 0 && "$f" == 0 ]]; }
stage(){ local n=$1 cap=$2 tf=$3 of=$4 ef=$5; shift 5; mkdir -p "$output_dir/stages"; printf '%s\n' "$n" >"$output_dir/CURRENT_STAGE"; if ! zero_swap; then printf 90 >"$output_dir/stages/${n}.rc"; return 90; fi; set +e; /usr/bin/time -v -o "$tf" timeout --foreground --signal=TERM --kill-after=30s "$cap" prlimit --as=103079215104 --fsize=34359738368 taskset --cpu-list 1 env PYTHONDONTWRITEBYTECODE=1 "$@" >"$of" 2>"$ef"; local rc=$?; set -e; printf '%s\n' "$rc" >"$output_dir/stages/${n}.rc"; if ! zero_swap; then printf 91 >"$output_dir/stages/${n}.rc"; return 91; fi; return "$rc"; }
mkdir -p "$compiled_dir" "$run_dir" "$output_dir/stages"; printf PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 -B "$case_dir/aws_preflight.py" --run-dir "$job_dir" --job-tag "$(basename "$job_dir")" --component "$component" --output "$records_dir/PREFLIGHT.json" >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || { printf '%s\n' NO_VERDICT_PREFLIGHT_OR_CONFLICT >"$output_dir/TERMINAL"; exit 31; }; printf AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"
cd "$case_dir"; sha256sum -c SOURCE.sha256 >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || { printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"; exit 32; }; sha256sum -c PREREGISTRATION.sha256 >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || { printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"; exit 33; }
stage PYTHON_SELFCHECK 180 "$output_dir/selfcheck.time" "$output_dir/selfcheck.stdout" "$output_dir/selfcheck.stderr" python3 -B "$case_dir/selfcheck_minor_census.py" --case-dir "$case_dir" --component "$component" --archive "$archive" || { printf '%s\n' NO_VERDICT_PYTHON_SELFCHECK >"$output_dir/TERMINAL"; exit 34; }; grep -q '^MINOR_CENSUS_SELFCHECK_PASS$' "$output_dir/selfcheck.stdout" || { printf '%s\n' NO_VERDICT_PYTHON_SELFCHECK_MARKER >"$output_dir/TERMINAL"; exit 35; }
stage BACKEND_SELFCHECK 60 "$output_dir/backend_selfcheck.time" "$output_dir/backend_selfcheck.stdout" "$output_dir/backend_selfcheck.stderr" Singular -q "$case_dir/adapter_selfcheck.sing" || { printf '%s\n' NO_VERDICT_BACKEND_SELFCHECK >"$output_dir/TERMINAL"; exit 36; }; grep -q '^MINOR_BACKEND_ADAPTER_SELFCHECK_PASS$' "$output_dir/backend_selfcheck.stdout" || { printf '%s\n' NO_VERDICT_BACKEND_SELFCHECK_MARKER >"$output_dir/TERMINAL"; exit 37; }
stage BUILD_MINOR_CENSUS 300 "$output_dir/build.time" "$output_dir/build.stdout" "$output_dir/build.stderr" python3 -B "$case_dir/build_minor_census.py" --component "$component" --archive "$archive" --output-dir "$compiled_dir" || { printf '%s\n' NO_VERDICT_BUILD >"$output_dir/TERMINAL"; exit 38; }; grep -q '^MINOR_CENSUS_BUILD_PASS$' "$output_dir/build.stdout" || { printf '%s\n' NO_VERDICT_BUILD_MARKER >"$output_dir/TERMINAL"; exit 39; }
stage PARSE_MINOR_MATRIX 120 "$run_dir/parse.time" "$run_dir/parse.stdout" "$run_dir/parse.stderr" Singular -q "$compiled_dir/${component}_parse.sing" || { printf '%s\n' NO_VERDICT_PARSE >"$output_dir/VERDICT"; printf '%s\n' MINOR_FACTOR_JOB_COMPLETE >"$output_dir/TERMINAL"; exit 0; }; grep -q '^MINOR_MATRIX_PARSE_PASS=' "$run_dir/parse.stdout" || { printf '%s\n' NO_VERDICT_PARSE_MARKER >"$output_dir/VERDICT"; printf '%s\n' MINOR_FACTOR_JOB_COMPLETE >"$output_dir/TERMINAL"; exit 0; }
cd "$run_dir"; stage RUN_MINOR_CENSUS 3600 "$run_dir/minors.time" "$run_dir/minors.stdout" "$run_dir/minors.stderr" Singular -q "$compiled_dir/${component}_minors.sing" || true
status=NO_VERDICT_ADAPTER_CAP_OR_MARKER
if grep -q '^MINOR_FACTOR_CENSUS_COMPLETE=1$' "$run_dir/minors.stdout"; then
 if grep -q '^RESIDUAL_RANK=9$' "$run_dir/minors.stdout"; then
  if grep -q '^RAW_MINOR_SLOT_COUNT=550$' "$run_dir/minors.stdout" && grep -q '^STRUCTURALLY_MATCHABLE_SLOT_COUNT=172$' "$run_dir/minors.stdout"; then status=EXACT_RANK9_MINOR_FACTOR_CENSUS; fi
 else
  if grep -q '^RESIDUAL_RANK=6$' "$run_dir/minors.stdout" && grep -q '^BLOCK_A_RANK=4$' "$run_dir/minors.stdout" && grep -q '^BLOCK_B_RANK=2$' "$run_dir/minors.stdout" && grep -q '^OFFBLOCK_NONZERO=0$' "$run_dir/minors.stdout" && grep -q '^FORMAL_I6_SLOT_COUNT=97020$' "$run_dir/minors.stdout" && grep -q '^FORMAL_I6_SIGNED_PRODUCT_COUNT=1470$' "$run_dir/minors.stdout" && grep -q '^BLOCK_FITTING_IDENTITY_REPLAY=1$' "$run_dir/minors.stdout"; then status=EXACT_RANK6_BLOCK_MINOR_FACTOR_CENSUS; fi
 fi
fi
printf 'component|status\n%s|%s\n' "$component" "$status" >"$output_dir/COMPONENT_RESULT.tsv"
if [[ "$status" == EXACT_* ]]; then printf '%s\n' NO_VERDICT_MINOR_FACTOR_CENSUS_ONLY >"$output_dir/VERDICT"; else printf '%s\n' NO_VERDICT_ADAPTER_CAP_OR_MARKER >"$output_dir/VERDICT"; fi
find "$compiled_dir" "$run_dir" -type f -print0 | sort -z | xargs -0 sha256sum >"$output_dir/EXACT_ARTIFACTS.sha256"; zero_swap || { printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"; exit 91; }; printf '%s\n' MINOR_FACTOR_JOB_COMPLETE >"$output_dir/TERMINAL"; printf COMPLETE >"$output_dir/CURRENT_STAGE"

