#!/usr/bin/env bash
set -u

job=$1
tag=$2

cd "$job" || exit 91
hostname > hostname.txt
date -u +%FT%TZ > worker_started_utc.txt
uname -a > uname.txt
nproc > nproc.txt
free -h > free.prelaunch.txt
/usr/bin/Singular --version > singular.version.txt 2>&1

if test "$(uname -s)" != Linux; then echo REFUSE_NON_LINUX > REFUSED; exit 92; fi
if test "$(cat /sys/class/dmi/id/sys_vendor 2>/dev/null)" != "Amazon EC2"; then
  echo REFUSE_NON_AWS_EC2 > REFUSED; exit 93
fi
case "$tag" in
  max12_912_order3_d1_double_root_control2_rees_certificate_*) ;;
  *) echo REFUSE_UNREGISTERED_TAG > REFUSED; exit 94 ;;
esac

echo "pid=$$" > worker.metadata
echo "tag=$tag" >> worker.metadata
echo "memory_kib=67108864" >> worker.metadata
echo "timeout=1800" >> worker.metadata
echo WAITING_GO >> worker.metadata
while test ! -f GO; do sleep 1; done

if ! sha256sum -c source.sha256 > source.check 2>&1; then
  echo SOURCE_HASH_FAILURE > FAILED; exit 95
fi
export JC2_AWS_TAG="$tag"
(
  ulimit -v 16777216
  nice -n 10 timeout 600 python3 -u \
    repo/cases/max12_912_order3_d1_double_root_control2_rees_certificate_20260826/compile_certificate.py
) > compiler.stdout 2> compiler.stderr
compiler_rc=$?
echo "$compiler_rc" > compiler.rc
sha256sum repo/cases/max12_912_order3_d1_double_root_control2_rees_certificate_20260826/compiled_certificate.sing > input.sha256 2>/dev/null || true
if test "$compiler_rc" -ne 0 || test -s compiler.stderr || \
   test "$(grep -c '^PASS_CONTROL2_REES_CERTIFICATE_COMPILER$' compiler.stdout 2>/dev/null)" -ne 1; then
  echo COMPILER_VALIDATION_FAILURE > FAILED; exit 96
fi
date -u +%FT%TZ > solve_started_utc.txt
(
  ulimit -v 67108864
  nice -n 10 timeout --signal=TERM --kill-after=60 1800 \
    /usr/bin/time -v -o singular.time /usr/bin/Singular -q \
    repo/cases/max12_912_order3_d1_double_root_control2_rees_certificate_20260826/compiled_certificate.sing
) > singular.stdout 2> singular.stderr
singular_rc=$?
echo "$singular_rc" > singular.rc
date -u +%FT%TZ > solve_finished_utc.txt
if test "$singular_rc" -ne 0 || test -s singular.stderr || \
   test "$(grep -c '^PASS_CONTROL2_REES_MONOMIAL_CERTIFICATE$' singular.stdout 2>/dev/null)" -ne 1 || \
   test "$(grep -c '^PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_B$' singular.stdout 2>/dev/null)" -ne 1 || \
   grep -q 'FAIL_' singular.stdout; then
  echo SOLVER_VALIDATION_FAILURE > FAILED; exit 97
fi
sha256sum compiler.stdout compiler.stderr compiler.rc input.sha256 singular.stdout \
  singular.stderr singular.time singular.rc > result.sha256
touch DONE
echo PASS_REMOTE_WORKER >> worker.metadata

