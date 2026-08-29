#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6
mkdir -p "$aws_job/run"; cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/compute_sparse_dag_v4.py "$aws_job/output" --characteristic "$characteristic" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En 'Traceback|RuntimeError|MemoryError' "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_H16_SPARSE_DAG_ENDPOINT=PASS_COEFFICIENT_ONLY_GRADE48' 'A_H16_SPARSE_DAG_DONE=1' 'A_H16_SPARSE_DAG_SCOPE=FIXED_H16_Q6_A4_RAW_ROWS_1_3_7_GRADE48_SPARSE_FUNCTIONAL_ONLY_NO_PREDECESSOR_REDUCTION_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
if [[ "$(grep -Fc 'A_H16_SPARSE_DAG_G48_SHA256=' "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_G48_HASH\n' >> "$aws_job/run/$tag.validation"; exit 93; fi
for artifact in result.json abstract_functional_support.json grade48_sparse_polynomial.json; do
 if [[ ! -s "$aws_job/output/$artifact" ]]; then printf 'validator=FAIL_MISSING_ARTIFACT:%s\n' "$artifact" >> "$aws_job/run/$tag.validation"; exit 94; fi
done
printf 'validator=PASS_A_H16_Q6_A4_G48_SPARSE_DAG_V4\n' >> "$aws_job/run/$tag.validation"

