#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 7 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
cap=$4
wall=$5
archive_sha=$6
host_label=$7
package=cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_20260827
case "$host_label" in r6d|box01) ;; *) exit 126 ;; esac
case "$tag" in max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_*_control_census_"$host_label") ;; *) exit 127 ;; esac
mkdir -p "$job/run"
printf 'tag=%s\nhost_label=%s\nhost=%s\nstart_utc=%s\nsource_archive_sha256=%s\n' \
  "$tag" "$host_label" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$archive_sha" > "$job/launch_registration.txt"
cd "$root"
sha256sum -c "$package/FREEZE_CONTROL_CENSUS.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap"
python=/home/ubuntu/venvs/td6/bin/python
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_compiler" timeout "$wall" \
  "$python" "$package/census_shape_controls_v38.py" "$job/compiled" --registered-lane "$tag"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" timeout "$wall" \
  "$python" "$package/validate_shape_controls_v38.py" --result "$job/compiled/census.json" \
  --compiler-stdout "$job/run/${tag}_compiler.stdout" --compiler-stderr "$job/run/${tag}_compiler.stderr" \
  --registered-lane "$tag" --output "$job/RESULT.json"
grep -Fx 'PASS-A1-GRADED-LADDER-V38-CONTROL-CENSUS' "$job/run/${tag}_validator.stdout" >/dev/null
grep -Fx "RESULT_SHA256=$(sha256sum "$job/RESULT.json" | awk '{print $1}')" \
  "$job/run/${tag}_validator.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256
)
