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

if test "$(uname -s)" != Linux; then
  echo REFUSE_NON_LINUX > REFUSED
  exit 92
fi
if test "$(cat /sys/class/dmi/id/sys_vendor 2>/dev/null)" != "Amazon EC2"; then
  echo REFUSE_NON_AWS_EC2 > REFUSED
  exit 93
fi
case "$tag" in
  max12_912_order3_d1_sat_return_type_probe_20260826T*_r6d) ;;
  *) echo REFUSE_UNREGISTERED_TAG > REFUSED; exit 94 ;;
esac

echo "pid=$$" > worker.metadata
echo "tag=$tag" >> worker.metadata
echo "memory_kib=1048576" >> worker.metadata
echo "timeout_seconds=120" >> worker.metadata
echo WAITING_GO >> worker.metadata
while test ! -f GO; do sleep 1; done

if ! sha256sum -c solve_source.sha256 > solve_source.check 2>&1; then
  echo SOURCE_HASH_FAILURE > SOLVE_FAILED
  exit 95
fi
date -u +%FT%TZ > solve_started_utc.txt
(
  ulimit -v 1048576
  nice -n 10 timeout --signal=TERM --kill-after=10 120 \
    /usr/bin/time -v -o singular.time /usr/bin/Singular -q sat_return_type_probe.sing
) > singular.stdout 2> singular.stderr
rc=$?
echo "$rc" > singular.rc
date -u +%FT%TZ > solve_finished_utc.txt
free -h > free.postsolve.txt
if test "$rc" -ne 0 || test -s singular.stderr || \
   test "$(grep -c '^PASS_SAT_RETURN_TYPE_PROBE$' singular.stdout 2>/dev/null)" -ne 1 || \
   grep -q '^FAIL_' singular.stdout; then
  echo SOLVER_VALIDATION_FAILURE > SOLVE_FAILED
  exit 96
fi
sha256sum sat_return_type_probe.sing singular.stdout singular.stderr \
  singular.time singular.rc > result.sha256
touch SOLVE_DONE
echo PASS_REMOTE_WORKER >> worker.metadata
