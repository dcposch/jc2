#!/usr/bin/env bash
set -Eeuo pipefail
job_dir=$1
case_dir="$job_dir/source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_replay_fix_r3_20260828"
builder_case="$job_dir/source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_replay_diag_r2_20260828"
r6_case="$job_dir/source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r6_20260828"
archive="$r6_case/custody/ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a.tar.gz"
output_dir="$job_dir/output"; records_dir="$job_dir/records"; compiled="$output_dir/compiled"
deadline=$((SECONDS + 30)); while [[ ! -f "$records_dir/REGISTERED" ]]; do if (( SECONDS >= deadline )); then printf '%s\n' NO_VERDICT_REGISTRATION_TIMEOUT >"$output_dir/TERMINAL"; exit 30; fi; sleep 0.05; done
zero_swap() { local total free; total=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo); free=$(awk '/^SwapFree:/{print $2}' /proc/meminfo); [[ "$total" == 0 && "$free" == 0 ]]; }
stage() { local name=$1 cap=$2; shift 2; printf '%s\n' "$name" >"$output_dir/CURRENT_STAGE"; zero_swap || return 90; set +e; /usr/bin/time -v -o "$output_dir/${name}.time" timeout --foreground --signal=TERM --kill-after=20s "$cap" prlimit --as=17179869184 --fsize=1073741824 taskset --cpu-list 1 env PYTHONDONTWRITEBYTECODE=1 "$@" >"$output_dir/${name}.stdout" 2>"$output_dir/${name}.stderr"; local rc=$?; set -e; printf '%s\n' "$rc" >"$output_dir/${name}.rc"; zero_swap || return 91; return "$rc"; }

mkdir -p "$output_dir" "$records_dir" "$compiled"; printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"
python3 -B "$case_dir/aws_preflight.py" --run-dir "$job_dir" --job-tag "$(basename "$job_dir")" --lane p --output "$records_dir/PREFLIGHT.json" >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr" || { printf '%s\n' NO_VERDICT_PREFLIGHT_OR_ACTIVE_CONFLICT >"$output_dir/TERMINAL"; exit 31; }
cd "$case_dir"; sha256sum -c SOURCE.sha256 >"$records_dir/SOURCE_CHECK.stdout" 2>"$records_dir/SOURCE_CHECK.stderr" || { printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"; exit 32; }; sha256sum -c PREREGISTRATION.sha256 >"$records_dir/PREREG_CHECK.stdout" 2>"$records_dir/PREREG_CHECK.stderr" || { printf '%s\n' NO_VERDICT_PREREG_DRIFT >"$output_dir/TERMINAL"; exit 33; }
stage BUILD_EXACT_REPLAY 60 python3 -B "$builder_case/build_replay_reducer_diag.py" --archive "$archive" --output-dir "$compiled" || { printf '%s\n' NO_VERDICT_ADAPTER_BUILD >"$output_dir/TERMINAL"; exit 34; }
grep -q '^REDUCER_DIAGNOSTIC_SCRIPT_SHA256_C8P_BRANCH_02=08bdc93c56b6e7ed8ab313413e9fd22af2eda098ef14814a9f6d68bbc8a46cf6$' "$output_dir/BUILD_EXACT_REPLAY.stdout" || { printf '%s\n' NO_VERDICT_ADAPTER_HASH >"$output_dir/TERMINAL"; exit 35; }
grep -q '^REDUCER_DIAGNOSTIC_SCRIPT_SHA256_TRIPLE_BRANCH_02=1feba464ee914d93935d4ef4165be7d260044940c6c28cb632f662b8cf7066ea$' "$output_dir/BUILD_EXACT_REPLAY.stdout" || { printf '%s\n' NO_VERDICT_ADAPTER_HASH >"$output_dir/TERMINAL"; exit 35; }

printf 'stratum|status|method|script_sha256\n' >"$output_dir/STRATUM_VERDICTS.tsv"; failed=0
for label in c8p_branch_02 triple_branch_02; do
  upper=$(printf '%s' "$label" | tr '[:lower:]' '[:upper:]'); branch_ok=1; cd "$output_dir"
  stage "KERNEL_${upper}" 180 Singular -q "$compiled/${label}_reducer_diag.sing" || branch_ok=0
  stdout="$output_dir/KERNEL_${upper}.stdout"
  for marker in 'AMBIENT_BRANCH_REDUCER_ZERO=1' 'QUOTIENT_DEFINING_IDEAL_NONEMPTY=1' 'QIDEAL_REDUCED_REPLAY_ZERO=1' 'QIDEAL_REDUCED_REPLAY_NONZERO_ENTRIES=0' 'MUTATION_QIDEAL_REDUCED_PIVOT_NONZERO=1' 'MUTATION_QIDEAL_REDUCED_REPLAY_ZERO=0' "REPLAY_REDUCER_MUTATION_CONTROL_PASS=${upper}" 'ENDPOINT_QUADRATIC=x14*x72+x1*x97' 'KERNEL_REPLAY_ZERO=1' 'ENDPOINT_PULLBACK_NONZERO_COEFFICIENTS=0' 'GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING=1'; do grep -q "^${marker}$" "$stdout" || branch_ok=0; done
  if [[ "$label" == c8p_branch_02 ]]; then expected_count=45; script_sha=08bdc93c56b6e7ed8ab313413e9fd22af2eda098ef14814a9f6d68bbc8a46cf6; else expected_count=78; script_sha=1feba464ee914d93935d4ef4165be7d260044940c6c28cb632f662b8cf7066ea; fi
  grep -q "^ENDPOINT_PULLBACK_COEFFICIENTS=${expected_count}$" "$stdout" || branch_ok=0
  if [[ "$branch_ok" -eq 1 ]]; then printf '%s|GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING|exact_qideal_reduced_replay|%s\n' "$upper" "$script_sha" >>"$output_dir/STRATUM_VERDICTS.tsv"; else printf '%s|NO_VERDICT_ADAPTER_OR_REPLAY|exact_qideal_reduced_replay|%s\n' "$upper" "$script_sha" >>"$output_dir/STRATUM_VERDICTS.tsv"; failed=$((failed + 1)); fi
done
zero_swap || { printf '%s\n' NO_VERDICT_SWAP_DRIFT >"$output_dir/TERMINAL"; exit 91; }
if [[ "$failed" -eq 0 ]]; then printf '%s\n' GENERIC_STRATA_ENDPOINT_DEAD_RANK_JUMPS_PENDING >"$output_dir/LANE_VERDICT"; printf '%s\n' NO_VERDICT_RANK_JUMP_SUBSTRATA_PENDING >"$output_dir/VERDICT"; else printf '%s\n' NO_VERDICT_INCOMPLETE_REPLAY >"$output_dir/LANE_VERDICT"; printf '%s\n' NO_VERDICT_INCOMPLETE_STRATA >"$output_dir/VERDICT"; fi
printf '%s\n' EXACT_REPLAY_FIX_JOB_COMPLETE >"$output_dir/TERMINAL"; printf '%s\n' COMPLETE >"$output_dir/CURRENT_STAGE"
