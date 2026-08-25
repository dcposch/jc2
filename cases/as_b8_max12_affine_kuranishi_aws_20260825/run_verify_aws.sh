#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}" "${VERIFY_INPUT:?}" "${EXPECTED_INPUT_SHA:?}" "${EXPECTED_PASS:?}"
test "$(sha256sum "${VERIFY_INPUT}" | cut -d' ' -f1)" = "${EXPECTED_INPUT_SHA}"
hostname > verify.host.txt
uname -a > verify.uname.txt
Singular --version > verify.singular-version.txt 2>&1
sha256sum "${VERIFY_INPUT}" > verify.INPUT.sha256
date -u +%Y-%m-%dT%H:%M:%SZ > verify.start.utc
set +e
/usr/bin/time -v timeout 1800 Singular -q "${VERIFY_INPUT}" \
  > verify.stdout 2> verify.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > verify.rc
date -u +%Y-%m-%dT%H:%M:%SZ > verify.end.utc
test "${rc}" = 0
if grep -q '^FAIL' verify.stdout; then
  echo "fail-closed verifier emitted FAIL" >&2
  exit 97
fi
grep -Fx "${EXPECTED_PASS}" verify.stdout
grep -Fx "MUTUAL_REDUCTION_ZERO true" verify.stdout
grep -Fx "IDEAL_EQUAL (s22,s26)" verify.stdout
grep -Fx "GEOMETRIC_DIMENSION 27" verify.stdout
grep -Fx "F3_POINT_COUNT 7625597484987" verify.stdout
sha256sum verify.host.txt verify.uname.txt verify.singular-version.txt \
  verify.INPUT.sha256 verify.start.utc verify.end.utc verify.rc \
  verify.stdout verify.stderr > verify.OUTPUT.sha256
