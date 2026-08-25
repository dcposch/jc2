#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${OUTPUT_JSON:?}"
: "${ANF_OUTPUT:?}"
case_dir="${JC2_ROOT}/cases/as_b8_max12_affine_kuranishi_aws_20260825"
parent="${JC2_ROOT}/cases/as_b8_max12_w3_gate_aws_20260825/replay_v2.py"
expected_compiler="a3f1b0356198f2acc9a967e2f99967f78ff74828318ef4ff12630cc60c594861"
expected_parent="691c89fc78dbbdb053449e0c26df326a5b459ab8de28b333cbd5329f48168a13"
test "$(sha256sum "${case_dir}/compile_affine_kuranishi.py" | cut -d' ' -f1)" = "${expected_compiler}"
test "$(sha256sum "${parent}" | cut -d' ' -f1)" = "${expected_parent}"
hostname > host.txt
uname -a > uname.txt
python3 --version > python-version.txt 2>&1
sha256sum "${case_dir}/PREREGISTRATION.md" \
  "${case_dir}/compile_affine_kuranishi.py" "${case_dir}/run_aws.sh" \
  "${parent}" > INPUT.sha256
date -u +%Y-%m-%dT%H:%M:%SZ > start.utc
set +e
/usr/bin/time -v timeout 7200 env \
  JC2_ROOT="${JC2_ROOT}" OUTPUT_JSON="${OUTPUT_JSON}" ANF_OUTPUT="${ANF_OUTPUT}" \
  python3 "${case_dir}/compile_affine_kuranishi.py" \
  > compiler.stdout 2> compiler.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > compiler.rc
date -u +%Y-%m-%dT%H:%M:%SZ > end.utc
sha256sum host.txt uname.txt python-version.txt INPUT.sha256 \
  start.utc end.utc compiler.rc compiler.stdout compiler.stderr \
  "${OUTPUT_JSON}" "${ANF_OUTPUT}" > OUTPUT.sha256 2>/dev/null || true
exit "${rc}"
