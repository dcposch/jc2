#!/usr/bin/env bash
set -u

job=$1
tag=$2
encoding=$3
memory_kib=$4
solve_timeout=$5
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
  max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826T*) ;;
  *) echo REFUSE_UNREGISTERED_TAG > REFUSED; exit 94 ;;
esac
case "$encoding" in
  LPDP) input=corrected_A_lpdp.sing; marker=PASS_CONTROL2_REES_CORRECTED_A_LPDP ;;
  DP) input=corrected_A_dp.sing; marker=PASS_CONTROL2_REES_CORRECTED_A_DP ;;
  *) echo REFUSE_BAD_ENCODING > REFUSED; exit 95 ;;
esac

echo "pid=$$" > worker.metadata
echo "tag=$tag" >> worker.metadata
echo "encoding=$encoding" >> worker.metadata
echo "compiler_memory_kib=4194304" >> worker.metadata
echo "compiler_timeout=600" >> worker.metadata
echo "solver_memory_kib=$memory_kib" >> worker.metadata
echo "solver_timeout=$solve_timeout" >> worker.metadata
echo WAITING_COMPILE >> worker.metadata
while test ! -f GO_COMPILE; do sleep 1; done

if ! sha256sum -c source.sha256 > source.check 2>&1; then
  echo SOURCE_HASH_FAILURE > COMPILE_FAILED; exit 96
fi
export JC2_AWS_TAG="$tag"
(
  ulimit -v 4194304
  nice -n 10 timeout 600 python3 -u compile_corrected_A.py
) > compiler.stdout 2> compiler.stderr
compiler_rc=$?
echo "$compiler_rc" > compiler.rc
sha256sum corrected_A_*.sing > compiled.sha256 2>/dev/null || true
if test "$compiler_rc" -ne 0 || test -s compiler.stderr || \
   test "$(grep -c '^PASS_CONTROL2_REES_CORRECTED_A_COMPILER$' compiler.stdout 2>/dev/null)" -ne 1; then
  echo COMPILER_FAILURE > COMPILE_FAILED; exit 97
fi
touch COMPILE_DONE
echo WAITING_SOLVE >> worker.metadata
while test ! -f GO_SOLVE; do sleep 1; done
if ! sha256sum -c solve_source.sha256 > solve_source.check 2>&1; then
  echo SOLVE_HASH_FAILURE > SOLVE_FAILED; exit 98
fi
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
if test "$solver_rc" -ne 0 || test -s singular.stderr || \
   test "$(grep -c "^${marker}$" singular.stdout 2>/dev/null)" -ne 1 || \
   test "$(grep -c '^PASS_A_B_SPECIAL_FIBRE_MUTUAL_REDUCTION$' singular.stdout 2>/dev/null)" -ne 1 || \
   test "$(grep -c '^LA20_IN_FULL_SPECIAL_FIBRE=1$' singular.stdout 2>/dev/null)" -ne 1 || \
   test "$(grep -c '^TORUS_SPECIAL_FIBRE_IS_UNIT=1$' singular.stdout 2>/dev/null)" -ne 1 || \
   grep -q '^FAIL_' singular.stdout; then
  echo SOLVER_FAILURE > SOLVE_FAILED; exit 99
fi
sha256sum compiler.stdout compiler.stderr compiler.rc corrected_A_*.sing \
  singular.stdout singular.stderr singular.time singular.rc > result.sha256
touch SOLVE_DONE
echo PASS_REMOTE_WORKER >> worker.metadata
