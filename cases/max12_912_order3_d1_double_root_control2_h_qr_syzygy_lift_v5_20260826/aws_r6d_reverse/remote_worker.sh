#!/usr/bin/env bash
set -u
run=$1
tag=$2
order=$3
cd "$run" || exit 91
hostname > hostname.txt
date -u +%FT%TZ > worker_started_utc.txt
uname -a > uname.txt
nproc > nproc.txt
free -h > free.prelaunch.txt
if test "$(uname -s)" != Linux; then echo REFUSE_NON_LINUX > REFUSED; exit 92; fi
if test "$(cat /sys/class/dmi/id/sys_vendor 2>/dev/null)" != "Amazon EC2"; then echo REFUSE_NON_AWS_EC2 > REFUSED; exit 93; fi
case "$tag" in max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826T*) ;; *) echo REFUSE_UNREGISTERED_TAG > REFUSED; exit 94 ;; esac
case "$order" in forward|reverse) ;; *) echo REFUSE_ORDER > REFUSED; exit 94 ;; esac
{
  echo "pid=$$"; echo "tag=$tag"; echo "order=$order"
  echo "memory_kib=4194304"; echo "timeout=900"; echo WAITING_GO
} > worker.metadata
while test ! -f GO; do sleep 1; done
if ! sha256sum -c SOURCE_CLOSURE.sha256 > source.check 2>&1; then echo SOURCE_HASH_FAILURE > FAILED; exit 95; fi
export JC2_AWS_TAG="$tag"
( ulimit -v 4194304; nice -n 10 timeout 900 /usr/bin/time -v -o compiler.time \
  python3 -u compile_h_qr_syzygy_lift_v5.py --order "$order" --output h_qr_lift.json \
) > compiler.stdout 2> compiler.stderr
rc=$?
echo "$rc" > compiler.rc
date -u +%FT%TZ > worker_finished_utc.txt
free -h > free.postsolve.txt
if test "$rc" -ne 0 || test -s compiler.stderr || \
   test "$(grep -Ec '^PASS_H_QR_SYZYGY_LIFT_V5_(SOLVABLE|COKERNEL)$' compiler.stdout 2>/dev/null)" -ne 1; then
  echo COMPILER_OR_DIAGNOSTIC_FAILURE > FAILED; exit 96
fi
sha256sum h_qr_lift.json compiler.stdout compiler.stderr compiler.rc compiler.time > result.sha256
touch DONE
echo PASS_REMOTE_WORKER >> worker.metadata
