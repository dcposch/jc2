#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 8 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
prime=$4
cap=$5
wall=$6
archive_sha=$7
expected_host=$8
package=cases/max12_812_order2_p0_total_rees_j2_a1_w19_tg19_7_compatibility_v39_20260827

mkdir -p "$job/run" "$job/mutation"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nselector_prime=%s\nsource_archive_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$prime" "$archive_sha" \
  > "$job/launch_registration.txt"
if [[ "$expected_host" != "$(hostname)" ]]; then exit 126; fi

cd "$root"
sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap"
python=/home/ubuntu/venvs/td6/bin/python
"$python" -c 'import flint; assert flint.__version__ == "0.9.0"'

bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_compiler" \
  timeout "$wall" "$python" "$package/solve_w19_compatibility_v39.py" "$job/compiled" \
  --selector-prime "$prime" --registered-lane "$tag"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" \
  "$python" "$package/validate_w19_compatibility_v39.py" \
  --result "$job/compiled/result.json" \
  --compiler-stdout "$job/run/${tag}_compiler.stdout" \
  --compiler-stderr "$job/run/${tag}_compiler.stderr" \
  --launch-registration "$job/launch_registration.txt" \
  --selector-prime "$prime" --registered-lane "$tag" --output "$job/RESULT.json"
grep -Fx 'PASS-A1-W19-TG19-7-COMPATIBILITY-V39' "$job/run/${tag}_validator.stdout" >/dev/null

"$python" "$package/mutate_target_v39.py" --result "$job/compiled/result.json" \
  --output "$job/mutation/mutated_result.json" > "$job/mutation/mutator.stdout" \
  2> "$job/mutation/mutator.stderr"
set +e
"$python" "$package/validate_w19_compatibility_v39.py" \
  --result "$job/mutation/mutated_result.json" \
  --compiler-stdout "$job/run/${tag}_compiler.stdout" \
  --compiler-stderr "$job/run/${tag}_compiler.stderr" \
  --launch-registration "$job/launch_registration.txt" \
  --selector-prime "$prime" --registered-lane "$tag" \
  --output "$job/mutation/SHOULD_NOT_EXIST.json" \
  > "$job/mutation/validator.stdout" 2> "$job/mutation/validator.stderr"
mutation_rc=$?
set -e
printf '%s\n' "$mutation_rc" > "$job/mutation/validator.exit_status"
if [[ "$mutation_rc" -eq 0 || -e "$job/mutation/SHOULD_NOT_EXIST.json" ]]; then exit 93; fi
if grep -Fq 'PASS-A1-W19-TG19-7-COMPATIBILITY-V39' "$job/mutation/validator.stdout"; then exit 94; fi
grep -F 'target polynomial mutation or bridge failure' "$job/mutation/validator.stderr" >/dev/null

if grep -ERq 'Traceback|FAIL_|Killed|out of memory' "$job/run"; then exit 91; fi
(
  cd "$job"
  LC_ALL=C find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum
) > "$job/EVIDENCE.sha256"
