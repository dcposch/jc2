#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6
mkdir -p "$aws_job/run"
{ printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"; } > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_h18_q6_a6_g54_direct_unit_v1_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 cases/max12_812_order2_affine_faber_a_h18_q6_a6_g54_direct_unit_v1_20260826/compute_h18_q6_a6_g54_v1.py "$aws_job/output" --characteristic "$characteristic" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En 'Traceback|RuntimeError' "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in \
 'A_H18Q6A6_LOWER_ZERO=1' \
 'A_H18Q6A6_G54=-2*m^3*p^2' \
 'A_H18Q6A6_ENDPOINT=PASS_G54_DIRECT_UNIT' \
 'A_H18Q6A6_DONE=1' \
 'A_H18Q6A6_SCOPE=FIXED_H18_Q6_A6_NORMALIZED_GRAPH_ODD_FUNCTIONAL_G54_ONLY_NO_SOURCE_FIXED_LOCUS_TAYLOR_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_H18_Q6_A6_G54_DIRECT_UNIT_V1\n' >> "$aws_job/run/$tag.validation"
