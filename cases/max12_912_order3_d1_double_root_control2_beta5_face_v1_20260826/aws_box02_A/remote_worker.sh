#!/usr/bin/env bash
set -u

run=$1
tag=$2
encoding=$3
memory_kib=$4
solve_timeout=$5
cd "$run" || exit 91
hostname > hostname.txt
date -u +%FT%TZ > worker_started_utc.txt
uname -a > uname.txt
nproc > nproc.txt
free -h > free.prelaunch.txt
/usr/bin/Singular --version > singular.version.txt 2>&1
if test "$(uname -s)" != Linux; then echo REFUSE_NON_LINUX > REFUSED; exit 92; fi
if test "$(cat /sys/class/dmi/id/sys_vendor 2>/dev/null)" != "Amazon EC2"; then echo REFUSE_NON_AWS_EC2 > REFUSED; exit 93; fi
case "$tag" in max12_912_order3_d1_double_root_control2_beta5_face_v1_20260826T*) ;; *) echo REFUSE_UNREGISTERED_TAG > REFUSED; exit 94 ;; esac
case "$encoding" in
  A) input=beta5_face_A_dp.sing; final=PASS_CONTROL2_BETA5_FACE_A ;;
  B) input=beta5_face_B_lpdp.sing; final=PASS_CONTROL2_BETA5_FACE_B ;;
  *) echo REFUSE_ENCODING > REFUSED; exit 94 ;;
esac
echo "pid=$$" > worker.metadata
echo "tag=$tag" >> worker.metadata
echo "encoding=$encoding" >> worker.metadata
echo "compiler_memory_kib=2097152" >> worker.metadata
echo "compiler_timeout=300" >> worker.metadata
echo "solver_memory_kib=$memory_kib" >> worker.metadata
echo "solver_timeout=$solve_timeout" >> worker.metadata
echo WAITING_COMPILE >> worker.metadata
while test ! -f GO_COMPILE; do sleep 1; done
if ! sha256sum -c SOURCE_CLOSURE.sha256 > source.check 2>&1; then echo SOURCE_HASH_FAILURE > COMPILE_FAILED; exit 95; fi
export JC2_AWS_TAG="$tag"
( ulimit -v 2097152; nice -n 10 timeout 300 python3 -u compile_beta5_face.py ) > compiler.stdout 2> compiler.stderr
compiler_rc=$?
echo "$compiler_rc" > compiler.rc
sha256sum beta5_face_A_dp.sing beta5_face_B_lpdp.sing > compiled.sha256 2>/dev/null || true
if test "$compiler_rc" -ne 0 || test -s compiler.stderr || test "$(grep -c '^PASS_CONTROL2_BETA5_FACE_COMPILER$' compiler.stdout 2>/dev/null)" -ne 1; then echo COMPILER_FAILURE > COMPILE_FAILED; exit 96; fi
touch COMPILE_DONE
echo WAITING_SOLVE >> worker.metadata
while test ! -f GO_SOLVE; do sleep 1; done
if ! sha256sum -c solve_source.sha256 > solve_source.check 2>&1; then echo SOLVE_HASH_FAILURE > SOLVE_FAILED; exit 97; fi
date -u +%FT%TZ > solve_started_utc.txt
(
  ulimit -v "$memory_kib"
  nice -n 10 timeout --signal=TERM --kill-after=300 "$solve_timeout" \
    /usr/bin/time -v -o singular.time /usr/bin/Singular -q "$input"
) > singular.stdout 2> singular.stderr
solver_rc=$?
echo "$solver_rc" > singular.rc
date -u +%FT%TZ > solve_finished_utc.txt
free -h > free.postsolve.txt
grep -En '(^// \*\*|^[[:space:]]*\?|^halt [0-9]+$|error occurred|wrong type|skipping text|outdated identifier)' singular.stdout > singular.stdout.diagnostics || true
if test "$solver_rc" -ne 0 || test -s singular.stderr || test -s singular.stdout.diagnostics || \
   test "$(grep -c '^PASS_WITNESS_FACE_MEMBERSHIP$' singular.stdout 2>/dev/null)" -ne 1 || \
   test "$(grep -Ec '^TORUS_FACE_IS_UNIT=[01]$' singular.stdout 2>/dev/null)" -ne 1 || \
   test "$(grep -c "^${final}$" singular.stdout 2>/dev/null)" -ne 1 || grep -q '^FAIL_' singular.stdout; then
  echo SOLVER_OR_DIAGNOSTIC_FAILURE > SOLVE_FAILED; exit 98
fi
sha256sum compiler.stdout compiler.stderr compiler.rc "$input" singular.stdout singular.stderr singular.stdout.diagnostics singular.time singular.rc > result.sha256
touch SOLVE_DONE
echo PASS_REMOTE_WORKER >> worker.metadata
