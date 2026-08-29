#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 9 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
prime=$4
cap=$5
wall=$6
archive_sha=$7
host_label=$8
target_label=$9
package=cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_20260827
case "$host_label" in r6d|box01) ;; *) exit 126 ;; esac
case "$prime" in 65521|65519|65497|65479) ;; *) exit 127 ;; esac
case "$target_label" in
  i1_j0|i1_j1|i1_j2|i1_j3|i1_j4|i1_j5|i2_j0|i2_j1|i2_j2|i2_j3|i3_j0|i3_j1|i3_j2|i4_j0|i4_j1|i5_j0) ;;
  *) exit 128 ;;
esac
case "$tag" in max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_*_q"$prime"_"$target_label") ;; *) exit 129 ;; esac
mkdir -p "$job/run"
printf 'tag=%s\nhost_label=%s\nhost=%s\nstart_utc=%s\nselector_prime=%s\ntarget_label=%s\nsource_archive_sha256=%s\n' \
  "$tag" "$host_label" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$prime" "$target_label" "$archive_sha" \
  > "$job/launch_registration.txt"
cd "$root"
sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap"
python=/home/ubuntu/venvs/td6/bin/python
"$python" -c 'import flint; assert flint.__version__ == "0.9.0"'
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_compiler" timeout "$wall" \
  "$python" "$package/solve_graded_ladder_v38.py" "$job/compiled" \
  --target-label "$target_label" --selector-prime "$prime" --registered-lane "$tag"
compiler_result_sha=$(sha256sum "$job/compiled/result.json" | awk '{print $1}')
grep -Fx "RESULT_SHA256=$compiler_result_sha" "$job/run/${tag}_compiler.stdout" >/dev/null
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" timeout "$wall" \
  "$python" "$package/validate_graded_ladder_v38.py" --result "$job/compiled/result.json" \
  --compiler-stdout "$job/run/${tag}_compiler.stdout" --compiler-stderr "$job/run/${tag}_compiler.stderr" \
  --target-label "$target_label" --selector-prime "$prime" --registered-lane "$tag" \
  --output "$job/RESULT.json"
grep -Fx 'PASS-A1-GRADED-LADDER-V38' "$job/run/${tag}_validator.stdout" >/dev/null
grep -Fx "RESULT_SHA256=$(sha256sum "$job/RESULT.json" | awk '{print $1}')" \
  "$job/run/${tag}_validator.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256
)
